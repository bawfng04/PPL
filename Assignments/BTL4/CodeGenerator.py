from Utils import *
# from StaticCheck import *
# from StaticError import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *
# Import necessary exceptions if needed, e.g., from CodeGenError.py
# from CodeGenError import IllegalRuntimeException

class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        #
        self.className = "MiniGoClass" # Tên class tổng của chương trình minigo
        self.astTree = None
        self.path = None
        self.emit = None
        self.function = None
        self.list_function = []
        self.arrayCell = None # Dùng để lưu kiểu của mảng khi duyệt vào 1 ArrayCell
        self.arrayCellType = None # Store the element type when visiting ArrayCell LHS
        self.struct: StructType = None  # Lưu struct hiện tại đang được duyệt
        self.list_type = {}  # Initialize list_type as an empty dictionary

    def init(self):
        mem = [
            Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("getInt", MType([], IntType()), CName("io", True)),
            Symbol("getFloat", MType([], FloatType()), CName("io", True)),
            Symbol("getBool", MType([], BoolType()), CName("io", True)),
            Symbol("getString", MType([], StringType()), CName("io", True)),
        ]
        return mem

    def gen(self, ast, dir_):
        # Nơi được gọi để khởi tạo classCodeGen và bắt đầu sinh mã !!!
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl) # Start visiting the Program node

    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        # sinh ra mã => .method public <init>()V
        frame.enterScope(True)  # Mỗi hàm có 1 frame riêng, và mỗi frame có 1 scope riêng, nên dùng enterScope để vào scope của frame này

        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        # sinh ra mã => .var 0 is this LMiniGoClass; from Label0 to Label1

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # sinh ra mã => Label0: (nơi body method bắt đầu)

        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame)) 
        # sinh ra mã => aload_0 (đưa biến this vào stack)

        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        # sinh ra mã => invokespecial java/lang/Object/<init>()V (gọi hàm khởi tạo của class cha là Object)  
     
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        # sinh ra mã => Label1: (nơi body method kết thúc)


        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        # sinh ra mã => return (trả về từ hàm khởi tạo này)

        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        # sinh ra mã limit stack 1, limit locals 1, end method (kết thúc định nghĩa phương thức <init>)

        frame.exitScope() 

    def emitObjectCInit(self, ast: Program, env):


        frame = Frame("<cinit>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame)) 
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env['frame'] = frame

        self.visit(Block([
            Assign(Id(item.varName), item.varInit)  # Create Assign nodes for initialization
            for item in ast.decl if isinstance(item, (VarDecl, ConstDecl)) and item.varInit is not None
        ]), env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()

    def visitProgram(self, ast: Program, c):
        # Biến c ban đầu là dãy Symbol "mem" ở hàm init() ở trên, chứa các hàm builtin của minigo.

        self.list_function = c + [Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)), item.retType), CName(self.className)) for item in ast.decl if isinstance(item, FuncDecl)]
        # Đoạn này nạp mấy hàm vào list_function, biến tụi nó thành Symbol để quản lí
        
        env = {}
        env['env'] = [c]


        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        # sinh ra mã => .source MiniGoClass.java
        #               .class public MiniGoClass
        #               .super java.lang.Object


        # Đoạn sau sinh mã cho khai báo biến và khai báo báo hàm:
        ## 1. Khai báo biến (duyệt trước vì hàm có thể dùng biến toàn cục, cập nhật biến/hằng toàn cục vào env)
        env = reduce(lambda a, x: self.visit(x, a) if isinstance(x, VarDecl) or  isinstance(x, ConstDecl) else a, ast.decl, env)

        ## 2. Khai báo hàm (gọi hàm visitFuncDecl cho từng hàm trong danh sách hàm trong ast.decl)
        reduce(lambda a, x: self.visit(x, a) if isinstance(x, FuncDecl) else a, ast.decl, env)



        # Gọi mấy hàm đã định nghĩa ở trên
        self.emitObjectInit()
        self.emitObjectCInit(ast, env)


        self.emit.printout(self.emit.emitEPILOG())

        for item in self.list_type.values():
            self.struct = item
            self.emit = Emitter(self.path + "/" + item.name + ".j")
            self.visit(item, {
                'env': env['env']
            })

        return env

    def visitFuncDecl(self, ast: FuncCall, o: dict) -> dict:

        #Lưu function đang duyệt vào biến self.function để dùng sau
        self.function = ast

        frame = Frame(ast.name, ast.retType)

        #Với hàm main thì có params và return cố định như bên dưới, này được định nghĩa trong spec:
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
            #ast.body = Block([] + ast.body.member)
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        

        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, frame))
        # sinh ra mã => .method public static main([Ljava/lang/String;)V đối với hàm main

        # Tiếp theo nhảy vào body hàm:
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        env['env'] = [[]] + env['env']
        # Lưu ý: mình đang dùng field env của env để lưu reference.

        # Sinh mã VAR tùy vào hàm có phải main hay không, đồng thời cũng cập nhật biến env['env'] với các tham số của hàm:
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)

        #Gọi hàm visitBlock, truyền env đã được cập nhật scope params.
        self.visit(ast.body,env)


        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))


        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        #Nếu trả về kiểu khác void thì hàm visitBlock đã sinh mã cho return rồi.

        self.emit.printout(self.emit.emitENDMETHOD(frame))


        frame.exitScope()
        # Kết thúc thân hàm


        return o

    def visitParamDecl(self, ast: ParamDecl, o: dict) -> dict:
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(self.emit.emitVAR(index, ast.parName, ast.parType, frame.getStartLabel() ,frame.getEndLabel(), frame))     
        return o

    def visitVarDecl(self, ast: VarDecl, o: dict) -> dict:
        def create_init(varType: Type, o: dict):
            if isinstance(varType, IntType):
                return IntLiteral(0)
            elif isinstance(varType, FloatType):
                return FloatLiteral(0.0)
            elif isinstance(varType, StringType):
                return StringLiteral("\"\"")
            elif isinstance(varType, BoolType):
                return BooleanLiteral(False)
            elif isinstance(varType, ArrayType):
                # Hàm đệ quy để tạo mảng giá trị mặc định dựa trên số chiều và kiểu phần tử
                def create_default_array(dimens, eleType):
                    if not dimens:  # Base case: không còn chiều nào
                        return create_init(eleType, o)  # Gọi lại hàm `create_init` để lấy giá trị mặc định cho phần tử
                    return [create_default_array(dimens[1:], eleType) for _ in range(dimens[0].value)]

                # Tạo danh sách giá trị mặc định cho mảng
                default_values = create_default_array(varType.dimens, varType.eleType)
                return ArrayLiteral(default_values, varType.eleType, varType.dimens)
            elif isinstance(varType, StructType):
                # Khởi tạo StructLiteral với các giá trị mặc định cho từng field
                struct_def = o['structs'].get(varType.name)  # Lấy định nghĩa của struct từ danh sách các struct
                if not struct_def:
                    raise TypeError(f"Undefined struct type: {varType.name}")

                # Tạo danh sách các giá trị mặc định cho từng field trong struct
                default_fields = [
                    (field_name, create_init(field_type, o))
                    for field_name, field_type in struct_def.elements
                ]
                return StructLiteral(varType.name, default_fields)


        varInit = ast.varInit # Giá trị khởi tạo của biến
        varType = ast.varType # Kiểu của biến
        
        #Nếu không có giá trị khởi tạo thì tự động gán cho nó 0, 0.0, false, "",..tùy vào kiểu biến:
        # int -> 0, float -> 0.0, bool -> false, string -> "", array -> mảng chứa các giá trị "zero" tùy thuộc vào kiểu phần tử.
        if not varInit:
            varInit = create_init(varType, o)
            ast.varInit = varInit
        env = o.copy()
        env['frame'] = Frame("<template_VT>", VoidType()) 

        # Như đã nói trong lưu ý ở trên thì trường hợp dimension là Id hay biểu thức sẽ đc xử lí ở visitArrayLiteral và là dòng dưới đây
        rhsCode, rhsType = self.visit(varInit, env)
        

        #Trường hợp khai báo với giá trị nhưng không có kiẻu thì mình sẽ tự động gán kiểu cho nó dựa vào giá trị khởi tạo.
        if not varType:
            varType = rhsType

        if 'frame' not in o: # TH global var => biến khai báo toàn cục thì mình
            o['env'][0].append(Symbol(ast.varName, varType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, varType, True, False, None))
        else:
            frame = o['frame']

            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, varType, Index(index))) # mỗi trường sẽ có 1 index riêng


            self.emit.printout(self.emit.emitVAR(index, ast.varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
            rhsCode, rhsType = self.visit(varInit, o)
            if type(varType) is FloatType and type(rhsType) is IntType:
                rhsCode += self.emit.emitI2F(o["frame"])  # Convert int to float
                  
            self.emit.printout(rhsCode)
            
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, varType, index,  frame)) # sinh mã gán giá trị vào biến                   
        return o

    def visitFuncCall(self, ast: FuncCall, o: dict) -> dict:
        # Find the function symbol in the list of functions
        sym = next(filter(lambda x: x.name == ast.funName, self.list_function), None)

        if o.get('stmt'):  # If the function call is a statement
            o["stmt"] = False  # Reset the statement flag

            # Generate code for the arguments
            argsCode = "".join([self.visit(arg, o)[0] for arg in ast.args])
            # Emit the function call
            self.emit.printout(argsCode)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame']))

            return o  # Return `o` since statements do not return a value

        # If the function call is an expression
        output = "".join([self.visit(arg, o)[0] for arg in ast.args])  # Generate code for the arguments
        output += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame'])  # Emit the function call

        # Return the generated code and the return type of the function
        return output, sym.mtype.rettype

    def visitBlock(self, ast: Block, o: dict) -> dict:
        # Copy the environment and create a new scope
        env = o.copy()
        env['env'] = [[]] + env['env']  # Add a new scope to the environment
        frame = env['frame']
        
        frame.enterScope(False)  # Enter a new scope for the frame

        # Emit the start label for the block
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Visit each member of the block
        for item in ast.member:
            if isinstance(item, FuncCall):  # Check if the item is a function call
                env["stmt"] = True  # Mark it as a statement
            elif isinstance(item, MethCall):  # Nếu là MethCall
                env["stmt"] = True
            env = self.visit(item, env)  # Visit the item

        # Emit the end label for the block
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        # Exit the scope
        frame.exitScope()
        return o
    
    def visitId(self, ast: Id, o: dict) -> dict:
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]), None)

        # Nếu không tìm thấy trong env, giả định là `this`
        if sym is None:
            if o.get('isLeft'):
                return self.emit.emitWRITEVAR(ast.name, self.struct, 0, o['frame']), self.struct
            return self.emit.emitREADVAR(ast.name, self.struct, 0, o['frame']), self.struct

        # Nếu tìm thấy trong env
        if o.get('isLeft'):
            if isinstance(sym.value, Index):
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
            return self.emit.emitPUTSTATIC(f"{self.className}/{sym.name}", sym.mtype, o['frame']), sym.mtype

        if isinstance(sym.value, Index):
            return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
        return self.emit.emitGETSTATIC(f"{self.className}/{sym.name}", sym.mtype, o['frame']), sym.mtype

    def visitAssign(self, ast: Assign, o: dict) -> dict:
        # Xem thử là biến này đã được khai báo chưa, trong minigo nếu phép gán mà biến chưa được khai báo thì sẽ tự động khai báo nó luôn.
        if type(ast.lhs) is Id and not next(filter(lambda x: x.name == ast.lhs.name, [j for i in o['env'] for j in i]), None):
            # Nếu biến chưa được khai báo, tạo và visit một VarDecl mới với kiểu None
            varDecl = VarDecl(ast.lhs.name, None, None)
            self.visit(varDecl, o)
            return o

        # Duyệt vế phải của phép gán để lấy mã và kiểu
        rhsCode, rhsType = self.visit(ast.rhs, o)

        # Trước khi duyệt vế trái (có thể chạy vào hàm visitId ở trên), bật biến cờ isLeft
        o['isLeft'] = True
        lhsCode, lhsType = self.visit(ast.lhs, o)
        o['isLeft'] = False

        # Nếu kiểu của vế trái là Float và vế phải là Int, thêm mã chuyển đổi kiểu int -> float
        if type(lhsType) is FloatType and type(rhsType) is IntType:
            rhsCode += self.emit.emitI2F(o['frame'])

        # Tăng kích thước stack lên 1 đơn vị
        o['frame'].push()

        # Nếu vế trái là một ArrayCell
        if type(ast.lhs) is ArrayCell:
            self.emit.printout(lhsCode)  # Mã truy cập mảng
            self.emit.printout(rhsCode)  # Mã giá trị cần gán
            self.emit.printout(self.emit.emitASTORE(self.arrayCellType, o['frame']))  # Lưu giá trị vào mảng
        else:
            # Nếu vế trái là một Id hoặc thuộc tính
            self.emit.printout(rhsCode)  # Mã giá trị cần gán
            self.emit.printout(lhsCode)  # Mã truy cập biến hoặc thuộc tính

        return o

    def visitReturn(self, ast: Return, o: dict) -> dict:
        frame = o['frame']
        retType = self.function.retType  # Get the return type of the current function

        # If the return statement has an expression
        if ast.expr:
            exprCode, exprType = self.visit(ast.expr, o)  # Visit the expression to generate code and get its type
            self.emit.printout(exprCode)  # Emit the code to push the expression result onto the stack

            # If the return type is Float but the expression type is Int, perform type conversion
            if isinstance(retType, FloatType) and isinstance(exprType, IntType):
                self.emit.printout(self.emit.emitI2F(frame))  # Convert int to float

        # Emit the return instruction with the correct type
        self.emit.printout(self.emit.emitRETURN(retType, frame))
        return o

    ##  END decl ------------------------------

    ##  basic expression ------------------------------
    def visitBinaryOp(self, ast: BinaryOp, o: dict) -> tuple[str, Type]:
        op = ast.op
        frame = o['frame']
        codeLeft, typeLeft = self.visit(ast.left, o)
        codeRight, typeRight = self.visit(ast.right, o)

        # Arithmetic Ops (+, -, *, /)
        if op in ['+', '-', '*', '/'] and isinstance(typeLeft, (IntType, FloatType)) and isinstance(typeRight, (IntType, FloatType)):
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                if type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            # Emit appropriate instruction
            if op in ['+', '-']:
                return codeLeft + codeRight + self.emit.emitADDOP(op, typeReturn, frame), typeReturn
            else: # '*', '/'
                return codeLeft + codeRight + self.emit.emitMULOP(op, typeReturn, frame), typeReturn

        # Integer Modulo (%)
        if op == '%' and type(typeLeft) is IntType and type(typeRight) is IntType:
            return codeLeft + codeRight + self.emit.emitMOD(frame), IntType()

        # Relational Ops (==, !=, <, >, >=, <=) for Numbers
        if op in ['==', '!=', '<', '>', '>=', '<='] and isinstance(typeLeft, (IntType, FloatType)) and isinstance(typeRight, (IntType, FloatType)):
            typeCmp = FloatType() # Default to float comparison if mixing
            if type(typeLeft) is IntType and type(typeRight) is IntType:
                typeCmp = IntType()
            elif type(typeLeft) is IntType: # Right is Float
                codeLeft += self.emit.emitI2F(frame)
            elif type(typeRight) is IntType: # Left is Float
                codeRight += self.emit.emitI2F(frame)
            # Else: Both are Float
            return codeLeft + codeRight + self.emit.emitREOP(op, typeCmp, frame), BoolType()

        # Boolean Ops (&&, ||)
        if op == '&&':
            return codeLeft + codeRight + self.emit.emitANDOP(frame), BoolType()
        if op == '||':
            return codeLeft + codeRight + self.emit.emitOROP(frame), BoolType()

        # String Concatenation (+)
        if op == '+' and type(typeLeft) is StringType and type(typeRight) is StringType:
            # Use java.lang.String.concat(String)
            return codeLeft + codeRight + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), frame), StringType()

        # String Comparison (==, !=, <, >, >=, <=)
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) is StringType and type(typeRight) is StringType:
            # Use java.lang.String.compareTo(String) -> int
            code = codeLeft + codeRight + self.emit.emitINVOKEVIRTUAL("java/lang/String/compareTo", MType([StringType()], IntType()), frame)
            # Compare result with 0
            code += self.emit.emitPUSHICONST(0, frame)
            # Need to swap operands for REOP if comparing result with 0
            # e.g., a > b -> a.compareTo(b) > 0 -> REOP '>' checks stack: val1 > val2
            # Stack: result, 0. We need REOP(op, IntType)
            code += self.emit.emitREOP(op, IntType(), frame)
            return code, BoolType()

        # Default case if no operation matches (should not happen with valid AST)
        return "", VoidType()

    def visitUnaryOp(self, ast: UnaryOp, o: dict) -> tuple[str, Type]:
        frame = o['frame']
        code, type_operand = self.visit(ast.body, o)

        if ast.op == '!':
            return code + self.emit.emitNOT(BoolType(), frame), BoolType()
        elif ast.op == '-':
            return code + self.emit.emitNEGOP(type_operand, frame), type_operand
        # Default case
        return "", VoidType()

    def visitIntLiteral(self, ast: IntLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()
    
    def visitFloatLiteral(self, ast: FloatLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHICONST(ast.value, o['frame']), BoolType()
    
    def visitStringLiteral(self, ast: StringLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHCONST(ast.value, StringType(), o['frame']), StringType()
    
    ## END basic expression ------------------------------

    ## array ------------------------------
    def visitArrayCell(self, ast: ArrayCell, o: dict) -> tuple[str, Type]:
        newO = o.copy()
        newO['isLeft'] = False

        # Visit the array expression (the part before the indices)
        codeGen, arrType = self.visit(ast.arr, newO)

        # Visit each index and generate code
        for idx, item in enumerate(ast.idx):
            codeGen += self.visit(item, newO)[0]
            if idx != len(ast.idx) - 1:
                codeGen += self.emit.emitALOAD(arrType, o['frame'])

        retType = None
        if len(arrType.dimens) == len(ast.idx):  # Fully indexed
            retType = arrType.eleType
            if not o.get('isLeft'):  # If on the right-hand side
                codeGen += self.emit.emitALOAD(retType, o['frame'])  # Load the array element
            else:  # If on the left-hand side
                self.arrayCell = ast  # Store the array cell for later use
                self.arrayCellType = retType  # Store the element type
        else:  # Partially indexed
            retType = ArrayType(arrType.dimens[len(ast.idx):], arrType.eleType)
            if not o.get('isLeft'):  # If on the right-hand side
                codeGen += self.emit.emitALOAD(retType, o['frame'])  # Load the partially indexed array
            else:  # If on the left-hand side
                self.arrayCell = ast  # Store the array cell for later use
                self.arrayCellType = retType  # Store the partially indexed array type

        return codeGen, retType

    def visitArrayLiteral(self, ast: ArrayLiteral, o: dict) -> tuple[str, Type]:
        # Phần ArrayLiteral.value là 1 nested list nên mình sẽ dùng đệ quy để duyệt nó.
        def nested2recursive(dat: Union[Literal, list['NestedList']], o: dict) -> tuple[str, Type]:
            # dat có thể là 1 Literal hoặc là 1 list chứa các Literal khác, nên mình sẽ kiểm tra xem dat có phải là list hay không.

            # Nếu là Literal thôi thì chỉ cần visit tới là xong, không cần đệ quy nữa
            if not isinstance(dat, list):
                if dat is None:  # Handle None values
                    raise ValueError("ArrayLiteral contains a None value")
                return self.visit(dat, o)

            # Nếu dat là 1 list thì đoạn code dưới sẽ giải quyết
            # Chuẩn bị ngữ cảnh
            frame = o['frame']  # lấy frame từ o
            codeGen = self.emit.emitPUSHCONST(len(dat), IntType(), frame)  # Sinh mã đẩy số lượng phần tử của mảng vào stack

            # Trường hợp danh sách không lồng nhau (vì phần tử đầu tiên không phải là list)
            if not isinstance(dat[0], list):
                if dat[0] is None:  # Handle None values
                    raise ValueError("ArrayLiteral contains a None value")
                _, type_element_array = self.visit(dat[0], o)  # Gọi hàm visit cho phần tử đầu tiên để lấy kiểu của nó
                if isinstance(type_element_array, IntType):
                    codeGen += self.emit.emitNEWARRAY(type_element_array, frame)  # Tạo mảng với kiểu phần tử là type_element_array
                else:
                    codeGen += self.emit.emitANEWARRAY(type_element_array, frame)  # Tạo mảng với kiểu phần tử là type_element_array

                # Lặp qua từng phần tử trong danh sách:
                for idx, item in enumerate(dat):
                    if item is None:  # Handle None values
                        raise ValueError("ArrayLiteral contains a None value")
                    codeGen += self.emit.emitDUP(frame)  # Nhân đôi tham chiếu mảng trên stack
                    codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame)  # Đẩy chỉ số của phần tử lên stack
                    codeGen += self.visit(item, o)[0]  # Gọi self.visit(item, o) để xử lý giá trị phần tử
                    codeGen += self.emit.emitASTORE(type_element_array, frame)  # Lưu giá trị vào mảng
                return codeGen, ArrayType([IntLiteral(len(dat))], type_element_array)

            # Trường hợp danh sách lồng nhau:
            # Gọi đệ quy nested2recursive(dat[0], o) để xử lý danh sách con
            if dat[0] is None:  # Handle None values
                raise ValueError("ArrayLiteral contains a None value")
            _, type_element_array = nested2recursive(dat[0], o)
            
            # Extract the element type if type_element_array is an ArrayType
            #element_type = type_element_array.eleType if isinstance(type_element_array, ArrayType) else type_element_array
            
            if isinstance(type_element_array, IntType):
                codeGen += self.emit.emitNEWARRAY(type_element_array, frame)  # Tạo mảng với kiểu phần tử là kiểu của danh sách con
            else:
                codeGen += self.emit.emitANEWARRAY(type_element_array, frame)  # Tạo mảng với kiểu phần tử là kiểu của danh sách con

            # Lặp qua từng phần tử trong danh sách:
            for idx, item in enumerate(dat):
                if item is None:  # Handle None values
                    raise ValueError("ArrayLiteral contains a None value")
                codeGen += self.emit.emitDUP(frame)  # Nhân đôi tham chiếu mảng trên stack
                codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame)  # Đẩy chỉ số của phần tử lên stack
                codeGen += nested2recursive(item, o)[0]  # Gọi đệ quy nested2recursive(item, o) để xử lý danh sách con
                codeGen += self.emit.emitASTORE(type_element_array, frame)  # Lưu giá trị vào mảng
            return codeGen, ArrayType([IntLiteral(len(dat))], type_element_array)

        if (type(ast.value) is ArrayType):
            return self.visit(ast.value, o)
        
        # Gọi hàm đệ quy trong đó tham số truyền vào là ast.value, o
        return nested2recursive(ast.value, o)

    def visitConstDecl(self, ast: ConstDecl, o: dict) -> dict:
        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)

    def visitArrayType(self, ast: ArrayType, o: dict) -> tuple[str, Type]:
        codeGen = ""

        # Lặp qua dimens để thêm code vào codeGen
        dimensCode = []
        for dim in ast.dimens:
            dimCode, _ = self.visit(dim, o)  # Visit each dimension to generate code
            dimensCode.append(dimCode)

        # Kết hợp mã của các dimension
        codeGen += "".join(dimensCode)

        # Dùng emitMULTIANEWARRAY để tạo mảng mới
        codeGen += self.emit.emitMULTIANEWARRAY(ast, o['frame'])

        return codeGen, ast

    # Helper lookup function (if not already in Utils)
    def lookup(self, name, lst, func):
        for x in lst:
            # Check if x is a list/scope itself
            if isinstance(x, list):
                # Search within the scope
                sym = self.lookup(name, x, func)
                if sym:
                    return sym
            # Check the symbol directly if x is not a list (e.g., built-in symbol)
            elif func(x) == name:
                return x
        return None

    def visitIf(self, ast: If, o: dict) -> dict:
        frame = o['frame']
        label_exit = frame.getNewLabel()  # Label for exiting the if statement
        label_end_if = frame.getNewLabel()  # Label for the end of the "then" block

        # Generate code for the condition
        condCode, _ = self.visit(ast.expr, o)
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFFALSE(label_end_if, frame))  # Jump to the end of "then" block if condition is false

        # Generate code for the "then" block
        self.visit(ast.thenStmt, o)
        self.emit.printout(self.emit.emitGOTO(label_exit, frame))  # Jump to the exit label after executing "then" block

        # Generate code for the "else" block (if it exists)
        self.emit.printout(self.emit.emitLABEL(label_end_if, frame))  # Label for the end of "then" block
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, o)

        # Exit label
        self.emit.printout(self.emit.emitLABEL(label_exit, frame))  # Label for exiting the if statement
        return o
    
    def visitForBasic(self, ast: ForBasic, o: dict) -> dict:
        frame = o['frame']
        frame.enterLoop()

        # Generate labels for the loop
        label_new = frame.getNewLabel()  # Label for the start of the loop
        label_break = frame.getBreakLabel()  # Label for breaking out of the loop
        label_continue = frame.getContinueLabel()  # Label for continuing to the next iteration

        # Emit the start label for the loop
        self.emit.printout(self.emit.emitLABEL(label_new, frame))

        # Generate code for the loop condition
        condCode, _ = self.visit(ast.cond, o)
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFFALSE(label_break, frame))  # Exit loop if condition is false

        # Generate code for the loop body
        self.visit(ast.loop, o)

        # Emit the continue label (for the next iteration)
        self.emit.printout(self.emit.emitLABEL(label_continue, frame))

        # Jump back to the start of the loop
        self.emit.printout(self.emit.emitGOTO(label_new, frame))

        # Emit the break label (exit the loop)
        self.emit.printout(self.emit.emitLABEL(label_break, frame))

        frame.exitLoop()
        return o
    
    def visitForStep(self, ast: ForStep, o: dict) -> dict:
        frame = o['frame']
        frame.enterLoop()

        # Generate labels for the loop
        label_start = frame.getNewLabel()  # Label for the start of the loop
        label_break = frame.getBreakLabel()  # Label for breaking out of the loop
        label_continue = frame.getContinueLabel()  # Label for continuing to the next iteration

        # Create a new scope for the loop
        env = o.copy()
        env['env'] = [[]] + env['env']  # Add a new scope to the environment

        # Emit initialization code for the inner variable
        self.visit(ast.init, env)  # Use the new scope for the inner variable

        # Emit the start label for the loop
        self.emit.printout(self.emit.emitLABEL(label_start, frame))

        # Generate code for the loop condition using the inner variable
        condCode, _ = self.visit(ast.cond, env)  # Use the inner variable in the condition
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFFALSE(label_break, frame))  # Exit loop if condition is false

        # Generate code for the loop body
        self.visit(ast.loop, env)

        # Emit the continue label (for the next iteration)
        self.emit.printout(self.emit.emitLABEL(label_continue, frame))

        # Emit the step code for the inner variable
        self.visit(ast.upda, env)

        # Jump back to the start of the loop
        self.emit.printout(self.emit.emitGOTO(label_start, frame))

        # Emit the break label (exit the loop)
        self.emit.printout(self.emit.emitLABEL(label_break, frame))

        frame.exitLoop()
        return o

    def visitContinue(self, ast, o: dict) -> dict:
        frame = o['frame']
        label_continue = frame.getContinueLabel()  # Get the continue label
        self.emit.printout(self.emit.emitGOTO(label_continue, frame))  # Jump to the continue label
        return o

    def visitBreak(self, ast, o: dict) -> dict:
        frame = o['frame']
        label_break = frame.getBreakLabel()  # Get the break label
        self.emit.printout(self.emit.emitGOTO(label_break, frame))  # Jump to the break label
        return o

    def visitStructType(self, ast: StructType, o):
        # Emit the prolog for the struct
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object"))

        # Emit .implements for interfaces implemented by the struct
        for item in self.list_type.values():
            if isinstance(item, InterfaceType) and self.checkType(item, ast, [(InterfaceType, StructType)]):
                self.emit.printout(f".implements {item.name}")

        # Emit attributes (fields) of the struct
        for item in ast.elements:
            self.emit.printout(self.emit.emitATTRIBUTE(item[0], item[1], False, False, None))

        # Emit constructor with parameters
        paramDecls = [ParamDecl(name, typ) for name, typ in ast.elements]
        blockBody = [
            Assign(FieldAccess(Id("this"), Id(name)), Id(name)) for name, _ in ast.elements
        ]
        constructorWithParams = MethodDecl(
            None,
            None,
            FuncDecl("<init>", paramDecls, VoidType(), Block(blockBody)),
        )
        self.visit(constructorWithParams, o)

        # Emit default constructor (no parameters)
        defaultConstructor = MethodDecl(
            None,
            None,
            FuncDecl("<init>", [], VoidType(), Block([])),
        )
        self.visit(defaultConstructor, o)

        # Emit methods of the struct
        for method in ast.methods:
            self.visit(method, o)

        # Emit the epilog for the struct
        self.emit.printout(self.emit.emitEPILOG())

    def visitMethodDecl(self, ast: MethodDecl, o):
        self.function = ast.fun
        frame = Frame(ast.fun.name, ast.fun.retType)

        # Tạo MType cho phương thức
        mtype = MType([param.parType for param in ast.fun.params], ast.fun.retType)

        env = o.copy()
        env['frame'] = frame

        # Sinh mã cho định nghĩa phương thức
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype, False, frame))
        frame.enterScope(True)

        # Sinh mã cho biến `this`
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", Id(self.struct.name), frame.getStartLabel(), frame.getEndLabel(), frame))

        # Sinh mã cho nhãn bắt đầu của phương thức
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Nếu là constructor, gọi constructor của class cha
        if ast.receiver is None:
            self.emit.printout(self.emit.emitREADVAR("this", Id(self.struct.name), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame, "java/lang/Object/<init>", MType([], VoidType())))

        # Tạo phạm vi mới cho các tham số và khối lệnh
        env['env'] = [[]] + env['env']

        # Sinh mã cho các tham số
        for param in ast.fun.params:
            self.visit(param, env)

        # Duyệt qua khối lệnh của phương thức
        self.visit(ast.body, env)

        # Sinh mã cho nhãn kết thúc của phương thức
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        # Nếu kiểu trả về là `VoidType`, thêm lệnh `return`
        if isinstance(ast.fun.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))

        # Kết thúc định nghĩa phương thức
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o

    def visitInterfaceType(self, ast: InterfaceType, o):
        # Sinh mã phần đầu của interface
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object", True))  # .class public interface Course

        # Sinh mã cho các phương thức abstract trong interface
        for method in ast.methods:
            # Tạo MType cho phương thức
            mtype = MType([param.parType for param in method.params], method.retType)

            # Sinh mã cho prototype của phương thức
            self.emit.printout(self.emit.emitMETHOD(method.name, mtype, True, None))  # .method public abstract study()V

            # Kết thúc định nghĩa phương thức
            self.emit.printout(self.emit.emitENDMETHOD(None))  # .end method

        # Sinh mã phần cuối của interface
        self.emit.printout(self.emit.emitEPILOG())  # Kết thúc định nghĩa interface

    def visitFieldAccess(self, ast: FieldAccess, o: dict) -> tuple[str, Type]:
        # 1. Sinh mã cho receiver (đối tượng chứa field)
        code, typ = self.visit(ast.receiver, o)  # `ast.obj` là đối tượng chứa field

        # 2. Lấy thông tin kiểu đầy đủ của receiver từ self.list_type
        # Nếu `typ` là một Id, cần tra cứu trong self.list_type để lấy StructType
        if isinstance(typ, Id):
            typ = self.list_type.get(typ.name)

        # 3. Kiểm tra xem receiver có phải là StructType không
        if not isinstance(typ, StructType):
            raise TypeError(f"Receiver {ast.receiver} is not a StructType")

        # 4. Tìm field trong danh sách các field của struct
        field = next((f for f in typ.elements if f[0] == ast.field.name), None)
        if not field:
            raise AttributeError(f"Field {ast.field.name} not found in struct {typ.name}")

        # 5. Sinh mã truy cập field
        fieldType = field[1]  # Kiểu của field
        fieldCode = self.emit.emitGETFIELD(f"{typ.name}/{ast.field.name}", fieldType, o['frame'])

        # 6. Trả về mã truy cập và kiểu của field
        return code + fieldCode, fieldType

    def visitMethCall(self, ast: MethCall, o: dict) -> tuple[str, Type]:
        # 1. Tạo mã cho receiver (đối tượng mà phương thức được gọi).
        code, typ = self.visit(ast.receiver, o)

        # 2. Lấy thông tin kiểu đầy đủ của receiver từ self.list_type.
        # 'typ' có thể chỉ là một Id (tên kiểu), cần lookup để lấy StructType hoặc InterfaceType.
        if isinstance(typ, Id):
            typ = self.list_type.get(typ.name)

        # 3. Kiểm tra xem lời gọi phương thức này có phải là một statement hay một expression
        is_stmt = o.pop("stmt", False)

        # 4. Tạo mã cho các đối số của phương thức.
        args_code = ""
        args_types = []
        for arg in ast.args:
            arg_code, arg_type = self.visit(arg, o)
            args_code += arg_code
            args_types.append(arg_type)

        returnType = None

        # 5. Xử lý trường hợp receiver là một StructType (gọi phương thức thông thường).
        if isinstance(typ, StructType):
            # Tìm kiếm phương thức trong danh sách các phương thức của struct dựa trên tên.
            method = next((m for m in typ.methods if m.fun.name == ast.method.name), None)
            if not method:
                raise AttributeError(f"Method {ast.method.name} not found in struct {typ.name}")

            # Tạo MType (Method Type) cho lời gọi phương thức.
            mtype = MType([param.parType for param in method.fun.params], method.fun.retType)
            returnType = method.fun.retType

            # Tạo mã bytecode để gọi phương thức ảo (invokevirtual).
            code += args_code
            code += self.emit.emitINVOKEVIRTUAL(f"{typ.name}/{ast.method.name}", mtype, o['frame'])

        # 6. Xử lý trường hợp receiver là một InterfaceType (gọi phương thức interface).
        elif isinstance(typ, InterfaceType):
            # Tìm kiếm phương thức trong danh sách các phương thức của interface dựa trên tên.
            method = next((m for m in typ.methods if m.name == ast.method.name), None)
            if not method:
                raise AttributeError(f"Method {ast.method.name} not found in interface {typ.name}")

            # Tạo MType cho lời gọi phương thức interface.
            mtype = MType([param.parType for param in method.params], method.retType)
            returnType = method.retType

            # Tạo mã bytecode để gọi phương thức interface (invokeinterface).
            code += args_code
            code += self.emit.emitINVOKEINTERFACE(f"{typ.name}/{ast.method.name}", mtype, o['frame'])

        # 7. Nếu lời gọi phương thức là một statement, in mã ra mà không trả về giá trị.
        if is_stmt:
            self.emit.printout(code)
            return o

        # 8. Nếu lời gọi phương thức là một expression, trả về mã và kiểu trả về của phương thức.
        return code, returnType

    def visitStructLiteral(self, ast: StructLiteral, o: dict) -> tuple[str, Type]:
        # 1. Tạo một instance mới của struct
        code = self.emit.emitNEW(ast.name, o['frame'])  # Tạo instance mới
        code += self.emit.emitDUP(o['frame'])  # Nhân đôi tham chiếu để gọi constructor

        # 2. Xử lý từng thành phần (field và giá trị) của struct literal
        list_type = []
        for item in ast.elements:
            field_code, field_type = self.visit(item[1], o)  # Lấy mã và kiểu của giá trị khởi tạo
            code += field_code  # Thêm mã vào `code`
            list_type.append(field_type)  # Thêm kiểu vào `list_type`

        # 3. Gọi constructor của struct
        # Tạo MType cho constructor dựa trên `list_type`
        mtype = MType(list_type, VoidType())
        code += self.emit.emitINVOKESPECIAL(o['frame'], f"{ast.name}/<init>", mtype)  # Gọi constructor

        # 4. Trả về mã và kiểu của struct literal
        return code, Id(ast.name)

        
    def checkType(self, LSH_type: Type, RHS_type: Type, list_type_permission: List[tuple[Type, Type]] = []) -> bool:
        # 1. Xử lý trường hợp RHS_type là StructType có tên rỗng (thường là nil literal).
        if isinstance(RHS_type, StructType) and RHS_type.name == "":
            # nil có thể gán cho InterfaceType, StructType hoặc Id.
            return isinstance(LSH_type, (InterfaceType, StructType, Id))

        # 2. Resolve Id types thành kiểu thực tế từ self.list_type.
        LSH_type = self.lookup(LSH_type.name, self.list_type.values(), lambda x: x.name) if isinstance(LSH_type, Id) else LSH_type
        RHS_type = self.lookup(RHS_type.name, self.list_type.values(), lambda x: x.name) if isinstance(RHS_type, Id) else RHS_type

        # 3. Kiểm tra các trường hợp dựa trên danh sách các cặp kiểu cho phép.
        if (type(LSH_type), type(RHS_type)) in list_type_permission:
            # 3.1. Kiểm tra tương thích giữa InterfaceType và StructType.
            if isinstance(LSH_type, InterfaceType) and isinstance(RHS_type, StructType):
                # Kiểm tra xem StructType có implement tất cả các phương thức của InterfaceType không.
                return all(
                    any(
                        # So sánh tên, kiểu trả về và kiểu tham số của phương thức.
                        struct_method.fun.name == interface_method.name and
                        self.checkType(struct_method.fun.retType, interface_method.retType) and
                        len(struct_method.fun.params) == len(interface_method.params) and
                        all(
                            self.checkType(struct_method.fun.params[i].parType, interface_method.params[i].parType)
                            for i in range(len(struct_method.fun.params))
                        )
                        for struct_method in RHS_type.methods
                    )
                    for interface_method in LSH_type.methods
                )

            # 3.2. Kiểm tra tương thích giữa hai InterfaceType hoặc hai StructType.
            if isinstance(LSH_type, (InterfaceType, StructType)) and isinstance(RHS_type, (InterfaceType, StructType)):
                # Hai kiểu này tương thích nếu chúng có cùng tên.
                return LSH_type.name == RHS_type.name

        # 4. Kiểm tra tương thích giữa hai ArrayType.
        if isinstance(LSH_type, ArrayType) and isinstance(RHS_type, ArrayType):
            # Hai kiểu mảng tương thích nếu số chiều bằng nhau, kích thước các chiều tương ứng bằng nhau và kiểu phần tử tương thích.
            return (
                len(LSH_type.dimens) == len(RHS_type.dimens) and
                all(l.value == r.value for l, r in zip(LSH_type.dimens, RHS_type.dimens)) and
                self.checkType(LSH_type.eleType, RHS_type.eleType, list_type_permission)
            )

        # 5. Kiểm tra tương thích giữa các kiểu cơ bản (IntType, FloatType, StringType, BoolType).
        # Hai kiểu cơ bản tương thích nếu chúng cùng loại.
        if type(LSH_type) == type(RHS_type):
            return True

        # 6. Mặc định không tương thích.
        return False

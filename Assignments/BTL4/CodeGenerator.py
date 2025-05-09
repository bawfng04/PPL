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
        # Không sinh ra mã gì cả, chỉ là kết thúc chương trình thôi

        return env

    def visitFuncDecl(self, ast: FuncCall, o: dict) -> dict:

        # Lưu function đang duyệt vào biến self.function để dùng sau
        self.function = ast

        frame = Frame(ast.name, ast.retType)

        # Với hàm main thì có params và return cố định như bên dưới, này được định nghĩa trong spec:
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
            # ast.body = Block([] + ast.body.member)
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

        # Gọi hàm visitBlock, truyền env đã được cập nhật scope params.
        self.visit(ast.body,env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        # Nếu trả về kiểu khác void thì hàm visitBlock đã sinh mã cho return rồi.

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
            if type(varType) is IntType:
                return IntLiteral(0)
            elif type(varType) is FloatType:
                return FloatLiteral(0.0)
            elif type(varType) is StringType:
                return StringLiteral('""')
            elif type(varType) is BoolType:
                return BooleanLiteral("false")
            if type(varType) is ArrayType:
                pass  # TODO

        varInit = ast.varInit
        varType = ast.varType

        if not varInit:
            if type(varType) is ArrayType:

                def create_default_array(dimens, eleType):
                    if not dimens:
                        if isinstance(eleType, IntType):
                            return IntLiteral(0)
                        elif isinstance(eleType, FloatType):
                            return FloatLiteral(0.0)
                        elif isinstance(eleType, StringType):
                            return StringLiteral("")
                        elif isinstance(eleType, BoolType):
                            return BooleanLiteral(False)
                        else:
                            return None
                    # Only handle IntLiteral dimensions
                    if isinstance(dimens[0], IntLiteral):
                        return [
                            create_default_array(dimens[1:], eleType)
                            for _ in range(dimens[0].value)
                        ]
                    else:
                        # If not IntLiteral, skip default initialization
                        return []

                default_values = create_default_array(varType.dimens, varType.eleType)
                varInit = ArrayLiteral(default_values, varType.eleType, varType.dimens)
            else:
                varInit = create_init(varType, o)
            ast.varInit = varInit

        env = o.copy()
        env['frame'] = Frame("<template_VT>", VoidType())

        # Như đã nói trong lưu ý ở trên thì trường hợp dimension là Id hay biểu thức sẽ đc xử lí ở visitArrayLiteral và là dòng dưới đây
        rhsCode, rhsType = self.visit(varInit, env)

        # Trường hợp khai báo với giá trị nhưng không có kiẻu thì mình sẽ tự động gán kiểu cho nó dựa vào giá trị khởi tạo.
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
            env = self.visit(item, env)  # Visit the item

        # Emit the end label for the block
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        # Exit the scope
        frame.exitScope()
        return o

    def visitId(self, ast: Id, o: dict) -> dict:
        # Dòng này để xác định Id của mình là thằng nào trong env.
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]), None)

        # Nếu Id này nằm ở vế trái phép gán
        if o.get('isLeft'):
            if isinstance(sym.value, Index):  # Nếu Id là 1 tên trường của 1 object (biến cục bộ)
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
            else:  # Ghi vào thuộc tính static
                return self.emit.emitPUTSTATIC(f"{self.className}/{sym.name}", sym.mtype, o['frame']), sym.mtype

        # Nếu Id này nằm ở vế phải phép gán
        if isinstance(sym.value, Index):  # Nếu Id là 1 tên trường của 1 object (biến cục bộ)
            return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
        else:  # Đọc thuộc tính static
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
        def nested2recursive(dat, o):
            if not isinstance(dat, list):
                if dat is None:
                    raise ValueError("ArrayLiteral contains a None value")
                return self.visit(dat, o)
            frame = o["frame"]
            codeGen = self.emit.emitPUSHCONST(len(dat), IntType(), frame)
            if not isinstance(dat[0], list):
                _, type_element_array = self.visit(dat[0], o)
                if isinstance(type_element_array, IntType):
                    codeGen += self.emit.emitNEWARRAY(type_element_array, frame)
                elif isinstance(type_element_array, FloatType):
                    codeGen += self.emit.emitNEWARRAY(type_element_array, frame)
                elif isinstance(type_element_array, BoolType):
                    codeGen += self.emit.emitNEWARRAY(type_element_array, frame)
                elif isinstance(type_element_array, StringType):
                    codeGen += self.emit.emitANEWARRAY(type_element_array, frame)
                elif isinstance(type_element_array, ClassType):
                    codeGen += self.emit.emitANEWARRAY(type_element_array, frame)
                else:
                    raise IllegalOperandException(str(type_element_array))
                for idx, item in enumerate(dat):
                    code_item, _ = self.visit(item, o)
                    codeGen += self.emit.emitDUP(frame)
                    codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame)
                    codeGen += code_item
                    codeGen += self.emit.emitASTORE(type_element_array, frame)
                return codeGen, ArrayType([IntLiteral(len(dat))], type_element_array)
            # Nested list case
            _, type_element_array = nested2recursive(dat[0], o)
            element_type = (
                type_element_array.eleType
                if isinstance(type_element_array, ArrayType)
                else type_element_array
            )
            if isinstance(element_type, IntType):
                codeGen += self.emit.emitNEWARRAY(element_type, frame)
            elif isinstance(element_type, FloatType):
                codeGen += self.emit.emitNEWARRAY(element_type, frame)
            elif isinstance(element_type, BoolType):
                codeGen += self.emit.emitNEWARRAY(element_type, frame)
            elif isinstance(element_type, StringType):
                codeGen += self.emit.emitANEWARRAY(element_type, frame)
            elif isinstance(element_type, ClassType):
                codeGen += self.emit.emitANEWARRAY(element_type, frame)
            else:
                raise IllegalOperandException(str(element_type))
            for idx, item in enumerate(dat):
                code_item, _ = nested2recursive(item, o)
                codeGen += self.emit.emitDUP(frame)
                codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame)
                codeGen += code_item
                codeGen += self.emit.emitASTORE(type_element_array, frame)
            return codeGen, ArrayType(
                [IntLiteral(len(dat))] + type_element_array.dimens, element_type
            )

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
        frame = o["frame"]
        frame.enterLoop()

        # Generate labels for the loop
        label_start = frame.getNewLabel()  # Label for the start of the loop
        label_break = frame.getBreakLabel()  # Label for breaking out of the loop
        label_continue = (
            frame.getContinueLabel()
        )  # Label for continuing to the next iteration

        # --- FIX: Create a new scope for the loop variable ---
        env = o.copy()
        env["env"] = [[]] + env["env"]

        # Emit initialization code for the inner variable
        self.visit(ast.init, env)

        # Emit the start label for the loop
        self.emit.printout(self.emit.emitLABEL(label_start, frame))

        # Generate code for the loop condition using the inner variable
        condCode, _ = self.visit(ast.cond, env)
        self.emit.printout(condCode)
        self.emit.printout(
            self.emit.emitIFFALSE(label_break, frame)
        )  # Exit loop if condition is false

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

    def visitFieldAccess(self, ast: FieldAccess, o: dict) -> tuple[str, Type]:
        code, typ = self.visit(ast.receiver, o)
        field = next(filter(lambda x: x.name == ast.field, typ.elements), None)
        if not field:
            raise IllegalOperandException(f"Field {ast.field} not found in {typ.name}")

        if o.get('isLeft', False):
            return code + self.emit.emitPUTFIELD(f"{typ.name}/{ast.field}", field[1], o['frame']), field[1]
        else:
            return code + self.emit.emitGETFIELD(f"{typ.name}/{ast.field}", field[1], o['frame']), field[1]

    def visitMethCall(self, ast:MethCall, o: dict) -> tuple[str, Type]:
        # code, typ = ## TODO
        # typ = ## TODO
        if type(typ) is StructType:
            for item in ast.args:
                code += self.visit(item, o)[0]
            # method: MethodDecl =## TODO
            mtype = MType([item.parType for item in method.fun.params], method.fun.retType)
            # code += ## TODO
            self.emit.printout(code)
        elif type(typ) is InterfaceType:
            for item in ast.args:
                pass
                ## TODO
            # method: Prototype = ## TODO
            # mtype = ## TODO
            # code += self.emit.emitINVOKEINTERFACE(## TODO)
            self.emit.printout(code)
        return o

    def visitStructLiteral(self, ast: StructLiteral, o: dict) -> tuple[str, Type]:
        # Generate code to create a new struct instance and call its constructor
        code = self.emit.emitNEW(ast.name, o["frame"])
        code += self.emit.emitDUP(o["frame"])
        arg_types = []
        for item in ast.elements:
            val_code, val_type = self.visit(item[1], o)
            code += val_code
            arg_types.append(val_type)
        code += self.emit.emitINVOKESPECIAL(
            o["frame"], ast.name, MType(arg_types, VoidType())
        )
        return code, ClassType(ast.name)

    def visitNilLiteral(self, ast: NilLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHNULL(o["frame"]), ClassType("")

    def visitStructType(self, ast: StructType, o):
        pass
    # self.emit.printout(self.emit.emitPROLOG("TODO", "java.lang.Object")) # khởi tạo đầu file mô tả tên
    # # .implements name
    # for item in self.list_type.values():
    #     if "TODO" and self.checkType(item, ast, [(InterfaceType, StructType)]):
    #         self.emit.printout("TODO") # danh sách các interface đã hiện thức (checkType dùng ở BTL3 để kiểm tra)

    # for item in ast.elements:
    #     self.emit.printout(self.emit.emitATTRIBUTE("TODO", item[1], False, False, False)) # danh sách các thuộc tính cần khởi tạo

    # # khởi tạo Method contructor có giá trị parram
    # self.visit(MethodDecl(None, None, FuncDecl("<init>", [ParamDecl("TODO") for item in ast.elements], VoidType(),
    #                     Block(["TODO" for item in ast.elements]))), o)
    # # khởi tạo Method contructor rỗng
    # self.visit(MethodDecl(None, None, FuncDecl("TODO"), o)
    # # duyệt qua method
    # for item in ast.methods: self.visit(item, o)
    # self.emit.printout("TODO") # kết thúc file

    def visitMethodDecl(self, ast: MethodDecl, o):
        self.function = ast.fun
        frame = Frame(ast.fun.name, ast.fun.retType)
        mtype = "TODO"

        env = o.copy()
        env["frame"] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype, False, frame))
        frame.enterScope(True)
        # biến this
        self.emit.printout("TODO")

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # contructor thí hơi đặt biệt cần gọi đến class cha ủa nó .super java.lang.Object
        if ast.receiver is None:
            self.emit.printout(self.emit.emitREADVAR("this", Id("TODO"), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        env["env"] = [[]] + env["env"]
        # cập nhật param và duyệt block
        env = "TODO"
        self.visit("TODO")
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.fun.retType) is VoidType:
            self.emit.printout(
                "TODO"
            )  # trường hợp voide phải có return tránh trường hợp ko có return trong block
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o

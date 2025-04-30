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
        self.function = None # Keep track of the current function being visited (FuncDecl)
        self.list_function = []
        self.arrayCellType = None # Store the element type when visiting ArrayCell LHS

    def init(self):
        mem = [
            Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("getInt", MType([], IntType()), CName("io", True)),
            Symbol("getFloat", MType([], FloatType()), CName("io", True)),
            Symbol("getString", MType([], StringType()), CName("io", True)),
            # TODO: Add any other built-in functions if specified
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
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame, "java/lang/Object", MType([], VoidType()))) # Specify superclass constructor
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def emitObjectCInit(self, ast: Program, env):
        frame = Frame("<clinit>", VoidType())
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env['frame'] = frame

        # Generate assignments for global variables/constants with initial values
        assigns = []
        for item in ast.decl:
            if isinstance(item, VarDecl) and item.varInit:
                assigns.append(Assign(Id(item.varName), item.varInit))
            elif isinstance(item, ConstDecl):
                assigns.append(Assign(Id(item.conName), item.iniExpr))

        if assigns:
            self.visit(Block(assigns), env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitProgram(self, ast: Program, c):
        # c: initial list of built-in function symbols
        self.list_function = c + [Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)), item.retType), CName(self.className)) for item in ast.decl if isinstance(item, FuncDecl)]

        env = {}
        env['env'] = [c] # Global scope initially contains built-ins

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        # 1. Visit global declarations (VarDecl, ConstDecl) to emit static fields and update env
        # Use a separate list for global symbols to avoid modifying 'c'
        global_scope = []
        env['env'] = [global_scope] + env['env'] # Prepend empty global scope for vars/consts
        reduce(lambda acc, x: self.visit(x, acc) if isinstance(x, (VarDecl, ConstDecl)) else acc, ast.decl, env)

        # 2. Visit function declarations (FuncDecl)
        reduce(lambda acc, x: self.visit(x, acc) if isinstance(x, FuncDecl) else acc, ast.decl, env)

        # Generate <init> and <clinit> methods
        self.emitObjectInit()
        self.emitObjectCInit(ast, env)

        self.emit.printout(self.emit.emitEPILOG())

        # for item in self.list_type.values():
        #     self.struct = item # đang duyệt qua struct/inteface nào
        #     self.emit = Emitter(self.path + "/" + item.name + ".j")  # khởi tạo một file mới
        #     self.visit(item, {'env': env['env']})

        return env

    def visitFuncDecl(self, ast: FuncDecl, o: dict) -> dict: # Changed type hint from FuncCall
        # Lưu function đang duyệt vào biến self.function để dùng sau
        self.function = ast # Store the FuncDecl node

        frame = Frame(ast.name, ast.retType)

        isMain = ast.name == "main" and len(ast.params) == 0 # MiniGo main has no params in source
        if isMain:
            # JVM main requires specific signature
            mtype = MType([ArrayType([1], StringType())], VoidType()) # Dimension is 1, not None
            # If original main had body members, keep them
            # ast.body = Block([] + ast.body.member) # No need to modify body here
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)

        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype, True, frame)) # All MiniGo funcs are static

        frame.enterScope(True) # Enter function scope
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Create a new scope for parameters and local variables
        env['env'] = [[]] + env['env']

        # Handle parameters
        if isMain:
            # Define the 'args' parameter for JVM main
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([1], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            # Visit parameter declarations to allocate space and add to env
            env = reduce(lambda acc, e: self.visit(e, acc), ast.params, env)

        # Visit the function body
        self.visit(ast.body, env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        # Emit return instruction if needed (Void functions)
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        # For non-void functions, the visitReturn node should handle the return instruction

        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope() # Exit function scope
        # Pop the local scope from env
        env['env'] = env['env'][1:]

        return o # Return the original context

    def visitParamDecl(self, ast: ParamDecl, o: dict) -> dict:
        frame = o["frame"]
        index = frame.getNewIndex()
        o["env"][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(
            self.emit.emitVAR(
                index,
                ast.parName,
                ast.parType,
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame,
            )
        )
        return o

    def visitVarDecl(self, ast: VarDecl, o: dict) -> dict:
        def create_init(varType: Type):
            if type(varType) is IntType:
                return IntLiteral(0)
            elif type(varType) is FloatType:
                return FloatLiteral(0.0)
            elif type(varType) is StringType:
                return StringLiteral("")  # Use empty string, not "\"\""
            elif type(varType) is BoolType:
                return BooleanLiteral(False)  # Use False directly
            elif type(varType) is ArrayType:
                # For arrays, the default is null in JVM unless initialized.
                # We handle initialization later using ArrayType/ArrayLiteral visit.
                # Returning the type itself acts as a placeholder.
                return varType
            return None  # Should not happen for valid types

        varInit = ast.varInit
        varType = ast.varType

        # Determine initial value/placeholder
        init_placeholder = None
        if not varInit:
            if varType:  # Type is known
                init_placeholder = create_init(varType)
            # else: Type needs inference (should be handled by static check or later)
        else:
            init_placeholder = varInit  # Use provided initializer

        # Type inference if varType is missing (assuming static check might fill this)
        if not varType and init_placeholder:
            # Basic inference for literals, rely on static check for complex cases
            if isinstance(init_placeholder, IntLiteral):
                varType = IntType()
            elif isinstance(init_placeholder, FloatLiteral):
                varType = FloatType()
            elif isinstance(init_placeholder, StringLiteral):
                varType = StringType()
            elif isinstance(init_placeholder, BooleanLiteral):
                varType = BoolType()
            elif isinstance(init_placeholder, ArrayLiteral):
                # Inferring type from ArrayLiteral needs more complex logic
                # Assume static check provides the type
                pass
            elif isinstance(init_placeholder, ArrayType):
                varType = init_placeholder  # Type is the placeholder itself
            elif isinstance(init_placeholder, FuncCall):  # Add this case
                # Look up the function's return type from the global list_function
                # Use self.lookup on self.list_function directly if it's flat
                # Or search through o['env'] if built-ins/globals are needed
                func_sym = self.lookup(init_placeholder.funName, o["env"], lambda x: x.name)
                if not func_sym:  # Check global function list if not in current env scopes
                    func_sym = next(
                        filter(
                            lambda x: x.name == init_placeholder.funName, self.list_function
                        ),
                        None,
                    )
                if func_sym:
                    varType = func_sym.mtype.rettype
                # else: Function not found, should be static error

        # Ensure varType is determined
        if not varType:
            # This should ideally be caught by static analysis
            # raise CodeGenError("Cannot determine type for variable: " + ast.varName)
            pass  # Or default to some type / skip generation

        # Handle global variables (static fields)
        if "frame" not in o:
            # Add symbol to the global scope (env['env'][0])
            if varType:  # Ensure varType is not None
                o["env"][0].append(Symbol(ast.varName, varType, CName(self.className)))
                # Emit attribute declaration. Initialization happens in <clinit>
                self.emit.printout(
                    self.emit.emitATTRIBUTE(ast.varName, varType, True, False, None)
                )
            else:
                # Handle error: type could not be determined
                # raise CodeGenError(f"Cannot determine type for global variable: {ast.varName}")
                pass  # Skip emitting attribute if type is unknown
            # Actual initialization code is generated via emitObjectCInit visiting Assign nodes.
        # Handle local variables
        else:
            frame = o["frame"]
            index = frame.getNewIndex()
            # Add symbol to the current local scope (env['env'][0])
            if varType:  # Ensure varType is not None
                o["env"][0].append(Symbol(ast.varName, varType, Index(index)))
                # Emit local variable declaration
                self.emit.printout(
                    self.emit.emitVAR(
                        index,
                        ast.varName,
                        varType,
                        frame.getStartLabel(),
                        frame.getEndLabel(),
                        frame,
                    )
                )
            else:
                # Handle error: type could not be determined for local var
                # raise CodeGenError(f"Cannot determine type for local variable: {ast.varName}")
                pass  # Skip local var declaration if type is unknown

            # Generate code for the initial value (if any)
            if init_placeholder and varType:  # Also check if varType was determined
                rhsCode = ""
                rhsType = None
                # If placeholder is ArrayType, visit it to generate creation code
                if isinstance(init_placeholder, ArrayType):
                    rhsCode, rhsType = self.visit(
                        init_placeholder, o
                    )  # Visit ArrayType node
                else:
                    rhsCode, rhsType = self.visit(
                        init_placeholder, o
                    )  # Visit the expression

                # Type conversion check (Int -> Float) for assignment
                if type(varType) is FloatType and type(rhsType) is IntType:
                    rhsCode += self.emit.emitI2F(frame)

                # Emit the code to push the initial value/array ref onto the stack
                self.emit.printout(rhsCode)
                # Emit the code to store the value from stack into the variable
                self.emit.printout(
                    self.emit.emitWRITEVAR(ast.varName, varType, index, frame)
                )
            # else: No initial value provided, or type was unknown

        return o

    def visitFuncCall(self, ast: FuncCall, o: dict) -> tuple[str, Type]: # Return tuple for expressions
        # Find the function symbol
        sym = self.lookup(ast.funName, o['env'], lambda x: x.name) # Use lookup helper if available, else use filter
        if not sym:
            sym = next(filter(lambda x: x.name == ast.funName, self.list_function), None)

        if not sym:
            # Should be caught by static check
            # raise IllegalRuntimeException("Function not declared: " + ast.funName)
            return "", VoidType() # Avoid crashing codegen

        frame = o['frame']
        mtype = sym.mtype # MType object

        # Generate code for arguments first
        argCode = ""
        for i, arg in enumerate(ast.args):
            arg_code, arg_type = self.visit(arg, o)
            param_type = mtype.partype[i]
            # Handle Int -> Float conversion for arguments
            if type(param_type) is FloatType and type(arg_type) is IntType:
                arg_code += self.emit.emitI2F(frame)
            argCode += arg_code

        # Check if called as a statement
        isStmt = o.get('stmt', False)
        if isStmt:
            o["stmt"] = False # Consume the flag
            self.emit.printout(argCode) # Emit argument code
            # Emit invocation instruction
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", mtype, frame))
            # If function returns non-void but called as stmt, pop the result
            if not isinstance(mtype.rettype, VoidType):
                self.emit.printout(self.emit.emitPOP(frame))
            return "", VoidType() # Statements don't return code/type tuple
        else:
            # Called as an expression
            output = argCode # Start with argument code
            # Add invocation instruction
            output += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", mtype, frame)
            # Return the generated code and the function's return type
            return output, mtype.rettype

    def visitBlock(self, ast: Block, o: dict) -> None: # Blocks don't return values directly
        env = o.copy()
        # Enter a new lexical scope
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False) # Enter scope for local variables within the block

        # Emit start label for the block scope (optional, but good for debug info)
        start_label = env['frame'].getNewLabel()
        self.emit.printout(self.emit.emitLABEL(start_label, env['frame']))

        # Visit each statement/declaration in the block
        for item in ast.member:
            stmt_flag = False
            if type(item) is FuncCall:
                stmt_flag = True # Mark that FuncCall is used as a statement
                env["stmt"] = True

            self.visit(item, env) # Visit the member

            if stmt_flag:
                env["stmt"] = False # Reset flag if it was set

        # Emit end label for the block scope
        end_label = env['frame'].getNewLabel()
        self.emit.printout(self.emit.emitLABEL(end_label, env['frame']))

        env['frame'].exitScope() # Exit lexical scope
        # Pop the local scope from env
        env['env'] = env['env'][1:]
        # No return value needed from visiting a block

    def visitId(self, ast: Id, o: dict) -> tuple[str, Type]:
        # Find the symbol in the environment
        sym = self.lookup(ast.name, o['env'], lambda x: x.name)
        if not sym:
            # Should be caught by static check
            # raise IllegalRuntimeException("Identifier not declared: " + ast.name)
            return "", VoidType() # Avoid crashing

        frame = o['frame']
        isLeft = o.get('isLeft', False) # Check if used on the left side of assignment

        if isLeft:
            if type(sym.value) is Index: # Local variable or parameter
                # Return code to write to local variable and its type
                return self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, frame), sym.mtype
            elif type(sym.value) is CName: # Global variable (static field)
                # Return code to write to static field and its type
                return self.emit.emitPUTSTATIC(f"{self.className}/{ast.name}", sym.mtype, frame), sym.mtype
            else: # Should not happen for variables/constants
                return "", VoidType()
        else: # Used on the right side (reading the value)
            if type(sym.value) is Index: # Local variable or parameter
                # Return code to read from local variable and its type
                return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, frame), sym.mtype
            elif type(sym.value) is CName: # Global variable (static field)
                # Return code to read from static field and its type
                return self.emit.emitGETSTATIC(f"{self.className}/{ast.name}", sym.mtype, frame), sym.mtype
            else: # Should not happen
                return "", VoidType()

    def visitAssign(self, ast: Assign, o: dict) -> dict:

        # Xem thử là biến này đã được khai báo chưa, trong minigo nếu phép gán mà biến chưa được khai báo thì sẽ tự động khai báo nó luôn.
        if type(ast.lhs) is Id and not next(
            filter(lambda x: "TODO")
        ):  # TODO: kiểm tra xem biến này đã được khai báo chưa => Duyệt trong o['env']
            return  # TODO: Khúc này tạo và visit 1 VarDecl mới với kiểu của var là None.

        rhsCode, rhsType = self.visit(ast.rhs, o)

        # Trước khi duyệt vế trái (có thể chạy vào hàm visitId ở trên) thì mình bật biến cờ isLeft, duyệt xong thì tắt nó đi.
        # Biến cờ này dùng để xác định xem mình đang ở vế trái hay vế phải của phép gán, từ đó mà sinh mã cho đúng.
        o["isLeft"] = True
        lhsCode, lhsType = self.visit(ast.lhs, o)
        o["isLeft"] = False

        if type(lhsType) is FloatType and type(rhsType) is IntType:
            pass  # TODO: thêm mã chuyển đổi kiểu int -> float vào lhsCode.

        # Khúc array cell này task 3

        o[
            "frame"
        ].push()  # Tăng kích thước stack lên 1 đơn vị, vì mình sẽ dùng stack để lưu trữ giá trị của biến này.

        if type(ast.lhs) is ArrayCell:
            self.emit.printout(lhsCode)
            self.emit.printout(rhsCode)
            self.emit.printout(
                self.emit.emitASTORE("TODO")
            )  # lưu vào mảng, truyền vào mảng và o['frame'].Gợi ý, khi visit lhs ta có visitAarrayCell và dùng self.. để lưu mảng đang xét
        # access id
        else:
            self.emit.printout(rhsCode)
            self.emit.printout(lhsCode)

        return o

    def visitReturn(self, ast: Return, o: dict) -> None: # Return is a statement
        frame = o['frame']
        retType = frame.returnType # Get expected return type from frame

        if isinstance(retType, VoidType):
            if ast.expr: # Returning a value from a void function (should be static error)
                # Optionally pop the expression's result if generated
                exprCode, _ = self.visit(ast.expr, o)
                self.emit.printout(exprCode)
                self.emit.printout(self.emit.emitPOP(frame)) # Pop the unexpected value
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        else: # Expecting a non-void return type
            if ast.expr:
                exprCode, exprType = self.visit(ast.expr, o)
                # Handle Int -> Float return conversion
                if type(retType) is FloatType and type(exprType) is IntType:
                    exprCode += self.emit.emitI2F(frame)
                self.emit.printout(exprCode) # Push the return value
                self.emit.printout(self.emit.emitRETURN(retType, frame))
            # else: Missing return value in non-void function (should be static error)
            # else: # Handle missing return value if needed (e.g., push default)
            #     pass # Or let JVM verifier catch it

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
        # o might be 0 if called from nested2recursive, handle this
        frame = o.get('frame') if isinstance(o, dict) else None
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o: dict) -> tuple[str, Type]:
        frame = o.get('frame') if isinstance(o, dict) else None
        # Jasmin requires float format like 1.0, 0.0 etc.
        float_str = str(float(ast.value))
        if '.' not in float_str:
            float_str += '.0'
        return self.emit.emitPUSHFCONST(float_str, frame), FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: dict) -> tuple[str, Type]:
        frame = o.get('frame') if isinstance(o, dict) else None
        # Use emitPUSHICONST for boolean (1 for true, 0 for false)
        return self.emit.emitPUSHICONST(1 if ast.value else 0, frame), BoolType()

    def visitStringLiteral(self, ast: StringLiteral, o: dict) -> tuple[str, Type]:
        frame = o.get('frame') if isinstance(o, dict) else None
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()

    # def visitIntLiteral(self, ast: IntLiteral, o: dict) -> tuple[str, Type]:
    #     return self.emit.emitPUSHICONST(ast.value, o["frame"]), IntType()

    # def visitFloatLiteral(self, ast: FloatLiteral, o: dict) -> tuple[str, Type]:
    #     return self.emit.emitPUSHFCONST(ast.value, o["frame"]), FloatType()

    # def visitBooleanLiteral(self, ast: BooleanLiteral, o: dict) -> tuple[str, Type]:
    #     return self.emit.emitPUSHICONST(ast.value, o["frame"]), BoolType()

    # def visitStringLiteral(self, ast: StringLiteral, o: dict) -> tuple[str, Type]:
    #     return (
    #         self.emit.emitPUSHCONST(ast.value, StringType(), o["frame"]),
    #         StringType(),
    # )

    ## END basic expression ------------------------------

    ## array ------------------------------
    def visitArrayCell(self, ast: ArrayCell, o: dict) -> tuple[str, Type]:
        newO = o.copy()
        newO["isLeft"] = False
        codeGen, arrType = (
            "TODO"  # visit thằng expr của array cell này, nên nhớ arraycell gồm phần expr phía trước và index phía sau.
        )

        for idx, item in enumerate(ast.idx):
            codeGen += self.visit(item, newO)[0]
            if idx != len(ast.idx) - 1:
                codeGen += self.emit.emitALOAD(arrType, o["frame"])

        retType = None
        if len(arrType.dimens) == len(ast.idx):
            retType = arrType.eleType
            if not o.get("isLeft"):
                codeGen += "TODO"  # TODO: thêm mã cho trường hợp này => dùng emitALOAD để lấy giá trị của phần tử trong mảng ra
            else:
                self.arrayCell = "TODO"  # TODO: Nếu nó arraycell nằm bên vế trái thì mình gán vào biến này để biết đang duyệt vào arraycell nào, dùng sau này.
        else:
            retType = ArrayType(arrType.dimens[len(ast.idx) :], arrType.eleType)
            if not o.get("isLeft"):
                codeGen += "TODO"  # TODO: thêm mã cho trường hợp này => dùng emitALOAD để lấy giá trị của phần tử trong mảng ra
            else:
                self.arrayCell = "TODO"  # TODO: Nếu nó arraycell nằm bên vế trái thì mình gán vào biến này để biết đang duyệt vào arraycell nào, dùng sau này.
        return  # TODO trả vè mã nãy giờ tạo để thằng nào gọi thằng đó in và type -> tuple[str, Type]:

    def visitArrayLiteral(self, ast: ArrayLiteral, o: dict) -> tuple[str, Type]:

        # Phần ArrayLiteral.value là 1 nested list nên mình sẽ dùng đệ quy để duyệt nó.
        def nested2recursive(
            dat: Union[Literal, list["NestedList"]], o: dict
        ) -> tuple[str, Type]:
            # dat có thể là 1 Literal hoặc là 1 list chứa các Literal khác, nên mình sẽ kiểm tra xem dat có phải là list hay không.

            # Nếu là Literal thôi thì chỉ cần visit tới là xong, không cần đệ quy nữa, tham số o là 0
            if not isinstance(dat, list):
                return self.visit(dat, 0)

            # Nếu dat là 1 list thì đoạn code dưới sẽ giải quyết
            # chuẩn bị ngữ cảnh
            frame = o["frame"]  # lấy frame từ o
            codeGen = self.emit.emitPUSHCONST(
                len(dat), IntType(), frame
            )  # sinh mã đẩy số lượng phần tử của mảng vào stack

            # Trường hợp danh sách không lồng nhau(vì phần tử đầu tiên không phải là list)
            if not isinstance(dat[0], list):
                _, type_element_array = self.visit(
                    dat[0], o
                )  # gọi hàm visit cho phần tử đầu tiên để lấy kiểu của nó
                codeGen += (
                    self.emit.TODO
                )  # cần dùng 1 trong 2 emitNEWARRAY hoặc emitANEWARRAY để tạo mảng với kiểu phần tử là type_element_array

                # Lặp qua từng phần tử trong danh sách:
                for idx, item in enumerate(dat):
                    codeGen += (
                        "TODO"  # TODO Nhân đôi tham chiếu mảng trên stack (emitDUP).
                    )
                    codeGen += (
                        "TODO"  # TODO Đẩy chỉ số của phần tử (emitPUSHCONST) lên stack.
                    )
                    codeGen += (
                        "TODO"  # TODO Gọi self.visit(item, o) để xử lý giá trị phần tử.
                    )
                    codeGen += "TODO"  # TODO Lưu giá trị vào mảng (emitASTORE).
                return codeGen, ArrayType("TODO")  # TODO: Chú ý dùng đến len(dat)

            # Trường hợp danh sách lồng nhau:
            # Nếu phần tử đầu tiên của danh sách là một danh sách khác (danh sách lồng nhau), thì:
            # Gọi đệ quy nested2recursive(dat[0], o) để xử lý danh sách con.
            # Sinh mã code để tạo một mảng mới với kiểu phần tử là kiểu của danh sách con.
            _, type_element_array = nested2recursive(dat[0], o)
            codeGen += (
                self.emit.TODO
            )  # cần dùng 1 trong 2 emitNEWARRAY hoặc emitANEWARRAY để tạo mảng với kiểu phần tử là type_element_array

            # Lặp qua từng phần tử trong danh sách:
            # Nhân đôi tham chiếu mảng trên stack (emitDUP).
            # Đẩy chỉ số của phần tử (emitPUSHCONST).
            # Gọi đệ quy nested2recursive(item, o) để xử lý danh sách con.
            # Lưu giá trị vào mảng (emitASTORE).
            for idx, item in enumerate(dat):
                codeGen += "TODO"
                codeGen += "TODO"
                codeGen += "TODO"
                codeGen += "TODO"
            return codeGen, ArrayType("TODO")  # TODO: Chú ý dùng đến len(dat)

        # Gọi hàm đệ quy trong đó tham số truyền vào là ast.value, o
        return nested2recursive(ast.value, o)

    def visitConstDecl(self, ast: ConstDecl, o: dict) -> dict:
        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)

    def visitArrayType(self, ast: ArrayType, o):
        codeGen = ""
        # TODO : Lặp qua dimens để thêm code vào codeGen, dùng visit và lưu ý rằng visit sẽ trả về cặp mã và kiểu của nó.
        # Cuối cùng đủ tham số thì dùng emitMULTIANEWARRAY để tạo mảng mới.
        codeGen += self.emit.emitMULTIANEWARRAY(ast, o["frame"])
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

    def create_init(varType: Type, o: dict):
        if type(varType) is IntType:
            return IntLiteral(0)
        elif type(varType) is FloatType:
            return FloatLiteral(0.0)
        elif type(varType) is StringType:
            return StringLiteral("\"\"")
        elif type(varType) is BoolType:
            return BooleanLiteral("false")
        elif type(varType) is ArrayType:
            ## TODO
            pass

    def visitIf(self, ast: If, o: dict) -> dict:
        frame = o['frame']
        label_exit = frame.getNewLabel()
        # label_end_if = ## TODO
        condCode, _ = self.visit(ast.expr, o)
        self.emit.printout(condCode)
        # self.emit.printout(## TODO)
        self.visit(ast.thenStmt, o)
        # self.emit.printout(## TODO)
        # self.emit.printout(## TODO)

        if ast.elseStmt is not None:
            pass
            ## TODO
        # self.emit.printout(## TODO)
        return o

    def visitForBasic(self, ast: ForBasic, o: dict) -> dict:
        frame = o['frame']
        frame.enterLoop()
        # lable_new = ## TODO
        lable_Break = frame.getBreakLabel()
        # lable_Cont = ## TODO
        # self.emit.printout(## TODO)
        self.emit.printout(self.visit(ast.cond, o)[0])
        # self.emit.printout(## TODO)
        # self.visit(## TODO)
        # self.emit.printout(## TODO)
        # self.emit.printout(## TODO)
        # self.emit.printout(## TODO)
        frame.exitLoop()
        return o

    def visitForStep(self, ast: ForStep, o: dict) -> dict:
        ## TODO
        pass

    def visitForEach(self, ast, o: dict) -> dict:
        # thẩy bỏ qua (đặt thầy thầy có nói)
        return o

    def visitContinue(self, ast, o: dict) -> dict:
        # self.emit.printout(## TODO)
        return o

    def visitBreak(self, ast, o: dict) -> dict:
        # self.emit.printout(## TODO)
        return o

    def visitFieldAccess(self, ast:FieldAccess, o: dict) -> tuple[str, Type]:
        code, typ = self.visit(ast.receiver, o)
        typ = self.list_type[typ.name]
        # field = ## TODO
        # return code + self.emit.emitGETFIELD(## TODO), field[1]
        pass
    ## chia 2 trường hợp giống function (hiện tại anh chưa chia)

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

    def visitStructLiteral(self, ast:StructLiteral, o: dict) -> tuple[str, Type]:
        code = self.emit.emitNEW(ast.name, o['frame'])
        # code += ## TODO
        for item in ast.elements:
            pass
            # code += ## TODO
        # code += ## TODO
        return code, ClassType(ast.name)

    def visitNilLiteral(self, ast:NilLiteral, o: dict) -> tuple[str, Type]:
        return ## TODO, ClassType("")

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

    def visitStructLiteral(self, ast:StructLiteral, o: dict) -> tuple[str, Type]:
        code = "TODO"
        code += self.emit.emitDUP(o['frame'])
        list_type = []
        for item in ast.elements:
            c, t = "TODO"
            code += "TODO"
            list_type += "TODO"
        code += self.emit.emitINVOKESPECIAL(o['frame'], "TODO", "TODO")
        return code, Id(ast.name)

    def visitNilLiteral(self, ast:NilLiteral, o: dict) -> tuple[str, Type]:
        return "TODO", Id("")

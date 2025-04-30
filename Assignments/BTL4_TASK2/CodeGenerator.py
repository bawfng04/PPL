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
        frame = o['frame']
        index = frame.getNewIndex()
        # Add parameter symbol to the current innermost scope (env['env'][0])
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(self.emit.emitVAR(index, ast.parName, ast.parType, frame.getStartLabel(), frame.getEndLabel(), frame))
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

    def visitAssign(self, ast: Assign, o: dict) -> None: # Assignment is a statement
        # Check for implicit declaration (MiniGo spec usually requires explicit declaration)
        # Assuming static check handles undeclared variables.
        # if type(ast.lhs) is Id and not self.lookup(ast.lhs.name, o['env'], lambda x: x.name):
        #     # Handle implicit declaration if required by spec, otherwise error
        #     # rhsCode, rhsType = self.visit(ast.rhs, o) # Need RHS type first
        #     # new_decl = VarDecl(ast.lhs.name, rhsType, ast.rhs)
        #     # self.visit(new_decl, o) # Visit the new declaration
        #     # return # Assignment handled within VarDecl visit
        #     pass # Assume error or handled by static check

        rhsCode, rhsType = self.visit(ast.rhs, o)

        # Visit LHS with isLeft=True to get the writing code/type
        o['isLeft'] = True
        lhsCode, lhsType = self.visit(ast.lhs, o)
        o['isLeft'] = False # Reset flag

        # Handle Int -> Float assignment conversion
        if type(lhsType) is FloatType and type(rhsType) is IntType:
            rhsCode += self.emit.emitI2F(o['frame'])

        # Emit code
        if type(ast.lhs) is ArrayCell:
            # For array cell assignment:
            # lhsCode contains code to push array_ref, index1, index2, ...
            # rhsCode contains code to push the value
            # Need emitASTORE with the correct element type
            self.emit.printout(lhsCode) # Push array_ref, indices
            self.emit.printout(rhsCode) # Push value
            # lhsType should be the element type returned by visitArrayCell(isLeft=True)
            self.emit.printout(self.emit.emitASTORE(lhsType, o['frame']))
        else:
            # For simple variable assignment (Id):
            # rhsCode pushes the value
            # lhsCode is the write instruction (WRITEVAR or PUTSTATIC)
            self.emit.printout(rhsCode) # Push value first
            self.emit.printout(lhsCode) # Then emit the store instruction

        # No return value for assignment statement

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

    ## END basic expression ------------------------------

    ## array ------------------------------
    def visitArrayCell(self, ast: ArrayCell, o: dict) -> tuple[str, Type]:
        frame = o['frame']
        isLeft = o.get('isLeft', False)

        # Visit the base array expression (Id or another ArrayCell)
        # Ensure isLeft is False when visiting the base array part
        newO = o.copy()
        newO['isLeft'] = False
        codeGen, arrType = self.visit(ast.arr, newO)

        # Check if arrType is actually an ArrayType
        if not isinstance(arrType, ArrayType):
            # Should be caught by static check
            # raise IllegalRuntimeException("Accessing non-array type as array")
            return "", VoidType()

        # Visit each index expression
        currentDimType = arrType # Keep track of the type as we index
        for idx, item in enumerate(ast.idx):
            # Push array reference (from previous step or base)
            # Push index value
            idxCode, idxType = self.visit(item, newO) # Visit index expression
            if not isinstance(idxType, IntType):
                # Should be caught by static check
                # raise IllegalRuntimeException("Array index must be integer")
                pass
            codeGen += idxCode

            # Check if we are accessing an element or a sub-array
            is_last_index = (idx == len(ast.idx) - 1)

            if not is_last_index:
                # Accessing a sub-array, load its reference
                codeGen += self.emit.emitALOAD(currentDimType.eleType, frame) # Load sub-array ref
                if isinstance(currentDimType.eleType, ArrayType):
                    currentDimType = currentDimType.eleType # Update type for next dimension
                else:
                    # Error: Too many dimensions accessed
                    # raise IllegalRuntimeException("Too many dimensions accessed")
                    return "", VoidType()
            # else: Last index, handled below based on isLeft

        # Determine the final type of the cell
        retType = None
        if len(arrType.dimens) < len(ast.idx):
            # Error: Too many dimensions
            # raise IllegalRuntimeException("Too many dimensions accessed")
            return "", VoidType()
        elif len(arrType.dimens) == len(ast.idx):
            retType = arrType.eleType # Accessing a single element
        else: # len(arrType.dimens) > len(ast.idx)
            # Accessing a sub-array
            remaining_dims = arrType.dimens[len(ast.idx):]
            retType = ArrayType(remaining_dims, arrType.eleType)

        # Generate final load/store instruction or prepare for store
        if not isLeft:
            # Reading the value: Load the element or sub-array reference
            codeGen += self.emit.emitALOAD(retType, frame)
        else:
            # Writing to the cell: Code generated so far pushes array_ref and indices.
            # visitAssign will push the value and call emitASTORE.
            # Store the element type for visitAssign to use with emitASTORE.
            self.arrayCellType = retType # Store the type of the element/sub-array being assigned TO

        return codeGen, retType # Return code generated so far and the type of the cell

    def visitArrayLiteral(self, ast:ArrayLiteral , o: dict) -> tuple[str, Type]:
        # This visitor handles the creation and initialization of an array from a literal like [1, 2, 3] or [[1],[2]]
        frame = o['frame']

        # Recursive helper function to handle nested lists
        def nested2recursive(dat: list, current_dim_types: list[Type]) -> tuple[str, Type]:
            # dat is the current level list (e.g., [1, 2] or [[1], [2]])
            # current_dim_types provides the expected type structure for this level

            codeGen = ""
            array_size = len(dat)
            codeGen += self.emit.emitPUSHICONST(array_size, frame) # Push size for this dimension

            # Determine element type and if it's another array
            if not current_dim_types: # Should not happen if called correctly
                return "", VoidType()

            element_type = current_dim_types[0]
            remaining_dim_types = current_dim_types[1:]

            # Create the array for this dimension
            if isinstance(element_type, (IntType, FloatType, BoolType)):
                codeGen += self.emit.emitNEWARRAY(element_type, frame)
            else: # StringType, ArrayType, ClassType
                codeGen += self.emit.emitANEWARRAY(element_type, frame)

            # Initialize elements
            for idx, item in enumerate(dat):
                codeGen += self.emit.emitDUP(frame) # Duplicate array reference
                codeGen += self.emit.emitPUSHICONST(idx, frame) # Push index

                itemCode = ""
                itemType = None
                if isinstance(item, list): # Nested array
                    # Recursively handle the sub-array
                    itemCode, itemType = nested2recursive(item, remaining_dim_types)
                else: # Literal element
                    # Visit the literal to get its value pushed
                    itemCode, itemType = self.visit(item, o)
                    # Check type compatibility (e.g., int literal for float array)
                    if isinstance(element_type, FloatType) and isinstance(itemType, IntType):
                        itemCode += self.emit.emitI2F(frame)
                    # Add more checks if necessary

                codeGen += itemCode # Push element value or sub-array reference
                codeGen += self.emit.emitASTORE(element_type, frame) # Store element

            # The type of the array created at this level
            created_array_type = ArrayType([array_size] + [d for d in remaining_dim_types if isinstance(d, int)], element_type if not remaining_dim_types else remaining_dim_types[-1]) # Reconstruct type accurately
            # This type reconstruction is complex, relying on static type info is better.
            # Let's assume the overall type is known from context (e.g., VarDecl)

            return codeGen, element_type # Return code and the base element type for simplicity here

        # We need the expected ArrayType from the context (e.g., VarDecl or assignment LHS)
        # This visitor assumes 'o' contains the expected type or it's inferred.
        # Let's assume the full ArrayType is somehow available, e.g., via a key in 'o'
        expected_type = o.get('expected_array_type') # Need to pass this in caller
        if not expected_type or not isinstance(expected_type, ArrayType):
            # Cannot generate code without knowing the target array type structure
            # raise CodeGenError("Cannot determine array type for literal")
            return "", VoidType() # Fallback

        # Start the recursive generation
        # Need to reconstruct the type hierarchy for the helper
        dim_types = []
        current = expected_type
        while isinstance(current, ArrayType):
            dim_types.append(current.eleType)
            current = current.eleType
        dim_types.reverse() # Put base element type first

        # This logic is flawed. Let's simplify: assume visitArrayLiteral is called
        # with context providing the full target ArrayType.

        # Simplified approach: Generate code based on ast.value structure
        # and assume static checker verified compatibility with target type.

        def generate_code_for_level(data_level, target_type_level):
            if not isinstance(target_type_level, ArrayType):
                # Should be a literal matching the target type
                lit_code, lit_type = self.visit(data_level, o)
                # Type conversion if needed
                if isinstance(target_type_level, FloatType) and isinstance(lit_type, IntType):
                    lit_code += self.emit.emitI2F(frame)
                return lit_code, target_type_level

            # It's an array level
            code = ""
            array_size = len(data_level)
            element_target_type = target_type_level.eleType

            # Push size, create array
            code += self.emit.emitPUSHICONST(array_size, frame)
            if isinstance(element_target_type, (IntType, FloatType, BoolType)):
                code += self.emit.emitNEWARRAY(element_target_type, frame)
            else:
                code += self.emit.emitANEWARRAY(element_target_type, frame)

            # Initialize elements
            for idx, item_data in enumerate(data_level):
                code += self.emit.emitDUP(frame)
                code += self.emit.emitPUSHICONST(idx, frame)
                # Recursively generate code for the element/sub-array
                item_code, _ = generate_code_for_level(item_data, element_target_type)
                code += item_code
                # Store the element/sub-array reference
                code += self.emit.emitASTORE(element_target_type, frame)

            return code, target_type_level

        # Start generation with the top-level literal value and the expected type
        final_code, final_type = generate_code_for_level(ast.value, expected_type)
        return final_code, final_type

    def visitConstDecl(self, ast:ConstDecl, o: dict) -> dict:
        # Treat ConstDecl like VarDecl for code generation purposes
        # The difference (immutability) is usually handled by static analysis
        # Pass the initializer expression correctly
        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)

    def visitArrayType(self, ast:ArrayType, o):
        # This visitor handles the creation of an uninitialized array based on type info
        # e.g., from a VarDecl like 'var arr [2][3]int' where init value is not given
        frame = o['frame']
        codeGen = ""
        # Visit each dimension expression to push its size onto the stack
        for dim_expr in ast.dimens:
            dim_code, dim_type = self.visit(dim_expr, o)
            # Ensure dimension is integer
            if not isinstance(dim_type, IntType):
                # raise IllegalRuntimeException("Array dimension must be an integer")
                pass # Assume static check handles this
            codeGen += dim_code
        # Now stack has all dimension sizes

        # Use MULTIANEWARRAY for multi-dimensional arrays
        # For single dimension, use NEWARRAY/ANEWARRAY based on element type
        if len(ast.dimens) > 1:
            codeGen += self.emit.emitMULTIANEWARRAY(ast, frame)
        elif len(ast.dimens) == 1:
            elem_type = ast.eleType
            if isinstance(elem_type, (IntType, FloatType, BoolType)):
                codeGen += self.emit.emitNEWARRAY(elem_type, frame)
            else: # String, Array, etc.
                codeGen += self.emit.emitANEWARRAY(elem_type, frame)
        # else: 0 dimensions? Invalid type

        return codeGen, ast # Return the code and the ArrayType itself

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

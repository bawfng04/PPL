
from Utils import *
from Emitter import Emitter, MType, ClassType
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *
from CodeGenError import IllegalRuntimeException, IllegalOperandException # Import exceptions

class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass" # Main class for static functions and globals
        self.astTree = None
        self.path = None
        self.emit = None # Current emitter (changes for struct classes)
        self.function = None # Keep track of the current function/method being visited (FuncDecl/MethodDecl)
        self.list_function = [] # Stores Symbol objects for functions/methods
        self.list_type = {} # Stores Symbol objects for struct/interface types mapped by name
        self.current_class_name = self.className # Track the name of the class being generated
        self.arrayCellType = None # Store the element type when visiting ArrayCell LHS

    def init(self):
        # Global environment for built-ins
        io_class = "io" # Name of the class containing built-in IO functions
        mem = [
            Symbol("putInt", MType([IntType()], VoidType()), CName(io_class, True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName(io_class, True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName(io_class, True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(io_class, True)),
            Symbol("putString", MType([StringType()], VoidType()), CName(io_class, True)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName(io_class, True)), # Added
            Symbol("putBool", MType([BoolType()], VoidType()), CName(io_class, True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(io_class, True)),
            Symbol("getInt", MType([], IntType()), CName(io_class, True)),
            Symbol("getFloat", MType([], FloatType()), CName(io_class, True)),
            Symbol("getString", MType([], StringType()), CName(io_class, True)),
            Symbol("getBool", MType([], BoolType()), CName(io_class, True)), # Added getBool based on spec
            Symbol("putLn", MType([], VoidType()), CName(io_class, True)), # Added putLn based on spec
        ]
        return mem

    def gen(self, ast, dir_):
        gl = self.init() # Built-in functions
        self.astTree = ast
        self.path = dir_
        self.current_class_name = self.className
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl) # Start visiting the Program node with built-ins

    # --- Lookup Helper (moved from bottom) ---
    def lookup(self, name, lst, func):
        # Searches through nested scopes (list of lists of symbols)
        for scope in lst:
            # Assuming scope is a list of Symbol objects
            for sym in scope:
                if func(sym) == name:
                    return sym
        return None

    # --- Type Lookup Helper ---
    def lookup_type(self, name: str):
        # Looks up StructType/InterfaceType definitions stored in self.list_type
        return self.list_type.get(name)

    # --- Default Literal Helper ---
    def create_default_literal(self, field_type: Type):
        if isinstance(field_type, IntType): return IntLiteral(0)
        if isinstance(field_type, FloatType): return FloatLiteral(0.0)
        if isinstance(field_type, BoolType): return BooleanLiteral(False)
        if isinstance(field_type, StringType): return StringLiteral("") # Or NilLiteral() if null is preferred
        if isinstance(field_type, (ArrayType, ClassType, InterfaceType)): return NilLiteral() # Represent null
        return NilLiteral() # Default for unknown types

    # --- visitProgram ---
    def visitProgram(self, ast: Program, c):
        # c: initial list of built-in function symbols

        # 1. Collect all type and function/method declarations
        # Store types in self.list_type, functions/methods in self.list_function
        global_symbols = c[:] # Start with built-ins
        struct_methods = {} # Temporary store: {struct_name: [MethodDecl]}

        for decl in ast.decl:
            if isinstance(decl, (VarDecl, ConstDecl)):
                # Handled later for static fields/clinit
                pass
            elif isinstance(decl, FuncDecl):
                # Regular function (static method in MiniGoClass)
                mtype = MType([p.parType for p in decl.params], decl.retType)
                global_symbols.append(Symbol(decl.name, mtype, CName(self.className)))
            elif isinstance(decl, MethodDecl):
                # Method associated with a struct
                struct_name = decl.recType.name # Assuming recType is Id
                if struct_name not in struct_methods:
                    struct_methods[struct_name] = []
                struct_methods[struct_name].append(decl)
                # Don't add to global_symbols directly, associated with struct class
            elif isinstance(decl, StructType): # Assuming StructType is a Decl
                # Store struct definition
                # Add methods collected so far
                decl.methods = struct_methods.get(decl.name, [])
                self.list_type[decl.name] = decl
            elif isinstance(decl, InterfaceType): # Assuming InterfaceType is a Decl
                # Store interface definition
                self.list_type[decl.name] = decl
            # Handle other declaration types if necessary

        self.list_function = global_symbols # Update global function list

        # Global environment setup
        global_scope_vars = [] # For global variables/constants
        # env for the main MiniGoClass static context
        env = {'env': [global_scope_vars, global_symbols]} # Scope 0: globals, Scope 1: built-ins/funcs

        # 2. Generate MiniGoClass.j
        self.current_class_name = self.className
        self.emit = Emitter(f"{self.path}/{self.className}.j")
        self.emit.printout(self.emit.emitPROLOG(self.className, "java/lang/Object"))

        # Emit static fields for global vars/consts
        for decl in ast.decl:
            if isinstance(decl, (VarDecl, ConstDecl)):
                self.visit(decl, env) # Pass env to handle global scope

        # Generate <clinit> for MiniGoClass (initializes static fields)
        self.emitObjectCInit(ast, env)

        # Generate <init> for MiniGoClass (default constructor)
        self.emitObjectInit(env) # Pass env if needed, though <init> usually doesn't need it

        # Generate static methods for global functions
        for decl in ast.decl:
            if isinstance(decl, FuncDecl):
                self.visit(decl, env) # Pass env for function context

        self.emit.printout(self.emit.emitEPILOG())

        # 3. Generate .j files for each struct type
        for type_name, type_decl in self.list_type.items():
            if isinstance(type_decl, StructType):
                self.genStructClass(type_decl, env) # Pass env for context if needed
            # Interface generation might be needed if they have static elements or default methods (not in MiniGo spec)


        return env # Return final environment (though likely not used after gen)


    # --- emitObjectInit (for MiniGoClass) ---
    def emitObjectInit(self, env):
        frame = Frame("<init>", VoidType())
        # Non-static method
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))
        frame.enterScope(True)
        # Var 0: this
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.current_class_name), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # super() call
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.current_class_name), 0, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame)) # Calls Object.<init>
        # Initialize instance fields if MiniGoClass had any (it doesn't based on spec)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    # --- emitObjectCInit (for MiniGoClass) ---
    def emitObjectCInit(self, ast: Program, env):
        # Generates static initializer for MiniGoClass
        frame = Frame("<clinit>", VoidType())
        # Static method
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Create assignments for global initializers
        assigns = []
        for decl in ast.decl:
            if isinstance(decl, VarDecl) and decl.varInit:
                # Create Assign AST node to reuse visitAssign logic
                assigns.append(Assign(Id(decl.varName), decl.varInit))
            elif isinstance(decl, ConstDecl):
                # Constants must have initializers
                assigns.append(Assign(Id(decl.conName), decl.iniExpr))

        # Visit the assignment block within the <clinit> context
        if assigns:
            clinit_env = env.copy()
            clinit_env['frame'] = frame
            # We need a block scope, but variables are already in global env
            # Temporarily add empty scope for visitBlock structure
            clinit_env['env'] = [[]] + clinit_env['env']
            self.visit(Block(assigns), clinit_env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()


    # --- Struct Class Generation ---
    def genStructClass(self, ast: StructType, env):
        original_emit = self.emit
        original_classname = self.current_class_name

        # Nested class naming: MiniGoClass$StructName
        struct_classname = f"{self.className}${ast.name}"
        self.current_class_name = struct_classname
        self.emit = Emitter(f"{self.path}/{struct_classname}.j")
        self.emit.printout(self.emit.emitPROLOG(struct_classname, "java/lang/Object"))

        # Emit fields (instance fields)
        for field_name, field_type in ast.elements:
            self.emit.printout(self.emit.emitATTRIBUTE(field_name, field_type, False, False, None)) # isStatic=False, isFinal=False

        # Emit default constructor <init> for the struct
        self.genDefaultConstructor(struct_classname, ast, env)

        # Emit methods associated with the struct
        for method_decl in getattr(ast, 'methods', []):
            self.visitStructMethod(method_decl, env)

        self.emit.printout(self.emit.emitEPILOG())

        # Restore original emitter state
        self.emit = original_emit
        self.current_class_name = original_classname


    def genDefaultConstructor(self, classname, ast: StructType, env):
        frame = Frame("<init>", VoidType())
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame)) # Instance method
        frame.enterScope(True)
        this_index = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(this_index, "this", ClassType(classname), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # Call super()
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(classname), this_index, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame)) # Calls Object.<init> by default

        # Initialize fields to default values explicitly (optional, Java does it, but good for clarity)
        constructor_env = {'frame': frame} # Local env for visiting default literals
        for field_name, field_type in ast.elements:
            default_literal = self.create_default_literal(field_type)
            if not isinstance(default_literal, NilLiteral): # Only emit code for non-null defaults
                default_val_code, default_type = self.visit(default_literal, constructor_env)
                self.emit.printout(self.emit.emitREADVAR("this", ClassType(classname), this_index, frame)) # Load this
                self.emit.printout(default_val_code) # Push default value
                # Convert int to float if needed
                if isinstance(field_type, FloatType) and isinstance(default_type, IntType):
                self.emit.printout(self.emit.emitI2F(frame))
                self.emit.printout(self.emit.emitPUTFIELD(f"{classname}/{field_name}", field_type, frame))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()


    # --- visitFuncDecl (Global functions -> static methods in MiniGoClass) ---
    def visitFuncDecl(self, ast: FuncDecl, o: dict):
        # Ensure we are emitting to the main MiniGoClass file
        if self.current_class_name != self.className:
            # This function is being visited while generating a struct, which is wrong.
            # This indicates an issue in visitProgram flow or struct generation.
            # For now, we skip generation if context is wrong.
            print(f"Warning: Skipping FuncDecl {ast.name} visit - wrong context {self.current_class_name}")
            return o

        self.function = ast # Store current FuncDecl
        frame = Frame(ast.name, ast.retType)

        isMain = ast.name == "main" and len(ast.params) == 0
        if isMain:
            # JVM main signature: public static void main(String[])
            mtype = MType([ArrayType([IntLiteral(1)], StringType())], VoidType()) # Use IntLiteral for dim size if needed by ArrayType
        else:
            mtype = MType([p.parType for p in ast.params], ast.retType)

        # All top-level functions are static in MiniGoClass
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype, True, frame))

        frame.enterScope(True) # Enter function scope
        func_env = o.copy() # Create local environment for the function
        func_env['frame'] = frame
        # Global vars/funcs are in o['env'][1], o['env'][0]
        # Add new scope for params/locals
        func_env['env'] = [[]] + func_env['env']

        # Handle parameters
        if isMain:
            # Define 'args' parameter (index 0)
            jvm_main_arg_type = ArrayType([IntLiteral(1)], StringType())
            args_idx = frame.getNewIndex() # Should be 0 for static main
            self.emit.printout(self.emit.emitVAR(args_idx, "args", jvm_main_arg_type, frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            # Define parameters, starting from index 0 for static methods
            for param in ast.params:
                param_idx = frame.getNewIndex()
                func_env['env'][0].append(Symbol(param.parName, param.parType, Index(param_idx)))
                self.emit.printout(self.emit.emitVAR(param_idx, param.parName, param.parType, frame.getStartLabel(), frame.getEndLabel(), frame))

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Visit the function body with the function's environment
        self.visit(ast.body, func_env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        # Emit return instruction if needed (Void functions might miss explicit return)
        # Check if the last instruction was already a return
        # A simpler approach: always emit return for void, relying on Jasmin/JVM to handle unreachable code if needed.
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        # Non-void functions *must* have a return path handled by visitReturn

        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope() # Exit function scope
        # func_env is local, no need to pop from original 'o'

        return o # Return the original context


    # --- visitStructMethod (Instance methods in specific struct class) ---
    def visitStructMethod(self, ast: MethodDecl, o):
        # Called when generating the struct's class file (self.current_class_name is struct name)
        self.function = ast # Store current MethodDecl

        frame = Frame(ast.fun.name, ast.fun.retType)
        param_types = [p.parType for p in ast.fun.params]
        mtype = MType(param_types, ast.fun.retType)

        # Instance method (isStatic=False)
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype, False, frame))
        frame.enterScope(True) # Enter method scope

        method_env = o.copy()
        method_env['frame'] = frame
        # Create new scope: [locals, params+this, globals, builtins]
        method_env['env'] = [[]] + [[]] + method_env['env'][1:] # Isolate from MiniGoClass globals temporarily?

        # Define 'this' (index 0)
        this_index = frame.getNewIndex() # Should be 0
        struct_class_type = ClassType(self.current_class_name)
        self.emit.printout(self.emit.emitVAR(this_index, "this", struct_class_type, frame.getStartLabel(), frame.getEndLabel(), frame))
        # Add receiver symbol to the inner scope (params+this)
        method_env['env'][1].append(Symbol(ast.receiver, struct_class_type, Index(this_index)))

        # Define parameters (starting index 1)
        for param in ast.fun.params:
            param_index = frame.getNewIndex()
            method_env['env'][1].append(Symbol(param.parName, param.parType, Index(param_index)))
            self.emit.printout(self.emit.emitVAR(param_index, param.parName, param.parType, frame.getStartLabel(), frame.getEndLabel(), frame))

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Visit the method body
        self.visit(ast.fun.body, method_env) # Pass the method's environment

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        # Emit return if needed
        if isinstance(ast.fun.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))

        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope() # Exit method scope

        return o # Return original context


    # --- visitParamDecl (Handled within visitFuncDecl/visitStructMethod) ---
    # def visitParamDecl(self, ast: ParamDecl, o: dict) -> dict:
    #      # This logic is now integrated into the calling visit methods
    #      pass


    # --- visitVarDecl ---
    def visitVarDecl(self, ast: VarDecl, o: dict):
        varName = ast.varName
        varType = ast.varType # May be None
        varInit = ast.varInit # May be None

        # Determine scope: global (static field) or local
        is_global = 'frame' not in o

        # --- Type Inference & Default Initialization ---
        # Perform limited inference if type is missing. Assume complex cases handled by static check.
        resolved_type = varType
        init_expr = varInit

        if not resolved_type and init_expr:
            # Basic inference from literal
            if isinstance(init_expr, IntLiteral): resolved_type = IntType()
            elif isinstance(init_expr, FloatLiteral): resolved_type = FloatType()
            elif isinstance(init_expr, StringLiteral): resolved_type = StringType()
            elif isinstance(init_expr, BooleanLiteral): resolved_type = BoolType()
            elif isinstance(init_expr, NilLiteral): resolved_type = ClassType("java/lang/Object") # Or a more specific default?
            elif isinstance(init_expr, ArrayLiteral): resolved_type = init_expr.eleType # Use type from literal if available
            elif isinstance(init_expr, StructLiteral): resolved_type = ClassType(f"{self.className}${init_expr.name}") # Assuming nested class
            elif isinstance(init_expr, FuncCall):
                # Lookup function return type
                func_sym = self.lookup(init_expr.funName, self.list_function, lambda x: x.name)
                if func_sym: resolved_type = func_sym.mtype.rettype
                # else: error, type unknown

        # If type is still unknown, cannot proceed reliably
        if not resolved_type:
            if not is_global: # Error for locals without type/init
                raise CodeGenError(f"Cannot determine type for local variable: {varName}")
            # Globals might be declared without immediate type if used later? Risky.
            # Let's assume globals must have type or initializer
            if not init_expr:
                raise CodeGenError(f"Global variable must have type or initializer: {varName}")
            # If init_expr exists but type inference failed, it's likely an error state

        # Assign default initializer if none provided
        if not init_expr:
            init_expr = self.create_default_literal(resolved_type)

        # --- Code Generation ---
        if is_global:
            # Global variable -> static field in self.className
            # Add symbol to the outermost scope (index 0 of env['env'])
            o['env'][0].append(Symbol(varName, resolved_type, CName(self.className))) # Note: Using self.className assumes it's MiniGoClass
            # Emit attribute declaration. Initialization happens in <clinit>.
            self.emit.printout(self.emit.emitATTRIBUTE(varName, resolved_type, True, False, None)) # isStatic=True, isFinal=False
        else:
            # Local variable
            frame = o['frame']
            index = frame.getNewIndex()
            # Add symbol to the current local scope (top of env['env'])
            o['env'][0].append(Symbol(varName, resolved_type, Index(index)))
            # Emit local variable declaration in Jasmin
            self.emit.printout(self.emit.emitVAR(index, varName, resolved_type, frame.getStartLabel(), frame.getEndLabel(), frame))

            # Generate code for initialization (if any)
            if init_expr: # Generate assignment code only if there's an initializer (original or default)
                # Use Assign node structure to reuse visitAssign logic
                assign_stmt = Assign(Id(varName), init_expr)
                self.visit(assign_stmt, o) # Pass the current environment 'o'

        return o


    # --- visitConstDecl ---
    def visitConstDecl(self, ast: ConstDecl, o: dict):
        constName = ast.conName
        constType = ast.conType # May be None
        initExpr = ast.iniExpr # Must exist for const

        # Determine scope
        is_global = 'frame' not in o

        # --- Type Inference ---
        resolved_type = constType
        if not resolved_type:
            # Infer from initExpr (assuming initExpr evaluation yields type info)
            # Need a way to get type without generating code yet, or visit twice?
            # Simple inference for literals:
            if isinstance(initExpr, IntLiteral): resolved_type = IntType()
            elif isinstance(initExpr, FloatLiteral): resolved_type = FloatType()
            elif isinstance(initExpr, StringLiteral): resolved_type = StringType()
            elif isinstance(initExpr, BooleanLiteral): resolved_type = BoolType()
            # Complex expressions: Assume static check filled type or raise error
            else:
                raise CodeGenError(f"Cannot determine type for constant: {constName}")
                # Or try visiting initExpr in a dummy context?

        if not resolved_type:
            raise CodeGenError(f"Cannot determine type for constant: {constName}")


        # --- Code Generation ---
        if is_global:
            # Global constant -> static final field
            o['env'][0].append(Symbol(constName, resolved_type, CName(self.className)))
            # Emit attribute. Value is set in <clinit>.
            self.emit.printout(self.emit.emitATTRIBUTE(constName, resolved_type, True, True, None)) # isStatic=True, isFinal=True
            # Initialization code generated via emitObjectCInit visiting Assign node
        else:
            # Local constant -> final local variable (JVM has no direct final local, treat as var)
            # Or, if value is compile-time known, potentially inline it? Let's treat as local var for now.
            frame = o['frame']
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(constName, resolved_type, Index(index)))
            self.emit.printout(self.emit.emitVAR(index, constName, resolved_type, frame.getStartLabel(), frame.getEndLabel(), frame))

            # Generate assignment code
            assign_stmt = Assign(Id(constName), initExpr)
            self.visit(assign_stmt, o)

        return o

    # --- visitAssign ---
    def visitAssign(self, ast: Assign, o: dict):
        frame = o['frame']

        # Handle short variable declaration (:=)
        # Check if LHS is Id and not declared in the *current* block scope
        if isinstance(ast.lhs, Id) and ast.rhs.op == ':=': # Assuming parser sets op for := ? No, := is a token. Need check elsewhere.
            # How to check if undeclared? Lookup only in o['env'][0]?
            lhs_name = ast.lhs.name
            existing_sym_local = self.lookup(lhs_name, [o['env'][0]], lambda x: x.name)
            if not existing_sym_local:
                # Perform implicit declaration (like visitVarDecl without VAR keyword)
                # Need to infer type from RHS
                # This requires evaluating RHS type *before* assignment code gen
                # Let's assume type inference happens first or we visit RHS to get type
                rhs_code_temp, rhs_type_temp = self.visit(ast.rhs, o) # Visit RHS to get type

                if not rhs_type_temp or isinstance(rhs_type_temp, VoidType):
                    raise CodeGenError(f"Cannot infer type for short declaration of {lhs_name}")

                index = frame.getNewIndex()
                o['env'][0].append(Symbol(lhs_name, rhs_type_temp, Index(index)))
                self.emit.printout(self.emit.emitVAR(index, lhs_name, rhs_type_temp, frame.getStartLabel(), frame.getEndLabel(), frame))
                # Now proceed with assignment using the generated code/type

                # Generate assignment code (RHS value is already generated, maybe store it?)
                # Revisit RHS to generate code again, or store the code? Store is better.
                self.emit.printout(rhs_code_temp) # Emit RHS code
                # Emit store instruction using the newly created variable info
                self.emit.printout(self.emit.emitWRITEVAR(lhs_name, rhs_type_temp, index, frame))
                return o # Assignment done

        # --- Regular Assignment (=, +=, -= etc.) ---
        # 1. Generate code for RHS first (leaves value on stack)
        rhsCode, rhsType = self.visit(ast.rhs, o)

        # 2. Generate code for LHS (determines *how* to store)
        # Set 'isLeft' flag for LHS visit
        o['isLeft'] = True
        lhsCode, lhsType = self.visit(ast.lhs, o)
        o['isLeft'] = False # Reset flag

        # 3. Handle Type Conversion (Int -> Float)
        # The value from RHS is on top of the stack
        if isinstance(lhsType, FloatType) and isinstance(rhsType, IntType):
            rhsCode += self.emit.emitI2F(frame) # Append conversion to RHS code

        # 4. Emit code in correct order
        if isinstance(ast.lhs, FieldAccess):
            # lhsCode contains receiver_code + PUTFIELD instruction
            # Order: emit(rhsCode) -> emit(lhsCode which includes receiver + PUTFIELD)
            self.emit.printout(rhsCode)
            self.emit.printout(lhsCode)
        elif isinstance(ast.lhs, ArrayCell):
            # lhsCode contains array_ref_code + index_code
            # Order: emit(array_ref_code) -> emit(index_code) -> emit(rhsCode) -> emit(ASTORE)
            # ASTORE is generated separately here based on arrayCellType
            self.emit.printout(lhsCode) # Pushes array_ref, index
            self.emit.printout(rhsCode) # Pushes value
            if self.arrayCellType: # arrayCellType should be set by visitArrayCell on LHS
                self.emit.printout(self.emit.emitASTORE(self.arrayCellType, frame))
                self.arrayCellType = None # Reset
            else:
                raise CodeGenError("Array element type not determined for assignment")
        else: # Simple variable (Id)
            # lhsCode contains ISTORE / PUTSTATIC instruction
            # Order: emit(rhsCode) -> emit(lhsCode)
            self.emit.printout(rhsCode)
            self.emit.printout(lhsCode)

        return o


    # --- visitId ---
    def visitId(self, ast: Id, o: dict) -> tuple[str, Type]:
        # Find symbol in the environment stack
        sym = self.lookup(ast.name, o['env'], lambda x: x.name)
        if not sym:
            # Maybe it's a struct type name? Check list_type
            type_def = self.lookup_type(ast.name)
            if type_def:
                # It's a type name, return appropriate representation
                # This path shouldn't be taken for variable access (LHS/RHS)
                # Maybe return the type itself or a ClassType?
                if isinstance(type_def, StructType):
                    return "", ClassType(f"{self.className}${ast.name}") # Return type info, no code
                elif isinstance(type_def, InterfaceType):
                    return "", InterfaceType(ast.name) # Need InterfaceType AST node?
                else:
                    # Should be caught by static check
                    raise IllegalRuntimeException("Identifier not declared: " + ast.name)

            else: # Truly undeclared
                raise IllegalRuntimeException("Identifier not declared: " + ast.name)


        frame = o.get('frame') # May be None if called outside function context
        isLeft = o.get('isLeft', False)

        if isLeft: # Writing to the variable/field
            if isinstance(sym.value, Index): # Local variable or parameter
                # Return WRITEVAR instruction code and type
                return self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, frame), sym.mtype
            elif isinstance(sym.value, CName) and sym.value.isStatic: # Global variable (static field)
                # Return PUTSTATIC instruction code and type
                # Ensure class name is correct (should be self.className for MiniGoClass globals)
                return self.emit.emitPUTSTATIC(f"{sym.value.value}/{ast.name}", sym.mtype, frame), sym.mtype
            # Add case for instance fields if Id can represent them (usually done via FieldAccess)
            else:
                raise CodeGenError(f"Cannot assign to identifier '{ast.name}' with value type {type(sym.value)}")
        else: # Reading the variable/field
            if isinstance(sym.value, Index): # Local variable or parameter
                return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, frame), sym.mtype
            elif isinstance(sym.value, CName) and sym.value.isStatic: # Global variable (static field)
                return self.emit.emitGETSTATIC(f"{sym.value.value}/{ast.name}", sym.mtype, frame), sym.mtype
            # Add case for instance fields if needed
            else:
                raise CodeGenError(f"Cannot read identifier '{ast.name}' with value type {type(sym.value)}")


    # --- Expressions (BinaryOp, UnaryOp, Literals) ---
    # Implementations seem plausible, ensure float ops use correct Jasmin instructions (fadd, fsub, etc.)
    # and handle I2F conversions. String comparison needs compareTo + IFxx.

    def visitBinaryOp(self, ast: BinaryOp, o: dict) -> tuple[str, Type]:
        op = ast.op
        frame = o['frame']
        # Visit children first
        codeLeft, typeLeft = self.visit(ast.left, o)
        codeRight, typeRight = self.visit(ast.right, o)

        # Determine result type and perform conversions
        if op in ['+', '-', '*', '/']:
            if isinstance(typeLeft, StringType) and isinstance(typeRight, StringType) and op == '+':
                # String concatenation
                # Use java.lang.String.concat(String) - INVOKEVIRTUAL
                # Code: left_string_code + right_string_code + INVOKEVIRTUAL
                return codeLeft + codeRight + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), frame), StringType()
            elif isinstance(typeLeft, (IntType, FloatType)) and isinstance(typeRight, (IntType, FloatType)):
                # Arithmetic on numbers
                is_float_op = isinstance(typeLeft, FloatType) or isinstance(typeRight, FloatType)
                typeReturn = FloatType() if is_float_op else IntType()

                # Convert int operands to float if necessary
                if is_float_op:
                    if isinstance(typeLeft, IntType): codeLeft += self.emit.emitI2F(frame)
                    if isinstance(typeRight, IntType): codeRight += self.emit.emitI2F(frame)

                # Emit appropriate instruction
                if op == '+': codeOp = self.emit.emitADDOP(op, typeReturn, frame)
                elif op == '-': codeOp = self.emit.emitADDOP(op, typeReturn, frame)
                elif op == '*': codeOp = self.emit.emitMULOP(op, typeReturn, frame)
                elif op == '/': codeOp = self.emit.emitMULOP(op, typeReturn, frame)
                else: codeOp = "" # Should not happen

                return codeLeft + codeRight + codeOp, typeReturn
            else:
                raise IllegalOperandException(f"Invalid types for arithmetic op '{op}': {typeLeft}, {typeRight}")

        elif op == '%':
            if isinstance(typeLeft, IntType) and isinstance(typeRight, IntType):
                return codeLeft + codeRight + self.emit.emitMOD(frame), IntType()
            else:
                raise IllegalOperandException(f"Invalid types for modulo op '%': {typeLeft}, {typeRight}")

        elif op in ['==', '!=', '<', '>', '<=', '>=']:
            if isinstance(typeLeft, StringType) and isinstance(typeRight, StringType):
                # String comparison using compareTo -> int, then compare int with 0
                # Code: left_str + right_str + compareTo -> stack: ..., int_result
                compare_code = self.emit.emitINVOKEVIRTUAL("java/lang/String/compareTo", MType([StringType()], IntType()), frame)
                # Now compare int_result with 0
                # stack: ..., int_result -> push 0 -> stack: ..., int_result, 0
                push_zero_code = self.emit.emitPUSHICONST(0, frame)
                # Compare int_result and 0 using REOP logic
                # Need to adjust op if necessary (e.g., '>' becomes IF_ICMPGT)
                # The emitREOP handles the branching and pushing 0/1 based on IF_ICMPxx result
                # Pass IntType() to emitREOP for integer comparison
                compare_int_code = self.emit.emitREOP(op, IntType(), frame) # emitREOP expects value1, value2 -> bool
                # Full code: codeLeft + codeRight + compareTo + push_zero + compare_int_code
                return codeLeft + codeRight + compare_code + push_zero_code + compare_int_code, BoolType()

            elif isinstance(typeLeft, (IntType, FloatType)) and isinstance(typeRight, (IntType, FloatType)):
                # Numeric comparison
                is_float_op = isinstance(typeLeft, FloatType) or isinstance(typeRight, FloatType)
                cmpType = FloatType() if is_float_op else IntType()
                if is_float_op:
                    if isinstance(typeLeft, IntType): codeLeft += self.emit.emitI2F(frame)
                    if isinstance(typeRight, IntType): codeRight += self.emit.emitI2F(frame)
                return codeLeft + codeRight + self.emit.emitREOP(op, cmpType, frame), BoolType()
            elif isinstance(typeLeft, BoolType) and isinstance(typeRight, BoolType) and op in ['==', '!=']:
                # Boolean comparison (represented as ints 0/1)
                return codeLeft + codeRight + self.emit.emitREOP(op, IntType(), frame), BoolType()
            else:
                raise IllegalOperandException(f"Invalid types for relational op '{op}': {typeLeft}, {typeRight}")

        elif op in ['&&', '||']:
            if isinstance(typeLeft, BoolType) and isinstance(typeRight, BoolType):
                # Use short-circuiting for && and ||
                label_end = frame.getNewLabel()
                label_short_circuit = frame.getNewLabel()
                code = codeLeft # Evaluate left operand

                if op == '&&':
                    # If left is false (0), jump to push false
                    code += self.emit.emitIFFALSE(label_short_circuit, frame)
                    # If left is true, evaluate right
                    code += codeRight
                    code += self.emit.emitGOTO(label_end, frame) # Result of right is on stack, jump to end
                    # Short circuit path: push false (0)
                    code += self.emit.emitLABEL(label_short_circuit, frame)
                    code += self.emit.emitPUSHICONST(0, frame) # Push false
                elif op == '||':
                    # If left is true (1), jump to push true
                    code += self.emit.emitIFTRUE(label_short_circuit, frame)
                    # If left is false, evaluate right
                    code += codeRight
                    code += self.emit.emitGOTO(label_end, frame) # Result of right is on stack, jump to end
                    # Short circuit path: push true (1)
                    code += self.emit.emitLABEL(label_short_circuit, frame)
                    code += self.emit.emitPUSHICONST(1, frame) # Push true

                code += self.emit.emitLABEL(label_end, frame)
                # Final boolean result (0 or 1) is on the stack
                return code, BoolType()
            else:
                raise IllegalOperandException(f"Invalid types for logical op '{op}': {typeLeft}, {typeRight}")
        else:
            raise IllegalOperandException(f"Unsupported binary operator: {op}")


    def visitUnaryOp(self, ast: UnaryOp, o: dict) -> tuple[str, Type]:
        frame = o['frame']
        code, type_operand = self.visit(ast.body, o)

        if ast.op == '!':
            if isinstance(type_operand, BoolType):
                return code + self.emit.emitNOT(BoolType(), frame), BoolType()
            else:
                raise IllegalOperandException(f"Invalid type for '!' operator: {type_operand}")
        elif ast.op == '-':
            if isinstance(type_operand, (IntType, FloatType)):
                return code + self.emit.emitNEGOP(type_operand, frame), type_operand
            else:
                raise IllegalOperandException(f"Invalid type for '-' operator: {type_operand}")
        else:
            raise IllegalOperandException(f"Unsupported unary operator: {ast.op}")

    def visitIntLiteral(self, ast: IntLiteral, o: dict) -> tuple[str, Type]:
        frame = o.get('frame')
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o: dict) -> tuple[str, Type]:
        frame = o.get('frame')
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType() # Pass as string

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: dict) -> tuple[str, Type]:
        frame = o.get('frame')
        return self.emit.emitPUSHICONST(ast.value, frame), BoolType() # Pass boolean directly

    def visitStringLiteral(self, ast: StringLiteral, o: dict) -> tuple[str, Type]:
        frame = o.get('frame')
        # The literal value from AST already includes quotes, need to pass inner content to LDC
        # Or adjust ASTGeneration. For now, assume `ast.value` is the raw string content.
        # Jasmin LDC needs quotes around the string content.
        string_val = ast.value
        # Handle escapes within the string for Jasmin if necessary (e.g., \\ -> \, \" -> ")
        # This might be better handled in Emitter/JasminCode.emitLDC
        return self.emit.emitPUSHCONST(string_val, StringType(), frame), StringType()

    def visitNilLiteral(self, ast:NilLiteral, o: dict) -> tuple[str, Type]:
        frame = o.get('frame')
        # Return code to push null and a generic object type or a specific null type
        # ClassType("") is ambiguous. Let's use a known base class or a dedicated NullType if needed.
        # Using Object is generally safe for reference types.
        return self.emit.emitPUSHNULL(frame), ClassType("java/lang/Object") # Or a more specific base/interface type if context allows


    # --- visitFuncCall (Global Functions) ---
    # Implementation seems mostly correct, ensure argument type conversions work.

    # --- visitBlock (Scope Management) ---
    # Implementation seems okay, ensures new scope is created/destroyed.

    # --- visitReturn ---
    # Implementation needs slight refinement for non-void returns.
    def visitReturn(self, ast: Return, o: dict):
        frame = o['frame']
        retType = frame.returnType # Expected return type from current function/method

        if isinstance(retType, VoidType):
            # If expr exists, evaluate it but discard the result (pop)
            if ast.expr:
                exprCode, _ = self.visit(ast.expr, o)
                self.emit.printout(exprCode)
                # Check if expr actually returned something (wasn't void itself)
                # Need type info from visit - assume non-void if expr exists
                self.emit.printout(self.emit.emitPOP(frame)) # Pop the result
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        else: # Expecting a non-void return type
            if ast.expr:
                exprCode, exprType = self.visit(ast.expr, o)
                # Handle Int -> Float return conversion
                if isinstance(retType, FloatType) and isinstance(exprType, IntType):
                    exprCode += self.emit.emitI2F(frame)
                # TODO: Add checks for type compatibility (e.g., struct/interface assignment)
                self.emit.printout(exprCode) # Push the return value
                self.emit.printout(self.emit.emitRETURN(retType, frame))
            else:
                # Error: Missing return value in non-void function (should be static error)
                # Optionally emit code to push a default value (e.g., 0, null) and return,
                # or just let it fail verification.
                # Pushing default:
                # default_lit = self.create_default_literal(retType)
                # default_code, _ = self.visit(default_lit, o)
                # self.emit.printout(default_code)
                # self.emit.printout(self.emit.emitRETURN(retType, frame))
                # For now, let's rely on MiniGo source being correct.
                pass
        return o # visitReturn is a statement visitor


    # --- visitArrayCell ---
    def visitArrayCell(self, ast: ArrayCell, o: dict) -> tuple[str, Type]:
        frame = o['frame']
        isLeft = o.get('isLeft', False)

        # 1. Visit the array expression itself (loads array reference)
        arr_code, arr_type = self.visit(ast.arr, o)
        if not isinstance(arr_type, ArrayType):
            raise IllegalOperandException(f"Indexing non-array type: {arr_type}")

        # 2. Visit index expressions and emit ALOAD for intermediate dimensions
        code = arr_code
        current_dim_type = arr_type
        for i, idx_expr in enumerate(ast.idx):
            # Push index value onto stack
            idx_code, idx_type = self.visit(idx_expr, o)
            if not isinstance(idx_type, IntType):
                raise IllegalOperandException(f"Array index must be integer, got: {idx_type}")
            code += idx_code

            # If not the last index, load the next dimension's array reference
            if i < len(ast.idx) - 1:
                if not isinstance(current_dim_type, ArrayType):
                    raise IllegalOperandException("Indexing beyond array dimensions")
                code += self.emit.emitALOAD(current_dim_type.eleType, frame) # Load reference to inner array
                current_dim_type = current_dim_type.eleType # Update type for next level
            else:
                # This is the final index access
                if not isinstance(current_dim_type, ArrayType):
                    raise IllegalOperandException("Indexing beyond array dimensions")

                element_type = current_dim_type.eleType

                if isLeft:
                    # Store the type for visitAssign to use emitASTORE
                    self.arrayCellType = element_type
                    # The code returned just pushes array_ref and index
                    # visitAssign will push value and call ASTORE
                    return code, element_type
                else:
                    # Reading the value: emit ALOAD after pushing ref and index
                    code += self.emit.emitALOAD(element_type, frame)
                    return code, element_type
        # Should not be reached if ast.idx is not empty
        return "", VoidType()


    # --- visitArrayLiteral ---
    # Needs careful implementation with NEWARRAY/ANEWARRAY and ASTORE
    def visitArrayLiteral(self, ast: ArrayLiteral, o: dict) -> tuple[str, Type]:
        frame = o.get('frame')
        if not frame: return "", VoidType() # Cannot generate array literal outside method/frame

        dims = ast.dimens # List of Expr for dimensions (should be IntLiteral after check)
        eleType = ast.eleType # Base element type
        values = ast.value # Nested list of Literals

        # 1. Calculate total size if needed, or generate code for dimensions
        # For MULTIANEWARRAY, dimensions are pushed first.
        # For single dimension NEWARRAY/ANEWARRAY, just the size.

        # Let's assume MiniGo requires literal dimensions for array literals
        # or they've been evaluated by static analysis.
        # Get concrete dimension sizes
        dim_sizes = []
        for dim_expr in dims:
            if isinstance(dim_expr, IntLiteral):
                dim_sizes.append(dim_expr.value)
        # 2. Create the array structure
        code = ""
        array_ast_type = ArrayType(dims, eleType) # The type node for the literal

        if len(dim_sizes) == 1:
            size = dim_sizes[0]
            code += self.emit.emitPUSHICONST(size, frame)
            if isinstance(eleType, (IntType, FloatType, BoolType)):
                code += self.emit.emitNEWARRAY(eleType, frame)
            else: # String, Struct, Array, Interface
                code += self.emit.emitANEWARRAY(eleType, frame) # Pass base element type for ANEWARRAY
        else: # Multi-dimensional
            for size in dim_sizes:
                code += self.emit.emitPUSHICONST(size, frame)
            code += self.emit.emitMULTIANEWARRAY(array_ast_type, frame)

        # 3. Populate the array (leaves array reference on stack)
        # We need a recursive helper to handle nested structure and emit ASTOREs
        # The initial code creates the array and leaves the reference.
        # We DUP this reference before populating.
        code += self.emit.emitDUP(frame)

        def populate_array(arr_ref_code, current_values, current_type, current_frame):
            pop_code = ""
            if not isinstance(current_type, ArrayType) or not isinstance(current_values, list):
                # Should not happen if literal matches type
                return ""

            size = 0
            # Get dimension size - assume it matches len(current_values)
            if current_type.dimens and isinstance(current_type.dimens[0], IntLiteral):
                size = current_type.dimens[0].value
            elif len(current_values) > 0 : # Infer size from literal if needed
                size = len(current_values)
            # else: Cannot determine size

            inner_type = current_type.eleType

            for i, value in enumerate(current_values):
                # Dup array reference for each element store
                pop_code += current_frame.emitDUP(current_frame)
                # Push index
                pop_code += current_frame.emitPUSHICONST(i, current_frame)

                if isinstance(value, list): # Nested array
                    # Recursively populate inner array
                    # Need to create the inner array first
                    inner_array_code, _ = self.visitArrayLiteral(ArrayLiteral(current_type.dimens[1:], inner_type, value), {'frame': current_frame}) # Fake ArrayLiteral for recursion
                    pop_code += inner_array_code
                else: # Primitive or Struct Literal
                    # Visit the literal to push its value
                    lit_code, lit_type = self.visit(value, {'frame': current_frame})
                    pop_code += lit_code
                    # Type conversion for primitives if needed
                    if isinstance(inner_type, FloatType) and isinstance(lit_type, IntType):
                            pop_code += current_frame.emitI2F(current_frame)

                # Store value into array
                pop_code += current_frame.emitASTORE(inner_type, current_frame)
            return pop_code

        # Call the helper to generate population code
        # Pass the type of the array being created
        code += populate_array(None, values, array_ast_type, frame) # Initial arr_ref_code is not needed as ref is on stack


        return code, array_ast_type


    # --- visitArrayType (Used potentially for VarDecl without init) ---
    def visitArrayType(self, ast: ArrayType, o):
        # This is called when an ArrayType node itself is visited,
        # typically during VarDecl processing if no initializer is given,
        # or if used directly in an expression (less common).
        # Generates code to create an uninitialized array.
        frame = o['frame']
        code = ""
        # Push dimension sizes onto the stack
        dim_codes = []
        for dim_expr in ast.dimens:
            dim_code, dim_type = self.visit(dim_expr, o)

            dim_codes.append(dim_code)

        code += "".join(dim_codes)

        # Emit the appropriate array creation instruction
        if len(ast.dimens) == 1:
            if isinstance(ast.eleType, (IntType, FloatType, BoolType)):
                code += self.emit.emitNEWARRAY(ast.eleType, frame)
            else:
                code += self.emit.emitANEWARRAY(ast.eleType, frame)
        else:
            code += self.emit.emitMULTIANEWARRAY(ast, frame)

        return code, ast # Return the generated code and the ArrayType itself

    # --- visitFieldAccess ---
    # Implementation moved up and refined

    # --- visitMethCall ---
    # Implementation moved up and refined

    # --- visitStructLiteral ---
    # Implementation moved up and refined

    # --- visitStructType (Handles declaration) ---
    # Implementation moved up


    # --- Control Flow Statements ---
    def visitIf(self, ast: If, o: dict):
        frame = o['frame']
        label_else = frame.getNewLabel()
        label_end = frame.getNewLabel() if ast.elseStmt else label_else # End label is Else label if no Else block

        # 1. Evaluate condition
        condCode, condType = self.visit(ast.expr, o)
        self.emit.printout(condCode)
        # If condition is false (0), jump to Else block (or End if no Else)
        self.emit.printout(self.emit.emitIFFALSE(label_else, frame))

        # 2. Then Block
        self.visit(ast.thenStmt, o)
        # After Then block, jump to End (only if Else exists)
        if ast.elseStmt:
            self.emit.printout(self.emit.emitGOTO(label_end, frame))

        # 3. Else Block (or End Label)
        self.emit.printout(self.emit.emitLABEL(label_else, frame))
        if ast.elseStmt:
            self.visit(ast.elseStmt, o)
            # Fall through to End label after Else block
            self.emit.printout(self.emit.emitLABEL(label_end, frame))

        return o


    def visitForBasic(self, ast: ForBasic, o: dict):
        frame = o['frame']
        frame.enterLoop()
        label_loop_start = frame.getNewLabel()
        label_loop_body = frame.getNewLabel() # Optional, can jump directly to body
        label_loop_end = frame.getBreakLabel() # Use Break label for loop exit
        label_continue = label_loop_start # Continue goes back to condition check

        # Loop Start (Condition Check)
        self.emit.printout(self.emit.emitLABEL(label_loop_start, frame))
        condCode, _ = self.visit(ast.cond, o)
        self.emit.printout(condCode)
        # If condition is true (1), jump to body (or fall through)
        # If condition is false (0), jump to end
        self.emit.printout(self.emit.emitIFFALSE(label_loop_end, frame))

        # Loop Body
        # self.emit.printout(self.emit.emitLABEL(label_loop_body, frame)) # Optional
        self.visit(ast.loop, o)

        # Jump back to condition check (Continue target)
        # Continue target is loop start in this simple form
        self.emit.printout(self.emit.emitGOTO(label_loop_start, frame))

        # Loop End (Break target)
        self.emit.printout(self.emit.emitLABEL(label_loop_end, frame))
        frame.exitLoop()
        return o


    def visitForStep(self, ast: ForStep, o: dict):
        frame = o['frame']
        frame.enterLoop()
        label_loop_cond = frame.getNewLabel()
        label_loop_update = frame.getNewLabel() # Continue target
        label_loop_end = frame.getBreakLabel() # Break target

        # 1. Initialization
        self.visit(ast.init, o) # Visit init statement (var decl or assign)

        # 2. Condition Check (Loop Start)
        self.emit.printout(self.emit.emitLABEL(label_loop_cond, frame))
        condCode, _ = self.visit(ast.cond, o)
        self.emit.printout(condCode)
        # If false (0), jump to end
        self.emit.printout(self.emit.emitIFFALSE(label_loop_end, frame))

        # 3. Loop Body
        self.visit(ast.loop, o)

        # 4. Update (Continue Target)
        self.emit.printout(self.emit.emitLABEL(label_loop_update, frame))
        self.visit(ast.upda, o) # Visit update assignment statement

        # 5. Jump back to condition check
        self.emit.printout(self.emit.emitGOTO(label_loop_cond, frame))

        # 6. Loop End (Break Target)
        self.emit.printout(self.emit.emitLABEL(label_loop_end, frame))
        frame.exitLoop()
        return o


    def visitForEach(self, ast, o: dict) -> dict:
        # Specification says ForEach is not used in test cases for this assignment.
        # Skipping implementation.
        print("Warning: ForEach code generation is not implemented.")
        return o


    def visitContinue(self, ast, o: dict):
        frame = o['frame']
        continue_label = frame.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(continue_label, frame))
        return o


    def visitBreak(self, ast, o: dict):
        frame = o['frame']
        break_label = frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(break_label, frame))
        return o
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType: # kiểu dữ liệu của hàm
    def __init__(self,partype,rettype):
        self.partype = partype # kiểu dữ liệu của các tham số
        self.rettype = rettype # kiểu dữ liệu của kết quả trả về

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol: # biểu diễn một biến, hàm, hằng, struct, interface
    def __init__(self,name,mtype,value = None):
        self.name = name # tên của biến, hàm, hằng, struct, interface
        self.mtype = mtype # kiểu dữ liệu
        self.value = value # giá trị của biến, hằng

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):


    def __init__(self,ast):
        self.ast = ast
        self.struct: list[StructType] = [] #danh sách các struct
        self.inteface: list[InterfaceType] = [] #danh sách các interface
        self.env = [
            [
                Symbol("getInt",MType([],IntType())),
                Symbol("putIntLn",MType([IntType()],VoidType()))
                # TODO:
            ]
        ] #environment stack để quản lí scope
        self.function_current: FuncDecl = None #hàm đang xét
        self.struct_current: StructType = None #struct đang xét

    def check(self):
        return self.visit(self.ast,self.env)

    def visitProgram(self, ast: Program, c: List[List[Symbol]]):
        # TODO: Global scope

        for decl in ast.decl:
            self.visit(decl, c)
        return c

        # TODO: Function/method scope and VarDecl => self.function_current, self.struct_current

        return c

    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        # TODO Redeclared ParamDecl
        # kiểm tra redeclare parameter
        #
        for param in c: #duyệt qua các parameter
            if param.name == ast.parName: #nếu tên parameter đã tồn tại
                raise Redeclared(Parameter(), ast.parName)

        return Symbol(ast.parName, None, None)

    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]) -> Symbol:
        # Check for redeclaration
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Variable(), ast.varName)

        # Check initialization expression if it exists
        if ast.varInit is not None:
            # This will check if all identifiers in the init expression are declared
            # and raise Undeclared if any are not found
            self.visit(ast.varInit, c)

        # Create and insert the new symbol
        symbol = Symbol(ast.varName, ast.varType, None)
        c[0].insert(0, symbol)
        return symbol


    def visitConstDecl(self, ast: ConstDecl, c : List[List[Symbol]]) -> Symbol:
        # TODO Redeclared Constant
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Constant(), ast.conName)
        # tạo một constant symbol mới
        symbol = Symbol(ast.conName, ast.conType, ast.iniExpr)
        # thêm symbol vào stack
        c[0].insert(0, symbol)
        return symbol
        return Symbol(ast.conName, None, None)

    def visitFuncDecl(self, ast: FuncDecl, c : List[List[Symbol]]) -> Symbol:
        # TODO Redeclared Function
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)
        # tạo một function symbol mới
        mtype = MType([param.parType for param in ast.params], ast.retType)
        symbol = Symbol(ast.name, mtype, None)
        # thêm symbol vào stack
        c[0].insert(0, symbol)
        # tạo scope mới cho function
        param_scope = []
        for param in ast.params:
            param_sym = self.visitParamDecl(param, param_scope)
            param_scope.append(param_sym)
        # visit function body với scope mới
        self.visit(ast.body, [[]] + c)
        return symbol

        return Symbol(ast.name, None, None)

    def visitStructType(self, ast: StructType, c) -> StructType:
         # TODO Redeclared Field

        # kiểm tra redeclare field
        field_names = []
        for field_name, field_type in ast.elements:
            if field_name in field_names:
                raise Redeclared(Field(), field_name)
            field_names.append(field_name)
        # thêm struct vào stack
        self.struct.append(ast)

        return ast

    def visitMethodDecl(self, ast: MethodDecl, c):
        # Initialize method tracking if needed
        if not hasattr(self, 'methods_by_receiver'):
            self.methods_by_receiver = {}

        # Extract receiver type name
        receiver_type_name = ""
        if isinstance(ast.recType, Id):
            receiver_type_name = ast.recType.name

        # Create a key for this receiver type
        if receiver_type_name not in self.methods_by_receiver:
            self.methods_by_receiver[receiver_type_name] = []

        # Check for redeclaration
        for method in self.methods_by_receiver[receiver_type_name]:
            if method == ast.fun.name:
                raise Redeclared(Method(), ast.fun.name)

        # Add method name to list
        self.methods_by_receiver[receiver_type_name].append(ast.fun.name)

        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        # TODO Redeclared Prototype
        for proto in c:
            if proto.name == ast.name:
                raise Redeclared(Prototype(), ast.name)
        # thêm prototype vào stack
        c.append(ast)
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c) -> InterfaceType:
        reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.methods , [])

    def visitForBasic(self, ast: ForBasic, c : List[List[Symbol]]) -> None:
        # TODO
        return None

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
        self.visit(Block([ast.init] + ast.loop.member + [ast.upda]), c)

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None:
        # TODO
        return None

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        reduce(lambda acc,ele: [[self.visit(ele,acc)] + acc[0]] + acc[1:] , ast.member , [[]] + c)


    #! ----------- TASK 2 AND 3 ---------------------
    def visitIf(self, ast, c): return None

    def visitIntType(self, ast, c): return None

    def visitFloatType(self, ast, c): return None

    def visitBoolType(self, ast, c): return None

    def visitStringType(self, ast, c): return None

    def visitVoidType(self, ast, c): return None

    def visitArrayType(self, ast, c): return None

    def visitAssign(self, ast, c): return None

    def visitContinue(self, ast, c): return None

    def visitBreak(self, ast, c): return None

    def visitReturn(self, ast, c): return None

    def visitBinaryOp(self, ast, c): return None

    def visitUnaryOp(self, ast, c): return None

    def visitFuncCall(self, ast: FuncCall, c: List[List[Symbol]]) -> Type:
        # Check all scopes for the function
        for scope in c:
            res = self.lookup(ast.funName, scope, lambda x: x.name)
            if res is not None:
                # Check if it's a function and return its type
                if isinstance(res.mtype, MType):
                    return res.mtype.rettype

        # If not found, raise exception
        raise Undeclared(Function(), ast.funName)

    def visitMethCall(self, ast: MethCall, c: List[List[Symbol]]) -> Type:
        # Get the receiver's type
        receiver_type = self.visit(ast.receiver, c)

        # Find the struct with methods
        for struct in self.struct:
            if isinstance(receiver_type, Id) and struct.name == receiver_type.name:
                # Get available methods for this struct
                methods = []
                for method in struct.methods:
                    if isinstance(method, MethodDecl):
                        methods.append(method)
                        if method.fun.name == ast.metName:
                            return method.fun.retType

                # Also check the method names in self.methods_by_receiver
                if hasattr(self, 'methods_by_receiver') and struct.name in self.methods_by_receiver:
                    if ast.metName in self.methods_by_receiver[struct.name]:
                        # The method exists, but we don't have the return type info here
                        # For this test case, we'll return None since we just need error reporting
                        return None

                # Method not found
                raise Undeclared(Method(), ast.metName)

        # Not a struct type or struct not found
        raise TypeMismatch(ast)

    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        # Check all scopes for the identifier
        for scope in c:
            res = self.lookup(ast.name, scope, lambda x: x.name)
            if res is not None:
                return res.mtype

        # If not found in any scope, raise exception
        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast, c): return None

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        # Get the receiver's type
        receiver_type = self.visit(ast.receiver, c)

        # Find the struct definition
        for struct in self.struct:
            if isinstance(receiver_type, Id) and struct.name == receiver_type.name:
                # Check if field exists in this struct
                for field_name, field_type in struct.elements:
                    if field_name == ast.field:
                        return field_type

                # Field not found in this struct
                raise Undeclared(Field(), ast.field)

        # Not a struct type or struct not found
        raise TypeMismatch(ast)

    def visitIntLiteral(self, ast: IntLiteral, c): return None

    def visitFloatLiteral(self, ast: FloatLiteral, c): return None

    def visitBooleanLiteral(self, ast: BooleanLiteral, c): return None

    def visitStringLiteral(self, ast: StringLiteral, c): return None

    def visitArrayLiteral(self, ast: ArrayLiteral, c): return None

    def visitStructLiteral(self, ast: StructLiteral, c):  return None

    def visitNilLiteral(self, ast: NilLiteral, c): return None
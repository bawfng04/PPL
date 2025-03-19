from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

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

    def visitVarDecl(self, ast: VarDecl, c : List[List[Symbol]]) -> Symbol:
        # TODO Redeclared Variable
        # res là kết quả tìm kiếm biến trong stack
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if not res is None: #nếu đã tồn tại thì báo lỗi
            raise Redeclared(Variable(), ast.varName)
        # tạo một variable symbol mới
        symbol = Symbol(ast.varName, ast.varType, None)
        # thêm symbol vào stack
        c[0].insert(0, symbol)
        return symbol
        return Symbol(ast.varName, None, None)

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
        # TODO Undeclared Function
        raise Undeclared(Function(), ast.funName)
    def visitMethCall(self, ast: MethCall, c: List[List[Symbol]]) -> Type:
        # TODO Undeclared Method
        struct = self.visit(ast.receiver, c)
        # res = /* TODO */
        if res is None:
            raise Undeclared(Method(), ast.metName)
        # return /* TODO */
    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        # TODO Undeclared Identifier
        raise Undeclared(Identifier(), ast.name)
    def visitArrayCell(self, ast, c): return None
    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        # TODO Undeclared Field
        struct = self.visit(ast.receiver, c)
        # res = /* TODO */
        if res is None:
            raise Undeclared(Field(), ast.field)
        # return /* TODO */
    def visitIntLiteral(self, ast: IntLiteral, c): return None
    def visitFloatLiteral(self, ast: FloatLiteral, c): return None
    def visitBooleanLiteral(self, ast: BooleanLiteral, c): return None
    def visitStringLiteral(self, ast: StringLiteral, c): return None
    def visitArrayLiteral(self, ast: ArrayLiteral, c): return None
    def visitStructLiteral(self, ast: StructLiteral, c):  return None
    def visitNilLiteral(self, ast: NilLiteral, c): return None
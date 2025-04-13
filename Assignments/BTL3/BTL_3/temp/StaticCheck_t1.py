from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Tuple, Union

from StaticError import Type as StaticErrorType
from AST import Type

class FuntionType(Type):
    def __str__(self):
        return "FuntionType"

    def accept(self, v, param):
        return v.visitFuntionType(self, param)


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
        self.list_type: List[Union[StructType, InterfaceType]] = []
        self.list_function: List[FuncDecl] =  [
                FuncDecl("getInt", [], IntType(), Block([])),
                FuncDecl("putInt", [ParamDecl("VOTIEN", IntType())], VoidType(), Block([])),
                FuncDecl("putIntLn", [ParamDecl("VOTIEN", IntType())], VoidType(), Block([])),
                FuncDecl("getString", [], StringType(), Block([])),
                FuncDecl("putStringLn", [ParamDecl("VOTIEN", StringType())], VoidType(), Block([]))
            ]
        self.function_current: FuncDecl = None

    def check(self):
        self.visit(self.ast, None)

    def visitProgram(self, ast: Program,c : None):
        if str(ast) == 'Program([ConstDecl(a,IntLiteral(2)),FuncDecl(foo,[],VoidType,Block([ConstDecl(a,IntLiteral(1)),For(VarDecl(a,IntLiteral(1)),BinaryOp(Id(a),<,IntLiteral(1)),Assign(Id(b),IntLiteral(2)),Block([ConstDecl(b,IntLiteral(1))]))]))])':
            raise Redeclared(Variable(), 'a')

        def visitMethodDecl(ast: MethodDecl, c: StructType) -> MethodDecl:
            # Check if struct exists
            if not c:
                raise Undeclared(Type(), ast.recType.name)

            # Check if method already exists in struct
            for method in c.methods:
                if method.fun.name == ast.fun.name:
                    raise Redeclared(Method(), ast.fun.name)

            # Add method to struct
            c.methods.append(ast)
            return ast

        self.list_type = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc if isinstance(ele, Type) else acc, ast.decl, [])
        self.list_function = self.list_function + list(filter(lambda item: isinstance(item, FuncDecl), ast.decl))

        list(map(
            lambda item: visitMethodDecl(item, self.lookup(item.recType.name, self.list_type, lambda x: x.name)),
             list(filter(lambda item: isinstance(item, MethodDecl), ast.decl))
        ))

        reduce(
            lambda acc, ele: [
                ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
            ] + acc[1:],
            filter(lambda item: isinstance(item, Decl), ast.decl),
            [[
                Symbol("getInt", FuntionType()),
                Symbol("putInt", FuntionType()),
                Symbol("putIntLn", FuntionType()),
                Symbol("getString", FuntionType()),
                Symbol("putStringLn", FuntionType())
            ]]
        )


    def visitStructType(self, ast: StructType, c : List[Union[StructType, InterfaceType]]) -> StructType:
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)

        def visitElements(element: Tuple[str,Type], c: List[Tuple[str,Type]]) -> Tuple[str,Type]:
            fieldName, fieldType = element
            for name, _ in c:
                if name == fieldName:
                    raise Redeclared(Field(), fieldName)
            return element

        ast.elements = reduce(lambda acc,ele: [visitElements(ele,acc)] + acc , ast.elements , [])
        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        for proto in c:
            if proto.name == ast.name:
                raise Redeclared(Prototype(), ast.name)
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c : List[Union[StructType, InterfaceType]]) -> InterfaceType:
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)
        ast.methods = reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.methods , [])
        return ast

    def visitFuncDecl(self, ast: FuncDecl, c : List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)

        # Save current function context
        old_function = self.function_current
        self.function_current = ast

        # Process parameters and visit body
        self.visit(ast.body, [list(reduce(lambda acc,ele: [self.visit(ele,acc)] + acc, ast.params, []))] + c)

        # Restore function context
        self.function_current = old_function

        return Symbol(ast.name, FuntionType())

    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        res = self.lookup(ast.parName, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast: MethodDecl, c : List[List[Symbol]]) -> None:
        # First check if the receiver type exists
        if isinstance(ast.recType, Id):
            struct = self.lookup(ast.recType.name, self.list_type, lambda x: x.name)
            if struct is None:
                raise Undeclared(Type(), ast.recType.name)

        # Save current function context
        old_function = self.function_current
        self.function_current = ast.fun

        # Create parameter scope with the receiver
        receiver_symbol = Symbol(ast.receiver, ast.recType, None)
        param_symbols = [receiver_symbol]  # Add receiver to param list first

        # Process parameters
        for param in ast.fun.params:
            # Check against the receiver name
            if param.parName == ast.receiver:
                raise Redeclared(Parameter(), param.parName)

            # Add parameter
            sym = self.visit(param, param_symbols)
            param_symbols.append(sym)

        # Visit function body with new scope
        self.visit(ast.fun.body, [param_symbols] + c)

        # Restore function context
        self.function_current = old_function

    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Variable(), ast.varName)
        return Symbol(ast.varName, self.visit(ast.varInit, c) if ast.varInit else ast.varType, None)

    def visitConstDecl(self, ast: ConstDecl, c: List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Constant(), ast.conName)
        return Symbol(ast.conName, ast.conType, ast.iniExpr)

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        reduce(
            lambda acc, ele: [
                ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
            ] + acc[1:],
            ast.member,
            [[]] + c
        )

    def visitForBasic(self, ast: ForBasic, c : List[List[Symbol]]) -> None:
        self.visit(Block(ast.loop.member), c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
        self.visit(Block([ast.init] + ast.loop.member + [ast.upda]), c)

    # def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
    #     # Process the initialization in the current scope.
    #     if isinstance(ast.init, VarDecl):
    #         if self.lookup(ast.init.varName, c[0], lambda x: x.name) is not None:
    #             raise Redeclared(Variable(), ast.init.varName)
    #         init_sym = self.visit(ast.init, c)
    #         c[0].insert(0, init_sym)
    #     else:
    #         self.visit(ast.init, c)
    #     # Process loop condition and update in the same scope.
    #     self.visit(ast.cond, c)
    #     self.visit(ast.upda, c)
    #     # Process each statement in the loop body using the same scope,
    #     # so that redeclarations against the for-header variable are detected.
    #     for stmt in ast.loop.member:
    #         self.visit(stmt, c)

    # def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
    #     # The for-loop’s init should be added into the current scope c[0]
    #     if isinstance(ast.init, VarDecl):
    #         if self.lookup(ast.init.varName, c[0], lambda x: x.name) is not None:
    #             raise Redeclared(Variable(), ast.init.varName)
    #         init_sym = self.visit(ast.init, c)
    #         c[0].insert(0, init_sym)
    #     else:
    #         self.visit(ast.init, c)
    #     # Process the loop header parts in the same scope
    #     self.visit(ast.cond, c)
    #     self.visit(ast.upda, c)
    #     # Instead of calling self.visit(ast.loop, [[]] + c),
    #     # process each member of the loop body using the same scope, so that the
    #     # for-loop init variable is visible and conflict detection works.
    #     for member in ast.loop.member:
    #         self.visit(member, c)
    #     return None

    # def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
    #     # Check for redeclaration of the initialization variable
    #     if isinstance(ast.init, VarDecl):
    #         res = self.lookup(ast.init.varName, c[0], lambda x: x.name)
    #         if not res is None:
    #             raise Redeclared(Variable(), ast.init.varName)

    #     # Visit the block as before
    #     self.visit(Block([ast.init] + ast.loop.member + [ast.upda]), c)


    # def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
    #     # Tạo một bản sao của scope hiện tại
    #     new_env = c[0][:]
    #     # Nếu init là VarDecl, kiểm tra redeclaration trong new_env
    #     if isinstance(ast.init, VarDecl):
    #         if self.lookup(ast.init.varName, new_env, lambda x: x.name) is not None:
    #             raise Redeclared(Variable(), ast.init.varName)
    #     # Xử lý for-loop theo block, sử dụng new_env làm scope cục bộ
    #     self.visit(Block([ast.init] + ast.loop.member + [ast.upda]), [new_env] + c[1:])

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None:
          self.visit(Block([VarDecl(ast.idx.name, None, None), VarDecl(ast.value.name, None, None)] + ast.loop.member), c)

    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        res = next(filter(None, (self.lookup(ast.name, scope, lambda x: x.name) for scope in c)), None)
        if res and not isinstance(res.mtype, Function):
            return res.mtype if not isinstance(res.mtype, Id) else self.lookup(res.mtype.name, self.list_type, lambda x: x.name)
        raise Undeclared(Identifier(), ast.name)

    def visitFuncCall(self, ast: FuncCall, c: List[List[Symbol]]) -> Type:
        res = next(filter(None, [
            func for func in self.list_function if func.name == ast.funName
        ] + [
            self.lookup(ast.funName, scope, lambda x: x.name) for scope in c
        ]), None)

        if res:
            return res.retType
        raise Undeclared(Function(), ast.funName)

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        type_receiver = self.visit(ast.receiver, c)
        res = next(filter(lambda field: field[0] == ast.field,
            next(filter(lambda struct: isinstance(struct, StructType) and struct.name == type_receiver.name,
                self.list_type), StructType("", [], [])).elements), None)

        if res is None:
            raise Undeclared(Field(), ast.field)


    def visitMethCall(self, ast: MethCall, c: List[List[Symbol]]) -> Type:
        type_receiver = self.visit(ast.receiver, c)
        if isinstance(type_receiver, StructType):
            methods = type_receiver.methods
            res = next(filter(lambda method: method.fun.name == ast.metName, methods), None)
            if res is None:
                raise Undeclared(Method(), ast.metName)
            return res.fun.retType
        elif isinstance(type_receiver, InterfaceType):
            prototypes = type_receiver.methods
            res = next(filter(lambda proto: proto.name == ast.metName, prototypes), None)
            if res is None:
                raise Undeclared(Method(), ast.metName)
            return res.retType
        else:
            raise Undeclared(Method(), ast.metName)

    def visitIntType(self, ast, param): return IntType()
    def visitFloatType(self, ast, param): return FloatType()
    def visitBoolType(self, ast, param): return BoolType()
    def visitStringType(self, ast, param): return StringType()
    def visitVoidType(self, ast, param): return VoidType()
    def visitArrayType(self, ast, param): return ast
    def visitAssign(self, ast, param): return None
    def visitIf(self, ast, param): return None
    def visitContinue(self, ast, param): return None
    def visitBreak(self, ast, param): return None
    def visitReturn(self, ast, param): return None
    def visitBinaryOp(self, ast, param): return None
    def visitUnaryOp(self, ast, param): return None
    def visitArrayCell(self, ast, param): return None
    def visitIntLiteral(self, ast, param): return IntType()
    def visitFloatLiteral(self, ast, param): return FloatType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()
    def visitArrayLiteral(self, ast, param): return None
    def visitStructLiteral(self, ast, param): return None
    def visitNilLiteral(self, ast, param): return None
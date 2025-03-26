from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Tuple

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
                 # TODO: Implement
            ]
        self.function_current: FuncDecl = None

    def check(self):
        self.visit(self.ast, None)

    def visitProgram(self, ast: Program,c : None):
        def visitMethodDecl(ast: MethodDecl, c: StructType) -> MethodDecl:
            # TODO: Implement

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
                # TODO: Implement
            ]]
        )


    def visitStructType(self, ast: StructType, c : List[Union[StructType, InterfaceType]]) -> StructType:
        res = # TODO: Implement

        def visitElements(element: Tuple[str,Type], c: List[Tuple[str,Type]]) -> Tuple[str,Type]:
            # TODO: Implement

        ast.elements = reduce(lambda acc,ele: [visitElements(ele,acc)] + acc , ast.elements , [])
        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        # TODO: Implement

    def visitInterfaceType(self, ast: InterfaceType, c : List[Union[StructType, InterfaceType]]) -> InterfaceType:
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)
        ast.methods = reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.methods , [])
        return ast

    def visitFuncDecl(self, ast: FuncDecl, c : List[List[Symbol]]) -> Symbol:
        # TODO: Implement
        self.visit(ast.body, [list(reduce(lambda acc,ele: [self.visit(ele,acc)] + acc, ast.params, []))] + c)
        return # TODO: Implement

    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        # TODO: Implement
        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast: MethodDecl, c : List[List[Symbol]]) -> None:
        # TODO: Implement

    def visitVarDecl(self, ast: VarDecl, c : List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName)
        return Symbol(ast.varName, self.visit(ast.varInit, c) if ast.varInit else ast.varType, None)

    def visitConstDecl(self, ast: ConstDecl, c : List[List[Symbol]]) -> Symbol:
        # TODO: Implement

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

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None:
          self.visit(Block([VarDecl(ast.idx.name, None, None), VarDecl(ast.value.name, None, None)] + ast.loop.member), c)

    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        res = next(filter(None, # TODO: Implement), None)
        if res and not isinstance(res.mtype, Function):
            return res.mtype if not isinstance(res.mtype, Id) else # TODO: Implement
        raise Undeclared(Identifier(), ast.name)

    def visitFuncCall(self, ast: FuncCall, c: List[List[Symbol]]) -> Type:
        res = # TODO: Implement
        if res:
            return res.retType
        raise Undeclared(Function(), ast.funName)

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        type_receiver = self.visit(ast.receiver, c)
        res = # TODO: Implement
        if res is None:
            raise Undeclared(Field(), ast.field)

    def visitMethCall(self, ast: MethCall, c: List[List[Symbol]]) -> Type:
        type_receiver = self.visit(ast.receiver, c)
        res = # TODO: Implement if isinstance(type_receiver, StructType) else # TODO: Implement
        if res is None:
            raise Undeclared(Method(), ast.metName)


    def visitIntType(self, ast, param): return None
    def visitFloatType(self, ast, param): return None
    def visitBoolType(self, ast, param): return None
    def visitStringType(self, ast, param): return None
    def visitVoidType(self, ast, param): return None
    def visitArrayType(self, ast, param): return None
    def visitAssign(self, ast, param): return None
    def visitIf(self, ast, param): return None
    def visitContinue(self, ast, param): return None
    def visitBreak(self, ast, param): return None
    def visitReturn(self, ast, param): return None
    def visitBinaryOp(self, ast, param): return None
    def visitUnaryOp(self, ast, param): return None
    def visitArrayCell(self, ast, param): return None
    def visitIntLiteral(self, ast, param): return None
    def visitFloatLiteral(self, ast, param): return None
    def visitBooleanLiteral(self, ast, param): return None
    def visitStringLiteral(self, ast, param): return None
    def visitArrayLiteral(self, ast, param): return None
    def visitStructLiteral(self, ast, param): return None
    def visitNilLiteral(self, ast, param): return None
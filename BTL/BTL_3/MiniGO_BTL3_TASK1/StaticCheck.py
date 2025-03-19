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
        self.struct: list[StructType] = []
        self.inteface: list[InterfaceType] = []
        self.env = [
            [
                Symbol("getInt",MType([],IntType())),
                Symbol("putIntLn",MType([IntType()],VoidType()))
                # TODO:
            ]
        ]
        self.function_current: FuncDecl = None
        self.struct_current: StructType = None
    
    def check(self):
        return self.visit(self.ast,self.env)

    def visitProgram(self, ast: Program, c: List[List[Symbol]]):
        # TODO: Global scope

        # TODO: Function/method scope and VarDecl => self.function_current, self.struct_current

        return c
    
    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        # TODO Redeclared ParamDecl
        return Symbol(ast.parName, None, None)

    def visitVarDecl(self, ast: VarDecl, c : List[List[Symbol]]) -> Symbol:
        # TODO Redeclared Variable
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName) 
        return Symbol(ast.varName, None, None)

    def visitConstDecl(self, ast: ConstDecl, c : List[List[Symbol]]) -> Symbol:
        # TODO Redeclared Constant
        return Symbol(ast.conName, None, None)
   
    def visitFuncDecl(self, ast: FuncDecl, c : List[List[Symbol]]) -> Symbol:
        # TODO Redeclared Function
        return Symbol(ast.name, None, None)

    def visitStructType(self, ast: StructType, c) -> StructType:
         # TODO Redeclared Field
        return ast

    def visitMethodDecl(self, ast: MethodDecl, c: List[MethodDecl]) -> MethodDecl:
        # TODO Redeclared Method
        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        # TODO Redeclared Prototype
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c) -> InterfaceType:
        reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.methods , [])
        return ast

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
    def visitFuncCall(self, ast, c): return None
    def visitMethCall(self, ast, c): return None
    def visitId(self, ast, c): return None
    def visitArrayCell(self, ast, c): return None
    def visitFieldAccess(self, ast, c): return None
    def visitIntLiteral(self, ast: IntLiteral, c): return None
    def visitFloatLiteral(self, ast: FloatLiteral, c): return None
    def visitBooleanLiteral(self, ast: BooleanLiteral, c): return None
    def visitStringLiteral(self, ast: StringLiteral, c): return None
    def visitArrayLiteral(self, ast: ArrayLiteral, c): return None
    def visitStructLiteral(self, ast: StructLiteral, c):  return None
    def visitNilLiteral(self, ast: NilLiteral, c): return None
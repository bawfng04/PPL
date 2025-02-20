from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        method_name = 'visit{}'.format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self,param)

class Expr(AST):
    __metaclass__ = ABCMeta
    pass

class LHS(Expr):
    __metaclass__ = ABCMeta
    pass

@dataclass
class Id(LHS):
    name:str
    def __str__(self):
        return "Id(\"" + self.name + "\")"

class Type(AST):
    __metaclass__ = ABCMeta
    pass

class IntType(Type):
    def __str__(self):
        return "IntType()"

class FloatType(Type):
    def __str__(self):
        return "FloatType()"

class StringType(Type):
    def __str__(self):
        return "StringType()"

class BooleanType(Type):
    def __str__(self):
        return "BooleanType()"

# struct Type and interface Type

@dataclass
class ClassType(Type):
    name: Id
    def __str__(self):
        return f"ClassType({str(self.name)})"

class VoidType(Type):
    def __str__(self):
        return "VoidType()"

# used for binary expression
@dataclass
class BinaryOp(Expr):
    op:str
    left:Expr
    right:Expr
    def __str__(self):
        return "BinaryOp(\"" + self.op + "\"," + str(self.left) + "," + str(self.right) + ")"

#used for unary expression with orerand like !,+,-
@dataclass
class UnaryOp(Expr):
    op:str
    body:Expr
    def __str__(self):
        return "UnaryOp(\"" + self.op + "\"," + str(self.body) + ")"


@dataclass
class CallExpr(Expr):
    obj: Expr # None if there is no obj
    method:Id
    param:List[Expr]
    def __str__(self):
        return "CallExpr(" + ((str(self.obj) + ",") if self.obj else "None,") + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

@dataclass
class ArrayCell(LHS):
    arr:Expr
    idx:Expr
    def __str__(self):
        return "ArrayCell(" + str(self.arr) + "," + str(self.idx) + ")"

@dataclass
class FieldAccess(LHS):
    obj:Expr
    fieldname:Id
    def __str__(self):
        return "FieldAccess(" + ((str(self.obj) + ",") if self.obj else "") + str(self.fieldname) + ")"

class Literal(Expr):
    __metaclass__ = ABCMeta
    pass

@dataclass
class IntLiteral(Literal):
    value:int
    def __str__(self):
        return "IntLiteral(" + str(self.value) + ")"

@dataclass
class FloatLiteral(Literal):
    value:float
    def __str__(self):
        return "FloatLiteral(" + str(self.value) + ")"

@dataclass
class StringLiteral(Literal):
    value:str
    def __str__(self):
        return "StringLiteral(\"" + self.value + "\")"

@dataclass
class BooleanLiteral(Literal):
    value:bool
    def __str__(self):
        return "BooleanLiteral(" + str(self.value) + ")"
@dataclass
class ArrayLiteral(Literal):
    typ : Type
    dimensions : list[int]
    value: List[Expr]
    def __str__(self):
        return (f"ArrayLiteral({self.typ}, "
                f"{self.dimensions}, "
                f"value=[{', '.join(str(x) for x in self.value)}])")
@dataclass
class StructLiteral(Literal):
    name: Id
    value: List[Tuple[Id, Expr]]
    def __str__(self):
        return f"StructLiteral({self.name}, [{','.join(f'({str(id)},{str(expr)})' for id, expr in self.value)}])"

@dataclass
class NilLiteral(Literal):
    def __str__(self):
        return "NilLiteral()"

class Stmt(AST):
    __metaclass__ = ABCMeta
    pass

@dataclass
class AssignStmt(Stmt):
    lhs:LHS
    assign: str
    exp:Expr
    def __str__(self):
        return "AssignStmt(" + str(self.lhs) + ",\"" +  (self.assign) + "\"," +  str(self.exp) + ")"

@dataclass
class If(Stmt):
    expr: Expr
    thenStmt: [Stmt]
    elifStmt: [(Expr, [Stmt])] = None
    elseStmt: [Stmt] = None

    def __str__(self):
        if self.elifStmt:
            elif_str = "[" + ", ".join(f"({str(e)}, [{', '.join(str(s) for s in stmts)}])" for e, stmts in self.elifStmt) + "]"
        else:
            elif_str = "None"

        return f"If({str(self.expr)}, [{', '.join(str(s) for s in self.thenStmt)}], {elif_str}, {'[' + ', '.join(str(s) for s in self.elseStmt) + ']' if self.elseStmt else None})"

@dataclass
class For(Stmt):
    initStmt:AssignStmt or VariablesDecl
    expr:Expr
    postStmt:AssignStmt
    loop:[Stmt]
    def __str__(self):
        return "For(" + str(self.initStmt) + "," + str(self.expr) + "," + str(self.postStmt) + ",[" + ", ".join(str(s) for s in self.loop) + "])"

@dataclass
class ForArray(Stmt):
    index: Id
    value: Id
    array: Expr
    loop:[Stmt]
    def __str__(self):
        return "For(" + str(self.index) + "," + str(self.value) + "," + str(self.array) + ",[" + ", ".join(str(s) for s in self.loop) + "])"


class Break(Stmt):
    def __str__(self):
        return "Break()"

class Continue(Stmt):
    def __str__(self):
        return "Continue()"

@dataclass
class Return(Stmt):
    expr:Expr
    def __str__(self):
        return "Return(" + (str(self.expr)  if  self.expr else "None") + ")"

@dataclass
class CallStmt(Stmt):
    obj: Expr  # None if there is no obj
    method:Id
    param:List[Expr]
    def __str__(self):
        return "CallStmt(" + ((str(self.obj) + ",") if self.obj else "None,") + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

class Declared(AST):
    __metaclass__ = ABCMeta
    pass

class StoreDecl(Stmt or Declared):
    __metaclass__ = ABCMeta
    pass

@dataclass
class VariablesDecl(StoreDecl):
    variable : Id
    varType : Type = None
    varInit : Expr = None
    def __str__(self):
        return "VariablesDecl(" + str(self.variable) + ", " + ( str(self.varType) if self.varType else "None") + ", " + (str(self.varInit) if self.varInit else "None") + ")"
    def toParam(self):
        return "Param(" + str(self.variable) + "," + str(self.varType) + ")"

@dataclass
class ConstDecl(StoreDecl):
    constant : Id
    value : Expr
    def __str__(self):
        return "ConstDecl(" + str(self.constant) + "," + str(self.value) + ")"


@dataclass
class FunctionDecl(Declared):
    name: Id
    returnType: Type
    methodReceiver: VariablesDecl # function if methodReceiver  else method
    param: List[VariablesDecl]
    stmts: [Stmt]
    def __str__(self):
        return f"FunctionDecl({str(self.name)}, {str(self.returnType)}, {str(self.methodReceiver)},[{','.join(str(i) for i in self.param)}],[{', '.join(str(i) for i in self.stmts)}])"


@dataclass
class InterfaceDecl(Declared):
    name: Id
    fields: List[FunctionDecl]
    def __str__(self):
        return "InterfaceDecl(" + str(self.name) +  ",[" +  ','.join(str(i) for i in self.fields) + "])"

@dataclass
class StructDecl(Declared):
    name: Id
    fields: List[VariablesDecl]
    def __str__(self):
        return "StructDecl(" + str(self.name) +  ",[" +  ','.join(str(i) for i in self.fields) + "])"

@dataclass
class ArrayType(Type):
    typ : Type
    dimensions : list[int]
    def __str__(self):
        return (f"ArrayType({self.typ}, "
                f"{self.dimensions})")

# used for whole program
@dataclass
class Program(AST):
    decl : List[Declared]
    def __str__(self):
        return "Program([\n\t\t\t" + ',\n\t\t\t'.join(str(i) for i in self.decl) + "\n\t\t])"


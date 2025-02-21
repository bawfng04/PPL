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

class StructType(Type):
    name: Id
    def __str__(self):
        return f"StructType({str(name)})"

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

# used for whole program
@dataclass
class Program(AST):
    decl : List[Expr]
    def __str__(self):
        print("line" + str(self.decl[0]))
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
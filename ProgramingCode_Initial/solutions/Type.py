# Given the AST declarations as follows:

# class Exp(ABC): #abstract class

# class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=

# class UnOp(Exp): #op:str,e:Exp #op is -, !

# class IntLit(Exp): #val:int

# class FloatLit(Exp): #val:float

# class BoolLit(Exp): #val:bool

# and the Visitor class is declared as follows:

# class StaticCheck(Visitor):

#     def visitBinOp(self,ctx:BinOp,o): pass

#     def visitUnOp(self,ctx:UnOp,o):pass

#     def visitIntLit(self,ctx:IntLit,o): pass

#     def visitFloatLit(self,ctx,o): pass

#     def visitBoolLit(self,ctx,o): pass

# Rewrite the body of the methods in class StaticCheck to check the following type constraints:

# + , - and * accept their operands in int or float type and return float type if at least one of their operands is in float type, otherwise, return int type
# / accepts their operands in int or float type and returns float type
# !, && and || accept their operands in bool type and return bool type
# >, <, == and != accept their operands in any type but must in the same type and return bool type
# If the expression does not conform the type constraints, the StaticCheck will raise exception TypeMismatchInExpression with the innermost sub-expression that contains type mismatch.
# Your code starts at line 55

# For example:

# Test	Result
# BinOp("+",IntLit(3),BoolLit(True))
# Type Mismatch In Expression: BinOp("+",IntLit(3),BoolLit(True))


class Exp(ABC): #abstract class
    pass
class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=
    pass
class UnOp(Exp): #op:str,e:Exp #op is -, !
    pass
class IntLit(Exp): #val:int
    pass
class FloatLit(Exp): #val:float
    pass
class BoolLit(Exp): #val:bool
    pass
class Visitor(ABC):
    pass


# 1
class StaticCheck(Visitor):
    def visitBinOp(self,ctx:BinOp,o):
        e1type = self.visit(ctx.e1, o)
        e2type = self.visit(ctx.e2, o)
        op = ctx.op
        # + , - and * accept their operands in int or float type and return float type if at least one of their operands is in float type, otherwise, return int type
        if op == '+' or op == '-' or op == '*':
            if e1type == '_bool' or e2type == '_bool':
                raise TypeMismatchInExpression(ctx)
            if e1type == '_int' and e2type == '_int':
                return '_int'
            else:
                return '_float'
        # / accepts their operands in int or float type and returns float type
        if op == '/':
            if e1type == '_bool' or e2type == '_bool':
                raise TypeMismatchInExpression(ctx)
            return '_float'
        # && and || accept their operands in bool type and return bool type
        if op == '&&' or op == '||':
            if e1type != '_bool' or e2type != '_bool':
                raise TypeMismatchInExpression(ctx)
            return '_bool'
        # >, <, == and != accept their operands in any type but must in the same type and return bool type
        if op == '>' or op == '<' or op == '==' or op == '!=':
            if e1type != e2type:
                raise TypeMismatchInExpression(ctx)
            return '_bool'

    def visitUnOp(self, ctx:UnOp, o):
        etype = self.visit(ctx.e, o)
        op = ctx.op

        # ! accepts operand in bool type and returns bool type
        if op == '!':
            if etype != '_bool':
                raise TypeMismatchInExpression(ctx)
            return '_bool'

        # - accepts operand in int or float type and returns the same type
        if op == '-':
            if etype == '_bool':
                raise TypeMismatchInExpression(ctx)
            return etype


    def visitIntLit(self,ctx:IntLit,o):
        return '_int'

    def visitFloatLit(self,ctx,o):
        return '_float'

    def visitBoolLit(self,ctx,o):
        return '_bool'



# 2
# Given the AST declarations as follows:

# class Program: #decl:List[VarDecl],exp:Exp

# class VarDecl: #name:str,typ:Type

# class Type(ABC): #abstract class

# class IntType(Type)

# class FloatType(Type)

# class BoolType(Type)

# class Exp(ABC): #abstract class

# class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=

# class UnOp(Exp): #op:str,e:Exp #op is -, !

# class IntLit(Exp): #val:int

# class FloatLit(Exp): #val:float

# class BoolLit(Exp): #val:bool

# class Id(Exp): #name:str

# and the Visitor class is declared as follows:

# class StaticCheck(Visitor):

#     def visitProgram(self,ctx:Program,o):pass

#     def visitVarDecl(self,ctx:VarDecl,o): pass

#     def visitIntType(self,ctx:IntType,o):pass

#     def visitFloatType(self,ctx:FloatType,o):pass

#     def visitBoolType(self,ctx:BoolType,o):pass

#     def visitBinOp(self,ctx:BinOp,o): pass

#     def visitUnOp(self,ctx:UnOp,o):pass

#     def visitIntLit(self,ctx:IntLit,o): pass

#     def visitFloatLit(self,ctx,o): pass

#     def visitBoolLit(self,ctx,o): pass

#     def visitId(self,ctx,o): pass

# Rewrite the body of the methods in class StaticCheck to check the following type constraints:

# + , - and * accept their operands in int or float type and return float type if at least one of their operands is in float type, otherwise, return int type
# / accepts their operands in int or float type and returns float type
# !, && and || accept their operands in bool type and return bool type
# >, <, == and != accept their operands in any type but must in the same type and return bool type
# the type of an Id is from the declarations, if the Id is not in the declarations, exception UndeclaredIdentifier should be raised with the name of the Id.
# If the expression does not conform the type constraints, the StaticCheck will raise exception TypeMismatchInExpression with the innermost sub-expression that contains type mismatch.
# Your code starts at line 90

# For example:

# Test	Result
# Program([VarDecl("x",IntType())],BinOp("*",BinOp("+",Id("x"),FloatLit(3.4)),BinOp(">",IntLit(3),FloatLit(2.1))))
# Type Mismatch In Expression: BinOp(">",IntLit(3),FloatLit(2.1))

class StaticCheck(Visitor):
    def visitProgram(self, ctx:Program, o):
        env = [] # dạng [(name, type)] - [(a, '_int'), (b, '_float')]
        for decl in ctx.decl:
            env = self.visit(decl, env)
        return self.visit(ctx.exp, env)

    def visitVarDecl(self, ctx:VarDecl, o):
        # thêm (name, type) vào env
        typ = self.visit(ctx.typ, o)
        return o + [(ctx.name, typ)]

    def visitIntType(self, ctx:IntType, o):
        return '_int'

    def visitFloatType(self, ctx:FloatType, o):
        return '_float'

    def visitBoolType(self, ctx:BoolType, o):
        return '_bool'

    def visitBinOp(self, ctx:BinOp, o):
        e1type = self.visit(ctx.e1, o)
        e2type = self.visit(ctx.e2, o)
        op = ctx.op

        # + , - and * accept their operands in int or float type and return float type if at least one of their operands is in float type, otherwise, return int type
        if op == '+' or op == '-' or op == '*':
            if e1type == '_bool' or e2type == '_bool':
                raise TypeMismatchInExpression(ctx)
            if e1type == '_int' and e2type == '_int':
                return '_int'
            else:
                return '_float'

        # / accepts their operands in int or float type and returns float type
        if op == '/':
            if e1type == '_bool' or e2type == '_bool':
                raise TypeMismatchInExpression(ctx)
            return '_float'

        # && and || accept their operands in bool type and return bool type
        if op == '&&' or op == '||':
            if e1type != '_bool' or e2type != '_bool':
                raise TypeMismatchInExpression(ctx)
            return '_bool'

        # >, <, == and != accept their operands in any type but must in the same type and return bool type
        if op == '>' or op == '<' or op == '==' or op == '!=':
            if e1type != e2type:
                raise TypeMismatchInExpression(ctx)
            return '_bool'

    def visitUnOp(self, ctx:UnOp, o):
        etype = self.visit(ctx.e, o)
        op = ctx.op

        # ! accepts operand in bool type and returns bool type
        if op == '!':
            if etype != '_bool':
                raise TypeMismatchInExpression(ctx)
            return '_bool'

        # - accepts operand in int or float type and returns the same type
        if op == '-':
            if etype == '_bool':
                raise TypeMismatchInExpression(ctx)
            return etype

    def visitIntLit(self, ctx:IntLit, o):
        return '_int'

    def visitFloatLit(self, ctx, o):
        return '_float'

    def visitBoolLit(self, ctx, o):
        return '_bool'

    def visitId(self, ctx, o):
        # Tìm id trong env
        for name, typ in o:
            if name == ctx.name:
                return typ
        raise UndeclaredIdentifier(ctx.name)



# 3
# Given the AST declarations as follows:

# class Program: #decl:List[VarDecl],stmts:List[Assign]

# class VarDecl: #name:str

# class Assign: #lhs:Id,rhs:Exp

# class Exp(ABC): #abstract class

# class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b

# class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor

# class IntLit(Exp): #val:int

# class FloatLit(Exp): #val:float

# class BoolLit(Exp): #val:bool

# class Id(Exp): #name:str

# and the Visitor class is declared as follows:

# class StaticCheck(Visitor):

#     def visitProgram(self,ctx:Program,o):pass

#     def visitVarDecl(self,ctx:VarDecl,o): pass

#     def visitAssign(self,ctx:Assign,o): pass

#     def visitBinOp(self,ctx:BinOp,o): pass

#     def visitUnOp(self,ctx:UnOp,o):pass

#     def visitIntLit(self,ctx:IntLit,o): pass

#     def visitFloatLit(self,ctx,o): pass

#     def visitBoolLit(self,ctx,o): pass

#     def visitId(self,ctx,o): pass

# Rewrite the body of the methods in class StaticCheck to infer the type of identifiers and check the following type constraints:

# + , - , *, / accept their operands in int type and return int type
# +., -., *., /. accept their operands in float type and return float type
# > and = accept their operands in int type and return bool type
# >. and =. accept their operands in float type and return bool type
# !, &&, ||, >b and =b accept their operands in bool type and return bool type
# i2f accepts its operand in int type and return float type
# floor accept its operand in float type and return int type
# In an Assign, the type of lhs must be the same as that of rhs, otherwise, the exception TypeMismatchInStatement should be raised together with the Assign
# the type of an Id is inferred from the above constraints in the first usage,
# if the Id is not in the declarations, exception UndeclaredIdentifier should be raised together with the name of the Id, or
# If the Id cannot be inferred in the first usage, exception TypeCannotBeInferred should be raised together with the name of the identifier
# If the expression does not conform the type constraints, the StaticCheck will raise exception TypeMismatchInExpression with the assign statement where contains the type-unresolved identifier.
# Your code starts at line 95

# For example:

# Test	Result
# Program([VarDecl("x")],[Assign(Id("x"),BinOp("*",BinOp("+",Id("x"),IntLit(3.4)),BinOp("-",Id("x"),FloatLit(2.1))))])
# Type Mismatch In Expression: BinOp("-",Id("x"),FloatLit(2.1))
# Program([VarDecl("x"),VarDecl("y"),VarDecl("z")],[Assign(Id("x"),BinOp(">b",BinOp("&&",Id("x"),Id("y")),BinOp("||",BoolLit(False),BinOp(">",Id("z"),IntLit(3))))),Assign(Id("z"),Id("x"))])
# Type Mismatch In Statement: Assign(Id("z"),Id("x"))
# Program([VarDecl("x"),VarDecl("y")],[Assign(Id("x"),Id("y"))])
# Type Cannot Be Inferred: Assign(Id("x"),Id("y"))




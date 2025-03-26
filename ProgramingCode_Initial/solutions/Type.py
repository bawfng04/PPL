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



# class StaticCheck(Visitor):

#     def visitProgram(self, ctx: Program, o):
#         o = {}
#         for decl in ctx.decl:
#             self.visit(decl, o)
#         for stmt in ctx.stmts:
#             self.visit(stmt, o)

#     def visitVarDecl(self, ctx: VarDecl, o):
#         o[ctx.name] = "None"

#     def visitAssign(self, ctx: Assign, o):
#         lhs = self.visit(ctx.lhs, o)
#         rhs = self.visit(ctx.rhs, o)
#         if lhs == "None":
#             if rhs == "None":
#                 raise TypeCannotBeInferred(ctx)
#             else:
#                 o[ctx.lhs.name] = rhs
#                 lhs = rhs
#         if rhs == "None":
#             if lhs == "None":
#                 raise TypeCannotBeInferred(ctx)
#             o[ctx.rhs.name] = lhs
#             rhs = lhs
#         if lhs != rhs:
#             raise TypeMismatchInStatement(ctx)

#     def visitBinOp(self, ctx: BinOp, o):
#         ltype = self.visit(ctx.e1, o)
#         rtype = self.visit(ctx.e2, o)
#         if ctx.op in ["+", "-", "*", "/"]:
#             if ltype == "None":
#                 o[ctx.e1.name] = "_int"
#                 ltype = "_int"
#             if rtype == "None":
#                 o[ctx.e2.name] = "_int"
#                 rtype = "_int"
#             if ltype == "_int" and rtype == "_int":
#                 return "_int"
#             raise TypeMismatchInExpression(ctx)
#         if ctx.op in ["+.", "-.", "*.", "/."]:
#             if ltype == "None":
#                 o[ctx.e1.name] = "_float"
#                 ltype = "_float"
#             if rtype == "None":
#                 o[ctx.e2.name] = "_float"
#                 rtype = "_float"
#             if ltype == "_float" and rtype == "_float":
#                 return "_float"
#             raise TypeMismatchInExpression(ctx)
#         if ctx.op in [">", "="]:
#             if ltype == "None":
#                 o[ctx.e1.name] = "_int"
#                 ltype = "_int"
#             if rtype == "None":
#                 o[ctx.e2.name] = "_int"
#                 rtype = "_int"
#             if ltype == "_int" and rtype == "_int":
#                 return "_bool"
#             raise TypeMismatchInExpression(ctx)
#         if ctx.op in [">.", "=."]:
#             if ltype == "None":
#                 o[ctx.e1.name] = "_float"
#                 ltype = "_float"
#             if rtype == "None":
#                 o[ctx.e2.name] = "_float"
#                 rtype = "_float"
#             if ltype == "_float" and rtype == "_float":
#                 return "_bool"
#             raise TypeMismatchInExpression(ctx)
#         if ctx.op in ["&&", "||", ">b", "=b"]:
#             if ltype == "None":
#                 o[ctx.e1.name] = "_bool"
#                 ltype = "_bool"
#             if rtype == "None":
#                 o[ctx.e2.name] = "_bool"
#                 rtype = "_bool"
#             if ltype == "_bool" and rtype == "_bool":
#                 return "_bool"
#             raise TypeMismatchInExpression(ctx)

#     def visitUnOp(self, ctx: UnOp, o):
#         typ = self.visit(ctx.e, o)
#         if ctx.op == "-":
#             if typ == "None":
#                 o[ctx.e.name] = "_int"
#                 typ = "_int"
#             if typ == "_int":
#                 return "_int"
#             raise TypeMismatchInExpression(ctx)
#         if ctx.op == "-.":
#             if typ == "None":
#                 o[ctx.e.name] = "_float"
#                 typ = "_float"
#             if typ == "_float":
#                 return "_float"
#             raise TypeMismatchInExpression(ctx)
#         if ctx.op == "!":
#             if typ == "None":
#                 o[ctx.e.name] = "_bool"
#                 typ = "_bool"
#             if typ == "_bool":
#                 return "_bool"
#             raise TypeMismatchInExpression(ctx)
#         if ctx.op == "i2f":
#             if typ == "None":
#                 o[ctx.e.name] = "_int"
#                 typ = "_int"
#             if typ == "_int":
#                 return "_float"
#             raise TypeMismatchInExpression(ctx)
#         if ctx.op == "_floor":
#             if typ == "None":
#                 o[ctx.e.name] = "_float"
#                 typ = "_float"
#             if typ == "_float":
#                 return "_int"
#             raise TypeMismatchInExpression(ctx)

#     def visitIntLit(self, ctx: IntLit, o):
#         return "_int"

#     def visitFloatLit(self, ctx, o):
#         return "_float"

#     def visitBoolLit(self, ctx, o):
#         return "_bool"

#     def visitId(self, ctx: Id, o):
#         if ctx.name in o:
#             return o[ctx.name]
#         raise UndeclaredIdentifier(ctx.name)

class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o = {}
        for decl in ctx.decl:
            self.visit(decl,o)
        for stmt in ctx.stmts:
            self.visit(stmt,o)

    def visitVarDecl(self,ctx:VarDecl,o):
        o[ctx.name] = "none"

    def visitAssign(self,ctx:Assign,o):
        rhs = self.visit(ctx.rhs,o)
        lhs = self.visit(ctx.lhs, o)
        if lhs == "none":
            if rhs == "none":
                raise TypeCannotBeInferred(ctx)
            else:
                o[ctx.lhs.name] = rhs
                lhs = rhs
        if rhs == "none":
            if lhs == "none":
                raise TypeCannotBeInferred(ctx)
            o[ctx.rhs.name] = lhs
            rhs=lhs
        if lhs != rhs:
            raise TypeMismatchInStatement(ctx)


    def visitBinOp(self,ctx:BinOp,o):
        ltype = self.visit(ctx.e1,o)
        rtype = self.visit(ctx.e2,o)

        if ctx.op in ["+", "-", "*", "/"]:
            if ltype == "none":
                o[ctx.e1.name] = "int"
                ltype = "int"
            if rtype == "none":
                o[ctx.e2.name] = "int"
                rtype = "int"
            if ltype == "int" and rtype == "int":
                return "int"
            raise TypeMismatchInExpression(ctx)
        if ctx.op in ["+.", "-.", "*.", "/."]:
            if ltype == "none":
                o[ctx.e1.name] = "float"
                ltype = "float"
            if rtype == "none":
                o[ctx.e2.name] = "float"
                rtype = "float"
            if ltype == "float" and rtype == "float":
                return "float"
            raise TypeMismatchInExpression(ctx)
        if ctx.op in [">","="]:
            if ltype == "none":
                o[ctx.e1.name] = "int"
                ltype = "int"
            if rtype == "none":
                o[ctx.e2.name] = "int"
                rtype = "int"
            if ltype == "int" and rtype == "int":
                return "bool"
            raise TypeMismatchInExpression(ctx)
        if ctx.op in [">.", "=."]:
            if ltype == "none":
                o[ctx.e1.name] = "float"
                ltype = "float"
            if rtype == "none":
                o[ctx.e2.name] = "float"
                rtype = "float"
            if ltype == "float" and rtype == "float":
                return "bool"
            raise TypeMismatchInExpression(ctx)
        if ctx.op in ["&&", "||", ">b", "=b"]:
            if ltype == "none":
                o[ctx.e1.name] = "bool"
                ltype = "bool"
            if rtype == "none":
                o[ctx.e2.name] = "bool"
                rtype = "bool"
            if ltype == "bool" and rtype == "bool":
                return "bool"
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        typ = self.visit(ctx.e,o)
        if ctx.op == "-":
            if typ == "none":
                o[ctx.e.name] = "int"
                typ = "int"
            if typ == "int":
                return "int"
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "-.":
            if typ == "none":
                o[ctx.e.name] = "float"
                typ = "float"
            if typ == "float":
                return "float"
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "!":
            if typ == "none":
                o[ctx.e.name] = "bool"
                typ = "bool"
            if typ == "bool":
                return "bool"
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "i2f":
            if typ == "none":
                o[ctx.e.name] = "int"
                typ = "int"
            if typ == "int":
                return "float"
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "floor":
            if typ == "none":
                o[ctx.e.name] = "float"
                typ = "float"
            if typ == "float":
                return "int"
            raise TypeMismatchInExpression(ctx)

    def visitIntLit(self,ctx:IntLit,o):
        return "int"

    def visitFloatLit(self,ctx,o):
        return "float"

    def visitBoolLit(self,ctx,o):
        return "bool"

    def visitId(self,ctx,o):
        if ctx.name in o:
            return o[ctx.name]
        raise UndeclaredIdentifier(ctx.name)


# 4

# Given the AST declarations as follows:

# class Program: #decl:List[VarDecl],stmts:List[Stmt]

# class VarDecl: #name:str

# class Stmt(ABC): #abstract class

# class Block(Stmt): #decl:List[VarDecl],stmts:List[Stmt]

# class Assign(Stmt): #lhs:Id,rhs:Exp

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

#     def visitBlock(self,ctx:Block,o): pass

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
# In an assignment statement, the type of lhs must be the same as that of rhs, otherwise, the exception TypeMismatchInStatement should be raised together with the assignment statement.
# the type of an Id is inferred from the above constraints in the first usage,
# if the Id is not in the declarations, exception UndeclaredIdentifier should be raised together with the name of the Id, or
# If the Id cannot be inferred in the first usage, exception TypeCannotBeInferred should be raised together with the assignment statement which contains the type-unresolved identifier.
# For static referencing environment, this language applies the scope rules of block-structured programming language. When there is a declaration duplication of a name in a scope, exception Redeclared should be raised together with the second declaration.
# If an expression does not conform the type constraints, the StaticCheck will raise exception TypeMismatchInExpression with the expression.
# Your code starts at line 110

# For example:

# Test	Result
# Program([VarDecl("x")],[Assign(Id("x"),IntLit(3)),Block([VarDecl("y")],[Assign(Id("x"),Id("y")),Assign(Id("y"),BoolLit(True))])])
# Type Mismatch In Statement: Assign(Id("y"),BoolLit(True))

class StaticCheck(Visitor):
    def visitProgram(self, ctx:Program, o):
        # Create initial environment
        env = [{}]  # List of dictionaries for different scopes
        for decl in ctx.decl:
            self.visit(decl, env)
        for stmt in ctx.stmts:
            self.visit(stmt, env)

    def visitVarDecl(self, ctx:VarDecl, o):
        # Check for redeclaration in current scope
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        # Add to current scope with "none" type (not yet inferred)
        o[0][ctx.name] = "none"

    def visitBlock(self, ctx:Block, o):
        # Create new scope
        o.insert(0, {})
        # Process declarations
        for decl in ctx.decl:
            self.visit(decl, o)
        # Process statements
        for stmt in ctx.stmts:
            self.visit(stmt, o)
        # Remove the scope when exiting the block
        o.pop(0)

    def visitAssign(self, ctx:Assign, o):
        # Visit rhs first to get its type
        rhs_type = self.visit(ctx.rhs, o)
        lhs_type = self.visit(ctx.lhs, o)

        # Handle type inference
        if lhs_type == "none":
            if rhs_type == "none":
                raise TypeCannotBeInferred(ctx)
            # Update identifier type in the first scope it appears
            self.updateType(ctx.lhs.name, rhs_type, o)
            lhs_type = rhs_type

        if rhs_type == "none":
            if lhs_type == "none":
                raise TypeCannotBeInferred(ctx)
            # Update identifier type in the first scope it appears
            self.updateType(ctx.rhs.name, lhs_type, o)
            rhs_type = lhs_type

        # Check type matching
        if lhs_type != rhs_type:
            raise TypeMismatchInStatement(ctx)

    def updateType(self, name, typ, o):
        # Update type in the first scope where the name is found
        for scope in o:
            if name in scope:
                scope[name] = typ
                return

    def visitBinOp(self, ctx:BinOp, o):
        # Process left and right operands
        ltype = self.visit(ctx.e1, o)
        rtype = self.visit(ctx.e2, o)

        # Int operators: +, -, *, /
        if ctx.op in ["+", "-", "*", "/"]:
            if ltype == "none" and isinstance(ctx.e1, Id):
                self.updateType(ctx.e1.name, "int", o)
                ltype = "int"
            if rtype == "none" and isinstance(ctx.e2, Id):
                self.updateType(ctx.e2.name, "int", o)
                rtype = "int"
            if ltype == "int" and rtype == "int":
                return "int"
            raise TypeMismatchInExpression(ctx)

        # Float operators: +., -., *., /.
        if ctx.op in ["+.", "-.", "*.", "/."]:
            if ltype == "none" and isinstance(ctx.e1, Id):
                self.updateType(ctx.e1.name, "float", o)
                ltype = "float"
            if rtype == "none" and isinstance(ctx.e2, Id):
                self.updateType(ctx.e2.name, "float", o)
                rtype = "float"
            if ltype == "float" and rtype == "float":
                return "float"
            raise TypeMismatchInExpression(ctx)

        # Int comparison: >, =
        if ctx.op in [">", "="]:
            if ltype == "none" and isinstance(ctx.e1, Id):
                self.updateType(ctx.e1.name, "int", o)
                ltype = "int"
            if rtype == "none" and isinstance(ctx.e2, Id):
                self.updateType(ctx.e2.name, "int", o)
                rtype = "int"
            if ltype == "int" and rtype == "int":
                return "bool"
            raise TypeMismatchInExpression(ctx)

        # Float comparison: >., =.
        if ctx.op in [">.", "=."]:
            if ltype == "none" and isinstance(ctx.e1, Id):
                self.updateType(ctx.e1.name, "float", o)
                ltype = "float"
            if rtype == "none" and isinstance(ctx.e2, Id):
                self.updateType(ctx.e2.name, "float", o)
                rtype = "float"
            if ltype == "float" and rtype == "float":
                return "bool"
            raise TypeMismatchInExpression(ctx)

        # Boolean operators: &&, ||, >b, =b
        if ctx.op in ["&&", "||", ">b", "=b"]:
            if ltype == "none" and isinstance(ctx.e1, Id):
                self.updateType(ctx.e1.name, "bool", o)
                ltype = "bool"
            if rtype == "none" and isinstance(ctx.e2, Id):
                self.updateType(ctx.e2.name, "bool", o)
                rtype = "bool"
            if ltype == "bool" and rtype == "bool":
                return "bool"
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx:UnOp, o):
        # Get operand type
        etype = self.visit(ctx.e, o)

        # Integer negation: -
        if ctx.op == "-":
            if etype == "none" and isinstance(ctx.e, Id):
                self.updateType(ctx.e.name, "int", o)
                etype = "int"
            if etype == "int":
                return "int"
            raise TypeMismatchInExpression(ctx)

        # Float negation: -.
        if ctx.op == "-.":
            if etype == "none" and isinstance(ctx.e, Id):
                self.updateType(ctx.e.name, "float", o)
                etype = "float"
            if etype == "float":
                return "float"
            raise TypeMismatchInExpression(ctx)

        # Logical not: !
        if ctx.op == "!":
            if etype == "none" and isinstance(ctx.e, Id):
                self.updateType(ctx.e.name, "bool", o)
                etype = "bool"
            if etype == "bool":
                return "bool"
            raise TypeMismatchInExpression(ctx)

        # Int to float conversion: i2f
        if ctx.op == "i2f":
            if etype == "none" and isinstance(ctx.e, Id):
                self.updateType(ctx.e.name, "int", o)
                etype = "int"
            if etype == "int":
                return "float"
            raise TypeMismatchInExpression(ctx)

        # Floor function: floor
        if ctx.op == "floor":
            if etype == "none" and isinstance(ctx.e, Id):
                self.updateType(ctx.e.name, "float", o)
                etype = "float"
            if etype == "float":
                return "int"
            raise TypeMismatchInExpression(ctx)

    def visitIntLit(self, ctx:IntLit, o):
        return "int"

    def visitFloatLit(self, ctx, o):
        return "float"

    def visitBoolLit(self, ctx, o):
        return "bool"

    def visitId(self, ctx, o):
        # Search for the name in all scopes, from innermost to outermost
        for scope in o:
            if ctx.name in scope:
                return scope[ctx.name]
        # If not found, raise exception
        raise UndeclaredIdentifier(ctx.name)

# 5
# Given the AST declarations as follows:

# class Program: #decl:List[Decl],stmts:List[Stmt]

# class Decl(ABC): #abstract class

# class VarDecl(Decl): #name:str

# class FuncDecl(Decl): #name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]

# class Stmt(ABC): #abstract class

# class Assign(Stmt): #lhs:Id,rhs:Exp

# class CallStmt(Stmt): #name:str,args:List[Exp]

# class Exp(ABC): #abstract class

# class IntLit(Exp): #val:int

# class FloatLit(Exp): #val:float

# class BoolLit(Exp): #val:bool

# class Id(Exp): #name:str

# and the Visitor class is declared as follows:

# class StaticCheck(Visitor):

#     def visitProgram(self,ctx:Program,o):pass

#     def visitVarDecl(self,ctx:VarDecl,o): pass

#     def visitFuncDecl(self,ctx:FuncDecl,o): pass

#     def visitCallStmt(self,ctx:CallStmt,o):pass

#     def visitAssign(self,ctx:Assign,o): pass

#     def visitIntLit(self,ctx:IntLit,o): pass

#     def visitFloatLit(self,ctx,o): pass

#     def visitBoolLit(self,ctx,o): pass

#     def visitId(self,ctx,o): pass

# Rewrite the body of the methods in class StaticCheck to infer the type of identifiers and check the following type constraints:

# In an Assign, the type of lhs must be the same as that of rhs, otherwise, the exception TypeMismatchInStatement should be raised together with the Assign
# the type of an Id is inferred from the above constraints in the first usage,
# if the Id is not in the declarations, exception UndeclaredIdentifier should be raised together with the name of the Id, or
# If the Id cannot be inferred in the first usage, exception TypeCannotBeInferred should be raised together with the statement
# For static referencing environment, this language applies the scope rules of block-structured programming language where a function is a block. When there is a declaration duplication of a name in a scope, exception Redeclared should be raised together with the second declaration.
# In a call statement, the argument type must be the same as the parameter type. If there is no function declaration in the static referencing environment, exception UndeclaredIdentifier should be raised together with the function call name. If the numbers of parameters and arguments are not the same or at least one argument type is not the same as the type of the corresponding parameter, exception TypeMismatchInStatement should be raise with the call statement. If there is at least one parameter type cannot be resolved, exception TypeCannotBeInferred should be raised together with the call statement.
# Your code starts at line 120

# For example:

# Test	Result
# Program([VarDecl("x"),FuncDecl("foo",[VarDecl("x")],[],[Assign(Id("x"),FloatLit(2))])],[Assign(Id("x"),IntLit(3)),CallStmt("foo",[Id("x")])])
# Type Mismatch In Statement: CallStmt("foo",[Id("x")])
# Program([VarDecl("x"),FuncDecl("foo",[VarDecl("y"),VarDecl("z")],[],[])],[CallStmt("foo",[IntLit(3),Id("x")])])
# Type Cannot Be Inferred: CallStmt("foo",[IntLit(3),Id("x")])

class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o):
        # Environment contains both variable and function information
        # For variables: {name: type}
        # For functions: {name: {'params': [(param_name, param_type)], 'return': return_type}}
        env = [{}]

        # First pass: Process all declarations to handle function references
        for decl in ctx.decl:
            if isinstance(decl, VarDecl):
                self.visitVarDecl(decl, env)
            elif isinstance(decl, FuncDecl):
                self.visitFuncDecl(decl, env)

        # Second pass: Process all statements
        for stmt in ctx.stmts:
            self.visit(stmt, env)

    def visitVarDecl(self, ctx: VarDecl, o):
        # Check for redeclaration in current scope
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        # Add to current scope with "none" type (not yet inferred)
        o[0][ctx.name] = "none"
        return o

    def visitFuncDecl(self, ctx: FuncDecl, o):
        # Check for redeclaration
        if ctx.name in o[0]:
            raise Redeclared(ctx)

        # Create function entry with parameter information
        # Each parameter starts with "none" type
        params = []
        for param in ctx.param:
            params.append((param.name, "none"))

        # Store function in environment
        o[0][ctx.name] = {"params": params}

        # Create new scope for function body
        local_env = [{}] + o

        # Add parameters to function's local scope
        for param_name, _ in params:
            local_env[0][param_name] = "none"

        # Process local declarations
        for decl in ctx.local:
            self.visit(decl, local_env)

        # Process function statements to infer types
        for stmt in ctx.stmts:
            self.visit(stmt, local_env)

        # Update parameter types in function definition
        for i, (param_name, _) in enumerate(params):
            if param_name in local_env[0]:
                params[i] = (param_name, local_env[0][param_name])

        # Update function entry with inferred parameter types
        o[0][ctx.name]["params"] = params

        return o

    def visitCallStmt(self, ctx: CallStmt, o):
        # Check if function exists
        found = False
        func_info = None

        for scope in o:
            if ctx.name in scope and isinstance(scope[ctx.name], dict) and "params" in scope[ctx.name]:
                found = True
                func_info = scope[ctx.name]
                break

        if not found:
            raise UndeclaredIdentifier(ctx.name)

        # Check number of arguments match number of parameters
        if len(ctx.args) != len(func_info["params"]):
            raise TypeMismatchInStatement(ctx)

        # Evaluate argument types
        arg_types = []
        for arg in ctx.args:
            arg_types.append(self.visit(arg, o))

        # Check if all parameter types are inferred
        param_types = [param_type for _, param_type in func_info["params"]]

        if "none" in param_types:
            # If there's a parameter without a type, try to infer from the arguments
            for i, (param_name, param_type) in enumerate(func_info["params"]):
                if param_type == "none" and arg_types[i] != "none":
                    # Update the parameter type from the argument
                    for scope in o:
                        if ctx.name in scope and isinstance(scope[ctx.name], dict):
                            new_params = list(scope[ctx.name]["params"])
                            new_params[i] = (param_name, arg_types[i])
                            scope[ctx.name]["params"] = new_params
                            break

            # Re-check if all parameters have types now
            param_types = [param_type for _, param_type in func_info["params"]]
            if "none" in param_types:
                raise TypeCannotBeInferred(ctx)

        # Check that argument types match parameter types
        for i, arg_type in enumerate(arg_types):
            param_name, param_type = func_info["params"][i]

            if arg_type == "none" and isinstance(ctx.args[i], Id):
                # If argument is an Id with unknown type, infer from parameter
                for scope in o:
                    if ctx.args[i].name in scope:
                        scope[ctx.args[i].name] = param_type
                        break
            elif arg_type != param_type and not (arg_type == "none" or param_type == "none"):
                raise TypeMismatchInStatement(ctx)

    def visitAssign(self, ctx: Assign, o):
        rhs_type = self.visit(ctx.rhs, o)
        lhs_type = self.visit(ctx.lhs, o)

        # Handle type inference
        if lhs_type == "none":
            if rhs_type == "none":
                raise TypeCannotBeInferred(ctx)
            # Update LHS type
            for scope in o:
                if ctx.lhs.name in scope:
                    scope[ctx.lhs.name] = rhs_type
                    lhs_type = rhs_type
                    break

        if rhs_type == "none" and isinstance(ctx.rhs, Id):
            if lhs_type == "none":
                raise TypeCannotBeInferred(ctx)
            # Update RHS type
            for scope in o:
                if ctx.rhs.name in scope:
                    scope[ctx.rhs.name] = lhs_type
                    rhs_type = lhs_type
                    break

        # Check type matching
        if lhs_type != rhs_type:
            raise TypeMismatchInStatement(ctx)

    def visitIntLit(self, ctx: IntLit, o):
        return "int"

    def visitFloatLit(self, ctx, o):
        return "float"

    def visitBoolLit(self, ctx, o):
        return "bool"

    def visitId(self, ctx, o):
        # Search for the name in all scopes, from innermost to outermost
        for scope in o:
            if ctx.name in scope and not isinstance(scope[ctx.name], dict):
                return scope[ctx.name]

        # If not found, raise exception
        raise UndeclaredIdentifier(ctx.name)
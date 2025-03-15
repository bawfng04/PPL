# Let AST of a programming language be defined as follows:

# class Program: #decl:List[Decl]

# class Decl(ABC): #abstract class

# class VarDecl(Decl): #name:str,typ:Type

# class ConstDecl(Decl): #name:str,val:Lit

# class Type(ABC): #abstract class

# class IntType(Type)

# class FloatType(Type)

# class Lit(ABC): #abstract class

# class IntLit(Lit): #val:int

# and exception RedeclaredDeclaration:

# class RedeclaredDeclaration(Exception): #name:str

# Implement the methods of the following class Visitor to travel on the above ASST to detect redeclared declarations (throw exception RedeclaredDeclaration):

# class StaticCheck(Visitor):

#     def visitProgram(self,ctx:Program,o:object): pass

#     def visitVarDecl(self,ctx:VarDecl,o:object):pass

#     def visitConstDecl(self,ctx:ConstDecl,o:object):pass

#     def visitIntType(self,ctx:IntType,o:object):pass

#     def visitFloatType(self,ctx:FloatType,o:object):pass

#     def visitIntLit(self,ctx:IntLit,o:object):pass

# Your code starts at line 40

# For example:

# Test	Result
# x = Program([VarDecl("a",IntType()),ConstDecl("b",IntLit(3)),VarDecl("a",FloatType())])
# a

# 1

class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object):
        o = []
        for i in ctx.decl:
            self.visit(i, o)

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        else:
            o.append(ctx.name)

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        else:
            o.append(ctx.name)

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass


# 2
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object):
        o = []
        for i in ctx.decl:
            self.visit(i, o)

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        else:
            o.append(ctx.name)

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        else:
            o.append(ctx.name)

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass


# 3
class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        o = []
        for a in ctx.decl:
            self.visit(a, o)

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        o.append(ctx.name)

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        o.append(ctx.name)

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        o.append(ctx.name)
        new_scope = []
        for param in ctx.param:
            self.visit(param, new_scope)
        for decl in ctx.body:
            self.visit(decl, new_scope)

    def visitIntType(self, ctx: IntType, o: object):
        return ctx

    def visitFloatType(self, ctx: FloatType, o: object):
        return ctx

    def visitIntLit(self, ctx: IntLit, o: object):
        return ctx




# 4

class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o: object):
        # Tạo list rỗng
        env = [set()] #scope trong cùng nằm ở vị trí 0
        for decl in ctx.decl:
            self.visit(decl, env)

    def visitVarDecl(self, ctx: VarDecl, o: list):
        # Check redeclaration only in the current scope (innermost set)
        if ctx.name in o[0]: #o[0] là set chứa các biến trong scope hiện tại
            raise RedeclaredVariable(ctx.name)
        o[0].add(ctx.name)

        self.visit(ctx.typ, o)

    def visitConstDecl(self, ctx: ConstDecl, o: list):
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)
        o[0].add(ctx.name)

        self.visit(ctx.val, o)

    def visitFuncDecl(self, ctx: FuncDecl, o: list):
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)
        o[0].add(ctx.name) # thêm tên hàm vào scope hiện tại
        # Tạo một scope mới cho hàm
        local_env = [set()] + o
        # Process function parameters
        for param in ctx.param:
            self.visit(param, local_env)
        # The function body is a tuple: (list of declarations, list of expressions)
        decls, exprs = ctx.body
        for d in decls:
            self.visit(d, local_env)
        for e in exprs:
            self.visit(e, local_env)

    def visitIntType(self, ctx: IntType, o: object):
        return ctx

    def visitFloatType(self, ctx: FloatType, o: object):
        return ctx

    def visitIntLit(self, ctx: IntLit, o: object):
        return ctx

    def visitId(self, ctx: Id, o: list):
        # Look up the identifier in all scopes (starting at the innermost)
        for scope in o:
            if ctx.name in scope:
                return ctx
        raise UndeclaredIdentifier(ctx.name)
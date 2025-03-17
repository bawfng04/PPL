from functools import reduce

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
    def visitProgram(self, ctx: Program, o: object):
        reduce(lambda env, decl: self.visit(decl, env) or env, ctx.decl, [])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        else:
            # o.append(ctx.name)
            return o + [ctx.name]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        else:
            # o.append(ctx.name)
            return o + [ctx.name]

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
    # def visitProgram(self, ctx: Program, o: object):
    #     env = [[]]  # Using list instead of set for the innermost scope
    #     for decl in ctx.decl:
    #         self.visit(decl, env)

    def visitProgram(self, ctx: Program, o: object):
        reduce(lambda env, decl: self.visit(decl, env) or env, ctx.decl, [[]])

    def visitVarDecl(self, ctx: VarDecl, o: list):
        if ctx.name in o[0]:  # o[0] is the list containing variables in current scope
            raise RedeclaredVariable(ctx.name)
        o[0].append(ctx.name)

        self.visit(ctx.typ, o)

    def visitConstDecl(self, ctx: ConstDecl, o: list):
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)
        o[0].append(ctx.name)

        self.visit(ctx.val, o)

    def visitFuncDecl(self, ctx: FuncDecl, o: list):
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)
        o[0].append(ctx.name)  # Add function name to current scope

        # Create new scope for function
        local_env = [[]] + o

        # Process parameters
        for param in ctx.param:
            self.visit(param, local_env)

        # Process function body
        decls, exprs = ctx.body
        # for d in decls:
        #     self.visit(d, local_env)
        list(map(lambda d: self.visit(d, local_env), decls))
        # for e in exprs:
        #     self.visit(e, local_env)
        list(map(lambda e: self.visit(e, local_env), exprs))

    def visitIntType(self, ctx: IntType, o: object):
        return ctx

    def visitFloatType(self, ctx: FloatType, o: object):
        return ctx

    def visitIntLit(self, ctx: IntLit, o: object):
        return ctx

    def visitId(self, ctx: Id, o: list):
        # Search for identifier in all scopes from innermost to outermost
        # for scope in o:
        #     if ctx.name in scope:
        #         return ctx
        # raise UndeclaredIdentifier(ctx.name)



        found = reduce(lambda acc, scope: ctx if ctx.name in scope else acc, o, None)
        if found:
            return found
        raise UndeclaredIdentifier(ctx.name)



        # matching_scopes = list(filter(lambda scope: ctx.name in scope, o))
        # if matching_scopes:
        #     return ctx
        # raise UndeclaredIdentifier(ctx.name)

        # len(filter(lambda x: x == ctx.name, o)) > 0 or UndeclaredIdentifier(ctx.name)


#2 c2
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object):
       reduce(lambda env, decl: self.visit(decl, env) or env, ctx.decl, [])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        else:
            return o + [ctx.name]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        else:
            return o + [ctx.name]

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass




#3 c2
class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        reduce(lambda env, decl: self.visit(decl, env) or env, ctx.decl, [])

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return o + [ctx.name]

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return o + [ctx.name]

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        o = o + [ctx.name]
        new_scope = []
        # for param in ctx.param:
        #     self.visit(param, new_scope)
        new_scope = reduce(lambda env, param: self.visit(param, env) or env, ctx.param, new_scope)

        # for decl in ctx.body:
        #     self.visit(decl, new_scope)
        reduce(lambda env, decl: self.visit(decl, env) or env, ctx.body, new_scope)

    def visitIntType(self, ctx: IntType, o: object):
        return ctx

    def visitFloatType(self, ctx: FloatType, o: object):
        return ctx

    def visitIntLit(self, ctx: IntLit, o: object):
        return ctx



class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        o = []
        for decl in ctx.decl:
            #o là danh sách các scope, trong đó scope 0 là scope global
            o += self.visit(decl,o)

    def visitVarDecl(self,ctx:VarDecl,o:object):
        n = ctx.name
        if n in o:
            raise RedeclaredVariable(n)
        return n #Trả về tên hằng số để thêm vào scope

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        n = ctx.name
        if n in o:
            raise RedeclaredConstant(n)
        return n
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        n=ctx.name
        listVar=ctx.param
        listbody=ctx.body[0]
        listId=ctx.body[1]
        name=[] #tạo một scope mới cho hàm
        if n in o:
            raise RedeclaredFunction(n)
        else:
            # o[0].append(n)
            o = o + n
        for nameVar in listVar:
            name+=self.visit(nameVar,name)
        for nameBody in listbody:
            name+=self.visit(nameBody,name+o)
        for id in listId:
            self.visit(id,name+o) #thêm scope của hàm vào scope global




    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        n = ctx.name
        for a in o:
            if n in a:
                return True
        raise UndeclaredIdentifier(n)






# 4 reduce

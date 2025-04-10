# Let AST of a programming language be defined as follows:

# class Program: #decl:List[ClassDecl]

# class Decl(ABC): #abstract class

# class ClassDecl:#name:str,parent:str,mem:List[Decl]

# class VarDecl(Decl): #name:str,typ:Type

# class FuncDecl(Decl): #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])

# class Type(ABC): #abstract class

# class IntType(Type)

# class FloatType(Type)

# class ClassType(Type):#name:str

# class Expr(ABC): #abstract class

# class Lit(Expr): #abstract class

# class IntLit(Lit): #val:int

# class Id(Expr): #name:str

# class FieldAccess(Expr): #exp:Expr,field:str

# and exceptions:

# class RedeclaredField(Exception): #name:str

# class RedeclaredMethod(Exception): #name:str

# Implement the methods of the following class Visitor to travel on the above AST to detect redeclared declarations (field and method in a class).

# class StaticCheck(Visitor):

#     def visitProgram(self,ctx:Program,o:object): pass

#     def visitClassDecl(self,ctx:ClassDecl,o:object):pass

#     def visitVarDecl(self,ctx:VarDecl,o:object):pass

#     def visitFuncDecl(self,ctx:FuncDecl,o:object):pass

#     def visitIntType(self,ctx:IntType,o:object):pass

#     def visitFloatType(self,ctx:FloatType,o:object):pass

#     def visitClassType(self,ctx:ClassType,o:object):pass

#     def visitIntLit(self,ctx:IntLit,o:object):pass

#     def visitId(self,ctx:Id,o:object):pass

#     def visitFieldAccess(self,ctx:FieldAccess,o:object):pass

# Your code starts at line 65

# For example:

# Test	Result
# Program([ClassDecl("x","",[VarDecl("a",IntType()),FuncDecl("a",[],([VarDecl("m",ClassType("x"))],[FieldAccess(Id("m"),"a"),FieldAccess(Id("m"),"b")]))])])
# Redeclared Method: a


# 1

class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        # Visit each class declaration in the program.
        for classDecl in ctx.decl:
            self.visit(classDecl, None)
        return None

    def visitClassDecl(self, ctx: ClassDecl, o: object):
        seen = {} # Dùng để kiểm tra trùng lặp
        # Kiểm tra trùng lặp giữa các field và method
        for mem in ctx.mem:
            if mem.name in seen:
                if isinstance(mem, FuncDecl):
                    raise RedeclaredMethod(mem.name)
                else:
                    raise RedeclaredField(mem.name)
            seen[mem.name] = mem #ví dụ: {a: VarDecl("a",IntType()), a: FuncDecl("a",[],([VarDecl("m",ClassType("x"))],[FieldAccess(Id("m"),"a"),FieldAccess(Id("m"),"b")]))}
        # Visit each member for further checking if needed.
        for mem in ctx.mem:
            self.visit(mem, None)
        return None

    def visitVarDecl(self, ctx: VarDecl, o: object):
        return None

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        # Check for duplicate parameter names.
        seen_params = {}
        for param in ctx.param:
            if param.name in seen_params:
                raise RedeclaredField(param.name)
            seen_params[param.name] = param
        # Visit declarations and expressions in the function body.
        decls, exprs = ctx.body
        for decl in decls:
            self.visit(decl, None)
        for expr in exprs:
            self.visit(expr, None)
        return None

    def visitIntType(self, ctx: IntType, o: object):
        return ctx

    def visitFloatType(self, ctx: FloatType, o: object):
        return ctx

    def visitClassType(self, ctx: ClassType, o: object):
        return ctx

    def visitIntLit(self, ctx: IntLit, o: object):
        return ctx

    def visitId(self, ctx: Id, o: object):
        return ctx

    def visitFieldAccess(self, ctx: FieldAccess, o: object):
        self.visit(ctx.exp, None)
        return ctx



#2
class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o: object):
        global_map = {}
        for classDecl in ctx.decl:
            if classDecl.name in global_map:
                # If duplicate class declarations must be reported, you can raise an exception here.
                raise RedeclaredField(classDecl.name)
            global_map[classDecl.name] = classDecl
        # tạo một global environment chứa các class declarations
        new_o = {'global': global_map, 'env': {}}
        for classDecl in ctx.decl:
            self.visit(classDecl, new_o)
        return None

    def visitClassDecl(self, ctx: ClassDecl, o: object):
        # Check for redeclared members (fields or methods) in a class.
        member_env = {}
        for mem in ctx.mem:
            if mem.name in member_env:
                if isinstance(mem, FuncDecl):
                    raise RedeclaredMethod(mem.name)
                else:
                    raise RedeclaredField(mem.name)
            member_env[mem.name] = mem

        # For each member (methods and fields), check declarations inside.
        # Methods get a fresh variable environment.
        for mem in ctx.mem:
            self.visit(mem, {'global': o['global'], 'env': {}})
        return ctx

    def visitVarDecl(self, ctx: VarDecl, o: object):
        # If the variable's type is a class, ensure that the class exists.
        if isinstance(ctx.typ, ClassType):
            if ctx.typ.name not in o['global']:
                raise UndeclaredClass(ctx.typ.name)
        return ctx

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        local_env = {}
        # Check parameters for duplicate names and validate their types.
        for param in ctx.param:
            if param.name in local_env:
                raise RedeclaredField(param.name)
            local_env[param.name] = param
            self.visit(param, o)  # Validate the parameter's type.
        new_o = {'global': o['global'], 'env': local_env}
        decls, exprs = ctx.body
        # Process local declarations (e.g. variable declarations).
        for decl in decls:
            if isinstance(decl, VarDecl):
                if decl.name in new_o['env']:
                    raise RedeclaredField(decl.name)
                new_o['env'][decl.name] = decl
                self.visit(decl, o)
            else:
                self.visit(decl, new_o)
        # Process expressions in the function body.
        for expr in exprs:
            self.visit(expr, new_o)
        return ctx

    def visitIntType(self, ctx: IntType, o: object):
        return ctx

    def visitFloatType(self, ctx: FloatType, o: object):
        return ctx

    def visitClassType(self, ctx: ClassType, o: object):
        # A class type must exist in the global environment.
        if ctx.name not in o['global']:
            raise UndeclaredClass(ctx.name)
        return ctx

    def visitIntLit(self, ctx: IntLit, o: object):
        return ctx

    def visitId(self, ctx: Id, o: object):
        env = o.get('env', {})
        if ctx.name not in env:
            raise UndeclaredIdentifier(ctx.name)
        return env[ctx.name]

    def visitFieldAccess(self, ctx: FieldAccess, o: object):
        # Evaluate the expression to get the variable declaration.
        var_decl = self.visit(ctx.exp, o)
        # The variable declaration must have a type.
        typ = getattr(var_decl, 'typ', None)
        if not isinstance(typ, ClassType):
            raise UndeclaredField(ctx.field)
        global_env = o['global']
        if typ.name not in global_env:
            raise UndeclaredClass(typ.name)
        class_decl = global_env[typ.name]
        # Look for a field declaration (a VarDecl) with the name of the field.
        for mem in class_decl.mem:
            if isinstance(mem, VarDecl) and mem.name == ctx.field:
                return mem
        # If not found, report an undeclared field.
        raise UndeclaredField(ctx.field)


#3
class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o: object):
        # Build global environment with all class declarations.
        global_env = {}
        for classDecl in ctx.decl:
            if classDecl.name in global_env:
                # Duplicate class declarations; you may raise a redeclared error.
                raise RedeclaredField(classDecl.name)
            global_env[classDecl.name] = classDecl
        new_o = {'global': global_env, 'env': {}}
        for classDecl in ctx.decl:
            self.visit(classDecl, new_o)
        return None

    def visitClassDecl(self, ctx: ClassDecl, o: object):
        # Check duplicates among members.
        member_env = {}
        for mem in ctx.mem:
            if mem.name in member_env:
                if isinstance(mem, FuncDecl):
                    raise RedeclaredMethod(mem.name)
                else:
                    raise RedeclaredField(mem.name)
            member_env[mem.name] = mem
        # Process each member with a fresh local environment.
        for mem in ctx.mem:
            self.visit(mem, {'global': o['global'], 'env': {}})
        return ctx

    def visitVarDecl(self, ctx: VarDecl, o: object):
        # If the declared type is a ClassType, check that the class exists.
        if isinstance(ctx.typ, ClassType):
            if ctx.typ.name not in o['global']:
                raise UndeclaredIdentifier(ctx.typ.name)
        return ctx

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        local_env = {}
        # Check parameters for duplicate names and validate their types.
        for param in ctx.param:
            if param.name in local_env:
                raise RedeclaredField(param.name)
            local_env[param.name] = param
            self.visit(param, o)
        new_o = {'global': o['global'], 'env': local_env}
        decls, exprs = ctx.body
        # Process local declarations within the function body.
        for decl in decls:
            if isinstance(decl, VarDecl):
                if decl.name in new_o['env']:
                    raise RedeclaredField(decl.name)
                new_o['env'][decl.name] = decl
                self.visit(decl, o)
            else:
                self.visit(decl, new_o)
        # Process each expression.
        for expr in exprs:
            self.visit(expr, new_o)
        return ctx

    def visitIntType(self, ctx: IntType, o: object):
        return ctx

    def visitFloatType(self, ctx: FloatType, o: object):
        return ctx

    def visitClassType(self, ctx: ClassType, o: object):
        # Ensure that the class used in a type exists.
        if ctx.name not in o['global']:
            raise UndeclaredIdentifier(ctx.name)
        return ctx

    def visitIntLit(self, ctx: IntLit, o: object):
        return ctx

    def visitId(self, ctx: Id, o: object):
        env = o.get('env', {})
        if ctx.name not in env:
            raise UndeclaredIdentifier(ctx.name)
        return env[ctx.name]

    def lookupField(self, class_decl: ClassDecl, field: str, global_env: dict):
        # Check current class members.
        for mem in class_decl.mem:
            if isinstance(mem, VarDecl) and mem.name == field:
                return mem
        # If not found and there is a parent, check parent's members.
        if class_decl.parent != "":
            if class_decl.parent in global_env:
                parent_class = global_env[class_decl.parent]
                return self.lookupField(parent_class, field, global_env)
        return None

    def visitFieldAccess(self, ctx: FieldAccess, o: object):
        # Evaluate the expression to obtain the variable declaration.
        var_decl = self.visit(ctx.exp, o)
        # The variable must have a type.
        typ = getattr(var_decl, 'typ', None)
        if not isinstance(typ, ClassType):
            raise UndeclaredField(ctx.field)
        global_env = o['global']
        # Ensure the class exists.
        if typ.name not in global_env:
            raise UndeclaredIdentifier(typ.name)
        class_decl = global_env[typ.name]
        # Look up the field recursively along its inheritance chain.
        field_decl = self.lookupField(class_decl, ctx.field, global_env)
        if field_decl is None:
            raise UndeclaredField(ctx.field)
        return field_decl
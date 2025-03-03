
# Given the grammar of MP as follows:

# program: vardecls EOF;

# vardecls: vardecl vardecltail;

# vardecltail: vardecl vardecltail | ;

# vardecl: mptype ids ';' ;

# mptype: INTTYPE | FLOATTYPE;

# ids: ID ',' ids | ID;

# INTTYPE: 'int';

# FLOATTYPE: 'float';

# ID: [a-z]+ ;

# Please copy the following class into your answer and modify the bodies of its methods to count the terminal nodes in the parse tree?

# class ASTGeneration(MPVisitor):

#     def visitProgram(self,ctx:MPParser.ProgramContext):

#         return None

#     def visitVardecls(self,ctx:MPParser.VardeclsContext):

#         return None

#     def visitVardecltail(self,ctx:MPParser.VardecltailContext):

#         return None

#     def visitVardecl(self,ctx:MPParser.VardeclContext):
#         return None

#     def visitMptype(self,ctx:MPParser.MptypeContext):

#         return None

#     def visitIds(self,ctx:MPParser.IdsContext):

#         return None


# 1 Terminal nodes
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        # Program has vardecls and EOF terminals
        # Count 1 for EOF and add count from vardecls
        return self.visit(ctx.vardecls()) + 1

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        # vardecls -> vardecl vardecltail
        # Count terminals from both children
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self,ctx:MPParser.VardecltailContext):
        # vardecltail -> vardecl vardecltail | epsilon
        # If no children (epsilon), return 0
        # Otherwise, count terminals from both children
        if ctx.getChildCount() == 0:
            return 0
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecl(self,ctx:MPParser.VardeclContext):
        # vardecl -> mptype ids ';'
        # Count terminals from mptype and ids, plus 1 for the semicolon
        return self.visit(ctx.mptype()) + self.visit(ctx.ids()) + 1

    def visitMptype(self,ctx:MPParser.MptypeContext):
        # mptype -> INTTYPE | FLOATTYPE
        # Either case has one terminal node
        return 1

    def visitIds(self,ctx:MPParser.IdsContext):
        # ids -> ID ',' ids | ID
        # If it has comma, count terminals from ID and ids and add 1 for the comma
        # Otherwise, just count 1 for the ID
        if ctx.getChildCount() == 1:
            return 1
        else:
            return 1 + 1 + self.visit(ctx.ids())


# 2 - Non-terminals nodes
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        # Program is a non-terminal node
        # Count 1 for this node + count from vardecls
        return 1 + self.visit(ctx.vardecls())

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        # vardecls is a non-terminal node
        # Count 1 for this node + count from its children
        return 1 + self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self,ctx:MPParser.VardecltailContext):
        # vardecltail is a non-terminal
        # If it has no children, return 1
        if ctx.getChildCount() == 0:
            return 1
        # Count 1 for this node + count from its children
        return 1 + self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecl(self,ctx:MPParser.VardeclContext):
        # vardecl is a non-terminal node
        # Count 1 for this node + count from its children (mptype and ids)
        return 1 + self.visit(ctx.mptype()) + self.visit(ctx.ids())

    def visitMptype(self,ctx:MPParser.MptypeContext):
        # mptype is a non-terminal node
        # Count 1 for this node
        return 1

    def visitIds(self,ctx:MPParser.IdsContext):
        # ids is a non-terminal node
        # If it has multiple IDs, count 1 for this node + count from child ids
        # Otherwise just count 1 for this node
        if ctx.getChildCount() == 1:
            return 1
        else:
            return 1 + self.visit(ctx.ids())

# 3
# # Given the grammar of MP as follows:

# program: vardecls EOF;

# vardecls: vardecl vardecltail;

# vardecltail: vardecl vardecltail | ;

# vardecl: mptype ids ';' ;

# mptype: INTTYPE | FLOATTYPE;

# ids: ID ',' ids | ID;

# INTTYPE: 'int';

# FLOATTYPE: 'float';

# ID: [a-z]+ ;

# and AST classes as follows:

# class Program:#decl:list(VarDecl)

# class Type(ABC): pass

# class IntType(Type): pass

# class FloatType(Type): pass

# class VarDecl: #variable:Id; varType: Type

# class Id: #name:str

# Please copy the following class into your answer
# and modify the bodies of its methods to generate the AST of a MP input?

class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        # Program contains a list of VarDecl objects
        decl = self.visit(ctx.vardecls())
        return Program(decl)

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        # vardecls -> vardecl vardecltail
        # Get the VarDecl from vardecl and combine with the list from vardecltail
        vardecl_result = self.visit(ctx.vardecl())
        vardecltail_result = self.visit(ctx.vardecltail())
        # If vardecl_result is a list, combine with vardecltail_result
        # Otherwise, create a list with vardecl_result and combine with vardecltail_result
        if isinstance(vardecl_result, list):
            return vardecl_result + vardecltail_result
        else:
            return [vardecl_result] + vardecltail_result

    def visitVardecltail(self,ctx:MPParser.VardecltailContext):
        # If no children (epsilon), return empty list
        if ctx.getChildCount() == 0:
            return []

        # Otherwise, combine VarDecl from vardecl with the list from vardecltail
        vardecl_result = self.visit(ctx.vardecl())
        vardecltail_result = self.visit(ctx.vardecltail())

        if isinstance(vardecl_result, list):
            return vardecl_result + vardecltail_result
        else:
            return [vardecl_result] + vardecltail_result

    def visitVardecl(self,ctx:MPParser.VardeclContext):
        # vardecl -> mptype ids ';'
        # Get the Type from mptype
        var_type = self.visit(ctx.mptype())
        # Get the list of Id objects from ids
        id_list = self.visit(ctx.ids())

        # Create a VarDecl for each Id with the same Type
        return [VarDecl(id, var_type) for id in id_list]

    def visitMptype(self,ctx:MPParser.MptypeContext):
        # Return the corresponding Type object (IntType or FloatType)
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        # ids -> ID ',' ids | ID
        if ctx.getChildCount() == 1:
            # Only one ID
            return [Id(ctx.ID().getText())]
        else:
            # ID ',' ids
            # Create an Id object for the current ID and combine with the list from child ids
            return [Id(ctx.ID().getText())] + self.visit(ctx.ids())


# 4
# Given the grammar of MP as follows:

# program: vardecl+ EOF;

# vardecl: mptype ids ';' ;

# mptype: INTTYPE | FLOATTYPE;

# ids: ID (',' ID)*;

# INTTYPE: 'int';

# FLOATTYPE: 'float';

# ID: [a-z]+ ;

# and AST classes as follows:

# class Program:#decl:list(VarDecl)

# class Type(ABC): pass

# class IntType(Type): pass

# class FloatType(Type): pass

# class VarDecl: #variable:Id; varType: Type

# class Id: #name:str

# Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?

# class ASTGeneration(MPVisitor):

#     def visitProgram(self,ctx:MPParser.ProgramContext):

#         return None

#     def visitVardecl(self,ctx:MPParser.VardeclContext):
#         return None

#     def visitMptype(self,ctx:MPParser.MptypeContext):

#         return None

#     def visitIds(self,ctx:MPParser.IdsContext):

#         return None


class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        # Collect all VarDecl objects from all vardecl nodes
        decl_list = []
        for vardecl in ctx.vardecl():
            decl_list.extend(self.visit(vardecl))

        return Program(decl_list)

    def visitVardecl(self,ctx:MPParser.VardeclContext):
        # Get the Type object from mptype
        var_type = self.visit(ctx.mptype())

        # Get list of Id objects from ids
        id_list = self.visit(ctx.ids())

        # Create a VarDecl for each Id with the same Type
        return [VarDecl(id_obj, var_type) for id_obj in id_list]

    def visitMptype(self,ctx:MPParser.MptypeContext):
        # Return the appropriate Type based on the terminal
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        # For the new grammar: ids: ID (',' ID)*
        # Create a list of Id objects for all IDs
        result = []

        # First ID is always present
        result.append(Id(ctx.ID(0).getText()))

        # Add any additional IDs
        for i in range(1, len(ctx.ID())):
            result.append(Id(ctx.ID(i).getText()))

        return result
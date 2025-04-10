
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



# 5

# Given the grammar of MP as follows:

# program: exp EOF;

# exp: term ASSIGN exp | term;

# term: factor COMPARE factor | factor;

# factor: factor ANDOR operand | operand;

# operand: ID | INTLIT | BOOLIT | '(' exp ')';

# INTLIT: [0-9]+ ;

# BOOLIT: 'True' | 'False' ;

# ANDOR: 'and' | 'or' ;

# ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;

# COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;

# ID: [a-z]+ ;

# and AST classes as follows:

# class AST(ABC):
#     def __eq__(self, other):
#         return self.__dict__ == other.__dict__

#     @abstractmethod
#     def accept(self, v, param):
#         return v.visit(self, param)

# class Expr(AST):
#     __metaclass__ = ABCMeta
#     pass

# class Binary(Expr):
#     #op:string:
#     #left:Expr
#     #right:Expr
#     def __init__(self, op, left, right):
#         self.op = op
#         self.left = left
#         self.right = right

#     def __str__(self):
#         return "Binary(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"

#     def accept(self, v, param):
#         return v.visitBinaryOp(self, param)

# class Id(Expr):
#     #value:string
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return "Id(" + self.value + ")"

#     def accept(self, v, param):
#         return v.visitId(self, param)

# class IntLiteral(Expr):
#     #value:int
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return "IntLiteral(" + str(self.value) + ")"

#     def accept(self, v, param):
#         return v.visitIntLiteral(self, param)

# class BooleanLiteral(Expr):
#     #value:boolean
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return "BooleanLiteral(" + str(self.value) + ")"

#     def accept(self, v, param):
#         return v.visitBooleanLiteral(self, param)


# Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?

# class ASTGeneration(MPVisitor):

#     def visitProgram(self,ctx:MPParser.ProgramContext):

#         return None

#     def visitExp(self,ctx:MPParser.ExpContext):

#         return None

#     def visitTerm(self,ctx:MPParser.TermContext):

#         return None

#     def visitFactor(self,ctx:MPParser.FactorContext):

#         return None

#     def visitOperand(self,ctx:MPParser.OperandContext):

#         return None

# For example:

# Test	Result
# "a := b := 4"
# Binary(:=,Id(a),Binary(:=,Id(b),IntLiteral(4)))

class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self, ctx:MPParser.ExpContext):
        if ctx.getChildCount() == 1:  # term
            return self.visit(ctx.term())
        else:  # term ASSIGN exp
            left = self.visit(ctx.term())
            op = ctx.ASSIGN().getText()
            right = self.visit(ctx.exp())
            return Binary(op, left, right)

    def visitTerm(self, ctx:MPParser.TermContext):
        if ctx.getChildCount() == 1:  # factor
            return self.visit(ctx.factor(0))
        else:  # factor COMPARE factor
            left = self.visit(ctx.factor(0))
            op = ctx.COMPARE().getText()
            right = self.visit(ctx.factor(1))
            return Binary(op, left, right)

    def visitFactor(self, ctx:MPParser.FactorContext):
        if ctx.getChildCount() == 1:  # operand
            return self.visit(ctx.operand())
        else:  # factor ANDOR operand
            left = self.visit(ctx.factor())
            op = ctx.ANDOR().getText()
            right = self.visit(ctx.operand())
            return Binary(op, left, right)

    def visitOperand(self, ctx:MPParser.OperandContext):
        if ctx.ID():  # ID
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():  # INTLIT
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():  # BOOLIT
            return BooleanLiteral(ctx.BOOLIT().getText() == 'True')
        else:  # '(' exp ')'
            return self.visit(ctx.exp())

# 6
# Given the grammar of MP as follows:

# program: exp EOF;

# exp: (term ASSIGN)* term;

# term: factor COMPARE factor | factor;

# factor: operand (ANDOR operand)*;

# operand: ID | INTLIT | BOOLIT | '(' exp ')';

# INTLIT: [0-9]+ ;

# BOOLIT: 'True' | 'False' ;

# ANDOR: 'and' | 'or' ;

# ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;

# COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;

# ID: [a-z]+ ;

# and AST classes as follows:

# class Expr(ABC):

# class Binary(Expr):  #op:string;left:Expr;right:Expr

# class Id(Expr): #value:string

# class IntLiteral(Expr): #value:int

# class BooleanLiteral(Expr): #value:boolean

# Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?

# class ASTGeneration(MPVisitor):

#     def visitProgram(self,ctx:MPParser.ProgramContext):

#         return None

#     def visitExp(self,ctx:MPParser.ExpContext):

#         return None

#     def visitTerm(self,ctx:MPParser.TermContext):

#         return None

#     def visitFactor(self,ctx:MPParser.FactorContext):

#         return None

#     def visitOperand(self,ctx:MPParser.OperandContext):

#         return None

# For example:

# Test	Result
# "a := b := 4"
# Binary(:=,Id(a),Binary(:=,Id(b),IntLiteral(4)))


class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self, ctx:MPParser.ExpContext):
        # Handle (term ASSIGN)* term
        # Start with the rightmost term
        result = self.visit(ctx.term(len(ctx.term()) - 1))

        # Process assignments from right to left
        for i in range(len(ctx.term()) - 2, -1, -1):
            op = ctx.ASSIGN(i).getText()
            left = self.visit(ctx.term(i))
            result = Binary(op, left, result)

        return result

    def visitTerm(self, ctx:MPParser.TermContext):
        if ctx.getChildCount() == 1:  # factor
            return self.visit(ctx.factor(0))
        else:  # factor COMPARE factor
            left = self.visit(ctx.factor(0))
            op = ctx.COMPARE().getText()
            right = self.visit(ctx.factor(1))
            return Binary(op, left, right)

    def visitFactor(self, ctx:MPParser.FactorContext):
        # Handle operand (ANDOR operand)*
        # Start with the leftmost operand
        result = self.visit(ctx.operand(0))

        # Process from left to right
        for i in range(len(ctx.ANDOR())):
            op = ctx.ANDOR(i).getText()
            right = self.visit(ctx.operand(i + 1))
            result = Binary(op, result, right)

        return result

    def visitOperand(self, ctx:MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText() == "True")
        else:  # '(' exp ')'
            return self.visit(ctx.exp())
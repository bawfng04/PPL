# Generated from d:/Projects/PPL-Assignment/TemplatePPL_Parser/main/VoTien.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .VoTienParser import VoTienParser
else:
    from VoTienParser import VoTienParser

# This class defines a complete listener for a parse tree produced by VoTienParser.
class VoTienListener(ParseTreeListener):

    # Enter a parse tree produced by VoTienParser#program.
    def enterProgram(self, ctx:VoTienParser.ProgramContext):
        pass

    # Exit a parse tree produced by VoTienParser#program.
    def exitProgram(self, ctx:VoTienParser.ProgramContext):
        pass


    # Enter a parse tree produced by VoTienParser#stm.
    def enterStm(self, ctx:VoTienParser.StmContext):
        pass

    # Exit a parse tree produced by VoTienParser#stm.
    def exitStm(self, ctx:VoTienParser.StmContext):
        pass


    # Enter a parse tree produced by VoTienParser#declarationStm.
    def enterDeclarationStm(self, ctx:VoTienParser.DeclarationStmContext):
        pass

    # Exit a parse tree produced by VoTienParser#declarationStm.
    def exitDeclarationStm(self, ctx:VoTienParser.DeclarationStmContext):
        pass


    # Enter a parse tree produced by VoTienParser#var_decl_list.
    def enterVar_decl_list(self, ctx:VoTienParser.Var_decl_listContext):
        pass

    # Exit a parse tree produced by VoTienParser#var_decl_list.
    def exitVar_decl_list(self, ctx:VoTienParser.Var_decl_listContext):
        pass


    # Enter a parse tree produced by VoTienParser#single_decl.
    def enterSingle_decl(self, ctx:VoTienParser.Single_declContext):
        pass

    # Exit a parse tree produced by VoTienParser#single_decl.
    def exitSingle_decl(self, ctx:VoTienParser.Single_declContext):
        pass


    # Enter a parse tree produced by VoTienParser#multiple_decl.
    def enterMultiple_decl(self, ctx:VoTienParser.Multiple_declContext):
        pass

    # Exit a parse tree produced by VoTienParser#multiple_decl.
    def exitMultiple_decl(self, ctx:VoTienParser.Multiple_declContext):
        pass


    # Enter a parse tree produced by VoTienParser#assignmentStm.
    def enterAssignmentStm(self, ctx:VoTienParser.AssignmentStmContext):
        pass

    # Exit a parse tree produced by VoTienParser#assignmentStm.
    def exitAssignmentStm(self, ctx:VoTienParser.AssignmentStmContext):
        pass


    # Enter a parse tree produced by VoTienParser#single_assign.
    def enterSingle_assign(self, ctx:VoTienParser.Single_assignContext):
        pass

    # Exit a parse tree produced by VoTienParser#single_assign.
    def exitSingle_assign(self, ctx:VoTienParser.Single_assignContext):
        pass


    # Enter a parse tree produced by VoTienParser#multiple_assign.
    def enterMultiple_assign(self, ctx:VoTienParser.Multiple_assignContext):
        pass

    # Exit a parse tree produced by VoTienParser#multiple_assign.
    def exitMultiple_assign(self, ctx:VoTienParser.Multiple_assignContext):
        pass


    # Enter a parse tree produced by VoTienParser#expr_list.
    def enterExpr_list(self, ctx:VoTienParser.Expr_listContext):
        pass

    # Exit a parse tree produced by VoTienParser#expr_list.
    def exitExpr_list(self, ctx:VoTienParser.Expr_listContext):
        pass


    # Enter a parse tree produced by VoTienParser#expression.
    def enterExpression(self, ctx:VoTienParser.ExpressionContext):
        pass

    # Exit a parse tree produced by VoTienParser#expression.
    def exitExpression(self, ctx:VoTienParser.ExpressionContext):
        pass


    # Enter a parse tree produced by VoTienParser#term.
    def enterTerm(self, ctx:VoTienParser.TermContext):
        pass

    # Exit a parse tree produced by VoTienParser#term.
    def exitTerm(self, ctx:VoTienParser.TermContext):
        pass


    # Enter a parse tree produced by VoTienParser#factor.
    def enterFactor(self, ctx:VoTienParser.FactorContext):
        pass

    # Exit a parse tree produced by VoTienParser#factor.
    def exitFactor(self, ctx:VoTienParser.FactorContext):
        pass


    # Enter a parse tree produced by VoTienParser#primary.
    def enterPrimary(self, ctx:VoTienParser.PrimaryContext):
        pass

    # Exit a parse tree produced by VoTienParser#primary.
    def exitPrimary(self, ctx:VoTienParser.PrimaryContext):
        pass



del VoTienParser
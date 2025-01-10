# Generated from main/VoTien.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VoTienParser import VoTienParser
else:
    from VoTienParser import VoTienParser

# This class defines a complete generic visitor for a parse tree produced by VoTienParser.

class VoTienVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VoTienParser#program.
    def visitProgram(self, ctx:VoTienParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#stm.
    def visitStm(self, ctx:VoTienParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#declaration.
    def visitDeclaration(self, ctx:VoTienParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#assignment.
    def visitAssignment(self, ctx:VoTienParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#var_decl_list.
    def visitVar_decl_list(self, ctx:VoTienParser.Var_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#var_list.
    def visitVar_list(self, ctx:VoTienParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#expr_list.
    def visitExpr_list(self, ctx:VoTienParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#expression.
    def visitExpression(self, ctx:VoTienParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#term.
    def visitTerm(self, ctx:VoTienParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#factor.
    def visitFactor(self, ctx:VoTienParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#primary.
    def visitPrimary(self, ctx:VoTienParser.PrimaryContext):
        return self.visitChildren(ctx)



del VoTienParser
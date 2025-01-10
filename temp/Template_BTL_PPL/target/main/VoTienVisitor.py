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


    # Visit a parse tree produced by VoTienParser#statement.
    def visitStatement(self, ctx:VoTienParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#declaration_statement.
    def visitDeclaration_statement(self, ctx:VoTienParser.Declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#call_statement.
    def visitCall_statement(self, ctx:VoTienParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#expression.
    def visitExpression(self, ctx:VoTienParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#expression1.
    def visitExpression1(self, ctx:VoTienParser.Expression1Context):
        return self.visitChildren(ctx)



del VoTienParser
"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 02.01.2025
"""
from VoTienVisitor import VoTienVisitor
from VoTienParser import VoTienParser
from AST import *
from functools import reduce

class ASTGeneration(VoTienVisitor):

    # Visit a parse tree produced by VoTienParser#program.
    #* program: statement+ EOF;
    def visitProgram(self, ctx:VoTienParser.ProgramContext):
        return Program([self.visit(stmt) for stmt in ctx.statement()])


    # Visit a parse tree produced by VoTienParser#statement.
    #* statement: (declaration_statement | call_statement) ;
    def visitStatement(self, ctx:VoTienParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoTienParser#declaration_statement.
    #* declaration_statement: INT ID ASSIGNI expression COMCOMMA;
    def visitDeclaration_statement(self, ctx:VoTienParser.Declaration_statementContext):
        return VarDecl(ctx.ID().getText(), IntType(), self.visit(ctx.expression()))


    # Visit a parse tree produced by VoTienParser#call_statement.
    #* call_statement       : PRINT LP expression RP COMCOMMA;
    def visitCall_statement(self, ctx:VoTienParser.Call_statementContext):
        return CallStmt(ctx.PRINT().getText(), self.visit(ctx.expression()))


    # Visit a parse tree produced by VoTienParser#expression.
    #* expression : expression1 ADD expression | expression1;
    def visitExpression(self, ctx:VoTienParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1())
    
        left = self.visit(ctx.expression1())
        right = self.visit(ctx.expression())
        return BinaryOp('+', left, right)


    # Visit a parse tree produced by VoTienParser#expression1.
    #* expression1 : ID | INT_LIT;
    def visitExpression1(self, ctx:VoTienParser.Expression1Context):
        if ctx.ID(): 
            return Id(ctx.ID().getText())
        return IntLiteral(ctx.INT_LIT().getText())
# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal_prim.
    def visitLiteral_prim(self, ctx:MiniGoParser.Literal_primContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_literal_array.
    def visitList_literal_array(self, ctx:MiniGoParser.List_literal_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element_array.
    def visitElement_array(self, ctx:MiniGoParser.Element_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimensions.
    def visitDimensions(self, ctx:MiniGoParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_r.
    def visitType_r(self, ctx:MiniGoParser.Type_rContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_elements.
    def visitList_elements(self, ctx:MiniGoParser.List_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element.
    def visitElement(self, ctx:MiniGoParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression3.
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression4.
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression5.
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression6.
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funtion_call.
    def visitFuntion_call(self, ctx:MiniGoParser.Funtion_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_minigo.
    def visitType_minigo(self, ctx:MiniGoParser.Type_minigoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared_statement.
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variables.
    def visitVariables(self, ctx:MiniGoParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constants.
    def visitConstants(self, ctx:MiniGoParser.ConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_else_if.
    def visitList_else_if(self, ctx:MiniGoParser.List_else_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if.
    def visitElse_if(self, ctx:MiniGoParser.Else_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_for.
    def visitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_loop.
    def visitFor_loop(self, ctx:MiniGoParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_array.
    def visitFor_array(self, ctx:MiniGoParser.For_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variables_for.
    def visitVariables_for(self, ctx:MiniGoParser.Variables_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_for.
    def visitAssign_for(self, ctx:MiniGoParser.Assign_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared.
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function.
    def visitFunction(self, ctx:MiniGoParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method.
    def visitMethod(self, ctx:MiniGoParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_type_declared.
    def visitStruct_type_declared(self, ctx:MiniGoParser.Struct_type_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_fields.
    def visitList_fields(self, ctx:MiniGoParser.List_fieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fields.
    def visitFields(self, ctx:MiniGoParser.FieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_type_declared.
    def visitInterface_type_declared(self, ctx:MiniGoParser.Interface_type_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_meth_interface.
    def visitList_meth_interface(self, ctx:MiniGoParser.List_meth_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#meth_interface.
    def visitMeth_interface(self, ctx:MiniGoParser.Meth_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_param.
    def visitList_param(self, ctx:MiniGoParser.List_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_ID.
    def visitList_ID(self, ctx:MiniGoParser.List_IDContext):
        return self.visitChildren(ctx)



del MiniGoParser
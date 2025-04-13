# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#newlines.
    def visitNewlines(self, ctx:MiniGoParser.NewlinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#more_declared.
    def visitMore_declared(self, ctx:MiniGoParser.More_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared.
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variables_declared.
    def visitVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_name_ids.
    def visitType_name_ids(self, ctx:MiniGoParser.Type_name_idsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#comma_ids.
    def visitComma_ids(self, ctx:MiniGoParser.Comma_idsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constants_declared.
    def visitConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl_list.
    def visitConst_decl_list(self, ctx:MiniGoParser.Const_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_declared.
    def visitFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_type.
    def visitReturn_type(self, ctx:MiniGoParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#more_types.
    def visitMore_types(self, ctx:MiniGoParser.More_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_declared.
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#params_list.
    def visitParams_list(self, ctx:MiniGoParser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#comma_param_ids.
    def visitComma_param_ids(self, ctx:MiniGoParser.Comma_param_idsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declared.
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_type_list.
    def visitStruct_type_list(self, ctx:MiniGoParser.Struct_type_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#more_struct_fields.
    def visitMore_struct_fields(self, ctx:MiniGoParser.More_struct_fieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#opt_newlines.
    def visitOpt_newlines(self, ctx:MiniGoParser.Opt_newlinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_field.
    def visitStruct_field(self, ctx:MiniGoParser.Struct_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#more_ids.
    def visitMore_ids(self, ctx:MiniGoParser.More_idsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declared.
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_type_list.
    def visitInterface_type_list(self, ctx:MiniGoParser.Interface_type_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#more_interface_methods.
    def visitMore_interface_methods(self, ctx:MiniGoParser.More_interface_methodsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method.
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared_statement.
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_op.
    def visitAssign_op(self, ctx:MiniGoParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_lhs.
    def visitAssign_lhs(self, ctx:MiniGoParser.Assign_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#more_access.
    def visitMore_access(self, ctx:MiniGoParser.More_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if_chain.
    def visitElse_if_chain(self, ctx:MiniGoParser.Else_if_chainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if_branch.
    def visitElse_if_branch(self, ctx:MiniGoParser.Else_if_branchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_clause.
    def visitElse_clause(self, ctx:MiniGoParser.Else_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_condition.
    def visitFor_condition(self, ctx:MiniGoParser.For_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_three_parts.
    def visitFor_three_parts(self, ctx:MiniGoParser.For_three_partsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_range.
    def visitFor_range(self, ctx:MiniGoParser.For_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_declaration.
    def visitFor_declaration(self, ctx:MiniGoParser.For_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_assign.
    def visitFor_assign(self, ctx:MiniGoParser.For_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block_stmt.
    def visitBlock_stmt(self, ctx:MiniGoParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block_content.
    def visitBlock_content(self, ctx:MiniGoParser.Block_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_list.
    def visitExpr_list(self, ctx:MiniGoParser.Expr_listContext):
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


    # Visit a parse tree produced by MiniGoParser#more_access_expr.
    def visitMore_access_expr(self, ctx:MiniGoParser.More_access_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operand.
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element_access.
    def visitElement_access(self, ctx:MiniGoParser.Element_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_access.
    def visitField_access(self, ctx:MiniGoParser.Field_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_expr.
    def visitCall_expr(self, ctx:MiniGoParser.Call_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typed_array_literal.
    def visitTyped_array_literal(self, ctx:MiniGoParser.Typed_array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#untyped_array_literal.
    def visitUntyped_array_literal(self, ctx:MiniGoParser.Untyped_array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal_list.
    def visitLiteral_list(self, ctx:MiniGoParser.Literal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal_item.
    def visitLiteral_item(self, ctx:MiniGoParser.Literal_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#more_dimensions.
    def visitMore_dimensions(self, ctx:MiniGoParser.More_dimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_name.
    def visitType_name(self, ctx:MiniGoParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#optional_field_list.
    def visitOptional_field_list(self, ctx:MiniGoParser.Optional_field_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_list.
    def visitField_list(self, ctx:MiniGoParser.Field_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_init.
    def visitField_init(self, ctx:MiniGoParser.Field_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visitChildren(ctx)



del MiniGoParser
# Generated from d:/Projects/PPL-Assignment/BTL/BTL_2/BTL_2_task_6_update/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete listener for a parse tree produced by MiniGoParser.
class MiniGoListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGoParser#program.
    def enterProgram(self, ctx:MiniGoParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGoParser#program.
    def exitProgram(self, ctx:MiniGoParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGoParser#newlines.
    def enterNewlines(self, ctx:MiniGoParser.NewlinesContext):
        pass

    # Exit a parse tree produced by MiniGoParser#newlines.
    def exitNewlines(self, ctx:MiniGoParser.NewlinesContext):
        pass


    # Enter a parse tree produced by MiniGoParser#more_declared.
    def enterMore_declared(self, ctx:MiniGoParser.More_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#more_declared.
    def exitMore_declared(self, ctx:MiniGoParser.More_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#declared.
    def enterDeclared(self, ctx:MiniGoParser.DeclaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#declared.
    def exitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_statement.
    def enterList_statement(self, ctx:MiniGoParser.List_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_statement.
    def exitList_statement(self, ctx:MiniGoParser.List_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#statement.
    def enterStatement(self, ctx:MiniGoParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#statement.
    def exitStatement(self, ctx:MiniGoParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#variables_declared.
    def enterVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#variables_declared.
    def exitVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#var_decl.
    def enterVar_decl(self, ctx:MiniGoParser.Var_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#var_decl.
    def exitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#type_name_ids.
    def enterType_name_ids(self, ctx:MiniGoParser.Type_name_idsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#type_name_ids.
    def exitType_name_ids(self, ctx:MiniGoParser.Type_name_idsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#comma_ids.
    def enterComma_ids(self, ctx:MiniGoParser.Comma_idsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#comma_ids.
    def exitComma_ids(self, ctx:MiniGoParser.Comma_idsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#constants_declared.
    def enterConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#constants_declared.
    def exitConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#const_decl_list.
    def enterConst_decl_list(self, ctx:MiniGoParser.Const_decl_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#const_decl_list.
    def exitConst_decl_list(self, ctx:MiniGoParser.Const_decl_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#const_decl.
    def enterConst_decl(self, ctx:MiniGoParser.Const_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#const_decl.
    def exitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#function_declared.
    def enterFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#function_declared.
    def exitFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#return_type.
    def enterReturn_type(self, ctx:MiniGoParser.Return_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#return_type.
    def exitReturn_type(self, ctx:MiniGoParser.Return_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#more_types.
    def enterMore_types(self, ctx:MiniGoParser.More_typesContext):
        pass

    # Exit a parse tree produced by MiniGoParser#more_types.
    def exitMore_types(self, ctx:MiniGoParser.More_typesContext):
        pass


    # Enter a parse tree produced by MiniGoParser#receiver.
    def enterReceiver(self, ctx:MiniGoParser.ReceiverContext):
        pass

    # Exit a parse tree produced by MiniGoParser#receiver.
    def exitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_declared.
    def enterMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_declared.
    def exitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#params_list.
    def enterParams_list(self, ctx:MiniGoParser.Params_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#params_list.
    def exitParams_list(self, ctx:MiniGoParser.Params_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#param.
    def enterParam(self, ctx:MiniGoParser.ParamContext):
        pass

    # Exit a parse tree produced by MiniGoParser#param.
    def exitParam(self, ctx:MiniGoParser.ParamContext):
        pass


    # Enter a parse tree produced by MiniGoParser#comma_param_ids.
    def enterComma_param_ids(self, ctx:MiniGoParser.Comma_param_idsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#comma_param_ids.
    def exitComma_param_ids(self, ctx:MiniGoParser.Comma_param_idsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_declared.
    def enterStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_declared.
    def exitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_type_list.
    def enterStruct_type_list(self, ctx:MiniGoParser.Struct_type_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_type_list.
    def exitStruct_type_list(self, ctx:MiniGoParser.Struct_type_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#more_struct_fields.
    def enterMore_struct_fields(self, ctx:MiniGoParser.More_struct_fieldsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#more_struct_fields.
    def exitMore_struct_fields(self, ctx:MiniGoParser.More_struct_fieldsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#opt_newlines.
    def enterOpt_newlines(self, ctx:MiniGoParser.Opt_newlinesContext):
        pass

    # Exit a parse tree produced by MiniGoParser#opt_newlines.
    def exitOpt_newlines(self, ctx:MiniGoParser.Opt_newlinesContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_field.
    def enterStruct_field(self, ctx:MiniGoParser.Struct_fieldContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_field.
    def exitStruct_field(self, ctx:MiniGoParser.Struct_fieldContext):
        pass


    # Enter a parse tree produced by MiniGoParser#more_ids.
    def enterMore_ids(self, ctx:MiniGoParser.More_idsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#more_ids.
    def exitMore_ids(self, ctx:MiniGoParser.More_idsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_declared.
    def enterInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_declared.
    def exitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_type_list.
    def enterInterface_type_list(self, ctx:MiniGoParser.Interface_type_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_type_list.
    def exitInterface_type_list(self, ctx:MiniGoParser.Interface_type_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#more_interface_methods.
    def enterMore_interface_methods(self, ctx:MiniGoParser.More_interface_methodsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#more_interface_methods.
    def exitMore_interface_methods(self, ctx:MiniGoParser.More_interface_methodsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_method.
    def enterInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_method.
    def exitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        pass


    # Enter a parse tree produced by MiniGoParser#declared_statement.
    def enterDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#declared_statement.
    def exitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assign_statement.
    def enterAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assign_statement.
    def exitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assign_op.
    def enterAssign_op(self, ctx:MiniGoParser.Assign_opContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assign_op.
    def exitAssign_op(self, ctx:MiniGoParser.Assign_opContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assign_lhs.
    def enterAssign_lhs(self, ctx:MiniGoParser.Assign_lhsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assign_lhs.
    def exitAssign_lhs(self, ctx:MiniGoParser.Assign_lhsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#more_access.
    def enterMore_access(self, ctx:MiniGoParser.More_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#more_access.
    def exitMore_access(self, ctx:MiniGoParser.More_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#if_statement.
    def enterIf_statement(self, ctx:MiniGoParser.If_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#if_statement.
    def exitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#else_if_list.
    def enterElse_if_list(self, ctx:MiniGoParser.Else_if_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#else_if_list.
    def exitElse_if_list(self, ctx:MiniGoParser.Else_if_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#else_if.
    def enterElse_if(self, ctx:MiniGoParser.Else_ifContext):
        pass

    # Exit a parse tree produced by MiniGoParser#else_if.
    def exitElse_if(self, ctx:MiniGoParser.Else_ifContext):
        pass


    # Enter a parse tree produced by MiniGoParser#else_part.
    def enterElse_part(self, ctx:MiniGoParser.Else_partContext):
        pass

    # Exit a parse tree produced by MiniGoParser#else_part.
    def exitElse_part(self, ctx:MiniGoParser.Else_partContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_statement.
    def enterFor_statement(self, ctx:MiniGoParser.For_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_statement.
    def exitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#basic_for.
    def enterBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        pass

    # Exit a parse tree produced by MiniGoParser#basic_for.
    def exitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_loop.
    def enterFor_loop(self, ctx:MiniGoParser.For_loopContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_loop.
    def exitFor_loop(self, ctx:MiniGoParser.For_loopContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_array.
    def enterFor_array(self, ctx:MiniGoParser.For_arrayContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_array.
    def exitFor_array(self, ctx:MiniGoParser.For_arrayContext):
        pass


    # Enter a parse tree produced by MiniGoParser#variables_for.
    def enterVariables_for(self, ctx:MiniGoParser.Variables_forContext):
        pass

    # Exit a parse tree produced by MiniGoParser#variables_for.
    def exitVariables_for(self, ctx:MiniGoParser.Variables_forContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assign_for.
    def enterAssign_for(self, ctx:MiniGoParser.Assign_forContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assign_for.
    def exitAssign_for(self, ctx:MiniGoParser.Assign_forContext):
        pass


    # Enter a parse tree produced by MiniGoParser#break_statement.
    def enterBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#break_statement.
    def exitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#continue_statement.
    def enterContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#continue_statement.
    def exitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#return_statement.
    def enterReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#return_statement.
    def exitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#call_statement.
    def enterCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#call_statement.
    def exitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#block_stmt.
    def enterBlock_stmt(self, ctx:MiniGoParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#block_stmt.
    def exitBlock_stmt(self, ctx:MiniGoParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#block_content.
    def enterBlock_content(self, ctx:MiniGoParser.Block_contentContext):
        pass

    # Exit a parse tree produced by MiniGoParser#block_content.
    def exitBlock_content(self, ctx:MiniGoParser.Block_contentContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expr_list.
    def enterExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expr_list.
    def exitExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expression.
    def enterExpression(self, ctx:MiniGoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expression.
    def exitExpression(self, ctx:MiniGoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expression1.
    def enterExpression1(self, ctx:MiniGoParser.Expression1Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression1.
    def exitExpression1(self, ctx:MiniGoParser.Expression1Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression2.
    def enterExpression2(self, ctx:MiniGoParser.Expression2Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression2.
    def exitExpression2(self, ctx:MiniGoParser.Expression2Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression3.
    def enterExpression3(self, ctx:MiniGoParser.Expression3Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression3.
    def exitExpression3(self, ctx:MiniGoParser.Expression3Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression4.
    def enterExpression4(self, ctx:MiniGoParser.Expression4Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression4.
    def exitExpression4(self, ctx:MiniGoParser.Expression4Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression5.
    def enterExpression5(self, ctx:MiniGoParser.Expression5Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression5.
    def exitExpression5(self, ctx:MiniGoParser.Expression5Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression6.
    def enterExpression6(self, ctx:MiniGoParser.Expression6Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression6.
    def exitExpression6(self, ctx:MiniGoParser.Expression6Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression7.
    def enterExpression7(self, ctx:MiniGoParser.Expression7Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression7.
    def exitExpression7(self, ctx:MiniGoParser.Expression7Context):
        pass


    # Enter a parse tree produced by MiniGoParser#more_access_expr.
    def enterMore_access_expr(self, ctx:MiniGoParser.More_access_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#more_access_expr.
    def exitMore_access_expr(self, ctx:MiniGoParser.More_access_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#operand.
    def enterOperand(self, ctx:MiniGoParser.OperandContext):
        pass

    # Exit a parse tree produced by MiniGoParser#operand.
    def exitOperand(self, ctx:MiniGoParser.OperandContext):
        pass


    # Enter a parse tree produced by MiniGoParser#element_access.
    def enterElement_access(self, ctx:MiniGoParser.Element_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#element_access.
    def exitElement_access(self, ctx:MiniGoParser.Element_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#field_access.
    def enterField_access(self, ctx:MiniGoParser.Field_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#field_access.
    def exitField_access(self, ctx:MiniGoParser.Field_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#call_expr.
    def enterCall_expr(self, ctx:MiniGoParser.Call_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#call_expr.
    def exitCall_expr(self, ctx:MiniGoParser.Call_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literal.
    def enterLiteral(self, ctx:MiniGoParser.LiteralContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literal.
    def exitLiteral(self, ctx:MiniGoParser.LiteralContext):
        pass


    # Enter a parse tree produced by MiniGoParser#typed_array_literal.
    def enterTyped_array_literal(self, ctx:MiniGoParser.Typed_array_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#typed_array_literal.
    def exitTyped_array_literal(self, ctx:MiniGoParser.Typed_array_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#untyped_array_literal.
    def enterUntyped_array_literal(self, ctx:MiniGoParser.Untyped_array_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#untyped_array_literal.
    def exitUntyped_array_literal(self, ctx:MiniGoParser.Untyped_array_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literal_list.
    def enterLiteral_list(self, ctx:MiniGoParser.Literal_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literal_list.
    def exitLiteral_list(self, ctx:MiniGoParser.Literal_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literal_item.
    def enterLiteral_item(self, ctx:MiniGoParser.Literal_itemContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literal_item.
    def exitLiteral_item(self, ctx:MiniGoParser.Literal_itemContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_type.
    def enterArray_type(self, ctx:MiniGoParser.Array_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_type.
    def exitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#more_dimensions.
    def enterMore_dimensions(self, ctx:MiniGoParser.More_dimensionsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#more_dimensions.
    def exitMore_dimensions(self, ctx:MiniGoParser.More_dimensionsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#type_name.
    def enterType_name(self, ctx:MiniGoParser.Type_nameContext):
        pass

    # Exit a parse tree produced by MiniGoParser#type_name.
    def exitType_name(self, ctx:MiniGoParser.Type_nameContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_literal.
    def enterStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_literal.
    def exitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#optional_field_list.
    def enterOptional_field_list(self, ctx:MiniGoParser.Optional_field_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#optional_field_list.
    def exitOptional_field_list(self, ctx:MiniGoParser.Optional_field_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#field_list.
    def enterField_list(self, ctx:MiniGoParser.Field_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#field_list.
    def exitField_list(self, ctx:MiniGoParser.Field_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#field_init.
    def enterField_init(self, ctx:MiniGoParser.Field_initContext):
        pass

    # Exit a parse tree produced by MiniGoParser#field_init.
    def exitField_init(self, ctx:MiniGoParser.Field_initContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_expression.
    def enterList_expression(self, ctx:MiniGoParser.List_expressionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_expression.
    def exitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        pass



del MiniGoParser
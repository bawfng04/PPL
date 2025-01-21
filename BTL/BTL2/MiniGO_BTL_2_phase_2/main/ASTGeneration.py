"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 20.01.2025
"""
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

##! continue update
class ASTGeneration(MiniGoVisitor):
    #copy function target/main/MiniGoVisitor.py
    pass
    # Tất cả các hàm trong class MiniGoVisitor
    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx: MiniGoParser.ProgramContext):
        decls = []
        for child in ctx.children:
            if isinstance(child, MiniGoParser.DeclaredContext):
                decl = self.visit(child)
                if isinstance(decl, list):
                    decls.extend(decl)
                else:
                    decls.append(decl)
        return Program(decls)


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
        if not ctx.var_decl_list():
            return []
        return self.visit(ctx.var_decl_list())


    # Visit a parse tree produced by MiniGoParser#var_decl_list.
    def visitVar_decl_list(self, ctx:MiniGoParser.Var_decl_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.var_decl())]
        return [self.visit(ctx.var_decl())] + self.visit(ctx.var_decl_list())


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        # Handle single ID case
        if not ctx.COMMA():
            id = Id(ctx.ID(0).getText()) # Get first ID
            typ = self.visit(ctx.type_name()) if ctx.type_name() else None
            init = self.visit(ctx.expression()) if ctx.expression() else None
            return VariablesDecl(id, typ, init)

        # Handle multiple IDs case
        ids = [Id(id.getText()) for id in ctx.ID()]
        typ = self.visit(ctx.type_name()) if ctx.type_name() else None
        inits = self.visit(ctx.expr_list()) if ctx.expr_list() else None
        if isinstance(inits, list):
            return [VariablesDecl(id, typ, init) for id, init in zip(ids, inits)]
        return [VariablesDecl(id, typ, None) for id in ids]


    # Visit a parse tree produced by MiniGoParser#constants_declared.
    def visitConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        if not ctx.const_decl_list():
            return []
        return self.visit(ctx.const_decl_list())


    # Visit a parse tree produced by MiniGoParser#const_decl_list.
    def visitConst_decl_list(self, ctx:MiniGoParser.Const_decl_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.const_decl())]
        return [self.visit(ctx.const_decl())] + self.visit(ctx.const_decl_list())

    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return ConstDecl(Id(ctx.ID().getText()), self.visit(ctx.expression()))


    # Visit a parse tree produced by MiniGoParser#function_declared.
    def visitFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        name = Id(ctx.ID().getText())
        returnType = VoidType()
        if ctx.type_name(): # Check if type_name exists
            type_nodes = ctx.type_name()
            if isinstance(type_nodes, list):
                returnType = self.visit(type_nodes[0]) # Get first type if multiple
            else:
                returnType = self.visit(type_nodes)
        params = []
        if ctx.params_list():
            params = self.visit(ctx.params_list())
        return FunctionDecl(name, returnType, None, params, [])


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_declared.
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_params.
    def visitMethod_params(self, ctx:MiniGoParser.Method_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_param.
    def visitMethod_param(self, ctx:MiniGoParser.Method_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#params_list.
    def visitParams_list(self, ctx:MiniGoParser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declared.
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_type.
    def visitStruct_type(self, ctx:MiniGoParser.Struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_field.
    def visitStruct_field(self, ctx:MiniGoParser.Struct_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#more_ids.
    def visitMore_ids(self, ctx:MiniGoParser.More_idsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_end.
    def visitStruct_end(self, ctx:MiniGoParser.Struct_endContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declared.
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_type.
    def visitInterface_type(self, ctx:MiniGoParser.Interface_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method.
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#optional_params.
    def visitOptional_params(self, ctx:MiniGoParser.Optional_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#optional_type.
    def visitOptional_type(self, ctx:MiniGoParser.Optional_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#optional_semi.
    def visitOptional_semi(self, ctx:MiniGoParser.Optional_semiContext):
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


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_init.
    def visitFor_init(self, ctx:MiniGoParser.For_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_update.
    def visitFor_update(self, ctx:MiniGoParser.For_updateContext):
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


    # Visit a parse tree produced by MiniGoParser#expr_list.
    def visitExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        # return self.visitChildren(ctx)
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1())
        return BinaryOp("||", self.visit(ctx.expression()), self.visit(ctx.expression1()))

    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        # return self.visitChildren(ctx)
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2())
        return BinaryOp("&&", self.visit(ctx.expression1()), self.visit(ctx.expression2()))

    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx: MiniGoParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        op = ctx.getChild(1).getText()
        return BinaryOp(op, self.visit(ctx.expression2()), self.visit(ctx.expression3()))

    def visitExpression3(self, ctx: MiniGoParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        op = ctx.getChild(1).getText()
        return BinaryOp(op, self.visit(ctx.expression3()), self.visit(ctx.expression4()))

    def visitExpression4(self, ctx: MiniGoParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        op = ctx.getChild(1).getText()
        return BinaryOp(op, self.visit(ctx.expression4()), self.visit(ctx.expression5()))

    def visitExpression5(self, ctx: MiniGoParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        op = ctx.getChild(1).getText()
        return BinaryOp(op, self.visit(ctx.expression5()), self.visit(ctx.expression6()))

    def visitExpression6(self, ctx: MiniGoParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        if ctx.NOT():
            return UnaryOp("!", self.visit(ctx.expression6()))
        return UnaryOp("-", self.visit(ctx.expression6()))


    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx: MiniGoParser.Expression7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operand())
        result = self.visit(ctx.operand())
        for i in range(len(ctx.children)):
            child = ctx.children[i]
            if child.getRuleIndex() == MiniGoParser.RULE_element_access:
                result = ArrayCell(result, self.visit(child))
            elif child.getRuleIndex() == MiniGoParser.RULE_field_access:
                result = FieldAccess(result, self.visit(child))
            elif child.getRuleIndex() == MiniGoParser.RULE_call_expr:
                if isinstance(result, Id):
                    # For function calls
                    result = CallExpr(None, result, self.visit(child))
                else:
                    # For method calls
                    method_name = result.fieldname if isinstance(result, FieldAccess) else None
                    result = CallExpr(result.obj if isinstance(result, FieldAccess) else result,
                                    method_name, self.visit(child))
        return result

    # Visit a parse tree produced by MiniGoParser#operand.
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        # return self.visitChildren(ctx)
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.expression())

    # Visit a parse tree produced by MiniGoParser#element_access.

    def visitElement_access(self, ctx: MiniGoParser.Element_accessContext):
        return self.visit(ctx.expression())


    # Visit a parse tree produced by MiniGoParser#field_access.
    def visitField_access(self, ctx:MiniGoParser.Field_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_expr.
    def visitCall_expr(self, ctx: MiniGoParser.Call_exprContext):
        if ctx.list_expression():
            return self.visit(ctx.list_expression())
        return []


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx: MiniGoParser.LiteralContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.TRUE():
            return BooleanLiteral(True)
        if ctx.FALSE():
            return BooleanLiteral(False)
        if ctx.NIL():
            return NilLiteral()
        if ctx.array_literal():
            return self.visit(ctx.array_literal())
        return self.visit(ctx.struct_literal())


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx: MiniGoParser.Array_literalContext):
        type_info = self.visit(ctx.array_type())
        values = []
        if ctx.list_expression():
            values = self.visit(ctx.list_expression())
            if not isinstance(values, list):
                values = [values]

        # Use empty list for dimensions in first array literal
        if len(type_info[1]) == 1:
            dimensions = []
        else:
            dimensions = type_info[1][1:]

        return ArrayLiteral(type_info[0], dimensions, values)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx: MiniGoParser.Array_typeContext):
        # Handle base type
        if ctx.type_name():
            if ctx.type_name().INT():
                typ = IntType()
            elif ctx.type_name().FLOAT():
                typ = FloatType()
            elif ctx.type_name().STRING():
                typ = StringType()
            elif ctx.type_name().BOOLEAN():
                typ = BooleanType()
            elif ctx.type_name().ID():
                typ = Id(ctx.type_name().ID().getText())
            else:
                typ = self.visit(ctx.type_name())
        else:
            typ = None

        # Collect dimensions
        dimensions = []
        for lit in ctx.INT_LIT():
            dimensions.append(int(lit.getText()))

        return (typ, dimensions)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx: MiniGoParser.Struct_literalContext):
        name = Id(ctx.ID().getText())
        fields = []
        if ctx.field_list():
            fields = self.visit(ctx.field_list())
        return StructLiteral(name, fields)

    def visitField_list(self, ctx: MiniGoParser.Field_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.field_init())]
        return [self.visit(ctx.field_init())] + self.visit(ctx.field_list())

    # Visit a parse tree produced by MiniGoParser#field_list.
    def visitField_access(self, ctx: MiniGoParser.Field_accessContext):
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#field_init.
    def visitField_init(self, ctx: MiniGoParser.Field_initContext):
        return (Id(ctx.ID().getText()), self.visit(ctx.expression()))


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        # return self.visitChildren(ctx)
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.list_expression())
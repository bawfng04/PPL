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
        # Process the initial declared
        initial_declared = ctx.declared()
        if initial_declared:
            initial_decls = self.visit(initial_declared)
            if isinstance(initial_decls, list):
                decls.extend(initial_decls)
            else:
                decls.append(initial_decls)
        # Process more_declared to collect additional declared nodes
        more_declared_node = ctx.more_declared()
        if more_declared_node:
            more_decls = self.visit(more_declared_node)
            if isinstance(more_decls, list):
                decls.extend(more_decls)
            else:
                decls.append(more_decls)
        return Program(decls)


    # Visit a parse tree produced by MiniGoParser#newlines.
    def visitNewlines(self, ctx:MiniGoParser.NewlinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#more_declared.
    # def visitMore_declared(self, ctx:MiniGoParser.More_declaredContext):
    #     if not ctx.children:
    #         return []

    #     decls = []
    #     if ctx.declared():
    #         decl = self.visit(ctx.declared())
    #         if isinstance(decl, list):
    #             decls.extend(decl)
    #         else:
    #             decls.append(decl)

    #     if ctx.more_declared():
    #         more_decls = self.visit(ctx.more_declared())
    #         if isinstance(more_decls, list):
    #             decls.extend(more_decls)
    #         else:
    #             decls.append(more_decls)

    #     return decls

    def visitMore_declared(self, ctx: MiniGoParser.More_declaredContext):
        if not ctx.children:
            return []
        # Extract declared from current more_declared and recurse
        current_decl = self.visit(ctx.declared())
        more_decls = self.visit(ctx.more_declared())
        # Flatten if current_decl is a list (from variables_declared)
        current_list = current_decl if isinstance(current_decl, list) else [current_decl]
        return current_list + more_decls

    # Visit a parse tree produced by MiniGoParser#declared.
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        # Handle each type of declaration
        if ctx.variables_declared():
            vars_decl = self.visit(ctx.variables_declared())
            return vars_decl if isinstance(vars_decl, list) else [vars_decl]
        elif ctx.constants_declared():
            return self.visit(ctx.constants_declared())
        elif ctx.function_declared():
            return self.visit(ctx.function_declared())
        elif ctx.method_declared():
            return self.visit(ctx.method_declared())
        elif ctx.struct_declared():
            return self.visit(ctx.struct_declared())
        elif ctx.interface_declared():
            return self.visit(ctx.interface_declared())
        return None


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        if ctx.declared_statement():
            return self.visit(ctx.declared_statement())
        elif ctx.assign_statement():
            return self.visit(ctx.assign_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.call_statement():
            return self.visit(ctx.call_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())


    # Fix variables_declared to handle multiple declarations correctly
    def visitVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        if not ctx.var_decl_list():
            return []
        decls = self.visit(ctx.var_decl_list())
        # Flatten the list if needed
        if isinstance(decls[0], list):
            return [item for sublist in decls for item in sublist]
        return decls


    # Visit a parse tree produced by MiniGoParser#var_decl_list.
    def visitVar_decl_list(self, ctx:MiniGoParser.Var_decl_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.var_decl())]
        return [self.visit(ctx.var_decl())] + self.visit(ctx.var_decl_list())


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        # Handle single ID case
        if not ctx.COMMA():
            id = Id(ctx.ID(0).getText())
            typ = self.visit(ctx.type_name()) if ctx.type_name() else None
            init = self.visit(ctx.expression()) if ctx.expression() else None
            return VariablesDecl(id, typ, init)

        # Handle multiple IDs case
        ids = [Id(id.getText()) for id in ctx.ID()]
        typ = self.visit(ctx.type_name()) if ctx.type_name() else None
        inits = []
        if ctx.expr_list():
            inits = self.visit(ctx.expr_list())
        return [VariablesDecl(id, typ, init) for id, init in zip(ids, inits)] if inits else [VariablesDecl(id, typ, None) for id in ids]


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

        # Handle return type
        if ctx.type_name():
            if isinstance(ctx.type_name(), list):
                returnType = self.visit(ctx.type_name()[0])
            else:
                returnType = self.visit(ctx.type_name())

        # Handle parameters
        params = []
        if ctx.params_list():
            params = self.visit(ctx.params_list())
            if not isinstance(params, list):
                params = [params]

        # Handle block statement
        body = []
        if ctx.block_stmt():
            body = self.visit(ctx.block_stmt())

        return FunctionDecl(name, returnType, None, params, body)



    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx: MiniGoParser.ReceiverContext):
        var_name = ctx.ID(0).getText()
        class_name = ctx.ID(1).getText() if ctx.ID(1) else None
        var_type = ClassType(Id(class_name))
        return VariablesDecl(Id(var_name), var_type, None)


    # Visit a parse tree produced by MiniGoParser#method_declared.
    def visitMethod_declared(self, ctx: MiniGoParser.Method_declaredContext):
        # Get method name
        name = Id(ctx.ID().getText())

        # Get receiver
        receiver = self.visit(ctx.receiver())

        # Handle return type
        returnType = VoidType()
        if ctx.type_name():
            if isinstance(ctx.type_name(), list):
                returnType = self.visit(ctx.type_name()[0])
            else:
                returnType = self.visit(ctx.type_name())

        # Handle parameters
        params = []
        if ctx.method_params():
            params = self.visit(ctx.method_params())
            if not isinstance(params, list):
                params = [params]

        # Initialize empty list for body/statements
        stmts = []

        return FunctionDecl(name, returnType, receiver, params, stmts)



    # Visit a parse tree produced by MiniGoParser#method_params.
    def visitMethod_params(self, ctx: MiniGoParser.Method_paramsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.method_param())]
        return [self.visit(ctx.method_param())] + self.visit(ctx.method_params())


    # Visit a parse tree produced by MiniGoParser#method_param.
    def visitMethod_param(self, ctx: MiniGoParser.Method_paramContext):
        param_name = ctx.ID().getText()
        param_type = self.visit(ctx.type_name())
        return VariablesDecl(Id(param_name), param_type, None)


    ##
    def visitType_name(self, ctx: MiniGoParser.Type_nameContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        return VoidType()
    # Visit a parse tree produced by MiniGoParser#params_list.
    def visitParams_list(self, ctx: MiniGoParser.Params_listContext):
        if ctx.getChildCount() == 1:
            params = self.visit(ctx.param())
            return params if isinstance(params, list) else [params]
        return self.visit(ctx.param()) + self.visit(ctx.params_list())

    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx: MiniGoParser.ParamContext):
        typ = self.visit(ctx.type_name())
        return [VariablesDecl(Id(id.getText()), typ, None) for id in ctx.ID()]



    # Visit a parse tree produced by MiniGoParser#struct_declared.
    def visitStruct_declared(self, ctx: MiniGoParser.Struct_declaredContext):
        name = Id(ctx.ID().getText())
        fields = []
        if ctx.struct_type():
            fields = self.visit(ctx.struct_type())
        return StructDecl(name, fields)


    # Visit a parse tree produced by MiniGoParser#struct_type.
    def visitStruct_type(self, ctx: MiniGoParser.Struct_typeContext):
        if not ctx.children:
            return []
        return self.visit(ctx.struct_field()) + self.visit(ctx.struct_type())



    # Visit a parse tree produced by MiniGoParser#struct_field.
    def visitStruct_field(self, ctx: MiniGoParser.Struct_fieldContext):
        typ = self.visit(ctx.type_name())
        ids = [Id(ctx.ID().getText())]
        if ctx.more_ids():
            ids.extend([Id(id.getText()) for id in self.visit(ctx.more_ids())])
        return [VariablesDecl(id, typ, None) for id in ids]



    # Visit a parse tree produced by MiniGoParser#more_ids.
    def visitMore_ids(self, ctx: MiniGoParser.More_idsContext):
        if not ctx.children:
            return []
        return [ctx.ID()] + self.visit(ctx.more_ids())



    # Visit a parse tree produced by MiniGoParser#struct_end.
    def visitStruct_end(self, ctx:MiniGoParser.Struct_endContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declared.
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        name = Id(ctx.ID().getText())
        methods = []
        if ctx.interface_type():
            methods = self.visit(ctx.interface_type())
        return InterfaceDecl(name, methods)


    # Visit a parse tree produced by MiniGoParser#interface_type.
    def visitInterface_type(self, ctx:MiniGoParser.Interface_typeContext):
        if not ctx.children:
            return []
        return [self.visit(ctx.interface_method())] + self.visit(ctx.interface_type())



    # Visit a parse tree produced by MiniGoParser#interface_method.
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        name = Id(ctx.ID().getText())

        # Handle parameters
        params = []
        if ctx.optional_params() and ctx.optional_params().params_list():
            params = self.visit(ctx.optional_params().params_list())

        # Handle return type
        returnType = VoidType()
        if ctx.optional_type() and ctx.optional_type().type_name():
            returnType = self.visit(ctx.optional_type().type_name())

        return FunctionDecl(name, returnType, None, params, [])


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
    def visitDeclared_statement(self, ctx: MiniGoParser.Declared_statementContext):
        if ctx.variables_declared():
            return self.visit(ctx.variables_declared())
        else:
            return self.visit(ctx.constants_declared())


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx: MiniGoParser.Assign_statementContext):
        lhs = self.visit(ctx.assign_lhs()) if ctx.assign_lhs() else None
        op = ctx.assign_op().getText()
        exp = self.visit(ctx.expression())
        return AssignStmt(lhs, op, exp)


    # Visit a parse tree produced by MiniGoParser#assign_op.
    def visitAssign_op(self, ctx:MiniGoParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_lhs.
    def visitAssign_lhs(self, ctx:MiniGoParser.Assign_lhsContext):
        if ctx.ID():
            result = Id(ctx.ID().getText())
            if not ctx.field_access() and not ctx.element_access():
                return result

            for i in range(len(ctx.children)):
                child = ctx.children[i]
                if child.getRuleIndex() == MiniGoParser.RULE_element_access:
                    result = ArrayCell(result, self.visit(child))
                elif child.getRuleIndex() == MiniGoParser.RULE_field_access:
                    result = FieldAccess(result, self.visit(child))
            return result
        return None


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        # Get condition
        expr = self.visit(ctx.expression())

        # Get then statement block
        thenStmt = []
        if ctx.block_stmt(0):
            thenStmt = self.visit(ctx.block_stmt(0))
            if not isinstance(thenStmt, list):
                thenStmt = [thenStmt]

        elifStmt = None
        elseStmt = None

        if ctx.ELSE():
            if ctx.if_statement():
                # Handle else-if
                elif_if = self.visit(ctx.if_statement())
                if isinstance(elif_if, If):
                    elifStmt = [(elif_if.expr, elif_if.thenStmt)]
                    if elif_if.elifStmt:
                        elifStmt.extend(elif_if.elifStmt)
                    elseStmt = elif_if.elseStmt
            else:
                # Handle else block
                elseStmt = self.visit(ctx.block_stmt(1))
                if not isinstance(elseStmt, list):
                    elseStmt = [elseStmt]

        return If(expr, thenStmt, elifStmt, elseStmt)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        # Handle range-based for
        if ctx.SHORT_ASSIGN() and ctx.RANGE():
            index = Id(ctx.ID(0).getText())
            value = Id(ctx.ID(1).getText()) if ctx.ID(1) else None
            array = self.visit(ctx.expression())
            body = self.visit(ctx.block_stmt())
            if not isinstance(body, list):
                body = [body]
            return ForArray(index, value, array, body)

        # Handle traditional for loop
        init = None
        cond = None
        update = None

        if ctx.for_init():
            init = self.visit(ctx.for_init())
        if ctx.expression():
            cond = self.visit(ctx.expression())
        if ctx.for_update():
            update = self.visit(ctx.for_update())

        body = self.visit(ctx.block_stmt())
        if not isinstance(body, list):
            body = [body]
        return For(init, cond, update, body)


    # Visit a parse tree produced by MiniGoParser#for_init.
    def visitFor_init(self, ctx:MiniGoParser.For_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_update.
    def visitFor_update(self, ctx:MiniGoParser.For_updateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx: MiniGoParser.Break_statementContext):
        return Break()



    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx: MiniGoParser.Continue_statementContext):
        return Continue()


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx: MiniGoParser.Return_statementContext):
        expr = self.visit(ctx.expression()) if ctx.expression() else None
        return Return(expr)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        obj = None
        method = None

        # Get the method identifier
        if ctx.ID():
            # Direct function call
            method = Id(ctx.ID().getText())
        elif ctx.assign_lhs():
            # Method call on object
            obj = self.visit(ctx.assign_lhs())
            if ctx.ID():
                method = Id(ctx.ID().getText())
            elif isinstance(obj, FieldAccess):
                method = obj.fieldname
                obj = obj.obj

        # Get parameters
        params = []
        if ctx.list_expression():
            params = self.visit(ctx.list_expression())
            if not isinstance(params, list):
                params = [params]

        return CallStmt(obj, method, params)



    # Visit a parse tree produced by MiniGoParser#block_stmt.
    def visitBlock_stmt(self, ctx: MiniGoParser.Block_stmtContext):
        stmts = []
        for stmt_ctx in ctx.statement():
            stmt = self.visit(stmt_ctx)
            if isinstance(stmt, list):
                stmts.extend(stmt)
            else:
                stmts.append(stmt)
        return stmts

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
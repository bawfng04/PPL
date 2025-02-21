from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

##! continue update
class ASTGeneration(MiniGoVisitor):
    def getIntValue(self, text):
        if text.startswith('0b') or text.startswith('0B'):
            return int(text[2:], 2)
        elif text.startswith('0o') or text.startswith('0O'):
            return int(text[2:], 8)
        elif text.startswith('0x') or text.startswith('0X'):
            return int(text[2:], 16)
        else:
            return int(text)

    def visitProgram(self, ctx: MiniGoParser.ProgramContext):
        decl = []
        # Visit the first declaration if exists
        if ctx.declared():
            decl_ctx = ctx.declared()
            if decl_ctx.variables_declared():
                decl.append(self.visit(decl_ctx.variables_declared()))
            elif decl_ctx.constants_declared():
                decl.append(self.visit(decl_ctx.constants_declared()))
            elif decl_ctx.struct_declared():
                decl.append(self.visit(decl_ctx.struct_declared()))
            elif decl_ctx.function_declared():
                decl.append(self.visit(decl_ctx.function_declared()))
            elif decl_ctx.method_declared():
                decl.append(self.visit(decl_ctx.method_declared()))
            elif decl_ctx.interface_declared():
                decl.append(self.visit(decl_ctx.interface_declared()))

        # Visit remaining declarations
        if ctx.more_declared():
            more_decl = ctx.more_declared()
            while more_decl:
                if more_decl.declared():
                    decl_ctx = more_decl.declared()
                    if decl_ctx.variables_declared():
                        decl.append(self.visit(decl_ctx.variables_declared()))
                    elif decl_ctx.constants_declared():
                        decl.append(self.visit(decl_ctx.constants_declared()))
                    elif decl_ctx.struct_declared():
                        decl.append(self.visit(decl_ctx.struct_declared()))
                    elif decl_ctx.function_declared():
                        decl.append(self.visit(decl_ctx.function_declared()))
                    elif decl_ctx.method_declared():
                        decl.append(self.visit(decl_ctx.method_declared()))
                    elif decl_ctx.interface_declared():
                        decl.append(self.visit(decl_ctx.interface_declared()))
                more_decl = more_decl.more_declared()

        return Program(decl)

    def visitFunction_declared(self, ctx: MiniGoParser.Function_declaredContext):
        name = ctx.ID().getText()
        params = []
        if ctx.params_list():
            params = self.visit(ctx.params_list())

        returnType = VoidType()
        if ctx.return_type():
            returnType = self.visit(ctx.return_type())

        body = self.visit(ctx.block_stmt())
        return FuncDecl(name, params, returnType, body)

    def visitParams_list(self, ctx: MiniGoParser.Params_listContext):
        if ctx.type_name():
            # Case: ID type_name or ID comma_ids type_name
            typ = self.visit(ctx.type_name())
            params = [ParamDecl(ctx.ID().getText(), typ)]
            if ctx.comma_ids():
                more_ids = self.visit(ctx.comma_ids())
                if more_ids:  # Add null check
                    params.extend([ParamDecl(id, typ) for id in more_ids])
            return params
        elif ctx.param():
            # Case: param or param COMMA params_list
            params = self.visit(ctx.param())
            if ctx.params_list():
                more_params = self.visit(ctx.params_list())
                if more_params:  # Add null check
                    params.extend(more_params)
            return params
        return []

    def visitComma_ids(self, ctx: MiniGoParser.Comma_idsContext):
        if not ctx:
            return []
        ids = []
        if ctx.ID():
            ids.append(ctx.ID().getText())
            if ctx.comma_ids():
                more_ids = self.visit(ctx.comma_ids())
                if more_ids:  # Add null check
                    ids.extend(more_ids)
        return ids



    def visitParam(self, ctx: MiniGoParser.ParamContext):
        typ = self.visit(ctx.type_name())
        params = [ParamDecl(ctx.ID().getText(), typ)]
        if ctx.comma_param_ids():
            more_ids = self.visit(ctx.comma_param_ids())
            params.extend([ParamDecl(id, typ) for id in more_ids])
        return params

    def visitComma_param_ids(self, ctx: MiniGoParser.Comma_param_idsContext):
        ids = [ctx.ID().getText()]
        if ctx.comma_param_ids():
            ids.extend(self.visit(ctx.comma_param_ids()))
        return ids

    def visitReturn_type(self, ctx: MiniGoParser.Return_typeContext):
        if ctx.type_name():
            return self.visit(ctx.type_name())
        return None

    def visitMethod_declared(self, ctx: MiniGoParser.Method_declaredContext):
        # Get receiver name and type from receiver() rule
        receiver_name = ctx.receiver().ID(0).getText()
        receiver_type = Id(ctx.receiver().ID(1).getText()) if ctx.receiver().ID(1) else None

        # Get method name
        name = ctx.ID().getText()

        # Get parameters
        params = []
        if ctx.params_list():
            params = self.visit(ctx.params_list())

        # Get return type (default to VoidType if not specified)
        returnType = VoidType()
        if ctx.type_name():
            returnType = self.visit(ctx.type_name())

        # Get method body
        body = self.visit(ctx.block_stmt())

        # Create FuncDecl and wrap in MethodDecl
        func_decl = FuncDecl(name, params, returnType, body)
        return MethodDecl(receiver_name, receiver_type, func_decl)

    def visitInterface_declared(self, ctx: MiniGoParser.Interface_declaredContext):
        name = ctx.ID().getText()
        methods = []
        if ctx.interface_type_list():
            methods = self.visit(ctx.interface_type_list())
        return InterfaceType(name, methods)

    def visitInterface_type_list(self, ctx: MiniGoParser.Interface_type_listContext):
        methods = []
        if ctx.interface_method():
            methods.append(self.visit(ctx.interface_method()))
        if ctx.more_interface_methods():
            more_methods = ctx.more_interface_methods()
            while more_methods:
                if more_methods.interface_method():
                    methods.append(self.visit(more_methods.interface_method()))
                more_methods = more_methods.more_interface_methods()
        return methods

    def visitInterface_method(self, ctx: MiniGoParser.Interface_methodContext):
        name = ctx.ID().getText()
        params = []
        if ctx.params_list():
            param_list = self.visit(ctx.params_list())
            if param_list:  # Add null check
                params = [param.parType for param in param_list]

        returnType = VoidType()
        if ctx.type_name():
            returnType = self.visit(ctx.type_name())

        return Prototype(name, params, returnType)

    def visitBlock_stmt(self, ctx: MiniGoParser.Block_stmtContext):
        stmts = []
        if ctx.block_content():
            content = ctx.block_content()
            while content:
                if content.statement():
                    stmt = self.visit(content.statement())
                    if isinstance(stmt, list):
                        stmts.extend(stmt)
                    else:
                        stmts.append(stmt)
                content = content.block_content()
        return Block(stmts)

    def visitVariables_declared(self, ctx: MiniGoParser.Variables_declaredContext):
        # Visit the variable declaration inside variables_declared rule
        return self.visit(ctx.var_decl())

    def visitVar_decl(self, ctx: MiniGoParser.Var_declContext):
        # Get the variable name
        name = ctx.ID().getText()
        varType = None
        varInit = None
        # Check if there is an explicit type attached
        if ctx.type_name():
            varType = self.visit(ctx.type_name())
            # If varType is a tuple (from array_type), convert it to ArrayType
            if isinstance(varType, tuple):
                dimensions, base_type = varType
                varType = ArrayType(dimensions, base_type)
        # Check for an assignment expression
        if ctx.ASSIGN():
            varInit = self.visit(ctx.expression())
        return VarDecl(name, varType, varInit)

    def visitConstants_declared(self, ctx: MiniGoParser.Constants_declaredContext):
        # Visit the constant declaration list and return the first declaration
        return self.visit(ctx.const_decl_list())

    def visitConst_decl_list(self, ctx: MiniGoParser.Const_decl_listContext):
        # Visit the constant declaration and return it
        return self.visit(ctx.const_decl())

    def visitConst_decl(self, ctx: MiniGoParser.Const_declContext):
        # Create a constant declaration with name, type (None), and value
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        return ConstDecl(name, None, value)

    def visitExpression(self, ctx: MiniGoParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1())
        else:
            left = self.visit(ctx.expression())
            right = self.visit(ctx.expression1())
            op = "||"
            return BinaryOp(op, left, right)

    def visitExpression1(self, ctx: MiniGoParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2())
        else:
            left = self.visit(ctx.expression1())
            right = self.visit(ctx.expression2())
            op = "&&"
            return BinaryOp(op, left, right)

    def visitExpression2(self, ctx: MiniGoParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        else:
            left = self.visit(ctx.expression2())
            right = self.visit(ctx.expression3())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitExpression3(self, ctx: MiniGoParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        else:
            left = self.visit(ctx.expression3())
            right = self.visit(ctx.expression4())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitExpression4(self, ctx: MiniGoParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        else:
            left = self.visit(ctx.expression4())
            right = self.visit(ctx.expression5())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitExpression5(self, ctx: MiniGoParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        else:
            left = self.visit(ctx.expression5())
            right = self.visit(ctx.expression6())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitExpression6(self, ctx: MiniGoParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        else:
            op = ctx.getChild(0).getText()
            expr = self.visit(ctx.expression6())
            return UnaryOp(op, expr)

    def visitExpression7(self, ctx: MiniGoParser.Expression7Context):
        operand = self.visit(ctx.operand())
        if ctx.more_access_expr():
            return self.visitMore_access_expr(ctx.more_access_expr(), operand)
        return operand

    def visitMore_access_expr(self, ctx: MiniGoParser.More_access_exprContext, left):
        result = left
        # Process the current more_access_expr node:
        if ctx.field_access():
            field = ctx.field_access().ID().getText()
            result = FieldAccess(result, field)
        if ctx.call_expr():
            args = []
            if ctx.call_expr().list_expression():
                args = self.visit(ctx.call_expr().list_expression())
            if isinstance(result, FieldAccess):
                result = MethCall(result.receiver, result.field, args)
            elif isinstance(result, Id):
                result = FuncCall(result.name, args)
            else:
                result = MethCall(result, "call", args)
        if ctx.element_access():
            expr = self.visit(ctx.element_access().expression())
            result = ArrayCell(result, [expr])
        # Recurse if there is another access in the chain
        if ctx.more_access_expr():
            return self.visitMore_access_expr(ctx.more_access_expr(), result)
        return result

    def visitList_expression(self, ctx: MiniGoParser.List_expressionContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.list_expression())

    def visitOperand(self, ctx: MiniGoParser.OperandContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.expression())

    def visitLiteral(self, ctx: MiniGoParser.LiteralContext):
        if ctx.INT_LIT():
            text = ctx.INT_LIT().getText()
            if text.startswith('0b') or text.startswith('0B'):
                val = int(text[2:], 2)
            elif text.startswith('0o') or text.startswith('0O'):
                val = int(text[2:], 8)
            elif text.startswith('0x') or text.startswith('0X'):
                val = int(text[2:], 16)
            else:
                val = int(text)
            return IntLiteral(val)
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText()[1:-1])
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.typed_array_literal():
            return self.visit(ctx.typed_array_literal())
        elif ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        else:
            return NilLiteral()

    def visitStruct_literal(self, ctx: MiniGoParser.Struct_literalContext):
        name = ctx.ID().getText()
        fields = []
        if ctx.optional_field_list():
            if ctx.optional_field_list().field_list():
                fields = self.visit(ctx.optional_field_list().field_list())
        return StructLiteral(name, fields)

    def visitStruct_declared(self, ctx: MiniGoParser.Struct_declaredContext):
        # Get struct name
        name = ctx.ID().getText()
        elements = []
        methods = []

        # Visit struct type list if it exists
        if ctx.struct_type_list():
            elements = self.visit(ctx.struct_type_list())

        return StructType(name, elements, methods)


    def visitStruct_type_list(self, ctx: MiniGoParser.Struct_type_listContext):
        elements = []

        # Visit first struct field
        if ctx.struct_field():
            elements.extend(self.visit(ctx.struct_field()))

        # Visit remaining struct fields
        if ctx.more_struct_fields():
            more_fields = ctx.more_struct_fields()
            while more_fields:
                if more_fields.struct_field():
                    elements.extend(self.visit(more_fields.struct_field()))
                more_fields = more_fields.more_struct_fields()

        return elements

    def visitStruct_field(self, ctx: MiniGoParser.Struct_fieldContext):
        # Get field names
        names = [ctx.ID().getText()]

        # Get additional field names if they exist
        if ctx.more_ids():
            names.extend(self.visitMore_ids(ctx.more_ids()))

        # Get field type
        field_type = self.visit(ctx.type_name())

        # Create list of (name, type) tuples
        return [(name, field_type) for name in names]

    def visitMore_ids(self, ctx: MiniGoParser.More_idsContext):
        names = []
        if ctx.ID():
            names.append(ctx.ID().getText())
            if ctx.more_ids():
                names.extend(self.visitMore_ids(ctx.more_ids()))
        return names

    def visitField_list(self, ctx: MiniGoParser.Field_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.field_init())]
        return [self.visit(ctx.field_init())] + self.visit(ctx.field_list())

    def visitField_init(self, ctx: MiniGoParser.Field_initContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        return (name, value)

    def visitTyped_array_literal(self, ctx: MiniGoParser.Typed_array_literalContext):
        dimensions, base_type = self.visit(ctx.array_type())
        elements = self.visit(ctx.literal_list())
        return ArrayLiteral(dimensions, base_type, elements)

    def visitArray_type(self, ctx: MiniGoParser.Array_typeContext):
        if ctx.INT_LIT():
            first_dim = IntLiteral(int(ctx.INT_LIT().getText()))
        else:
            first_dim = Id(ctx.ID().getText())

        more_dims = []
        if ctx.more_dimensions():
            more_dims = self.visit(ctx.more_dimensions())

        base_type = self.visit(ctx.type_name())
        dims = [first_dim] + more_dims

        if isinstance(base_type, ArrayType):
            # If base_type is an ArrayType, merge its dimensions with current dimensions
            dims.extend(base_type.dimens)
            base_type = base_type.eleType

        return dims, base_type

    def visitMore_dimensions(self, ctx: MiniGoParser.More_dimensionsContext):
        if ctx.getChildCount() == 0:
            return []
        dimensions = []
        if ctx.INT_LIT():
            dimensions.append(IntLiteral(int(ctx.INT_LIT().getText())))
        else:
            dimensions.append(Id(ctx.ID().getText()))
        if ctx.more_dimensions():
            dimensions.extend(self.visitMore_dimensions(ctx.more_dimensions()))
        return dimensions

    def visitLiteral_list(self, ctx: MiniGoParser.Literal_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.literal_item())]
        return [self.visit(ctx.literal_item())] + self.visit(ctx.literal_list())

    def visitLiteral_item(self, ctx: MiniGoParser.Literal_itemContext):
        if ctx.untyped_array_literal():
            return self.visit(ctx.untyped_array_literal())
        elif ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        elif ctx.INT_LIT():
            text = ctx.INT_LIT().getText()
            return IntLiteral(self.getIntValue(text))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText()[1:-1])
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.ID():
            return Id(ctx.ID().getText())

    def visitUntyped_array_literal(self, ctx: MiniGoParser.Untyped_array_literalContext):
        return self.visit(ctx.literal_list())

    def visitType_name(self, ctx: MiniGoParser.Type_nameContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.array_type():
            dimensions, base_type = self.visit(ctx.array_type())
            return ArrayType(dimensions, base_type)

    def visitStatement(self, ctx: MiniGoParser.StatementContext):
        if ctx.declared_statement():
            return self.visit(ctx.declared_statement())
        elif ctx.assign_statement():
            return self.visit(ctx.assign_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.break_statement():
            return Break()
        elif ctx.continue_statement():
            return Continue()
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.call_statement():
            return self.visit(ctx.call_statement())

    def visitAssign_statement(self, ctx: MiniGoParser.Assign_statementContext):
        lhs = self.visit(ctx.assign_lhs())
        expr = self.visit(ctx.expression())
        op = ctx.assign_op().getText()

        if op == ':=':
            return Assign(lhs, expr)
        elif op in ['+=', '-=', '*=', '/=', '%=']:
            binOp = BinaryOp(op[0], lhs, expr)
            return Assign(lhs, binOp)
        else:  # op == '='
            return Assign(lhs, expr)

    def visitAssign_lhs(self, ctx: MiniGoParser.Assign_lhsContext):
        result = Id(ctx.ID().getText())
        if ctx.more_access():
            return self.visitMore_access(ctx.more_access(), result)
        return result

    def visitMore_access(self, ctx: MiniGoParser.More_accessContext, left):
        if not ctx:
            return left

        result = left
        if ctx.field_access():
            field = ctx.field_access().ID().getText()
            result = FieldAccess(result, field)
        if ctx.element_access():
            expr = self.visit(ctx.element_access().expression())
            result = ArrayCell(result, [expr])

        if ctx.more_access():
            return self.visitMore_access(ctx.more_access(), result)
        return result

    def visitIf_statement(self, ctx: MiniGoParser.If_statementContext):
        expr = self.visit(ctx.expression())
        thenStmt = self.visit(ctx.block_stmt())

        elifStmt = []
        elseStmt = None

        if ctx.ELSE():
            if ctx.if_statement():  # else if case
                elif_if = ctx.if_statement()
                while elif_if:
                    elif_expr = self.visit(elif_if.expression())
                    elif_block = self.visit(elif_if.block_stmt())
                    elifStmt.append((elif_expr, elif_block))

                    if elif_if.ELSE() and elif_if.if_statement():
                        elif_if = elif_if.if_statement()
                    else:
                        if elif_if.ELSE():
                            elseStmt = self.visit(elif_if.block_stmt(1))
                        break
            else:  # simple else case
                elseStmt = self.visit(ctx.block_stmt(1))

        return If(expr, thenStmt, elifStmt, elseStmt)

    def visitFor_statement(self, ctx: MiniGoParser.For_statementContext):
        if ctx.RANGE():  # For range
            idx = Id(ctx.ID(0).getText()) if ctx.ID(0) else None
            val = Id(ctx.ID(1).getText()) if ctx.ID(1) else None
            expr = self.visit(ctx.expression())
            block = self.visit(ctx.block_stmt())
            return ForEach(idx, val, expr, block)
        elif ctx.for_init():  # For with 3 parts
            init = self.visit(ctx.for_init())  # Get initialization
            cond = self.visit(ctx.expression()) # Get condition
            update = self.visit(ctx.for_update()) # Get update
            block = self.visit(ctx.block_stmt())  # Get loop body
            return ForStep(init, cond, update, block)
        else:  # Simple for
            expr = self.visit(ctx.expression())
            block = self.visit(ctx.block_stmt())
            return ForBasic(expr, block)

    def visitFor_init(self, ctx: MiniGoParser.For_initContext):
        if ctx.VAR():  # Case: var ID type? ASSIGN expression
            name = ctx.ID().getText()
            typ = self.visit(ctx.type_name()) if ctx.type_name() else None
            init = self.visit(ctx.expression())
            return VarDecl(name, typ, init)
        else:  # Case: ID assign_op expression
            lhs = Id(ctx.ID().getText())
            op = ctx.assign_op().getText()
            rhs = self.visit(ctx.expression())
            if op == ':=':
                return Assign(lhs, rhs)
            elif op in ['+=', '-=', '*=', '/=', '%=']:
                binOp = BinaryOp(op[0], lhs, rhs)
                return Assign(lhs, binOp)
            else:  # op == '='
                return Assign(lhs, rhs)

    def visitFor_update(self, ctx: MiniGoParser.For_updateContext):
        lhs = Id(ctx.ID().getText())
        op = ctx.assign_op().getText()
        rhs = self.visit(ctx.expression())
        if op == ':=':
            return Assign(lhs, rhs)
        elif op in ['+=', '-=', '*=', '/=', '%=']:
            binOp = BinaryOp(op[0], lhs, rhs)
            return Assign(lhs, binOp)
        else:  # op == '='
            return Assign(lhs, rhs)

    def visitReturn_statement(self, ctx: MiniGoParser.Return_statementContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        return Return(None)

    def visitCall_statement(self, ctx: MiniGoParser.Call_statementContext):
        if ctx.ID():  # Direct function call
            name = ctx.ID().getText()
            args = []
            if ctx.list_expression():
                args = self.visit(ctx.list_expression())
            return FuncCall(name, args)
        else:  # Method call through assign_lhs
            obj = self.visit(ctx.assign_lhs())
            args = []
            if ctx.list_expression():
                args = self.visit(ctx.list_expression())
            if isinstance(obj, FieldAccess):
                return MethCall(obj.receiver, obj.field, args)
            return MethCall(obj, "call", args)
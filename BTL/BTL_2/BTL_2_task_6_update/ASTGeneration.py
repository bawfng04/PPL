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
    # OK
    def visitProgram(self, ctx: MiniGoParser.ProgramContext):
        decl = []  # khai báo mảng decl = mảng các khai báo
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
        # Case 1: ID type_name (ASSIGN expression)?
        if ctx.type_name() and not ctx.type_name_ids() and not ctx.comma_ids():
            name = ctx.ID().getText()
            varType = self.visit(ctx.type_name())
            varInit = self.visit(ctx.expression()) if ctx.ASSIGN() else None
            return VarDecl(name, varType, varInit)

        # Case 2: ID type_name_ids type_name (ASSIGN expr_list)?
        elif ctx.type_name() and ctx.type_name_ids():
            varType = self.visit(ctx.type_name())
            names = [ctx.ID().getText()]
            if ctx.type_name_ids():
                names.extend(self.visit(ctx.type_name_ids()))

            varInits = []
            if ctx.ASSIGN():
                varInits = self.visit(ctx.expr_list())

            # Pad varInits with None if not enough initializers
            while len(varInits) < len(names):
                varInits.append(None)

            return [VarDecl(name, varType, init) for name, init in zip(names, varInits)]

        # Case 3: ID (ASSIGN expression)
        elif not ctx.type_name() and not ctx.comma_ids():
            name = ctx.ID().getText()
            varInit = self.visit(ctx.expression()) if ctx.ASSIGN() else None
            return VarDecl(name, None, varInit)

        # Case 4: ID comma_ids (ASSIGN expr_list)
        else:
            names = [ctx.ID().getText()]
            if ctx.comma_ids():
                names.extend(self.visit(ctx.comma_ids()))

            varInits = []
            if ctx.ASSIGN():
                varInits = self.visit(ctx.expr_list())

            # Pad varInits with None if not enough initializers
            while len(varInits) < len(names):
                varInits.append(None)

            return [VarDecl(name, None, init) for name, init in zip(names, varInits)]

    def visitConstants_declared(self, ctx: MiniGoParser.Constants_declaredContext):
        # Visit the constant declaration list and return the first declaration
        return self.visit(ctx.const_decl_list())

    def visitConst_decl_list(self, ctx: MiniGoParser.Const_decl_listContext):
        # Visit the constant declaration and return it
        return self.visit(ctx.const_decl())

    def visitConst_decl(self, ctx: MiniGoParser.Const_declContext):
        # Create a constant declaration with name, type (None), and value
        name = ctx.ID().getText() # lấy tên biến
        value = self.visit(ctx.expression()) # lấy giá trị
        return ConstDecl(name, None, value) # trả về một hằng số

    def visitExpression(self, ctx: MiniGoParser.ExpressionContext):
        if ctx.getChildCount() == 1: # nếu có 1 phần tử
            return self.visit(ctx.expression1()) # trả về phần tử đó
        else:
            left = self.visit(ctx.expression()) # lấy phần tử bên trái
            right = self.visit(ctx.expression1()) # lấy phần tử bên phải
            op = "||" # lấy toán tử
            return BinaryOp(op, left, right) # trả về một BinaryOp với toán tử và 2 phần tử

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
            left = self.visit(ctx.expression2()) # lấy phần tử bên trái
            right = self.visit(ctx.expression3()) # lấy phần tử bên phải
            op = ctx.getChild(1).getText() # lấy toán tử
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
        if not ctx:
            return left

        result = left
        # Process the current more_access_expr node:
        if ctx.field_access():
            field = ctx.field_access().ID().getText()
            result = FieldAccess(result, field)
        elif ctx.call_expr():
            args = []
            if ctx.call_expr().list_expression():
                args = self.visit(ctx.call_expr().list_expression())
            if isinstance(result, FieldAccess):
                result = MethCall(result.receiver, result.field, args)
            elif isinstance(result, Id):
                result = FuncCall(result.name, args)
            else:
                result = MethCall(result, "call", args)
        elif ctx.element_access():
            # Get the first dimension
            dimensions = [self.visit(ctx.element_access().expression())]

            # Process any additional array accesses in the chain before handling other access types
            next_access = ctx.more_access_expr()

            # Continue collecting dimensions as long as next access is element_access
            while next_access and next_access.element_access():
                dimensions.append(self.visit(next_access.element_access().expression()))
                next_access = next_access.more_access_expr()

            # Create the array cell with all dimensions
            result = ArrayCell(result, dimensions)

            # If there are still more accesses (like field access or call expr) after array accesses
            if next_access:
                return self.visitMore_access_expr(next_access, result)

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
        # Handle the case where ID() doesn't exist (field access or element access)
        if ctx.ID() is not None:
            result = Id(ctx.ID().getText())
            # Check for chained field/element accesses
            if ctx.field_access():
                field = ctx.field_access().ID().getText()
                result = FieldAccess(result, field)
            elif ctx.element_access():
                idx = self.visit(ctx.element_access().expression())
                result = ArrayCell(result, [idx])
            return result
        elif ctx.assign_lhs():
            # This is a recursive case where we have assign_lhs field_access or assign_lhs element_access
            base = self.visit(ctx.assign_lhs())
            if ctx.field_access():
                field = ctx.field_access().ID().getText()
                return FieldAccess(base, field)
            elif ctx.element_access():
                idx = self.visit(ctx.element_access().expression())
                if isinstance(base, ArrayCell):
                    # If already an array cell, add another dimension
                    base.idx.append(idx)
                    return base
                else:
                    return ArrayCell(base, [idx])
        return None  # Fallback case

    def visitMore_access(self, ctx: MiniGoParser.More_accessContext, left):
        if not ctx:
            return left

        result = left
        if ctx.field_access():
            field = ctx.field_access().ID().getText()
            result = FieldAccess(result, field)
        elif ctx.element_access():
            # Collect all dimensions
            dimensions = [self.visit(ctx.element_access().expression())]
            next_access = ctx.more_access()
            while next_access and next_access.element_access():
                dimensions.append(self.visit(next_access.element_access().expression()))
                next_access = next_access.more_access()
            result = ArrayCell(result, dimensions)
            if next_access:
                return self.visitMore_access(next_access, result)

        if ctx.more_access():
            return self.visitMore_access(ctx.more_access(), result)
        return result

    def visitIf_statement(self, ctx: MiniGoParser.If_statementContext):
        # Get condition
        expr = self.visit(ctx.expression())

        # Get then statement
        thenStmt = self.visit(ctx.block_stmt())

        # Handle else-if list and else part
        elseStmt = None

        if ctx.else_if_list():
            if_chain = ctx.else_if_list()
            current_if = None
            last_if = None

            while if_chain:
                if if_chain.else_if():
                    cond = self.visit(if_chain.else_if().expression())
                    then_block = self.visit(if_chain.else_if().block_stmt())
                    current_if = If(cond, then_block, None)

                    # If this is the first else-if in the chain, store it as the elseStmt
                    if elseStmt is None:
                        elseStmt = current_if
                    # Otherwise, link it to the else part of the last if
                    elif last_if is not None:
                        last_if.elseStmt = current_if

                    last_if = current_if
                    if_chain = if_chain.else_if_list()
                else:
                    break

            # Check for else part after processing all else-ifs
            if ctx.else_part() and last_if:
                last_if.elseStmt = self.visit(ctx.else_part())
        elif ctx.else_part():
            elseStmt = self.visit(ctx.else_part())

        return If(expr, thenStmt, elseStmt)

    def visitElse_if_list(self, ctx: MiniGoParser.Else_if_listContext):
        # Visit the first else-if to get its condition and then statement
        if ctx.else_if():
            expr = self.visit(ctx.else_if().expression())
            thenStmt = self.visit(ctx.else_if().block_stmt())

            # For the else part, check if there's another else-if or an else
            elseStmt = None
            if ctx.else_if_list():
                elseStmt = self.visit(ctx.else_if_list())

            # Return an If node with the condition, then statement, and else statement
            return If(expr, thenStmt, elseStmt)

        return None

    def visitElse_if(self, ctx: MiniGoParser.Else_ifContext):
        # Get condition
        expr = self.visit(ctx.expression())
        # Get then statement
        thenStmt = self.visit(ctx.block_stmt())
        # Return the condition and then statement, else part will be handled by the caller
        return expr, thenStmt

    def visitElse_part(self, ctx: MiniGoParser.Else_partContext):
        # Return the block statement of the else part
        return self.visit(ctx.block_stmt())


    def visitFor_statement(self, ctx: MiniGoParser.For_statementContext):
        if ctx.for_array():
            return self.visit(ctx.for_array())
        elif ctx.for_loop():
            return self.visit(ctx.for_loop())
        else:  # Basic for
            return self.visit(ctx.basic_for())

    def visitBasic_for(self, ctx: MiniGoParser.Basic_forContext):
        expr = self.visit(ctx.expression())
        block = self.visit(ctx.block_stmt())
        return ForBasic(expr, block)

    def visitFor_loop(self, ctx: MiniGoParser.For_loopContext):
        # Get init part
        if ctx.variables_for():
            init = self.visit(ctx.variables_for())
        else:  # assign_for
            init = self.visit(ctx.assign_for(0))

        # Get condition
        cond = self.visit(ctx.expression())

        # Get update - carefully get the second assign_for if it exists
        if len(ctx.assign_for()) > 1:
            update = self.visit(ctx.assign_for(1))
        else:
            # Use the first assign_for if there's only one
            update = self.visit(ctx.assign_for(0))

        # Get block
        block = self.visit(ctx.block_stmt())

        return ForStep(init, cond, update, block)


    def visitFor_array(self, ctx: MiniGoParser.For_arrayContext):
        # Check if we have index and value identifiers or underscores
        idx = Id(ctx.ID(0).getText()) if ctx.ID(0) else None
        val = Id(ctx.ID(1).getText()) if ctx.ID(1) else None

        # Get the expression to iterate over
        expr = self.visit(ctx.expression())

        # Get the loop block
        block = self.visit(ctx.block_stmt())

        return ForEach(idx, val, expr, block)

    def visitVariables_for(self, ctx: MiniGoParser.Variables_forContext):
        name = ctx.ID().getText()
        typ = self.visit(ctx.type_name()) if ctx.type_name() else None
        init = self.visit(ctx.expression())
        return VarDecl(name, typ, init)

    def visitAssign_for(self, ctx: MiniGoParser.Assign_forContext):
        lhs = Id(ctx.ID().getText())
        expr = self.visit(ctx.expression())
        op = ctx.assign_op().getText()

        if op == ':=':
            return Assign(lhs, expr)
        elif op in ['+=', '-=', '*=', '/=', '%=']:
            op_char = op[0]
            return Assign(lhs, BinaryOp(op_char, lhs, expr))
        else:  # op == '='
            return Assign(lhs, expr)

    # def visitFor_init(self, ctx: MiniGoParser.For_initContext):
    #     if ctx.VAR():  # var ID type? ASSIGN expression
    #         name = ctx.ID().getText()
    #         typ = self.visit(ctx.type_name()) if ctx.type_name() else None
    #         init = self.visit(ctx.expression())
    #         return VarDecl(name, typ, init)
    #     else:  # ID assign_op expression
    #         lhs = Id(ctx.ID().getText())
    #         expr = self.visit(ctx.expression())
    #         if ctx.assign_op():
    #             op = ctx.assign_op().getText()
    #             if op == ':=':
    #                 return Assign(lhs, expr)
    #             elif op in ['+=', '-=', '*=', '/=', '%=']:
    #                 binOp = BinaryOp(op[0], lhs, expr)
    #                 return Assign(lhs, binOp)
    #             else:  # op == '='
    #                 return Assign(lhs, expr)
    #         else:
    #             return Assign(lhs, expr)

    # def visitFor_update(self, ctx: MiniGoParser.For_updateContext):
    #     lhs = Id(ctx.ID().getText())
    #     op = ctx.assign_op().getText()
    #     rhs = self.visit(ctx.expression())
    #     if op == ':=':
    #         return Assign(lhs, rhs)
    #     elif op in ['+=', '-=', '*=', '/=', '%=']:
    #         # Convert to appropriate BinaryOp
    #         op_map = {
    #             '+=': '+',
    #             '-=': '-',
    #             '*=': '*',
    #             '/=': '/',
    #             '%=': '%'
    #         }
    #         return Assign(lhs, BinaryOp(op_map[op], lhs, rhs))
    #     else:
    #         return Assign(lhs, rhs)

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
        elif ctx.assign_lhs():  # Method call through assign_lhs
            obj = self.visit(ctx.assign_lhs())
            args = []
            if ctx.list_expression():
                args = self.visit(ctx.list_expression())
            if isinstance(obj, FieldAccess):
                return MethCall(obj.receiver, obj.field, args)
            return MethCall(obj, "call", args)
        return None  # Fallback case


    # Missing visitor methods:
    def visitList_statement(self, ctx: MiniGoParser.List_statementContext):
        """Used for handling sequences of statements"""
        if ctx.statement():
            if ctx.list_statement():
                return [self.visit(ctx.statement())] + self.visit(ctx.list_statement())
            return [self.visit(ctx.statement())]
        return []

    def visitDeclared_statement(self, ctx: MiniGoParser.Declared_statementContext):
        """Handles declarations that can appear as statements"""
        if ctx.variables_declared():
            return self.visit(ctx.variables_declared())
        elif ctx.constants_declared():
            return self.visit(ctx.constants_declared())
        elif ctx.struct_declared():
            return self.visit(ctx.struct_declared())
        elif ctx.function_declared():
            return self.visit(ctx.function_declared())
        elif ctx.method_declared():
            return self.visit(ctx.method_declared())
        elif ctx.interface_declared():
            return self.visit(ctx.interface_declared())
        return None

    def visitOptional_field_list(self, ctx: MiniGoParser.Optional_field_listContext):
        """Handles optional field lists in struct literals"""
        if ctx.field_list():
            return self.visit(ctx.field_list())
        return []

    def visitExpr_list(self, ctx: MiniGoParser.Expr_listContext):
        """Handles lists of expressions"""
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.expr_list())

    #OK
    def visitNewlines(self, ctx: MiniGoParser.NewlinesContext):
        return None

    def visitMore_declared(self, ctx: MiniGoParser.More_declaredContext):
        return self.visitChildren(ctx)

    def visitType_name_ids(self, ctx: MiniGoParser.Type_name_idsContext):
        return self.visitChildren(ctx)

    def visitMore_struct_fields(self, ctx: MiniGoParser.More_struct_fieldsContext):
        return self.visitChildren(ctx)

    def visitOpt_newlines(self, ctx: MiniGoParser.Opt_newlinesContext):
        return self.visitChildren(ctx)

    def visitMore_interface_methods(self, ctx: MiniGoParser.More_interface_methodsContext):
        return self.visitChildren(ctx)

    def visitAssign_op(self, ctx: MiniGoParser.Assign_opContext):
        return self.visitChildren(ctx)

    def visitBreak_statement(self, ctx: MiniGoParser.Break_statementContext):
        return Break()

    def visitContinue_statement(self, ctx: MiniGoParser.Continue_statementContext):
        return Continue()

    def visitBlock_content(self, ctx: MiniGoParser.Block_contentContext):
        statements = []
        if ctx.statement():
            stmt = self.visit(ctx.statement())
            if isinstance(stmt, list):
                statements.extend(stmt)
            else:
                statements.append(stmt)
        if ctx.block_content():
            next_content = self.visit(ctx.block_content())
            if next_content:
                statements.extend(next_content)
        return statements

    def visitElement_access(self, ctx: MiniGoParser.Element_accessContext):
        return self.visit(ctx.expression())

    def visitField_access(self, ctx: MiniGoParser.Field_accessContext):
        return ctx.ID().getText()

    def visitCall_expr(self, ctx: MiniGoParser.Call_exprContext):
        args = []
        if ctx.list_expression():
            args = self.visit(ctx.list_expression())
        return args

    def visitMore_types(self, ctx: MiniGoParser.More_typesContext):
        return self.visitChildren(ctx)

    def visitReceiver(self, ctx: MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)



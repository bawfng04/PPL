"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
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
        # Create list to store all declarations
        decl = []

        # Visit all declarations through the more_declared rule
        if ctx.declared():
            decl_ctx = ctx.declared()
            if decl_ctx.constants_declared():
                # Add constant declarations to the list
                decl.append(self.visit(decl_ctx.constants_declared()))

        # Visit remaining declarations
        if ctx.more_declared():
            more_decl = ctx.more_declared()
            while more_decl:
                if more_decl.declared():
                    decl_ctx = more_decl.declared()
                    if decl_ctx.constants_declared():
                        decl.append(self.visit(decl_ctx.constants_declared()))
                more_decl = more_decl.more_declared()

        return Program(decl)

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
            more_dims = self.visitMore_dimensions(ctx.more_dimensions())
        base_type = self.visit(ctx.type_name())
        dims = [first_dim] + more_dims
        if isinstance(base_type, tuple):
            dims += base_type[0]
            base_type = base_type[1]
        return (dims, base_type)

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
            return BooleanType()
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.array_type())
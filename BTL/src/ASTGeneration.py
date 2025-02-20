from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    def visitProgram(self, ctx: MiniGoParser.ProgramContext):
        const_name = ctx.ID().getText()
        expr = self.visit(ctx.expression())
        decl = ConstDecl(const_name, None, expr)
        return decl

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
        if ctx.getChildCount() == 0:
            return left

        if ctx.element_access():
            expr = self.visit(ctx.element_access().expression())
            left = ArrayCell(left, [expr])
        elif ctx.field_access():
            field = ctx.field_access().ID().getText()
            left = FieldAccess(left, field)
        elif ctx.call_expr(): # Modified this part
            args = []
            if ctx.call_expr().list_expression():
                args = self.visit(ctx.call_expr().list_expression())
            if isinstance(left, Id):
                left = FuncCall(left.name, args)
            else:
                method = "call"
                # Extract method name for method calls
                if isinstance(left, FieldAccess):
                    method = left.fieldname
                    left = left.obj
                left = MethCall(left, method, args)

        if ctx.more_access_expr():
            return self.visitMore_access_expr(ctx.more_access_expr(), left)

        return left

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
        else:
            return NilLiteral()
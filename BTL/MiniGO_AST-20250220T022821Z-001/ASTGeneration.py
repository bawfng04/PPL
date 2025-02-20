from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.declared()))

    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        if ctx.constants_declared():
            return self.visit(ctx.constants_declared())
        return []

    def visitConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        if ctx.const_decl():
            return self.visit(ctx.const_decl())
        return []

    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        return ConstDecl(name, None, value)

    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visitChildren(ctx)

    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.INT_LIT():
            text = ctx.INT_LIT().getText()
            if text.startswith('0b') or text.startswith('0B'):
                return IntLiteral(int(text[2:], 2))
            elif text.startswith('0o') or text.startswith('0O'):
                return IntLiteral(int(text[2:], 8))
            elif text.startswith('0x') or text.startswith('0X'):
                return IntLiteral(int(text[2:], 16))
            return IntLiteral(int(text))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()
        return self.visitChildren(ctx)
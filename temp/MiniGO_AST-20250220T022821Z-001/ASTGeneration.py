from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

# Class ASTGeneration kế thừa từ MiniGoVisitor
# Định nghĩa các phương thức duyệt Parse Tree -> Tạo ra cây AST
class ASTGeneration(MiniGoVisitor):
    # Xử lý nút gốc của Parse Tree, tạo ra đối tượng Program chứa danh sách các khai báo.
    def visitProgram(self, ctx: MiniGoParser.ProgramContext):
        """Convert parse tree to AST for program rule"""
        decl_list = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if child:
                node = self.visit(child)
                if node:
                    if isinstance(node, list):
                        decl_list.extend(node)
                    else:
                        decl_list.append(node)
        return Program(decl_list)

    def visitMore_declared(self, ctx: MiniGoParser.More_declaredContext):
        """Handle additional declarations"""
        if ctx.declared():
            decl_list = [self.visit(ctx.declared())]
            if ctx.more_declared():
                more_decls = self.visit(ctx.more_declared())
                if more_decls:
                    decl_list.extend(more_decls)
            return decl_list
        return []

    def visitDeclared(self, ctx: MiniGoParser.DeclaredContext):
        """Visit different types of declarations"""
        return self.visit(ctx.getChild(0))

    def visitVariables_declared(self, ctx: MiniGoParser.Variables_declaredContext):
        """Handle variable declarations"""
        return self.visit(ctx.var_decl())

    def visitVar_decl(self, ctx: MiniGoParser.Var_declContext):
        """Process variable declaration"""
        if ctx.type_name():
            # Single variable with type
            if ctx.expression():
                return VarDecl(ctx.ID().getText(),
                             self.visit(ctx.type_name()),
                             self.visit(ctx.expression()))
            return VarDecl(ctx.ID().getText(),
                          self.visit(ctx.type_name()),
                          None)
        # Single variable without type with initialization
        if ctx.expression():
            return VarDecl(ctx.ID().getText(),
                          None,
                          self.visit(ctx.expression()))
        # Multiple variables case
        return VarDecl(ctx.ID().getText(), None, None)

    def visitFunction_declared(self, ctx: MiniGoParser.Function_declaredContext):
        """Handle function declarations"""
        name = ctx.ID().getText()
        params = []
        if ctx.params_list():
            params = self.visit(ctx.params_list())
        return_type = VoidType()
        if ctx.return_type():
            return_type = self.visit(ctx.return_type())
        body = self.visit(ctx.block_stmt())
        return FuncDecl(name, params, return_type, body)

    def visitParams_list(self, ctx: MiniGoParser.Params_listContext):
        """Process function parameters"""
        if ctx.ID() and ctx.type_name():
            return [VarDecl(ctx.ID().getText(), self.visit(ctx.type_name()), None)]
        if ctx.param():
            param_list = [self.visit(ctx.param())]
            if ctx.params_list():
                param_list.extend(self.visit(ctx.params_list()))
            return param_list
        return []

    def visitType_name(self, ctx: MiniGoParser.Type_nameContext):
        """Convert type names to Type objects"""
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.array_type():
            return self.visit(ctx.array_type())
        # Only use ClassType if it's defined in AST.py
        if ctx.ID():
            return ClassType(ctx.ID().getText())
        return None

    def visitBlock_stmt(self, ctx: MiniGoParser.Block_stmtContext):
        """Process block statements"""
        stmt_list = []
        if ctx.block_content():
            stmts = self.visit(ctx.block_content())
            if stmts:
                stmt_list.extend(stmts)
        return Block(stmt_list)

    def visitBlock_content(self, ctx: MiniGoParser.Block_contentContext):
        """Handle block content"""
        if ctx.statement():
            stmt_list = [self.visit(ctx.statement())]
            if ctx.block_content():
                more_stmts = self.visit(ctx.block_content())
                if more_stmts:
                    stmt_list.extend(more_stmts)
            return stmt_list
        return []

    def visitIf_statement(self, ctx: MiniGoParser.If_statementContext):
        """Process if statements"""
        expr = self.visit(ctx.expression())
        thenStmt = self.visit(ctx.block_stmt(0))
        elseStmt = None
        if ctx.ELSE():
            if ctx.if_statement():  # else if case
                elseStmt = self.visit(ctx.if_statement())
            else:  # else case
                elseStmt = self.visit(ctx.block_stmt(1))
        return If(expr, thenStmt, elseStmt)

    def visitExpression(self, ctx: MiniGoParser.ExpressionContext):
        """Process expressions with OR operator"""
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1())
        left = self.visit(ctx.expression())
        right = self.visit(ctx.expression1())
        op = "||"
        return BinaryOp(op, left, right)

    def visitConstants_declared(self, ctx: MiniGoParser.Constants_declaredContext):
        """Process constant declarations"""
        return self.visit(ctx.const_decl_list())

    def visitStruct_declared(self, ctx: MiniGoParser.Struct_declaredContext):
        """Process struct declarations"""
        name = ctx.ID().getText()
        decl_list = []
        if ctx.struct_type_list():
            decl_list = self.visit(ctx.struct_type_list())
        return ClassDecl(name, decl_list)
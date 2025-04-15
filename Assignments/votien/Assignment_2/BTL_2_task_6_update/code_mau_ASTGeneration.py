from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

class ASTGeneration(MiniGoVisitor):
        def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
            return self.visitChildren(ctx)

        def visitLiteral_prim(self, ctx:MiniGoParser.Literal_primContext):
            if ctx.NIL():
                return NilLiteral()
            elif ctx.INT_LIT():
                return IntLiteral(ctx.INT_LIT().getText())
            elif ctx.FLOAT_LIT():
                return FloatLiteral(ctx.FLOAT_LIT().getText())
            elif ctx.TRUE():
                return BooleanLiteral(ctx.TRUE().getText())
            elif ctx.FALSE():
                return BooleanLiteral(ctx.FALSE().getText())
            return StringLiteral(ctx.STRING_LIT().getText())

        def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
            return ArrayLiteral(self.visit(ctx.dimensions()), self.visit(ctx.type_r()), self.visit(ctx.list_literal_array()))

        def visitList_literal_array(self, ctx:MiniGoParser.List_literal_arrayContext):
            return [self.visitChildren(ctx)] if ctx.getChildCount() == 1 else [self.visit(ctx.element_array())] + self.visit(ctx.list_literal_array())

        def visitElement_array(self, ctx:MiniGoParser.Element_arrayContext):
            if ctx.getChildCount() == 1:
                return self.visitChildren(ctx)
            return self.visit(ctx.list_literal_array())

        def visitDimensions(self, ctx:MiniGoParser.DimensionsContext):
            expr = None
            if ctx.INT_LIT():
                text = ctx.INT_LIT().getText()
                if text.startswith("0b") or text.startswith("0B"):  # Nhị phân
                    expr = IntLiteral(int(text, 2))
                elif text.startswith("0o") or text.startswith("0O"):  # Bát phân
                    expr =  IntLiteral(int(text, 8))
                elif text.startswith("0x") or text.startswith("0X"):  # Thập lục phân
                    expr =  IntLiteral(int(text, 16))
                else:  # Mặc định là thập phân
                    expr =  IntLiteral(int(text, 10))
            else:
                expr = Id(ctx.ID().getText())
            return [expr] if ctx.getChildCount() == 3 else [expr] + self.visit(ctx.dimensions())

        def visitType_r(self, ctx:MiniGoParser.Type_rContext):
            if ctx.INT():
                return IntType()
            elif ctx.FLOAT():
                return FloatType()
            elif ctx.BOOLEAN():
                return BoolType()
            elif ctx.STRING():
                return StringType()
            return Id(ctx.ID().getText())

        def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
            return StructLiteral(ctx.ID().getText(), self.visit(ctx.list_elements()) if ctx.list_elements() else [])

        def visitList_elements(self, ctx:MiniGoParser.List_elementsContext):
            return [self.visitChildren(ctx)] if ctx.getChildCount() == 1 else [self.visit(ctx.element())] + self.visit(ctx.list_elements())

        def visitElement(self, ctx:MiniGoParser.ElementContext):
            return (ctx.ID().getText(), self.visit(ctx.expression()))

        def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
            return [self.visitChildren(ctx)] if ctx.getChildCount() == 1 else [self.visit(ctx.expression())] + self.visit(ctx.list_expression())

        def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
            return self.visitChildren(ctx) if ctx.getChildCount() == 1 else BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression()),  self.visit(ctx.expression1())) 


        def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
            return self.visitChildren(ctx) if ctx.getChildCount() == 1 else BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression1()), self.visit(ctx.expression2()))

        def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
            return self.visitChildren(ctx) if ctx.getChildCount() == 1 else BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3())) 

        def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
            return self.visitChildren(ctx) if ctx.getChildCount() == 1 else BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4())) 

        def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
            return self.visitChildren(ctx) if ctx.getChildCount() == 1 else BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5())) 

        def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
            return self.visitChildren(ctx) if ctx.getChildCount() == 1 else UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expression5()))  

        def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
            if ctx.getChildCount() == 1:
                return self.visit(ctx.expression7())
            
            expression6 = self.visit(ctx.expression6())
            if ctx.expression():
                if type(expression6) == ArrayCell:
                    return ArrayCell(expression6.arr, expression6.idx  + [self.visit(ctx.expression())])
                return ArrayCell(expression6, [self.visit(ctx.expression())])
            elif ctx.getChildCount() == 3:
                return FieldAccess(expression6, ctx.ID().getText())
            return MethCall(expression6, ctx.ID().getText(), self.visit(ctx.list_expression()) if ctx.list_expression() else [])
            
        def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
            if ctx.ID():
                return Id(ctx.ID().getText())
            return self.visitChildren(ctx) if ctx.getChildCount() == 1 else self.visit(ctx.expression())

        def visitFuntion_call(self, ctx:MiniGoParser.Funtion_callContext):
            return FuncCall(ctx.ID().getText(), self.visit(ctx.list_expression()) if ctx.list_expression() else [])

        def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
            return [self.visitChildren(ctx)] if ctx.getChildCount() == 1 else [self.visit(ctx.statement())] + self.visit(ctx.list_statement())
        
        def visitStatement(self, ctx:MiniGoParser.StatementContext):
            return self.visit(ctx.getChild(0))

        def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
            return self.visitChildren(ctx)

        def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
            if ctx.SEMICOLON_ASSIGN():
                return Assign(self.visit(ctx.lhs()), self.visit(ctx.expression()))
            return Assign(self.visit(ctx.lhs()), BinaryOp(ctx.getChild(1).getText()[0], self.visit(ctx.lhs()), self.visit(ctx.expression()))) 

        def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
            return Break()

        def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
            return Continue()

        def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
            return Return(self.visitChildren(ctx) if ctx.expression() else None)
        
        def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
            if ctx.lhs():
                return MethCall(self.visit(ctx.lhs()), ctx.ID().getText(), self.visit(ctx.list_expression()) if ctx.list_expression() else [])
            return FuncCall(ctx.ID().getText(), self.visit(ctx.list_expression()) if ctx.list_expression() else [])

        def visitLhs(self, ctx:MiniGoParser.LhsContext):
            if ctx.getChildCount() == 1:
                return Id(ctx.ID().getText())
            elif ctx.LBRACK():
                lhs = self.visit(ctx.lhs())
                if type(lhs) == ArrayCell:
                    return ArrayCell(lhs.arr, lhs.idx  + [self.visit(ctx.expression())])
                return ArrayCell(lhs, [self.visit(ctx.expression())])
            return FieldAccess(self.visit(ctx.lhs()), ctx.ID().getText())

        def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
            list_else_if =  self.visit(ctx.list_else_if()) if ctx.list_else_if() else []
            if len(list_else_if) == 0:
                return If(
                    self.visit(ctx.expression()),
                    Block(self.visit(ctx.list_statement())),
                    self.visit(ctx.else_statement()) if ctx.else_statement() else None
                )
            
            def recursive_if(list_else_if_statement:List[Tuple[Expr,Block]], else_statement: Block):
                if len(list_else_if_statement) == 0:
                    return else_statement
                exp, block = list_else_if_statement[0]
                return If(exp, block, recursive_if(list_else_if_statement[1:], else_statement))

            return If(self.visit(ctx.expression()), Block(self.visit(ctx.list_statement())), recursive_if(list_else_if, self.visit(ctx.else_statement()) if ctx.else_statement() else None))
        
        def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
            return Block(self.visit(ctx.list_statement()) if ctx.list_statement() else [])
        
        def visitList_else_if(self, ctx:MiniGoParser.List_else_ifContext):
            return [self.visitChildren(ctx)] if ctx.getChildCount() == 1 else [self.visit(ctx.else_if())] + self.visit(ctx.list_else_if())
        
        def visitElse_if(self, ctx:MiniGoParser.Else_ifContext):
            return (self.visit(ctx.expression()), Block(self.visit(ctx.list_statement()) if ctx.list_statement() else []))

        def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
            return self.visitChildren(ctx)

        def visitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
            return ForBasic( self.visit(ctx.expression()), Block(self.visit(ctx.list_statement()) if ctx.list_statement() else []))

        def visitAssign_for(self, ctx:MiniGoParser.Assign_forContext):
            if ctx.SEMICOLON_ASSIGN():
                return Assign(Id(ctx.ID().getText()), self.visit(ctx.expression()))
            return Assign(Id(ctx.ID().getText()), BinaryOp(ctx.getChild(1).getText()[0], Id(ctx.ID().getText()), self.visit(ctx.expression()))) 

        def visitVariables_for(self, ctx:MiniGoParser.Variables_forContext):
            return VarDecl(
                ctx.ID().getText(),
                self.visit(ctx.type_minigo()) if ctx.type_minigo() else None,
                self.visit(ctx.expression())
            )

        def visitFor_loop(self, ctx:MiniGoParser.For_loopContext):
            return ForStep(
                self.visit(ctx.getChild(1)),
                self.visit(ctx.expression()),
                self.visit(ctx.assign_for()[1] if len(ctx.assign_for()) == 2 else ctx.assign_for()[0]),
                Block(self.visit(ctx.list_statement()) if ctx.list_statement() else [])
            )

        def visitFor_array(self, ctx:MiniGoParser.For_arrayContext):
            return ForEach(
                Id(ctx.ID()[0].getText()),
                Id(ctx.ID()[1].getText()),
                self.visit(ctx.expression()),
                Block(self.visit(ctx.list_statement()) if ctx.list_statement() else [])
            )

        def visitProgram(self, ctx:MiniGoParser.ProgramContext):
            return Program([self.visit(item) for item in ctx.declared()])

        def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
            return self.visitChildren(ctx)

        def visitVariables(self, ctx:MiniGoParser.VariablesContext):
            return VarDecl(
                ctx.ID().getText(),
                self.visit(ctx.type_minigo()) if ctx.type_minigo() else None,
                self.visit(ctx.expression()) if ctx.expression() else None,
            )

        def visitConstants(self, ctx:MiniGoParser.ConstantsContext):
            return ConstDecl(
                ctx.ID().getText(),
                None,
                self.visit(ctx.expression()) if ctx.expression() else None,   
            )

        def visitFunction(self, ctx:MiniGoParser.FunctionContext):
            return FuncDecl(
                ctx.ID().getText(),
                self.visit(ctx.list_param()) if ctx.list_param() else [],
                self.visit(ctx.type_minigo()) if ctx.type_minigo() else VoidType(),
                Block(self.visit(ctx.list_statement()) if ctx.list_statement() else Block([]))
            )   

        def visitMethod(self, ctx:MiniGoParser.MethodContext):
            return MethodDecl(
                ctx.ID()[0].getText(),
                Id(ctx.ID()[1].getText()),
                FuncDecl(
                    ctx.ID()[2].getText(),
                    self.visit(ctx.list_param()) if ctx.list_param() else [],
                    self.visit(ctx.type_minigo()) if ctx.type_minigo() else VoidType(),
                    Block(self.visit(ctx.list_statement()) if ctx.list_statement() else Block([]))
                )   
            )

        def visitStruct_type_declared(self, ctx:MiniGoParser.Struct_type_declaredContext):
            return StructType(
                ctx.ID().getText(),
                self.visit(ctx.list_fields()),
                []
            )

        def visitInterface_type_declared(self, ctx:MiniGoParser.Interface_type_declaredContext):
            return InterfaceType(
                ctx.ID().getText(),
                self.visit(ctx.list_method())
            )

        def visitType_minigo(self, ctx:MiniGoParser.Type_minigoContext):
            if ctx.dimensions():
                return ArrayType(self.visit(ctx.dimensions()), self.visit(ctx.type_r()))
            return self.visit(ctx.type_r())

        def visitList_fields(self, ctx:MiniGoParser.List_fieldsContext):
            return [self.visit(ctx.fields())] if ctx.getChildCount() == 2 else [self.visit(ctx.fields())] + self.visit(ctx.list_fields())

        def visitFields(self, ctx:MiniGoParser.FieldsContext):
            return (ctx.ID().getText(), self.visit(ctx.type_minigo()))

        def visitList_method(self, ctx:MiniGoParser.List_methodContext):
            return [self.visit(ctx.meth())] if ctx.getChildCount() == 2 else [self.visit(ctx.meth())] + self.visit(ctx.list_method())

        def visitMeth(self, ctx:MiniGoParser.MethContext):
            list_param = self.visit(ctx.list_param()) if ctx.list_param() else []
            return Prototype(
                ctx.ID().getText(),
                [item.parType for item in list_param],
                self.visit(ctx.type_minigo()) if ctx.type_minigo() else VoidType()
            )

        def visitList_param(self, ctx:MiniGoParser.List_paramContext):
            return self.visit(ctx.param()) if ctx.getChildCount() == 1 else self.visit(ctx.param()) + self.visit(ctx.list_param())

        def visitParam(self, ctx:MiniGoParser.ParamContext):
            list_ID = self.visit(ctx.list_ID())
            type_minigo = self.visit(ctx.type_minigo())
            return [ParamDecl(item, type_minigo) for item in list_ID] + (self.visit(ctx.param()) if ctx.param() else [])
        
        def visitList_ID(self, ctx:MiniGoParser.List_IDContext):
            return [ctx.ID().getText()] if ctx.getChildCount() == 1 else [ctx.ID().getText()] + self.visit(ctx.list_ID())
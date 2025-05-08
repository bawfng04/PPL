#2115257 Bui Le Van
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce


class ASTGeneration(MiniGoVisitor):
    

        def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
            if 1:
                return self.visitChildren(ctx)
            else: 
                return None

        def visitLiteral_prim(self, ctx:MiniGoParser.Literal_primContext):
            if 1 and ctx.NIL() :
                return NilLiteral()

            elif ctx.FALSE():
                return BooleanLiteral(ctx.FALSE().getText())
            elif ctx.FLOAT_LIT():
                van_float = ctx.FLOAT_LIT().getText()
                return FloatLiteral(float(van_float))
            elif 2 and ctx.TRUE():
                return BooleanLiteral(ctx.TRUE().getText())
            elif 1 and ctx.INT_LIT():
                Van_Text = ctx.INT_LIT().getText()
                return IntLiteral(int(Van_Text))
            Van_String = ctx.STRING_LIT().getText()
            return StringLiteral(Van_String)


        def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
            if 1:
                van_dimensions_part = self.visit(ctx.dimensions())
            van_type_primitive = self.visit(ctx.type_r())
            van_list_lit_ar = self.visit(ctx.list_literal_array())
            
            return ArrayLiteral(van_dimensions_part, van_type_primitive, van_list_lit_ar)


        def visitList_literal_array(self, ctx:MiniGoParser.List_literal_arrayContext):
            van_element_array = self.visit(ctx.element_array())
            if ctx.COMMA():
                list_lit = self.visit(ctx.list_literal_array())
                return [van_element_array] + list_lit
            else:
                return [van_element_array]


        def visitElement_array(self, ctx:MiniGoParser.Element_arrayContext):
            if ctx.getChildCount() + 1> 2:
                return self.visit(ctx.list_literal_array())
            elif 3 and ctx.struct_literal():
                return self.visit(ctx.struct_literal())
            return self.visit(ctx.literal_prim())
            
        def visitDimensions(self, ctx:MiniGoParser.DimensionsContext):
            if not ctx.dimensions():
                    return [self.visit(ctx.expression())]
            return [self.visit(ctx.expression())] + self.visit(ctx.dimensions())

        def visitType_r(self, ctx:MiniGoParser.Type_rContext):
            list_type = [IntType(), FloatType(), BoolType(), StringType()]
            if 1 and ctx.ID():
                idtext = ctx.ID().getText()
                return Id(idtext)
            elif 2 and ctx.STRING():
                return list_type[3]
            elif ctx.INT():
                return list_type[0]
            elif ctx.FLOAT():
                return list_type[1]
            return list_type[2]


        def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
            struct_name_van = ctx.ID().getText()
            if 3 and ctx.list_elements():
                res_list_elements = self.visit(ctx.list_elements())
                return StructLiteral(struct_name_van, res_list_elements)
            return StructLiteral(struct_name_van, [])


        def visitList_elements(self, ctx:MiniGoParser.List_elementsContext):
            if 1: 
                list_e = [self.visit(ctx.element())]

            if not ctx.getChildCount() == 3:
                return list_e
            return list_e + (self.visit(ctx.list_elements()))
                
            


        def visitElement(self, ctx:MiniGoParser.ElementContext):
            if 1:
                attr1 = ctx.ID().getText()
            attr2 = self.visit(ctx.expression())
            return (attr1, attr2)

        def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
            if ctx.list_expression():
                return [self.visit(ctx.expression())] + self.visit(ctx.list_expression())
            return [self.visit(ctx.expression())]


        def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
            if 1:
                e1 = self.visit(ctx.expression1())
            if ctx.getChildCount() + 1 > 2:
                ex = self.visit(ctx.expression())
                return BinaryOp(ctx.getChild(1).getText(), ex, e1)
            return e1


   
        def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
            if 1:
                ex2 = self.visit(ctx.expression2())
            if ctx.getChildCount() > 1:
                ex1 = self.visit(ctx.expression1())
                return BinaryOp(ctx.getChild(1).getText(), ex1, ex2)
            return ex2
        
     
        def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
            ex3 = self.visit(ctx.expression3())
            if ctx.getChildCount() == 1:
                return ex3
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression2()), ex3)  


      
        def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
            if 1 and ctx.getChildCount() == 1:
                return self.visitChildren(ctx)
            else:
                if ctx.getChildCount() != 1:
                    e3 = self.visit(ctx.expression3())
                    e4 = self.visit(ctx.expression4())
                    return BinaryOp(ctx.getChild(1).getText(), e3, e4)
                return None


     
        def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
            if 1 and ctx.getChildCount() - 1 == 0:
                return self.visitChildren(ctx)
            else:
                if ctx.getChildCount() != 1:
                    e4 = self.visit(ctx.expression4())
                    e5 = self.visit(ctx.expression5())
                    return BinaryOp(ctx.getChild(1).getText(), e4, e5)
                return None


       
        def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
            if ctx.getChildCount() - 1 == 0:    
                return self.visitChildren(ctx)
            if ctx.getChildCount() != 1:
                return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expression5()))


       
        def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
            if 2 and ctx.getChildCount() - 1 == 0:
                return self.visit(ctx.expression7())
            
            ex6 = self.visit(ctx.expression6())

            if ctx.expression():
                if 3 and isinstance(ex6, ArrayCell):
                    return ArrayCell(ex6.arr, ex6.idx  + [self.visit(ctx.expression())])
                return ArrayCell(ex6, [self.visit(ctx.expression())])
            if 1 and ctx.getChildCount() + 1== 4:
                return FieldAccess(ex6, ctx.ID().getText())
            list_param = []
            if 4 and ctx.list_expression():
                list_param = self.visit(ctx.list_expression())
            return MethCall(ex6, ctx.ID().getText(), list_param)
            

        # Visit a parse tree produced by MiniGoParser#expression7.
        def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
            if 1:
                a = 1
            if ctx.ID():
                return Id(ctx.ID().getText())
            if ctx.getChildCount() == 1:
                return self.visitChildren(ctx)
            if ctx.expression():
                return self.visit(ctx.expression())
            return None

        def visitFuntion_call(self, ctx:MiniGoParser.Funtion_callContext):
            if ctx.list_expression():
                return FuncCall(ctx.ID().getText(), self.visit(ctx.list_expression()))
            return FuncCall(ctx.ID().getText(), [])

      
        def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
            if ctx.getChildCount() -1 == 0:
                return [self.visitChildren(ctx)]
            return [self.visit(ctx.statement())] + self.visit(ctx.list_statement())
  
        def visitStatement(self, ctx:MiniGoParser.StatementContext):
            if 1 and ctx.getChild(1 - 1):
                child = ctx.getChild(0)
                return self.visit(child)
            return None

        def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
            return self.visitChildren(ctx)


      
        def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
            expr = self.visit(ctx.expression())
            if ctx.SEMICOLON_ASSIGN():
                return Assign(self.visit(ctx.lhs()), expr)
            lhs = None
            if ctx.lhs():
                lhs = self.visit(ctx.lhs())
            bin_op = BinaryOp(ctx.getChild(1).getText()[0], lhs, expr)
            return Assign(lhs, bin_op) 



        def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
            body = None
            if ctx.expression():
                body = self.visitChildren(ctx)
            return Return(body)

        
        def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
            if ctx.lhs() and ctx.DOT():
                lhs = self.visit(ctx.lhs())
                if ctx.list_expression():
                    return MethCall(lhs, ctx.ID().getText(), self.visit(ctx.list_expression()))
                return MethCall(lhs, ctx.ID().getText(), [])
            if ctx.list_expression():
                return FuncCall(ctx.ID().getText(), self.visit(ctx.list_expression()))
            return FuncCall(ctx.ID().getText(), [])
        
        def visitList_else_if(self, ctx:MiniGoParser.List_else_ifContext):
            if ctx.getChildCount() == 1:
                return [self.visitChildren(ctx)]
            return [self.visit(ctx.else_if())] + self.visit(ctx.list_else_if())
        
        def visitElse_if(self, ctx:MiniGoParser.Else_ifContext):
            expr = self.visit(ctx.expression())
            if ctx.list_statement():
                return (expr, Block(self.visit(ctx.list_statement())))
            return (expr, Block([]))

        def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
            vanchild = self.visitChildren(ctx)
            return vanchild

        def visitLhs(self, ctx:MiniGoParser.LhsContext):
            if ctx.getChildCount() == 1:
                return Id(ctx.ID().getText())
            if ctx.LBRACK():
                left_hand = self.visit(ctx.lhs())
                if isinstance(left_hand, ArrayCell):
                    return ArrayCell(left_hand.arr, left_hand.idx  + [self.visit(ctx.expression())])
                else:
                    return ArrayCell(left_hand, [self.visit(ctx.expression())])
            return FieldAccess(self.visit(ctx.lhs()), ctx.ID().getText())

        def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
            list_elif =  self.visit(ctx.list_else_if()) if ctx.list_else_if() else []
            if len(list_elif) == 0:
                return If(
                    self.visit(ctx.expression()),
                    Block(self.visit(ctx.list_statement())),
                    self.visit(ctx.else_statement()) if ctx.else_statement() else None
                )
            
            def xuli_elif(list_elif, elsest: Block):
                if list_elif == []:
                    return elsest
                expr, block = list_elif[0]
                return If(expr,block,xuli_elif(list_elif[1:], elsest))

            if ctx.else_statement():
                return If(
                        self.visit(ctx.expression()),
                        Block(self.visit(ctx.list_statement())),
                        xuli_elif(list_elif, self.visit(ctx.else_statement()))
                    )
            return If(
                    self.visit(ctx.expression()),
                    Block(self.visit(ctx.list_statement())),
                    xuli_elif(list_elif, None)
                )



 
        
        def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
            def have_list():
                return ctx.list_statement()
            if have_list():
                return Block(self.visit(ctx.list_statement()))
            return Block([])

            
        



        def visitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
            if ctx.list_statement():
                return ForBasic(
                    self.visit(ctx.expression()),
                    Block(self.visit(ctx.list_statement()))
                )
            return ForBasic(
                self.visit(ctx.expression()),
                Block([])
            )

        def visitAssign_for(self, ctx:MiniGoParser.Assign_forContext):
            ido = None 
            if ctx.ID():
                ido = Id(ctx.ID().getText())
            if ctx.SEMICOLON_ASSIGN():
                return Assign(ido, self.visit(ctx.expression()))
            return Assign(ido, BinaryOp(ctx.getChild(1).getText()[0], ido, self.visit(ctx.expression()))) 

        def visitVariables_for(self, ctx:MiniGoParser.Variables_forContext):
            return VarDecl(ctx.ID().getText(),self.visit(ctx.type_minigo()) if ctx.type_minigo() else None,self.visit(ctx.expression()))



        def visitFor_loop(self, ctx:MiniGoParser.For_loopContext):
            if ctx.list_statement():
                blockfor = Block(self.visit(ctx.list_statement()))
            else:
                blockfor = Block([])
            if  len(ctx.assign_for()) == 2:
                asfor = self.visit(ctx.assign_for()[1])
            else :
                asfor = self.visit(ctx.assign_for()[0])
            return ForStep(self.visit(ctx.getChild(1)),self.visit(ctx.expression()),asfor,blockfor)


        def visitFor_array(self, ctx:MiniGoParser.For_arrayContext):
            return ForEach(Id(ctx.ID()[0].getText()),Id(ctx.ID()[1].getText()),self.visit(ctx.expression()),
                Block(self.visit(ctx.list_statement()) if ctx.list_statement() else [])
            )


        def visitProgram(self, ctx:MiniGoParser.ProgramContext):
            decllist = []
            for itemdecl in ctx.declared():
                decl = self.visit(itemdecl)
                decllist.append(decl)
            return Program(decllist)


        def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
            return self.visitChildren(ctx)


        def visitVariables(self, ctx:MiniGoParser.VariablesContext):
            return VarDecl(
                ctx.ID().getText(),
                None if not ctx.type_minigo() else self.visit(ctx.type_minigo()),
                None if not ctx.expression() else self.visit(ctx.expression()),
            )

        def visitConstants(self, ctx:MiniGoParser.ConstantsContext):
            if ctx.expression():
                return ConstDecl(
                    ctx.ID().getText(),
                    None,
                    self.visit(ctx.expression())
                )
            return ConstDecl(
                ctx.ID().getText(),
                None,
                None,   
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
            def visit_list_fields():
                x = self.visit(ctx.list_fields())
                return x
            return StructType(
                ctx.ID().getText(),
                visit_list_fields(),
                []
            )

        def visitInterface_type_declared(self, ctx:MiniGoParser.Interface_type_declaredContext):
            def visit_list_meth_inteface():
                x = self.visit(ctx.list_meth_interface())
                return x
            return InterfaceType(
                ctx.ID().getText(),
               visit_list_meth_inteface()
            )

        def visitType_minigo(self, ctx:MiniGoParser.Type_minigoContext):
            def getype():
                return self.visit(ctx.type_r())
            typ = getype()
            if not ctx.dimensions():
                return typ
            return ArrayType(self.visit(ctx.dimensions()), typ)


        def visitList_fields(self, ctx:MiniGoParser.List_fieldsContext):
            def child_count():
                return ctx.getChildCount()
            if not child_count() == 2:
                return [self.visit(ctx.fields())] + self.visit(ctx.list_fields())
            return [self.visit(ctx.fields())]
            

     
        def visitFields(self, ctx:MiniGoParser.FieldsContext):
            return (ctx.ID().getText(), self.visit(ctx.type_minigo()))


    
        def visitList_meth_interface(self, ctx:MiniGoParser.List_meth_interfaceContext):
            def child_count():
                return ctx.getChildCount()
            if not child_count() == 2:
                return [self.visit(ctx.meth_interface())] + self.visit(ctx.list_meth_interface())
            return [self.visit(ctx.meth_interface())]
            
        def visitMeth_interface(self, ctx:MiniGoParser.Meth_interfaceContext):
            list_param = self.visit(ctx.list_param()) if ctx.list_param() else []
            list_param_par = []
            for item in list_param:
                list_param_par.append(item.parType)
            def getype():
                return self.visit(ctx.type_minigo()) if ctx.type_minigo() else VoidType()
            return Prototype(
                ctx.ID().getText(),
                list_param_par,
                getype()
            )

       
        def visitList_param(self, ctx:MiniGoParser.List_paramContext):
            par = self.visit(ctx.param())
            if not ctx.getChildCount() == 1:
                par.append(self.visit(ctx.list_param()))
            return par

        def visitParam(self, ctx:MiniGoParser.ParamContext):
            list_ID_van = self.visit(ctx.list_ID())
            type_minigo = self.visit(ctx.type_minigo())
            paramlist = []
            for item in list_ID_van:
                paramlist.append(ParamDecl(item, type_minigo))
            if ctx.COMMA():
                return paramlist + self.visit(ctx.param())
            return paramlist 


        def visitList_ID(self, ctx:MiniGoParser.List_IDContext):
            if ctx.COMMA():
                return [ctx.ID().getText()] + self.visit(ctx.list_ID())
            return [ctx.ID().getText()]
        
        def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
            if 1:
                return Break()
            return None

        def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
            if 1:
                return Continue()
            return None
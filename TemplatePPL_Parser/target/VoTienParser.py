# Generated from main/VoTien.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\6\2\32\n\2")
        buf.write("\r\2\16\2\33\3\2\3\2\3\3\3\3\5\3\"\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6\60\n\6\3\7\3\7\3")
        buf.write("\7\7\7\65\n\7\f\7\16\78\13\7\3\b\3\b\3\b\7\b=\n\b\f\b")
        buf.write("\16\b@\13\b\3\t\3\t\3\t\7\tE\n\t\f\t\16\tH\13\t\3\n\3")
        buf.write("\n\3\n\7\nM\n\n\f\n\16\nP\13\n\3\13\3\13\3\13\5\13U\n")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f]\n\f\3\f\2\2\r\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\2\4\3\2\4\5\3\2\6\7\2]\2\31\3\2\2")
        buf.write("\2\4!\3\2\2\2\6#\3\2\2\2\b\'\3\2\2\2\n,\3\2\2\2\f\61\3")
        buf.write("\2\2\2\169\3\2\2\2\20A\3\2\2\2\22I\3\2\2\2\24Q\3\2\2\2")
        buf.write("\26\\\3\2\2\2\30\32\5\4\3\2\31\30\3\2\2\2\32\33\3\2\2")
        buf.write("\2\33\31\3\2\2\2\33\34\3\2\2\2\34\35\3\2\2\2\35\36\7\2")
        buf.write("\2\3\36\3\3\2\2\2\37\"\5\6\4\2 \"\5\b\5\2!\37\3\2\2\2")
        buf.write("! \3\2\2\2\"\5\3\2\2\2#$\7\3\2\2$%\5\n\6\2%&\7\r\2\2&")
        buf.write("\7\3\2\2\2\'(\5\f\7\2()\7\t\2\2)*\5\16\b\2*+\7\r\2\2+")
        buf.write("\t\3\2\2\2,/\5\f\7\2-.\7\t\2\2.\60\5\16\b\2/-\3\2\2\2")
        buf.write("/\60\3\2\2\2\60\13\3\2\2\2\61\66\7\16\2\2\62\63\7\f\2")
        buf.write("\2\63\65\7\16\2\2\64\62\3\2\2\2\658\3\2\2\2\66\64\3\2")
        buf.write("\2\2\66\67\3\2\2\2\67\r\3\2\2\28\66\3\2\2\29>\5\20\t\2")
        buf.write(":;\7\f\2\2;=\5\20\t\2<:\3\2\2\2=@\3\2\2\2><\3\2\2\2>?")
        buf.write("\3\2\2\2?\17\3\2\2\2@>\3\2\2\2AF\5\22\n\2BC\t\2\2\2CE")
        buf.write("\5\22\n\2DB\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\21")
        buf.write("\3\2\2\2HF\3\2\2\2IN\5\24\13\2JK\t\3\2\2KM\5\24\13\2L")
        buf.write("J\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\23\3\2\2\2PN")
        buf.write("\3\2\2\2QT\5\26\f\2RS\7\b\2\2SU\5\26\f\2TR\3\2\2\2TU\3")
        buf.write("\2\2\2U\25\3\2\2\2V]\7\17\2\2W]\7\16\2\2XY\7\n\2\2YZ\5")
        buf.write("\20\t\2Z[\7\13\2\2[]\3\2\2\2\\V\3\2\2\2\\W\3\2\2\2\\X")
        buf.write("\3\2\2\2]\27\3\2\2\2\13\33!/\66>FNT\\")
        return buf.getvalue()


class VoTienParser ( Parser ):

    grammarFileName = "VoTien.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'+'", "'-'", "'*'", "'/'", "'**'", 
                     "'='", "'('", "')'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "INT", "ADD", "SUB", "MUL", "DIV", "EXP", 
                      "ASSIGNI", "LP", "RP", "CM", "SEM", "ID", "INT_LIT", 
                      "COMMENTS", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_stm = 1
    RULE_declaration = 2
    RULE_assignment = 3
    RULE_var_decl_list = 4
    RULE_var_list = 5
    RULE_expr_list = 6
    RULE_expression = 7
    RULE_term = 8
    RULE_factor = 9
    RULE_primary = 10

    ruleNames =  [ "program", "stm", "declaration", "assignment", "var_decl_list", 
                   "var_list", "expr_list", "expression", "term", "factor", 
                   "primary" ]

    EOF = Token.EOF
    INT=1
    ADD=2
    SUB=3
    MUL=4
    DIV=5
    EXP=6
    ASSIGNI=7
    LP=8
    RP=9
    CM=10
    SEM=11
    ID=12
    INT_LIT=13
    COMMENTS=14
    WS=15
    ERROR_CHAR=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(VoTienParser.EOF, 0)

        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VoTienParser.StmContext)
            else:
                return self.getTypedRuleContext(VoTienParser.StmContext,i)


        def getRuleIndex(self):
            return VoTienParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = VoTienParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.stm()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VoTienParser.INT or _la==VoTienParser.ID):
                    break

            self.state = 27
            self.match(VoTienParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(VoTienParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(VoTienParser.AssignmentContext,0)


        def getRuleIndex(self):
            return VoTienParser.RULE_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = VoTienParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stm)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VoTienParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.declaration()
                pass
            elif token in [VoTienParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.assignment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(VoTienParser.INT, 0)

        def var_decl_list(self):
            return self.getTypedRuleContext(VoTienParser.Var_decl_listContext,0)


        def SEM(self):
            return self.getToken(VoTienParser.SEM, 0)

        def getRuleIndex(self):
            return VoTienParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = VoTienParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(VoTienParser.INT)
            self.state = 34
            self.var_decl_list()
            self.state = 35
            self.match(VoTienParser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_list(self):
            return self.getTypedRuleContext(VoTienParser.Var_listContext,0)


        def ASSIGNI(self):
            return self.getToken(VoTienParser.ASSIGNI, 0)

        def expr_list(self):
            return self.getTypedRuleContext(VoTienParser.Expr_listContext,0)


        def SEM(self):
            return self.getToken(VoTienParser.SEM, 0)

        def getRuleIndex(self):
            return VoTienParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = VoTienParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.var_list()
            self.state = 38
            self.match(VoTienParser.ASSIGNI)
            self.state = 39
            self.expr_list()
            self.state = 40
            self.match(VoTienParser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_list(self):
            return self.getTypedRuleContext(VoTienParser.Var_listContext,0)


        def ASSIGNI(self):
            return self.getToken(VoTienParser.ASSIGNI, 0)

        def expr_list(self):
            return self.getTypedRuleContext(VoTienParser.Expr_listContext,0)


        def getRuleIndex(self):
            return VoTienParser.RULE_var_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_list" ):
                return visitor.visitVar_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_list(self):

        localctx = VoTienParser.Var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.var_list()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VoTienParser.ASSIGNI:
                self.state = 43
                self.match(VoTienParser.ASSIGNI)
                self.state = 44
                self.expr_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(VoTienParser.ID)
            else:
                return self.getToken(VoTienParser.ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(VoTienParser.CM)
            else:
                return self.getToken(VoTienParser.CM, i)

        def getRuleIndex(self):
            return VoTienParser.RULE_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = VoTienParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(VoTienParser.ID)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VoTienParser.CM:
                self.state = 48
                self.match(VoTienParser.CM)
                self.state = 49
                self.match(VoTienParser.ID)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VoTienParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(VoTienParser.ExpressionContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(VoTienParser.CM)
            else:
                return self.getToken(VoTienParser.CM, i)

        def getRuleIndex(self):
            return VoTienParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = VoTienParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.expression()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VoTienParser.CM:
                self.state = 56
                self.match(VoTienParser.CM)
                self.state = 57
                self.expression()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VoTienParser.TermContext)
            else:
                return self.getTypedRuleContext(VoTienParser.TermContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(VoTienParser.ADD)
            else:
                return self.getToken(VoTienParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(VoTienParser.SUB)
            else:
                return self.getToken(VoTienParser.SUB, i)

        def getRuleIndex(self):
            return VoTienParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = VoTienParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.term()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VoTienParser.ADD or _la==VoTienParser.SUB:
                self.state = 64
                _la = self._input.LA(1)
                if not(_la==VoTienParser.ADD or _la==VoTienParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 65
                self.term()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VoTienParser.FactorContext)
            else:
                return self.getTypedRuleContext(VoTienParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(VoTienParser.MUL)
            else:
                return self.getToken(VoTienParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(VoTienParser.DIV)
            else:
                return self.getToken(VoTienParser.DIV, i)

        def getRuleIndex(self):
            return VoTienParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = VoTienParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.factor()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VoTienParser.MUL or _la==VoTienParser.DIV:
                self.state = 72
                _la = self._input.LA(1)
                if not(_la==VoTienParser.MUL or _la==VoTienParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 73
                self.factor()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VoTienParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(VoTienParser.PrimaryContext,i)


        def EXP(self):
            return self.getToken(VoTienParser.EXP, 0)

        def getRuleIndex(self):
            return VoTienParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = VoTienParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.primary()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VoTienParser.EXP:
                self.state = 80
                self.match(VoTienParser.EXP)
                self.state = 81
                self.primary()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(VoTienParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(VoTienParser.ID, 0)

        def LP(self):
            return self.getToken(VoTienParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(VoTienParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(VoTienParser.RP, 0)

        def getRuleIndex(self):
            return VoTienParser.RULE_primary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = VoTienParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_primary)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VoTienParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(VoTienParser.INT_LIT)
                pass
            elif token in [VoTienParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(VoTienParser.ID)
                pass
            elif token in [VoTienParser.LP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.match(VoTienParser.LP)
                self.state = 87
                self.expression()
                self.state = 88
                self.match(VoTienParser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






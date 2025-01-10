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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("/\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\2\3\2\3\3\3\3\5\3\30\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\5\6+\n\6\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\3")
        buf.write("\3\2\n\13\2+\2\17\3\2\2\2\4\27\3\2\2\2\6\31\3\2\2\2\b")
        buf.write("\37\3\2\2\2\n*\3\2\2\2\f,\3\2\2\2\16\20\5\4\3\2\17\16")
        buf.write("\3\2\2\2\20\21\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22")
        buf.write("\23\3\2\2\2\23\24\7\2\2\3\24\3\3\2\2\2\25\30\5\6\4\2\26")
        buf.write("\30\5\b\5\2\27\25\3\2\2\2\27\26\3\2\2\2\30\5\3\2\2\2\31")
        buf.write("\32\7\3\2\2\32\33\7\n\2\2\33\34\7\5\2\2\34\35\5\n\6\2")
        buf.write("\35\36\7\t\2\2\36\7\3\2\2\2\37 \7\6\2\2 !\7\7\2\2!\"\5")
        buf.write("\n\6\2\"#\7\b\2\2#$\7\t\2\2$\t\3\2\2\2%&\5\f\7\2&\'\7")
        buf.write("\4\2\2\'(\5\n\6\2(+\3\2\2\2)+\5\f\7\2*%\3\2\2\2*)\3\2")
        buf.write("\2\2+\13\3\2\2\2,-\t\2\2\2-\r\3\2\2\2\5\21\27*")
        return buf.getvalue()


class VoTienParser ( Parser ):

    grammarFileName = "VoTien.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'+'", "'='", "'print'", "'('", 
                     "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "INT", "ADD", "ASSIGNI", "PRINT", "LP", 
                      "RP", "COMCOMMA", "ID", "INT_LIT", "COMMENTS", "WS", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declaration_statement = 2
    RULE_call_statement = 3
    RULE_expression = 4
    RULE_expression1 = 5

    ruleNames =  [ "program", "statement", "declaration_statement", "call_statement", 
                   "expression", "expression1" ]

    EOF = Token.EOF
    INT=1
    ADD=2
    ASSIGNI=3
    PRINT=4
    LP=5
    RP=6
    COMCOMMA=7
    ID=8
    INT_LIT=9
    COMMENTS=10
    WS=11
    ERROR_CHAR=12

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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VoTienParser.StatementContext)
            else:
                return self.getTypedRuleContext(VoTienParser.StatementContext,i)


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
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.statement()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VoTienParser.INT or _la==VoTienParser.PRINT):
                    break

            self.state = 17
            self.match(VoTienParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_statement(self):
            return self.getTypedRuleContext(VoTienParser.Declaration_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(VoTienParser.Call_statementContext,0)


        def getRuleIndex(self):
            return VoTienParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = VoTienParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VoTienParser.INT]:
                self.state = 19
                self.declaration_statement()
                pass
            elif token in [VoTienParser.PRINT]:
                self.state = 20
                self.call_statement()
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


    class Declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(VoTienParser.INT, 0)

        def ID(self):
            return self.getToken(VoTienParser.ID, 0)

        def ASSIGNI(self):
            return self.getToken(VoTienParser.ASSIGNI, 0)

        def expression(self):
            return self.getTypedRuleContext(VoTienParser.ExpressionContext,0)


        def COMCOMMA(self):
            return self.getToken(VoTienParser.COMCOMMA, 0)

        def getRuleIndex(self):
            return VoTienParser.RULE_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_statement" ):
                return visitor.visitDeclaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def declaration_statement(self):

        localctx = VoTienParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(VoTienParser.INT)
            self.state = 24
            self.match(VoTienParser.ID)
            self.state = 25
            self.match(VoTienParser.ASSIGNI)
            self.state = 26
            self.expression()
            self.state = 27
            self.match(VoTienParser.COMCOMMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(VoTienParser.PRINT, 0)

        def LP(self):
            return self.getToken(VoTienParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(VoTienParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(VoTienParser.RP, 0)

        def COMCOMMA(self):
            return self.getToken(VoTienParser.COMCOMMA, 0)

        def getRuleIndex(self):
            return VoTienParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = VoTienParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(VoTienParser.PRINT)
            self.state = 30
            self.match(VoTienParser.LP)
            self.state = 31
            self.expression()
            self.state = 32
            self.match(VoTienParser.RP)
            self.state = 33
            self.match(VoTienParser.COMCOMMA)
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

        def expression1(self):
            return self.getTypedRuleContext(VoTienParser.Expression1Context,0)


        def ADD(self):
            return self.getToken(VoTienParser.ADD, 0)

        def expression(self):
            return self.getTypedRuleContext(VoTienParser.ExpressionContext,0)


        def getRuleIndex(self):
            return VoTienParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = VoTienParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.expression1()
                self.state = 36
                self.match(VoTienParser.ADD)
                self.state = 37
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VoTienParser.ID, 0)

        def INT_LIT(self):
            return self.getToken(VoTienParser.INT_LIT, 0)

        def getRuleIndex(self):
            return VoTienParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = VoTienParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not(_la==VoTienParser.ID or _la==VoTienParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






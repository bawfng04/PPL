# Generated from /home/don/Code/Course/PPL/Template_BTL_PPL/main/VoTien.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,45,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,41,8,4,1,
        5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,1,1,0,8,9,41,0,13,1,0,0,0,2,21,1,
        0,0,0,4,23,1,0,0,0,6,29,1,0,0,0,8,40,1,0,0,0,10,42,1,0,0,0,12,14,
        3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,
        16,17,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,22,3,4,2,0,20,22,3,6,
        3,0,21,19,1,0,0,0,21,20,1,0,0,0,22,3,1,0,0,0,23,24,5,1,0,0,24,25,
        5,8,0,0,25,26,5,3,0,0,26,27,3,8,4,0,27,28,5,7,0,0,28,5,1,0,0,0,29,
        30,5,4,0,0,30,31,5,5,0,0,31,32,3,8,4,0,32,33,5,6,0,0,33,34,5,7,0,
        0,34,7,1,0,0,0,35,36,3,10,5,0,36,37,5,2,0,0,37,38,3,8,4,0,38,41,
        1,0,0,0,39,41,3,10,5,0,40,35,1,0,0,0,40,39,1,0,0,0,41,9,1,0,0,0,
        42,43,7,0,0,0,43,11,1,0,0,0,3,15,21,40
    ]

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
        self.checkVersion("4.13.1")
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
                if not (_la==1 or _la==4):
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




    def statement(self):

        localctx = VoTienParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 19
                self.declaration_statement()
                pass
            elif token in [4]:
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




    def expression1(self):

        localctx = VoTienParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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






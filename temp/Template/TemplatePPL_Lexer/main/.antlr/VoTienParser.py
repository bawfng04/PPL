# Generated from d:/Projects/PPL-Assignment/TemplatePPL_Lexer/main/VoTien.g4 by ANTLR 4.13.1
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
        4,1,43,14,2,0,7,0,1,0,1,0,5,0,5,8,0,10,0,12,0,8,9,0,3,0,10,8,0,1,
        0,1,0,1,0,0,0,1,0,0,0,14,0,9,1,0,0,0,2,10,5,32,0,0,3,5,5,43,0,0,
        4,3,1,0,0,0,5,8,1,0,0,0,6,4,1,0,0,0,6,7,1,0,0,0,7,10,1,0,0,0,8,6,
        1,0,0,0,9,2,1,0,0,0,9,6,1,0,0,0,10,11,1,0,0,0,11,12,5,0,0,1,12,1,
        1,0,0,0,2,6,9
    ]

class VoTienParser ( Parser ):

    grammarFileName = "VoTien.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'T'", "'F'", "'continue'", "'if'", "'else'", 
                     "'for'", "'bool'", "'number'", "'return'", "'string'", 
                     "'func'", "'endfunc'", "'call'", "'+'", "'-'", "'*'", 
                     "'='", "'<'", "'>'", "'**'", "'#'", "'<-'", "'['", 
                     "']'", "'('", "')'", "'{'", "'}'", "';'", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "T", "F", "CONTINUE", "IF", "ELSE", "FOR", 
                      "BOOL", "NUMBER", "RETURN", "STRING", "FUNC", "ENDFUNC", 
                      "CALL", "ADD", "SUB", "MUL", "EQUAL", "LT", "GT", 
                      "POW", "HASH", "ASSIGN", "LSB", "RSB", "LP", "RP", 
                      "LB", "RB", "SC", "COLON", "CM", "ID", "IDG", "INTEGER", 
                      "FLOAT", "STRING_LIT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_STRING" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    T=1
    F=2
    CONTINUE=3
    IF=4
    ELSE=5
    FOR=6
    BOOL=7
    NUMBER=8
    RETURN=9
    STRING=10
    FUNC=11
    ENDFUNC=12
    CALL=13
    ADD=14
    SUB=15
    MUL=16
    EQUAL=17
    LT=18
    GT=19
    POW=20
    HASH=21
    ASSIGN=22
    LSB=23
    RSB=24
    LP=25
    RP=26
    LB=27
    RB=28
    SC=29
    COLON=30
    CM=31
    ID=32
    IDG=33
    INTEGER=34
    FLOAT=35
    STRING_LIT=36
    WS=37
    LINE_COMMENT=38
    BLOCK_COMMENT=39
    ERROR_CHAR=40
    UNCLOSE_STRING=41
    ILLEGAL_ESCAPE=42
    ERROR_STRING=43

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

        def ID(self):
            return self.getToken(VoTienParser.ID, 0)

        def ERROR_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(VoTienParser.ERROR_STRING)
            else:
                return self.getToken(VoTienParser.ERROR_STRING, i)

        def getRuleIndex(self):
            return VoTienParser.RULE_program




    def program(self):

        localctx = VoTienParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.state = 2
                self.match(VoTienParser.ID)
                pass
            elif token in [-1, 43]:
                self.state = 6
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==43:
                    self.state = 3
                    self.match(VoTienParser.ERROR_STRING)
                    self.state = 8
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 11
            self.match(VoTienParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






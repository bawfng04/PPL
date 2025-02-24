# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("m\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\6\b+\n\b\r\b\16\b,\3\t\6\t\60\n\t\r\t\16\t\61\3\t")
        buf.write("\3\t\6\t\66\n\t\r\t\16\t\67\3\t\3\t\5\t<\n\t\3\t\6\t?")
        buf.write("\n\t\r\t\16\t@\5\tC\n\t\3\t\6\tF\n\t\r\t\16\tG\3\t\3\t")
        buf.write("\5\tL\n\t\3\t\6\tO\n\t\r\t\16\tP\5\tS\n\t\3\n\3\n\3\n")
        buf.write("\3\n\7\nY\n\n\f\n\16\n\\\13\n\3\n\3\n\3\13\6\13a\n\13")
        buf.write("\r\13\16\13b\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\2")
        buf.write("\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\3\2\b\4\2\f\f\17\17\3\2\62;\4\2GGgg\4\2")
        buf.write("--//\5\2\f\f\17\17))\5\2\13\f\17\17\"\"\2y\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2")
        buf.write("\2\2\5\37\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2\r")
        buf.write("\'\3\2\2\2\17*\3\2\2\2\21R\3\2\2\2\23T\3\2\2\2\25`\3\2")
        buf.write("\2\2\27f\3\2\2\2\31i\3\2\2\2\33k\3\2\2\2\35\36\7,\2\2")
        buf.write("\36\4\3\2\2\2\37 \7\61\2\2 \6\3\2\2\2!\"\7-\2\2\"\b\3")
        buf.write("\2\2\2#$\7/\2\2$\n\3\2\2\2%&\7*\2\2&\f\3\2\2\2\'(\7+\2")
        buf.write("\2(\16\3\2\2\2)+\t\2\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2")
        buf.write(",-\3\2\2\2-\20\3\2\2\2.\60\t\3\2\2/.\3\2\2\2\60\61\3\2")
        buf.write("\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2\2\63\65\7\60")
        buf.write("\2\2\64\66\t\3\2\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3")
        buf.write("\2\2\2\678\3\2\2\28B\3\2\2\29;\t\4\2\2:<\t\5\2\2;:\3\2")
        buf.write("\2\2;<\3\2\2\2<>\3\2\2\2=?\t\3\2\2>=\3\2\2\2?@\3\2\2\2")
        buf.write("@>\3\2\2\2@A\3\2\2\2AC\3\2\2\2B9\3\2\2\2BC\3\2\2\2CS\3")
        buf.write("\2\2\2DF\t\3\2\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2")
        buf.write("\2HI\3\2\2\2IK\t\4\2\2JL\t\5\2\2KJ\3\2\2\2KL\3\2\2\2L")
        buf.write("N\3\2\2\2MO\t\3\2\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3")
        buf.write("\2\2\2QS\3\2\2\2R/\3\2\2\2RE\3\2\2\2S\22\3\2\2\2TZ\7)")
        buf.write("\2\2UY\n\6\2\2VW\7)\2\2WY\7)\2\2XU\3\2\2\2XV\3\2\2\2Y")
        buf.write("\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[]\3\2\2\2\\Z\3\2\2\2]^")
        buf.write("\7)\2\2^\24\3\2\2\2_a\t\7\2\2`_\3\2\2\2ab\3\2\2\2b`\3")
        buf.write("\2\2\2bc\3\2\2\2cd\3\2\2\2de\b\13\2\2e\26\3\2\2\2fg\13")
        buf.write("\2\2\2gh\b\f\3\2h\30\3\2\2\2ij\13\2\2\2j\32\3\2\2\2kl")
        buf.write("\13\2\2\2l\34\3\2\2\2\20\2,\61\67;@BGKPRXZb\4\b\2\2\3")
        buf.write("\f\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    NEWLINE = 7
    REAL = 8
    STRING = 9
    WS = 10
    ERROR_CHAR = 11
    UNCLOSE_STRING = 12
    ILLEGAL_ESCAPE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "REAL", "STRING", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "NEWLINE", 
                  "REAL", "STRING", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[10] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     



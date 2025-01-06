# Generated from main/VoTien.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("P\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\7\t\62\n\t\f\t\16\t\65")
        buf.write("\13\t\3\n\6\n8\n\n\r\n\16\n9\3\13\3\13\3\13\3\13\7\13")
        buf.write("@\n\13\f\13\16\13C\13\13\3\13\3\13\3\f\6\fH\n\f\r\f\16")
        buf.write("\fI\3\f\3\f\3\r\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\3\2\7\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\3\2\62;\3\2\f\f\5\2\n\f\16\17\"\"\2S\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2")
        buf.write("\5\37\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13)\3\2\2\2\r+\3\2")
        buf.write("\2\2\17-\3\2\2\2\21/\3\2\2\2\23\67\3\2\2\2\25;\3\2\2\2")
        buf.write("\27G\3\2\2\2\31M\3\2\2\2\33\34\7k\2\2\34\35\7p\2\2\35")
        buf.write("\36\7v\2\2\36\4\3\2\2\2\37 \7-\2\2 \6\3\2\2\2!\"\7?\2")
        buf.write("\2\"\b\3\2\2\2#$\7r\2\2$%\7t\2\2%&\7k\2\2&\'\7p\2\2\'")
        buf.write("(\7v\2\2(\n\3\2\2\2)*\7*\2\2*\f\3\2\2\2+,\7+\2\2,\16\3")
        buf.write("\2\2\2-.\7=\2\2.\20\3\2\2\2/\63\t\2\2\2\60\62\t\3\2\2")
        buf.write("\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2")
        buf.write("\2\64\22\3\2\2\2\65\63\3\2\2\2\668\t\4\2\2\67\66\3\2\2")
        buf.write("\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:\24\3\2\2\2;<\7%\2")
        buf.write("\2<=\7%\2\2=A\3\2\2\2>@\n\5\2\2?>\3\2\2\2@C\3\2\2\2A?")
        buf.write("\3\2\2\2AB\3\2\2\2BD\3\2\2\2CA\3\2\2\2DE\b\13\2\2E\26")
        buf.write("\3\2\2\2FH\t\6\2\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2")
        buf.write("\2\2JK\3\2\2\2KL\b\f\2\2L\30\3\2\2\2MN\13\2\2\2NO\b\r")
        buf.write("\3\2O\32\3\2\2\2\7\2\639AI\4\b\2\2\3\r\2")
        return buf.getvalue()


class VoTienLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    ADD = 2
    ASSIGNI = 3
    PRINT = 4
    LP = 5
    RP = 6
    COMCOMMA = 7
    ID = 8
    INT_LIT = 9
    COMMENTS = 10
    WS = 11
    ERROR_CHAR = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'+'", "'='", "'print'", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ADD", "ASSIGNI", "PRINT", "LP", "RP", "COMCOMMA", "ID", 
            "INT_LIT", "COMMENTS", "WS", "ERROR_CHAR" ]

    ruleNames = [ "INT", "ADD", "ASSIGNI", "PRINT", "LP", "RP", "COMCOMMA", 
                  "ID", "INT_LIT", "COMMENTS", "WS", "ERROR_CHAR" ]

    grammarFileName = "VoTien.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[11] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     



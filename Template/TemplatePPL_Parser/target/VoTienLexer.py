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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\7\r?\n\r\f\r\16")
        buf.write("\rB\13\r\3\16\6\16E\n\16\r\16\16\16F\3\17\3\17\3\17\3")
        buf.write("\17\7\17M\n\17\f\17\16\17P\13\17\3\17\3\17\3\20\6\20U")
        buf.write("\n\20\r\20\16\20V\3\20\3\20\3\21\3\21\3\21\2\2\22\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22\3\2\7\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\3\2\62;\3\2\f\f\5\2\n\f\16\17\"\"\2`\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5\'\3\2\2\2\7)\3\2")
        buf.write("\2\2\t+\3\2\2\2\13-\3\2\2\2\r/\3\2\2\2\17\62\3\2\2\2\21")
        buf.write("\64\3\2\2\2\23\66\3\2\2\2\258\3\2\2\2\27:\3\2\2\2\31<")
        buf.write("\3\2\2\2\33D\3\2\2\2\35H\3\2\2\2\37T\3\2\2\2!Z\3\2\2\2")
        buf.write("#$\7k\2\2$%\7p\2\2%&\7v\2\2&\4\3\2\2\2\'(\7-\2\2(\6\3")
        buf.write("\2\2\2)*\7/\2\2*\b\3\2\2\2+,\7,\2\2,\n\3\2\2\2-.\7\61")
        buf.write("\2\2.\f\3\2\2\2/\60\7,\2\2\60\61\7,\2\2\61\16\3\2\2\2")
        buf.write("\62\63\7?\2\2\63\20\3\2\2\2\64\65\7*\2\2\65\22\3\2\2\2")
        buf.write("\66\67\7+\2\2\67\24\3\2\2\289\7.\2\29\26\3\2\2\2:;\7=")
        buf.write("\2\2;\30\3\2\2\2<@\t\2\2\2=?\t\3\2\2>=\3\2\2\2?B\3\2\2")
        buf.write("\2@>\3\2\2\2@A\3\2\2\2A\32\3\2\2\2B@\3\2\2\2CE\t\4\2\2")
        buf.write("DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\34\3\2\2\2H")
        buf.write("I\7%\2\2IJ\7%\2\2JN\3\2\2\2KM\n\5\2\2LK\3\2\2\2MP\3\2")
        buf.write("\2\2NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PN\3\2\2\2QR\b\17\2")
        buf.write("\2R\36\3\2\2\2SU\t\6\2\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2")
        buf.write("VW\3\2\2\2WX\3\2\2\2XY\b\20\2\2Y \3\2\2\2Z[\13\2\2\2[")
        buf.write("\\\b\21\3\2\\\"\3\2\2\2\7\2@FNV\4\b\2\2\3\21\2")
        return buf.getvalue()


class VoTienLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    EXP = 6
    ASSIGNI = 7
    LP = 8
    RP = 9
    CM = 10
    SEM = 11
    ID = 12
    INT_LIT = 13
    COMMENTS = 14
    WS = 15
    ERROR_CHAR = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'+'", "'-'", "'*'", "'/'", "'**'", "'='", "'('", "')'", 
            "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ADD", "SUB", "MUL", "DIV", "EXP", "ASSIGNI", "LP", "RP", 
            "CM", "SEM", "ID", "INT_LIT", "COMMENTS", "WS", "ERROR_CHAR" ]

    ruleNames = [ "INT", "ADD", "SUB", "MUL", "DIV", "EXP", "ASSIGNI", "LP", 
                  "RP", "CM", "SEM", "ID", "INT_LIT", "COMMENTS", "WS", 
                  "ERROR_CHAR" ]

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
            actions[15] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     



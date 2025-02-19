# Generated from d:/Projects/PPL-Assignment/TemplatePPL_Parser/main/VoTien.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,16,91,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,
        1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,
        11,1,11,5,11,61,8,11,10,11,12,11,64,9,11,1,12,4,12,67,8,12,11,12,
        12,12,68,1,13,1,13,1,13,1,13,5,13,75,8,13,10,13,12,13,78,9,13,1,
        13,1,13,1,14,4,14,83,8,14,11,14,12,14,84,1,14,1,14,1,15,1,15,1,15,
        0,0,16,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,
        25,13,27,14,29,15,31,16,1,0,5,3,0,65,90,95,95,97,122,4,0,48,57,65,
        90,95,95,97,122,1,0,48,57,1,0,10,10,3,0,8,10,12,13,32,32,94,0,1,
        1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,
        0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,
        0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,
        0,0,1,33,1,0,0,0,3,37,1,0,0,0,5,39,1,0,0,0,7,41,1,0,0,0,9,43,1,0,
        0,0,11,45,1,0,0,0,13,48,1,0,0,0,15,50,1,0,0,0,17,52,1,0,0,0,19,54,
        1,0,0,0,21,56,1,0,0,0,23,58,1,0,0,0,25,66,1,0,0,0,27,70,1,0,0,0,
        29,82,1,0,0,0,31,88,1,0,0,0,33,34,5,105,0,0,34,35,5,110,0,0,35,36,
        5,116,0,0,36,2,1,0,0,0,37,38,5,43,0,0,38,4,1,0,0,0,39,40,5,45,0,
        0,40,6,1,0,0,0,41,42,5,42,0,0,42,8,1,0,0,0,43,44,5,47,0,0,44,10,
        1,0,0,0,45,46,5,42,0,0,46,47,5,42,0,0,47,12,1,0,0,0,48,49,5,61,0,
        0,49,14,1,0,0,0,50,51,5,40,0,0,51,16,1,0,0,0,52,53,5,41,0,0,53,18,
        1,0,0,0,54,55,5,44,0,0,55,20,1,0,0,0,56,57,5,59,0,0,57,22,1,0,0,
        0,58,62,7,0,0,0,59,61,7,1,0,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,
        1,0,0,0,62,63,1,0,0,0,63,24,1,0,0,0,64,62,1,0,0,0,65,67,7,2,0,0,
        66,65,1,0,0,0,67,68,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,26,1,
        0,0,0,70,71,5,35,0,0,71,72,5,35,0,0,72,76,1,0,0,0,73,75,8,3,0,0,
        74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,1,
        0,0,0,78,76,1,0,0,0,79,80,6,13,0,0,80,28,1,0,0,0,81,83,7,4,0,0,82,
        81,1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,
        0,86,87,6,14,0,0,87,30,1,0,0,0,88,89,9,0,0,0,89,90,6,15,1,0,90,32,
        1,0,0,0,5,0,62,68,76,84,2,6,0,0,1,15,0
    ]

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
        self.checkVersion("4.13.1")
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
     



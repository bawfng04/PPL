# Generated from d:/Projects/PPL-Assignment/TemplatePPL_Parser/main/VoTien.g4 by ANTLR 4.13.1
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
        4,1,16,127,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,1,0,1,1,1,1,3,1,38,8,1,1,2,1,2,1,
        2,1,2,1,3,1,3,3,3,46,8,3,1,4,1,4,1,4,3,4,51,8,4,1,5,1,5,1,5,1,5,
        1,5,5,5,58,8,5,10,5,12,5,61,9,5,1,5,1,5,3,5,65,8,5,1,6,1,6,3,6,69,
        8,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,5,8,81,8,8,10,8,12,8,
        84,9,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,93,8,9,10,9,12,9,96,9,9,1,
        10,1,10,1,10,5,10,101,8,10,10,10,12,10,104,9,10,1,11,1,11,1,11,5,
        11,109,8,11,10,11,12,11,112,9,11,1,12,1,12,1,12,3,12,117,8,12,1,
        13,1,13,1,13,1,13,1,13,1,13,3,13,125,8,13,1,13,0,0,14,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,0,2,1,0,2,3,1,0,4,5,126,0,29,1,0,0,0,
        2,37,1,0,0,0,4,39,1,0,0,0,6,45,1,0,0,0,8,47,1,0,0,0,10,52,1,0,0,
        0,12,68,1,0,0,0,14,70,1,0,0,0,16,75,1,0,0,0,18,89,1,0,0,0,20,97,
        1,0,0,0,22,105,1,0,0,0,24,113,1,0,0,0,26,124,1,0,0,0,28,30,3,2,1,
        0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,33,
        1,0,0,0,33,34,5,0,0,1,34,1,1,0,0,0,35,38,3,4,2,0,36,38,3,12,6,0,
        37,35,1,0,0,0,37,36,1,0,0,0,38,3,1,0,0,0,39,40,5,1,0,0,40,41,3,6,
        3,0,41,42,5,11,0,0,42,5,1,0,0,0,43,46,3,8,4,0,44,46,3,10,5,0,45,
        43,1,0,0,0,45,44,1,0,0,0,46,7,1,0,0,0,47,50,5,12,0,0,48,49,5,7,0,
        0,49,51,3,20,10,0,50,48,1,0,0,0,50,51,1,0,0,0,51,9,1,0,0,0,52,53,
        5,12,0,0,53,54,5,10,0,0,54,59,5,12,0,0,55,56,5,10,0,0,56,58,5,12,
        0,0,57,55,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,64,
        1,0,0,0,61,59,1,0,0,0,62,63,5,7,0,0,63,65,3,18,9,0,64,62,1,0,0,0,
        64,65,1,0,0,0,65,11,1,0,0,0,66,69,3,14,7,0,67,69,3,16,8,0,68,66,
        1,0,0,0,68,67,1,0,0,0,69,13,1,0,0,0,70,71,5,12,0,0,71,72,5,7,0,0,
        72,73,3,20,10,0,73,74,5,11,0,0,74,15,1,0,0,0,75,76,5,12,0,0,76,77,
        5,10,0,0,77,82,5,12,0,0,78,79,5,10,0,0,79,81,5,12,0,0,80,78,1,0,
        0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,
        1,0,0,0,85,86,5,7,0,0,86,87,3,18,9,0,87,88,5,11,0,0,88,17,1,0,0,
        0,89,94,3,20,10,0,90,91,5,10,0,0,91,93,3,20,10,0,92,90,1,0,0,0,93,
        96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,19,1,0,0,0,96,94,1,0,0,
        0,97,102,3,22,11,0,98,99,7,0,0,0,99,101,3,22,11,0,100,98,1,0,0,0,
        101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,21,1,0,0,0,104,
        102,1,0,0,0,105,110,3,24,12,0,106,107,7,1,0,0,107,109,3,24,12,0,
        108,106,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,
        111,23,1,0,0,0,112,110,1,0,0,0,113,116,3,26,13,0,114,115,5,6,0,0,
        115,117,3,26,13,0,116,114,1,0,0,0,116,117,1,0,0,0,117,25,1,0,0,0,
        118,125,5,12,0,0,119,125,5,13,0,0,120,121,5,8,0,0,121,122,3,20,10,
        0,122,123,5,9,0,0,123,125,1,0,0,0,124,118,1,0,0,0,124,119,1,0,0,
        0,124,120,1,0,0,0,125,27,1,0,0,0,13,31,37,45,50,59,64,68,82,94,102,
        110,116,124
    ]

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
    RULE_declarationStm = 2
    RULE_var_decl_list = 3
    RULE_single_decl = 4
    RULE_multiple_decl = 5
    RULE_assignmentStm = 6
    RULE_single_assign = 7
    RULE_multiple_assign = 8
    RULE_expr_list = 9
    RULE_expression = 10
    RULE_term = 11
    RULE_factor = 12
    RULE_primary = 13

    ruleNames =  [ "program", "stm", "declarationStm", "var_decl_list", 
                   "single_decl", "multiple_decl", "assignmentStm", "single_assign", 
                   "multiple_assign", "expr_list", "expression", "term", 
                   "factor", "primary" ]

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

        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VoTienParser.StmContext)
            else:
                return self.getTypedRuleContext(VoTienParser.StmContext,i)


        def getRuleIndex(self):
            return VoTienParser.RULE_program




    def program(self):

        localctx = VoTienParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.stm()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==12):
                    break

            self.state = 33
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

        def declarationStm(self):
            return self.getTypedRuleContext(VoTienParser.DeclarationStmContext,0)


        def assignmentStm(self):
            return self.getTypedRuleContext(VoTienParser.AssignmentStmContext,0)


        def getRuleIndex(self):
            return VoTienParser.RULE_stm




    def stm(self):

        localctx = VoTienParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stm)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.declarationStm()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.assignmentStm()
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


    class DeclarationStmContext(ParserRuleContext):
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
            return VoTienParser.RULE_declarationStm




    def declarationStm(self):

        localctx = VoTienParser.DeclarationStmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declarationStm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(VoTienParser.INT)
            self.state = 40
            self.var_decl_list()
            self.state = 41
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

        def single_decl(self):
            return self.getTypedRuleContext(VoTienParser.Single_declContext,0)


        def multiple_decl(self):
            return self.getTypedRuleContext(VoTienParser.Multiple_declContext,0)


        def getRuleIndex(self):
            return VoTienParser.RULE_var_decl_list




    def var_decl_list(self):

        localctx = VoTienParser.Var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_decl_list)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.single_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.multiple_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VoTienParser.ID, 0)

        def ASSIGNI(self):
            return self.getToken(VoTienParser.ASSIGNI, 0)

        def expression(self):
            return self.getTypedRuleContext(VoTienParser.ExpressionContext,0)


        def getRuleIndex(self):
            return VoTienParser.RULE_single_decl




    def single_decl(self):

        localctx = VoTienParser.Single_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_single_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(VoTienParser.ID)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 48
                self.match(VoTienParser.ASSIGNI)
                self.state = 49
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiple_declContext(ParserRuleContext):
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

        def ASSIGNI(self):
            return self.getToken(VoTienParser.ASSIGNI, 0)

        def expr_list(self):
            return self.getTypedRuleContext(VoTienParser.Expr_listContext,0)


        def getRuleIndex(self):
            return VoTienParser.RULE_multiple_decl




    def multiple_decl(self):

        localctx = VoTienParser.Multiple_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_multiple_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(VoTienParser.ID)
            self.state = 53
            self.match(VoTienParser.CM)
            self.state = 54
            self.match(VoTienParser.ID)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 55
                self.match(VoTienParser.CM)
                self.state = 56
                self.match(VoTienParser.ID)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 62
                self.match(VoTienParser.ASSIGNI)
                self.state = 63
                self.expr_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_assign(self):
            return self.getTypedRuleContext(VoTienParser.Single_assignContext,0)


        def multiple_assign(self):
            return self.getTypedRuleContext(VoTienParser.Multiple_assignContext,0)


        def getRuleIndex(self):
            return VoTienParser.RULE_assignmentStm




    def assignmentStm(self):

        localctx = VoTienParser.AssignmentStmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignmentStm)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.single_assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.multiple_assign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VoTienParser.ID, 0)

        def ASSIGNI(self):
            return self.getToken(VoTienParser.ASSIGNI, 0)

        def expression(self):
            return self.getTypedRuleContext(VoTienParser.ExpressionContext,0)


        def SEM(self):
            return self.getToken(VoTienParser.SEM, 0)

        def getRuleIndex(self):
            return VoTienParser.RULE_single_assign




    def single_assign(self):

        localctx = VoTienParser.Single_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_single_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(VoTienParser.ID)
            self.state = 71
            self.match(VoTienParser.ASSIGNI)
            self.state = 72
            self.expression()
            self.state = 73
            self.match(VoTienParser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiple_assignContext(ParserRuleContext):
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

        def ASSIGNI(self):
            return self.getToken(VoTienParser.ASSIGNI, 0)

        def expr_list(self):
            return self.getTypedRuleContext(VoTienParser.Expr_listContext,0)


        def SEM(self):
            return self.getToken(VoTienParser.SEM, 0)

        def getRuleIndex(self):
            return VoTienParser.RULE_multiple_assign




    def multiple_assign(self):

        localctx = VoTienParser.Multiple_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_multiple_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(VoTienParser.ID)
            self.state = 76
            self.match(VoTienParser.CM)
            self.state = 77
            self.match(VoTienParser.ID)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 78
                self.match(VoTienParser.CM)
                self.state = 79
                self.match(VoTienParser.ID)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(VoTienParser.ASSIGNI)
            self.state = 86
            self.expr_list()
            self.state = 87
            self.match(VoTienParser.SEM)
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




    def expr_list(self):

        localctx = VoTienParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.expression()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 90
                self.match(VoTienParser.CM)
                self.state = 91
                self.expression()
                self.state = 96
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




    def expression(self):

        localctx = VoTienParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.term()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 98
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 99
                self.term()
                self.state = 104
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




    def term(self):

        localctx = VoTienParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.factor()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 106
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 107
                self.factor()
                self.state = 112
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




    def factor(self):

        localctx = VoTienParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.primary()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 114
                self.match(VoTienParser.EXP)
                self.state = 115
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

        def ID(self):
            return self.getToken(VoTienParser.ID, 0)

        def INT_LIT(self):
            return self.getToken(VoTienParser.INT_LIT, 0)

        def LP(self):
            return self.getToken(VoTienParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(VoTienParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(VoTienParser.RP, 0)

        def getRuleIndex(self):
            return VoTienParser.RULE_primary




    def primary(self):

        localctx = VoTienParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primary)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(VoTienParser.ID)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(VoTienParser.INT_LIT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.match(VoTienParser.LP)
                self.state = 121
                self.expression()
                self.state = 122
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






# Generated from main/MiniGo.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u0148\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%")
        buf.write("\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\6\66\u013a\n\66\r")
        buf.write("\66\16\66\u013b\3\66\3\66\3\67\3\67\3\67\38\38\38\39\3")
        buf.write("9\39\2\2:\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:\3\2\5\5\2C\\aac|\3\2\62;\5\2\13\f\16\17\"\"")
        buf.write("\2\u0148\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\3s\3\2\2\2\5z\3\2\2\2\7}\3\2\2\2\t")
        buf.write("\u0082\3\2\2\2\13\u0086\3\2\2\2\r\u008d\3\2\2\2\17\u0092")
        buf.write("\3\2\2\2\21\u0097\3\2\2\2\23\u009e\3\2\2\2\25\u00a8\3")
        buf.write("\2\2\2\27\u00af\3\2\2\2\31\u00b3\3\2\2\2\33\u00b9\3\2")
        buf.write("\2\2\35\u00c1\3\2\2\2\37\u00c7\3\2\2\2!\u00cb\3\2\2\2")
        buf.write("#\u00d4\3\2\2\2%\u00da\3\2\2\2\'\u00e0\3\2\2\2)\u00e4")
        buf.write("\3\2\2\2+\u00e9\3\2\2\2-\u00ef\3\2\2\2/\u00f1\3\2\2\2")
        buf.write("\61\u00f3\3\2\2\2\63\u00f5\3\2\2\2\65\u00f7\3\2\2\2\67")
        buf.write("\u00f9\3\2\2\29\u00fc\3\2\2\2;\u00ff\3\2\2\2=\u0101\3")
        buf.write("\2\2\2?\u0104\3\2\2\2A\u0106\3\2\2\2C\u0109\3\2\2\2E\u010c")
        buf.write("\3\2\2\2G\u010f\3\2\2\2I\u0111\3\2\2\2K\u0113\3\2\2\2")
        buf.write("M\u0116\3\2\2\2O\u0119\3\2\2\2Q\u011c\3\2\2\2S\u011f\3")
        buf.write("\2\2\2U\u0122\3\2\2\2W\u0124\3\2\2\2Y\u0126\3\2\2\2[\u0128")
        buf.write("\3\2\2\2]\u012a\3\2\2\2_\u012c\3\2\2\2a\u012e\3\2\2\2")
        buf.write("c\u0130\3\2\2\2e\u0132\3\2\2\2g\u0134\3\2\2\2i\u0136\3")
        buf.write("\2\2\2k\u0139\3\2\2\2m\u013f\3\2\2\2o\u0142\3\2\2\2q\u0145")
        buf.write("\3\2\2\2st\7x\2\2tu\7q\2\2uv\7v\2\2vw\7k\2\2wx\7g\2\2")
        buf.write("xy\7p\2\2y\4\3\2\2\2z{\7k\2\2{|\7h\2\2|\6\3\2\2\2}~\7")
        buf.write("g\2\2~\177\7n\2\2\177\u0080\7u\2\2\u0080\u0081\7g\2\2")
        buf.write("\u0081\b\3\2\2\2\u0082\u0083\7h\2\2\u0083\u0084\7q\2\2")
        buf.write("\u0084\u0085\7t\2\2\u0085\n\3\2\2\2\u0086\u0087\7t\2\2")
        buf.write("\u0087\u0088\7g\2\2\u0088\u0089\7v\2\2\u0089\u008a\7w")
        buf.write("\2\2\u008a\u008b\7t\2\2\u008b\u008c\7p\2\2\u008c\f\3\2")
        buf.write("\2\2\u008d\u008e\7h\2\2\u008e\u008f\7w\2\2\u008f\u0090")
        buf.write("\7p\2\2\u0090\u0091\7e\2\2\u0091\16\3\2\2\2\u0092\u0093")
        buf.write("\7v\2\2\u0093\u0094\7{\2\2\u0094\u0095\7r\2\2\u0095\u0096")
        buf.write("\7g\2\2\u0096\20\3\2\2\2\u0097\u0098\7u\2\2\u0098\u0099")
        buf.write("\7v\2\2\u0099\u009a\7t\2\2\u009a\u009b\7w\2\2\u009b\u009c")
        buf.write("\7e\2\2\u009c\u009d\7v\2\2\u009d\22\3\2\2\2\u009e\u009f")
        buf.write("\7k\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4\7h\2\2\u00a4\u00a5")
        buf.write("\7c\2\2\u00a5\u00a6\7e\2\2\u00a6\u00a7\7g\2\2\u00a7\24")
        buf.write("\3\2\2\2\u00a8\u00a9\7u\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae")
        buf.write("\7i\2\2\u00ae\26\3\2\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1")
        buf.write("\7p\2\2\u00b1\u00b2\7v\2\2\u00b2\30\3\2\2\2\u00b3\u00b4")
        buf.write("\7h\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7")
        buf.write("\7c\2\2\u00b7\u00b8\7v\2\2\u00b8\32\3\2\2\2\u00b9\u00ba")
        buf.write("\7d\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd")
        buf.write("\7n\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7c\2\2\u00bf\u00c0")
        buf.write("\7p\2\2\u00c0\34\3\2\2\2\u00c1\u00c2\7e\2\2\u00c2\u00c3")
        buf.write("\7q\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7u\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6\36\3\2\2\2\u00c7\u00c8\7x\2\2\u00c8\u00c9")
        buf.write("\7c\2\2\u00c9\u00ca\7t\2\2\u00ca \3\2\2\2\u00cb\u00cc")
        buf.write("\7e\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf")
        buf.write("\7v\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2")
        buf.write("\7w\2\2\u00d2\u00d3\7g\2\2\u00d3\"\3\2\2\2\u00d4\u00d5")
        buf.write("\7d\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8")
        buf.write("\7c\2\2\u00d8\u00d9\7m\2\2\u00d9$\3\2\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de")
        buf.write("\7i\2\2\u00de\u00df\7g\2\2\u00df&\3\2\2\2\u00e0\u00e1")
        buf.write("\7p\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7n\2\2\u00e3(\3")
        buf.write("\2\2\2\u00e4\u00e5\7v\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7")
        buf.write("\7w\2\2\u00e7\u00e8\7g\2\2\u00e8*\3\2\2\2\u00e9\u00ea")
        buf.write("\7h\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7n\2\2\u00ec\u00ed")
        buf.write("\7u\2\2\u00ed\u00ee\7g\2\2\u00ee,\3\2\2\2\u00ef\u00f0")
        buf.write("\7-\2\2\u00f0.\3\2\2\2\u00f1\u00f2\7/\2\2\u00f2\60\3\2")
        buf.write("\2\2\u00f3\u00f4\7,\2\2\u00f4\62\3\2\2\2\u00f5\u00f6\7")
        buf.write("\61\2\2\u00f6\64\3\2\2\2\u00f7\u00f8\7\'\2\2\u00f8\66")
        buf.write("\3\2\2\2\u00f9\u00fa\7?\2\2\u00fa\u00fb\7?\2\2\u00fb8")
        buf.write("\3\2\2\2\u00fc\u00fd\7#\2\2\u00fd\u00fe\7?\2\2\u00fe:")
        buf.write("\3\2\2\2\u00ff\u0100\7>\2\2\u0100<\3\2\2\2\u0101\u0102")
        buf.write("\7>\2\2\u0102\u0103\7?\2\2\u0103>\3\2\2\2\u0104\u0105")
        buf.write("\7@\2\2\u0105@\3\2\2\2\u0106\u0107\7@\2\2\u0107\u0108")
        buf.write("\7?\2\2\u0108B\3\2\2\2\u0109\u010a\7(\2\2\u010a\u010b")
        buf.write("\7(\2\2\u010bD\3\2\2\2\u010c\u010d\7~\2\2\u010d\u010e")
        buf.write("\7~\2\2\u010eF\3\2\2\2\u010f\u0110\7#\2\2\u0110H\3\2\2")
        buf.write("\2\u0111\u0112\7?\2\2\u0112J\3\2\2\2\u0113\u0114\7-\2")
        buf.write("\2\u0114\u0115\7?\2\2\u0115L\3\2\2\2\u0116\u0117\7/\2")
        buf.write("\2\u0117\u0118\7?\2\2\u0118N\3\2\2\2\u0119\u011a\7,\2")
        buf.write("\2\u011a\u011b\7?\2\2\u011bP\3\2\2\2\u011c\u011d\7\61")
        buf.write("\2\2\u011d\u011e\7?\2\2\u011eR\3\2\2\2\u011f\u0120\7\'")
        buf.write("\2\2\u0120\u0121\7?\2\2\u0121T\3\2\2\2\u0122\u0123\7\60")
        buf.write("\2\2\u0123V\3\2\2\2\u0124\u0125\7*\2\2\u0125X\3\2\2\2")
        buf.write("\u0126\u0127\7+\2\2\u0127Z\3\2\2\2\u0128\u0129\7}\2\2")
        buf.write("\u0129\\\3\2\2\2\u012a\u012b\7\177\2\2\u012b^\3\2\2\2")
        buf.write("\u012c\u012d\7]\2\2\u012d`\3\2\2\2\u012e\u012f\7_\2\2")
        buf.write("\u012fb\3\2\2\2\u0130\u0131\7.\2\2\u0131d\3\2\2\2\u0132")
        buf.write("\u0133\7=\2\2\u0133f\3\2\2\2\u0134\u0135\t\2\2\2\u0135")
        buf.write("h\3\2\2\2\u0136\u0137\t\3\2\2\u0137j\3\2\2\2\u0138\u013a")
        buf.write("\t\4\2\2\u0139\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d\u013e\b\66\2\2\u013el\3\2\2\2\u013f\u0140\13\2")
        buf.write("\2\2\u0140\u0141\b\67\3\2\u0141n\3\2\2\2\u0142\u0143\7")
        buf.write("W\2\2\u0143\u0144\b8\4\2\u0144p\3\2\2\2\u0145\u0146\7")
        buf.write("K\2\2\u0146\u0147\b9\5\2\u0147r\3\2\2\2\4\2\u013b\6\b")
        buf.write("\2\2\3\67\2\38\3\39\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IF = 2
    ELSE = 3
    FOR = 4
    RETURN = 5
    FUNC = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    STRING = 10
    INT = 11
    FLOAT = 12
    BOOLEAN = 13
    CONST = 14
    VAR = 15
    CONTINUE = 16
    BREAK = 17
    RANGE = 18
    NIL = 19
    TRUE = 20
    FALSE = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    EQUAL = 27
    NOT_EQUAL = 28
    LESS = 29
    LESS_OR_EQUAL = 30
    GREATER = 31
    GREATER_OR_EQUAL = 32
    AND = 33
    OR = 34
    NOT = 35
    ASSIGN = 36
    ADD_ASSIGN = 37
    SUB_ASSIGN = 38
    MUL_ASSIGN = 39
    DIV_ASSIGN = 40
    MOD_ASSIGN = 41
    DOT = 42
    LP = 43
    RP = 44
    LB = 45
    RB = 46
    LSB = 47
    RSB = 48
    COMMA = 49
    SEMI = 50
    ID = 51
    INT_LIT = 52
    WS = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'votien'", "'if'", "'else'", "'for'", "'return'", "'func'", 
            "'type'", "'struct'", "'interface'", "'string'", "'int'", "'float'", 
            "'boolean'", "'const'", "'var'", "'continue'", "'break'", "'range'", 
            "'nil'", "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
            "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", "'U'", 
            "'I'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
            "GREATER", "GREATER_OR_EQUAL", "AND", "OR", "NOT", "ASSIGN", 
            "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
            "DOT", "LP", "RP", "LB", "RB", "LSB", "RSB", "COMMA", "SEMI", 
            "ID", "INT_LIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
                  "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
                  "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "LP", 
                  "RP", "LB", "RB", "LSB", "RSB", "COMMA", "SEMI", "ID", 
                  "INT_LIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text);
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[53] = self.ERROR_CHAR_action 
            actions[54] = self.UNCLOSE_STRING_action 
            actions[55] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise UncloseString(self.text[1:-2])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text[1:])

     



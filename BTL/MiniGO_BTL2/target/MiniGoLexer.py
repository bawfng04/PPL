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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u0215\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\5\2\u0097")
        buf.write("\n\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3")
        buf.write("&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\7\65\u015b\n\65\f\65\16\65")
        buf.write("\u015e\13\65\3\66\3\66\3\67\3\67\38\38\38\38\58\u0168")
        buf.write("\n8\38\68\u016b\n8\r8\168\u016c\39\39\3:\3:\3:\3:\5:\u0175")
        buf.write("\n:\3:\6:\u0178\n:\r:\16:\u0179\3;\3;\3;\7;\u017f\n;\f")
        buf.write(";\16;\u0182\13;\5;\u0184\n;\3<\3<\7<\u0188\n<\f<\16<\u018b")
        buf.write("\13<\3=\3=\3>\3>\3>\3>\5>\u0193\n>\3>\6>\u0196\n>\r>\16")
        buf.write(">\u0197\3?\3?\5?\u019c\n?\3?\6?\u019f\n?\r?\16?\u01a0")
        buf.write("\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u01ad\n@\3A\6A\u01b0")
        buf.write("\nA\rA\16A\u01b1\3A\3A\5A\u01b6\nA\3A\3A\5A\u01ba\nA\3")
        buf.write("A\6A\u01bd\nA\rA\16A\u01be\3A\5A\u01c2\nA\3B\3B\3C\3C")
        buf.write("\3C\5C\u01c9\nC\3D\3D\7D\u01cd\nD\fD\16D\u01d0\13D\3D")
        buf.write("\3D\3D\3E\6E\u01d6\nE\rE\16E\u01d7\3E\3E\3F\3F\3F\3F\7")
        buf.write("F\u01e0\nF\fF\16F\u01e3\13F\3F\3F\3G\3G\3G\3G\3G\7G\u01ec")
        buf.write("\nG\fG\16G\u01ef\13G\3G\3G\3G\3G\3G\3H\3H\7H\u01f8\nH")
        buf.write("\fH\16H\u01fb\13H\3H\5H\u01fe\nH\3H\3H\3I\3I\7I\u0204")
        buf.write("\nI\fI\16I\u0207\13I\3I\3I\3I\7I\u020c\nI\fI\16I\u020f")
        buf.write("\13I\3I\3I\3J\3J\3J\3\u01ed\2K\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2\177")
        buf.write("\67\u00818\u0083\2\u0085\2\u00879\u0089:\u008b;\u008d")
        buf.write("<\u008f=\u0091>\u0093?\3\2\20\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\3\2\62;\3\2\629\5\2\62;CHch\3\2\63;\3\2\62\63\4\2G")
        buf.write("Ggg\4\2--//\t\2$$))^^ddppttvv\6\2\f\f\17\17$$^^\5\2\13")
        buf.write("\f\16\17\"\"\4\2\f\f\17\17\4\3\f\f\17\17\2\u0227\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0087\3")
        buf.write("\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2")
        buf.write("\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\3\u0096")
        buf.write("\3\2\2\2\5\u009c\3\2\2\2\7\u009e\3\2\2\2\t\u00a1\3\2\2")
        buf.write("\2\13\u00a6\3\2\2\2\r\u00aa\3\2\2\2\17\u00b1\3\2\2\2\21")
        buf.write("\u00b6\3\2\2\2\23\u00bb\3\2\2\2\25\u00c2\3\2\2\2\27\u00cc")
        buf.write("\3\2\2\2\31\u00d3\3\2\2\2\33\u00d7\3\2\2\2\35\u00dd\3")
        buf.write("\2\2\2\37\u00e5\3\2\2\2!\u00eb\3\2\2\2#\u00ef\3\2\2\2")
        buf.write("%\u00f8\3\2\2\2\'\u00fe\3\2\2\2)\u0104\3\2\2\2+\u0108")
        buf.write("\3\2\2\2-\u010d\3\2\2\2/\u0113\3\2\2\2\61\u0115\3\2\2")
        buf.write("\2\63\u0117\3\2\2\2\65\u0119\3\2\2\2\67\u011b\3\2\2\2")
        buf.write("9\u011d\3\2\2\2;\u0120\3\2\2\2=\u0123\3\2\2\2?\u0125\3")
        buf.write("\2\2\2A\u0128\3\2\2\2C\u012a\3\2\2\2E\u012d\3\2\2\2G\u0130")
        buf.write("\3\2\2\2I\u0133\3\2\2\2K\u0135\3\2\2\2M\u0137\3\2\2\2")
        buf.write("O\u013a\3\2\2\2Q\u013d\3\2\2\2S\u0140\3\2\2\2U\u0143\3")
        buf.write("\2\2\2W\u0146\3\2\2\2Y\u0148\3\2\2\2[\u014a\3\2\2\2]\u014c")
        buf.write("\3\2\2\2_\u014e\3\2\2\2a\u0150\3\2\2\2c\u0152\3\2\2\2")
        buf.write("e\u0154\3\2\2\2g\u0156\3\2\2\2i\u0158\3\2\2\2k\u015f\3")
        buf.write("\2\2\2m\u0161\3\2\2\2o\u0167\3\2\2\2q\u016e\3\2\2\2s\u0174")
        buf.write("\3\2\2\2u\u0183\3\2\2\2w\u0185\3\2\2\2y\u018c\3\2\2\2")
        buf.write("{\u0192\3\2\2\2}\u0199\3\2\2\2\177\u01ac\3\2\2\2\u0081")
        buf.write("\u01c1\3\2\2\2\u0083\u01c3\3\2\2\2\u0085\u01c8\3\2\2\2")
        buf.write("\u0087\u01ca\3\2\2\2\u0089\u01d5\3\2\2\2\u008b\u01db\3")
        buf.write("\2\2\2\u008d\u01e6\3\2\2\2\u008f\u01f5\3\2\2\2\u0091\u0201")
        buf.write("\3\2\2\2\u0093\u0212\3\2\2\2\u0095\u0097\7\17\2\2\u0096")
        buf.write("\u0095\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\u0099\7\f\2\2\u0099\u009a\3\2\2\2\u009a\u009b\b")
        buf.write("\2\2\2\u009b\4\3\2\2\2\u009c\u009d\7<\2\2\u009d\6\3\2")
        buf.write("\2\2\u009e\u009f\7k\2\2\u009f\u00a0\7h\2\2\u00a0\b\3\2")
        buf.write("\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7n\2\2\u00a3\u00a4")
        buf.write("\7u\2\2\u00a4\u00a5\7g\2\2\u00a5\n\3\2\2\2\u00a6\u00a7")
        buf.write("\7h\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9\7t\2\2\u00a9\f")
        buf.write("\3\2\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad")
        buf.write("\7v\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af\7t\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\16\3\2\2\2\u00b1\u00b2\7h\2\2\u00b2\u00b3")
        buf.write("\7w\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7e\2\2\u00b5\20")
        buf.write("\3\2\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7{\2\2\u00b8\u00b9")
        buf.write("\7r\2\2\u00b9\u00ba\7g\2\2\u00ba\22\3\2\2\2\u00bb\u00bc")
        buf.write("\7u\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7w\2\2\u00bf\u00c0\7e\2\2\u00c0\u00c1\7v\2\2\u00c1\24")
        buf.write("\3\2\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5")
        buf.write("\7v\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8")
        buf.write("\7h\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7e\2\2\u00ca\u00cb")
        buf.write("\7g\2\2\u00cb\26\3\2\2\2\u00cc\u00cd\7u\2\2\u00cd\u00ce")
        buf.write("\7v\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7i\2\2\u00d2\30\3\2\2\2\u00d3\u00d4")
        buf.write("\7k\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6\7v\2\2\u00d6\32")
        buf.write("\3\2\2\2\u00d7\u00d8\7h\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da")
        buf.write("\7q\2\2\u00da\u00db\7c\2\2\u00db\u00dc\7v\2\2\u00dc\34")
        buf.write("\3\2\2\2\u00dd\u00de\7d\2\2\u00de\u00df\7q\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3")
        buf.write("\7c\2\2\u00e3\u00e4\7p\2\2\u00e4\36\3\2\2\2\u00e5\u00e6")
        buf.write("\7e\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9")
        buf.write("\7u\2\2\u00e9\u00ea\7v\2\2\u00ea \3\2\2\2\u00eb\u00ec")
        buf.write("\7x\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7t\2\2\u00ee\"")
        buf.write("\3\2\2\2\u00ef\u00f0\7e\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2")
        buf.write("\7p\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5")
        buf.write("\7p\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7\7g\2\2\u00f7$\3")
        buf.write("\2\2\2\u00f8\u00f9\7d\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb")
        buf.write("\7g\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd\7m\2\2\u00fd&\3")
        buf.write("\2\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7c\2\2\u0100\u0101")
        buf.write("\7p\2\2\u0101\u0102\7i\2\2\u0102\u0103\7g\2\2\u0103(\3")
        buf.write("\2\2\2\u0104\u0105\7p\2\2\u0105\u0106\7k\2\2\u0106\u0107")
        buf.write("\7n\2\2\u0107*\3\2\2\2\u0108\u0109\7v\2\2\u0109\u010a")
        buf.write("\7t\2\2\u010a\u010b\7w\2\2\u010b\u010c\7g\2\2\u010c,\3")
        buf.write("\2\2\2\u010d\u010e\7h\2\2\u010e\u010f\7c\2\2\u010f\u0110")
        buf.write("\7n\2\2\u0110\u0111\7u\2\2\u0111\u0112\7g\2\2\u0112.\3")
        buf.write("\2\2\2\u0113\u0114\7-\2\2\u0114\60\3\2\2\2\u0115\u0116")
        buf.write("\7/\2\2\u0116\62\3\2\2\2\u0117\u0118\7,\2\2\u0118\64\3")
        buf.write("\2\2\2\u0119\u011a\7\61\2\2\u011a\66\3\2\2\2\u011b\u011c")
        buf.write("\7\'\2\2\u011c8\3\2\2\2\u011d\u011e\7?\2\2\u011e\u011f")
        buf.write("\7?\2\2\u011f:\3\2\2\2\u0120\u0121\7#\2\2\u0121\u0122")
        buf.write("\7?\2\2\u0122<\3\2\2\2\u0123\u0124\7>\2\2\u0124>\3\2\2")
        buf.write("\2\u0125\u0126\7>\2\2\u0126\u0127\7?\2\2\u0127@\3\2\2")
        buf.write("\2\u0128\u0129\7@\2\2\u0129B\3\2\2\2\u012a\u012b\7@\2")
        buf.write("\2\u012b\u012c\7?\2\2\u012cD\3\2\2\2\u012d\u012e\7(\2")
        buf.write("\2\u012e\u012f\7(\2\2\u012fF\3\2\2\2\u0130\u0131\7~\2")
        buf.write("\2\u0131\u0132\7~\2\2\u0132H\3\2\2\2\u0133\u0134\7#\2")
        buf.write("\2\u0134J\3\2\2\2\u0135\u0136\7?\2\2\u0136L\3\2\2\2\u0137")
        buf.write("\u0138\7-\2\2\u0138\u0139\7?\2\2\u0139N\3\2\2\2\u013a")
        buf.write("\u013b\7/\2\2\u013b\u013c\7?\2\2\u013cP\3\2\2\2\u013d")
        buf.write("\u013e\7,\2\2\u013e\u013f\7?\2\2\u013fR\3\2\2\2\u0140")
        buf.write("\u0141\7\61\2\2\u0141\u0142\7?\2\2\u0142T\3\2\2\2\u0143")
        buf.write("\u0144\7\'\2\2\u0144\u0145\7?\2\2\u0145V\3\2\2\2\u0146")
        buf.write("\u0147\7\60\2\2\u0147X\3\2\2\2\u0148\u0149\7*\2\2\u0149")
        buf.write("Z\3\2\2\2\u014a\u014b\7+\2\2\u014b\\\3\2\2\2\u014c\u014d")
        buf.write("\7}\2\2\u014d^\3\2\2\2\u014e\u014f\7\177\2\2\u014f`\3")
        buf.write("\2\2\2\u0150\u0151\7]\2\2\u0151b\3\2\2\2\u0152\u0153\7")
        buf.write("_\2\2\u0153d\3\2\2\2\u0154\u0155\7.\2\2\u0155f\3\2\2\2")
        buf.write("\u0156\u0157\7=\2\2\u0157h\3\2\2\2\u0158\u015c\t\2\2\2")
        buf.write("\u0159\u015b\t\3\2\2\u015a\u0159\3\2\2\2\u015b\u015e\3")
        buf.write("\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015dj")
        buf.write("\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0160\t\4\2\2\u0160")
        buf.write("l\3\2\2\2\u0161\u0162\t\5\2\2\u0162n\3\2\2\2\u0163\u0164")
        buf.write("\7\62\2\2\u0164\u0168\7q\2\2\u0165\u0166\7\62\2\2\u0166")
        buf.write("\u0168\7Q\2\2\u0167\u0163\3\2\2\2\u0167\u0165\3\2\2\2")
        buf.write("\u0168\u016a\3\2\2\2\u0169\u016b\t\5\2\2\u016a\u0169\3")
        buf.write("\2\2\2\u016b\u016c\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d")
        buf.write("\3\2\2\2\u016dp\3\2\2\2\u016e\u016f\t\6\2\2\u016fr\3\2")
        buf.write("\2\2\u0170\u0171\7\62\2\2\u0171\u0175\7z\2\2\u0172\u0173")
        buf.write("\7\62\2\2\u0173\u0175\7Z\2\2\u0174\u0170\3\2\2\2\u0174")
        buf.write("\u0172\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0178\t\6\2\2")
        buf.write("\u0177\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u0177\3")
        buf.write("\2\2\2\u0179\u017a\3\2\2\2\u017at\3\2\2\2\u017b\u0184")
        buf.write("\7\62\2\2\u017c\u0180\t\7\2\2\u017d\u017f\t\4\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0180\u0181\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3")
        buf.write("\2\2\2\u0183\u017b\3\2\2\2\u0183\u017c\3\2\2\2\u0184v")
        buf.write("\3\2\2\2\u0185\u0189\7\60\2\2\u0186\u0188\t\4\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018ax\3\2\2\2\u018b\u0189\3\2\2")
        buf.write("\2\u018c\u018d\t\b\2\2\u018dz\3\2\2\2\u018e\u018f\7\62")
        buf.write("\2\2\u018f\u0193\7d\2\2\u0190\u0191\7\62\2\2\u0191\u0193")
        buf.write("\7D\2\2\u0192\u018e\3\2\2\2\u0192\u0190\3\2\2\2\u0193")
        buf.write("\u0195\3\2\2\2\u0194\u0196\t\b\2\2\u0195\u0194\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3")
        buf.write("\2\2\2\u0198|\3\2\2\2\u0199\u019b\t\t\2\2\u019a\u019c")
        buf.write("\t\n\2\2\u019b\u019a\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("\u019e\3\2\2\2\u019d\u019f\t\4\2\2\u019e\u019d\3\2\2\2")
        buf.write("\u019f\u01a0\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1\3")
        buf.write("\2\2\2\u01a1~\3\2\2\2\u01a2\u01ad\5u;\2\u01a3\u01a4\5")
        buf.write("s:\2\u01a4\u01a5\b@\3\2\u01a5\u01ad\3\2\2\2\u01a6\u01a7")
        buf.write("\5o8\2\u01a7\u01a8\b@\4\2\u01a8\u01ad\3\2\2\2\u01a9\u01aa")
        buf.write("\5{>\2\u01aa\u01ab\b@\5\2\u01ab\u01ad\3\2\2\2\u01ac\u01a2")
        buf.write("\3\2\2\2\u01ac\u01a3\3\2\2\2\u01ac\u01a6\3\2\2\2\u01ac")
        buf.write("\u01a9\3\2\2\2\u01ad\u0080\3\2\2\2\u01ae\u01b0\t\4\2\2")
        buf.write("\u01af\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01af\3")
        buf.write("\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5")
        buf.write("\5w<\2\u01b4\u01b6\5}?\2\u01b5\u01b4\3\2\2\2\u01b5\u01b6")
        buf.write("\3\2\2\2\u01b6\u01c2\3\2\2\2\u01b7\u01b9\5w<\2\u01b8\u01ba")
        buf.write("\5}?\2\u01b9\u01b8\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01c2")
        buf.write("\3\2\2\2\u01bb\u01bd\t\4\2\2\u01bc\u01bb\3\2\2\2\u01bd")
        buf.write("\u01be\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf\u01c0\3\2\2\2\u01c0\u01c2\5}?\2\u01c1\u01af\3\2")
        buf.write("\2\2\u01c1\u01b7\3\2\2\2\u01c1\u01bc\3\2\2\2\u01c2\u0082")
        buf.write("\3\2\2\2\u01c3\u01c4\t\13\2\2\u01c4\u0084\3\2\2\2\u01c5")
        buf.write("\u01c9\n\f\2\2\u01c6\u01c7\7^\2\2\u01c7\u01c9\5\u0083")
        buf.write("B\2\u01c8\u01c5\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9\u0086")
        buf.write("\3\2\2\2\u01ca\u01ce\7$\2\2\u01cb\u01cd\5\u0085C\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01ce\3")
        buf.write("\2\2\2\u01d1\u01d2\7$\2\2\u01d2\u01d3\bD\6\2\u01d3\u0088")
        buf.write("\3\2\2\2\u01d4\u01d6\t\r\2\2\u01d5\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d7\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2")
        buf.write("\u01d8\u01d9\3\2\2\2\u01d9\u01da\bE\2\2\u01da\u008a\3")
        buf.write("\2\2\2\u01db\u01dc\7\61\2\2\u01dc\u01dd\7\61\2\2\u01dd")
        buf.write("\u01e1\3\2\2\2\u01de\u01e0\n\16\2\2\u01df\u01de\3\2\2")
        buf.write("\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2")
        buf.write("\3\2\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4")
        buf.write("\u01e5\bF\2\2\u01e5\u008c\3\2\2\2\u01e6\u01e7\7\61\2\2")
        buf.write("\u01e7\u01e8\7,\2\2\u01e8\u01ed\3\2\2\2\u01e9\u01ec\5")
        buf.write("\u008dG\2\u01ea\u01ec\13\2\2\2\u01eb\u01e9\3\2\2\2\u01eb")
        buf.write("\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01ee\3\2\2\2")
        buf.write("\u01ed\u01eb\3\2\2\2\u01ee\u01f0\3\2\2\2\u01ef\u01ed\3")
        buf.write("\2\2\2\u01f0\u01f1\7,\2\2\u01f1\u01f2\7\61\2\2\u01f2\u01f3")
        buf.write("\3\2\2\2\u01f3\u01f4\bG\2\2\u01f4\u008e\3\2\2\2\u01f5")
        buf.write("\u01f9\7$\2\2\u01f6\u01f8\5\u0085C\2\u01f7\u01f6\3\2\2")
        buf.write("\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa")
        buf.write("\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc")
        buf.write("\u01fe\t\17\2\2\u01fd\u01fc\3\2\2\2\u01fe\u01ff\3\2\2")
        buf.write("\2\u01ff\u0200\bH\7\2\u0200\u0090\3\2\2\2\u0201\u0205")
        buf.write("\7$\2\2\u0202\u0204\5\u0085C\2\u0203\u0202\3\2\2\2\u0204")
        buf.write("\u0207\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206\3\2\2\2")
        buf.write("\u0206\u0208\3\2\2\2\u0207\u0205\3\2\2\2\u0208\u0209\7")
        buf.write("^\2\2\u0209\u020d\n\13\2\2\u020a\u020c\5\u0085C\2\u020b")
        buf.write("\u020a\3\2\2\2\u020c\u020f\3\2\2\2\u020d\u020b\3\2\2\2")
        buf.write("\u020d\u020e\3\2\2\2\u020e\u0210\3\2\2\2\u020f\u020d\3")
        buf.write("\2\2\2\u0210\u0211\bI\b\2\u0211\u0092\3\2\2\2\u0212\u0213")
        buf.write("\13\2\2\2\u0213\u0214\bJ\t\2\u0214\u0094\3\2\2\2 \2\u0096")
        buf.write("\u015c\u0167\u016c\u0174\u0179\u0180\u0183\u0189\u0192")
        buf.write("\u0197\u019b\u01a0\u01ac\u01b1\u01b5\u01b9\u01be\u01c1")
        buf.write("\u01c8\u01ce\u01d7\u01e1\u01eb\u01ed\u01f9\u01fd\u0205")
        buf.write("\u020d\n\b\2\2\3@\2\3@\3\3@\4\3D\5\3H\6\3I\7\3J\b")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NEWLINE = 1
    COLON = 2
    IF = 3
    ELSE = 4
    FOR = 5
    RETURN = 6
    FUNC = 7
    TYPE = 8
    STRUCT = 9
    INTERFACE = 10
    STRING = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    CONST = 15
    VAR = 16
    CONTINUE = 17
    BREAK = 18
    RANGE = 19
    NIL = 20
    TRUE = 21
    FALSE = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQUAL = 28
    NOT_EQUAL = 29
    LESS = 30
    LESS_OR_EQUAL = 31
    GREATER = 32
    GREATER_OR_EQUAL = 33
    AND = 34
    OR = 35
    NOT = 36
    ASSIGN = 37
    ADD_ASSIGN = 38
    SUB_ASSIGN = 39
    MUL_ASSIGN = 40
    DIV_ASSIGN = 41
    MOD_ASSIGN = 42
    DOT = 43
    LP = 44
    RP = 45
    LB = 46
    RB = 47
    LSB = 48
    RSB = 49
    COMMA = 50
    SEMI = 51
    ID = 52
    INT_LIT = 53
    FLOAT_LIT = 54
    STRING_LIT = 55
    WS = 56
    LINE_COMMENT = 57
    BLOCK_COMMENT = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "COLON", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
            "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
            "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
            "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
            "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", "AND", 
            "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
            "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "LP", "RP", "LB", "RB", "LSB", 
            "RSB", "COMMA", "SEMI", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
            "WS", "LINE_COMMENT", "BLOCK_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "NEWLINE", "COLON", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                  "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                  "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                  "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", 
                  "GREATER_OR_EQUAL", "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", 
                  "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "DOT", "LP", "RP", "LB", "RB", "LSB", "RSB", "COMMA", 
                  "SEMI", "ID", "DIGIT", "OCTAL_DIGIT", "OCTAL", "HEX_DIGIT", 
                  "HEX", "DECIMAL", "DECIMAL_PART", "BINARY_DIGIT", "BINARY", 
                  "EXPONENT", "INT_LIT", "FLOAT_LIT", "ESC_CHAR", "STR_CHAR", 
                  "STRING_LIT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[62] = self.INT_LIT_action 
            actions[66] = self.STRING_LIT_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            actions[72] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = str(int(self.text,16))
     

        if actionIndex == 1:
            self.text = str(int(self.text,8))
     

        if actionIndex == 2:
            self.text = str(int(self.text,2))
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             self.text = self.text[1:-1] 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    if self.text[-1] in ['\r','\n']: #nếu kết thúc bằng dấu xuống dòng thì cắt dấu xuống dòng
                        self.text = self.text[1:-1]
                    else: #nếu kết thúc bằng EOF thì lấy từ đầu chuỗi đến hết
                        self.text = self.text[1:]
                    raise UncloseString(self.text)
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
              #nếu có kí tự escape không hợp lệ (không phải \b, \r, \n, \t, \', \", \\)
                illegal_str = str(self.text)
                i = illegal_str.find('\\') #tìm vị trí xuất hiện đầu tiên của kí tự escape
                while i != -1 and illegal_str[i+1] in 'brnt\'"\\': #hợp lệ thì tìm tiếp
                    i = illegal_str.find('\\', i+2)
                raise IllegalEscape(illegal_str[1:i+2])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     



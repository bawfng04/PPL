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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u021a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\7\65\u0159\n\65\f\65\16\65\u015c\13\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\38\38\58\u0166\n8\38\68\u0169\n")
        buf.write("8\r8\168\u016a\39\39\3:\3:\3:\3:\5:\u0173\n:\3:\6:\u0176")
        buf.write("\n:\r:\16:\u0177\3;\3;\3;\7;\u017d\n;\f;\16;\u0180\13")
        buf.write(";\5;\u0182\n;\3<\3<\7<\u0186\n<\f<\16<\u0189\13<\3=\3")
        buf.write("=\3>\3>\3>\3>\5>\u0191\n>\3>\6>\u0194\n>\r>\16>\u0195")
        buf.write("\3?\3?\5?\u019a\n?\3?\6?\u019d\n?\r?\16?\u019e\3@\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3@\5@\u01ab\n@\3A\6A\u01ae\nA\rA\16")
        buf.write("A\u01af\3A\3A\5A\u01b4\nA\3A\3A\5A\u01b8\nA\3A\6A\u01bb")
        buf.write("\nA\rA\16A\u01bc\3A\5A\u01c0\nA\3B\3B\3C\3C\3C\5C\u01c7")
        buf.write("\nC\3D\3D\7D\u01cb\nD\fD\16D\u01ce\13D\3D\3D\3D\3E\6E")
        buf.write("\u01d4\nE\rE\16E\u01d5\3E\3E\3F\5F\u01db\nF\3F\3F\3F\3")
        buf.write("F\3G\3G\3G\3G\7G\u01e5\nG\fG\16G\u01e8\13G\3G\3G\3H\3")
        buf.write("H\3H\3H\3H\7H\u01f1\nH\fH\16H\u01f4\13H\3H\3H\3H\3H\3")
        buf.write("H\3I\3I\7I\u01fd\nI\fI\16I\u0200\13I\3I\5I\u0203\nI\3")
        buf.write("I\3I\3J\3J\7J\u0209\nJ\fJ\16J\u020c\13J\3J\3J\3J\7J\u0211")
        buf.write("\nJ\fJ\16J\u0214\13J\3J\3J\3K\3K\3K\3\u01f2\2L\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\2q\2s\2u\2w\2")
        buf.write("y\2{\2}\2\177\67\u00818\u0083\2\u0085\2\u00879\u0089:")
        buf.write("\u008b;\u008d<\u008f=\u0091>\u0093?\u0095@\3\2\20\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\629\5\2\62;CHch\3\2")
        buf.write("\63;\3\2\62\63\4\2GGgg\4\2--//\t\2$$))^^ddppttvv\6\2\f")
        buf.write("\f\17\17$$^^\5\2\13\f\16\17\"\"\4\2\f\f\17\17\4\3\f\f")
        buf.write("\17\17\2\u022c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2\177\3\2\2\2\2\u0081\3")
        buf.write("\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2")
        buf.write("\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\3\u0097\3\2\2\2\5\u009a\3\2\2")
        buf.write("\2\7\u009f\3\2\2\2\t\u00a3\3\2\2\2\13\u00aa\3\2\2\2\r")
        buf.write("\u00af\3\2\2\2\17\u00b4\3\2\2\2\21\u00bb\3\2\2\2\23\u00c5")
        buf.write("\3\2\2\2\25\u00cc\3\2\2\2\27\u00d0\3\2\2\2\31\u00d6\3")
        buf.write("\2\2\2\33\u00de\3\2\2\2\35\u00e4\3\2\2\2\37\u00e8\3\2")
        buf.write("\2\2!\u00f1\3\2\2\2#\u00f7\3\2\2\2%\u00fd\3\2\2\2\'\u0101")
        buf.write("\3\2\2\2)\u0106\3\2\2\2+\u010c\3\2\2\2-\u010e\3\2\2\2")
        buf.write("/\u0110\3\2\2\2\61\u0112\3\2\2\2\63\u0114\3\2\2\2\65\u0116")
        buf.write("\3\2\2\2\67\u0119\3\2\2\29\u011c\3\2\2\2;\u011e\3\2\2")
        buf.write("\2=\u0121\3\2\2\2?\u0123\3\2\2\2A\u0126\3\2\2\2C\u0129")
        buf.write("\3\2\2\2E\u012c\3\2\2\2G\u012e\3\2\2\2I\u0130\3\2\2\2")
        buf.write("K\u0133\3\2\2\2M\u0136\3\2\2\2O\u0139\3\2\2\2Q\u013c\3")
        buf.write("\2\2\2S\u013f\3\2\2\2U\u0141\3\2\2\2W\u0143\3\2\2\2Y\u0146")
        buf.write("\3\2\2\2[\u0148\3\2\2\2]\u014a\3\2\2\2_\u014c\3\2\2\2")
        buf.write("a\u014e\3\2\2\2c\u0150\3\2\2\2e\u0152\3\2\2\2g\u0154\3")
        buf.write("\2\2\2i\u0156\3\2\2\2k\u015d\3\2\2\2m\u015f\3\2\2\2o\u0165")
        buf.write("\3\2\2\2q\u016c\3\2\2\2s\u0172\3\2\2\2u\u0181\3\2\2\2")
        buf.write("w\u0183\3\2\2\2y\u018a\3\2\2\2{\u0190\3\2\2\2}\u0197\3")
        buf.write("\2\2\2\177\u01aa\3\2\2\2\u0081\u01bf\3\2\2\2\u0083\u01c1")
        buf.write("\3\2\2\2\u0085\u01c6\3\2\2\2\u0087\u01c8\3\2\2\2\u0089")
        buf.write("\u01d3\3\2\2\2\u008b\u01da\3\2\2\2\u008d\u01e0\3\2\2\2")
        buf.write("\u008f\u01eb\3\2\2\2\u0091\u01fa\3\2\2\2\u0093\u0206\3")
        buf.write("\2\2\2\u0095\u0217\3\2\2\2\u0097\u0098\7k\2\2\u0098\u0099")
        buf.write("\7h\2\2\u0099\4\3\2\2\2\u009a\u009b\7g\2\2\u009b\u009c")
        buf.write("\7n\2\2\u009c\u009d\7u\2\2\u009d\u009e\7g\2\2\u009e\6")
        buf.write("\3\2\2\2\u009f\u00a0\7h\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2")
        buf.write("\7t\2\2\u00a2\b\3\2\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5")
        buf.write("\7g\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7\7w\2\2\u00a7\u00a8")
        buf.write("\7t\2\2\u00a8\u00a9\7p\2\2\u00a9\n\3\2\2\2\u00aa\u00ab")
        buf.write("\7h\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae")
        buf.write("\7e\2\2\u00ae\f\3\2\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1")
        buf.write("\7{\2\2\u00b1\u00b2\7r\2\2\u00b2\u00b3\7g\2\2\u00b3\16")
        buf.write("\3\2\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7")
        buf.write("\7t\2\2\u00b7\u00b8\7w\2\2\u00b8\u00b9\7e\2\2\u00b9\u00ba")
        buf.write("\7v\2\2\u00ba\20\3\2\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd")
        buf.write("\7p\2\2\u00bd\u00be\7v\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0")
        buf.write("\7t\2\2\u00c0\u00c1\7h\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3")
        buf.write("\7e\2\2\u00c3\u00c4\7g\2\2\u00c4\22\3\2\2\2\u00c5\u00c6")
        buf.write("\7u\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9")
        buf.write("\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb\7i\2\2\u00cb\24")
        buf.write("\3\2\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf")
        buf.write("\7v\2\2\u00cf\26\3\2\2\2\u00d0\u00d1\7h\2\2\u00d1\u00d2")
        buf.write("\7n\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5")
        buf.write("\7v\2\2\u00d5\30\3\2\2\2\u00d6\u00d7\7d\2\2\u00d7\u00d8")
        buf.write("\7q\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7n\2\2\u00da\u00db")
        buf.write("\7g\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd\7p\2\2\u00dd\32")
        buf.write("\3\2\2\2\u00de\u00df\7e\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1")
        buf.write("\7p\2\2\u00e1\u00e2\7u\2\2\u00e2\u00e3\7v\2\2\u00e3\34")
        buf.write("\3\2\2\2\u00e4\u00e5\7x\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7")
        buf.write("\7t\2\2\u00e7\36\3\2\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7w\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0 \3\2\2\2\u00f1\u00f2\7d\2\2\u00f2\u00f3")
        buf.write("\7t\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6")
        buf.write("\7m\2\2\u00f6\"\3\2\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9")
        buf.write("\7c\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb\7i\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc$\3\2\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7n\2\2\u0100&\3\2\2\2\u0101\u0102")
        buf.write("\7v\2\2\u0102\u0103\7t\2\2\u0103\u0104\7w\2\2\u0104\u0105")
        buf.write("\7g\2\2\u0105(\3\2\2\2\u0106\u0107\7h\2\2\u0107\u0108")
        buf.write("\7c\2\2\u0108\u0109\7n\2\2\u0109\u010a\7u\2\2\u010a\u010b")
        buf.write("\7g\2\2\u010b*\3\2\2\2\u010c\u010d\7-\2\2\u010d,\3\2\2")
        buf.write("\2\u010e\u010f\7/\2\2\u010f.\3\2\2\2\u0110\u0111\7,\2")
        buf.write("\2\u0111\60\3\2\2\2\u0112\u0113\7\61\2\2\u0113\62\3\2")
        buf.write("\2\2\u0114\u0115\7\'\2\2\u0115\64\3\2\2\2\u0116\u0117")
        buf.write("\7?\2\2\u0117\u0118\7?\2\2\u0118\66\3\2\2\2\u0119\u011a")
        buf.write("\7#\2\2\u011a\u011b\7?\2\2\u011b8\3\2\2\2\u011c\u011d")
        buf.write("\7>\2\2\u011d:\3\2\2\2\u011e\u011f\7>\2\2\u011f\u0120")
        buf.write("\7?\2\2\u0120<\3\2\2\2\u0121\u0122\7@\2\2\u0122>\3\2\2")
        buf.write("\2\u0123\u0124\7@\2\2\u0124\u0125\7?\2\2\u0125@\3\2\2")
        buf.write("\2\u0126\u0127\7(\2\2\u0127\u0128\7(\2\2\u0128B\3\2\2")
        buf.write("\2\u0129\u012a\7~\2\2\u012a\u012b\7~\2\2\u012bD\3\2\2")
        buf.write("\2\u012c\u012d\7#\2\2\u012dF\3\2\2\2\u012e\u012f\7?\2")
        buf.write("\2\u012fH\3\2\2\2\u0130\u0131\7-\2\2\u0131\u0132\7?\2")
        buf.write("\2\u0132J\3\2\2\2\u0133\u0134\7/\2\2\u0134\u0135\7?\2")
        buf.write("\2\u0135L\3\2\2\2\u0136\u0137\7,\2\2\u0137\u0138\7?\2")
        buf.write("\2\u0138N\3\2\2\2\u0139\u013a\7\61\2\2\u013a\u013b\7?")
        buf.write("\2\2\u013bP\3\2\2\2\u013c\u013d\7\'\2\2\u013d\u013e\7")
        buf.write("?\2\2\u013eR\3\2\2\2\u013f\u0140\7\60\2\2\u0140T\3\2\2")
        buf.write("\2\u0141\u0142\7<\2\2\u0142V\3\2\2\2\u0143\u0144\7<\2")
        buf.write("\2\u0144\u0145\7?\2\2\u0145X\3\2\2\2\u0146\u0147\7*\2")
        buf.write("\2\u0147Z\3\2\2\2\u0148\u0149\7+\2\2\u0149\\\3\2\2\2\u014a")
        buf.write("\u014b\7}\2\2\u014b^\3\2\2\2\u014c\u014d\7\177\2\2\u014d")
        buf.write("`\3\2\2\2\u014e\u014f\7]\2\2\u014fb\3\2\2\2\u0150\u0151")
        buf.write("\7_\2\2\u0151d\3\2\2\2\u0152\u0153\7.\2\2\u0153f\3\2\2")
        buf.write("\2\u0154\u0155\7=\2\2\u0155h\3\2\2\2\u0156\u015a\t\2\2")
        buf.write("\2\u0157\u0159\t\3\2\2\u0158\u0157\3\2\2\2\u0159\u015c")
        buf.write("\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b")
        buf.write("j\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e\t\4\2\2\u015e")
        buf.write("l\3\2\2\2\u015f\u0160\t\5\2\2\u0160n\3\2\2\2\u0161\u0162")
        buf.write("\7\62\2\2\u0162\u0166\7q\2\2\u0163\u0164\7\62\2\2\u0164")
        buf.write("\u0166\7Q\2\2\u0165\u0161\3\2\2\2\u0165\u0163\3\2\2\2")
        buf.write("\u0166\u0168\3\2\2\2\u0167\u0169\t\5\2\2\u0168\u0167\3")
        buf.write("\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b")
        buf.write("\3\2\2\2\u016bp\3\2\2\2\u016c\u016d\t\6\2\2\u016dr\3\2")
        buf.write("\2\2\u016e\u016f\7\62\2\2\u016f\u0173\7z\2\2\u0170\u0171")
        buf.write("\7\62\2\2\u0171\u0173\7Z\2\2\u0172\u016e\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0173\u0175\3\2\2\2\u0174\u0176\t\6\2\2")
        buf.write("\u0175\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0175\3")
        buf.write("\2\2\2\u0177\u0178\3\2\2\2\u0178t\3\2\2\2\u0179\u0182")
        buf.write("\7\62\2\2\u017a\u017e\t\7\2\2\u017b\u017d\t\4\2\2\u017c")
        buf.write("\u017b\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3")
        buf.write("\2\2\2\u0181\u0179\3\2\2\2\u0181\u017a\3\2\2\2\u0182v")
        buf.write("\3\2\2\2\u0183\u0187\7\60\2\2\u0184\u0186\t\4\2\2\u0185")
        buf.write("\u0184\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0188\3\2\2\2\u0188x\3\2\2\2\u0189\u0187\3\2\2")
        buf.write("\2\u018a\u018b\t\b\2\2\u018bz\3\2\2\2\u018c\u018d\7\62")
        buf.write("\2\2\u018d\u0191\7d\2\2\u018e\u018f\7\62\2\2\u018f\u0191")
        buf.write("\7D\2\2\u0190\u018c\3\2\2\2\u0190\u018e\3\2\2\2\u0191")
        buf.write("\u0193\3\2\2\2\u0192\u0194\t\b\2\2\u0193\u0192\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3")
        buf.write("\2\2\2\u0196|\3\2\2\2\u0197\u0199\t\t\2\2\u0198\u019a")
        buf.write("\t\n\2\2\u0199\u0198\3\2\2\2\u0199\u019a\3\2\2\2\u019a")
        buf.write("\u019c\3\2\2\2\u019b\u019d\t\4\2\2\u019c\u019b\3\2\2\2")
        buf.write("\u019d\u019e\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3")
        buf.write("\2\2\2\u019f~\3\2\2\2\u01a0\u01ab\5u;\2\u01a1\u01a2\5")
        buf.write("s:\2\u01a2\u01a3\b@\2\2\u01a3\u01ab\3\2\2\2\u01a4\u01a5")
        buf.write("\5o8\2\u01a5\u01a6\b@\3\2\u01a6\u01ab\3\2\2\2\u01a7\u01a8")
        buf.write("\5{>\2\u01a8\u01a9\b@\4\2\u01a9\u01ab\3\2\2\2\u01aa\u01a0")
        buf.write("\3\2\2\2\u01aa\u01a1\3\2\2\2\u01aa\u01a4\3\2\2\2\u01aa")
        buf.write("\u01a7\3\2\2\2\u01ab\u0080\3\2\2\2\u01ac\u01ae\t\4\2\2")
        buf.write("\u01ad\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01ad\3")
        buf.write("\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b3")
        buf.write("\5w<\2\u01b2\u01b4\5}?\2\u01b3\u01b2\3\2\2\2\u01b3\u01b4")
        buf.write("\3\2\2\2\u01b4\u01c0\3\2\2\2\u01b5\u01b7\5w<\2\u01b6\u01b8")
        buf.write("\5}?\2\u01b7\u01b6\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01c0")
        buf.write("\3\2\2\2\u01b9\u01bb\t\4\2\2\u01ba\u01b9\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2")
        buf.write("\u01bd\u01be\3\2\2\2\u01be\u01c0\5}?\2\u01bf\u01ad\3\2")
        buf.write("\2\2\u01bf\u01b5\3\2\2\2\u01bf\u01ba\3\2\2\2\u01c0\u0082")
        buf.write("\3\2\2\2\u01c1\u01c2\t\13\2\2\u01c2\u0084\3\2\2\2\u01c3")
        buf.write("\u01c7\n\f\2\2\u01c4\u01c5\7^\2\2\u01c5\u01c7\5\u0083")
        buf.write("B\2\u01c6\u01c3\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u0086")
        buf.write("\3\2\2\2\u01c8\u01cc\7$\2\2\u01c9\u01cb\5\u0085C\2\u01ca")
        buf.write("\u01c9\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2")
        buf.write("\u01cc\u01cd\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01cc\3")
        buf.write("\2\2\2\u01cf\u01d0\7$\2\2\u01d0\u01d1\bD\5\2\u01d1\u0088")
        buf.write("\3\2\2\2\u01d2\u01d4\t\r\2\2\u01d3\u01d2\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2")
        buf.write("\u01d6\u01d7\3\2\2\2\u01d7\u01d8\bE\6\2\u01d8\u008a\3")
        buf.write("\2\2\2\u01d9\u01db\7\17\2\2\u01da\u01d9\3\2\2\2\u01da")
        buf.write("\u01db\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01dd\7\f\2\2")
        buf.write("\u01dd\u01de\3\2\2\2\u01de\u01df\bF\6\2\u01df\u008c\3")
        buf.write("\2\2\2\u01e0\u01e1\7\61\2\2\u01e1\u01e2\7\61\2\2\u01e2")
        buf.write("\u01e6\3\2\2\2\u01e3\u01e5\n\16\2\2\u01e4\u01e3\3\2\2")
        buf.write("\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7")
        buf.write("\3\2\2\2\u01e7\u01e9\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e9")
        buf.write("\u01ea\bG\6\2\u01ea\u008e\3\2\2\2\u01eb\u01ec\7\61\2\2")
        buf.write("\u01ec\u01ed\7,\2\2\u01ed\u01f2\3\2\2\2\u01ee\u01f1\5")
        buf.write("\u008fH\2\u01ef\u01f1\13\2\2\2\u01f0\u01ee\3\2\2\2\u01f0")
        buf.write("\u01ef\3\2\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f3\3\2\2\2")
        buf.write("\u01f2\u01f0\3\2\2\2\u01f3\u01f5\3\2\2\2\u01f4\u01f2\3")
        buf.write("\2\2\2\u01f5\u01f6\7,\2\2\u01f6\u01f7\7\61\2\2\u01f7\u01f8")
        buf.write("\3\2\2\2\u01f8\u01f9\bH\6\2\u01f9\u0090\3\2\2\2\u01fa")
        buf.write("\u01fe\7$\2\2\u01fb\u01fd\5\u0085C\2\u01fc\u01fb\3\2\2")
        buf.write("\2\u01fd\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff")
        buf.write("\3\2\2\2\u01ff\u0202\3\2\2\2\u0200\u01fe\3\2\2\2\u0201")
        buf.write("\u0203\t\17\2\2\u0202\u0201\3\2\2\2\u0203\u0204\3\2\2")
        buf.write("\2\u0204\u0205\bI\7\2\u0205\u0092\3\2\2\2\u0206\u020a")
        buf.write("\7$\2\2\u0207\u0209\5\u0085C\2\u0208\u0207\3\2\2\2\u0209")
        buf.write("\u020c\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2")
        buf.write("\u020b\u020d\3\2\2\2\u020c\u020a\3\2\2\2\u020d\u020e\7")
        buf.write("^\2\2\u020e\u0212\n\13\2\2\u020f\u0211\5\u0085C\2\u0210")
        buf.write("\u020f\3\2\2\2\u0211\u0214\3\2\2\2\u0212\u0210\3\2\2\2")
        buf.write("\u0212\u0213\3\2\2\2\u0213\u0215\3\2\2\2\u0214\u0212\3")
        buf.write("\2\2\2\u0215\u0216\bJ\b\2\u0216\u0094\3\2\2\2\u0217\u0218")
        buf.write("\13\2\2\2\u0218\u0219\bK\t\2\u0219\u0096\3\2\2\2 \2\u015a")
        buf.write("\u0165\u016a\u0172\u0177\u017e\u0181\u0187\u0190\u0195")
        buf.write("\u0199\u019e\u01aa\u01af\u01b3\u01b7\u01bc\u01bf\u01c6")
        buf.write("\u01cc\u01d5\u01da\u01e6\u01f0\u01f2\u01fe\u0202\u020a")
        buf.write("\u0212\n\3@\2\3@\3\3@\4\3D\5\b\2\2\3I\6\3J\7\3K\b")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    EQUAL = 26
    NOT_EQUAL = 27
    LESS = 28
    LESS_OR_EQUAL = 29
    GREATER = 30
    GREATER_OR_EQUAL = 31
    AND = 32
    OR = 33
    NOT = 34
    ASSIGN = 35
    ADD_ASSIGN = 36
    SUB_ASSIGN = 37
    MUL_ASSIGN = 38
    DIV_ASSIGN = 39
    MOD_ASSIGN = 40
    DOT = 41
    COLON = 42
    SHORT_ASSIGN = 43
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
    NEWLINE = 57
    LINE_COMMENT = 58
    BLOCK_COMMENT = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "':'", 
            "':='", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
            "GREATER", "GREATER_OR_EQUAL", "AND", "OR", "NOT", "ASSIGN", 
            "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
            "DOT", "COLON", "SHORT_ASSIGN", "LP", "RP", "LB", "RB", "LSB", 
            "RSB", "COMMA", "SEMI", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
            "WS", "NEWLINE", "LINE_COMMENT", "BLOCK_COMMENT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
                  "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
                  "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", 
                  "SHORT_ASSIGN", "LP", "RP", "LB", "RB", "LSB", "RSB", 
                  "COMMA", "SEMI", "ID", "DIGIT", "OCTAL_DIGIT", "OCTAL", 
                  "HEX_DIGIT", "HEX", "DECIMAL", "DECIMAL_PART", "BINARY_DIGIT", 
                  "BINARY", "EXPONENT", "INT_LIT", "FLOAT_LIT", "ESC_CHAR", 
                  "STR_CHAR", "STRING_LIT", "WS", "NEWLINE", "LINE_COMMENT", 
                  "BLOCK_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.ERROR_CHAR_action 
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
     



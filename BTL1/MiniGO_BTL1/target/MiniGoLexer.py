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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u01f8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\7\3\u0099\n\3\f\3\16\3\u009c\13\3\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3")
        buf.write("*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\38\78\u0161\n8\f8\168\u0164\138\58\u0166")
        buf.write("\n8\39\39\69\u016a\n9\r9\169\u016b\3:\3:\3:\3:\5:\u0172")
        buf.write("\n:\3:\6:\u0175\n:\r:\16:\u0176\3;\3;\5;\u017b\n;\3;\6")
        buf.write(";\u017e\n;\r;\16;\u017f\3<\3<\7<\u0184\n<\f<\16<\u0187")
        buf.write("\13<\3=\3=\3=\3=\3=\3=\3=\5=\u0190\n=\3>\6>\u0193\n>\r")
        buf.write(">\16>\u0194\3>\3>\5>\u0199\n>\3>\3>\5>\u019d\n>\3>\6>")
        buf.write("\u01a0\n>\r>\16>\u01a1\3>\5>\u01a5\n>\3?\3?\3@\3@\3@\5")
        buf.write("@\u01ac\n@\3A\3A\7A\u01b0\nA\fA\16A\u01b3\13A\3A\3A\3")
        buf.write("A\3B\6B\u01b9\nB\rB\16B\u01ba\3B\3B\3C\3C\3C\3C\7C\u01c3")
        buf.write("\nC\fC\16C\u01c6\13C\3C\3C\3D\3D\3D\3D\3D\7D\u01cf\nD")
        buf.write("\fD\16D\u01d2\13D\3D\3D\3D\3D\3D\3E\3E\7E\u01db\nE\fE")
        buf.write("\16E\u01de\13E\3E\5E\u01e1\nE\3E\3E\3F\3F\7F\u01e7\nF")
        buf.write("\fF\16F\u01ea\13F\3F\3F\3F\7F\u01ef\nF\fF\16F\u01f2\13")
        buf.write("F\3F\3F\3G\3G\3G\3\u01d0\2H\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\2k\2m\2o\2q\2s\2u\2w\2y\66{\67}\2\177\2\u0081")
        buf.write("8\u00839\u0085:\u0087;\u0089<\u008b=\u008d>\3\2\17\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\629\5\2\62;CHch\3\2")
        buf.write("\63;\4\2GGgg\4\2--//\t\2$$))^^ddppttvv\6\2\f\f\17\17$")
        buf.write("$^^\5\2\13\f\16\17\"\"\4\2\f\f\17\17\4\3\f\f\17\17\2\u0207")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u008f\3\2\2\2\5\u0096")
        buf.write("\3\2\2\2\7\u009d\3\2\2\2\t\u00a0\3\2\2\2\13\u00a5\3\2")
        buf.write("\2\2\r\u00a9\3\2\2\2\17\u00b0\3\2\2\2\21\u00b5\3\2\2\2")
        buf.write("\23\u00ba\3\2\2\2\25\u00c1\3\2\2\2\27\u00cb\3\2\2\2\31")
        buf.write("\u00d2\3\2\2\2\33\u00d6\3\2\2\2\35\u00dc\3\2\2\2\37\u00e4")
        buf.write("\3\2\2\2!\u00ea\3\2\2\2#\u00ee\3\2\2\2%\u00f7\3\2\2\2")
        buf.write("\'\u00fd\3\2\2\2)\u0103\3\2\2\2+\u0107\3\2\2\2-\u010c")
        buf.write("\3\2\2\2/\u0112\3\2\2\2\61\u0114\3\2\2\2\63\u0116\3\2")
        buf.write("\2\2\65\u0118\3\2\2\2\67\u011a\3\2\2\29\u011c\3\2\2\2")
        buf.write(";\u011f\3\2\2\2=\u0122\3\2\2\2?\u0124\3\2\2\2A\u0127\3")
        buf.write("\2\2\2C\u0129\3\2\2\2E\u012c\3\2\2\2G\u012f\3\2\2\2I\u0132")
        buf.write("\3\2\2\2K\u0134\3\2\2\2M\u0136\3\2\2\2O\u0139\3\2\2\2")
        buf.write("Q\u013c\3\2\2\2S\u013f\3\2\2\2U\u0142\3\2\2\2W\u0145\3")
        buf.write("\2\2\2Y\u0147\3\2\2\2[\u0149\3\2\2\2]\u014b\3\2\2\2_\u014d")
        buf.write("\3\2\2\2a\u014f\3\2\2\2c\u0151\3\2\2\2e\u0153\3\2\2\2")
        buf.write("g\u0155\3\2\2\2i\u0157\3\2\2\2k\u0159\3\2\2\2m\u015b\3")
        buf.write("\2\2\2o\u0165\3\2\2\2q\u0167\3\2\2\2s\u0171\3\2\2\2u\u0178")
        buf.write("\3\2\2\2w\u0181\3\2\2\2y\u018f\3\2\2\2{\u01a4\3\2\2\2")
        buf.write("}\u01a6\3\2\2\2\177\u01ab\3\2\2\2\u0081\u01ad\3\2\2\2")
        buf.write("\u0083\u01b8\3\2\2\2\u0085\u01be\3\2\2\2\u0087\u01c9\3")
        buf.write("\2\2\2\u0089\u01d8\3\2\2\2\u008b\u01e4\3\2\2\2\u008d\u01f5")
        buf.write("\3\2\2\2\u008f\u0090\7x\2\2\u0090\u0091\7q\2\2\u0091\u0092")
        buf.write("\7v\2\2\u0092\u0093\7k\2\2\u0093\u0094\7g\2\2\u0094\u0095")
        buf.write("\7p\2\2\u0095\4\3\2\2\2\u0096\u009a\t\2\2\2\u0097\u0099")
        buf.write("\t\3\2\2\u0098\u0097\3\2\2\2\u0099\u009c\3\2\2\2\u009a")
        buf.write("\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\6\3\2\2\2\u009c")
        buf.write("\u009a\3\2\2\2\u009d\u009e\7k\2\2\u009e\u009f\7h\2\2\u009f")
        buf.write("\b\3\2\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7n\2\2\u00a2")
        buf.write("\u00a3\7u\2\2\u00a3\u00a4\7g\2\2\u00a4\n\3\2\2\2\u00a5")
        buf.write("\u00a6\7h\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7t\2\2\u00a8")
        buf.write("\f\3\2\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab\7g\2\2\u00ab")
        buf.write("\u00ac\7v\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae\7t\2\2\u00ae")
        buf.write("\u00af\7p\2\2\u00af\16\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1")
        buf.write("\u00b2\7w\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4\7e\2\2\u00b4")
        buf.write("\20\3\2\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7{\2\2\u00b7")
        buf.write("\u00b8\7r\2\2\u00b8\u00b9\7g\2\2\u00b9\22\3\2\2\2\u00ba")
        buf.write("\u00bb\7u\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7t\2\2\u00bd")
        buf.write("\u00be\7w\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0\7v\2\2\u00c0")
        buf.write("\24\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3")
        buf.write("\u00c4\7v\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7t\2\2\u00c6")
        buf.write("\u00c7\7h\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7e\2\2\u00c9")
        buf.write("\u00ca\7g\2\2\u00ca\26\3\2\2\2\u00cb\u00cc\7u\2\2\u00cc")
        buf.write("\u00cd\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7k\2\2\u00cf")
        buf.write("\u00d0\7p\2\2\u00d0\u00d1\7i\2\2\u00d1\30\3\2\2\2\u00d2")
        buf.write("\u00d3\7k\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7v\2\2\u00d5")
        buf.write("\32\3\2\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8\7n\2\2\u00d8")
        buf.write("\u00d9\7q\2\2\u00d9\u00da\7c\2\2\u00da\u00db\7v\2\2\u00db")
        buf.write("\34\3\2\2\2\u00dc\u00dd\7d\2\2\u00dd\u00de\7q\2\2\u00de")
        buf.write("\u00df\7q\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1\7g\2\2\u00e1")
        buf.write("\u00e2\7c\2\2\u00e2\u00e3\7p\2\2\u00e3\36\3\2\2\2\u00e4")
        buf.write("\u00e5\7e\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7p\2\2\u00e7")
        buf.write("\u00e8\7u\2\2\u00e8\u00e9\7v\2\2\u00e9 \3\2\2\2\u00ea")
        buf.write("\u00eb\7x\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7t\2\2\u00ed")
        buf.write("\"\3\2\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0\7q\2\2\u00f0")
        buf.write("\u00f1\7p\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7k\2\2\u00f3")
        buf.write("\u00f4\7p\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6\7g\2\2\u00f6")
        buf.write("$\3\2\2\2\u00f7\u00f8\7d\2\2\u00f8\u00f9\7t\2\2\u00f9")
        buf.write("\u00fa\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7m\2\2\u00fc")
        buf.write("&\3\2\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7c\2\2\u00ff")
        buf.write("\u0100\7p\2\2\u0100\u0101\7i\2\2\u0101\u0102\7g\2\2\u0102")
        buf.write("(\3\2\2\2\u0103\u0104\7p\2\2\u0104\u0105\7k\2\2\u0105")
        buf.write("\u0106\7n\2\2\u0106*\3\2\2\2\u0107\u0108\7v\2\2\u0108")
        buf.write("\u0109\7t\2\2\u0109\u010a\7w\2\2\u010a\u010b\7g\2\2\u010b")
        buf.write(",\3\2\2\2\u010c\u010d\7h\2\2\u010d\u010e\7c\2\2\u010e")
        buf.write("\u010f\7n\2\2\u010f\u0110\7u\2\2\u0110\u0111\7g\2\2\u0111")
        buf.write(".\3\2\2\2\u0112\u0113\7-\2\2\u0113\60\3\2\2\2\u0114\u0115")
        buf.write("\7/\2\2\u0115\62\3\2\2\2\u0116\u0117\7,\2\2\u0117\64\3")
        buf.write("\2\2\2\u0118\u0119\7\61\2\2\u0119\66\3\2\2\2\u011a\u011b")
        buf.write("\7\'\2\2\u011b8\3\2\2\2\u011c\u011d\7?\2\2\u011d\u011e")
        buf.write("\7?\2\2\u011e:\3\2\2\2\u011f\u0120\7#\2\2\u0120\u0121")
        buf.write("\7?\2\2\u0121<\3\2\2\2\u0122\u0123\7>\2\2\u0123>\3\2\2")
        buf.write("\2\u0124\u0125\7>\2\2\u0125\u0126\7?\2\2\u0126@\3\2\2")
        buf.write("\2\u0127\u0128\7@\2\2\u0128B\3\2\2\2\u0129\u012a\7@\2")
        buf.write("\2\u012a\u012b\7?\2\2\u012bD\3\2\2\2\u012c\u012d\7(\2")
        buf.write("\2\u012d\u012e\7(\2\2\u012eF\3\2\2\2\u012f\u0130\7~\2")
        buf.write("\2\u0130\u0131\7~\2\2\u0131H\3\2\2\2\u0132\u0133\7#\2")
        buf.write("\2\u0133J\3\2\2\2\u0134\u0135\7?\2\2\u0135L\3\2\2\2\u0136")
        buf.write("\u0137\7-\2\2\u0137\u0138\7?\2\2\u0138N\3\2\2\2\u0139")
        buf.write("\u013a\7/\2\2\u013a\u013b\7?\2\2\u013bP\3\2\2\2\u013c")
        buf.write("\u013d\7,\2\2\u013d\u013e\7?\2\2\u013eR\3\2\2\2\u013f")
        buf.write("\u0140\7\61\2\2\u0140\u0141\7?\2\2\u0141T\3\2\2\2\u0142")
        buf.write("\u0143\7\'\2\2\u0143\u0144\7?\2\2\u0144V\3\2\2\2\u0145")
        buf.write("\u0146\7\60\2\2\u0146X\3\2\2\2\u0147\u0148\7*\2\2\u0148")
        buf.write("Z\3\2\2\2\u0149\u014a\7+\2\2\u014a\\\3\2\2\2\u014b\u014c")
        buf.write("\7}\2\2\u014c^\3\2\2\2\u014d\u014e\7\177\2\2\u014e`\3")
        buf.write("\2\2\2\u014f\u0150\7]\2\2\u0150b\3\2\2\2\u0151\u0152\7")
        buf.write("_\2\2\u0152d\3\2\2\2\u0153\u0154\7.\2\2\u0154f\3\2\2\2")
        buf.write("\u0155\u0156\7=\2\2\u0156h\3\2\2\2\u0157\u0158\t\4\2\2")
        buf.write("\u0158j\3\2\2\2\u0159\u015a\t\5\2\2\u015al\3\2\2\2\u015b")
        buf.write("\u015c\t\6\2\2\u015cn\3\2\2\2\u015d\u0166\7\62\2\2\u015e")
        buf.write("\u0162\t\7\2\2\u015f\u0161\t\4\2\2\u0160\u015f\3\2\2\2")
        buf.write("\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3")
        buf.write("\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u015d")
        buf.write("\3\2\2\2\u0165\u015e\3\2\2\2\u0166p\3\2\2\2\u0167\u0169")
        buf.write("\7\62\2\2\u0168\u016a\t\5\2\2\u0169\u0168\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016cr\3\2\2\2\u016d\u016e\7\62\2\2\u016e\u0172\7z\2")
        buf.write("\2\u016f\u0170\7\62\2\2\u0170\u0172\7Z\2\2\u0171\u016d")
        buf.write("\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0174\3\2\2\2\u0173")
        buf.write("\u0175\t\6\2\2\u0174\u0173\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177t\3\2\2")
        buf.write("\2\u0178\u017a\t\b\2\2\u0179\u017b\t\t\2\2\u017a\u0179")
        buf.write("\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017d\3\2\2\2\u017c")
        buf.write("\u017e\t\4\2\2\u017d\u017c\3\2\2\2\u017e\u017f\3\2\2\2")
        buf.write("\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180v\3\2\2")
        buf.write("\2\u0181\u0185\7\60\2\2\u0182\u0184\t\4\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0183\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186x\3\2\2\2\u0187\u0185\3\2\2\2\u0188")
        buf.write("\u0190\5o8\2\u0189\u018a\5s:\2\u018a\u018b\b=\2\2\u018b")
        buf.write("\u0190\3\2\2\2\u018c\u018d\5q9\2\u018d\u018e\b=\3\2\u018e")
        buf.write("\u0190\3\2\2\2\u018f\u0188\3\2\2\2\u018f\u0189\3\2\2\2")
        buf.write("\u018f\u018c\3\2\2\2\u0190z\3\2\2\2\u0191\u0193\t\4\2")
        buf.write("\2\u0192\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u0198\5w<\2\u0197\u0199\5u;\2\u0198\u0197\3\2\2\2\u0198")
        buf.write("\u0199\3\2\2\2\u0199\u01a5\3\2\2\2\u019a\u019c\5w<\2\u019b")
        buf.write("\u019d\5u;\2\u019c\u019b\3\2\2\2\u019c\u019d\3\2\2\2\u019d")
        buf.write("\u01a5\3\2\2\2\u019e\u01a0\t\4\2\2\u019f\u019e\3\2\2\2")
        buf.write("\u01a0\u01a1\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3")
        buf.write("\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a5\5u;\2\u01a4\u0192")
        buf.write("\3\2\2\2\u01a4\u019a\3\2\2\2\u01a4\u019f\3\2\2\2\u01a5")
        buf.write("|\3\2\2\2\u01a6\u01a7\t\n\2\2\u01a7~\3\2\2\2\u01a8\u01ac")
        buf.write("\n\13\2\2\u01a9\u01aa\7^\2\2\u01aa\u01ac\5}?\2\u01ab\u01a8")
        buf.write("\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u0080\3\2\2\2\u01ad")
        buf.write("\u01b1\7$\2\2\u01ae\u01b0\5\177@\2\u01af\u01ae\3\2\2\2")
        buf.write("\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3")
        buf.write("\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b5")
        buf.write("\7$\2\2\u01b5\u01b6\bA\4\2\u01b6\u0082\3\2\2\2\u01b7\u01b9")
        buf.write("\t\f\2\2\u01b8\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba")
        buf.write("\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc\3\2\2\2")
        buf.write("\u01bc\u01bd\bB\5\2\u01bd\u0084\3\2\2\2\u01be\u01bf\7")
        buf.write("\61\2\2\u01bf\u01c0\7\61\2\2\u01c0\u01c4\3\2\2\2\u01c1")
        buf.write("\u01c3\n\r\2\2\u01c2\u01c1\3\2\2\2\u01c3\u01c6\3\2\2\2")
        buf.write("\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c7\3")
        buf.write("\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c8\bC\5\2\u01c8\u0086")
        buf.write("\3\2\2\2\u01c9\u01ca\7\61\2\2\u01ca\u01cb\7,\2\2\u01cb")
        buf.write("\u01d0\3\2\2\2\u01cc\u01cf\5\u0087D\2\u01cd\u01cf\13\2")
        buf.write("\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf\u01d2")
        buf.write("\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1")
        buf.write("\u01d3\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d4\7,\2\2")
        buf.write("\u01d4\u01d5\7\61\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7")
        buf.write("\bD\5\2\u01d7\u0088\3\2\2\2\u01d8\u01dc\7$\2\2\u01d9\u01db")
        buf.write("\5\177@\2\u01da\u01d9\3\2\2\2\u01db\u01de\3\2\2\2\u01dc")
        buf.write("\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01e0\3\2\2\2")
        buf.write("\u01de\u01dc\3\2\2\2\u01df\u01e1\t\16\2\2\u01e0\u01df")
        buf.write("\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3\bE\6\2\u01e3")
        buf.write("\u008a\3\2\2\2\u01e4\u01e8\7$\2\2\u01e5\u01e7\5\177@\2")
        buf.write("\u01e6\u01e5\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3")
        buf.write("\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01eb\3\2\2\2\u01ea\u01e8")
        buf.write("\3\2\2\2\u01eb\u01ec\7^\2\2\u01ec\u01f0\n\n\2\2\u01ed")
        buf.write("\u01ef\5\177@\2\u01ee\u01ed\3\2\2\2\u01ef\u01f2\3\2\2")
        buf.write("\2\u01f0\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f3")
        buf.write("\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f3\u01f4\bF\7\2\u01f4")
        buf.write("\u008c\3\2\2\2\u01f5\u01f6\13\2\2\2\u01f6\u01f7\bG\b\2")
        buf.write("\u01f7\u008e\3\2\2\2\34\2\u009a\u0162\u0165\u016b\u0171")
        buf.write("\u0176\u017a\u017f\u0185\u018f\u0194\u0198\u019c\u01a1")
        buf.write("\u01a4\u01ab\u01b1\u01ba\u01c4\u01ce\u01d0\u01dc\u01e0")
        buf.write("\u01e8\u01f0\t\3=\2\3=\3\3A\4\b\2\2\3E\5\3F\6\3G\7")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    ID = 2
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
    INT_LIT = 52
    FLOAT_LIT = 53
    STRING_LIT = 54
    WS = 55
    LINE_COMMENT = 56
    BLOCK_COMMENT = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59
    ERROR_CHAR = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'votien'", "'if'", "'else'", "'for'", "'return'", "'func'", 
            "'type'", "'struct'", "'interface'", "'string'", "'int'", "'float'", 
            "'boolean'", "'const'", "'var'", "'continue'", "'break'", "'range'", 
            "'nil'", "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
            "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
            "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", 
            "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
            "GREATER", "GREATER_OR_EQUAL", "AND", "OR", "NOT", "ASSIGN", 
            "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
            "DOT", "LP", "RP", "LB", "RB", "LSB", "RSB", "COMMA", "SEMI", 
            "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", "LINE_COMMENT", 
            "BLOCK_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "ID", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
                  "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
                  "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "LP", 
                  "RP", "LB", "RB", "LSB", "RSB", "COMMA", "SEMI", "DIGIT", 
                  "OCTAL_DIGIT", "HEX_DIGIT", "DECIMAL", "OCTAL", "HEX", 
                  "EXPONENT", "DECIMAL_PART", "INT_LIT", "FLOAT_LIT", "ESC_CHAR", 
                  "STR_CHAR", "STRING_LIT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            raise UncloseString(result.text[1:]);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text[1:]);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text);
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[59] = self.INT_LIT_action 
            actions[63] = self.STRING_LIT_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.ERROR_CHAR_action 
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
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             self.text = self.text[1:-1] 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    if self.text[-1] in ['\r','\n']:
                        self.text = self.text[1:-1]
                    else:
                        self.text = self.text[1:]
                    raise UncloseString(self.text)
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                illegal_str = str(self.text)
                i = illegal_str.find('\\')
                while i != -1 and illegal_str[i+1] in 'brnt\'"\\':
                    i = illegal_str.find('\\', i+2)
                raise IllegalEscape(illegal_str[1:i+2])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     



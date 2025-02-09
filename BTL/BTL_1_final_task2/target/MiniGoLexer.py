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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u020f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\7\66\u0157\n\66\f\66\16\66\u015a\13\66\3\67\3\67")
        buf.write("\3\67\7\67\u015f\n\67\f\67\16\67\u0162\13\67\5\67\u0164")
        buf.write("\n\67\38\38\38\38\58\u016a\n8\38\68\u016d\n8\r8\168\u016e")
        buf.write("\39\39\39\39\59\u0175\n9\39\69\u0178\n9\r9\169\u0179\3")
        buf.write(":\3:\3:\3:\5:\u0180\n:\3:\6:\u0183\n:\r:\16:\u0184\3;")
        buf.write("\6;\u0188\n;\r;\16;\u0189\3<\3<\7<\u018e\n<\f<\16<\u0191")
        buf.write("\13<\3=\3=\5=\u0195\n=\3=\3=\3>\3>\3>\3>\5>\u019d\n>\3")
        buf.write("?\3?\3?\5?\u01a2\n?\3?\3?\3?\3?\3?\6?\u01a9\n?\r?\16?")
        buf.write("\u01aa\3?\5?\u01ae\n?\3?\3?\3?\5?\u01b3\n?\3@\3@\3A\3")
        buf.write("A\3A\5A\u01ba\nA\3B\3B\7B\u01be\nB\fB\16B\u01c1\13B\3")
        buf.write("B\3B\3B\3C\5C\u01c7\nC\3C\3C\3C\3D\6D\u01cd\nD\rD\16D")
        buf.write("\u01ce\3D\3D\3E\3E\3E\3E\3E\7E\u01d8\nE\fE\16E\u01db\13")
        buf.write("E\3E\3E\3E\3E\3E\3F\3F\3F\3F\7F\u01e6\nF\fF\16F\u01e9")
        buf.write("\13F\3F\3F\3G\3G\7G\u01ef\nG\fG\16G\u01f2\13G\3G\5G\u01f5")
        buf.write("\nG\3G\3G\3H\3H\7H\u01fb\nH\fH\16H\u01fe\13H\3H\3H\3H")
        buf.write("\7H\u0203\nH\fH\16H\u0206\13H\3H\5H\u0209\nH\3H\3H\3I")
        buf.write("\3I\3I\3\u01d9\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m\2o\2q\2s\2u\2w\2y\2{8}9\177\2\u0081\2\u0083")
        buf.write(":\u0085;\u0087<\u0089=\u008b>\u008d?\u008f@\u0091A\3\2")
        buf.write("\20\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\5\2\62;")
        buf.write("CHch\3\2\629\3\2\62\63\4\2GGgg\4\2--//\7\2$$^^ppttvv\6")
        buf.write("\2\f\f\17\17$$^^\5\2\13\13\16\17\"\"\4\2\f\f\17\17\4\3")
        buf.write("\f\f\17\17\2\u0225\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u0096")
        buf.write("\3\2\2\2\7\u009b\3\2\2\2\t\u009f\3\2\2\2\13\u00a6\3\2")
        buf.write("\2\2\r\u00ab\3\2\2\2\17\u00b0\3\2\2\2\21\u00b7\3\2\2\2")
        buf.write("\23\u00c1\3\2\2\2\25\u00c8\3\2\2\2\27\u00cc\3\2\2\2\31")
        buf.write("\u00d2\3\2\2\2\33\u00da\3\2\2\2\35\u00e0\3\2\2\2\37\u00e4")
        buf.write("\3\2\2\2!\u00ed\3\2\2\2#\u00f3\3\2\2\2%\u00f9\3\2\2\2")
        buf.write("\'\u00fd\3\2\2\2)\u0102\3\2\2\2+\u0108\3\2\2\2-\u010a")
        buf.write("\3\2\2\2/\u010c\3\2\2\2\61\u010e\3\2\2\2\63\u0110\3\2")
        buf.write("\2\2\65\u0112\3\2\2\2\67\u0115\3\2\2\29\u0118\3\2\2\2")
        buf.write(";\u011a\3\2\2\2=\u011d\3\2\2\2?\u011f\3\2\2\2A\u0122\3")
        buf.write("\2\2\2C\u0125\3\2\2\2E\u0128\3\2\2\2G\u012a\3\2\2\2I\u012c")
        buf.write("\3\2\2\2K\u012f\3\2\2\2M\u0132\3\2\2\2O\u0135\3\2\2\2")
        buf.write("Q\u0138\3\2\2\2S\u013b\3\2\2\2U\u013d\3\2\2\2W\u013f\3")
        buf.write("\2\2\2Y\u0142\3\2\2\2[\u0144\3\2\2\2]\u0146\3\2\2\2_\u0148")
        buf.write("\3\2\2\2a\u014a\3\2\2\2c\u014c\3\2\2\2e\u014e\3\2\2\2")
        buf.write("g\u0150\3\2\2\2i\u0152\3\2\2\2k\u0154\3\2\2\2m\u0163\3")
        buf.write("\2\2\2o\u0169\3\2\2\2q\u0174\3\2\2\2s\u017f\3\2\2\2u\u0187")
        buf.write("\3\2\2\2w\u018b\3\2\2\2y\u0192\3\2\2\2{\u019c\3\2\2\2")
        buf.write("}\u01b2\3\2\2\2\177\u01b4\3\2\2\2\u0081\u01b9\3\2\2\2")
        buf.write("\u0083\u01bb\3\2\2\2\u0085\u01c6\3\2\2\2\u0087\u01cc\3")
        buf.write("\2\2\2\u0089\u01d2\3\2\2\2\u008b\u01e1\3\2\2\2\u008d\u01ec")
        buf.write("\3\2\2\2\u008f\u01f8\3\2\2\2\u0091\u020c\3\2\2\2\u0093")
        buf.write("\u0094\7k\2\2\u0094\u0095\7h\2\2\u0095\4\3\2\2\2\u0096")
        buf.write("\u0097\7g\2\2\u0097\u0098\7n\2\2\u0098\u0099\7u\2\2\u0099")
        buf.write("\u009a\7g\2\2\u009a\6\3\2\2\2\u009b\u009c\7h\2\2\u009c")
        buf.write("\u009d\7q\2\2\u009d\u009e\7t\2\2\u009e\b\3\2\2\2\u009f")
        buf.write("\u00a0\7t\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7v\2\2\u00a2")
        buf.write("\u00a3\7w\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5\7p\2\2\u00a5")
        buf.write("\n\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8\7w\2\2\u00a8")
        buf.write("\u00a9\7p\2\2\u00a9\u00aa\7e\2\2\u00aa\f\3\2\2\2\u00ab")
        buf.write("\u00ac\7v\2\2\u00ac\u00ad\7{\2\2\u00ad\u00ae\7r\2\2\u00ae")
        buf.write("\u00af\7g\2\2\u00af\16\3\2\2\2\u00b0\u00b1\7u\2\2\u00b1")
        buf.write("\u00b2\7v\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4\7w\2\2\u00b4")
        buf.write("\u00b5\7e\2\2\u00b5\u00b6\7v\2\2\u00b6\20\3\2\2\2\u00b7")
        buf.write("\u00b8\7k\2\2\u00b8\u00b9\7p\2\2\u00b9\u00ba\7v\2\2\u00ba")
        buf.write("\u00bb\7g\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7h\2\2\u00bd")
        buf.write("\u00be\7c\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0\7g\2\2\u00c0")
        buf.write("\22\3\2\2\2\u00c1\u00c2\7u\2\2\u00c2\u00c3\7v\2\2\u00c3")
        buf.write("\u00c4\7t\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7p\2\2\u00c6")
        buf.write("\u00c7\7i\2\2\u00c7\24\3\2\2\2\u00c8\u00c9\7k\2\2\u00c9")
        buf.write("\u00ca\7p\2\2\u00ca\u00cb\7v\2\2\u00cb\26\3\2\2\2\u00cc")
        buf.write("\u00cd\7h\2\2\u00cd\u00ce\7n\2\2\u00ce\u00cf\7q\2\2\u00cf")
        buf.write("\u00d0\7c\2\2\u00d0\u00d1\7v\2\2\u00d1\30\3\2\2\2\u00d2")
        buf.write("\u00d3\7d\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7q\2\2\u00d5")
        buf.write("\u00d6\7n\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8\7c\2\2\u00d8")
        buf.write("\u00d9\7p\2\2\u00d9\32\3\2\2\2\u00da\u00db\7e\2\2\u00db")
        buf.write("\u00dc\7q\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7u\2\2\u00de")
        buf.write("\u00df\7v\2\2\u00df\34\3\2\2\2\u00e0\u00e1\7x\2\2\u00e1")
        buf.write("\u00e2\7c\2\2\u00e2\u00e3\7t\2\2\u00e3\36\3\2\2\2\u00e4")
        buf.write("\u00e5\7e\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7p\2\2\u00e7")
        buf.write("\u00e8\7v\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7p\2\2\u00ea")
        buf.write("\u00eb\7w\2\2\u00eb\u00ec\7g\2\2\u00ec \3\2\2\2\u00ed")
        buf.write("\u00ee\7d\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0\7g\2\2\u00f0")
        buf.write("\u00f1\7c\2\2\u00f1\u00f2\7m\2\2\u00f2\"\3\2\2\2\u00f3")
        buf.write("\u00f4\7t\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7p\2\2\u00f6")
        buf.write("\u00f7\7i\2\2\u00f7\u00f8\7g\2\2\u00f8$\3\2\2\2\u00f9")
        buf.write("\u00fa\7p\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc\7n\2\2\u00fc")
        buf.write("&\3\2\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7t\2\2\u00ff")
        buf.write("\u0100\7w\2\2\u0100\u0101\7g\2\2\u0101(\3\2\2\2\u0102")
        buf.write("\u0103\7h\2\2\u0103\u0104\7c\2\2\u0104\u0105\7n\2\2\u0105")
        buf.write("\u0106\7u\2\2\u0106\u0107\7g\2\2\u0107*\3\2\2\2\u0108")
        buf.write("\u0109\7-\2\2\u0109,\3\2\2\2\u010a\u010b\7/\2\2\u010b")
        buf.write(".\3\2\2\2\u010c\u010d\7,\2\2\u010d\60\3\2\2\2\u010e\u010f")
        buf.write("\7\61\2\2\u010f\62\3\2\2\2\u0110\u0111\7\'\2\2\u0111\64")
        buf.write("\3\2\2\2\u0112\u0113\7?\2\2\u0113\u0114\7?\2\2\u0114\66")
        buf.write("\3\2\2\2\u0115\u0116\7#\2\2\u0116\u0117\7?\2\2\u01178")
        buf.write("\3\2\2\2\u0118\u0119\7>\2\2\u0119:\3\2\2\2\u011a\u011b")
        buf.write("\7>\2\2\u011b\u011c\7?\2\2\u011c<\3\2\2\2\u011d\u011e")
        buf.write("\7@\2\2\u011e>\3\2\2\2\u011f\u0120\7@\2\2\u0120\u0121")
        buf.write("\7?\2\2\u0121@\3\2\2\2\u0122\u0123\7(\2\2\u0123\u0124")
        buf.write("\7(\2\2\u0124B\3\2\2\2\u0125\u0126\7~\2\2\u0126\u0127")
        buf.write("\7~\2\2\u0127D\3\2\2\2\u0128\u0129\7#\2\2\u0129F\3\2\2")
        buf.write("\2\u012a\u012b\7?\2\2\u012bH\3\2\2\2\u012c\u012d\7-\2")
        buf.write("\2\u012d\u012e\7?\2\2\u012eJ\3\2\2\2\u012f\u0130\7/\2")
        buf.write("\2\u0130\u0131\7?\2\2\u0131L\3\2\2\2\u0132\u0133\7,\2")
        buf.write("\2\u0133\u0134\7?\2\2\u0134N\3\2\2\2\u0135\u0136\7\61")
        buf.write("\2\2\u0136\u0137\7?\2\2\u0137P\3\2\2\2\u0138\u0139\7\'")
        buf.write("\2\2\u0139\u013a\7?\2\2\u013aR\3\2\2\2\u013b\u013c\7\60")
        buf.write("\2\2\u013cT\3\2\2\2\u013d\u013e\7<\2\2\u013eV\3\2\2\2")
        buf.write("\u013f\u0140\7<\2\2\u0140\u0141\7?\2\2\u0141X\3\2\2\2")
        buf.write("\u0142\u0143\7a\2\2\u0143Z\3\2\2\2\u0144\u0145\7*\2\2")
        buf.write("\u0145\\\3\2\2\2\u0146\u0147\7+\2\2\u0147^\3\2\2\2\u0148")
        buf.write("\u0149\7}\2\2\u0149`\3\2\2\2\u014a\u014b\7\177\2\2\u014b")
        buf.write("b\3\2\2\2\u014c\u014d\7]\2\2\u014dd\3\2\2\2\u014e\u014f")
        buf.write("\7_\2\2\u014ff\3\2\2\2\u0150\u0151\7.\2\2\u0151h\3\2\2")
        buf.write("\2\u0152\u0153\7=\2\2\u0153j\3\2\2\2\u0154\u0158\t\2\2")
        buf.write("\2\u0155\u0157\t\3\2\2\u0156\u0155\3\2\2\2\u0157\u015a")
        buf.write("\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159")
        buf.write("l\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u0164\7\62\2\2\u015c")
        buf.write("\u0160\t\4\2\2\u015d\u015f\t\5\2\2\u015e\u015d\3\2\2\2")
        buf.write("\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3")
        buf.write("\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0163\u015b")
        buf.write("\3\2\2\2\u0163\u015c\3\2\2\2\u0164n\3\2\2\2\u0165\u0166")
        buf.write("\7\62\2\2\u0166\u016a\7z\2\2\u0167\u0168\7\62\2\2\u0168")
        buf.write("\u016a\7Z\2\2\u0169\u0165\3\2\2\2\u0169\u0167\3\2\2\2")
        buf.write("\u016a\u016c\3\2\2\2\u016b\u016d\t\6\2\2\u016c\u016b\3")
        buf.write("\2\2\2\u016d\u016e\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f")
        buf.write("\3\2\2\2\u016fp\3\2\2\2\u0170\u0171\7\62\2\2\u0171\u0175")
        buf.write("\7q\2\2\u0172\u0173\7\62\2\2\u0173\u0175\7Q\2\2\u0174")
        buf.write("\u0170\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0177\3\2\2\2")
        buf.write("\u0176\u0178\t\7\2\2\u0177\u0176\3\2\2\2\u0178\u0179\3")
        buf.write("\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017ar")
        buf.write("\3\2\2\2\u017b\u017c\7\62\2\2\u017c\u0180\7d\2\2\u017d")
        buf.write("\u017e\7\62\2\2\u017e\u0180\7D\2\2\u017f\u017b\3\2\2\2")
        buf.write("\u017f\u017d\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u0183\t")
        buf.write("\b\2\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185t\3\2\2\2\u0186\u0188")
        buf.write("\t\5\2\2\u0187\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018av\3\2\2\2\u018b")
        buf.write("\u018f\7\60\2\2\u018c\u018e\t\5\2\2\u018d\u018c\3\2\2")
        buf.write("\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190")
        buf.write("\3\2\2\2\u0190x\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0194")
        buf.write("\t\t\2\2\u0193\u0195\t\n\2\2\u0194\u0193\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\5u;\2\u0197")
        buf.write("z\3\2\2\2\u0198\u019d\5m\67\2\u0199\u019d\5o8\2\u019a")
        buf.write("\u019d\5q9\2\u019b\u019d\5s:\2\u019c\u0198\3\2\2\2\u019c")
        buf.write("\u0199\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019b\3\2\2\2")
        buf.write("\u019d|\3\2\2\2\u019e\u019f\5u;\2\u019f\u01a1\5w<\2\u01a0")
        buf.write("\u01a2\5y=\2\u01a1\u01a0\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01b3\3\2\2\2\u01a3\u01a4\5u;\2\u01a4\u01a5\5y=\2\u01a5")
        buf.write("\u01b3\3\2\2\2\u01a6\u01a8\5w<\2\u01a7\u01a9\t\5\2\2\u01a8")
        buf.write("\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01a8\3\2\2\2")
        buf.write("\u01aa\u01ab\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac\u01ae\5")
        buf.write("y=\2\u01ad\u01ac\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b3")
        buf.write("\3\2\2\2\u01af\u01b0\5u;\2\u01b0\u01b1\5w<\2\u01b1\u01b3")
        buf.write("\3\2\2\2\u01b2\u019e\3\2\2\2\u01b2\u01a3\3\2\2\2\u01b2")
        buf.write("\u01a6\3\2\2\2\u01b2\u01af\3\2\2\2\u01b3~\3\2\2\2\u01b4")
        buf.write("\u01b5\t\13\2\2\u01b5\u0080\3\2\2\2\u01b6\u01ba\n\f\2")
        buf.write("\2\u01b7\u01b8\7^\2\2\u01b8\u01ba\5\177@\2\u01b9\u01b6")
        buf.write("\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u0082\3\2\2\2\u01bb")
        buf.write("\u01bf\7$\2\2\u01bc\u01be\5\u0081A\2\u01bd\u01bc\3\2\2")
        buf.write("\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0")
        buf.write("\3\2\2\2\u01c0\u01c2\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2")
        buf.write("\u01c3\7$\2\2\u01c3\u01c4\bB\2\2\u01c4\u0084\3\2\2\2\u01c5")
        buf.write("\u01c7\7\17\2\2\u01c6\u01c5\3\2\2\2\u01c6\u01c7\3\2\2")
        buf.write("\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\7\f\2\2\u01c9\u01ca")
        buf.write("\bC\3\2\u01ca\u0086\3\2\2\2\u01cb\u01cd\t\r\2\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cc\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\b")
        buf.write("D\4\2\u01d1\u0088\3\2\2\2\u01d2\u01d3\7\61\2\2\u01d3\u01d4")
        buf.write("\7,\2\2\u01d4\u01d9\3\2\2\2\u01d5\u01d8\5\u0089E\2\u01d6")
        buf.write("\u01d8\13\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d6\3\2\2")
        buf.write("\2\u01d8\u01db\3\2\2\2\u01d9\u01da\3\2\2\2\u01d9\u01d7")
        buf.write("\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc")
        buf.write("\u01dd\7,\2\2\u01dd\u01de\7\61\2\2\u01de\u01df\3\2\2\2")
        buf.write("\u01df\u01e0\bE\4\2\u01e0\u008a\3\2\2\2\u01e1\u01e2\7")
        buf.write("\61\2\2\u01e2\u01e3\7\61\2\2\u01e3\u01e7\3\2\2\2\u01e4")
        buf.write("\u01e6\n\16\2\2\u01e5\u01e4\3\2\2\2\u01e6\u01e9\3\2\2")
        buf.write("\2\u01e7\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01ea")
        buf.write("\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01eb\bF\4\2\u01eb")
        buf.write("\u008c\3\2\2\2\u01ec\u01f0\7$\2\2\u01ed\u01ef\5\u0081")
        buf.write("A\2\u01ee\u01ed\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0\u01ee")
        buf.write("\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f4\3\2\2\2\u01f2")
        buf.write("\u01f0\3\2\2\2\u01f3\u01f5\t\17\2\2\u01f4\u01f3\3\2\2")
        buf.write("\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7\bG\5\2\u01f7\u008e")
        buf.write("\3\2\2\2\u01f8\u01fc\7$\2\2\u01f9\u01fb\5\u0081A\2\u01fa")
        buf.write("\u01f9\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2")
        buf.write("\u01fc\u01fd\3\2\2\2\u01fd\u01ff\3\2\2\2\u01fe\u01fc\3")
        buf.write("\2\2\2\u01ff\u0200\7^\2\2\u0200\u0204\n\13\2\2\u0201\u0203")
        buf.write("\5\u0081A\2\u0202\u0201\3\2\2\2\u0203\u0206\3\2\2\2\u0204")
        buf.write("\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0208\3\2\2\2")
        buf.write("\u0206\u0204\3\2\2\2\u0207\u0209\7$\2\2\u0208\u0207\3")
        buf.write("\2\2\2\u0208\u0209\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020b")
        buf.write("\bH\6\2\u020b\u0090\3\2\2\2\u020c\u020d\13\2\2\2\u020d")
        buf.write("\u020e\bI\7\2\u020e\u0092\3\2\2\2 \2\u0158\u0160\u0163")
        buf.write("\u0169\u016e\u0174\u0179\u017f\u0184\u0189\u018f\u0194")
        buf.write("\u019c\u01a1\u01aa\u01ad\u01b2\u01b9\u01bf\u01c6\u01ce")
        buf.write("\u01d7\u01d9\u01e7\u01f0\u01f4\u01fc\u0204\u0208\b\3B")
        buf.write("\2\3C\3\b\2\2\3G\4\3H\5\3I\6")
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
    UNDERSCORE = 44
    LP = 45
    RP = 46
    LB = 47
    RB = 48
    LSB = 49
    RSB = 50
    COMMA = 51
    SEMI = 52
    ID = 53
    INT_LIT = 54
    FLOAT_LIT = 55
    STRING_LIT = 56
    NEWLINE = 57
    WS = 58
    BLOCK_COMMENT = 59
    LINE_COMMENT = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "':'", 
            "':='", "'_'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
            "';'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
            "GREATER", "GREATER_OR_EQUAL", "AND", "OR", "NOT", "ASSIGN", 
            "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
            "DOT", "COLON", "SHORT_ASSIGN", "UNDERSCORE", "LP", "RP", "LB", 
            "RB", "LSB", "RSB", "COMMA", "SEMI", "ID", "INT_LIT", "FLOAT_LIT", 
            "STRING_LIT", "NEWLINE", "WS", "BLOCK_COMMENT", "LINE_COMMENT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
                  "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
                  "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", 
                  "SHORT_ASSIGN", "UNDERSCORE", "LP", "RP", "LB", "RB", 
                  "LSB", "RSB", "COMMA", "SEMI", "ID", "DECIMAL", "HEX", 
                  "OCTAL", "BINARY", "FLOAT_DECIMAL", "DECIMAL_PART", "EXPONENT", 
                  "INT_LIT", "FLOAT_LIT", "ESC_CHAR", "STR_CHAR", "STRING_LIT", 
                  "NEWLINE", "WS", "BLOCK_COMMENT", "LINE_COMMENT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.preType = None

    def emit(self):
        tk = self.type
        self.preType = tk;
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
            actions[64] = self.STRING_LIT_action 
            actions[65] = self.NEWLINE_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            actions[71] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = self.text[1:-1] 
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    if self.preType in [self.ID, self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT,
                                       self.TRUE, self.FALSE, self.NIL,
                                       self.RETURN, self.CONTINUE, self.BREAK,
                                       self.RP, self.RB, self.RSB
            						   ]:
                        self.text = ';'
                    else:
                        self.skip()
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    if self.text[-1] in ['\r','\n']: #nếu kết thúc bằng dấu xuống dòng thì cắt dấu xuống dòng
                        self.text = self.text[1:-1]
                    else: #nếu kết thúc bằng EOF thì lấy từ đầu chuỗi đến hết
                        self.text = self.text[1:]
                    raise UncloseString(self.text)
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    illegal_str = str(self.text)
                    i = illegal_str.find('\\')
                    while i != -1 and illegal_str[i+1] in 'rnt"\\':
                        i = illegal_str.find('\\', i+2)
                    raise IllegalEscape(illegal_str[1:i+2])
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     



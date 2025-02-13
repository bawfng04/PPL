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
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\7\66")
        buf.write("\u0155\n\66\f\66\16\66\u0158\13\66\3\67\3\67\3\67\7\67")
        buf.write("\u015d\n\67\f\67\16\67\u0160\13\67\5\67\u0162\n\67\38")
        buf.write("\38\38\38\58\u0168\n8\38\68\u016b\n8\r8\168\u016c\39\3")
        buf.write("9\39\39\59\u0173\n9\39\69\u0176\n9\r9\169\u0177\3:\3:")
        buf.write("\3:\3:\5:\u017e\n:\3:\6:\u0181\n:\r:\16:\u0182\3;\6;\u0186")
        buf.write("\n;\r;\16;\u0187\3<\3<\5<\u018c\n<\3<\3<\3=\3=\3=\7=\u0193")
        buf.write("\n=\f=\16=\u0196\13=\3=\5=\u0199\n=\3>\3>\3>\3>\5>\u019f")
        buf.write("\n>\3?\3?\3@\3@\3@\5@\u01a6\n@\3A\3A\7A\u01aa\nA\fA\16")
        buf.write("A\u01ad\13A\3A\3A\3A\3B\5B\u01b3\nB\3B\3B\3B\3C\6C\u01b9")
        buf.write("\nC\rC\16C\u01ba\3C\3C\3D\3D\3D\3D\3D\7D\u01c4\nD\fD\16")
        buf.write("D\u01c7\13D\3D\3D\3D\3D\3D\3E\3E\3E\3E\7E\u01d2\nE\fE")
        buf.write("\16E\u01d5\13E\3E\3E\3F\3F\7F\u01db\nF\fF\16F\u01de\13")
        buf.write("F\3F\5F\u01e1\nF\3F\3F\3G\3G\7G\u01e7\nG\fG\16G\u01ea")
        buf.write("\13G\3G\3G\3G\7G\u01ef\nG\fG\16G\u01f2\13G\3G\3G\3H\3")
        buf.write("H\3H\3\u01c5\2I\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m\2o\2q\2s\2u\2w\2y8{9}\2\177\2\u0081:\u0083;")
        buf.write("\u0085<\u0087=\u0089>\u008b?\u008d@\u008fA\3\2\20\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\5\2\62;CHch\3\2")
        buf.write("\629\3\2\62\63\4\2GGgg\4\2--//\7\2$$^^ppttvv\6\2\f\f\17")
        buf.write("\17$$^^\5\2\13\13\16\17\"\"\4\2\f\f\17\17\4\3\f\f\17\17")
        buf.write("\2\u0209\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
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
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2y\3\2\2\2\2{")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\3\u0091\3\2\2\2\5\u0094\3\2\2")
        buf.write("\2\7\u0099\3\2\2\2\t\u009d\3\2\2\2\13\u00a4\3\2\2\2\r")
        buf.write("\u00a9\3\2\2\2\17\u00ae\3\2\2\2\21\u00b5\3\2\2\2\23\u00bf")
        buf.write("\3\2\2\2\25\u00c6\3\2\2\2\27\u00ca\3\2\2\2\31\u00d0\3")
        buf.write("\2\2\2\33\u00d8\3\2\2\2\35\u00de\3\2\2\2\37\u00e2\3\2")
        buf.write("\2\2!\u00eb\3\2\2\2#\u00f1\3\2\2\2%\u00f7\3\2\2\2\'\u00fb")
        buf.write("\3\2\2\2)\u0100\3\2\2\2+\u0106\3\2\2\2-\u0108\3\2\2\2")
        buf.write("/\u010a\3\2\2\2\61\u010c\3\2\2\2\63\u010e\3\2\2\2\65\u0110")
        buf.write("\3\2\2\2\67\u0113\3\2\2\29\u0116\3\2\2\2;\u0118\3\2\2")
        buf.write("\2=\u011b\3\2\2\2?\u011d\3\2\2\2A\u0120\3\2\2\2C\u0123")
        buf.write("\3\2\2\2E\u0126\3\2\2\2G\u0128\3\2\2\2I\u012a\3\2\2\2")
        buf.write("K\u012d\3\2\2\2M\u0130\3\2\2\2O\u0133\3\2\2\2Q\u0136\3")
        buf.write("\2\2\2S\u0139\3\2\2\2U\u013b\3\2\2\2W\u013d\3\2\2\2Y\u0140")
        buf.write("\3\2\2\2[\u0142\3\2\2\2]\u0144\3\2\2\2_\u0146\3\2\2\2")
        buf.write("a\u0148\3\2\2\2c\u014a\3\2\2\2e\u014c\3\2\2\2g\u014e\3")
        buf.write("\2\2\2i\u0150\3\2\2\2k\u0152\3\2\2\2m\u0161\3\2\2\2o\u0167")
        buf.write("\3\2\2\2q\u0172\3\2\2\2s\u017d\3\2\2\2u\u0185\3\2\2\2")
        buf.write("w\u0189\3\2\2\2y\u018f\3\2\2\2{\u019e\3\2\2\2}\u01a0\3")
        buf.write("\2\2\2\177\u01a5\3\2\2\2\u0081\u01a7\3\2\2\2\u0083\u01b2")
        buf.write("\3\2\2\2\u0085\u01b8\3\2\2\2\u0087\u01be\3\2\2\2\u0089")
        buf.write("\u01cd\3\2\2\2\u008b\u01d8\3\2\2\2\u008d\u01e4\3\2\2\2")
        buf.write("\u008f\u01f5\3\2\2\2\u0091\u0092\7k\2\2\u0092\u0093\7")
        buf.write("h\2\2\u0093\4\3\2\2\2\u0094\u0095\7g\2\2\u0095\u0096\7")
        buf.write("n\2\2\u0096\u0097\7u\2\2\u0097\u0098\7g\2\2\u0098\6\3")
        buf.write("\2\2\2\u0099\u009a\7h\2\2\u009a\u009b\7q\2\2\u009b\u009c")
        buf.write("\7t\2\2\u009c\b\3\2\2\2\u009d\u009e\7t\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\u00a0\7v\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2")
        buf.write("\7t\2\2\u00a2\u00a3\7p\2\2\u00a3\n\3\2\2\2\u00a4\u00a5")
        buf.write("\7h\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8")
        buf.write("\7e\2\2\u00a8\f\3\2\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab")
        buf.write("\7{\2\2\u00ab\u00ac\7r\2\2\u00ac\u00ad\7g\2\2\u00ad\16")
        buf.write("\3\2\2\2\u00ae\u00af\7u\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1")
        buf.write("\7t\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3\7e\2\2\u00b3\u00b4")
        buf.write("\7v\2\2\u00b4\20\3\2\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7")
        buf.write("\7p\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba")
        buf.write("\7t\2\2\u00ba\u00bb\7h\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd")
        buf.write("\7e\2\2\u00bd\u00be\7g\2\2\u00be\22\3\2\2\2\u00bf\u00c0")
        buf.write("\7u\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7i\2\2\u00c5\24")
        buf.write("\3\2\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\26\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc")
        buf.write("\7n\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf")
        buf.write("\7v\2\2\u00cf\30\3\2\2\2\u00d0\u00d1\7d\2\2\u00d1\u00d2")
        buf.write("\7q\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5")
        buf.write("\7g\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7p\2\2\u00d7\32")
        buf.write("\3\2\2\2\u00d8\u00d9\7e\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7v\2\2\u00dd\34")
        buf.write("\3\2\2\2\u00de\u00df\7x\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\36\3\2\2\2\u00e2\u00e3\7e\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7")
        buf.write("\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea \3\2\2\2\u00eb\u00ec\7d\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0")
        buf.write("\7m\2\2\u00f0\"\3\2\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3")
        buf.write("\7c\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7i\2\2\u00f5\u00f6")
        buf.write("\7g\2\2\u00f6$\3\2\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7k\2\2\u00f9\u00fa\7n\2\2\u00fa&\3\2\2\2\u00fb\u00fc")
        buf.write("\7v\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff")
        buf.write("\7g\2\2\u00ff(\3\2\2\2\u0100\u0101\7h\2\2\u0101\u0102")
        buf.write("\7c\2\2\u0102\u0103\7n\2\2\u0103\u0104\7u\2\2\u0104\u0105")
        buf.write("\7g\2\2\u0105*\3\2\2\2\u0106\u0107\7-\2\2\u0107,\3\2\2")
        buf.write("\2\u0108\u0109\7/\2\2\u0109.\3\2\2\2\u010a\u010b\7,\2")
        buf.write("\2\u010b\60\3\2\2\2\u010c\u010d\7\61\2\2\u010d\62\3\2")
        buf.write("\2\2\u010e\u010f\7\'\2\2\u010f\64\3\2\2\2\u0110\u0111")
        buf.write("\7?\2\2\u0111\u0112\7?\2\2\u0112\66\3\2\2\2\u0113\u0114")
        buf.write("\7#\2\2\u0114\u0115\7?\2\2\u01158\3\2\2\2\u0116\u0117")
        buf.write("\7>\2\2\u0117:\3\2\2\2\u0118\u0119\7>\2\2\u0119\u011a")
        buf.write("\7?\2\2\u011a<\3\2\2\2\u011b\u011c\7@\2\2\u011c>\3\2\2")
        buf.write("\2\u011d\u011e\7@\2\2\u011e\u011f\7?\2\2\u011f@\3\2\2")
        buf.write("\2\u0120\u0121\7(\2\2\u0121\u0122\7(\2\2\u0122B\3\2\2")
        buf.write("\2\u0123\u0124\7~\2\2\u0124\u0125\7~\2\2\u0125D\3\2\2")
        buf.write("\2\u0126\u0127\7#\2\2\u0127F\3\2\2\2\u0128\u0129\7?\2")
        buf.write("\2\u0129H\3\2\2\2\u012a\u012b\7-\2\2\u012b\u012c\7?\2")
        buf.write("\2\u012cJ\3\2\2\2\u012d\u012e\7/\2\2\u012e\u012f\7?\2")
        buf.write("\2\u012fL\3\2\2\2\u0130\u0131\7,\2\2\u0131\u0132\7?\2")
        buf.write("\2\u0132N\3\2\2\2\u0133\u0134\7\61\2\2\u0134\u0135\7?")
        buf.write("\2\2\u0135P\3\2\2\2\u0136\u0137\7\'\2\2\u0137\u0138\7")
        buf.write("?\2\2\u0138R\3\2\2\2\u0139\u013a\7\60\2\2\u013aT\3\2\2")
        buf.write("\2\u013b\u013c\7<\2\2\u013cV\3\2\2\2\u013d\u013e\7<\2")
        buf.write("\2\u013e\u013f\7?\2\2\u013fX\3\2\2\2\u0140\u0141\7a\2")
        buf.write("\2\u0141Z\3\2\2\2\u0142\u0143\7*\2\2\u0143\\\3\2\2\2\u0144")
        buf.write("\u0145\7+\2\2\u0145^\3\2\2\2\u0146\u0147\7}\2\2\u0147")
        buf.write("`\3\2\2\2\u0148\u0149\7\177\2\2\u0149b\3\2\2\2\u014a\u014b")
        buf.write("\7]\2\2\u014bd\3\2\2\2\u014c\u014d\7_\2\2\u014df\3\2\2")
        buf.write("\2\u014e\u014f\7.\2\2\u014fh\3\2\2\2\u0150\u0151\7=\2")
        buf.write("\2\u0151j\3\2\2\2\u0152\u0156\t\2\2\2\u0153\u0155\t\3")
        buf.write("\2\2\u0154\u0153\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157l\3\2\2\2\u0158\u0156")
        buf.write("\3\2\2\2\u0159\u0162\7\62\2\2\u015a\u015e\t\4\2\2\u015b")
        buf.write("\u015d\t\5\2\2\u015c\u015b\3\2\2\2\u015d\u0160\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0162\3")
        buf.write("\2\2\2\u0160\u015e\3\2\2\2\u0161\u0159\3\2\2\2\u0161\u015a")
        buf.write("\3\2\2\2\u0162n\3\2\2\2\u0163\u0164\7\62\2\2\u0164\u0168")
        buf.write("\7z\2\2\u0165\u0166\7\62\2\2\u0166\u0168\7Z\2\2\u0167")
        buf.write("\u0163\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u016a\3\2\2\2")
        buf.write("\u0169\u016b\t\6\2\2\u016a\u0169\3\2\2\2\u016b\u016c\3")
        buf.write("\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016dp")
        buf.write("\3\2\2\2\u016e\u016f\7\62\2\2\u016f\u0173\7q\2\2\u0170")
        buf.write("\u0171\7\62\2\2\u0171\u0173\7Q\2\2\u0172\u016e\3\2\2\2")
        buf.write("\u0172\u0170\3\2\2\2\u0173\u0175\3\2\2\2\u0174\u0176\t")
        buf.write("\7\2\2\u0175\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0175")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178r\3\2\2\2\u0179\u017a")
        buf.write("\7\62\2\2\u017a\u017e\7d\2\2\u017b\u017c\7\62\2\2\u017c")
        buf.write("\u017e\7D\2\2\u017d\u0179\3\2\2\2\u017d\u017b\3\2\2\2")
        buf.write("\u017e\u0180\3\2\2\2\u017f\u0181\t\b\2\2\u0180\u017f\3")
        buf.write("\2\2\2\u0181\u0182\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183t\3\2\2\2\u0184\u0186\t\5\2\2\u0185\u0184")
        buf.write("\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0185\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188v\3\2\2\2\u0189\u018b\t\t\2\2\u018a")
        buf.write("\u018c\t\n\2\2\u018b\u018a\3\2\2\2\u018b\u018c\3\2\2\2")
        buf.write("\u018c\u018d\3\2\2\2\u018d\u018e\5u;\2\u018ex\3\2\2\2")
        buf.write("\u018f\u0190\5u;\2\u0190\u0194\7\60\2\2\u0191\u0193\t")
        buf.write("\5\2\2\u0192\u0191\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0198\3\2\2\2\u0196")
        buf.write("\u0194\3\2\2\2\u0197\u0199\5w<\2\u0198\u0197\3\2\2\2\u0198")
        buf.write("\u0199\3\2\2\2\u0199z\3\2\2\2\u019a\u019f\5m\67\2\u019b")
        buf.write("\u019f\5o8\2\u019c\u019f\5q9\2\u019d\u019f\5s:\2\u019e")
        buf.write("\u019a\3\2\2\2\u019e\u019b\3\2\2\2\u019e\u019c\3\2\2\2")
        buf.write("\u019e\u019d\3\2\2\2\u019f|\3\2\2\2\u01a0\u01a1\t\13\2")
        buf.write("\2\u01a1~\3\2\2\2\u01a2\u01a6\n\f\2\2\u01a3\u01a4\7^\2")
        buf.write("\2\u01a4\u01a6\5}?\2\u01a5\u01a2\3\2\2\2\u01a5\u01a3\3")
        buf.write("\2\2\2\u01a6\u0080\3\2\2\2\u01a7\u01ab\7$\2\2\u01a8\u01aa")
        buf.write("\5\177@\2\u01a9\u01a8\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab")
        buf.write("\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2")
        buf.write("\u01ad\u01ab\3\2\2\2\u01ae\u01af\7$\2\2\u01af\u01b0\b")
        buf.write("A\2\2\u01b0\u0082\3\2\2\2\u01b1\u01b3\7\17\2\2\u01b2\u01b1")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b5\7\f\2\2\u01b5\u01b6\bB\3\2\u01b6\u0084\3\2\2\2")
        buf.write("\u01b7\u01b9\t\r\2\2\u01b8\u01b7\3\2\2\2\u01b9\u01ba\3")
        buf.write("\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc")
        buf.write("\3\2\2\2\u01bc\u01bd\bC\4\2\u01bd\u0086\3\2\2\2\u01be")
        buf.write("\u01bf\7\61\2\2\u01bf\u01c0\7,\2\2\u01c0\u01c5\3\2\2\2")
        buf.write("\u01c1\u01c4\5\u0087D\2\u01c2\u01c4\13\2\2\2\u01c3\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5")
        buf.write("\u01c6\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c8\3\2\2\2")
        buf.write("\u01c7\u01c5\3\2\2\2\u01c8\u01c9\7,\2\2\u01c9\u01ca\7")
        buf.write("\61\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc\bD\4\2\u01cc\u0088")
        buf.write("\3\2\2\2\u01cd\u01ce\7\61\2\2\u01ce\u01cf\7\61\2\2\u01cf")
        buf.write("\u01d3\3\2\2\2\u01d0\u01d2\n\16\2\2\u01d1\u01d0\3\2\2")
        buf.write("\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4")
        buf.write("\3\2\2\2\u01d4\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6")
        buf.write("\u01d7\bE\4\2\u01d7\u008a\3\2\2\2\u01d8\u01dc\7$\2\2\u01d9")
        buf.write("\u01db\5\177@\2\u01da\u01d9\3\2\2\2\u01db\u01de\3\2\2")
        buf.write("\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01e0")
        buf.write("\3\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e1\t\17\2\2\u01e0")
        buf.write("\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3\bF\5\2")
        buf.write("\u01e3\u008c\3\2\2\2\u01e4\u01e8\7$\2\2\u01e5\u01e7\5")
        buf.write("\177@\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8")
        buf.write("\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01eb\3\2\2\2")
        buf.write("\u01ea\u01e8\3\2\2\2\u01eb\u01ec\7^\2\2\u01ec\u01f0\n")
        buf.write("\13\2\2\u01ed\u01ef\5\177@\2\u01ee\u01ed\3\2\2\2\u01ef")
        buf.write("\u01f2\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2")
        buf.write("\u01f1\u01f3\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f3\u01f4\b")
        buf.write("G\6\2\u01f4\u008e\3\2\2\2\u01f5\u01f6\13\2\2\2\u01f6\u01f7")
        buf.write("\bH\7\2\u01f7\u0090\3\2\2\2\34\2\u0156\u015e\u0161\u0167")
        buf.write("\u016c\u0172\u0177\u017d\u0182\u0187\u018b\u0194\u0198")
        buf.write("\u019e\u01a5\u01ab\u01b2\u01ba\u01c3\u01c5\u01d3\u01dc")
        buf.write("\u01e0\u01e8\u01f0\b\3A\2\3B\3\b\2\2\3F\4\3G\5\3H\6")
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
    FLOAT_LIT = 54
    INT_LIT = 55
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
            "RB", "LSB", "RSB", "COMMA", "SEMI", "ID", "FLOAT_LIT", "INT_LIT", 
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
                  "OCTAL", "BINARY", "FLOAT_DECIMAL", "EXPONENT", "FLOAT_LIT", 
                  "INT_LIT", "ESC_CHAR", "STR_CHAR", "STRING_LIT", "NEWLINE", 
                  "WS", "BLOCK_COMMENT", "LINE_COMMENT", "UNCLOSE_STRING", 
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
            actions[63] = self.STRING_LIT_action 
            actions[64] = self.NEWLINE_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.ERROR_CHAR_action 
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
                        self.text = '\"' + self.text[1:-1]
                    else: #nếu kết thúc bằng EOF thì lấy từ đầu chuỗi đến hết
                        self.text = '\"' + self.text[1:]
                    raise UncloseString(self.text)
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    illegal_str = self.text[1:] # Remove leading quote
                    result = '"' + illegal_str # Reconstruct with leading quote
                    raise IllegalEscape(result)
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     



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
        buf.write("\u0211\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\7\63\u0150\n\63\f\63\16\63\u0153")
        buf.write("\13\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\66\5\66\u015d")
        buf.write("\n\66\3\66\6\66\u0160\n\66\r\66\16\66\u0161\3\67\3\67")
        buf.write("\38\38\38\38\58\u016a\n8\38\68\u016d\n8\r8\168\u016e\3")
        buf.write("9\39\39\79\u0174\n9\f9\169\u0177\139\59\u0179\n9\3:\3")
        buf.write(":\7:\u017d\n:\f:\16:\u0180\13:\3;\3;\3<\3<\3<\3<\5<\u0188")
        buf.write("\n<\3<\6<\u018b\n<\r<\16<\u018c\3=\3=\5=\u0191\n=\3=\6")
        buf.write("=\u0194\n=\r=\16=\u0195\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>")
        buf.write("\5>\u01a2\n>\3?\6?\u01a5\n?\r?\16?\u01a6\3?\3?\5?\u01ab")
        buf.write("\n?\3?\3?\5?\u01af\n?\3?\6?\u01b2\n?\r?\16?\u01b3\3?\5")
        buf.write("?\u01b7\n?\3@\3@\3A\3A\3A\5A\u01be\nA\3B\3B\7B\u01c2\n")
        buf.write("B\fB\16B\u01c5\13B\3B\3B\3B\3C\6C\u01cb\nC\rC\16C\u01cc")
        buf.write("\3C\3C\3D\5D\u01d2\nD\3D\3D\3D\3D\3E\3E\3E\3E\7E\u01dc")
        buf.write("\nE\fE\16E\u01df\13E\3E\3E\3F\3F\3F\3F\3F\7F\u01e8\nF")
        buf.write("\fF\16F\u01eb\13F\3F\3F\3F\3F\3F\3G\3G\7G\u01f4\nG\fG")
        buf.write("\16G\u01f7\13G\3G\5G\u01fa\nG\3G\3G\3H\3H\7H\u0200\nH")
        buf.write("\fH\16H\u0203\13H\3H\3H\3H\7H\u0208\nH\fH\16H\u020b\13")
        buf.write("H\3H\3H\3I\3I\3I\3\u01e9\2J\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\2i\2k\2m\2o\2q\2s\2u\2w\2y\2{\65}\66\177\2\u0081")
        buf.write("\2\u0083\67\u00858\u00879\u0089:\u008b;\u008d<\u008f=")
        buf.write("\u0091>\3\2\20\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\62")
        buf.write("9\5\2\62;CHch\3\2\63;\3\2\62\63\4\2GGgg\4\2--//\t\2$$")
        buf.write("))^^ddppttvv\6\2\f\f\17\17$$^^\5\2\13\f\16\17\"\"\4\2")
        buf.write("\f\f\17\17\4\3\f\f\17\17\2\u0223\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\3\u0093\3\2\2\2\5\u0096\3\2\2\2\7\u009b\3\2\2")
        buf.write("\2\t\u009f\3\2\2\2\13\u00a6\3\2\2\2\r\u00ab\3\2\2\2\17")
        buf.write("\u00b0\3\2\2\2\21\u00b7\3\2\2\2\23\u00c1\3\2\2\2\25\u00c8")
        buf.write("\3\2\2\2\27\u00cc\3\2\2\2\31\u00d2\3\2\2\2\33\u00da\3")
        buf.write("\2\2\2\35\u00e0\3\2\2\2\37\u00e4\3\2\2\2!\u00ed\3\2\2")
        buf.write("\2#\u00f3\3\2\2\2%\u00f9\3\2\2\2\'\u00fd\3\2\2\2)\u0102")
        buf.write("\3\2\2\2+\u0108\3\2\2\2-\u010a\3\2\2\2/\u010c\3\2\2\2")
        buf.write("\61\u010e\3\2\2\2\63\u0110\3\2\2\2\65\u0112\3\2\2\2\67")
        buf.write("\u0115\3\2\2\29\u0118\3\2\2\2;\u011a\3\2\2\2=\u011d\3")
        buf.write("\2\2\2?\u011f\3\2\2\2A\u0122\3\2\2\2C\u0125\3\2\2\2E\u0128")
        buf.write("\3\2\2\2G\u012a\3\2\2\2I\u012c\3\2\2\2K\u012f\3\2\2\2")
        buf.write("M\u0132\3\2\2\2O\u0135\3\2\2\2Q\u0138\3\2\2\2S\u013b\3")
        buf.write("\2\2\2U\u013d\3\2\2\2W\u013f\3\2\2\2Y\u0141\3\2\2\2[\u0143")
        buf.write("\3\2\2\2]\u0145\3\2\2\2_\u0147\3\2\2\2a\u0149\3\2\2\2")
        buf.write("c\u014b\3\2\2\2e\u014d\3\2\2\2g\u0154\3\2\2\2i\u0156\3")
        buf.write("\2\2\2k\u015c\3\2\2\2m\u0163\3\2\2\2o\u0169\3\2\2\2q\u0178")
        buf.write("\3\2\2\2s\u017a\3\2\2\2u\u0181\3\2\2\2w\u0187\3\2\2\2")
        buf.write("y\u018e\3\2\2\2{\u01a1\3\2\2\2}\u01b6\3\2\2\2\177\u01b8")
        buf.write("\3\2\2\2\u0081\u01bd\3\2\2\2\u0083\u01bf\3\2\2\2\u0085")
        buf.write("\u01ca\3\2\2\2\u0087\u01d1\3\2\2\2\u0089\u01d7\3\2\2\2")
        buf.write("\u008b\u01e2\3\2\2\2\u008d\u01f1\3\2\2\2\u008f\u01fd\3")
        buf.write("\2\2\2\u0091\u020e\3\2\2\2\u0093\u0094\7k\2\2\u0094\u0095")
        buf.write("\7h\2\2\u0095\4\3\2\2\2\u0096\u0097\7g\2\2\u0097\u0098")
        buf.write("\7n\2\2\u0098\u0099\7u\2\2\u0099\u009a\7g\2\2\u009a\6")
        buf.write("\3\2\2\2\u009b\u009c\7h\2\2\u009c\u009d\7q\2\2\u009d\u009e")
        buf.write("\7t\2\2\u009e\b\3\2\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1")
        buf.write("\7g\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3\7w\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\u00a5\7p\2\2\u00a5\n\3\2\2\2\u00a6\u00a7")
        buf.write("\7h\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa")
        buf.write("\7e\2\2\u00aa\f\3\2\2\2\u00ab\u00ac\7v\2\2\u00ac\u00ad")
        buf.write("\7{\2\2\u00ad\u00ae\7r\2\2\u00ae\u00af\7g\2\2\u00af\16")
        buf.write("\3\2\2\2\u00b0\u00b1\7u\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3")
        buf.write("\7t\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7e\2\2\u00b5\u00b6")
        buf.write("\7v\2\2\u00b6\20\3\2\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9")
        buf.write("\7p\2\2\u00b9\u00ba\7v\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7h\2\2\u00bd\u00be\7c\2\2\u00be\u00bf")
        buf.write("\7e\2\2\u00bf\u00c0\7g\2\2\u00c0\22\3\2\2\2\u00c1\u00c2")
        buf.write("\7u\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5")
        buf.write("\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7i\2\2\u00c7\24")
        buf.write("\3\2\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb")
        buf.write("\7v\2\2\u00cb\26\3\2\2\2\u00cc\u00cd\7h\2\2\u00cd\u00ce")
        buf.write("\7n\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1")
        buf.write("\7v\2\2\u00d1\30\3\2\2\2\u00d2\u00d3\7d\2\2\u00d3\u00d4")
        buf.write("\7q\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7p\2\2\u00d9\32")
        buf.write("\3\2\2\2\u00da\u00db\7e\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd\u00de\7u\2\2\u00de\u00df\7v\2\2\u00df\34")
        buf.write("\3\2\2\2\u00e0\u00e1\7x\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3")
        buf.write("\7t\2\2\u00e3\36\3\2\2\2\u00e4\u00e5\7e\2\2\u00e5\u00e6")
        buf.write("\7q\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9")
        buf.write("\7k\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec")
        buf.write("\7g\2\2\u00ec \3\2\2\2\u00ed\u00ee\7d\2\2\u00ee\u00ef")
        buf.write("\7t\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2")
        buf.write("\7m\2\2\u00f2\"\3\2\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5")
        buf.write("\7c\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7i\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8$\3\2\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb")
        buf.write("\7k\2\2\u00fb\u00fc\7n\2\2\u00fc&\3\2\2\2\u00fd\u00fe")
        buf.write("\7v\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7w\2\2\u0100\u0101")
        buf.write("\7g\2\2\u0101(\3\2\2\2\u0102\u0103\7h\2\2\u0103\u0104")
        buf.write("\7c\2\2\u0104\u0105\7n\2\2\u0105\u0106\7u\2\2\u0106\u0107")
        buf.write("\7g\2\2\u0107*\3\2\2\2\u0108\u0109\7-\2\2\u0109,\3\2\2")
        buf.write("\2\u010a\u010b\7/\2\2\u010b.\3\2\2\2\u010c\u010d\7,\2")
        buf.write("\2\u010d\60\3\2\2\2\u010e\u010f\7\61\2\2\u010f\62\3\2")
        buf.write("\2\2\u0110\u0111\7\'\2\2\u0111\64\3\2\2\2\u0112\u0113")
        buf.write("\7?\2\2\u0113\u0114\7?\2\2\u0114\66\3\2\2\2\u0115\u0116")
        buf.write("\7#\2\2\u0116\u0117\7?\2\2\u01178\3\2\2\2\u0118\u0119")
        buf.write("\7>\2\2\u0119:\3\2\2\2\u011a\u011b\7>\2\2\u011b\u011c")
        buf.write("\7?\2\2\u011c<\3\2\2\2\u011d\u011e\7@\2\2\u011e>\3\2\2")
        buf.write("\2\u011f\u0120\7@\2\2\u0120\u0121\7?\2\2\u0121@\3\2\2")
        buf.write("\2\u0122\u0123\7(\2\2\u0123\u0124\7(\2\2\u0124B\3\2\2")
        buf.write("\2\u0125\u0126\7~\2\2\u0126\u0127\7~\2\2\u0127D\3\2\2")
        buf.write("\2\u0128\u0129\7#\2\2\u0129F\3\2\2\2\u012a\u012b\7?\2")
        buf.write("\2\u012bH\3\2\2\2\u012c\u012d\7-\2\2\u012d\u012e\7?\2")
        buf.write("\2\u012eJ\3\2\2\2\u012f\u0130\7/\2\2\u0130\u0131\7?\2")
        buf.write("\2\u0131L\3\2\2\2\u0132\u0133\7,\2\2\u0133\u0134\7?\2")
        buf.write("\2\u0134N\3\2\2\2\u0135\u0136\7\61\2\2\u0136\u0137\7?")
        buf.write("\2\2\u0137P\3\2\2\2\u0138\u0139\7\'\2\2\u0139\u013a\7")
        buf.write("?\2\2\u013aR\3\2\2\2\u013b\u013c\7\60\2\2\u013cT\3\2\2")
        buf.write("\2\u013d\u013e\7*\2\2\u013eV\3\2\2\2\u013f\u0140\7+\2")
        buf.write("\2\u0140X\3\2\2\2\u0141\u0142\7}\2\2\u0142Z\3\2\2\2\u0143")
        buf.write("\u0144\7\177\2\2\u0144\\\3\2\2\2\u0145\u0146\7]\2\2\u0146")
        buf.write("^\3\2\2\2\u0147\u0148\7_\2\2\u0148`\3\2\2\2\u0149\u014a")
        buf.write("\7.\2\2\u014ab\3\2\2\2\u014b\u014c\7=\2\2\u014cd\3\2\2")
        buf.write("\2\u014d\u0151\t\2\2\2\u014e\u0150\t\3\2\2\u014f\u014e")
        buf.write("\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u0152f\3\2\2\2\u0153\u0151\3\2\2\2\u0154")
        buf.write("\u0155\t\4\2\2\u0155h\3\2\2\2\u0156\u0157\t\5\2\2\u0157")
        buf.write("j\3\2\2\2\u0158\u0159\7\62\2\2\u0159\u015d\7q\2\2\u015a")
        buf.write("\u015b\7\62\2\2\u015b\u015d\7Q\2\2\u015c\u0158\3\2\2\2")
        buf.write("\u015c\u015a\3\2\2\2\u015d\u015f\3\2\2\2\u015e\u0160\t")
        buf.write("\5\2\2\u015f\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u015f")
        buf.write("\3\2\2\2\u0161\u0162\3\2\2\2\u0162l\3\2\2\2\u0163\u0164")
        buf.write("\t\6\2\2\u0164n\3\2\2\2\u0165\u0166\7\62\2\2\u0166\u016a")
        buf.write("\7z\2\2\u0167\u0168\7\62\2\2\u0168\u016a\7Z\2\2\u0169")
        buf.write("\u0165\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016c\3\2\2\2")
        buf.write("\u016b\u016d\t\6\2\2\u016c\u016b\3\2\2\2\u016d\u016e\3")
        buf.write("\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016fp")
        buf.write("\3\2\2\2\u0170\u0179\7\62\2\2\u0171\u0175\t\7\2\2\u0172")
        buf.write("\u0174\t\4\2\2\u0173\u0172\3\2\2\2\u0174\u0177\3\2\2\2")
        buf.write("\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0179\3")
        buf.write("\2\2\2\u0177\u0175\3\2\2\2\u0178\u0170\3\2\2\2\u0178\u0171")
        buf.write("\3\2\2\2\u0179r\3\2\2\2\u017a\u017e\7\60\2\2\u017b\u017d")
        buf.write("\t\4\2\2\u017c\u017b\3\2\2\2\u017d\u0180\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017ft\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0181\u0182\t\b\2\2\u0182v\3\2\2\2\u0183")
        buf.write("\u0184\7\62\2\2\u0184\u0188\7d\2\2\u0185\u0186\7\62\2")
        buf.write("\2\u0186\u0188\7D\2\2\u0187\u0183\3\2\2\2\u0187\u0185")
        buf.write("\3\2\2\2\u0188\u018a\3\2\2\2\u0189\u018b\t\b\2\2\u018a")
        buf.write("\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018a\3\2\2\2")
        buf.write("\u018c\u018d\3\2\2\2\u018dx\3\2\2\2\u018e\u0190\t\t\2")
        buf.write("\2\u018f\u0191\t\n\2\2\u0190\u018f\3\2\2\2\u0190\u0191")
        buf.write("\3\2\2\2\u0191\u0193\3\2\2\2\u0192\u0194\t\4\2\2\u0193")
        buf.write("\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0193\3\2\2\2")
        buf.write("\u0195\u0196\3\2\2\2\u0196z\3\2\2\2\u0197\u01a2\5q9\2")
        buf.write("\u0198\u0199\5o8\2\u0199\u019a\b>\2\2\u019a\u01a2\3\2")
        buf.write("\2\2\u019b\u019c\5k\66\2\u019c\u019d\b>\3\2\u019d\u01a2")
        buf.write("\3\2\2\2\u019e\u019f\5w<\2\u019f\u01a0\b>\4\2\u01a0\u01a2")
        buf.write("\3\2\2\2\u01a1\u0197\3\2\2\2\u01a1\u0198\3\2\2\2\u01a1")
        buf.write("\u019b\3\2\2\2\u01a1\u019e\3\2\2\2\u01a2|\3\2\2\2\u01a3")
        buf.write("\u01a5\t\4\2\2\u01a4\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2")
        buf.write("\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\3")
        buf.write("\2\2\2\u01a8\u01aa\5s:\2\u01a9\u01ab\5y=\2\u01aa\u01a9")
        buf.write("\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01b7\3\2\2\2\u01ac")
        buf.write("\u01ae\5s:\2\u01ad\u01af\5y=\2\u01ae\u01ad\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01b7\3\2\2\2\u01b0\u01b2\t\4\2\2")
        buf.write("\u01b1\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b1\3")
        buf.write("\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b7")
        buf.write("\5y=\2\u01b6\u01a4\3\2\2\2\u01b6\u01ac\3\2\2\2\u01b6\u01b1")
        buf.write("\3\2\2\2\u01b7~\3\2\2\2\u01b8\u01b9\t\13\2\2\u01b9\u0080")
        buf.write("\3\2\2\2\u01ba\u01be\n\f\2\2\u01bb\u01bc\7^\2\2\u01bc")
        buf.write("\u01be\5\177@\2\u01bd\u01ba\3\2\2\2\u01bd\u01bb\3\2\2")
        buf.write("\2\u01be\u0082\3\2\2\2\u01bf\u01c3\7$\2\2\u01c0\u01c2")
        buf.write("\5\u0081A\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c6\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c6\u01c7\7$\2\2\u01c7\u01c8\b")
        buf.write("B\5\2\u01c8\u0084\3\2\2\2\u01c9\u01cb\t\r\2\2\u01ca\u01c9")
        buf.write("\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\bC\6\2")
        buf.write("\u01cf\u0086\3\2\2\2\u01d0\u01d2\7\17\2\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3")
        buf.write("\u01d4\7\f\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6\bD\6\2")
        buf.write("\u01d6\u0088\3\2\2\2\u01d7\u01d8\7\61\2\2\u01d8\u01d9")
        buf.write("\7\61\2\2\u01d9\u01dd\3\2\2\2\u01da\u01dc\n\16\2\2\u01db")
        buf.write("\u01da\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01dd\u01de\3\2\2\2\u01de\u01e0\3\2\2\2\u01df\u01dd\3")
        buf.write("\2\2\2\u01e0\u01e1\bE\6\2\u01e1\u008a\3\2\2\2\u01e2\u01e3")
        buf.write("\7\61\2\2\u01e3\u01e4\7,\2\2\u01e4\u01e9\3\2\2\2\u01e5")
        buf.write("\u01e8\5\u008bF\2\u01e6\u01e8\13\2\2\2\u01e7\u01e5\3\2")
        buf.write("\2\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01ea")
        buf.write("\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01ec\3\2\2\2\u01eb")
        buf.write("\u01e9\3\2\2\2\u01ec\u01ed\7,\2\2\u01ed\u01ee\7\61\2\2")
        buf.write("\u01ee\u01ef\3\2\2\2\u01ef\u01f0\bF\6\2\u01f0\u008c\3")
        buf.write("\2\2\2\u01f1\u01f5\7$\2\2\u01f2\u01f4\5\u0081A\2\u01f3")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f5\u01f6\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3")
        buf.write("\2\2\2\u01f8\u01fa\t\17\2\2\u01f9\u01f8\3\2\2\2\u01fa")
        buf.write("\u01fb\3\2\2\2\u01fb\u01fc\bG\7\2\u01fc\u008e\3\2\2\2")
        buf.write("\u01fd\u0201\7$\2\2\u01fe\u0200\5\u0081A\2\u01ff\u01fe")
        buf.write("\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202\u0204\3\2\2\2\u0203\u0201\3\2\2\2")
        buf.write("\u0204\u0205\7^\2\2\u0205\u0209\n\13\2\2\u0206\u0208\5")
        buf.write("\u0081A\2\u0207\u0206\3\2\2\2\u0208\u020b\3\2\2\2\u0209")
        buf.write("\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020c\3\2\2\2")
        buf.write("\u020b\u0209\3\2\2\2\u020c\u020d\bH\b\2\u020d\u0090\3")
        buf.write("\2\2\2\u020e\u020f\13\2\2\2\u020f\u0210\bI\t\2\u0210\u0092")
        buf.write("\3\2\2\2 \2\u0151\u015c\u0161\u0169\u016e\u0175\u0178")
        buf.write("\u017e\u0187\u018c\u0190\u0195\u01a1\u01a6\u01aa\u01ae")
        buf.write("\u01b3\u01b6\u01bd\u01c3\u01cc\u01d1\u01dd\u01e7\u01e9")
        buf.write("\u01f5\u01f9\u0201\u0209\n\3>\2\3>\3\3>\4\3B\5\b\2\2\3")
        buf.write("G\6\3H\7\3I\b")
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
    LP = 42
    RP = 43
    LB = 44
    RB = 45
    LSB = 46
    RSB = 47
    COMMA = 48
    SEMI = 49
    ID = 50
    INT_LIT = 51
    FLOAT_LIT = 52
    STRING_LIT = 53
    WS = 54
    NEWLINE = 55
    LINE_COMMENT = 56
    BLOCK_COMMENT = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59
    ERROR_CHAR = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
            "GREATER", "GREATER_OR_EQUAL", "AND", "OR", "NOT", "ASSIGN", 
            "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
            "DOT", "LP", "RP", "LB", "RB", "LSB", "RSB", "COMMA", "SEMI", 
            "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", "NEWLINE", 
            "LINE_COMMENT", "BLOCK_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
                  "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
                  "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "LP", 
                  "RP", "LB", "RB", "LSB", "RSB", "COMMA", "SEMI", "ID", 
                  "DIGIT", "OCTAL_DIGIT", "OCTAL", "HEX_DIGIT", "HEX", "DECIMAL", 
                  "DECIMAL_PART", "BINARY_DIGIT", "BINARY", "EXPONENT", 
                  "INT_LIT", "FLOAT_LIT", "ESC_CHAR", "STR_CHAR", "STRING_LIT", 
                  "WS", "NEWLINE", "LINE_COMMENT", "BLOCK_COMMENT", "UNCLOSE_STRING", 
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
            actions[60] = self.INT_LIT_action 
            actions[64] = self.STRING_LIT_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            actions[71] = self.ERROR_CHAR_action 
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
     



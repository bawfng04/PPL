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
        buf.write("\u021e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\7\66\u015d\n\66\f\66\16\66\u0160")
        buf.write("\13\66\3\67\3\67\38\38\39\39\39\39\59\u016a\n9\39\69\u016d")
        buf.write("\n9\r9\169\u016e\3:\3:\3;\3;\3;\3;\5;\u0177\n;\3;\6;\u017a")
        buf.write("\n;\r;\16;\u017b\3<\3<\3<\7<\u0181\n<\f<\16<\u0184\13")
        buf.write("<\5<\u0186\n<\3=\3=\7=\u018a\n=\f=\16=\u018d\13=\3>\3")
        buf.write(">\3?\3?\3?\3?\5?\u0195\n?\3?\6?\u0198\n?\r?\16?\u0199")
        buf.write("\3@\3@\5@\u019e\n@\3@\6@\u01a1\n@\r@\16@\u01a2\3A\3A\3")
        buf.write("A\3A\3A\3A\3A\3A\3A\3A\5A\u01af\nA\3B\6B\u01b2\nB\rB\16")
        buf.write("B\u01b3\3B\3B\5B\u01b8\nB\3B\3B\5B\u01bc\nB\3B\6B\u01bf")
        buf.write("\nB\rB\16B\u01c0\3B\5B\u01c4\nB\3C\3C\3D\3D\3D\5D\u01cb")
        buf.write("\nD\3E\3E\7E\u01cf\nE\fE\16E\u01d2\13E\3E\3E\3E\3F\6F")
        buf.write("\u01d8\nF\rF\16F\u01d9\3F\3F\3G\5G\u01df\nG\3G\3G\3G\3")
        buf.write("G\3H\3H\3H\3H\7H\u01e9\nH\fH\16H\u01ec\13H\3H\3H\3I\3")
        buf.write("I\3I\3I\3I\7I\u01f5\nI\fI\16I\u01f8\13I\3I\3I\3I\3I\3")
        buf.write("I\3J\3J\7J\u0201\nJ\fJ\16J\u0204\13J\3J\5J\u0207\nJ\3")
        buf.write("J\3J\3K\3K\7K\u020d\nK\fK\16K\u0210\13K\3K\3K\3K\7K\u0215")
        buf.write("\nK\fK\16K\u0218\13K\3K\3K\3L\3L\3L\3\u01f6\2M\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q\2s\2u\2w\2")
        buf.write("y\2{\2}\2\177\2\u00818\u00839\u0085\2\u0087\2\u0089:\u008b")
        buf.write(";\u008d<\u008f=\u0091>\u0093?\u0095@\u0097A\3\2\20\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\629\5\2\62;CHch\3\2")
        buf.write("\63;\3\2\62\63\4\2GGgg\4\2--//\t\2$$))^^ddppttvv\6\2\f")
        buf.write("\f\17\17$$^^\5\2\13\f\16\17\"\"\4\2\f\f\17\17\4\3\f\f")
        buf.write("\17\17\2\u0230\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
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
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2\u0081\3\2")
        buf.write("\2\2\2\u0083\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2")
        buf.write("\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u0099\3\2\2")
        buf.write("\2\5\u009c\3\2\2\2\7\u00a1\3\2\2\2\t\u00a5\3\2\2\2\13")
        buf.write("\u00ac\3\2\2\2\r\u00b1\3\2\2\2\17\u00b6\3\2\2\2\21\u00bd")
        buf.write("\3\2\2\2\23\u00c7\3\2\2\2\25\u00ce\3\2\2\2\27\u00d2\3")
        buf.write("\2\2\2\31\u00d8\3\2\2\2\33\u00e0\3\2\2\2\35\u00e6\3\2")
        buf.write("\2\2\37\u00ea\3\2\2\2!\u00f3\3\2\2\2#\u00f9\3\2\2\2%\u00ff")
        buf.write("\3\2\2\2\'\u0103\3\2\2\2)\u0108\3\2\2\2+\u010e\3\2\2\2")
        buf.write("-\u0110\3\2\2\2/\u0112\3\2\2\2\61\u0114\3\2\2\2\63\u0116")
        buf.write("\3\2\2\2\65\u0118\3\2\2\2\67\u011b\3\2\2\29\u011e\3\2")
        buf.write("\2\2;\u0120\3\2\2\2=\u0123\3\2\2\2?\u0125\3\2\2\2A\u0128")
        buf.write("\3\2\2\2C\u012b\3\2\2\2E\u012e\3\2\2\2G\u0130\3\2\2\2")
        buf.write("I\u0132\3\2\2\2K\u0135\3\2\2\2M\u0138\3\2\2\2O\u013b\3")
        buf.write("\2\2\2Q\u013e\3\2\2\2S\u0141\3\2\2\2U\u0143\3\2\2\2W\u0145")
        buf.write("\3\2\2\2Y\u0148\3\2\2\2[\u014a\3\2\2\2]\u014c\3\2\2\2")
        buf.write("_\u014e\3\2\2\2a\u0150\3\2\2\2c\u0152\3\2\2\2e\u0154\3")
        buf.write("\2\2\2g\u0156\3\2\2\2i\u0158\3\2\2\2k\u015a\3\2\2\2m\u0161")
        buf.write("\3\2\2\2o\u0163\3\2\2\2q\u0169\3\2\2\2s\u0170\3\2\2\2")
        buf.write("u\u0176\3\2\2\2w\u0185\3\2\2\2y\u0187\3\2\2\2{\u018e\3")
        buf.write("\2\2\2}\u0194\3\2\2\2\177\u019b\3\2\2\2\u0081\u01ae\3")
        buf.write("\2\2\2\u0083\u01c3\3\2\2\2\u0085\u01c5\3\2\2\2\u0087\u01ca")
        buf.write("\3\2\2\2\u0089\u01cc\3\2\2\2\u008b\u01d7\3\2\2\2\u008d")
        buf.write("\u01de\3\2\2\2\u008f\u01e4\3\2\2\2\u0091\u01ef\3\2\2\2")
        buf.write("\u0093\u01fe\3\2\2\2\u0095\u020a\3\2\2\2\u0097\u021b\3")
        buf.write("\2\2\2\u0099\u009a\7k\2\2\u009a\u009b\7h\2\2\u009b\4\3")
        buf.write("\2\2\2\u009c\u009d\7g\2\2\u009d\u009e\7n\2\2\u009e\u009f")
        buf.write("\7u\2\2\u009f\u00a0\7g\2\2\u00a0\6\3\2\2\2\u00a1\u00a2")
        buf.write("\7h\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4\7t\2\2\u00a4\b")
        buf.write("\3\2\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8")
        buf.write("\7v\2\2\u00a8\u00a9\7w\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab")
        buf.write("\7p\2\2\u00ab\n\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae")
        buf.write("\7w\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7e\2\2\u00b0\f")
        buf.write("\3\2\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7{\2\2\u00b3\u00b4")
        buf.write("\7r\2\2\u00b4\u00b5\7g\2\2\u00b5\16\3\2\2\2\u00b6\u00b7")
        buf.write("\7u\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba")
        buf.write("\7w\2\2\u00ba\u00bb\7e\2\2\u00bb\u00bc\7v\2\2\u00bc\20")
        buf.write("\3\2\2\2\u00bd\u00be\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0")
        buf.write("\7v\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7h\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7e\2\2\u00c5\u00c6")
        buf.write("\7g\2\2\u00c6\22\3\2\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7i\2\2\u00cd\24\3\2\2\2\u00ce\u00cf")
        buf.write("\7k\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7v\2\2\u00d1\26")
        buf.write("\3\2\2\2\u00d2\u00d3\7h\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5")
        buf.write("\7q\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7v\2\2\u00d7\30")
        buf.write("\3\2\2\2\u00d8\u00d9\7d\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de")
        buf.write("\7c\2\2\u00de\u00df\7p\2\2\u00df\32\3\2\2\2\u00e0\u00e1")
        buf.write("\7e\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4")
        buf.write("\7u\2\2\u00e4\u00e5\7v\2\2\u00e5\34\3\2\2\2\u00e6\u00e7")
        buf.write("\7x\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9\7t\2\2\u00e9\36")
        buf.write("\3\2\2\2\u00ea\u00eb\7e\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed")
        buf.write("\7p\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7p\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2\7g\2\2\u00f2 \3")
        buf.write("\2\2\2\u00f3\u00f4\7d\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6")
        buf.write("\7g\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7m\2\2\u00f8\"")
        buf.write("\3\2\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7p\2\2\u00fc\u00fd\7i\2\2\u00fd\u00fe\7g\2\2\u00fe$\3")
        buf.write("\2\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7k\2\2\u0101\u0102")
        buf.write("\7n\2\2\u0102&\3\2\2\2\u0103\u0104\7v\2\2\u0104\u0105")
        buf.write("\7t\2\2\u0105\u0106\7w\2\2\u0106\u0107\7g\2\2\u0107(\3")
        buf.write("\2\2\2\u0108\u0109\7h\2\2\u0109\u010a\7c\2\2\u010a\u010b")
        buf.write("\7n\2\2\u010b\u010c\7u\2\2\u010c\u010d\7g\2\2\u010d*\3")
        buf.write("\2\2\2\u010e\u010f\7-\2\2\u010f,\3\2\2\2\u0110\u0111\7")
        buf.write("/\2\2\u0111.\3\2\2\2\u0112\u0113\7,\2\2\u0113\60\3\2\2")
        buf.write("\2\u0114\u0115\7\61\2\2\u0115\62\3\2\2\2\u0116\u0117\7")
        buf.write("\'\2\2\u0117\64\3\2\2\2\u0118\u0119\7?\2\2\u0119\u011a")
        buf.write("\7?\2\2\u011a\66\3\2\2\2\u011b\u011c\7#\2\2\u011c\u011d")
        buf.write("\7?\2\2\u011d8\3\2\2\2\u011e\u011f\7>\2\2\u011f:\3\2\2")
        buf.write("\2\u0120\u0121\7>\2\2\u0121\u0122\7?\2\2\u0122<\3\2\2")
        buf.write("\2\u0123\u0124\7@\2\2\u0124>\3\2\2\2\u0125\u0126\7@\2")
        buf.write("\2\u0126\u0127\7?\2\2\u0127@\3\2\2\2\u0128\u0129\7(\2")
        buf.write("\2\u0129\u012a\7(\2\2\u012aB\3\2\2\2\u012b\u012c\7~\2")
        buf.write("\2\u012c\u012d\7~\2\2\u012dD\3\2\2\2\u012e\u012f\7#\2")
        buf.write("\2\u012fF\3\2\2\2\u0130\u0131\7?\2\2\u0131H\3\2\2\2\u0132")
        buf.write("\u0133\7-\2\2\u0133\u0134\7?\2\2\u0134J\3\2\2\2\u0135")
        buf.write("\u0136\7/\2\2\u0136\u0137\7?\2\2\u0137L\3\2\2\2\u0138")
        buf.write("\u0139\7,\2\2\u0139\u013a\7?\2\2\u013aN\3\2\2\2\u013b")
        buf.write("\u013c\7\61\2\2\u013c\u013d\7?\2\2\u013dP\3\2\2\2\u013e")
        buf.write("\u013f\7\'\2\2\u013f\u0140\7?\2\2\u0140R\3\2\2\2\u0141")
        buf.write("\u0142\7\60\2\2\u0142T\3\2\2\2\u0143\u0144\7<\2\2\u0144")
        buf.write("V\3\2\2\2\u0145\u0146\7<\2\2\u0146\u0147\7?\2\2\u0147")
        buf.write("X\3\2\2\2\u0148\u0149\7a\2\2\u0149Z\3\2\2\2\u014a\u014b")
        buf.write("\7*\2\2\u014b\\\3\2\2\2\u014c\u014d\7+\2\2\u014d^\3\2")
        buf.write("\2\2\u014e\u014f\7}\2\2\u014f`\3\2\2\2\u0150\u0151\7\177")
        buf.write("\2\2\u0151b\3\2\2\2\u0152\u0153\7]\2\2\u0153d\3\2\2\2")
        buf.write("\u0154\u0155\7_\2\2\u0155f\3\2\2\2\u0156\u0157\7.\2\2")
        buf.write("\u0157h\3\2\2\2\u0158\u0159\7=\2\2\u0159j\3\2\2\2\u015a")
        buf.write("\u015e\t\2\2\2\u015b\u015d\t\3\2\2\u015c\u015b\3\2\2\2")
        buf.write("\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3")
        buf.write("\2\2\2\u015fl\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162")
        buf.write("\t\4\2\2\u0162n\3\2\2\2\u0163\u0164\t\5\2\2\u0164p\3\2")
        buf.write("\2\2\u0165\u0166\7\62\2\2\u0166\u016a\7q\2\2\u0167\u0168")
        buf.write("\7\62\2\2\u0168\u016a\7Q\2\2\u0169\u0165\3\2\2\2\u0169")
        buf.write("\u0167\3\2\2\2\u016a\u016c\3\2\2\2\u016b\u016d\t\5\2\2")
        buf.write("\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016c\3")
        buf.write("\2\2\2\u016e\u016f\3\2\2\2\u016fr\3\2\2\2\u0170\u0171")
        buf.write("\t\6\2\2\u0171t\3\2\2\2\u0172\u0173\7\62\2\2\u0173\u0177")
        buf.write("\7z\2\2\u0174\u0175\7\62\2\2\u0175\u0177\7Z\2\2\u0176")
        buf.write("\u0172\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0179\3\2\2\2")
        buf.write("\u0178\u017a\t\6\2\2\u0179\u0178\3\2\2\2\u017a\u017b\3")
        buf.write("\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017cv")
        buf.write("\3\2\2\2\u017d\u0186\7\62\2\2\u017e\u0182\t\7\2\2\u017f")
        buf.write("\u0181\t\4\2\2\u0180\u017f\3\2\2\2\u0181\u0184\3\2\2\2")
        buf.write("\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0186\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0185\u017d\3\2\2\2\u0185\u017e")
        buf.write("\3\2\2\2\u0186x\3\2\2\2\u0187\u018b\7\60\2\2\u0188\u018a")
        buf.write("\t\4\2\2\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018cz\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018e\u018f\t\b\2\2\u018f|\3\2\2\2\u0190")
        buf.write("\u0191\7\62\2\2\u0191\u0195\7d\2\2\u0192\u0193\7\62\2")
        buf.write("\2\u0193\u0195\7D\2\2\u0194\u0190\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0195\u0197\3\2\2\2\u0196\u0198\t\b\2\2\u0197")
        buf.write("\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u0197\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019a~\3\2\2\2\u019b\u019d\t\t\2")
        buf.write("\2\u019c\u019e\t\n\2\2\u019d\u019c\3\2\2\2\u019d\u019e")
        buf.write("\3\2\2\2\u019e\u01a0\3\2\2\2\u019f\u01a1\t\4\2\2\u01a0")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2")
        buf.write("\u01a2\u01a3\3\2\2\2\u01a3\u0080\3\2\2\2\u01a4\u01af\5")
        buf.write("w<\2\u01a5\u01a6\5u;\2\u01a6\u01a7\bA\2\2\u01a7\u01af")
        buf.write("\3\2\2\2\u01a8\u01a9\5q9\2\u01a9\u01aa\bA\3\2\u01aa\u01af")
        buf.write("\3\2\2\2\u01ab\u01ac\5}?\2\u01ac\u01ad\bA\4\2\u01ad\u01af")
        buf.write("\3\2\2\2\u01ae\u01a4\3\2\2\2\u01ae\u01a5\3\2\2\2\u01ae")
        buf.write("\u01a8\3\2\2\2\u01ae\u01ab\3\2\2\2\u01af\u0082\3\2\2\2")
        buf.write("\u01b0\u01b2\t\4\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b3\3")
        buf.write("\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5")
        buf.write("\3\2\2\2\u01b5\u01b7\5y=\2\u01b6\u01b8\5\177@\2\u01b7")
        buf.write("\u01b6\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01c4\3\2\2\2")
        buf.write("\u01b9\u01bb\5y=\2\u01ba\u01bc\5\177@\2\u01bb\u01ba\3")
        buf.write("\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01c4\3\2\2\2\u01bd\u01bf")
        buf.write("\t\4\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\3\2\2\2")
        buf.write("\u01c2\u01c4\5\177@\2\u01c3\u01b1\3\2\2\2\u01c3\u01b9")
        buf.write("\3\2\2\2\u01c3\u01be\3\2\2\2\u01c4\u0084\3\2\2\2\u01c5")
        buf.write("\u01c6\t\13\2\2\u01c6\u0086\3\2\2\2\u01c7\u01cb\n\f\2")
        buf.write("\2\u01c8\u01c9\7^\2\2\u01c9\u01cb\5\u0085C\2\u01ca\u01c7")
        buf.write("\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u0088\3\2\2\2\u01cc")
        buf.write("\u01d0\7$\2\2\u01cd\u01cf\5\u0087D\2\u01ce\u01cd\3\2\2")
        buf.write("\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1")
        buf.write("\3\2\2\2\u01d1\u01d3\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3")
        buf.write("\u01d4\7$\2\2\u01d4\u01d5\bE\5\2\u01d5\u008a\3\2\2\2\u01d6")
        buf.write("\u01d8\t\r\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2")
        buf.write("\u01d9\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01db\3")
        buf.write("\2\2\2\u01db\u01dc\bF\6\2\u01dc\u008c\3\2\2\2\u01dd\u01df")
        buf.write("\7\17\2\2\u01de\u01dd\3\2\2\2\u01de\u01df\3\2\2\2\u01df")
        buf.write("\u01e0\3\2\2\2\u01e0\u01e1\7\f\2\2\u01e1\u01e2\3\2\2\2")
        buf.write("\u01e2\u01e3\bG\6\2\u01e3\u008e\3\2\2\2\u01e4\u01e5\7")
        buf.write("\61\2\2\u01e5\u01e6\7\61\2\2\u01e6\u01ea\3\2\2\2\u01e7")
        buf.write("\u01e9\n\16\2\2\u01e8\u01e7\3\2\2\2\u01e9\u01ec\3\2\2")
        buf.write("\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ed")
        buf.write("\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01ee\bH\6\2\u01ee")
        buf.write("\u0090\3\2\2\2\u01ef\u01f0\7\61\2\2\u01f0\u01f1\7,\2\2")
        buf.write("\u01f1\u01f6\3\2\2\2\u01f2\u01f5\5\u0091I\2\u01f3\u01f5")
        buf.write("\13\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f3\3\2\2\2\u01f5")
        buf.write("\u01f8\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f6\u01f4\3\2\2\2")
        buf.write("\u01f7\u01f9\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u01fa\7")
        buf.write(",\2\2\u01fa\u01fb\7\61\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd")
        buf.write("\bI\6\2\u01fd\u0092\3\2\2\2\u01fe\u0202\7$\2\2\u01ff\u0201")
        buf.write("\5\u0087D\2\u0200\u01ff\3\2\2\2\u0201\u0204\3\2\2\2\u0202")
        buf.write("\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0206\3\2\2\2")
        buf.write("\u0204\u0202\3\2\2\2\u0205\u0207\t\17\2\2\u0206\u0205")
        buf.write("\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0209\bJ\7\2\u0209")
        buf.write("\u0094\3\2\2\2\u020a\u020e\7$\2\2\u020b\u020d\5\u0087")
        buf.write("D\2\u020c\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e\u020c")
        buf.write("\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0211\3\2\2\2\u0210")
        buf.write("\u020e\3\2\2\2\u0211\u0212\7^\2\2\u0212\u0216\n\13\2\2")
        buf.write("\u0213\u0215\5\u0087D\2\u0214\u0213\3\2\2\2\u0215\u0218")
        buf.write("\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0217\3\2\2\2\u0217")
        buf.write("\u0219\3\2\2\2\u0218\u0216\3\2\2\2\u0219\u021a\bK\b\2")
        buf.write("\u021a\u0096\3\2\2\2\u021b\u021c\13\2\2\2\u021c\u021d")
        buf.write("\bL\t\2\u021d\u0098\3\2\2\2 \2\u015e\u0169\u016e\u0176")
        buf.write("\u017b\u0182\u0185\u018b\u0194\u0199\u019d\u01a2\u01ae")
        buf.write("\u01b3\u01b7\u01bb\u01c0\u01c3\u01ca\u01d0\u01d9\u01de")
        buf.write("\u01ea\u01f4\u01f6\u0202\u0206\u020e\u0216\n\3A\2\3A\3")
        buf.write("\3A\4\3E\5\b\2\2\3J\6\3K\7\3L\b")
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
    WS = 57
    NEWLINE = 58
    LINE_COMMENT = 59
    BLOCK_COMMENT = 60
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
            "STRING_LIT", "WS", "NEWLINE", "LINE_COMMENT", "BLOCK_COMMENT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
                  "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
                  "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", 
                  "SHORT_ASSIGN", "UNDERSCORE", "LP", "RP", "LB", "RB", 
                  "LSB", "RSB", "COMMA", "SEMI", "ID", "DIGIT", "OCTAL_DIGIT", 
                  "OCTAL", "HEX_DIGIT", "HEX", "DECIMAL", "DECIMAL_PART", 
                  "BINARY_DIGIT", "BINARY", "EXPONENT", "INT_LIT", "FLOAT_LIT", 
                  "ESC_CHAR", "STR_CHAR", "STRING_LIT", "WS", "NEWLINE", 
                  "LINE_COMMENT", "BLOCK_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

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
            actions[63] = self.INT_LIT_action 
            actions[67] = self.STRING_LIT_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.ERROR_CHAR_action 
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
     



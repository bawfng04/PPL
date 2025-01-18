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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0227\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#")
        buf.write("\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\3*\3+\3+\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\7\67\u0166\n\67\f\67\16\67\u0169\13\67")
        buf.write("\38\38\39\39\3:\3:\3:\3:\5:\u0173\n:\3:\6:\u0176\n:\r")
        buf.write(":\16:\u0177\3;\3;\3<\3<\3<\3<\5<\u0180\n<\3<\6<\u0183")
        buf.write("\n<\r<\16<\u0184\3=\3=\3=\7=\u018a\n=\f=\16=\u018d\13")
        buf.write("=\5=\u018f\n=\3>\3>\7>\u0193\n>\f>\16>\u0196\13>\3?\3")
        buf.write("?\3@\3@\3@\3@\5@\u019e\n@\3@\6@\u01a1\n@\r@\16@\u01a2")
        buf.write("\3A\3A\5A\u01a7\nA\3A\6A\u01aa\nA\rA\16A\u01ab\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\3B\5B\u01b8\nB\3C\6C\u01bb\nC\rC\16")
        buf.write("C\u01bc\3C\3C\5C\u01c1\nC\3C\3C\5C\u01c5\nC\3C\6C\u01c8")
        buf.write("\nC\rC\16C\u01c9\3C\5C\u01cd\nC\3D\3D\3E\3E\3E\5E\u01d4")
        buf.write("\nE\3F\3F\7F\u01d8\nF\fF\16F\u01db\13F\3F\3F\3F\3G\6G")
        buf.write("\u01e1\nG\rG\16G\u01e2\3G\3G\3H\5H\u01e8\nH\3H\3H\3H\3")
        buf.write("H\3I\3I\3I\3I\7I\u01f2\nI\fI\16I\u01f5\13I\3I\3I\3J\3")
        buf.write("J\3J\3J\3J\7J\u01fe\nJ\fJ\16J\u0201\13J\3J\3J\3J\3J\3")
        buf.write("J\3K\3K\7K\u020a\nK\fK\16K\u020d\13K\3K\5K\u0210\nK\3")
        buf.write("K\3K\3L\3L\7L\u0216\nL\fL\16L\u0219\13L\3L\3L\3L\7L\u021e")
        buf.write("\nL\fL\16L\u0221\13L\3L\3L\3M\3M\3M\3\u01ff\2N\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o\2q\2s\2u\2w\2")
        buf.write("y\2{\2}\2\177\2\u0081\2\u00839\u0085:\u0087\2\u0089\2")
        buf.write("\u008b;\u008d<\u008f=\u0091>\u0093?\u0095@\u0097A\u0099")
        buf.write("B\3\2\20\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\629\5\2")
        buf.write("\62;CHch\3\2\63;\3\2\62\63\4\2GGgg\4\2--//\t\2$$))^^d")
        buf.write("dppttvv\6\2\f\f\17\17$$^^\5\2\13\f\16\17\"\"\4\2\f\f\17")
        buf.write("\17\4\3\f\f\17\17\2\u0239\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u008b\3")
        buf.write("\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2")
        buf.write("\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\3\u009b\3\2\2\2\5\u00a2\3\2\2\2\7\u00a5\3\2\2")
        buf.write("\2\t\u00aa\3\2\2\2\13\u00ae\3\2\2\2\r\u00b5\3\2\2\2\17")
        buf.write("\u00ba\3\2\2\2\21\u00bf\3\2\2\2\23\u00c6\3\2\2\2\25\u00d0")
        buf.write("\3\2\2\2\27\u00d7\3\2\2\2\31\u00db\3\2\2\2\33\u00e1\3")
        buf.write("\2\2\2\35\u00e9\3\2\2\2\37\u00ef\3\2\2\2!\u00f3\3\2\2")
        buf.write("\2#\u00fc\3\2\2\2%\u0102\3\2\2\2\'\u0108\3\2\2\2)\u010c")
        buf.write("\3\2\2\2+\u0111\3\2\2\2-\u0117\3\2\2\2/\u0119\3\2\2\2")
        buf.write("\61\u011b\3\2\2\2\63\u011d\3\2\2\2\65\u011f\3\2\2\2\67")
        buf.write("\u0121\3\2\2\29\u0124\3\2\2\2;\u0127\3\2\2\2=\u0129\3")
        buf.write("\2\2\2?\u012c\3\2\2\2A\u012e\3\2\2\2C\u0131\3\2\2\2E\u0134")
        buf.write("\3\2\2\2G\u0137\3\2\2\2I\u0139\3\2\2\2K\u013b\3\2\2\2")
        buf.write("M\u013e\3\2\2\2O\u0141\3\2\2\2Q\u0144\3\2\2\2S\u0147\3")
        buf.write("\2\2\2U\u014a\3\2\2\2W\u014c\3\2\2\2Y\u014e\3\2\2\2[\u0151")
        buf.write("\3\2\2\2]\u0153\3\2\2\2_\u0155\3\2\2\2a\u0157\3\2\2\2")
        buf.write("c\u0159\3\2\2\2e\u015b\3\2\2\2g\u015d\3\2\2\2i\u015f\3")
        buf.write("\2\2\2k\u0161\3\2\2\2m\u0163\3\2\2\2o\u016a\3\2\2\2q\u016c")
        buf.write("\3\2\2\2s\u0172\3\2\2\2u\u0179\3\2\2\2w\u017f\3\2\2\2")
        buf.write("y\u018e\3\2\2\2{\u0190\3\2\2\2}\u0197\3\2\2\2\177\u019d")
        buf.write("\3\2\2\2\u0081\u01a4\3\2\2\2\u0083\u01b7\3\2\2\2\u0085")
        buf.write("\u01cc\3\2\2\2\u0087\u01ce\3\2\2\2\u0089\u01d3\3\2\2\2")
        buf.write("\u008b\u01d5\3\2\2\2\u008d\u01e0\3\2\2\2\u008f\u01e7\3")
        buf.write("\2\2\2\u0091\u01ed\3\2\2\2\u0093\u01f8\3\2\2\2\u0095\u0207")
        buf.write("\3\2\2\2\u0097\u0213\3\2\2\2\u0099\u0224\3\2\2\2\u009b")
        buf.write("\u009c\7x\2\2\u009c\u009d\7q\2\2\u009d\u009e\7v\2\2\u009e")
        buf.write("\u009f\7k\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7p\2\2\u00a1")
        buf.write("\4\3\2\2\2\u00a2\u00a3\7k\2\2\u00a3\u00a4\7h\2\2\u00a4")
        buf.write("\6\3\2\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7\7n\2\2\u00a7")
        buf.write("\u00a8\7u\2\2\u00a8\u00a9\7g\2\2\u00a9\b\3\2\2\2\u00aa")
        buf.write("\u00ab\7h\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad\7t\2\2\u00ad")
        buf.write("\n\3\2\2\2\u00ae\u00af\7t\2\2\u00af\u00b0\7g\2\2\u00b0")
        buf.write("\u00b1\7v\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3\7t\2\2\u00b3")
        buf.write("\u00b4\7p\2\2\u00b4\f\3\2\2\2\u00b5\u00b6\7h\2\2\u00b6")
        buf.write("\u00b7\7w\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7e\2\2\u00b9")
        buf.write("\16\3\2\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7{\2\2\u00bc")
        buf.write("\u00bd\7r\2\2\u00bd\u00be\7g\2\2\u00be\20\3\2\2\2\u00bf")
        buf.write("\u00c0\7u\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7t\2\2\u00c2")
        buf.write("\u00c3\7w\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5\7v\2\2\u00c5")
        buf.write("\22\3\2\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8")
        buf.write("\u00c9\7v\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb\7t\2\2\u00cb")
        buf.write("\u00cc\7h\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7e\2\2\u00ce")
        buf.write("\u00cf\7g\2\2\u00cf\24\3\2\2\2\u00d0\u00d1\7u\2\2\u00d1")
        buf.write("\u00d2\7v\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7k\2\2\u00d4")
        buf.write("\u00d5\7p\2\2\u00d5\u00d6\7i\2\2\u00d6\26\3\2\2\2\u00d7")
        buf.write("\u00d8\7k\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da\7v\2\2\u00da")
        buf.write("\30\3\2\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd\7n\2\2\u00dd")
        buf.write("\u00de\7q\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7v\2\2\u00e0")
        buf.write("\32\3\2\2\2\u00e1\u00e2\7d\2\2\u00e2\u00e3\7q\2\2\u00e3")
        buf.write("\u00e4\7q\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6\7g\2\2\u00e6")
        buf.write("\u00e7\7c\2\2\u00e7\u00e8\7p\2\2\u00e8\34\3\2\2\2\u00e9")
        buf.write("\u00ea\7e\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec\7p\2\2\u00ec")
        buf.write("\u00ed\7u\2\2\u00ed\u00ee\7v\2\2\u00ee\36\3\2\2\2\u00ef")
        buf.write("\u00f0\7x\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7t\2\2\u00f2")
        buf.write(" \3\2\2\2\u00f3\u00f4\7e\2\2\u00f4\u00f5\7q\2\2\u00f5")
        buf.write("\u00f6\7p\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8\7k\2\2\u00f8")
        buf.write("\u00f9\7p\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb\7g\2\2\u00fb")
        buf.write("\"\3\2\2\2\u00fc\u00fd\7d\2\2\u00fd\u00fe\7t\2\2\u00fe")
        buf.write("\u00ff\7g\2\2\u00ff\u0100\7c\2\2\u0100\u0101\7m\2\2\u0101")
        buf.write("$\3\2\2\2\u0102\u0103\7t\2\2\u0103\u0104\7c\2\2\u0104")
        buf.write("\u0105\7p\2\2\u0105\u0106\7i\2\2\u0106\u0107\7g\2\2\u0107")
        buf.write("&\3\2\2\2\u0108\u0109\7p\2\2\u0109\u010a\7k\2\2\u010a")
        buf.write("\u010b\7n\2\2\u010b(\3\2\2\2\u010c\u010d\7v\2\2\u010d")
        buf.write("\u010e\7t\2\2\u010e\u010f\7w\2\2\u010f\u0110\7g\2\2\u0110")
        buf.write("*\3\2\2\2\u0111\u0112\7h\2\2\u0112\u0113\7c\2\2\u0113")
        buf.write("\u0114\7n\2\2\u0114\u0115\7u\2\2\u0115\u0116\7g\2\2\u0116")
        buf.write(",\3\2\2\2\u0117\u0118\7-\2\2\u0118.\3\2\2\2\u0119\u011a")
        buf.write("\7/\2\2\u011a\60\3\2\2\2\u011b\u011c\7,\2\2\u011c\62\3")
        buf.write("\2\2\2\u011d\u011e\7\61\2\2\u011e\64\3\2\2\2\u011f\u0120")
        buf.write("\7\'\2\2\u0120\66\3\2\2\2\u0121\u0122\7?\2\2\u0122\u0123")
        buf.write("\7?\2\2\u01238\3\2\2\2\u0124\u0125\7#\2\2\u0125\u0126")
        buf.write("\7?\2\2\u0126:\3\2\2\2\u0127\u0128\7>\2\2\u0128<\3\2\2")
        buf.write("\2\u0129\u012a\7>\2\2\u012a\u012b\7?\2\2\u012b>\3\2\2")
        buf.write("\2\u012c\u012d\7@\2\2\u012d@\3\2\2\2\u012e\u012f\7@\2")
        buf.write("\2\u012f\u0130\7?\2\2\u0130B\3\2\2\2\u0131\u0132\7(\2")
        buf.write("\2\u0132\u0133\7(\2\2\u0133D\3\2\2\2\u0134\u0135\7~\2")
        buf.write("\2\u0135\u0136\7~\2\2\u0136F\3\2\2\2\u0137\u0138\7#\2")
        buf.write("\2\u0138H\3\2\2\2\u0139\u013a\7?\2\2\u013aJ\3\2\2\2\u013b")
        buf.write("\u013c\7-\2\2\u013c\u013d\7?\2\2\u013dL\3\2\2\2\u013e")
        buf.write("\u013f\7/\2\2\u013f\u0140\7?\2\2\u0140N\3\2\2\2\u0141")
        buf.write("\u0142\7,\2\2\u0142\u0143\7?\2\2\u0143P\3\2\2\2\u0144")
        buf.write("\u0145\7\61\2\2\u0145\u0146\7?\2\2\u0146R\3\2\2\2\u0147")
        buf.write("\u0148\7\'\2\2\u0148\u0149\7?\2\2\u0149T\3\2\2\2\u014a")
        buf.write("\u014b\7\60\2\2\u014bV\3\2\2\2\u014c\u014d\7<\2\2\u014d")
        buf.write("X\3\2\2\2\u014e\u014f\7<\2\2\u014f\u0150\7?\2\2\u0150")
        buf.write("Z\3\2\2\2\u0151\u0152\7a\2\2\u0152\\\3\2\2\2\u0153\u0154")
        buf.write("\7*\2\2\u0154^\3\2\2\2\u0155\u0156\7+\2\2\u0156`\3\2\2")
        buf.write("\2\u0157\u0158\7}\2\2\u0158b\3\2\2\2\u0159\u015a\7\177")
        buf.write("\2\2\u015ad\3\2\2\2\u015b\u015c\7]\2\2\u015cf\3\2\2\2")
        buf.write("\u015d\u015e\7_\2\2\u015eh\3\2\2\2\u015f\u0160\7.\2\2")
        buf.write("\u0160j\3\2\2\2\u0161\u0162\7=\2\2\u0162l\3\2\2\2\u0163")
        buf.write("\u0167\t\2\2\2\u0164\u0166\t\3\2\2\u0165\u0164\3\2\2\2")
        buf.write("\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3")
        buf.write("\2\2\2\u0168n\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016b")
        buf.write("\t\4\2\2\u016bp\3\2\2\2\u016c\u016d\t\5\2\2\u016dr\3\2")
        buf.write("\2\2\u016e\u016f\7\62\2\2\u016f\u0173\7q\2\2\u0170\u0171")
        buf.write("\7\62\2\2\u0171\u0173\7Q\2\2\u0172\u016e\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0173\u0175\3\2\2\2\u0174\u0176\t\5\2\2")
        buf.write("\u0175\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0175\3")
        buf.write("\2\2\2\u0177\u0178\3\2\2\2\u0178t\3\2\2\2\u0179\u017a")
        buf.write("\t\6\2\2\u017av\3\2\2\2\u017b\u017c\7\62\2\2\u017c\u0180")
        buf.write("\7z\2\2\u017d\u017e\7\62\2\2\u017e\u0180\7Z\2\2\u017f")
        buf.write("\u017b\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0182\3\2\2\2")
        buf.write("\u0181\u0183\t\6\2\2\u0182\u0181\3\2\2\2\u0183\u0184\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185x")
        buf.write("\3\2\2\2\u0186\u018f\7\62\2\2\u0187\u018b\t\7\2\2\u0188")
        buf.write("\u018a\t\4\2\2\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2")
        buf.write("\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018f\3")
        buf.write("\2\2\2\u018d\u018b\3\2\2\2\u018e\u0186\3\2\2\2\u018e\u0187")
        buf.write("\3\2\2\2\u018fz\3\2\2\2\u0190\u0194\7\60\2\2\u0191\u0193")
        buf.write("\t\4\2\2\u0192\u0191\3\2\2\2\u0193\u0196\3\2\2\2\u0194")
        buf.write("\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195|\3\2\2\2\u0196")
        buf.write("\u0194\3\2\2\2\u0197\u0198\t\b\2\2\u0198~\3\2\2\2\u0199")
        buf.write("\u019a\7\62\2\2\u019a\u019e\7d\2\2\u019b\u019c\7\62\2")
        buf.write("\2\u019c\u019e\7D\2\2\u019d\u0199\3\2\2\2\u019d\u019b")
        buf.write("\3\2\2\2\u019e\u01a0\3\2\2\2\u019f\u01a1\t\b\2\2\u01a0")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2")
        buf.write("\u01a2\u01a3\3\2\2\2\u01a3\u0080\3\2\2\2\u01a4\u01a6\t")
        buf.write("\t\2\2\u01a5\u01a7\t\n\2\2\u01a6\u01a5\3\2\2\2\u01a6\u01a7")
        buf.write("\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8\u01aa\t\4\2\2\u01a9")
        buf.write("\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01a9\3\2\2\2")
        buf.write("\u01ab\u01ac\3\2\2\2\u01ac\u0082\3\2\2\2\u01ad\u01b8\5")
        buf.write("y=\2\u01ae\u01af\5w<\2\u01af\u01b0\bB\2\2\u01b0\u01b8")
        buf.write("\3\2\2\2\u01b1\u01b2\5s:\2\u01b2\u01b3\bB\3\2\u01b3\u01b8")
        buf.write("\3\2\2\2\u01b4\u01b5\5\177@\2\u01b5\u01b6\bB\4\2\u01b6")
        buf.write("\u01b8\3\2\2\2\u01b7\u01ad\3\2\2\2\u01b7\u01ae\3\2\2\2")
        buf.write("\u01b7\u01b1\3\2\2\2\u01b7\u01b4\3\2\2\2\u01b8\u0084\3")
        buf.write("\2\2\2\u01b9\u01bb\t\4\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01bc")
        buf.write("\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd")
        buf.write("\u01be\3\2\2\2\u01be\u01c0\5{>\2\u01bf\u01c1\5\u0081A")
        buf.write("\2\u01c0\u01bf\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01cd")
        buf.write("\3\2\2\2\u01c2\u01c4\5{>\2\u01c3\u01c5\5\u0081A\2\u01c4")
        buf.write("\u01c3\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01cd\3\2\2\2")
        buf.write("\u01c6\u01c8\t\4\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01c9\3")
        buf.write("\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb")
        buf.write("\3\2\2\2\u01cb\u01cd\5\u0081A\2\u01cc\u01ba\3\2\2\2\u01cc")
        buf.write("\u01c2\3\2\2\2\u01cc\u01c7\3\2\2\2\u01cd\u0086\3\2\2\2")
        buf.write("\u01ce\u01cf\t\13\2\2\u01cf\u0088\3\2\2\2\u01d0\u01d4")
        buf.write("\n\f\2\2\u01d1\u01d2\7^\2\2\u01d2\u01d4\5\u0087D\2\u01d3")
        buf.write("\u01d0\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u008a\3\2\2\2")
        buf.write("\u01d5\u01d9\7$\2\2\u01d6\u01d8\5\u0089E\2\u01d7\u01d6")
        buf.write("\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9")
        buf.write("\u01da\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01d9\3\2\2\2")
        buf.write("\u01dc\u01dd\7$\2\2\u01dd\u01de\bF\5\2\u01de\u008c\3\2")
        buf.write("\2\2\u01df\u01e1\t\r\2\2\u01e0\u01df\3\2\2\2\u01e1\u01e2")
        buf.write("\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3")
        buf.write("\u01e4\3\2\2\2\u01e4\u01e5\bG\6\2\u01e5\u008e\3\2\2\2")
        buf.write("\u01e6\u01e8\7\17\2\2\u01e7\u01e6\3\2\2\2\u01e7\u01e8")
        buf.write("\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ea\7\f\2\2\u01ea")
        buf.write("\u01eb\3\2\2\2\u01eb\u01ec\bH\6\2\u01ec\u0090\3\2\2\2")
        buf.write("\u01ed\u01ee\7\61\2\2\u01ee\u01ef\7\61\2\2\u01ef\u01f3")
        buf.write("\3\2\2\2\u01f0\u01f2\n\16\2\2\u01f1\u01f0\3\2\2\2\u01f2")
        buf.write("\u01f5\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2")
        buf.write("\u01f4\u01f6\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f6\u01f7\b")
        buf.write("I\6\2\u01f7\u0092\3\2\2\2\u01f8\u01f9\7\61\2\2\u01f9\u01fa")
        buf.write("\7,\2\2\u01fa\u01ff\3\2\2\2\u01fb\u01fe\5\u0093J\2\u01fc")
        buf.write("\u01fe\13\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fc\3\2\2")
        buf.write("\2\u01fe\u0201\3\2\2\2\u01ff\u0200\3\2\2\2\u01ff\u01fd")
        buf.write("\3\2\2\2\u0200\u0202\3\2\2\2\u0201\u01ff\3\2\2\2\u0202")
        buf.write("\u0203\7,\2\2\u0203\u0204\7\61\2\2\u0204\u0205\3\2\2\2")
        buf.write("\u0205\u0206\bJ\6\2\u0206\u0094\3\2\2\2\u0207\u020b\7")
        buf.write("$\2\2\u0208\u020a\5\u0089E\2\u0209\u0208\3\2\2\2\u020a")
        buf.write("\u020d\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020c\3\2\2\2")
        buf.write("\u020c\u020f\3\2\2\2\u020d\u020b\3\2\2\2\u020e\u0210\t")
        buf.write("\17\2\2\u020f\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("\u0212\bK\7\2\u0212\u0096\3\2\2\2\u0213\u0217\7$\2\2\u0214")
        buf.write("\u0216\5\u0089E\2\u0215\u0214\3\2\2\2\u0216\u0219\3\2")
        buf.write("\2\2\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u021a")
        buf.write("\3\2\2\2\u0219\u0217\3\2\2\2\u021a\u021b\7^\2\2\u021b")
        buf.write("\u021f\n\13\2\2\u021c\u021e\5\u0089E\2\u021d\u021c\3\2")
        buf.write("\2\2\u021e\u0221\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220")
        buf.write("\3\2\2\2\u0220\u0222\3\2\2\2\u0221\u021f\3\2\2\2\u0222")
        buf.write("\u0223\bL\b\2\u0223\u0098\3\2\2\2\u0224\u0225\13\2\2\2")
        buf.write("\u0225\u0226\bM\t\2\u0226\u009a\3\2\2\2 \2\u0167\u0172")
        buf.write("\u0177\u017f\u0184\u018b\u018e\u0194\u019d\u01a2\u01a6")
        buf.write("\u01ab\u01b7\u01bc\u01c0\u01c4\u01c9\u01cc\u01d3\u01d9")
        buf.write("\u01e2\u01e7\u01f3\u01fd\u01ff\u020b\u020f\u0217\u021f")
        buf.write("\n\3B\2\3B\3\3B\4\3F\5\b\2\2\3K\6\3L\7\3M\b")
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
    COLON = 43
    SHORT_ASSIGN = 44
    UNDERSCORE = 45
    LP = 46
    RP = 47
    LB = 48
    RB = 49
    LSB = 50
    RSB = 51
    COMMA = 52
    SEMI = 53
    ID = 54
    INT_LIT = 55
    FLOAT_LIT = 56
    STRING_LIT = 57
    WS = 58
    NEWLINE = 59
    LINE_COMMENT = 60
    BLOCK_COMMENT = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'votien'", "'if'", "'else'", "'for'", "'return'", "'func'", 
            "'type'", "'struct'", "'interface'", "'string'", "'int'", "'float'", 
            "'boolean'", "'const'", "'var'", "'continue'", "'break'", "'range'", 
            "'nil'", "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
            "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "':'", "':='", "'_'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "','", "';'" ]

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

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
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
            actions[64] = self.INT_LIT_action 
            actions[68] = self.STRING_LIT_action 
            actions[73] = self.UNCLOSE_STRING_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
            actions[75] = self.ERROR_CHAR_action 
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
     



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
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(")
        buf.write("\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\7\64\u0154\n")
        buf.write("\64\f\64\16\64\u0157\13\64\3\65\3\65\3\66\3\66\3\67\3")
        buf.write("\67\3\67\3\67\5\67\u0161\n\67\3\67\6\67\u0164\n\67\r\67")
        buf.write("\16\67\u0165\38\38\39\39\39\39\59\u016e\n9\39\69\u0171")
        buf.write("\n9\r9\169\u0172\3:\3:\3:\7:\u0178\n:\f:\16:\u017b\13")
        buf.write(":\5:\u017d\n:\3;\3;\7;\u0181\n;\f;\16;\u0184\13;\3<\3")
        buf.write("<\3=\3=\3=\3=\5=\u018c\n=\3=\6=\u018f\n=\r=\16=\u0190")
        buf.write("\3>\3>\5>\u0195\n>\3>\6>\u0198\n>\r>\16>\u0199\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\3?\3?\3?\5?\u01a6\n?\3@\6@\u01a9\n@\r@\16")
        buf.write("@\u01aa\3@\3@\5@\u01af\n@\3@\3@\5@\u01b3\n@\3@\6@\u01b6")
        buf.write("\n@\r@\16@\u01b7\3@\5@\u01bb\n@\3A\3A\3B\3B\3B\5B\u01c2")
        buf.write("\nB\3C\3C\7C\u01c6\nC\fC\16C\u01c9\13C\3C\3C\3C\3D\6D")
        buf.write("\u01cf\nD\rD\16D\u01d0\3D\3D\3E\5E\u01d6\nE\3E\3E\3E\3")
        buf.write("E\3F\3F\3F\3F\7F\u01e0\nF\fF\16F\u01e3\13F\3F\3F\3G\3")
        buf.write("G\3G\3G\3G\7G\u01ec\nG\fG\16G\u01ef\13G\3G\3G\3G\3G\3")
        buf.write("G\3H\3H\7H\u01f8\nH\fH\16H\u01fb\13H\3H\5H\u01fe\nH\3")
        buf.write("H\3H\3I\3I\7I\u0204\nI\fI\16I\u0207\13I\3I\3I\3I\7I\u020c")
        buf.write("\nI\fI\16I\u020f\13I\3I\3I\3J\3J\3J\3\u01ed\2K\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\2k\2m\2o\2q\2s\2u\2w\2y")
        buf.write("\2{\2}\66\177\67\u0081\2\u0083\2\u00858\u00879\u0089:")
        buf.write("\u008b;\u008d<\u008f=\u0091>\u0093?\3\2\20\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\3\2\62;\3\2\629\5\2\62;CHch\3\2\63;\3")
        buf.write("\2\62\63\4\2GGgg\4\2--//\t\2$$))^^ddppttvv\6\2\f\f\17")
        buf.write("\17$$^^\5\2\13\f\16\17\"\"\4\2\f\f\17\17\4\3\f\f\17\17")
        buf.write("\2\u0227\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
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
        buf.write("\2\2\2\2g\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0085\3\2")
        buf.write("\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2")
        buf.write("\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\3\u0095\3\2\2\2\5\u0098\3\2\2\2\7\u009d\3\2\2")
        buf.write("\2\t\u00a1\3\2\2\2\13\u00a8\3\2\2\2\r\u00ad\3\2\2\2\17")
        buf.write("\u00b2\3\2\2\2\21\u00b9\3\2\2\2\23\u00c3\3\2\2\2\25\u00ca")
        buf.write("\3\2\2\2\27\u00ce\3\2\2\2\31\u00d4\3\2\2\2\33\u00dc\3")
        buf.write("\2\2\2\35\u00e2\3\2\2\2\37\u00e6\3\2\2\2!\u00ef\3\2\2")
        buf.write("\2#\u00f5\3\2\2\2%\u00fb\3\2\2\2\'\u00ff\3\2\2\2)\u0104")
        buf.write("\3\2\2\2+\u010a\3\2\2\2-\u010c\3\2\2\2/\u010e\3\2\2\2")
        buf.write("\61\u0110\3\2\2\2\63\u0112\3\2\2\2\65\u0114\3\2\2\2\67")
        buf.write("\u0117\3\2\2\29\u011a\3\2\2\2;\u011c\3\2\2\2=\u011f\3")
        buf.write("\2\2\2?\u0121\3\2\2\2A\u0124\3\2\2\2C\u0127\3\2\2\2E\u012a")
        buf.write("\3\2\2\2G\u012c\3\2\2\2I\u012e\3\2\2\2K\u0131\3\2\2\2")
        buf.write("M\u0134\3\2\2\2O\u0137\3\2\2\2Q\u013a\3\2\2\2S\u013d\3")
        buf.write("\2\2\2U\u013f\3\2\2\2W\u0141\3\2\2\2Y\u0143\3\2\2\2[\u0145")
        buf.write("\3\2\2\2]\u0147\3\2\2\2_\u0149\3\2\2\2a\u014b\3\2\2\2")
        buf.write("c\u014d\3\2\2\2e\u014f\3\2\2\2g\u0151\3\2\2\2i\u0158\3")
        buf.write("\2\2\2k\u015a\3\2\2\2m\u0160\3\2\2\2o\u0167\3\2\2\2q\u016d")
        buf.write("\3\2\2\2s\u017c\3\2\2\2u\u017e\3\2\2\2w\u0185\3\2\2\2")
        buf.write("y\u018b\3\2\2\2{\u0192\3\2\2\2}\u01a5\3\2\2\2\177\u01ba")
        buf.write("\3\2\2\2\u0081\u01bc\3\2\2\2\u0083\u01c1\3\2\2\2\u0085")
        buf.write("\u01c3\3\2\2\2\u0087\u01ce\3\2\2\2\u0089\u01d5\3\2\2\2")
        buf.write("\u008b\u01db\3\2\2\2\u008d\u01e6\3\2\2\2\u008f\u01f5\3")
        buf.write("\2\2\2\u0091\u0201\3\2\2\2\u0093\u0212\3\2\2\2\u0095\u0096")
        buf.write("\7k\2\2\u0096\u0097\7h\2\2\u0097\4\3\2\2\2\u0098\u0099")
        buf.write("\7g\2\2\u0099\u009a\7n\2\2\u009a\u009b\7u\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\6\3\2\2\2\u009d\u009e\7h\2\2\u009e\u009f")
        buf.write("\7q\2\2\u009f\u00a0\7t\2\2\u00a0\b\3\2\2\2\u00a1\u00a2")
        buf.write("\7t\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7v\2\2\u00a4\u00a5")
        buf.write("\7w\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7\7p\2\2\u00a7\n")
        buf.write("\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab")
        buf.write("\7p\2\2\u00ab\u00ac\7e\2\2\u00ac\f\3\2\2\2\u00ad\u00ae")
        buf.write("\7v\2\2\u00ae\u00af\7{\2\2\u00af\u00b0\7r\2\2\u00b0\u00b1")
        buf.write("\7g\2\2\u00b1\16\3\2\2\2\u00b2\u00b3\7u\2\2\u00b3\u00b4")
        buf.write("\7v\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7")
        buf.write("\7e\2\2\u00b7\u00b8\7v\2\2\u00b8\20\3\2\2\2\u00b9\u00ba")
        buf.write("\7k\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd")
        buf.write("\7g\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7h\2\2\u00bf\u00c0")
        buf.write("\7c\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2\7g\2\2\u00c2\22")
        buf.write("\3\2\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6")
        buf.write("\7t\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7i\2\2\u00c9\24\3\2\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7v\2\2\u00cd\26\3\2\2\2\u00ce\u00cf")
        buf.write("\7h\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2")
        buf.write("\7c\2\2\u00d2\u00d3\7v\2\2\u00d3\30\3\2\2\2\u00d4\u00d5")
        buf.write("\7d\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8")
        buf.write("\7n\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7c\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db\32\3\2\2\2\u00dc\u00dd\7e\2\2\u00dd\u00de")
        buf.write("\7q\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\34\3\2\2\2\u00e2\u00e3\7x\2\2\u00e3\u00e4")
        buf.write("\7c\2\2\u00e4\u00e5\7t\2\2\u00e5\36\3\2\2\2\u00e6\u00e7")
        buf.write("\7e\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea")
        buf.write("\7v\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed")
        buf.write("\7w\2\2\u00ed\u00ee\7g\2\2\u00ee \3\2\2\2\u00ef\u00f0")
        buf.write("\7d\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3")
        buf.write("\7c\2\2\u00f3\u00f4\7m\2\2\u00f4\"\3\2\2\2\u00f5\u00f6")
        buf.write("\7t\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7i\2\2\u00f9\u00fa\7g\2\2\u00fa$\3\2\2\2\u00fb\u00fc")
        buf.write("\7p\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe\7n\2\2\u00fe&\3")
        buf.write("\2\2\2\u00ff\u0100\7v\2\2\u0100\u0101\7t\2\2\u0101\u0102")
        buf.write("\7w\2\2\u0102\u0103\7g\2\2\u0103(\3\2\2\2\u0104\u0105")
        buf.write("\7h\2\2\u0105\u0106\7c\2\2\u0106\u0107\7n\2\2\u0107\u0108")
        buf.write("\7u\2\2\u0108\u0109\7g\2\2\u0109*\3\2\2\2\u010a\u010b")
        buf.write("\7-\2\2\u010b,\3\2\2\2\u010c\u010d\7/\2\2\u010d.\3\2\2")
        buf.write("\2\u010e\u010f\7,\2\2\u010f\60\3\2\2\2\u0110\u0111\7\61")
        buf.write("\2\2\u0111\62\3\2\2\2\u0112\u0113\7\'\2\2\u0113\64\3\2")
        buf.write("\2\2\u0114\u0115\7?\2\2\u0115\u0116\7?\2\2\u0116\66\3")
        buf.write("\2\2\2\u0117\u0118\7#\2\2\u0118\u0119\7?\2\2\u01198\3")
        buf.write("\2\2\2\u011a\u011b\7>\2\2\u011b:\3\2\2\2\u011c\u011d\7")
        buf.write(">\2\2\u011d\u011e\7?\2\2\u011e<\3\2\2\2\u011f\u0120\7")
        buf.write("@\2\2\u0120>\3\2\2\2\u0121\u0122\7@\2\2\u0122\u0123\7")
        buf.write("?\2\2\u0123@\3\2\2\2\u0124\u0125\7(\2\2\u0125\u0126\7")
        buf.write("(\2\2\u0126B\3\2\2\2\u0127\u0128\7~\2\2\u0128\u0129\7")
        buf.write("~\2\2\u0129D\3\2\2\2\u012a\u012b\7#\2\2\u012bF\3\2\2\2")
        buf.write("\u012c\u012d\7?\2\2\u012dH\3\2\2\2\u012e\u012f\7-\2\2")
        buf.write("\u012f\u0130\7?\2\2\u0130J\3\2\2\2\u0131\u0132\7/\2\2")
        buf.write("\u0132\u0133\7?\2\2\u0133L\3\2\2\2\u0134\u0135\7,\2\2")
        buf.write("\u0135\u0136\7?\2\2\u0136N\3\2\2\2\u0137\u0138\7\61\2")
        buf.write("\2\u0138\u0139\7?\2\2\u0139P\3\2\2\2\u013a\u013b\7\'\2")
        buf.write("\2\u013b\u013c\7?\2\2\u013cR\3\2\2\2\u013d\u013e\7\60")
        buf.write("\2\2\u013eT\3\2\2\2\u013f\u0140\7<\2\2\u0140V\3\2\2\2")
        buf.write("\u0141\u0142\7*\2\2\u0142X\3\2\2\2\u0143\u0144\7+\2\2")
        buf.write("\u0144Z\3\2\2\2\u0145\u0146\7}\2\2\u0146\\\3\2\2\2\u0147")
        buf.write("\u0148\7\177\2\2\u0148^\3\2\2\2\u0149\u014a\7]\2\2\u014a")
        buf.write("`\3\2\2\2\u014b\u014c\7_\2\2\u014cb\3\2\2\2\u014d\u014e")
        buf.write("\7.\2\2\u014ed\3\2\2\2\u014f\u0150\7=\2\2\u0150f\3\2\2")
        buf.write("\2\u0151\u0155\t\2\2\2\u0152\u0154\t\3\2\2\u0153\u0152")
        buf.write("\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153\3\2\2\2\u0155")
        buf.write("\u0156\3\2\2\2\u0156h\3\2\2\2\u0157\u0155\3\2\2\2\u0158")
        buf.write("\u0159\t\4\2\2\u0159j\3\2\2\2\u015a\u015b\t\5\2\2\u015b")
        buf.write("l\3\2\2\2\u015c\u015d\7\62\2\2\u015d\u0161\7q\2\2\u015e")
        buf.write("\u015f\7\62\2\2\u015f\u0161\7Q\2\2\u0160\u015c\3\2\2\2")
        buf.write("\u0160\u015e\3\2\2\2\u0161\u0163\3\2\2\2\u0162\u0164\t")
        buf.write("\5\2\2\u0163\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0163")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166n\3\2\2\2\u0167\u0168")
        buf.write("\t\6\2\2\u0168p\3\2\2\2\u0169\u016a\7\62\2\2\u016a\u016e")
        buf.write("\7z\2\2\u016b\u016c\7\62\2\2\u016c\u016e\7Z\2\2\u016d")
        buf.write("\u0169\3\2\2\2\u016d\u016b\3\2\2\2\u016e\u0170\3\2\2\2")
        buf.write("\u016f\u0171\t\6\2\2\u0170\u016f\3\2\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173r")
        buf.write("\3\2\2\2\u0174\u017d\7\62\2\2\u0175\u0179\t\7\2\2\u0176")
        buf.write("\u0178\t\4\2\2\u0177\u0176\3\2\2\2\u0178\u017b\3\2\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017d\3")
        buf.write("\2\2\2\u017b\u0179\3\2\2\2\u017c\u0174\3\2\2\2\u017c\u0175")
        buf.write("\3\2\2\2\u017dt\3\2\2\2\u017e\u0182\7\60\2\2\u017f\u0181")
        buf.write("\t\4\2\2\u0180\u017f\3\2\2\2\u0181\u0184\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183v\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0185\u0186\t\b\2\2\u0186x\3\2\2\2\u0187")
        buf.write("\u0188\7\62\2\2\u0188\u018c\7d\2\2\u0189\u018a\7\62\2")
        buf.write("\2\u018a\u018c\7D\2\2\u018b\u0187\3\2\2\2\u018b\u0189")
        buf.write("\3\2\2\2\u018c\u018e\3\2\2\2\u018d\u018f\t\b\2\2\u018e")
        buf.write("\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u018e\3\2\2\2")
        buf.write("\u0190\u0191\3\2\2\2\u0191z\3\2\2\2\u0192\u0194\t\t\2")
        buf.write("\2\u0193\u0195\t\n\2\2\u0194\u0193\3\2\2\2\u0194\u0195")
        buf.write("\3\2\2\2\u0195\u0197\3\2\2\2\u0196\u0198\t\4\2\2\u0197")
        buf.write("\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u0197\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019a|\3\2\2\2\u019b\u01a6\5s:\2")
        buf.write("\u019c\u019d\5q9\2\u019d\u019e\b?\2\2\u019e\u01a6\3\2")
        buf.write("\2\2\u019f\u01a0\5m\67\2\u01a0\u01a1\b?\3\2\u01a1\u01a6")
        buf.write("\3\2\2\2\u01a2\u01a3\5y=\2\u01a3\u01a4\b?\4\2\u01a4\u01a6")
        buf.write("\3\2\2\2\u01a5\u019b\3\2\2\2\u01a5\u019c\3\2\2\2\u01a5")
        buf.write("\u019f\3\2\2\2\u01a5\u01a2\3\2\2\2\u01a6~\3\2\2\2\u01a7")
        buf.write("\u01a9\t\4\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\3")
        buf.write("\2\2\2\u01ac\u01ae\5u;\2\u01ad\u01af\5{>\2\u01ae\u01ad")
        buf.write("\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01bb\3\2\2\2\u01b0")
        buf.write("\u01b2\5u;\2\u01b1\u01b3\5{>\2\u01b2\u01b1\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u01bb\3\2\2\2\u01b4\u01b6\t\4\2\2")
        buf.write("\u01b5\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b5\3")
        buf.write("\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bb")
        buf.write("\5{>\2\u01ba\u01a8\3\2\2\2\u01ba\u01b0\3\2\2\2\u01ba\u01b5")
        buf.write("\3\2\2\2\u01bb\u0080\3\2\2\2\u01bc\u01bd\t\13\2\2\u01bd")
        buf.write("\u0082\3\2\2\2\u01be\u01c2\n\f\2\2\u01bf\u01c0\7^\2\2")
        buf.write("\u01c0\u01c2\5\u0081A\2\u01c1\u01be\3\2\2\2\u01c1\u01bf")
        buf.write("\3\2\2\2\u01c2\u0084\3\2\2\2\u01c3\u01c7\7$\2\2\u01c4")
        buf.write("\u01c6\5\u0083B\2\u01c5\u01c4\3\2\2\2\u01c6\u01c9\3\2")
        buf.write("\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01ca")
        buf.write("\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cb\7$\2\2\u01cb")
        buf.write("\u01cc\bC\5\2\u01cc\u0086\3\2\2\2\u01cd\u01cf\t\r\2\2")
        buf.write("\u01ce\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01ce\3")
        buf.write("\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3")
        buf.write("\bD\6\2\u01d3\u0088\3\2\2\2\u01d4\u01d6\7\17\2\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7\3\2\2\2")
        buf.write("\u01d7\u01d8\7\f\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\b")
        buf.write("E\6\2\u01da\u008a\3\2\2\2\u01db\u01dc\7\61\2\2\u01dc\u01dd")
        buf.write("\7\61\2\2\u01dd\u01e1\3\2\2\2\u01de\u01e0\n\16\2\2\u01df")
        buf.write("\u01de\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2")
        buf.write("\u01e1\u01e2\3\2\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01e1\3")
        buf.write("\2\2\2\u01e4\u01e5\bF\6\2\u01e5\u008c\3\2\2\2\u01e6\u01e7")
        buf.write("\7\61\2\2\u01e7\u01e8\7,\2\2\u01e8\u01ed\3\2\2\2\u01e9")
        buf.write("\u01ec\5\u008dG\2\u01ea\u01ec\13\2\2\2\u01eb\u01e9\3\2")
        buf.write("\2\2\u01eb\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01ee")
        buf.write("\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ee\u01f0\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01f0\u01f1\7,\2\2\u01f1\u01f2\7\61\2\2")
        buf.write("\u01f2\u01f3\3\2\2\2\u01f3\u01f4\bG\6\2\u01f4\u008e\3")
        buf.write("\2\2\2\u01f5\u01f9\7$\2\2\u01f6\u01f8\5\u0083B\2\u01f7")
        buf.write("\u01f6\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2")
        buf.write("\u01f9\u01fa\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3")
        buf.write("\2\2\2\u01fc\u01fe\t\17\2\2\u01fd\u01fc\3\2\2\2\u01fe")
        buf.write("\u01ff\3\2\2\2\u01ff\u0200\bH\7\2\u0200\u0090\3\2\2\2")
        buf.write("\u0201\u0205\7$\2\2\u0202\u0204\5\u0083B\2\u0203\u0202")
        buf.write("\3\2\2\2\u0204\u0207\3\2\2\2\u0205\u0203\3\2\2\2\u0205")
        buf.write("\u0206\3\2\2\2\u0206\u0208\3\2\2\2\u0207\u0205\3\2\2\2")
        buf.write("\u0208\u0209\7^\2\2\u0209\u020d\n\13\2\2\u020a\u020c\5")
        buf.write("\u0083B\2\u020b\u020a\3\2\2\2\u020c\u020f\3\2\2\2\u020d")
        buf.write("\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u0210\3\2\2\2")
        buf.write("\u020f\u020d\3\2\2\2\u0210\u0211\bI\b\2\u0211\u0092\3")
        buf.write("\2\2\2\u0212\u0213\13\2\2\2\u0213\u0214\bJ\t\2\u0214\u0094")
        buf.write("\3\2\2\2 \2\u0155\u0160\u0165\u016d\u0172\u0179\u017c")
        buf.write("\u0182\u018b\u0190\u0194\u0199\u01a5\u01aa\u01ae\u01b2")
        buf.write("\u01b7\u01ba\u01c1\u01c7\u01d0\u01d5\u01e1\u01eb\u01ed")
        buf.write("\u01f9\u01fd\u0205\u020d\n\3?\2\3?\3\3?\4\3C\5\b\2\2\3")
        buf.write("H\6\3I\7\3J\b")
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
    FLOAT_LIT = 53
    STRING_LIT = 54
    WS = 55
    NEWLINE = 56
    LINE_COMMENT = 57
    BLOCK_COMMENT = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "':'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
            "GREATER", "GREATER_OR_EQUAL", "AND", "OR", "NOT", "ASSIGN", 
            "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
            "DOT", "COLON", "LP", "RP", "LB", "RB", "LSB", "RSB", "COMMA", 
            "SEMI", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", "NEWLINE", 
            "LINE_COMMENT", "BLOCK_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
                  "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
                  "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", 
                  "LP", "RP", "LB", "RB", "LSB", "RSB", "COMMA", "SEMI", 
                  "ID", "DIGIT", "OCTAL_DIGIT", "OCTAL", "HEX_DIGIT", "HEX", 
                  "DECIMAL", "DECIMAL_PART", "BINARY_DIGIT", "BINARY", "EXPONENT", 
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
            actions[61] = self.INT_LIT_action 
            actions[65] = self.STRING_LIT_action 
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
     



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
        buf.write("\u022b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\7\67")
        buf.write("\u0160\n\67\f\67\16\67\u0163\13\67\38\38\38\78\u0168\n")
        buf.write("8\f8\168\u016b\138\58\u016d\n8\39\39\39\39\59\u0173\n")
        buf.write("9\39\69\u0176\n9\r9\169\u0177\3:\3:\3:\3:\5:\u017e\n:")
        buf.write("\3:\6:\u0181\n:\r:\16:\u0182\3;\3;\3;\3;\5;\u0189\n;\3")
        buf.write(";\6;\u018c\n;\r;\16;\u018d\3<\3<\3<\7<\u0193\n<\f<\16")
        buf.write("<\u0196\13<\5<\u0198\n<\3=\3=\7=\u019c\n=\f=\16=\u019f")
        buf.write("\13=\3>\3>\5>\u01a3\n>\3>\3>\3>\7>\u01a8\n>\f>\16>\u01ab")
        buf.write("\13>\5>\u01ad\n>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u01b9")
        buf.write("\n?\3@\3@\3@\5@\u01be\n@\3@\3@\3@\3@\3@\6@\u01c5\n@\r")
        buf.write("@\16@\u01c6\3@\5@\u01ca\n@\3@\3@\3@\5@\u01cf\n@\3A\3A")
        buf.write("\3B\3B\3B\5B\u01d6\nB\3C\3C\7C\u01da\nC\fC\16C\u01dd\13")
        buf.write("C\3C\3C\3C\3D\6D\u01e3\nD\rD\16D\u01e4\3D\3D\3E\5E\u01ea")
        buf.write("\nE\3E\3E\3E\3F\3F\3F\3F\3F\7F\u01f4\nF\fF\16F\u01f7\13")
        buf.write("F\3F\3F\3F\3F\3F\3G\3G\3G\3G\7G\u0202\nG\fG\16G\u0205")
        buf.write("\13G\3G\3G\3H\3H\7H\u020b\nH\fH\16H\u020e\13H\3H\5H\u0211")
        buf.write("\nH\3H\3H\3I\3I\7I\u0217\nI\fI\16I\u021a\13I\3I\3I\3I")
        buf.write("\7I\u021f\nI\fI\16I\u0222\13I\3I\5I\u0225\nI\3I\3I\3J")
        buf.write("\3J\3J\3\u01f5\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o\2q\2s\2u\2w\2y\2{\2}9\177:\u0081\2\u0083\2")
        buf.write("\u0085;\u0087<\u0089=\u008b>\u008d?\u008f@\u0091A\u0093")
        buf.write("B\3\2\20\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\5\2")
        buf.write("\62;CHch\3\2\629\3\2\62\63\4\2GGgg\4\2--//\7\2$$^^ppt")
        buf.write("tvv\6\2\f\f\17\17$$^^\5\2\13\13\16\17\"\"\4\2\f\f\17\17")
        buf.write("\4\3\f\f\17\17\2\u0244\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\3\u0095")
        buf.write("\3\2\2\2\5\u009c\3\2\2\2\7\u009f\3\2\2\2\t\u00a4\3\2\2")
        buf.write("\2\13\u00a8\3\2\2\2\r\u00af\3\2\2\2\17\u00b4\3\2\2\2\21")
        buf.write("\u00b9\3\2\2\2\23\u00c0\3\2\2\2\25\u00ca\3\2\2\2\27\u00d1")
        buf.write("\3\2\2\2\31\u00d5\3\2\2\2\33\u00db\3\2\2\2\35\u00e3\3")
        buf.write("\2\2\2\37\u00e9\3\2\2\2!\u00ed\3\2\2\2#\u00f6\3\2\2\2")
        buf.write("%\u00fc\3\2\2\2\'\u0102\3\2\2\2)\u0106\3\2\2\2+\u010b")
        buf.write("\3\2\2\2-\u0111\3\2\2\2/\u0113\3\2\2\2\61\u0115\3\2\2")
        buf.write("\2\63\u0117\3\2\2\2\65\u0119\3\2\2\2\67\u011b\3\2\2\2")
        buf.write("9\u011e\3\2\2\2;\u0121\3\2\2\2=\u0123\3\2\2\2?\u0126\3")
        buf.write("\2\2\2A\u0128\3\2\2\2C\u012b\3\2\2\2E\u012e\3\2\2\2G\u0131")
        buf.write("\3\2\2\2I\u0133\3\2\2\2K\u0135\3\2\2\2M\u0138\3\2\2\2")
        buf.write("O\u013b\3\2\2\2Q\u013e\3\2\2\2S\u0141\3\2\2\2U\u0144\3")
        buf.write("\2\2\2W\u0146\3\2\2\2Y\u0148\3\2\2\2[\u014b\3\2\2\2]\u014d")
        buf.write("\3\2\2\2_\u014f\3\2\2\2a\u0151\3\2\2\2c\u0153\3\2\2\2")
        buf.write("e\u0155\3\2\2\2g\u0157\3\2\2\2i\u0159\3\2\2\2k\u015b\3")
        buf.write("\2\2\2m\u015d\3\2\2\2o\u016c\3\2\2\2q\u0172\3\2\2\2s\u017d")
        buf.write("\3\2\2\2u\u0188\3\2\2\2w\u0197\3\2\2\2y\u0199\3\2\2\2")
        buf.write("{\u01a0\3\2\2\2}\u01b8\3\2\2\2\177\u01ce\3\2\2\2\u0081")
        buf.write("\u01d0\3\2\2\2\u0083\u01d5\3\2\2\2\u0085\u01d7\3\2\2\2")
        buf.write("\u0087\u01e2\3\2\2\2\u0089\u01e9\3\2\2\2\u008b\u01ee\3")
        buf.write("\2\2\2\u008d\u01fd\3\2\2\2\u008f\u0208\3\2\2\2\u0091\u0214")
        buf.write("\3\2\2\2\u0093\u0228\3\2\2\2\u0095\u0096\7x\2\2\u0096")
        buf.write("\u0097\7q\2\2\u0097\u0098\7v\2\2\u0098\u0099\7k\2\2\u0099")
        buf.write("\u009a\7g\2\2\u009a\u009b\7p\2\2\u009b\4\3\2\2\2\u009c")
        buf.write("\u009d\7k\2\2\u009d\u009e\7h\2\2\u009e\6\3\2\2\2\u009f")
        buf.write("\u00a0\7g\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2\7u\2\2\u00a2")
        buf.write("\u00a3\7g\2\2\u00a3\b\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5")
        buf.write("\u00a6\7q\2\2\u00a6\u00a7\7t\2\2\u00a7\n\3\2\2\2\u00a8")
        buf.write("\u00a9\7t\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7v\2\2\u00ab")
        buf.write("\u00ac\7w\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae\7p\2\2\u00ae")
        buf.write("\f\3\2\2\2\u00af\u00b0\7h\2\2\u00b0\u00b1\7w\2\2\u00b1")
        buf.write("\u00b2\7p\2\2\u00b2\u00b3\7e\2\2\u00b3\16\3\2\2\2\u00b4")
        buf.write("\u00b5\7v\2\2\u00b5\u00b6\7{\2\2\u00b6\u00b7\7r\2\2\u00b7")
        buf.write("\u00b8\7g\2\2\u00b8\20\3\2\2\2\u00b9\u00ba\7u\2\2\u00ba")
        buf.write("\u00bb\7v\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7w\2\2\u00bd")
        buf.write("\u00be\7e\2\2\u00be\u00bf\7v\2\2\u00bf\22\3\2\2\2\u00c0")
        buf.write("\u00c1\7k\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3\7v\2\2\u00c3")
        buf.write("\u00c4\7g\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6\7h\2\2\u00c6")
        buf.write("\u00c7\7c\2\2\u00c7\u00c8\7e\2\2\u00c8\u00c9\7g\2\2\u00c9")
        buf.write("\24\3\2\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7v\2\2\u00cc")
        buf.write("\u00cd\7t\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7p\2\2\u00cf")
        buf.write("\u00d0\7i\2\2\u00d0\26\3\2\2\2\u00d1\u00d2\7k\2\2\u00d2")
        buf.write("\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\30\3\2\2\2\u00d5")
        buf.write("\u00d6\7h\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8\7q\2\2\u00d8")
        buf.write("\u00d9\7c\2\2\u00d9\u00da\7v\2\2\u00da\32\3\2\2\2\u00db")
        buf.write("\u00dc\7d\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7q\2\2\u00de")
        buf.write("\u00df\7n\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1\7c\2\2\u00e1")
        buf.write("\u00e2\7p\2\2\u00e2\34\3\2\2\2\u00e3\u00e4\7e\2\2\u00e4")
        buf.write("\u00e5\7q\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7u\2\2\u00e7")
        buf.write("\u00e8\7v\2\2\u00e8\36\3\2\2\2\u00e9\u00ea\7x\2\2\u00ea")
        buf.write("\u00eb\7c\2\2\u00eb\u00ec\7t\2\2\u00ec \3\2\2\2\u00ed")
        buf.write("\u00ee\7e\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7p\2\2\u00f0")
        buf.write("\u00f1\7v\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7p\2\2\u00f3")
        buf.write("\u00f4\7w\2\2\u00f4\u00f5\7g\2\2\u00f5\"\3\2\2\2\u00f6")
        buf.write("\u00f7\7d\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7g\2\2\u00f9")
        buf.write("\u00fa\7c\2\2\u00fa\u00fb\7m\2\2\u00fb$\3\2\2\2\u00fc")
        buf.write("\u00fd\7t\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7p\2\2\u00ff")
        buf.write("\u0100\7i\2\2\u0100\u0101\7g\2\2\u0101&\3\2\2\2\u0102")
        buf.write("\u0103\7p\2\2\u0103\u0104\7k\2\2\u0104\u0105\7n\2\2\u0105")
        buf.write("(\3\2\2\2\u0106\u0107\7v\2\2\u0107\u0108\7t\2\2\u0108")
        buf.write("\u0109\7w\2\2\u0109\u010a\7g\2\2\u010a*\3\2\2\2\u010b")
        buf.write("\u010c\7h\2\2\u010c\u010d\7c\2\2\u010d\u010e\7n\2\2\u010e")
        buf.write("\u010f\7u\2\2\u010f\u0110\7g\2\2\u0110,\3\2\2\2\u0111")
        buf.write("\u0112\7-\2\2\u0112.\3\2\2\2\u0113\u0114\7/\2\2\u0114")
        buf.write("\60\3\2\2\2\u0115\u0116\7,\2\2\u0116\62\3\2\2\2\u0117")
        buf.write("\u0118\7\61\2\2\u0118\64\3\2\2\2\u0119\u011a\7\'\2\2\u011a")
        buf.write("\66\3\2\2\2\u011b\u011c\7?\2\2\u011c\u011d\7?\2\2\u011d")
        buf.write("8\3\2\2\2\u011e\u011f\7#\2\2\u011f\u0120\7?\2\2\u0120")
        buf.write(":\3\2\2\2\u0121\u0122\7>\2\2\u0122<\3\2\2\2\u0123\u0124")
        buf.write("\7>\2\2\u0124\u0125\7?\2\2\u0125>\3\2\2\2\u0126\u0127")
        buf.write("\7@\2\2\u0127@\3\2\2\2\u0128\u0129\7@\2\2\u0129\u012a")
        buf.write("\7?\2\2\u012aB\3\2\2\2\u012b\u012c\7(\2\2\u012c\u012d")
        buf.write("\7(\2\2\u012dD\3\2\2\2\u012e\u012f\7~\2\2\u012f\u0130")
        buf.write("\7~\2\2\u0130F\3\2\2\2\u0131\u0132\7#\2\2\u0132H\3\2\2")
        buf.write("\2\u0133\u0134\7?\2\2\u0134J\3\2\2\2\u0135\u0136\7-\2")
        buf.write("\2\u0136\u0137\7?\2\2\u0137L\3\2\2\2\u0138\u0139\7/\2")
        buf.write("\2\u0139\u013a\7?\2\2\u013aN\3\2\2\2\u013b\u013c\7,\2")
        buf.write("\2\u013c\u013d\7?\2\2\u013dP\3\2\2\2\u013e\u013f\7\61")
        buf.write("\2\2\u013f\u0140\7?\2\2\u0140R\3\2\2\2\u0141\u0142\7\'")
        buf.write("\2\2\u0142\u0143\7?\2\2\u0143T\3\2\2\2\u0144\u0145\7\60")
        buf.write("\2\2\u0145V\3\2\2\2\u0146\u0147\7<\2\2\u0147X\3\2\2\2")
        buf.write("\u0148\u0149\7<\2\2\u0149\u014a\7?\2\2\u014aZ\3\2\2\2")
        buf.write("\u014b\u014c\7a\2\2\u014c\\\3\2\2\2\u014d\u014e\7*\2\2")
        buf.write("\u014e^\3\2\2\2\u014f\u0150\7+\2\2\u0150`\3\2\2\2\u0151")
        buf.write("\u0152\7}\2\2\u0152b\3\2\2\2\u0153\u0154\7\177\2\2\u0154")
        buf.write("d\3\2\2\2\u0155\u0156\7]\2\2\u0156f\3\2\2\2\u0157\u0158")
        buf.write("\7_\2\2\u0158h\3\2\2\2\u0159\u015a\7.\2\2\u015aj\3\2\2")
        buf.write("\2\u015b\u015c\7=\2\2\u015cl\3\2\2\2\u015d\u0161\t\2\2")
        buf.write("\2\u015e\u0160\t\3\2\2\u015f\u015e\3\2\2\2\u0160\u0163")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("n\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u016d\7\62\2\2\u0165")
        buf.write("\u0169\t\4\2\2\u0166\u0168\t\5\2\2\u0167\u0166\3\2\2\2")
        buf.write("\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3")
        buf.write("\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u0164")
        buf.write("\3\2\2\2\u016c\u0165\3\2\2\2\u016dp\3\2\2\2\u016e\u016f")
        buf.write("\7\62\2\2\u016f\u0173\7z\2\2\u0170\u0171\7\62\2\2\u0171")
        buf.write("\u0173\7Z\2\2\u0172\u016e\3\2\2\2\u0172\u0170\3\2\2\2")
        buf.write("\u0173\u0175\3\2\2\2\u0174\u0176\t\6\2\2\u0175\u0174\3")
        buf.write("\2\2\2\u0176\u0177\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178")
        buf.write("\3\2\2\2\u0178r\3\2\2\2\u0179\u017a\7\62\2\2\u017a\u017e")
        buf.write("\7q\2\2\u017b\u017c\7\62\2\2\u017c\u017e\7Q\2\2\u017d")
        buf.write("\u0179\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u0180\3\2\2\2")
        buf.write("\u017f\u0181\t\7\2\2\u0180\u017f\3\2\2\2\u0181\u0182\3")
        buf.write("\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183t")
        buf.write("\3\2\2\2\u0184\u0185\7\62\2\2\u0185\u0189\7d\2\2\u0186")
        buf.write("\u0187\7\62\2\2\u0187\u0189\7D\2\2\u0188\u0184\3\2\2\2")
        buf.write("\u0188\u0186\3\2\2\2\u0189\u018b\3\2\2\2\u018a\u018c\t")
        buf.write("\b\2\2\u018b\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018b")
        buf.write("\3\2\2\2\u018d\u018e\3\2\2\2\u018ev\3\2\2\2\u018f\u0198")
        buf.write("\7\62\2\2\u0190\u0194\t\4\2\2\u0191\u0193\t\5\2\2\u0192")
        buf.write("\u0191\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0194\3")
        buf.write("\2\2\2\u0197\u018f\3\2\2\2\u0197\u0190\3\2\2\2\u0198x")
        buf.write("\3\2\2\2\u0199\u019d\7\60\2\2\u019a\u019c\t\5\2\2\u019b")
        buf.write("\u019a\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019d\u019e\3\2\2\2\u019ez\3\2\2\2\u019f\u019d\3\2\2")
        buf.write("\2\u01a0\u01a2\t\t\2\2\u01a1\u01a3\t\n\2\2\u01a2\u01a1")
        buf.write("\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01ac\3\2\2\2\u01a4")
        buf.write("\u01ad\7\62\2\2\u01a5\u01a9\t\4\2\2\u01a6\u01a8\t\5\2")
        buf.write("\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab")
        buf.write("\u01a9\3\2\2\2\u01ac\u01a4\3\2\2\2\u01ac\u01a5\3\2\2\2")
        buf.write("\u01ad|\3\2\2\2\u01ae\u01b9\5o8\2\u01af\u01b0\5q9\2\u01b0")
        buf.write("\u01b1\b?\2\2\u01b1\u01b9\3\2\2\2\u01b2\u01b3\5s:\2\u01b3")
        buf.write("\u01b4\b?\3\2\u01b4\u01b9\3\2\2\2\u01b5\u01b6\5u;\2\u01b6")
        buf.write("\u01b7\b?\4\2\u01b7\u01b9\3\2\2\2\u01b8\u01ae\3\2\2\2")
        buf.write("\u01b8\u01af\3\2\2\2\u01b8\u01b2\3\2\2\2\u01b8\u01b5\3")
        buf.write("\2\2\2\u01b9~\3\2\2\2\u01ba\u01bb\5w<\2\u01bb\u01bd\5")
        buf.write("y=\2\u01bc\u01be\5{>\2\u01bd\u01bc\3\2\2\2\u01bd\u01be")
        buf.write("\3\2\2\2\u01be\u01cf\3\2\2\2\u01bf\u01c0\5w<\2\u01c0\u01c1")
        buf.write("\5{>\2\u01c1\u01cf\3\2\2\2\u01c2\u01c4\5y=\2\u01c3\u01c5")
        buf.write("\t\5\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6")
        buf.write("\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c9\3\2\2\2")
        buf.write("\u01c8\u01ca\5{>\2\u01c9\u01c8\3\2\2\2\u01c9\u01ca\3\2")
        buf.write("\2\2\u01ca\u01cf\3\2\2\2\u01cb\u01cc\5w<\2\u01cc\u01cd")
        buf.write("\5y=\2\u01cd\u01cf\3\2\2\2\u01ce\u01ba\3\2\2\2\u01ce\u01bf")
        buf.write("\3\2\2\2\u01ce\u01c2\3\2\2\2\u01ce\u01cb\3\2\2\2\u01cf")
        buf.write("\u0080\3\2\2\2\u01d0\u01d1\t\13\2\2\u01d1\u0082\3\2\2")
        buf.write("\2\u01d2\u01d6\n\f\2\2\u01d3\u01d4\7^\2\2\u01d4\u01d6")
        buf.write("\5\u0081A\2\u01d5\u01d2\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6")
        buf.write("\u0084\3\2\2\2\u01d7\u01db\7$\2\2\u01d8\u01da\5\u0083")
        buf.write("B\2\u01d9\u01d8\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9")
        buf.write("\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd")
        buf.write("\u01db\3\2\2\2\u01de\u01df\7$\2\2\u01df\u01e0\bC\5\2\u01e0")
        buf.write("\u0086\3\2\2\2\u01e1\u01e3\t\r\2\2\u01e2\u01e1\3\2\2\2")
        buf.write("\u01e3\u01e4\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3")
        buf.write("\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7\bD\6\2\u01e7\u0088")
        buf.write("\3\2\2\2\u01e8\u01ea\7\17\2\2\u01e9\u01e8\3\2\2\2\u01e9")
        buf.write("\u01ea\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec\7\f\2\2")
        buf.write("\u01ec\u01ed\bE\7\2\u01ed\u008a\3\2\2\2\u01ee\u01ef\7")
        buf.write("\61\2\2\u01ef\u01f0\7,\2\2\u01f0\u01f5\3\2\2\2\u01f1\u01f4")
        buf.write("\5\u008bF\2\u01f2\u01f4\13\2\2\2\u01f3\u01f1\3\2\2\2\u01f3")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f6\3\2\2\2")
        buf.write("\u01f5\u01f3\3\2\2\2\u01f6\u01f8\3\2\2\2\u01f7\u01f5\3")
        buf.write("\2\2\2\u01f8\u01f9\7,\2\2\u01f9\u01fa\7\61\2\2\u01fa\u01fb")
        buf.write("\3\2\2\2\u01fb\u01fc\bF\6\2\u01fc\u008c\3\2\2\2\u01fd")
        buf.write("\u01fe\7\61\2\2\u01fe\u01ff\7\61\2\2\u01ff\u0203\3\2\2")
        buf.write("\2\u0200\u0202\n\16\2\2\u0201\u0200\3\2\2\2\u0202\u0205")
        buf.write("\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204")
        buf.write("\u0206\3\2\2\2\u0205\u0203\3\2\2\2\u0206\u0207\bG\6\2")
        buf.write("\u0207\u008e\3\2\2\2\u0208\u020c\7$\2\2\u0209\u020b\5")
        buf.write("\u0083B\2\u020a\u0209\3\2\2\2\u020b\u020e\3\2\2\2\u020c")
        buf.write("\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u0210\3\2\2\2")
        buf.write("\u020e\u020c\3\2\2\2\u020f\u0211\t\17\2\2\u0210\u020f")
        buf.write("\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0213\bH\b\2\u0213")
        buf.write("\u0090\3\2\2\2\u0214\u0218\7$\2\2\u0215\u0217\5\u0083")
        buf.write("B\2\u0216\u0215\3\2\2\2\u0217\u021a\3\2\2\2\u0218\u0216")
        buf.write("\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021b\3\2\2\2\u021a")
        buf.write("\u0218\3\2\2\2\u021b\u021c\7^\2\2\u021c\u0220\n\13\2\2")
        buf.write("\u021d\u021f\5\u0083B\2\u021e\u021d\3\2\2\2\u021f\u0222")
        buf.write("\3\2\2\2\u0220\u021e\3\2\2\2\u0220\u0221\3\2\2\2\u0221")
        buf.write("\u0224\3\2\2\2\u0222\u0220\3\2\2\2\u0223\u0225\7$\2\2")
        buf.write("\u0224\u0223\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0226\3")
        buf.write("\2\2\2\u0226\u0227\bI\t\2\u0227\u0092\3\2\2\2\u0228\u0229")
        buf.write("\13\2\2\2\u0229\u022a\bJ\n\2\u022a\u0094\3\2\2\2#\2\u0161")
        buf.write("\u0169\u016c\u0172\u0177\u017d\u0182\u0188\u018d\u0194")
        buf.write("\u0197\u019d\u01a2\u01a9\u01ac\u01b8\u01bd\u01c6\u01c9")
        buf.write("\u01ce\u01d5\u01db\u01e4\u01e9\u01f3\u01f5\u0203\u020c")
        buf.write("\u0210\u0218\u0220\u0224\13\3?\2\3?\3\3?\4\3C\5\b\2\2")
        buf.write("\3E\6\3H\7\3I\b\3J\t")
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
    BLOCK_COMMENT = 60
    LINE_COMMENT = 61
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
            "STRING_LIT", "WS", "NEWLINE", "BLOCK_COMMENT", "LINE_COMMENT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
                  "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
                  "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", 
                  "SHORT_ASSIGN", "UNDERSCORE", "LP", "RP", "LB", "RB", 
                  "LSB", "RSB", "COMMA", "SEMI", "ID", "DECIMAL", "HEX", 
                  "OCTAL", "BINARY", "FLOAT_DECIMAL", "DECIMAL_PART", "EXPONENT", 
                  "INT_LIT", "FLOAT_LIT", "ESC_CHAR", "STR_CHAR", "STRING_LIT", 
                  "WS", "NEWLINE", "BLOCK_COMMENT", "LINE_COMMENT", "UNCLOSE_STRING", 
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
            actions[61] = self.INT_LIT_action 
            actions[65] = self.STRING_LIT_action 
            actions[67] = self.NEWLINE_action 
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
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = "\n"
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                    if self.text[-1] in ['\r','\n']: #nếu kết thúc bằng dấu xuống dòng thì cắt dấu xuống dòng
                        self.text = self.text[1:-1]
                    else: #nếu kết thúc bằng EOF thì lấy từ đầu chuỗi đến hết
                        self.text = self.text[1:]
                    raise UncloseString(self.text)
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                    illegal_str = str(self.text)
                    i = illegal_str.find('\\')
                    while i != -1 and illegal_str[i+1] in 'rnt"\\':
                        i = illegal_str.find('\\', i+2)
                    raise IllegalEscape(illegal_str[1:i+2])
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise ErrorToken(self.text)
     



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
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\7\64\u0157\n\64\f\64\16\64\u015a\13\64\3")
        buf.write("\65\3\65\3\66\3\66\3\67\3\67\3\67\3\67\5\67\u0164\n\67")
        buf.write("\3\67\6\67\u0167\n\67\r\67\16\67\u0168\38\38\39\39\39")
        buf.write("\39\59\u0171\n9\39\69\u0174\n9\r9\169\u0175\3:\3:\3:\7")
        buf.write(":\u017b\n:\f:\16:\u017e\13:\5:\u0180\n:\3;\3;\7;\u0184")
        buf.write("\n;\f;\16;\u0187\13;\3<\3<\3=\3=\3=\3=\5=\u018f\n=\3=")
        buf.write("\6=\u0192\n=\r=\16=\u0193\3>\3>\5>\u0198\n>\3>\6>\u019b")
        buf.write("\n>\r>\16>\u019c\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u01a9")
        buf.write("\n?\3@\6@\u01ac\n@\r@\16@\u01ad\3@\3@\5@\u01b2\n@\3@\3")
        buf.write("@\5@\u01b6\n@\3@\6@\u01b9\n@\r@\16@\u01ba\3@\5@\u01be")
        buf.write("\n@\3A\3A\3B\3B\3B\5B\u01c5\nB\3C\3C\7C\u01c9\nC\fC\16")
        buf.write("C\u01cc\13C\3C\3C\3C\3D\6D\u01d2\nD\rD\16D\u01d3\3D\3")
        buf.write("D\3E\3E\3E\3E\7E\u01dc\nE\fE\16E\u01df\13E\3E\3E\3F\3")
        buf.write("F\3F\3F\3F\7F\u01e8\nF\fF\16F\u01eb\13F\3F\3F\3F\3F\3")
        buf.write("F\3G\3G\7G\u01f4\nG\fG\16G\u01f7\13G\3G\5G\u01fa\nG\3")
        buf.write("G\3G\3H\3H\7H\u0200\nH\fH\16H\u0203\13H\3H\3H\3H\7H\u0208")
        buf.write("\nH\fH\16H\u020b\13H\3H\3H\3I\3I\3I\3\u01e9\2J\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\2k\2m\2o\2q\2s\2u\2w\2y")
        buf.write("\2{\2}\66\177\67\u0081\2\u0083\2\u00858\u00879\u0089:")
        buf.write("\u008b;\u008d<\u008f=\u0091>\3\2\20\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\62;\3\2\629\5\2\62;CHch\3\2\63;\3\2\62\63")
        buf.write("\4\2GGgg\4\2--//\t\2$$))^^ddppttvv\6\2\f\f\17\17$$^^\5")
        buf.write("\2\13\f\16\17\"\"\4\2\f\f\17\17\4\3\f\f\17\17\2\u0222")
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
        buf.write("\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u009a")
        buf.write("\3\2\2\2\7\u009d\3\2\2\2\t\u00a2\3\2\2\2\13\u00a6\3\2")
        buf.write("\2\2\r\u00ad\3\2\2\2\17\u00b2\3\2\2\2\21\u00b7\3\2\2\2")
        buf.write("\23\u00be\3\2\2\2\25\u00c8\3\2\2\2\27\u00cf\3\2\2\2\31")
        buf.write("\u00d3\3\2\2\2\33\u00d9\3\2\2\2\35\u00e1\3\2\2\2\37\u00e7")
        buf.write("\3\2\2\2!\u00eb\3\2\2\2#\u00f4\3\2\2\2%\u00fa\3\2\2\2")
        buf.write("\'\u0100\3\2\2\2)\u0104\3\2\2\2+\u0109\3\2\2\2-\u010f")
        buf.write("\3\2\2\2/\u0111\3\2\2\2\61\u0113\3\2\2\2\63\u0115\3\2")
        buf.write("\2\2\65\u0117\3\2\2\2\67\u0119\3\2\2\29\u011c\3\2\2\2")
        buf.write(";\u011f\3\2\2\2=\u0121\3\2\2\2?\u0124\3\2\2\2A\u0126\3")
        buf.write("\2\2\2C\u0129\3\2\2\2E\u012c\3\2\2\2G\u012f\3\2\2\2I\u0131")
        buf.write("\3\2\2\2K\u0133\3\2\2\2M\u0136\3\2\2\2O\u0139\3\2\2\2")
        buf.write("Q\u013c\3\2\2\2S\u013f\3\2\2\2U\u0142\3\2\2\2W\u0144\3")
        buf.write("\2\2\2Y\u0146\3\2\2\2[\u0148\3\2\2\2]\u014a\3\2\2\2_\u014c")
        buf.write("\3\2\2\2a\u014e\3\2\2\2c\u0150\3\2\2\2e\u0152\3\2\2\2")
        buf.write("g\u0154\3\2\2\2i\u015b\3\2\2\2k\u015d\3\2\2\2m\u0163\3")
        buf.write("\2\2\2o\u016a\3\2\2\2q\u0170\3\2\2\2s\u017f\3\2\2\2u\u0181")
        buf.write("\3\2\2\2w\u0188\3\2\2\2y\u018e\3\2\2\2{\u0195\3\2\2\2")
        buf.write("}\u01a8\3\2\2\2\177\u01bd\3\2\2\2\u0081\u01bf\3\2\2\2")
        buf.write("\u0083\u01c4\3\2\2\2\u0085\u01c6\3\2\2\2\u0087\u01d1\3")
        buf.write("\2\2\2\u0089\u01d7\3\2\2\2\u008b\u01e2\3\2\2\2\u008d\u01f1")
        buf.write("\3\2\2\2\u008f\u01fd\3\2\2\2\u0091\u020e\3\2\2\2\u0093")
        buf.write("\u0094\7x\2\2\u0094\u0095\7q\2\2\u0095\u0096\7v\2\2\u0096")
        buf.write("\u0097\7k\2\2\u0097\u0098\7g\2\2\u0098\u0099\7p\2\2\u0099")
        buf.write("\4\3\2\2\2\u009a\u009b\7k\2\2\u009b\u009c\7h\2\2\u009c")
        buf.write("\6\3\2\2\2\u009d\u009e\7g\2\2\u009e\u009f\7n\2\2\u009f")
        buf.write("\u00a0\7u\2\2\u00a0\u00a1\7g\2\2\u00a1\b\3\2\2\2\u00a2")
        buf.write("\u00a3\7h\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5\7t\2\2\u00a5")
        buf.write("\n\3\2\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7g\2\2\u00a8")
        buf.write("\u00a9\7v\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab\7t\2\2\u00ab")
        buf.write("\u00ac\7p\2\2\u00ac\f\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae")
        buf.write("\u00af\7w\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7e\2\2\u00b1")
        buf.write("\16\3\2\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7{\2\2\u00b4")
        buf.write("\u00b5\7r\2\2\u00b5\u00b6\7g\2\2\u00b6\20\3\2\2\2\u00b7")
        buf.write("\u00b8\7u\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7t\2\2\u00ba")
        buf.write("\u00bb\7w\2\2\u00bb\u00bc\7e\2\2\u00bc\u00bd\7v\2\2\u00bd")
        buf.write("\22\3\2\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0")
        buf.write("\u00c1\7v\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\7t\2\2\u00c3")
        buf.write("\u00c4\7h\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6\7e\2\2\u00c6")
        buf.write("\u00c7\7g\2\2\u00c7\24\3\2\2\2\u00c8\u00c9\7u\2\2\u00c9")
        buf.write("\u00ca\7v\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7k\2\2\u00cc")
        buf.write("\u00cd\7p\2\2\u00cd\u00ce\7i\2\2\u00ce\26\3\2\2\2\u00cf")
        buf.write("\u00d0\7k\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7v\2\2\u00d2")
        buf.write("\30\3\2\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5\7n\2\2\u00d5")
        buf.write("\u00d6\7q\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7v\2\2\u00d8")
        buf.write("\32\3\2\2\2\u00d9\u00da\7d\2\2\u00da\u00db\7q\2\2\u00db")
        buf.write("\u00dc\7q\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7g\2\2\u00de")
        buf.write("\u00df\7c\2\2\u00df\u00e0\7p\2\2\u00e0\34\3\2\2\2\u00e1")
        buf.write("\u00e2\7e\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7p\2\2\u00e4")
        buf.write("\u00e5\7u\2\2\u00e5\u00e6\7v\2\2\u00e6\36\3\2\2\2\u00e7")
        buf.write("\u00e8\7x\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea\7t\2\2\u00ea")
        buf.write(" \3\2\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed\7q\2\2\u00ed")
        buf.write("\u00ee\7p\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7k\2\2\u00f0")
        buf.write("\u00f1\7p\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3\7g\2\2\u00f3")
        buf.write("\"\3\2\2\2\u00f4\u00f5\7d\2\2\u00f5\u00f6\7t\2\2\u00f6")
        buf.write("\u00f7\7g\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7m\2\2\u00f9")
        buf.write("$\3\2\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7c\2\2\u00fc")
        buf.write("\u00fd\7p\2\2\u00fd\u00fe\7i\2\2\u00fe\u00ff\7g\2\2\u00ff")
        buf.write("&\3\2\2\2\u0100\u0101\7p\2\2\u0101\u0102\7k\2\2\u0102")
        buf.write("\u0103\7n\2\2\u0103(\3\2\2\2\u0104\u0105\7v\2\2\u0105")
        buf.write("\u0106\7t\2\2\u0106\u0107\7w\2\2\u0107\u0108\7g\2\2\u0108")
        buf.write("*\3\2\2\2\u0109\u010a\7h\2\2\u010a\u010b\7c\2\2\u010b")
        buf.write("\u010c\7n\2\2\u010c\u010d\7u\2\2\u010d\u010e\7g\2\2\u010e")
        buf.write(",\3\2\2\2\u010f\u0110\7-\2\2\u0110.\3\2\2\2\u0111\u0112")
        buf.write("\7/\2\2\u0112\60\3\2\2\2\u0113\u0114\7,\2\2\u0114\62\3")
        buf.write("\2\2\2\u0115\u0116\7\61\2\2\u0116\64\3\2\2\2\u0117\u0118")
        buf.write("\7\'\2\2\u0118\66\3\2\2\2\u0119\u011a\7?\2\2\u011a\u011b")
        buf.write("\7?\2\2\u011b8\3\2\2\2\u011c\u011d\7#\2\2\u011d\u011e")
        buf.write("\7?\2\2\u011e:\3\2\2\2\u011f\u0120\7>\2\2\u0120<\3\2\2")
        buf.write("\2\u0121\u0122\7>\2\2\u0122\u0123\7?\2\2\u0123>\3\2\2")
        buf.write("\2\u0124\u0125\7@\2\2\u0125@\3\2\2\2\u0126\u0127\7@\2")
        buf.write("\2\u0127\u0128\7?\2\2\u0128B\3\2\2\2\u0129\u012a\7(\2")
        buf.write("\2\u012a\u012b\7(\2\2\u012bD\3\2\2\2\u012c\u012d\7~\2")
        buf.write("\2\u012d\u012e\7~\2\2\u012eF\3\2\2\2\u012f\u0130\7#\2")
        buf.write("\2\u0130H\3\2\2\2\u0131\u0132\7?\2\2\u0132J\3\2\2\2\u0133")
        buf.write("\u0134\7-\2\2\u0134\u0135\7?\2\2\u0135L\3\2\2\2\u0136")
        buf.write("\u0137\7/\2\2\u0137\u0138\7?\2\2\u0138N\3\2\2\2\u0139")
        buf.write("\u013a\7,\2\2\u013a\u013b\7?\2\2\u013bP\3\2\2\2\u013c")
        buf.write("\u013d\7\61\2\2\u013d\u013e\7?\2\2\u013eR\3\2\2\2\u013f")
        buf.write("\u0140\7\'\2\2\u0140\u0141\7?\2\2\u0141T\3\2\2\2\u0142")
        buf.write("\u0143\7\60\2\2\u0143V\3\2\2\2\u0144\u0145\7*\2\2\u0145")
        buf.write("X\3\2\2\2\u0146\u0147\7+\2\2\u0147Z\3\2\2\2\u0148\u0149")
        buf.write("\7}\2\2\u0149\\\3\2\2\2\u014a\u014b\7\177\2\2\u014b^\3")
        buf.write("\2\2\2\u014c\u014d\7]\2\2\u014d`\3\2\2\2\u014e\u014f\7")
        buf.write("_\2\2\u014fb\3\2\2\2\u0150\u0151\7.\2\2\u0151d\3\2\2\2")
        buf.write("\u0152\u0153\7=\2\2\u0153f\3\2\2\2\u0154\u0158\t\2\2\2")
        buf.write("\u0155\u0157\t\3\2\2\u0156\u0155\3\2\2\2\u0157\u015a\3")
        buf.write("\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159h")
        buf.write("\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015c\t\4\2\2\u015c")
        buf.write("j\3\2\2\2\u015d\u015e\t\5\2\2\u015el\3\2\2\2\u015f\u0160")
        buf.write("\7\62\2\2\u0160\u0164\7q\2\2\u0161\u0162\7\62\2\2\u0162")
        buf.write("\u0164\7Q\2\2\u0163\u015f\3\2\2\2\u0163\u0161\3\2\2\2")
        buf.write("\u0164\u0166\3\2\2\2\u0165\u0167\t\5\2\2\u0166\u0165\3")
        buf.write("\2\2\2\u0167\u0168\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169n\3\2\2\2\u016a\u016b\t\6\2\2\u016bp\3\2")
        buf.write("\2\2\u016c\u016d\7\62\2\2\u016d\u0171\7z\2\2\u016e\u016f")
        buf.write("\7\62\2\2\u016f\u0171\7Z\2\2\u0170\u016c\3\2\2\2\u0170")
        buf.write("\u016e\3\2\2\2\u0171\u0173\3\2\2\2\u0172\u0174\t\6\2\2")
        buf.write("\u0173\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0173\3")
        buf.write("\2\2\2\u0175\u0176\3\2\2\2\u0176r\3\2\2\2\u0177\u0180")
        buf.write("\7\62\2\2\u0178\u017c\t\7\2\2\u0179\u017b\t\4\2\2\u017a")
        buf.write("\u0179\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3")
        buf.write("\2\2\2\u017f\u0177\3\2\2\2\u017f\u0178\3\2\2\2\u0180t")
        buf.write("\3\2\2\2\u0181\u0185\7\60\2\2\u0182\u0184\t\4\2\2\u0183")
        buf.write("\u0182\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0183\3\2\2\2")
        buf.write("\u0185\u0186\3\2\2\2\u0186v\3\2\2\2\u0187\u0185\3\2\2")
        buf.write("\2\u0188\u0189\t\b\2\2\u0189x\3\2\2\2\u018a\u018b\7\62")
        buf.write("\2\2\u018b\u018f\7d\2\2\u018c\u018d\7\62\2\2\u018d\u018f")
        buf.write("\7D\2\2\u018e\u018a\3\2\2\2\u018e\u018c\3\2\2\2\u018f")
        buf.write("\u0191\3\2\2\2\u0190\u0192\t\b\2\2\u0191\u0190\3\2\2\2")
        buf.write("\u0192\u0193\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3")
        buf.write("\2\2\2\u0194z\3\2\2\2\u0195\u0197\t\t\2\2\u0196\u0198")
        buf.write("\t\n\2\2\u0197\u0196\3\2\2\2\u0197\u0198\3\2\2\2\u0198")
        buf.write("\u019a\3\2\2\2\u0199\u019b\t\4\2\2\u019a\u0199\3\2\2\2")
        buf.write("\u019b\u019c\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3")
        buf.write("\2\2\2\u019d|\3\2\2\2\u019e\u01a9\5s:\2\u019f\u01a0\5")
        buf.write("q9\2\u01a0\u01a1\b?\2\2\u01a1\u01a9\3\2\2\2\u01a2\u01a3")
        buf.write("\5m\67\2\u01a3\u01a4\b?\3\2\u01a4\u01a9\3\2\2\2\u01a5")
        buf.write("\u01a6\5y=\2\u01a6\u01a7\b?\4\2\u01a7\u01a9\3\2\2\2\u01a8")
        buf.write("\u019e\3\2\2\2\u01a8\u019f\3\2\2\2\u01a8\u01a2\3\2\2\2")
        buf.write("\u01a8\u01a5\3\2\2\2\u01a9~\3\2\2\2\u01aa\u01ac\t\4\2")
        buf.write("\2\u01ab\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ab")
        buf.write("\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af\3\2\2\2\u01af")
        buf.write("\u01b1\5u;\2\u01b0\u01b2\5{>\2\u01b1\u01b0\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01be\3\2\2\2\u01b3\u01b5\5u;\2\u01b4")
        buf.write("\u01b6\5{>\2\u01b5\u01b4\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write("\u01be\3\2\2\2\u01b7\u01b9\t\4\2\2\u01b8\u01b7\3\2\2\2")
        buf.write("\u01b9\u01ba\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3")
        buf.write("\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be\5{>\2\u01bd\u01ab")
        buf.write("\3\2\2\2\u01bd\u01b3\3\2\2\2\u01bd\u01b8\3\2\2\2\u01be")
        buf.write("\u0080\3\2\2\2\u01bf\u01c0\t\13\2\2\u01c0\u0082\3\2\2")
        buf.write("\2\u01c1\u01c5\n\f\2\2\u01c2\u01c3\7^\2\2\u01c3\u01c5")
        buf.write("\5\u0081A\2\u01c4\u01c1\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5")
        buf.write("\u0084\3\2\2\2\u01c6\u01ca\7$\2\2\u01c7\u01c9\5\u0083")
        buf.write("B\2\u01c8\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc")
        buf.write("\u01ca\3\2\2\2\u01cd\u01ce\7$\2\2\u01ce\u01cf\bC\5\2\u01cf")
        buf.write("\u0086\3\2\2\2\u01d0\u01d2\t\r\2\2\u01d1\u01d0\3\2\2\2")
        buf.write("\u01d2\u01d3\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3")
        buf.write("\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6\bD\6\2\u01d6\u0088")
        buf.write("\3\2\2\2\u01d7\u01d8\7\61\2\2\u01d8\u01d9\7\61\2\2\u01d9")
        buf.write("\u01dd\3\2\2\2\u01da\u01dc\n\16\2\2\u01db\u01da\3\2\2")
        buf.write("\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de")
        buf.write("\3\2\2\2\u01de\u01e0\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0")
        buf.write("\u01e1\bE\6\2\u01e1\u008a\3\2\2\2\u01e2\u01e3\7\61\2\2")
        buf.write("\u01e3\u01e4\7,\2\2\u01e4\u01e9\3\2\2\2\u01e5\u01e8\5")
        buf.write("\u008bF\2\u01e6\u01e8\13\2\2\2\u01e7\u01e5\3\2\2\2\u01e7")
        buf.write("\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01ea\3\2\2\2")
        buf.write("\u01e9\u01e7\3\2\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01e9\3")
        buf.write("\2\2\2\u01ec\u01ed\7,\2\2\u01ed\u01ee\7\61\2\2\u01ee\u01ef")
        buf.write("\3\2\2\2\u01ef\u01f0\bF\6\2\u01f0\u008c\3\2\2\2\u01f1")
        buf.write("\u01f5\7$\2\2\u01f2\u01f4\5\u0083B\2\u01f3\u01f2\3\2\2")
        buf.write("\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6")
        buf.write("\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8")
        buf.write("\u01fa\t\17\2\2\u01f9\u01f8\3\2\2\2\u01fa\u01fb\3\2\2")
        buf.write("\2\u01fb\u01fc\bG\7\2\u01fc\u008e\3\2\2\2\u01fd\u0201")
        buf.write("\7$\2\2\u01fe\u0200\5\u0083B\2\u01ff\u01fe\3\2\2\2\u0200")
        buf.write("\u0203\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2")
        buf.write("\u0202\u0204\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u0205\7")
        buf.write("^\2\2\u0205\u0209\n\13\2\2\u0206\u0208\5\u0083B\2\u0207")
        buf.write("\u0206\3\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207\3\2\2\2")
        buf.write("\u0209\u020a\3\2\2\2\u020a\u020c\3\2\2\2\u020b\u0209\3")
        buf.write("\2\2\2\u020c\u020d\bH\b\2\u020d\u0090\3\2\2\2\u020e\u020f")
        buf.write("\13\2\2\2\u020f\u0210\bI\t\2\u0210\u0092\3\2\2\2\37\2")
        buf.write("\u0158\u0163\u0168\u0170\u0175\u017c\u017f\u0185\u018e")
        buf.write("\u0193\u0197\u019c\u01a8\u01ad\u01b1\u01b5\u01ba\u01bd")
        buf.write("\u01c4\u01ca\u01d3\u01dd\u01e7\u01e9\u01f5\u01f9\u0201")
        buf.write("\u0209\n\3?\2\3?\3\3?\4\3C\5\b\2\2\3G\6\3H\7\3I\b")
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
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
            "GREATER", "GREATER_OR_EQUAL", "AND", "OR", "NOT", "ASSIGN", 
            "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
            "DOT", "LP", "RP", "LB", "RB", "LSB", "RSB", "COMMA", "SEMI", 
            "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", "LINE_COMMENT", 
            "BLOCK_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
                  "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
                  "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "LP", 
                  "RP", "LB", "RB", "LSB", "RSB", "COMMA", "SEMI", "ID", 
                  "DIGIT", "OCTAL_DIGIT", "OCTAL", "HEX_DIGIT", "HEX", "DECIMAL", 
                  "DECIMAL_PART", "BINARY_DIGIT", "BINARY", "EXPONENT", 
                  "INT_LIT", "FLOAT_LIT", "ESC_CHAR", "STR_CHAR", "STRING_LIT", 
                  "WS", "LINE_COMMENT", "BLOCK_COMMENT", "UNCLOSE_STRING", 
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
     



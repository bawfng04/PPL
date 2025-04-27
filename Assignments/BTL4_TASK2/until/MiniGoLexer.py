# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
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
        buf.write("\u01d5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3")
        buf.write("*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\64\3\64\5\64\u0141\n\64\3\64")
        buf.write("\3\64\5\64\u0145\n\64\3\65\3\65\7\65\u0149\n\65\f\65\16")
        buf.write("\65\u014c\13\65\3\66\3\66\7\66\u0150\n\66\f\66\16\66\u0153")
        buf.write("\13\66\3\66\3\66\3\66\3\66\6\66\u0159\n\66\r\66\16\66")
        buf.write("\u015a\3\66\3\66\3\66\6\66\u0160\n\66\r\66\16\66\u0161")
        buf.write("\3\66\3\66\3\66\6\66\u0167\n\66\r\66\16\66\u0168\5\66")
        buf.write("\u016b\n\66\3\67\6\67\u016e\n\67\r\67\16\67\u016f\3\67")
        buf.write("\3\67\7\67\u0174\n\67\f\67\16\67\u0177\13\67\3\67\3\67")
        buf.write("\5\67\u017b\n\67\3\67\6\67\u017e\n\67\r\67\16\67\u017f")
        buf.write("\5\67\u0182\n\67\38\38\38\38\78\u0188\n8\f8\168\u018b")
        buf.write("\138\38\38\39\39\59\u0191\n9\3:\3:\3;\3;\3;\3;\7;\u0199")
        buf.write("\n;\f;\16;\u019c\13;\3;\3;\3<\3<\3<\3<\3<\7<\u01a5\n<")
        buf.write("\f<\16<\u01a8\13<\3<\3<\3<\3<\3<\3=\6=\u01b0\n=\r=\16")
        buf.write("=\u01b1\3=\3=\3>\3>\3>\3?\3?\3?\3?\7?\u01bd\n?\f?\16?")
        buf.write("\u01c0\13?\3?\3?\3?\5?\u01c5\n?\3?\3?\3@\3@\3@\3@\7@\u01cd")
        buf.write("\n@\f@\16@\u01d0\13@\3@\3@\3@\3@\3\u01a6\2A\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}")
        buf.write("@\177A\3\2\23\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62")
        buf.write(";\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CH")
        buf.write("ch\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\7\2$$^^ppttvv\3\2")
        buf.write("\f\f\5\2\13\13\16\17\"\"\3\3\f\f\2\u01f0\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\3\u0081\3\2\2\2\5\u0084\3\2\2\2\7")
        buf.write("\u0089\3\2\2\2\t\u008d\3\2\2\2\13\u0094\3\2\2\2\r\u0099")
        buf.write("\3\2\2\2\17\u009e\3\2\2\2\21\u00a5\3\2\2\2\23\u00af\3")
        buf.write("\2\2\2\25\u00b6\3\2\2\2\27\u00ba\3\2\2\2\31\u00c0\3\2")
        buf.write("\2\2\33\u00c8\3\2\2\2\35\u00ce\3\2\2\2\37\u00d2\3\2\2")
        buf.write("\2!\u00db\3\2\2\2#\u00e1\3\2\2\2%\u00e7\3\2\2\2\'\u00eb")
        buf.write("\3\2\2\2)\u00f0\3\2\2\2+\u00f6\3\2\2\2-\u00f8\3\2\2\2")
        buf.write("/\u00fa\3\2\2\2\61\u00fc\3\2\2\2\63\u00fe\3\2\2\2\65\u0100")
        buf.write("\3\2\2\2\67\u0103\3\2\2\29\u0106\3\2\2\2;\u0108\3\2\2")
        buf.write("\2=\u010b\3\2\2\2?\u010d\3\2\2\2A\u0110\3\2\2\2C\u0113")
        buf.write("\3\2\2\2E\u0116\3\2\2\2G\u0118\3\2\2\2I\u011a\3\2\2\2")
        buf.write("K\u011d\3\2\2\2M\u0120\3\2\2\2O\u0123\3\2\2\2Q\u0126\3")
        buf.write("\2\2\2S\u0129\3\2\2\2U\u012c\3\2\2\2W\u012e\3\2\2\2Y\u0130")
        buf.write("\3\2\2\2[\u0132\3\2\2\2]\u0134\3\2\2\2_\u0136\3\2\2\2")
        buf.write("a\u0138\3\2\2\2c\u013a\3\2\2\2e\u013c\3\2\2\2g\u0144\3")
        buf.write("\2\2\2i\u0146\3\2\2\2k\u016a\3\2\2\2m\u016d\3\2\2\2o\u0183")
        buf.write("\3\2\2\2q\u0190\3\2\2\2s\u0192\3\2\2\2u\u0194\3\2\2\2")
        buf.write("w\u019f\3\2\2\2y\u01af\3\2\2\2{\u01b5\3\2\2\2}\u01b8\3")
        buf.write("\2\2\2\177\u01c8\3\2\2\2\u0081\u0082\7k\2\2\u0082\u0083")
        buf.write("\7h\2\2\u0083\4\3\2\2\2\u0084\u0085\7g\2\2\u0085\u0086")
        buf.write("\7n\2\2\u0086\u0087\7u\2\2\u0087\u0088\7g\2\2\u0088\6")
        buf.write("\3\2\2\2\u0089\u008a\7h\2\2\u008a\u008b\7q\2\2\u008b\u008c")
        buf.write("\7t\2\2\u008c\b\3\2\2\2\u008d\u008e\7t\2\2\u008e\u008f")
        buf.write("\7g\2\2\u008f\u0090\7v\2\2\u0090\u0091\7w\2\2\u0091\u0092")
        buf.write("\7t\2\2\u0092\u0093\7p\2\2\u0093\n\3\2\2\2\u0094\u0095")
        buf.write("\7h\2\2\u0095\u0096\7w\2\2\u0096\u0097\7p\2\2\u0097\u0098")
        buf.write("\7e\2\2\u0098\f\3\2\2\2\u0099\u009a\7v\2\2\u009a\u009b")
        buf.write("\7{\2\2\u009b\u009c\7r\2\2\u009c\u009d\7g\2\2\u009d\16")
        buf.write("\3\2\2\2\u009e\u009f\7u\2\2\u009f\u00a0\7v\2\2\u00a0\u00a1")
        buf.write("\7t\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3\7e\2\2\u00a3\u00a4")
        buf.write("\7v\2\2\u00a4\20\3\2\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa")
        buf.write("\7t\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad")
        buf.write("\7e\2\2\u00ad\u00ae\7g\2\2\u00ae\22\3\2\2\2\u00af\u00b0")
        buf.write("\7u\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3")
        buf.write("\7k\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7i\2\2\u00b5\24")
        buf.write("\3\2\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9")
        buf.write("\7v\2\2\u00b9\26\3\2\2\2\u00ba\u00bb\7h\2\2\u00bb\u00bc")
        buf.write("\7n\2\2\u00bc\u00bd\7q\2\2\u00bd\u00be\7c\2\2\u00be\u00bf")
        buf.write("\7v\2\2\u00bf\30\3\2\2\2\u00c0\u00c1\7d\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7n\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7\7p\2\2\u00c7\32")
        buf.write("\3\2\2\2\u00c8\u00c9\7e\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb")
        buf.write("\7p\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd\7v\2\2\u00cd\34")
        buf.write("\3\2\2\2\u00ce\u00cf\7x\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1")
        buf.write("\7t\2\2\u00d1\36\3\2\2\2\u00d2\u00d3\7e\2\2\u00d3\u00d4")
        buf.write("\7q\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6\7v\2\2\u00d6\u00d7")
        buf.write("\7k\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9\7w\2\2\u00d9\u00da")
        buf.write("\7g\2\2\u00da \3\2\2\2\u00db\u00dc\7d\2\2\u00dc\u00dd")
        buf.write("\7t\2\2\u00dd\u00de\7g\2\2\u00de\u00df\7c\2\2\u00df\u00e0")
        buf.write("\7m\2\2\u00e0\"\3\2\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3")
        buf.write("\7c\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7i\2\2\u00e5\u00e6")
        buf.write("\7g\2\2\u00e6$\3\2\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9")
        buf.write("\7k\2\2\u00e9\u00ea\7n\2\2\u00ea&\3\2\2\2\u00eb\u00ec")
        buf.write("\7v\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7w\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef(\3\2\2\2\u00f0\u00f1\7h\2\2\u00f1\u00f2")
        buf.write("\7c\2\2\u00f2\u00f3\7n\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5")
        buf.write("\7g\2\2\u00f5*\3\2\2\2\u00f6\u00f7\7-\2\2\u00f7,\3\2\2")
        buf.write("\2\u00f8\u00f9\7/\2\2\u00f9.\3\2\2\2\u00fa\u00fb\7,\2")
        buf.write("\2\u00fb\60\3\2\2\2\u00fc\u00fd\7\61\2\2\u00fd\62\3\2")
        buf.write("\2\2\u00fe\u00ff\7\'\2\2\u00ff\64\3\2\2\2\u0100\u0101")
        buf.write("\7?\2\2\u0101\u0102\7?\2\2\u0102\66\3\2\2\2\u0103\u0104")
        buf.write("\7#\2\2\u0104\u0105\7?\2\2\u01058\3\2\2\2\u0106\u0107")
        buf.write("\7>\2\2\u0107:\3\2\2\2\u0108\u0109\7>\2\2\u0109\u010a")
        buf.write("\7?\2\2\u010a<\3\2\2\2\u010b\u010c\7@\2\2\u010c>\3\2\2")
        buf.write("\2\u010d\u010e\7@\2\2\u010e\u010f\7?\2\2\u010f@\3\2\2")
        buf.write("\2\u0110\u0111\7(\2\2\u0111\u0112\7(\2\2\u0112B\3\2\2")
        buf.write("\2\u0113\u0114\7~\2\2\u0114\u0115\7~\2\2\u0115D\3\2\2")
        buf.write("\2\u0116\u0117\7#\2\2\u0117F\3\2\2\2\u0118\u0119\7?\2")
        buf.write("\2\u0119H\3\2\2\2\u011a\u011b\7<\2\2\u011b\u011c\7?\2")
        buf.write("\2\u011cJ\3\2\2\2\u011d\u011e\7-\2\2\u011e\u011f\7?\2")
        buf.write("\2\u011fL\3\2\2\2\u0120\u0121\7/\2\2\u0121\u0122\7?\2")
        buf.write("\2\u0122N\3\2\2\2\u0123\u0124\7,\2\2\u0124\u0125\7?\2")
        buf.write("\2\u0125P\3\2\2\2\u0126\u0127\7\61\2\2\u0127\u0128\7?")
        buf.write("\2\2\u0128R\3\2\2\2\u0129\u012a\7\'\2\2\u012a\u012b\7")
        buf.write("?\2\2\u012bT\3\2\2\2\u012c\u012d\7\60\2\2\u012dV\3\2\2")
        buf.write("\2\u012e\u012f\7*\2\2\u012fX\3\2\2\2\u0130\u0131\7+\2")
        buf.write("\2\u0131Z\3\2\2\2\u0132\u0133\7}\2\2\u0133\\\3\2\2\2\u0134")
        buf.write("\u0135\7\177\2\2\u0135^\3\2\2\2\u0136\u0137\7]\2\2\u0137")
        buf.write("`\3\2\2\2\u0138\u0139\7_\2\2\u0139b\3\2\2\2\u013a\u013b")
        buf.write("\7.\2\2\u013bd\3\2\2\2\u013c\u013d\7<\2\2\u013df\3\2\2")
        buf.write("\2\u013e\u0145\7=\2\2\u013f\u0141\7\17\2\2\u0140\u013f")
        buf.write("\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\3\2\2\2\u0142")
        buf.write("\u0143\7\f\2\2\u0143\u0145\b\64\2\2\u0144\u013e\3\2\2")
        buf.write("\2\u0144\u0140\3\2\2\2\u0145h\3\2\2\2\u0146\u014a\t\2")
        buf.write("\2\2\u0147\u0149\t\3\2\2\u0148\u0147\3\2\2\2\u0149\u014c")
        buf.write("\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b")
        buf.write("j\3\2\2\2\u014c\u014a\3\2\2\2\u014d\u0151\t\4\2\2\u014e")
        buf.write("\u0150\t\5\2\2\u014f\u014e\3\2\2\2\u0150\u0153\3\2\2\2")
        buf.write("\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u016b\3")
        buf.write("\2\2\2\u0153\u0151\3\2\2\2\u0154\u016b\7\62\2\2\u0155")
        buf.write("\u0156\7\62\2\2\u0156\u0158\t\6\2\2\u0157\u0159\t\7\2")
        buf.write("\2\u0158\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u016b\3\2\2\2\u015c")
        buf.write("\u015d\7\62\2\2\u015d\u015f\t\b\2\2\u015e\u0160\t\t\2")
        buf.write("\2\u015f\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u015f")
        buf.write("\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u016b\3\2\2\2\u0163")
        buf.write("\u0164\7\62\2\2\u0164\u0166\t\n\2\2\u0165\u0167\t\13\2")
        buf.write("\2\u0166\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0166")
        buf.write("\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016b\3\2\2\2\u016a")
        buf.write("\u014d\3\2\2\2\u016a\u0154\3\2\2\2\u016a\u0155\3\2\2\2")
        buf.write("\u016a\u015c\3\2\2\2\u016a\u0163\3\2\2\2\u016bl\3\2\2")
        buf.write("\2\u016c\u016e\t\5\2\2\u016d\u016c\3\2\2\2\u016e\u016f")
        buf.write("\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170")
        buf.write("\u0171\3\2\2\2\u0171\u0175\7\60\2\2\u0172\u0174\t\5\2")
        buf.write("\2\u0173\u0172\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173")
        buf.write("\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0181\3\2\2\2\u0177")
        buf.write("\u0175\3\2\2\2\u0178\u017a\t\f\2\2\u0179\u017b\t\r\2\2")
        buf.write("\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017d\3")
        buf.write("\2\2\2\u017c\u017e\t\5\2\2\u017d\u017c\3\2\2\2\u017e\u017f")
        buf.write("\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0182\3\2\2\2\u0181\u0178\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182n\3\2\2\2\u0183\u0189\7$\2\2\u0184\u0188\n\16\2")
        buf.write("\2\u0185\u0186\7^\2\2\u0186\u0188\t\17\2\2\u0187\u0184")
        buf.write("\3\2\2\2\u0187\u0185\3\2\2\2\u0188\u018b\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c\3\2\2\2")
        buf.write("\u018b\u0189\3\2\2\2\u018c\u018d\7$\2\2\u018dp\3\2\2\2")
        buf.write("\u018e\u0191\5\'\24\2\u018f\u0191\5)\25\2\u0190\u018e")
        buf.write("\3\2\2\2\u0190\u018f\3\2\2\2\u0191r\3\2\2\2\u0192\u0193")
        buf.write("\5%\23\2\u0193t\3\2\2\2\u0194\u0195\7\61\2\2\u0195\u0196")
        buf.write("\7\61\2\2\u0196\u019a\3\2\2\2\u0197\u0199\n\20\2\2\u0198")
        buf.write("\u0197\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2")
        buf.write("\u019a\u019b\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u019a\3")
        buf.write("\2\2\2\u019d\u019e\b;\3\2\u019ev\3\2\2\2\u019f\u01a0\7")
        buf.write("\61\2\2\u01a0\u01a1\7,\2\2\u01a1\u01a6\3\2\2\2\u01a2\u01a5")
        buf.write("\5w<\2\u01a3\u01a5\13\2\2\2\u01a4\u01a2\3\2\2\2\u01a4")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a7\3\2\2\2")
        buf.write("\u01a6\u01a4\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8\u01a6\3")
        buf.write("\2\2\2\u01a9\u01aa\7,\2\2\u01aa\u01ab\7\61\2\2\u01ab\u01ac")
        buf.write("\3\2\2\2\u01ac\u01ad\b<\3\2\u01adx\3\2\2\2\u01ae\u01b0")
        buf.write("\t\21\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\3\2\2\2")
        buf.write("\u01b3\u01b4\b=\4\2\u01b4z\3\2\2\2\u01b5\u01b6\13\2\2")
        buf.write("\2\u01b6\u01b7\b>\5\2\u01b7|\3\2\2\2\u01b8\u01be\7$\2")
        buf.write("\2\u01b9\u01bd\n\16\2\2\u01ba\u01bb\7^\2\2\u01bb\u01bd")
        buf.write("\t\17\2\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd")
        buf.write("\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf\u01c4\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c2\7")
        buf.write("\17\2\2\u01c2\u01c5\7\f\2\2\u01c3\u01c5\t\22\2\2\u01c4")
        buf.write("\u01c1\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c7\b?\6\2\u01c7~\3\2\2\2\u01c8\u01ce\7$\2\2")
        buf.write("\u01c9\u01cd\n\16\2\2\u01ca\u01cb\7^\2\2\u01cb\u01cd\t")
        buf.write("\17\2\2\u01cc\u01c9\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd")
        buf.write("\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2")
        buf.write("\u01cf\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d2\7")
        buf.write("^\2\2\u01d2\u01d3\n\17\2\2\u01d3\u01d4\b@\7\2\u01d4\u0080")
        buf.write("\3\2\2\2\34\2\u0140\u0144\u014a\u0151\u015a\u0161\u0168")
        buf.write("\u016a\u016f\u0175\u017a\u017f\u0181\u0187\u0189\u0190")
        buf.write("\u019a\u01a4\u01a6\u01b1\u01bc\u01be\u01c4\u01cc\u01ce")
        buf.write("\b\3\64\2\b\2\2\3=\3\3>\4\3?\5\3@\6")
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
    EQ = 26
    NE = 27
    LT = 28
    LE = 29
    GT = 30
    GE = 31
    AND = 32
    OR = 33
    NOT = 34
    ASSIGN = 35
    SEMICOLON_ASSIGN = 36
    ADD_ASSIGN = 37
    SUB_ASSIGN = 38
    MUL_ASSIGN = 39
    DIV_ASSIGN = 40
    MOD_ASSIGN = 41
    DOT = 42
    LPAREN = 43
    RPAREN = 44
    LBRACE = 45
    RBRACE = 46
    LBRACK = 47
    RBRACK = 48
    COMMA = 49
    COLON = 50
    SEMICOLON = 51
    ID = 52
    INT_LIT = 53
    FLOAT_LIT = 54
    STRING_LIT = 55
    BOOL_LIT = 56
    NIL_LIT = 57
    COMEMENTS = 58
    COMMENT = 59
    WS = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQ", "NE", "LT", "LE", "GT", "GE", "AND", "OR", 
            "NOT", "ASSIGN", "SEMICOLON_ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
            "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "LPAREN", "RPAREN", 
            "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", "COLON", "SEMICOLON", 
            "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "BOOL_LIT", "NIL_LIT", 
            "COMEMENTS", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "NE", "LT", "LE", 
                  "GT", "GE", "AND", "OR", "NOT", "ASSIGN", "SEMICOLON_ASSIGN", 
                  "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "LBRACK", "RBRACK", "COMMA", "COLON", "SEMICOLON", "ID", 
                  "INT_LIT", "FLOAT_LIT", "STRING_LIT", "BOOL_LIT", "NIL_LIT", 
                  "COMEMENTS", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[50] = self.SEMICOLON_action 
            actions[59] = self.WS_action 
            actions[60] = self.ERROR_CHAR_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def SEMICOLON_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	tk = self.preType;
            	if (tk):
            		list = [self.INT_LIT, self.FLOAT_LIT, self.ID,
            		self.STRING_LIT, self.TRUE, self.NIL_LIT,self.FALSE, self.NIL,
            		self.RETURN, self.CONTINUE, self.BREAK, self.RBRACE, self.RBRACK, self.RPAREN]
            	
            		if tk in list:
            			self.text = ';'
            		else:
            			self.skip()
            	else:
            		self.skip()

     

    def WS_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.skip()
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[:-1])
                else:
                    raise UncloseString(self.text[:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                raise IllegalEscape(self.text)

     



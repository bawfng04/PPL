# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0240\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\5\2t")
        buf.write("\n\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\u0083\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u008b\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0096\n\7\3\b")
        buf.write("\3\b\3\t\3\t\3\t\5\t\u009d\n\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\5\n\u00a6\n\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\5\f\u00b1\n\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00b9\n")
        buf.write("\r\f\r\16\r\u00bc\13\r\3\16\3\16\3\16\3\16\3\16\3\16\7")
        buf.write("\16\u00c4\n\16\f\16\16\16\u00c7\13\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\7\17\u00cf\n\17\f\17\16\17\u00d2\13\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\7\20\u00da\n\20\f\20\16\20")
        buf.write("\u00dd\13\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00e5")
        buf.write("\n\21\f\21\16\21\u00e8\13\21\3\22\3\22\3\22\5\22\u00ed")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00ff\n\23\3\23\7")
        buf.write("\23\u0102\n\23\f\23\16\23\u0105\13\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\5\24\u010e\n\24\3\25\3\25\3\25\5\25")
        buf.write("\u0113\n\25\3\25\3\25\3\26\3\26\3\26\3\26\5\26\u011b\n")
        buf.write("\26\3\27\3\27\3\27\3\27\5\27\u0121\n\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\5\30\u012b\n\30\3\30\3\30\3")
        buf.write("\31\3\31\5\31\u0131\n\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0140\n\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0156")
        buf.write("\n\35\f\35\16\35\u0159\13\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u0161\n\36\3\36\3\36\5\36\u0165\n\36\3\36\5")
        buf.write("\36\u0168\n\36\3\37\3\37\3\37\3\37\5\37\u016e\n\37\3 ")
        buf.write("\3 \3 \5 \u0173\n \3 \3 \3!\3!\3!\3!\3!\3!\3!\5!\u017e")
        buf.write("\n!\3!\3!\3\"\3\"\3\"\5\"\u0185\n\"\3#\3#\3#\3#\5#\u018b")
        buf.write("\n#\3#\3#\3$\3$\3$\5$\u0192\n$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01a5\n%\3%\3%\3&\3&\3")
        buf.write("&\5&\u01ac\n&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3)\3)\3*")
        buf.write("\3*\3*\5*\u01bc\n*\3*\3*\3*\5*\u01c1\n*\3*\3*\3+\3+\5")
        buf.write("+\u01c7\n+\3,\3,\3,\6,\u01cc\n,\r,\16,\u01cd\3,\3,\3-")
        buf.write("\3-\3-\3-\3-\3-\5-\u01d8\n-\3.\3.\3.\3.\5.\u01de\n.\3")
        buf.write(".\3.\5.\u01e2\n.\3.\3.\5.\u01e6\n.\3.\3.\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\5/\u01f2\n/\3/\3/\5/\u01f6\n/\3/\3/\5/\u01fa")
        buf.write("\n/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\5\61\u020c\n\61\3\62\3\62\3")
        buf.write("\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u021f\n\64\3\65\3\65\3\65\5")
        buf.write("\65\u0224\n\65\3\65\3\65\5\65\u0228\n\65\3\66\3\66\3\66")
        buf.write("\3\66\5\66\u022e\n\66\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\5\67\u0238\n\67\38\38\38\38\58\u023e\n8\38\2")
        buf.write("\t\30\32\34\36 $89\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("\2\t\4\2\24\26\679\4\2\13\16\66\66\3\2\34!\3\2\27\30\3")
        buf.write("\2\31\33\4\2\30\30$$\3\2&+\2\u024f\2s\3\2\2\2\4u\3\2\2")
        buf.write("\2\6w\3\2\2\2\b\u0082\3\2\2\2\n\u008a\3\2\2\2\f\u0095")
        buf.write("\3\2\2\2\16\u0097\3\2\2\2\20\u0099\3\2\2\2\22\u00a5\3")
        buf.write("\2\2\2\24\u00a7\3\2\2\2\26\u00b0\3\2\2\2\30\u00b2\3\2")
        buf.write("\2\2\32\u00bd\3\2\2\2\34\u00c8\3\2\2\2\36\u00d3\3\2\2")
        buf.write("\2 \u00de\3\2\2\2\"\u00ec\3\2\2\2$\u00ee\3\2\2\2&\u010d")
        buf.write("\3\2\2\2(\u010f\3\2\2\2*\u011a\3\2\2\2,\u0120\3\2\2\2")
        buf.write(".\u012a\3\2\2\2\60\u0130\3\2\2\2\62\u013f\3\2\2\2\64\u0141")
        buf.write("\3\2\2\2\66\u0146\3\2\2\28\u014a\3\2\2\2:\u015a\3\2\2")
        buf.write("\2<\u016d\3\2\2\2>\u016f\3\2\2\2@\u0176\3\2\2\2B\u0184")
        buf.write("\3\2\2\2D\u0186\3\2\2\2F\u018e\3\2\2\2H\u019b\3\2\2\2")
        buf.write("J\u01a8\3\2\2\2L\u01b0\3\2\2\2N\u01b4\3\2\2\2P\u01b6\3")
        buf.write("\2\2\2R\u01bb\3\2\2\2T\u01c4\3\2\2\2V\u01cb\3\2\2\2X\u01d7")
        buf.write("\3\2\2\2Z\u01d9\3\2\2\2\\\u01e9\3\2\2\2^\u01fd\3\2\2\2")
        buf.write("`\u020b\3\2\2\2b\u020d\3\2\2\2d\u0210\3\2\2\2f\u021e\3")
        buf.write("\2\2\2h\u0220\3\2\2\2j\u022d\3\2\2\2l\u0237\3\2\2\2n\u023d")
        buf.write("\3\2\2\2pt\5\4\3\2qt\5\6\4\2rt\5\20\t\2sp\3\2\2\2sq\3")
        buf.write("\2\2\2sr\3\2\2\2t\3\3\2\2\2uv\t\2\2\2v\5\3\2\2\2wx\5\f")
        buf.write("\7\2xy\5\16\b\2yz\7/\2\2z{\5\b\5\2{|\7\60\2\2|\7\3\2\2")
        buf.write("\2}~\5\n\6\2~\177\7\63\2\2\177\u0080\5\b\5\2\u0080\u0083")
        buf.write("\3\2\2\2\u0081\u0083\5\n\6\2\u0082}\3\2\2\2\u0082\u0081")
        buf.write("\3\2\2\2\u0083\t\3\2\2\2\u0084\u008b\5\20\t\2\u0085\u008b")
        buf.write("\5\4\3\2\u0086\u0087\7/\2\2\u0087\u0088\5\b\5\2\u0088")
        buf.write("\u0089\7\60\2\2\u0089\u008b\3\2\2\2\u008a\u0084\3\2\2")
        buf.write("\2\u008a\u0085\3\2\2\2\u008a\u0086\3\2\2\2\u008b\13\3")
        buf.write("\2\2\2\u008c\u008d\7\61\2\2\u008d\u008e\5\30\r\2\u008e")
        buf.write("\u008f\7\62\2\2\u008f\u0090\5\f\7\2\u0090\u0096\3\2\2")
        buf.write("\2\u0091\u0092\7\61\2\2\u0092\u0093\5\30\r\2\u0093\u0094")
        buf.write("\7\62\2\2\u0094\u0096\3\2\2\2\u0095\u008c\3\2\2\2\u0095")
        buf.write("\u0091\3\2\2\2\u0096\r\3\2\2\2\u0097\u0098\t\3\2\2\u0098")
        buf.write("\17\3\2\2\2\u0099\u009a\7\66\2\2\u009a\u009c\7/\2\2\u009b")
        buf.write("\u009d\5\22\n\2\u009c\u009b\3\2\2\2\u009c\u009d\3\2\2")
        buf.write("\2\u009d\u009e\3\2\2\2\u009e\u009f\7\60\2\2\u009f\21\3")
        buf.write("\2\2\2\u00a0\u00a1\5\24\13\2\u00a1\u00a2\7\63\2\2\u00a2")
        buf.write("\u00a3\5\22\n\2\u00a3\u00a6\3\2\2\2\u00a4\u00a6\5\24\13")
        buf.write("\2\u00a5\u00a0\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\23\3")
        buf.write("\2\2\2\u00a7\u00a8\7\66\2\2\u00a8\u00a9\7\64\2\2\u00a9")
        buf.write("\u00aa\5\30\r\2\u00aa\25\3\2\2\2\u00ab\u00ac\5\30\r\2")
        buf.write("\u00ac\u00ad\7\63\2\2\u00ad\u00ae\5\26\f\2\u00ae\u00b1")
        buf.write("\3\2\2\2\u00af\u00b1\5\30\r\2\u00b0\u00ab\3\2\2\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b1\27\3\2\2\2\u00b2\u00b3\b\r\1\2\u00b3")
        buf.write("\u00b4\5\32\16\2\u00b4\u00ba\3\2\2\2\u00b5\u00b6\f\4\2")
        buf.write("\2\u00b6\u00b7\7#\2\2\u00b7\u00b9\5\32\16\2\u00b8\u00b5")
        buf.write("\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\31\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd")
        buf.write("\u00be\b\16\1\2\u00be\u00bf\5\34\17\2\u00bf\u00c5\3\2")
        buf.write("\2\2\u00c0\u00c1\f\4\2\2\u00c1\u00c2\7\"\2\2\u00c2\u00c4")
        buf.write("\5\34\17\2\u00c3\u00c0\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\33\3\2\2\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c8\u00c9\b\17\1\2\u00c9\u00ca\5\36\20")
        buf.write("\2\u00ca\u00d0\3\2\2\2\u00cb\u00cc\f\4\2\2\u00cc\u00cd")
        buf.write("\t\4\2\2\u00cd\u00cf\5\36\20\2\u00ce\u00cb\3\2\2\2\u00cf")
        buf.write("\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1\35\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d4\b\20")
        buf.write("\1\2\u00d4\u00d5\5 \21\2\u00d5\u00db\3\2\2\2\u00d6\u00d7")
        buf.write("\f\4\2\2\u00d7\u00d8\t\5\2\2\u00d8\u00da\5 \21\2\u00d9")
        buf.write("\u00d6\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\37\3\2\2\2\u00dd\u00db\3\2")
        buf.write("\2\2\u00de\u00df\b\21\1\2\u00df\u00e0\5\"\22\2\u00e0\u00e6")
        buf.write("\3\2\2\2\u00e1\u00e2\f\4\2\2\u00e2\u00e3\t\6\2\2\u00e3")
        buf.write("\u00e5\5\"\22\2\u00e4\u00e1\3\2\2\2\u00e5\u00e8\3\2\2")
        buf.write("\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7!\3\2")
        buf.write("\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea\t\7\2\2\u00ea\u00ed")
        buf.write("\5\"\22\2\u00eb\u00ed\5$\23\2\u00ec\u00e9\3\2\2\2\u00ec")
        buf.write("\u00eb\3\2\2\2\u00ed#\3\2\2\2\u00ee\u00ef\b\23\1\2\u00ef")
        buf.write("\u00f0\5&\24\2\u00f0\u0103\3\2\2\2\u00f1\u00f2\f\6\2\2")
        buf.write("\u00f2\u00f3\7\61\2\2\u00f3\u00f4\5\30\r\2\u00f4\u00f5")
        buf.write("\7\62\2\2\u00f5\u0102\3\2\2\2\u00f6\u00f7\f\5\2\2\u00f7")
        buf.write("\u00f8\7,\2\2\u00f8\u0102\7\66\2\2\u00f9\u00fa\f\4\2\2")
        buf.write("\u00fa\u00fb\7,\2\2\u00fb\u00fc\7\66\2\2\u00fc\u00fe\7")
        buf.write("-\2\2\u00fd\u00ff\5\26\f\2\u00fe\u00fd\3\2\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0102\7.\2\2\u0101")
        buf.write("\u00f1\3\2\2\2\u0101\u00f6\3\2\2\2\u0101\u00f9\3\2\2\2")
        buf.write("\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3")
        buf.write("\2\2\2\u0104%\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u010e")
        buf.write("\7\66\2\2\u0107\u010e\5\2\2\2\u0108\u010e\5(\25\2\u0109")
        buf.write("\u010a\7-\2\2\u010a\u010b\5\30\r\2\u010b\u010c\7.\2\2")
        buf.write("\u010c\u010e\3\2\2\2\u010d\u0106\3\2\2\2\u010d\u0107\3")
        buf.write("\2\2\2\u010d\u0108\3\2\2\2\u010d\u0109\3\2\2\2\u010e\'")
        buf.write("\3\2\2\2\u010f\u0110\7\66\2\2\u0110\u0112\7-\2\2\u0111")
        buf.write("\u0113\5\26\f\2\u0112\u0111\3\2\2\2\u0112\u0113\3\2\2")
        buf.write("\2\u0113\u0114\3\2\2\2\u0114\u0115\7.\2\2\u0115)\3\2\2")
        buf.write("\2\u0116\u011b\5\16\b\2\u0117\u0118\5\f\7\2\u0118\u0119")
        buf.write("\5\16\b\2\u0119\u011b\3\2\2\2\u011a\u0116\3\2\2\2\u011a")
        buf.write("\u0117\3\2\2\2\u011b+\3\2\2\2\u011c\u011d\5.\30\2\u011d")
        buf.write("\u011e\5,\27\2\u011e\u0121\3\2\2\2\u011f\u0121\5.\30\2")
        buf.write("\u0120\u011c\3\2\2\2\u0120\u011f\3\2\2\2\u0121-\3\2\2")
        buf.write("\2\u0122\u012b\5\60\31\2\u0123\u012b\5\66\34\2\u0124\u012b")
        buf.write("\5:\36\2\u0125\u012b\5B\"\2\u0126\u012b\5N(\2\u0127\u012b")
        buf.write("\5P)\2\u0128\u012b\5R*\2\u0129\u012b\5T+\2\u012a\u0122")
        buf.write("\3\2\2\2\u012a\u0123\3\2\2\2\u012a\u0124\3\2\2\2\u012a")
        buf.write("\u0125\3\2\2\2\u012a\u0126\3\2\2\2\u012a\u0127\3\2\2\2")
        buf.write("\u012a\u0128\3\2\2\2\u012a\u0129\3\2\2\2\u012b\u012c\3")
        buf.write("\2\2\2\u012c\u012d\7\65\2\2\u012d/\3\2\2\2\u012e\u0131")
        buf.write("\5\62\32\2\u012f\u0131\5\64\33\2\u0130\u012e\3\2\2\2\u0130")
        buf.write("\u012f\3\2\2\2\u0131\61\3\2\2\2\u0132\u0133\7\20\2\2\u0133")
        buf.write("\u0134\7\66\2\2\u0134\u0140\5*\26\2\u0135\u0136\7\20\2")
        buf.write("\2\u0136\u0137\7\66\2\2\u0137\u0138\7%\2\2\u0138\u0140")
        buf.write("\5\30\r\2\u0139\u013a\7\20\2\2\u013a\u013b\7\66\2\2\u013b")
        buf.write("\u013c\5*\26\2\u013c\u013d\7%\2\2\u013d\u013e\5\30\r\2")
        buf.write("\u013e\u0140\3\2\2\2\u013f\u0132\3\2\2\2\u013f\u0135\3")
        buf.write("\2\2\2\u013f\u0139\3\2\2\2\u0140\63\3\2\2\2\u0141\u0142")
        buf.write("\7\17\2\2\u0142\u0143\7\66\2\2\u0143\u0144\7%\2\2\u0144")
        buf.write("\u0145\5\30\r\2\u0145\65\3\2\2\2\u0146\u0147\58\35\2\u0147")
        buf.write("\u0148\t\b\2\2\u0148\u0149\5\30\r\2\u0149\67\3\2\2\2\u014a")
        buf.write("\u014b\b\35\1\2\u014b\u014c\7\66\2\2\u014c\u0157\3\2\2")
        buf.write("\2\u014d\u014e\f\5\2\2\u014e\u014f\7\61\2\2\u014f\u0150")
        buf.write("\5\30\r\2\u0150\u0151\7\62\2\2\u0151\u0156\3\2\2\2\u0152")
        buf.write("\u0153\f\4\2\2\u0153\u0154\7,\2\2\u0154\u0156\7\66\2\2")
        buf.write("\u0155\u014d\3\2\2\2\u0155\u0152\3\2\2\2\u0156\u0159\3")
        buf.write("\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u01589")
        buf.write("\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015b\7\3\2\2\u015b")
        buf.write("\u015c\7-\2\2\u015c\u015d\5\30\r\2\u015d\u015e\7.\2\2")
        buf.write("\u015e\u0160\7/\2\2\u015f\u0161\5,\27\2\u0160\u015f\3")
        buf.write("\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0164")
        buf.write("\7\60\2\2\u0163\u0165\5<\37\2\u0164\u0163\3\2\2\2\u0164")
        buf.write("\u0165\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0168\5> \2\u0167")
        buf.write("\u0166\3\2\2\2\u0167\u0168\3\2\2\2\u0168;\3\2\2\2\u0169")
        buf.write("\u016a\5@!\2\u016a\u016b\5<\37\2\u016b\u016e\3\2\2\2\u016c")
        buf.write("\u016e\5@!\2\u016d\u0169\3\2\2\2\u016d\u016c\3\2\2\2\u016e")
        buf.write("=\3\2\2\2\u016f\u0170\7\4\2\2\u0170\u0172\7/\2\2\u0171")
        buf.write("\u0173\5,\27\2\u0172\u0171\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174\u0175\7\60\2\2\u0175?\3\2\2")
        buf.write("\2\u0176\u0177\7\4\2\2\u0177\u0178\7\3\2\2\u0178\u0179")
        buf.write("\7-\2\2\u0179\u017a\5\30\r\2\u017a\u017b\7.\2\2\u017b")
        buf.write("\u017d\7/\2\2\u017c\u017e\5,\27\2\u017d\u017c\3\2\2\2")
        buf.write("\u017d\u017e\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\7")
        buf.write("\60\2\2\u0180A\3\2\2\2\u0181\u0185\5D#\2\u0182\u0185\5")
        buf.write("F$\2\u0183\u0185\5H%\2\u0184\u0181\3\2\2\2\u0184\u0182")
        buf.write("\3\2\2\2\u0184\u0183\3\2\2\2\u0185C\3\2\2\2\u0186\u0187")
        buf.write("\7\5\2\2\u0187\u0188\5\30\r\2\u0188\u018a\7/\2\2\u0189")
        buf.write("\u018b\5,\27\2\u018a\u0189\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018b\u018c\3\2\2\2\u018c\u018d\7\60\2\2\u018dE\3\2\2")
        buf.write("\2\u018e\u0191\7\5\2\2\u018f\u0192\5L\'\2\u0190\u0192")
        buf.write("\5J&\2\u0191\u018f\3\2\2\2\u0191\u0190\3\2\2\2\u0192\u0193")
        buf.write("\3\2\2\2\u0193\u0194\7\65\2\2\u0194\u0195\5\30\r\2\u0195")
        buf.write("\u0196\7\65\2\2\u0196\u0197\5L\'\2\u0197\u0198\7/\2\2")
        buf.write("\u0198\u0199\5,\27\2\u0199\u019a\7\60\2\2\u019aG\3\2\2")
        buf.write("\2\u019b\u019c\7\5\2\2\u019c\u019d\7\66\2\2\u019d\u019e")
        buf.write("\7\63\2\2\u019e\u019f\7\66\2\2\u019f\u01a0\7&\2\2\u01a0")
        buf.write("\u01a1\7\23\2\2\u01a1\u01a2\5\30\r\2\u01a2\u01a4\7/\2")
        buf.write("\2\u01a3\u01a5\5,\27\2\u01a4\u01a3\3\2\2\2\u01a4\u01a5")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\7\60\2\2\u01a7")
        buf.write("I\3\2\2\2\u01a8\u01a9\7\20\2\2\u01a9\u01ab\7\66\2\2\u01aa")
        buf.write("\u01ac\5*\26\2\u01ab\u01aa\3\2\2\2\u01ab\u01ac\3\2\2\2")
        buf.write("\u01ac\u01ad\3\2\2\2\u01ad\u01ae\7%\2\2\u01ae\u01af\5")
        buf.write("\30\r\2\u01afK\3\2\2\2\u01b0\u01b1\7\66\2\2\u01b1\u01b2")
        buf.write("\t\b\2\2\u01b2\u01b3\5\30\r\2\u01b3M\3\2\2\2\u01b4\u01b5")
        buf.write("\7\22\2\2\u01b5O\3\2\2\2\u01b6\u01b7\7\21\2\2\u01b7Q\3")
        buf.write("\2\2\2\u01b8\u01b9\58\35\2\u01b9\u01ba\7,\2\2\u01ba\u01bc")
        buf.write("\3\2\2\2\u01bb\u01b8\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01be\7\66\2\2\u01be\u01c0\7-\2\2")
        buf.write("\u01bf\u01c1\5\26\f\2\u01c0\u01bf\3\2\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3\7.\2\2\u01c3")
        buf.write("S\3\2\2\2\u01c4\u01c6\7\6\2\2\u01c5\u01c7\5\30\r\2\u01c6")
        buf.write("\u01c5\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7U\3\2\2\2\u01c8")
        buf.write("\u01c9\5X-\2\u01c9\u01ca\7\65\2\2\u01ca\u01cc\3\2\2\2")
        buf.write("\u01cb\u01c8\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cb\3")
        buf.write("\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0")
        buf.write("\7\2\2\3\u01d0W\3\2\2\2\u01d1\u01d8\5\62\32\2\u01d2\u01d8")
        buf.write("\5\64\33\2\u01d3\u01d8\5Z.\2\u01d4\u01d8\5\\/\2\u01d5")
        buf.write("\u01d8\5^\60\2\u01d6\u01d8\5d\63\2\u01d7\u01d1\3\2\2\2")
        buf.write("\u01d7\u01d2\3\2\2\2\u01d7\u01d3\3\2\2\2\u01d7\u01d4\3")
        buf.write("\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8Y")
        buf.write("\3\2\2\2\u01d9\u01da\7\7\2\2\u01da\u01db\7\66\2\2\u01db")
        buf.write("\u01dd\7-\2\2\u01dc\u01de\5j\66\2\u01dd\u01dc\3\2\2\2")
        buf.write("\u01dd\u01de\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e1\7")
        buf.write(".\2\2\u01e0\u01e2\5*\26\2\u01e1\u01e0\3\2\2\2\u01e1\u01e2")
        buf.write("\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e5\7/\2\2\u01e4")
        buf.write("\u01e6\5,\27\2\u01e5\u01e4\3\2\2\2\u01e5\u01e6\3\2\2\2")
        buf.write("\u01e6\u01e7\3\2\2\2\u01e7\u01e8\7\60\2\2\u01e8[\3\2\2")
        buf.write("\2\u01e9\u01ea\7\7\2\2\u01ea\u01eb\7-\2\2\u01eb\u01ec")
        buf.write("\7\66\2\2\u01ec\u01ed\7\66\2\2\u01ed\u01ee\7.\2\2\u01ee")
        buf.write("\u01ef\7\66\2\2\u01ef\u01f1\7-\2\2\u01f0\u01f2\5j\66\2")
        buf.write("\u01f1\u01f0\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\3")
        buf.write("\2\2\2\u01f3\u01f5\7.\2\2\u01f4\u01f6\5*\26\2\u01f5\u01f4")
        buf.write("\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7")
        buf.write("\u01f9\7/\2\2\u01f8\u01fa\5,\27\2\u01f9\u01f8\3\2\2\2")
        buf.write("\u01f9\u01fa\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fc\7")
        buf.write("\60\2\2\u01fc]\3\2\2\2\u01fd\u01fe\7\b\2\2\u01fe\u01ff")
        buf.write("\7\66\2\2\u01ff\u0200\7\t\2\2\u0200\u0201\7/\2\2\u0201")
        buf.write("\u0202\5`\61\2\u0202\u0203\7\60\2\2\u0203_\3\2\2\2\u0204")
        buf.write("\u0205\5b\62\2\u0205\u0206\7\65\2\2\u0206\u0207\5`\61")
        buf.write("\2\u0207\u020c\3\2\2\2\u0208\u0209\5b\62\2\u0209\u020a")
        buf.write("\7\65\2\2\u020a\u020c\3\2\2\2\u020b\u0204\3\2\2\2\u020b")
        buf.write("\u0208\3\2\2\2\u020ca\3\2\2\2\u020d\u020e\7\66\2\2\u020e")
        buf.write("\u020f\5*\26\2\u020fc\3\2\2\2\u0210\u0211\7\b\2\2\u0211")
        buf.write("\u0212\7\66\2\2\u0212\u0213\7\n\2\2\u0213\u0214\7/\2\2")
        buf.write("\u0214\u0215\5f\64\2\u0215\u0216\7\60\2\2\u0216e\3\2\2")
        buf.write("\2\u0217\u0218\5h\65\2\u0218\u0219\7\65\2\2\u0219\u021a")
        buf.write("\5f\64\2\u021a\u021f\3\2\2\2\u021b\u021c\5h\65\2\u021c")
        buf.write("\u021d\7\65\2\2\u021d\u021f\3\2\2\2\u021e\u0217\3\2\2")
        buf.write("\2\u021e\u021b\3\2\2\2\u021fg\3\2\2\2\u0220\u0221\7\66")
        buf.write("\2\2\u0221\u0223\7-\2\2\u0222\u0224\5j\66\2\u0223\u0222")
        buf.write("\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0225\3\2\2\2\u0225")
        buf.write("\u0227\7.\2\2\u0226\u0228\5*\26\2\u0227\u0226\3\2\2\2")
        buf.write("\u0227\u0228\3\2\2\2\u0228i\3\2\2\2\u0229\u022a\5l\67")
        buf.write("\2\u022a\u022b\5j\66\2\u022b\u022e\3\2\2\2\u022c\u022e")
        buf.write("\5l\67\2\u022d\u0229\3\2\2\2\u022d\u022c\3\2\2\2\u022e")
        buf.write("k\3\2\2\2\u022f\u0230\5n8\2\u0230\u0231\5*\26\2\u0231")
        buf.write("\u0232\7\63\2\2\u0232\u0233\5l\67\2\u0233\u0238\3\2\2")
        buf.write("\2\u0234\u0235\5n8\2\u0235\u0236\5*\26\2\u0236\u0238\3")
        buf.write("\2\2\2\u0237\u022f\3\2\2\2\u0237\u0234\3\2\2\2\u0238m")
        buf.write("\3\2\2\2\u0239\u023a\7\66\2\2\u023a\u023b\7\63\2\2\u023b")
        buf.write("\u023e\5n8\2\u023c\u023e\7\66\2\2\u023d\u0239\3\2\2\2")
        buf.write("\u023d\u023c\3\2\2\2\u023eo\3\2\2\28s\u0082\u008a\u0095")
        buf.write("\u009c\u00a5\u00b0\u00ba\u00c5\u00d0\u00db\u00e6\u00ec")
        buf.write("\u00fe\u0101\u0103\u010d\u0112\u011a\u0120\u012a\u0130")
        buf.write("\u013f\u0155\u0157\u0160\u0164\u0167\u016d\u0172\u017d")
        buf.write("\u0184\u018a\u0191\u01a4\u01ab\u01bb\u01c0\u01c6\u01cd")
        buf.write("\u01d7\u01dd\u01e1\u01e5\u01f1\u01f5\u01f9\u020b\u021e")
        buf.write("\u0223\u0227\u022d\u0237\u023d")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "':='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQ", "NE", "LT", "LE", "GT", "GE", "AND", 
                      "OR", "NOT", "ASSIGN", "SEMICOLON_ASSIGN", "ADD_ASSIGN", 
                      "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "COMMA", "COLON", "SEMICOLON", "ID", "INT_LIT", 
                      "FLOAT_LIT", "STRING_LIT", "BOOL_LIT", "NIL_LIT", 
                      "COMEMENTS", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_literal = 0
    RULE_literal_prim = 1
    RULE_array_literal = 2
    RULE_list_literal_array = 3
    RULE_element_array = 4
    RULE_dimensions = 5
    RULE_type_r = 6
    RULE_struct_literal = 7
    RULE_list_elements = 8
    RULE_element = 9
    RULE_list_expression = 10
    RULE_expression = 11
    RULE_expression1 = 12
    RULE_expression2 = 13
    RULE_expression3 = 14
    RULE_expression4 = 15
    RULE_expression5 = 16
    RULE_expression6 = 17
    RULE_expression7 = 18
    RULE_funtion_call = 19
    RULE_type_minigo = 20
    RULE_list_statement = 21
    RULE_statement = 22
    RULE_declared_statement = 23
    RULE_variables = 24
    RULE_constants = 25
    RULE_assign_statement = 26
    RULE_lhs = 27
    RULE_if_statement = 28
    RULE_list_else_if = 29
    RULE_else_statement = 30
    RULE_else_if = 31
    RULE_for_statement = 32
    RULE_basic_for = 33
    RULE_for_loop = 34
    RULE_for_array = 35
    RULE_variables_for = 36
    RULE_assign_for = 37
    RULE_break_statement = 38
    RULE_continue_statement = 39
    RULE_call_statement = 40
    RULE_return_statement = 41
    RULE_program = 42
    RULE_declared = 43
    RULE_function = 44
    RULE_method = 45
    RULE_struct_type_declared = 46
    RULE_list_fields = 47
    RULE_fields = 48
    RULE_interface_type_declared = 49
    RULE_list_meth_interface = 50
    RULE_meth_interface = 51
    RULE_list_param = 52
    RULE_param = 53
    RULE_list_ID = 54

    ruleNames =  [ "literal", "literal_prim", "array_literal", "list_literal_array", 
                   "element_array", "dimensions", "type_r", "struct_literal", 
                   "list_elements", "element", "list_expression", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "funtion_call", 
                   "type_minigo", "list_statement", "statement", "declared_statement", 
                   "variables", "constants", "assign_statement", "lhs", 
                   "if_statement", "list_else_if", "else_statement", "else_if", 
                   "for_statement", "basic_for", "for_loop", "for_array", 
                   "variables_for", "assign_for", "break_statement", "continue_statement", 
                   "call_statement", "return_statement", "program", "declared", 
                   "function", "method", "struct_type_declared", "list_fields", 
                   "fields", "interface_type_declared", "list_meth_interface", 
                   "meth_interface", "list_param", "param", "list_ID" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQ=26
    NE=27
    LT=28
    LE=29
    GT=30
    GE=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    SEMICOLON_ASSIGN=36
    ADD_ASSIGN=37
    SUB_ASSIGN=38
    MUL_ASSIGN=39
    DIV_ASSIGN=40
    MOD_ASSIGN=41
    DOT=42
    LPAREN=43
    RPAREN=44
    LBRACE=45
    RBRACE=46
    LBRACK=47
    RBRACK=48
    COMMA=49
    COLON=50
    SEMICOLON=51
    ID=52
    INT_LIT=53
    FLOAT_LIT=54
    STRING_LIT=55
    BOOL_LIT=56
    NIL_LIT=57
    COMEMENTS=58
    COMMENT=59
    WS=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_prim(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_primContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_literal)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.literal_prim()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.struct_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_primContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_prim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_prim" ):
                return visitor.visitLiteral_prim(self)
            else:
                return visitor.visitChildren(self)




    def literal_prim(self):

        localctx = MiniGoParser.Literal_primContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literal_prim)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def type_r(self):
            return self.getTypedRuleContext(MiniGoParser.Type_rContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_literal_array(self):
            return self.getTypedRuleContext(MiniGoParser.List_literal_arrayContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.dimensions()
            self.state = 118
            self.type_r()
            self.state = 119
            self.match(MiniGoParser.LBRACE)
            self.state = 120
            self.list_literal_array()
            self.state = 121
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literal_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_array(self):
            return self.getTypedRuleContext(MiniGoParser.Element_arrayContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_literal_array(self):
            return self.getTypedRuleContext(MiniGoParser.List_literal_arrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_literal_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal_array" ):
                return visitor.visitList_literal_array(self)
            else:
                return visitor.visitChildren(self)




    def list_literal_array(self):

        localctx = MiniGoParser.List_literal_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list_literal_array)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.element_array()
                self.state = 124
                self.match(MiniGoParser.COMMA)
                self.state = 125
                self.list_literal_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.element_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def literal_prim(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_primContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_literal_array(self):
            return self.getTypedRuleContext(MiniGoParser.List_literal_arrayContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_element_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_array" ):
                return visitor.visitElement_array(self)
            else:
                return visitor.visitChildren(self)




    def element_array(self):

        localctx = MiniGoParser.Element_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_element_array)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.struct_literal()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.literal_prim()
                pass
            elif token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.match(MiniGoParser.LBRACE)
                self.state = 133
                self.list_literal_array()
                self.state = 134
                self.match(MiniGoParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = MiniGoParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dimensions)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(MiniGoParser.LBRACK)
                self.state = 139
                self.expression(0)
                self.state = 140
                self.match(MiniGoParser.RBRACK)
                self.state = 141
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(MiniGoParser.LBRACK)
                self.state = 144
                self.expression(0)
                self.state = 145
                self.match(MiniGoParser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_rContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_r

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_r" ):
                return visitor.visitType_r(self)
            else:
                return visitor.visitChildren(self)




    def type_r(self):

        localctx = MiniGoParser.Type_rContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type_r)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MiniGoParser.ID)
            self.state = 152
            self.match(MiniGoParser.LBRACE)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 153
                self.list_elements()


            self.state = 156
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(MiniGoParser.ElementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elements" ):
                return visitor.visitList_elements(self)
            else:
                return visitor.visitChildren(self)




    def list_elements(self):

        localctx = MiniGoParser.List_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_elements)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.element()
                self.state = 159
                self.match(MiniGoParser.COMMA)
                self.state = 160
                self.list_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = MiniGoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MiniGoParser.ID)
            self.state = 166
            self.match(MiniGoParser.COLON)
            self.state = 167
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_expression)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.expression(0)
                self.state = 170
                self.match(MiniGoParser.COMMA)
                self.state = 171
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 179
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 180
                    self.match(MiniGoParser.OR)
                    self.state = 181
                    self.expression1(0) 
                self.state = 186
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 190
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 191
                    self.match(MiniGoParser.AND)
                    self.state = 192
                    self.expression2(0) 
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NE(self):
            return self.getToken(MiniGoParser.NE, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 201
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 202
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NE) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 203
                    self.expression3(0) 
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 212
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 213
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 214
                    self.expression4(0) 
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 225
                    self.expression5() 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 232
                self.expression5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.expression6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 255
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 239
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 240
                        self.match(MiniGoParser.LBRACK)
                        self.state = 241
                        self.expression(0)
                        self.state = 242
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 244
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 245
                        self.match(MiniGoParser.DOT)
                        self.state = 246
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 247
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 248
                        self.match(MiniGoParser.DOT)
                        self.state = 249
                        self.match(MiniGoParser.ID)
                        self.state = 250
                        self.match(MiniGoParser.LPAREN)
                        self.state = 252
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                            self.state = 251
                            self.list_expression()


                        self.state = 254
                        self.match(MiniGoParser.RPAREN)
                        pass

             
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def funtion_call(self):
            return self.getTypedRuleContext(MiniGoParser.Funtion_callContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression7)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self.funtion_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 263
                self.match(MiniGoParser.LPAREN)
                self.state = 264
                self.expression(0)
                self.state = 265
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funtion_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funtion_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuntion_call" ):
                return visitor.visitFuntion_call(self)
            else:
                return visitor.visitChildren(self)




    def funtion_call(self):

        localctx = MiniGoParser.Funtion_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_funtion_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(MiniGoParser.ID)
            self.state = 270
            self.match(MiniGoParser.LPAREN)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 271
                self.list_expression()


            self.state = 274
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_minigoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_r(self):
            return self.getTypedRuleContext(MiniGoParser.Type_rContext,0)


        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_minigo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_minigo" ):
                return visitor.visitType_minigo(self)
            else:
                return visitor.visitChildren(self)




    def type_minigo(self):

        localctx = MiniGoParser.Type_minigoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_type_minigo)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.type_r()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.dimensions()
                self.state = 278
                self.type_r()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_statement)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.statement()
                self.state = 283
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 288
                self.declared_statement()
                pass

            elif la_ == 2:
                self.state = 289
                self.assign_statement()
                pass

            elif la_ == 3:
                self.state = 290
                self.if_statement()
                pass

            elif la_ == 4:
                self.state = 291
                self.for_statement()
                pass

            elif la_ == 5:
                self.state = 292
                self.break_statement()
                pass

            elif la_ == 6:
                self.state = 293
                self.continue_statement()
                pass

            elif la_ == 7:
                self.state = 294
                self.call_statement()
                pass

            elif la_ == 8:
                self.state = 295
                self.return_statement()
                pass


            self.state = 298
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(MiniGoParser.VariablesContext,0)


        def constants(self):
            return self.getTypedRuleContext(MiniGoParser.ConstantsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement" ):
                return visitor.visitDeclared_statement(self)
            else:
                return visitor.visitChildren(self)




    def declared_statement(self):

        localctx = MiniGoParser.Declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_declared_statement)
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.variables()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.constants()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_minigo(self):
            return self.getTypedRuleContext(MiniGoParser.Type_minigoContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = MiniGoParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_variables)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(MiniGoParser.VAR)
                self.state = 305
                self.match(MiniGoParser.ID)
                self.state = 306
                self.type_minigo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.match(MiniGoParser.VAR)
                self.state = 308
                self.match(MiniGoParser.ID)

                self.state = 309
                self.match(MiniGoParser.ASSIGN)
                self.state = 310
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
                self.match(MiniGoParser.VAR)
                self.state = 312
                self.match(MiniGoParser.ID)
                self.state = 313
                self.type_minigo()

                self.state = 314
                self.match(MiniGoParser.ASSIGN)
                self.state = 315
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constants

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstants" ):
                return visitor.visitConstants(self)
            else:
                return visitor.visitChildren(self)




    def constants(self):

        localctx = MiniGoParser.ConstantsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_constants)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(MiniGoParser.CONST)
            self.state = 320
            self.match(MiniGoParser.ID)
            self.state = 321
            self.match(MiniGoParser.ASSIGN)
            self.state = 322
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMICOLON_ASSIGN(self):
            return self.getToken(MiniGoParser.SEMICOLON_ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assign_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.lhs(0)
            self.state = 325
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SEMICOLON_ASSIGN) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 326
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 341
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 339
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 331
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 332
                        self.match(MiniGoParser.LBRACK)
                        self.state = 333
                        self.expression(0)
                        self.state = 334
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 336
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 337
                        self.match(MiniGoParser.DOT)
                        self.state = 338
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 343
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def list_else_if(self):
            return self.getTypedRuleContext(MiniGoParser.List_else_ifContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MiniGoParser.IF)
            self.state = 345
            self.match(MiniGoParser.LPAREN)
            self.state = 346
            self.expression(0)
            self.state = 347
            self.match(MiniGoParser.RPAREN)
            self.state = 348
            self.match(MiniGoParser.LBRACE)
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 349
                self.list_statement()


            self.state = 352
            self.match(MiniGoParser.RBRACE)
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 353
                self.list_else_if()


            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 356
                self.else_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_else_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Else_ifContext,0)


        def list_else_if(self):
            return self.getTypedRuleContext(MiniGoParser.List_else_ifContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_else_if" ):
                return visitor.visitList_else_if(self)
            else:
                return visitor.visitChildren(self)




    def list_else_if(self):

        localctx = MiniGoParser.List_else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_list_else_if)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.else_if()
                self.state = 360
                self.list_else_if()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.else_if()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = MiniGoParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MiniGoParser.ELSE)
            self.state = 366
            self.match(MiniGoParser.LBRACE)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 367
                self.list_statement()


            self.state = 370
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if" ):
                return visitor.visitElse_if(self)
            else:
                return visitor.visitChildren(self)




    def else_if(self):

        localctx = MiniGoParser.Else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_else_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(MiniGoParser.ELSE)
            self.state = 373
            self.match(MiniGoParser.IF)
            self.state = 374
            self.match(MiniGoParser.LPAREN)
            self.state = 375
            self.expression(0)
            self.state = 376
            self.match(MiniGoParser.RPAREN)
            self.state = 377
            self.match(MiniGoParser.LBRACE)
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 378
                self.list_statement()


            self.state = 381
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_for(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_forContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(MiniGoParser.For_loopContext,0)


        def for_array(self):
            return self.getTypedRuleContext(MiniGoParser.For_arrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_statement)
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.basic_for()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.for_loop()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 385
                self.for_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_for" ):
                return visitor.visitBasic_for(self)
            else:
                return visitor.visitChildren(self)




    def basic_for(self):

        localctx = MiniGoParser.Basic_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_basic_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(MiniGoParser.FOR)
            self.state = 389
            self.expression(0)
            self.state = 390
            self.match(MiniGoParser.LBRACE)
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 391
                self.list_statement()


            self.state = 394
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def assign_for(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assign_forContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assign_forContext,i)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def variables_for(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = MiniGoParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(MiniGoParser.FOR)
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 397
                self.assign_for()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 398
                self.variables_for()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 401
            self.match(MiniGoParser.SEMICOLON)
            self.state = 402
            self.expression(0)
            self.state = 403
            self.match(MiniGoParser.SEMICOLON)
            self.state = 404
            self.assign_for()
            self.state = 405
            self.match(MiniGoParser.LBRACE)
            self.state = 406
            self.list_statement()
            self.state = 407
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def SEMICOLON_ASSIGN(self):
            return self.getToken(MiniGoParser.SEMICOLON_ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_array" ):
                return visitor.visitFor_array(self)
            else:
                return visitor.visitChildren(self)




    def for_array(self):

        localctx = MiniGoParser.For_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_for_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(MiniGoParser.FOR)
            self.state = 410
            self.match(MiniGoParser.ID)
            self.state = 411
            self.match(MiniGoParser.COMMA)
            self.state = 412
            self.match(MiniGoParser.ID)
            self.state = 413
            self.match(MiniGoParser.SEMICOLON_ASSIGN)
            self.state = 414
            self.match(MiniGoParser.RANGE)
            self.state = 415
            self.expression(0)
            self.state = 416
            self.match(MiniGoParser.LBRACE)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 417
                self.list_statement()


            self.state = 420
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variables_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def type_minigo(self):
            return self.getTypedRuleContext(MiniGoParser.Type_minigoContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variables_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables_for" ):
                return visitor.visitVariables_for(self)
            else:
                return visitor.visitChildren(self)




    def variables_for(self):

        localctx = MiniGoParser.Variables_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_variables_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(MiniGoParser.VAR)
            self.state = 423
            self.match(MiniGoParser.ID)
            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 424
                self.type_minigo()


            self.state = 427
            self.match(MiniGoParser.ASSIGN)
            self.state = 428
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMICOLON_ASSIGN(self):
            return self.getToken(MiniGoParser.SEMICOLON_ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_for" ):
                return visitor.visitAssign_for(self)
            else:
                return visitor.visitChildren(self)




    def assign_for(self):

        localctx = MiniGoParser.Assign_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assign_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(MiniGoParser.ID)
            self.state = 431
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SEMICOLON_ASSIGN) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 432
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 438
                self.lhs(0)
                self.state = 439
                self.match(MiniGoParser.DOT)


            self.state = 443
            self.match(MiniGoParser.ID)
            self.state = 444
            self.match(MiniGoParser.LPAREN)
            self.state = 446
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 445
                self.list_expression()


            self.state = 448
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(MiniGoParser.RETURN)
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 451
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def declared(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclaredContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclaredContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 454
                self.declared()
                self.state = 455
                self.match(MiniGoParser.SEMICOLON)
                self.state = 459 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 461
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(MiniGoParser.VariablesContext,0)


        def constants(self):
            return self.getTypedRuleContext(MiniGoParser.ConstantsContext,0)


        def function(self):
            return self.getTypedRuleContext(MiniGoParser.FunctionContext,0)


        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def struct_type_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_type_declaredContext,0)


        def interface_type_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_type_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = MiniGoParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_declared)
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.variables()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.constants()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 465
                self.function()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 466
                self.method()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 467
                self.struct_type_declared()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 468
                self.interface_type_declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_param(self):
            return self.getTypedRuleContext(MiniGoParser.List_paramContext,0)


        def type_minigo(self):
            return self.getTypedRuleContext(MiniGoParser.Type_minigoContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = MiniGoParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(MiniGoParser.FUNC)
            self.state = 472
            self.match(MiniGoParser.ID)
            self.state = 473
            self.match(MiniGoParser.LPAREN)
            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 474
                self.list_param()


            self.state = 477
            self.match(MiniGoParser.RPAREN)
            self.state = 479
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 478
                self.type_minigo()


            self.state = 481
            self.match(MiniGoParser.LBRACE)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 482
                self.list_statement()


            self.state = 485
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_param(self):
            return self.getTypedRuleContext(MiniGoParser.List_paramContext,0)


        def type_minigo(self):
            return self.getTypedRuleContext(MiniGoParser.Type_minigoContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(MiniGoParser.FUNC)
            self.state = 488
            self.match(MiniGoParser.LPAREN)
            self.state = 489
            self.match(MiniGoParser.ID)
            self.state = 490
            self.match(MiniGoParser.ID)
            self.state = 491
            self.match(MiniGoParser.RPAREN)
            self.state = 492
            self.match(MiniGoParser.ID)
            self.state = 493
            self.match(MiniGoParser.LPAREN)
            self.state = 495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 494
                self.list_param()


            self.state = 497
            self.match(MiniGoParser.RPAREN)
            self.state = 499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 498
                self.type_minigo()


            self.state = 501
            self.match(MiniGoParser.LBRACE)
            self.state = 503
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 502
                self.list_statement()


            self.state = 505
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_type_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_fields(self):
            return self.getTypedRuleContext(MiniGoParser.List_fieldsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type_declared" ):
                return visitor.visitStruct_type_declared(self)
            else:
                return visitor.visitChildren(self)




    def struct_type_declared(self):

        localctx = MiniGoParser.Struct_type_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_struct_type_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(MiniGoParser.TYPE)
            self.state = 508
            self.match(MiniGoParser.ID)
            self.state = 509
            self.match(MiniGoParser.STRUCT)
            self.state = 510
            self.match(MiniGoParser.LBRACE)
            self.state = 511
            self.list_fields()
            self.state = 512
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_fieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fields(self):
            return self.getTypedRuleContext(MiniGoParser.FieldsContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def list_fields(self):
            return self.getTypedRuleContext(MiniGoParser.List_fieldsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_fields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_fields" ):
                return visitor.visitList_fields(self)
            else:
                return visitor.visitChildren(self)




    def list_fields(self):

        localctx = MiniGoParser.List_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_list_fields)
        try:
            self.state = 521
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.fields()
                self.state = 515
                self.match(MiniGoParser.SEMICOLON)
                self.state = 516
                self.list_fields()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 518
                self.fields()
                self.state = 519
                self.match(MiniGoParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_minigo(self):
            return self.getTypedRuleContext(MiniGoParser.Type_minigoContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFields" ):
                return visitor.visitFields(self)
            else:
                return visitor.visitChildren(self)




    def fields(self):

        localctx = MiniGoParser.FieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(MiniGoParser.ID)
            self.state = 524
            self.type_minigo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_type_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_meth_interface(self):
            return self.getTypedRuleContext(MiniGoParser.List_meth_interfaceContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type_declared" ):
                return visitor.visitInterface_type_declared(self)
            else:
                return visitor.visitChildren(self)




    def interface_type_declared(self):

        localctx = MiniGoParser.Interface_type_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_interface_type_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(MiniGoParser.TYPE)
            self.state = 527
            self.match(MiniGoParser.ID)
            self.state = 528
            self.match(MiniGoParser.INTERFACE)
            self.state = 529
            self.match(MiniGoParser.LBRACE)
            self.state = 530
            self.list_meth_interface()
            self.state = 531
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_meth_interfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def meth_interface(self):
            return self.getTypedRuleContext(MiniGoParser.Meth_interfaceContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def list_meth_interface(self):
            return self.getTypedRuleContext(MiniGoParser.List_meth_interfaceContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_meth_interface

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_meth_interface" ):
                return visitor.visitList_meth_interface(self)
            else:
                return visitor.visitChildren(self)




    def list_meth_interface(self):

        localctx = MiniGoParser.List_meth_interfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_list_meth_interface)
        try:
            self.state = 540
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self.meth_interface()
                self.state = 534
                self.match(MiniGoParser.SEMICOLON)
                self.state = 535
                self.list_meth_interface()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 537
                self.meth_interface()
                self.state = 538
                self.match(MiniGoParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Meth_interfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def list_param(self):
            return self.getTypedRuleContext(MiniGoParser.List_paramContext,0)


        def type_minigo(self):
            return self.getTypedRuleContext(MiniGoParser.Type_minigoContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_meth_interface

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeth_interface" ):
                return visitor.visitMeth_interface(self)
            else:
                return visitor.visitChildren(self)




    def meth_interface(self):

        localctx = MiniGoParser.Meth_interfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_meth_interface)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(MiniGoParser.ID)
            self.state = 543
            self.match(MiniGoParser.LPAREN)
            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 544
                self.list_param()


            self.state = 547
            self.match(MiniGoParser.RPAREN)
            self.state = 549
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 548
                self.type_minigo()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def list_param(self):
            return self.getTypedRuleContext(MiniGoParser.List_paramContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_param" ):
                return visitor.visitList_param(self)
            else:
                return visitor.visitChildren(self)




    def list_param(self):

        localctx = MiniGoParser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_list_param)
        try:
            self.state = 555
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.param()
                self.state = 552
                self.list_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 554
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def type_minigo(self):
            return self.getTypedRuleContext(MiniGoParser.Type_minigoContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_param)
        try:
            self.state = 565
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                self.list_ID()
                self.state = 558
                self.type_minigo()
                self.state = 559
                self.match(MiniGoParser.COMMA)
                self.state = 560
                self.param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
                self.list_ID()
                self.state = 563
                self.type_minigo()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_IDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_ID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ID" ):
                return visitor.visitList_ID(self)
            else:
                return visitor.visitChildren(self)




    def list_ID(self):

        localctx = MiniGoParser.List_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_list_ID)
        try:
            self.state = 571
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 567
                self.match(MiniGoParser.ID)
                self.state = 568
                self.match(MiniGoParser.COMMA)
                self.state = 569
                self.list_ID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 570
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expression_sempred
        self._predicates[12] = self.expression1_sempred
        self._predicates[13] = self.expression2_sempred
        self._predicates[14] = self.expression3_sempred
        self._predicates[15] = self.expression4_sempred
        self._predicates[17] = self.expression6_sempred
        self._predicates[27] = self.lhs_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         





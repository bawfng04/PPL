# Generated from main/MiniGo.g4 by ANTLR 4.9.2
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
        buf.write("\u02d3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\5\3\u008e\n\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4\u0095\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u009d")
        buf.write("\n\5\3\5\7\5\u00a0\n\5\f\5\16\5\u00a3\13\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\5\6\u00aa\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\5\7\u00b4\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u00bf\n\t\3\n\3\n\5\n\u00c3\n\n\3\n\3\n\5\n\u00c7\n\n")
        buf.write("\3\n\3\n\3\n\7\n\u00cc\n\n\f\n\16\n\u00cf\13\n\3\n\5\n")
        buf.write("\u00d2\n\n\3\n\3\n\5\n\u00d6\n\n\5\n\u00d8\n\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\f\u00e3\n\f\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u00ed\n\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\7\16\u00f4\n\16\f\16\16\16\u00f7\13")
        buf.write("\16\3\16\3\16\3\16\5\16\u00fc\n\16\3\16\5\16\u00ff\n\16")
        buf.write("\3\16\3\16\5\16\u0103\n\16\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\5\20\u010f\n\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\7\20\u0116\n\20\f\20\16\20\u0119\13\20\3\20")
        buf.write("\3\20\3\20\5\20\u011e\n\20\3\20\3\20\5\20\u0122\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\5\21\u0129\n\21\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u0133\n\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\7\24\u013b\n\24\f\24\16\24\u013e\13")
        buf.write("\24\5\24\u0140\n\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\7\25\u0149\n\25\f\25\16\25\u014c\13\25\3\25\3\25\7\25")
        buf.write("\u0150\n\25\f\25\16\25\u0153\13\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\7\26\u015a\n\26\f\26\16\26\u015d\13\26\3\26\7\26")
        buf.write("\u0160\n\26\f\26\16\26\u0163\13\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u016b\n\27\3\30\3\30\3\30\3\30\5\30\u0171")
        buf.write("\n\30\3\31\3\31\5\31\u0175\n\31\3\31\5\31\u0178\n\31\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u017e\n\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\7\33\u0185\n\33\f\33\16\33\u0188\13\33\3\33\3\33")
        buf.write("\3\33\5\33\u018d\n\33\3\34\3\34\3\34\3\34\5\34\u0193\n")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\5\36\u019f\n\36\3\37\3\37\5\37\u01a3\n\37\3 \3 \5 \u01a7")
        buf.write("\n \3!\3!\5!\u01ab\n!\3\"\3\"\3\"\3\"\5\"\u01b1\n\"\3")
        buf.write("#\3#\3$\3$\3$\7$\u01b8\n$\f$\16$\u01bb\13$\3%\3%\3%\3")
        buf.write("%\3%\5%\u01c2\n%\3%\3%\5%\u01c6\n%\3%\3%\3%\3%\5%\u01cc")
        buf.write("\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\5&\u01e1\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\5\'\u01ee\n\'\3\'\3\'\5\'\u01f2\n\'\3(\3(\3")
        buf.write("(\3(\3)\3)\3)\3*\3*\3*\3+\3+\5+\u0200\n+\3+\3+\5+\u0204")
        buf.write("\n+\3+\5+\u0207\n+\3,\3,\5,\u020b\n,\3,\3,\5,\u020f\n")
        buf.write(",\3,\3,\5,\u0213\n,\3-\5-\u0216\n-\3-\3-\5-\u021a\n-\3")
        buf.write("-\3-\7-\u021e\n-\f-\16-\u0221\13-\3-\5-\u0224\n-\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\5.\u022d\n.\3/\3/\3/\3/\3/\3/\7/\u0235")
        buf.write("\n/\f/\16/\u0238\13/\3\60\3\60\3\60\3\60\3\60\3\60\7\60")
        buf.write("\u0240\n\60\f\60\16\60\u0243\13\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\7\61\u024b\n\61\f\61\16\61\u024e\13\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\7\62\u0256\n\62\f\62\16\62\u0259")
        buf.write("\13\62\3\63\3\63\3\63\3\63\3\63\3\63\7\63\u0261\n\63\f")
        buf.write("\63\16\63\u0264\13\63\3\64\3\64\3\64\3\64\3\64\3\64\7")
        buf.write("\64\u026c\n\64\f\64\16\64\u026f\13\64\3\65\3\65\3\65\3")
        buf.write("\65\3\65\5\65\u0276\n\65\3\66\3\66\3\66\3\66\7\66\u027c")
        buf.write("\n\66\f\66\16\66\u027f\13\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\5\67\u0287\n\67\38\38\38\38\39\39\39\3:\3:\5:\u0292")
        buf.write("\n:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\5;\u029e\n;\3<\3<\3")
        buf.write("<\3<\3<\3=\3=\3=\3=\3=\3=\7=\u02ab\n=\f=\16=\u02ae\13")
        buf.write("=\3=\3=\3>\3>\3>\3>\3>\3>\5>\u02b8\n>\3?\3?\3?\5?\u02bd")
        buf.write("\n?\3?\3?\3@\3@\3@\3@\3@\5@\u02c6\n@\3A\3A\3A\3A\3B\3")
        buf.write("B\3B\3B\3B\5B\u02d1\nB\3B\2\b\\^`bdfC\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\2\n\4\2\66\66;")
        buf.write(";\4\2\t\n\67\67\4\2%*--\4\2..\67\67\3\2\34\35\3\2\36!")
        buf.write("\3\2\27\30\3\2\31\33\2\u02fe\2\u0084\3\2\2\2\4\u008d\3")
        buf.write("\2\2\2\6\u0094\3\2\2\2\b\u009c\3\2\2\2\n\u00a9\3\2\2\2")
        buf.write("\f\u00b3\3\2\2\2\16\u00b5\3\2\2\2\20\u00be\3\2\2\2\22")
        buf.write("\u00d7\3\2\2\2\24\u00d9\3\2\2\2\26\u00e2\3\2\2\2\30\u00e4")
        buf.write("\3\2\2\2\32\u00e8\3\2\2\2\34\u0104\3\2\2\2\36\u0107\3")
        buf.write("\2\2\2 \u0128\3\2\2\2\"\u012a\3\2\2\2$\u0132\3\2\2\2&")
        buf.write("\u013f\3\2\2\2(\u0143\3\2\2\2*\u0157\3\2\2\2,\u016a\3")
        buf.write("\2\2\2.\u0170\3\2\2\2\60\u0177\3\2\2\2\62\u017d\3\2\2")
        buf.write("\2\64\u017f\3\2\2\2\66\u0192\3\2\2\28\u0194\3\2\2\2:\u019e")
        buf.write("\3\2\2\2<\u01a2\3\2\2\2>\u01a6\3\2\2\2@\u01aa\3\2\2\2")
        buf.write("B\u01ac\3\2\2\2D\u01b2\3\2\2\2F\u01b4\3\2\2\2H\u01bc\3")
        buf.write("\2\2\2J\u01cd\3\2\2\2L\u01f1\3\2\2\2N\u01f3\3\2\2\2P\u01f7")
        buf.write("\3\2\2\2R\u01fa\3\2\2\2T\u01fd\3\2\2\2V\u020a\3\2\2\2")
        buf.write("X\u0215\3\2\2\2Z\u022c\3\2\2\2\\\u022e\3\2\2\2^\u0239")
        buf.write("\3\2\2\2`\u0244\3\2\2\2b\u024f\3\2\2\2d\u025a\3\2\2\2")
        buf.write("f\u0265\3\2\2\2h\u0275\3\2\2\2j\u0277\3\2\2\2l\u0286\3")
        buf.write("\2\2\2n\u0288\3\2\2\2p\u028c\3\2\2\2r\u028f\3\2\2\2t\u029d")
        buf.write("\3\2\2\2v\u029f\3\2\2\2x\u02a4\3\2\2\2z\u02b7\3\2\2\2")
        buf.write("|\u02b9\3\2\2\2~\u02c5\3\2\2\2\u0080\u02c7\3\2\2\2\u0082")
        buf.write("\u02d0\3\2\2\2\u0084\u0085\5\4\3\2\u0085\u0086\5\b\5\2")
        buf.write("\u0086\u0087\5\6\4\2\u0087\u0088\5\4\3\2\u0088\u0089\7")
        buf.write("\2\2\3\u0089\3\3\2\2\2\u008a\u008e\3\2\2\2\u008b\u008c")
        buf.write("\7;\2\2\u008c\u008e\5\4\3\2\u008d\u008a\3\2\2\2\u008d")
        buf.write("\u008b\3\2\2\2\u008e\5\3\2\2\2\u008f\u0095\3\2\2\2\u0090")
        buf.write("\u0091\5\4\3\2\u0091\u0092\5\b\5\2\u0092\u0093\5\6\4\2")
        buf.write("\u0093\u0095\3\2\2\2\u0094\u008f\3\2\2\2\u0094\u0090\3")
        buf.write("\2\2\2\u0095\7\3\2\2\2\u0096\u009d\5\16\b\2\u0097\u009d")
        buf.write("\5\24\13\2\u0098\u009d\5\32\16\2\u0099\u009d\5\36\20\2")
        buf.write("\u009a\u009d\5(\25\2\u009b\u009d\5\64\33\2\u009c\u0096")
        buf.write("\3\2\2\2\u009c\u0097\3\2\2\2\u009c\u0098\3\2\2\2\u009c")
        buf.write("\u0099\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009b\3\2\2\2")
        buf.write("\u009d\u00a1\3\2\2\2\u009e\u00a0\7;\2\2\u009f\u009e\3")
        buf.write("\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a2\t\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00aa")
        buf.write("\5\f\7\2\u00a5\u00a6\5\f\7\2\u00a6\u00a7\5\4\3\2\u00a7")
        buf.write("\u00a8\5\n\6\2\u00a8\u00aa\3\2\2\2\u00a9\u00a4\3\2\2\2")
        buf.write("\u00a9\u00a5\3\2\2\2\u00aa\13\3\2\2\2\u00ab\u00b4\5@!")
        buf.write("\2\u00ac\u00b4\5B\"\2\u00ad\u00b4\5H%\2\u00ae\u00b4\5")
        buf.write("J&\2\u00af\u00b4\5P)\2\u00b0\u00b4\5R*\2\u00b1\u00b4\5")
        buf.write("V,\2\u00b2\u00b4\5T+\2\u00b3\u00ab\3\2\2\2\u00b3\u00ac")
        buf.write("\3\2\2\2\u00b3\u00ad\3\2\2\2\u00b3\u00ae\3\2\2\2\u00b3")
        buf.write("\u00af\3\2\2\2\u00b3\u00b0\3\2\2\2\u00b3\u00b1\3\2\2\2")
        buf.write("\u00b3\u00b2\3\2\2\2\u00b4\r\3\2\2\2\u00b5\u00b6\7\20")
        buf.write("\2\2\u00b6\u00b7\5\20\t\2\u00b7\u00b8\7\66\2\2\u00b8\17")
        buf.write("\3\2\2\2\u00b9\u00bf\5\22\n\2\u00ba\u00bb\5\22\n\2\u00bb")
        buf.write("\u00bc\7\65\2\2\u00bc\u00bd\5\20\t\2\u00bd\u00bf\3\2\2")
        buf.write("\2\u00be\u00b9\3\2\2\2\u00be\u00ba\3\2\2\2\u00bf\21\3")
        buf.write("\2\2\2\u00c0\u00c2\7\67\2\2\u00c1\u00c3\5z>\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4")
        buf.write("\u00c5\7%\2\2\u00c5\u00c7\5\\/\2\u00c6\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00d8\3\2\2\2\u00c8\u00cd\7\67\2")
        buf.write("\2\u00c9\u00ca\7\65\2\2\u00ca\u00cc\7\67\2\2\u00cb\u00c9")
        buf.write("\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2")
        buf.write("\u00d0\u00d2\5z>\2\u00d1\u00d0\3\2\2\2\u00d1\u00d2\3\2")
        buf.write("\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d4\7%\2\2\u00d4\u00d6")
        buf.write("\5Z.\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d8")
        buf.write("\3\2\2\2\u00d7\u00c0\3\2\2\2\u00d7\u00c8\3\2\2\2\u00d8")
        buf.write("\23\3\2\2\2\u00d9\u00da\7\17\2\2\u00da\u00db\5\26\f\2")
        buf.write("\u00db\u00dc\t\2\2\2\u00dc\25\3\2\2\2\u00dd\u00e3\5\30")
        buf.write("\r\2\u00de\u00df\5\30\r\2\u00df\u00e0\7\65\2\2\u00e0\u00e1")
        buf.write("\5\26\f\2\u00e1\u00e3\3\2\2\2\u00e2\u00dd\3\2\2\2\u00e2")
        buf.write("\u00de\3\2\2\2\u00e3\27\3\2\2\2\u00e4\u00e5\7\67\2\2\u00e5")
        buf.write("\u00e6\7%\2\2\u00e6\u00e7\5\\/\2\u00e7\31\3\2\2\2\u00e8")
        buf.write("\u00e9\7\7\2\2\u00e9\u00ea\7\67\2\2\u00ea\u00ec\7/\2\2")
        buf.write("\u00eb\u00ed\5$\23\2\u00ec\u00eb\3\2\2\2\u00ec\u00ed\3")
        buf.write("\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00fb\7\60\2\2\u00ef")
        buf.write("\u00f0\7/\2\2\u00f0\u00f5\5z>\2\u00f1\u00f2\7\65\2\2\u00f2")
        buf.write("\u00f4\5z>\2\u00f3\u00f1\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2")
        buf.write("\u00f7\u00f5\3\2\2\2\u00f8\u00f9\7\60\2\2\u00f9\u00fc")
        buf.write("\3\2\2\2\u00fa\u00fc\5z>\2\u00fb\u00ef\3\2\2\2\u00fb\u00fa")
        buf.write("\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe\3\2\2\2\u00fd")
        buf.write("\u00ff\7;\2\2\u00fe\u00fd\3\2\2\2\u00fe\u00ff\3\2\2\2")
        buf.write("\u00ff\u0100\3\2\2\2\u0100\u0102\5X-\2\u0101\u0103\7\66")
        buf.write("\2\2\u0102\u0101\3\2\2\2\u0102\u0103\3\2\2\2\u0103\33")
        buf.write("\3\2\2\2\u0104\u0105\7\67\2\2\u0105\u0106\t\3\2\2\u0106")
        buf.write("\35\3\2\2\2\u0107\u0108\7\7\2\2\u0108\u0109\7/\2\2\u0109")
        buf.write("\u010a\5\34\17\2\u010a\u010b\7\60\2\2\u010b\u010c\7\67")
        buf.write("\2\2\u010c\u010e\7/\2\2\u010d\u010f\5 \21\2\u010e\u010d")
        buf.write("\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("\u011d\7\60\2\2\u0111\u0112\7/\2\2\u0112\u0117\5z>\2\u0113")
        buf.write("\u0114\7\65\2\2\u0114\u0116\5z>\2\u0115\u0113\3\2\2\2")
        buf.write("\u0116\u0119\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3")
        buf.write("\2\2\2\u0118\u011a\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b")
        buf.write("\7\60\2\2\u011b\u011e\3\2\2\2\u011c\u011e\5z>\2\u011d")
        buf.write("\u0111\3\2\2\2\u011d\u011c\3\2\2\2\u011d\u011e\3\2\2\2")
        buf.write("\u011e\u011f\3\2\2\2\u011f\u0121\5X-\2\u0120\u0122\7\66")
        buf.write("\2\2\u0121\u0120\3\2\2\2\u0121\u0122\3\2\2\2\u0122\37")
        buf.write("\3\2\2\2\u0123\u0129\5\"\22\2\u0124\u0125\5\"\22\2\u0125")
        buf.write("\u0126\7\65\2\2\u0126\u0127\5 \21\2\u0127\u0129\3\2\2")
        buf.write("\2\u0128\u0123\3\2\2\2\u0128\u0124\3\2\2\2\u0129!\3\2")
        buf.write("\2\2\u012a\u012b\7\67\2\2\u012b\u012c\5z>\2\u012c#\3\2")
        buf.write("\2\2\u012d\u0133\5&\24\2\u012e\u012f\5&\24\2\u012f\u0130")
        buf.write("\7\65\2\2\u0130\u0131\5$\23\2\u0131\u0133\3\2\2\2\u0132")
        buf.write("\u012d\3\2\2\2\u0132\u012e\3\2\2\2\u0133%\3\2\2\2\u0134")
        buf.write("\u0140\7\67\2\2\u0135\u0136\7\67\2\2\u0136\u0137\7\65")
        buf.write("\2\2\u0137\u013c\7\67\2\2\u0138\u0139\7\65\2\2\u0139\u013b")
        buf.write("\7\67\2\2\u013a\u0138\3\2\2\2\u013b\u013e\3\2\2\2\u013c")
        buf.write("\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u0140\3\2\2\2")
        buf.write("\u013e\u013c\3\2\2\2\u013f\u0134\3\2\2\2\u013f\u0135\3")
        buf.write("\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\5z>\2\u0142\'\3")
        buf.write("\2\2\2\u0143\u0144\7\b\2\2\u0144\u0145\7\67\2\2\u0145")
        buf.write("\u0146\7\t\2\2\u0146\u014a\7\61\2\2\u0147\u0149\7;\2\2")
        buf.write("\u0148\u0147\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3")
        buf.write("\2\2\2\u014a\u014b\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014a")
        buf.write("\3\2\2\2\u014d\u0151\5*\26\2\u014e\u0150\7;\2\2\u014f")
        buf.write("\u014e\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2")
        buf.write("\u0151\u0152\3\2\2\2\u0152\u0154\3\2\2\2\u0153\u0151\3")
        buf.write("\2\2\2\u0154\u0155\7\62\2\2\u0155\u0156\t\2\2\2\u0156")
        buf.write(")\3\2\2\2\u0157\u0161\5,\27\2\u0158\u015a\7;\2\2\u0159")
        buf.write("\u0158\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015b\u015c\3\2\2\2\u015c\u015e\3\2\2\2\u015d\u015b\3")
        buf.write("\2\2\2\u015e\u0160\5,\27\2\u015f\u015b\3\2\2\2\u0160\u0163")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("+\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165\7\67\2\2\u0165")
        buf.write("\u0166\5.\30\2\u0166\u0167\5z>\2\u0167\u0168\5\60\31\2")
        buf.write("\u0168\u016b\3\2\2\2\u0169\u016b\5\36\20\2\u016a\u0164")
        buf.write("\3\2\2\2\u016a\u0169\3\2\2\2\u016b-\3\2\2\2\u016c\u0171")
        buf.write("\3\2\2\2\u016d\u016e\7\65\2\2\u016e\u016f\7\67\2\2\u016f")
        buf.write("\u0171\5.\30\2\u0170\u016c\3\2\2\2\u0170\u016d\3\2\2\2")
        buf.write("\u0171/\3\2\2\2\u0172\u0178\7\66\2\2\u0173\u0175\7\66")
        buf.write("\2\2\u0174\u0173\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176\u0178\7;\2\2\u0177\u0172\3\2\2\2\u0177")
        buf.write("\u0174\3\2\2\2\u0178\61\3\2\2\2\u0179\u017e\3\2\2\2\u017a")
        buf.write("\u017b\5,\27\2\u017b\u017c\5\62\32\2\u017c\u017e\3\2\2")
        buf.write("\2\u017d\u0179\3\2\2\2\u017d\u017a\3\2\2\2\u017e\63\3")
        buf.write("\2\2\2\u017f\u0180\7\b\2\2\u0180\u0181\7\67\2\2\u0181")
        buf.write("\u0182\7\n\2\2\u0182\u0186\7\61\2\2\u0183\u0185\7;\2\2")
        buf.write("\u0184\u0183\3\2\2\2\u0185\u0188\3\2\2\2\u0186\u0184\3")
        buf.write("\2\2\2\u0186\u0187\3\2\2\2\u0187\u0189\3\2\2\2\u0188\u0186")
        buf.write("\3\2\2\2\u0189\u018a\5\66\34\2\u018a\u018c\7\62\2\2\u018b")
        buf.write("\u018d\7\66\2\2\u018c\u018b\3\2\2\2\u018c\u018d\3\2\2")
        buf.write("\2\u018d\65\3\2\2\2\u018e\u0193\3\2\2\2\u018f\u0190\5")
        buf.write("8\35\2\u0190\u0191\5\66\34\2\u0191\u0193\3\2\2\2\u0192")
        buf.write("\u018e\3\2\2\2\u0192\u018f\3\2\2\2\u0193\67\3\2\2\2\u0194")
        buf.write("\u0195\7\67\2\2\u0195\u0196\7/\2\2\u0196\u0197\5:\36\2")
        buf.write("\u0197\u0198\7\60\2\2\u0198\u0199\5<\37\2\u0199\u019a")
        buf.write("\5> \2\u019a\u019b\5\4\3\2\u019b9\3\2\2\2\u019c\u019f")
        buf.write("\3\2\2\2\u019d\u019f\5$\23\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019f;\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1")
        buf.write("\u01a3\5z>\2\u01a2\u01a0\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3")
        buf.write("=\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a7\7\66\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7?\3\2\2\2\u01a8")
        buf.write("\u01ab\5\16\b\2\u01a9\u01ab\5\24\13\2\u01aa\u01a8\3\2")
        buf.write("\2\2\u01aa\u01a9\3\2\2\2\u01abA\3\2\2\2\u01ac\u01ad\5")
        buf.write("F$\2\u01ad\u01ae\5D#\2\u01ae\u01b0\5\\/\2\u01af\u01b1")
        buf.write("\7\66\2\2\u01b0\u01af\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("C\3\2\2\2\u01b2\u01b3\t\4\2\2\u01b3E\3\2\2\2\u01b4\u01b9")
        buf.write("\7\67\2\2\u01b5\u01b8\5p9\2\u01b6\u01b8\5n8\2\u01b7\u01b5")
        buf.write("\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9")
        buf.write("\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01baG\3\2\2\2\u01bb")
        buf.write("\u01b9\3\2\2\2\u01bc\u01bd\7\3\2\2\u01bd\u01be\7/\2\2")
        buf.write("\u01be\u01bf\5\\/\2\u01bf\u01c1\7\60\2\2\u01c0\u01c2\7")
        buf.write(";\2\2\u01c1\u01c0\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3")
        buf.write("\3\2\2\2\u01c3\u01c5\5X-\2\u01c4\u01c6\7;\2\2\u01c5\u01c4")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01cb\3\2\2\2\u01c7")
        buf.write("\u01c8\7\4\2\2\u01c8\u01cc\5H%\2\u01c9\u01ca\7\4\2\2\u01ca")
        buf.write("\u01cc\5X-\2\u01cb\u01c7\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb")
        buf.write("\u01cc\3\2\2\2\u01ccI\3\2\2\2\u01cd\u01e0\7\5\2\2\u01ce")
        buf.write("\u01cf\t\5\2\2\u01cf\u01d0\7\65\2\2\u01d0\u01d1\t\5\2")
        buf.write("\2\u01d1\u01d2\7-\2\2\u01d2\u01d3\7\23\2\2\u01d3\u01d4")
        buf.write("\5\\/\2\u01d4\u01d5\5X-\2\u01d5\u01e1\3\2\2\2\u01d6\u01d7")
        buf.write("\5L\'\2\u01d7\u01d8\7\66\2\2\u01d8\u01d9\5\\/\2\u01d9")
        buf.write("\u01da\7\66\2\2\u01da\u01db\5N(\2\u01db\u01dc\5X-\2\u01dc")
        buf.write("\u01e1\3\2\2\2\u01dd\u01de\5\\/\2\u01de\u01df\5X-\2\u01df")
        buf.write("\u01e1\3\2\2\2\u01e0\u01ce\3\2\2\2\u01e0\u01d6\3\2\2\2")
        buf.write("\u01e0\u01dd\3\2\2\2\u01e1K\3\2\2\2\u01e2\u01e3\5F$\2")
        buf.write("\u01e3\u01e4\7-\2\2\u01e4\u01e5\5\\/\2\u01e5\u01f2\3\2")
        buf.write("\2\2\u01e6\u01e7\5F$\2\u01e7\u01e8\5D#\2\u01e8\u01e9\5")
        buf.write("\\/\2\u01e9\u01f2\3\2\2\2\u01ea\u01eb\7\20\2\2\u01eb\u01ed")
        buf.write("\7\67\2\2\u01ec\u01ee\5z>\2\u01ed\u01ec\3\2\2\2\u01ed")
        buf.write("\u01ee\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f0\7%\2\2")
        buf.write("\u01f0\u01f2\5\\/\2\u01f1\u01e2\3\2\2\2\u01f1\u01e6\3")
        buf.write("\2\2\2\u01f1\u01ea\3\2\2\2\u01f2M\3\2\2\2\u01f3\u01f4")
        buf.write("\5F$\2\u01f4\u01f5\5D#\2\u01f5\u01f6\5\\/\2\u01f6O\3\2")
        buf.write("\2\2\u01f7\u01f8\7\22\2\2\u01f8\u01f9\t\2\2\2\u01f9Q\3")
        buf.write("\2\2\2\u01fa\u01fb\7\21\2\2\u01fb\u01fc\t\2\2\2\u01fc")
        buf.write("S\3\2\2\2\u01fd\u0206\7\6\2\2\u01fe\u0200\5\\/\2\u01ff")
        buf.write("\u01fe\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0201\3\2\2\2")
        buf.write("\u0201\u0207\7\66\2\2\u0202\u0204\5\\/\2\u0203\u0202\3")
        buf.write("\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0207")
        buf.write("\7;\2\2\u0206\u01ff\3\2\2\2\u0206\u0203\3\2\2\2\u0207")
        buf.write("U\3\2\2\2\u0208\u020b\7\67\2\2\u0209\u020b\5F$\2\u020a")
        buf.write("\u0208\3\2\2\2\u020a\u0209\3\2\2\2\u020b\u020c\3\2\2\2")
        buf.write("\u020c\u020e\7/\2\2\u020d\u020f\5\u0082B\2\u020e\u020d")
        buf.write("\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0210\3\2\2\2\u0210")
        buf.write("\u0212\7\60\2\2\u0211\u0213\7\66\2\2\u0212\u0211\3\2\2")
        buf.write("\2\u0212\u0213\3\2\2\2\u0213W\3\2\2\2\u0214\u0216\7;\2")
        buf.write("\2\u0215\u0214\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0217")
        buf.write("\3\2\2\2\u0217\u0219\7\61\2\2\u0218\u021a\7;\2\2\u0219")
        buf.write("\u0218\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u021f\3\2\2\2")
        buf.write("\u021b\u021e\5\f\7\2\u021c\u021e\7;\2\2\u021d\u021b\3")
        buf.write("\2\2\2\u021d\u021c\3\2\2\2\u021e\u0221\3\2\2\2\u021f\u021d")
        buf.write("\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0223\3\2\2\2\u0221")
        buf.write("\u021f\3\2\2\2\u0222\u0224\7;\2\2\u0223\u0222\3\2\2\2")
        buf.write("\u0223\u0224\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0226\7")
        buf.write("\62\2\2\u0226Y\3\2\2\2\u0227\u022d\5\\/\2\u0228\u0229")
        buf.write("\5\\/\2\u0229\u022a\7\65\2\2\u022a\u022b\5Z.\2\u022b\u022d")
        buf.write("\3\2\2\2\u022c\u0227\3\2\2\2\u022c\u0228\3\2\2\2\u022d")
        buf.write("[\3\2\2\2\u022e\u022f\b/\1\2\u022f\u0230\5^\60\2\u0230")
        buf.write("\u0236\3\2\2\2\u0231\u0232\f\4\2\2\u0232\u0233\7#\2\2")
        buf.write("\u0233\u0235\5^\60\2\u0234\u0231\3\2\2\2\u0235\u0238\3")
        buf.write("\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237\3\2\2\2\u0237]")
        buf.write("\3\2\2\2\u0238\u0236\3\2\2\2\u0239\u023a\b\60\1\2\u023a")
        buf.write("\u023b\5`\61\2\u023b\u0241\3\2\2\2\u023c\u023d\f\4\2\2")
        buf.write("\u023d\u023e\7\"\2\2\u023e\u0240\5`\61\2\u023f\u023c\3")
        buf.write("\2\2\2\u0240\u0243\3\2\2\2\u0241\u023f\3\2\2\2\u0241\u0242")
        buf.write("\3\2\2\2\u0242_\3\2\2\2\u0243\u0241\3\2\2\2\u0244\u0245")
        buf.write("\b\61\1\2\u0245\u0246\5b\62\2\u0246\u024c\3\2\2\2\u0247")
        buf.write("\u0248\f\4\2\2\u0248\u0249\t\6\2\2\u0249\u024b\5b\62\2")
        buf.write("\u024a\u0247\3\2\2\2\u024b\u024e\3\2\2\2\u024c\u024a\3")
        buf.write("\2\2\2\u024c\u024d\3\2\2\2\u024da\3\2\2\2\u024e\u024c")
        buf.write("\3\2\2\2\u024f\u0250\b\62\1\2\u0250\u0251\5d\63\2\u0251")
        buf.write("\u0257\3\2\2\2\u0252\u0253\f\4\2\2\u0253\u0254\t\7\2\2")
        buf.write("\u0254\u0256\5d\63\2\u0255\u0252\3\2\2\2\u0256\u0259\3")
        buf.write("\2\2\2\u0257\u0255\3\2\2\2\u0257\u0258\3\2\2\2\u0258c")
        buf.write("\3\2\2\2\u0259\u0257\3\2\2\2\u025a\u025b\b\63\1\2\u025b")
        buf.write("\u025c\5f\64\2\u025c\u0262\3\2\2\2\u025d\u025e\f\4\2\2")
        buf.write("\u025e\u025f\t\b\2\2\u025f\u0261\5f\64\2\u0260\u025d\3")
        buf.write("\2\2\2\u0261\u0264\3\2\2\2\u0262\u0260\3\2\2\2\u0262\u0263")
        buf.write("\3\2\2\2\u0263e\3\2\2\2\u0264\u0262\3\2\2\2\u0265\u0266")
        buf.write("\b\64\1\2\u0266\u0267\5h\65\2\u0267\u026d\3\2\2\2\u0268")
        buf.write("\u0269\f\4\2\2\u0269\u026a\t\t\2\2\u026a\u026c\5h\65\2")
        buf.write("\u026b\u0268\3\2\2\2\u026c\u026f\3\2\2\2\u026d\u026b\3")
        buf.write("\2\2\2\u026d\u026e\3\2\2\2\u026eg\3\2\2\2\u026f\u026d")
        buf.write("\3\2\2\2\u0270\u0271\7$\2\2\u0271\u0276\5h\65\2\u0272")
        buf.write("\u0273\7\30\2\2\u0273\u0276\5h\65\2\u0274\u0276\5j\66")
        buf.write("\2\u0275\u0270\3\2\2\2\u0275\u0272\3\2\2\2\u0275\u0274")
        buf.write("\3\2\2\2\u0276i\3\2\2\2\u0277\u027d\5l\67\2\u0278\u027c")
        buf.write("\5n8\2\u0279\u027c\5p9\2\u027a\u027c\5r:\2\u027b\u0278")
        buf.write("\3\2\2\2\u027b\u0279\3\2\2\2\u027b\u027a\3\2\2\2\u027c")
        buf.write("\u027f\3\2\2\2\u027d\u027b\3\2\2\2\u027d\u027e\3\2\2\2")
        buf.write("\u027ek\3\2\2\2\u027f\u027d\3\2\2\2\u0280\u0287\5t;\2")
        buf.write("\u0281\u0287\7\67\2\2\u0282\u0283\7/\2\2\u0283\u0284\5")
        buf.write("\\/\2\u0284\u0285\7\60\2\2\u0285\u0287\3\2\2\2\u0286\u0280")
        buf.write("\3\2\2\2\u0286\u0281\3\2\2\2\u0286\u0282\3\2\2\2\u0287")
        buf.write("m\3\2\2\2\u0288\u0289\7\63\2\2\u0289\u028a\5\\/\2\u028a")
        buf.write("\u028b\7\64\2\2\u028bo\3\2\2\2\u028c\u028d\7+\2\2\u028d")
        buf.write("\u028e\7\67\2\2\u028eq\3\2\2\2\u028f\u0291\7/\2\2\u0290")
        buf.write("\u0292\5\u0082B\2\u0291\u0290\3\2\2\2\u0291\u0292\3\2")
        buf.write("\2\2\u0292\u0293\3\2\2\2\u0293\u0294\7\60\2\2\u0294s\3")
        buf.write("\2\2\2\u0295\u029e\78\2\2\u0296\u029e\79\2\2\u0297\u029e")
        buf.write("\7:\2\2\u0298\u029e\7\25\2\2\u0299\u029e\7\26\2\2\u029a")
        buf.write("\u029e\7\24\2\2\u029b\u029e\5v<\2\u029c\u029e\5|?\2\u029d")
        buf.write("\u0295\3\2\2\2\u029d\u0296\3\2\2\2\u029d\u0297\3\2\2\2")
        buf.write("\u029d\u0298\3\2\2\2\u029d\u0299\3\2\2\2\u029d\u029a\3")
        buf.write("\2\2\2\u029d\u029b\3\2\2\2\u029d\u029c\3\2\2\2\u029eu")
        buf.write("\3\2\2\2\u029f\u02a0\5x=\2\u02a0\u02a1\7\61\2\2\u02a1")
        buf.write("\u02a2\5\u0082B\2\u02a2\u02a3\7\62\2\2\u02a3w\3\2\2\2")
        buf.write("\u02a4\u02a5\7\63\2\2\u02a5\u02a6\78\2\2\u02a6\u02ac\7")
        buf.write("\64\2\2\u02a7\u02a8\7\63\2\2\u02a8\u02a9\78\2\2\u02a9")
        buf.write("\u02ab\7\64\2\2\u02aa\u02a7\3\2\2\2\u02ab\u02ae\3\2\2")
        buf.write("\2\u02ac\u02aa\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u02af")
        buf.write("\3\2\2\2\u02ae\u02ac\3\2\2\2\u02af\u02b0\5z>\2\u02b0y")
        buf.write("\3\2\2\2\u02b1\u02b8\7\f\2\2\u02b2\u02b8\7\r\2\2\u02b3")
        buf.write("\u02b8\7\13\2\2\u02b4\u02b8\7\16\2\2\u02b5\u02b8\7\67")
        buf.write("\2\2\u02b6\u02b8\5x=\2\u02b7\u02b1\3\2\2\2\u02b7\u02b2")
        buf.write("\3\2\2\2\u02b7\u02b3\3\2\2\2\u02b7\u02b4\3\2\2\2\u02b7")
        buf.write("\u02b5\3\2\2\2\u02b7\u02b6\3\2\2\2\u02b8{\3\2\2\2\u02b9")
        buf.write("\u02ba\7\67\2\2\u02ba\u02bc\7\61\2\2\u02bb\u02bd\5~@\2")
        buf.write("\u02bc\u02bb\3\2\2\2\u02bc\u02bd\3\2\2\2\u02bd\u02be\3")
        buf.write("\2\2\2\u02be\u02bf\7\62\2\2\u02bf}\3\2\2\2\u02c0\u02c6")
        buf.write("\5\u0080A\2\u02c1\u02c2\5\u0080A\2\u02c2\u02c3\7\65\2")
        buf.write("\2\u02c3\u02c4\5~@\2\u02c4\u02c6\3\2\2\2\u02c5\u02c0\3")
        buf.write("\2\2\2\u02c5\u02c1\3\2\2\2\u02c6\177\3\2\2\2\u02c7\u02c8")
        buf.write("\7\67\2\2\u02c8\u02c9\7,\2\2\u02c9\u02ca\5\\/\2\u02ca")
        buf.write("\u0081\3\2\2\2\u02cb\u02d1\5\\/\2\u02cc\u02cd\5\\/\2\u02cd")
        buf.write("\u02ce\7\65\2\2\u02ce\u02cf\5\u0082B\2\u02cf\u02d1\3\2")
        buf.write("\2\2\u02d0\u02cb\3\2\2\2\u02d0\u02cc\3\2\2\2\u02d1\u0083")
        buf.write("\3\2\2\2S\u008d\u0094\u009c\u00a1\u00a9\u00b3\u00be\u00c2")
        buf.write("\u00c6\u00cd\u00d1\u00d5\u00d7\u00e2\u00ec\u00f5\u00fb")
        buf.write("\u00fe\u0102\u010e\u0117\u011d\u0121\u0128\u0132\u013c")
        buf.write("\u013f\u014a\u0151\u015b\u0161\u016a\u0170\u0174\u0177")
        buf.write("\u017d\u0186\u018c\u0192\u019e\u01a2\u01a6\u01aa\u01b0")
        buf.write("\u01b7\u01b9\u01c1\u01c5\u01cb\u01e0\u01ed\u01f1\u01ff")
        buf.write("\u0203\u0206\u020a\u020e\u0212\u0215\u0219\u021d\u021f")
        buf.write("\u0223\u022c\u0236\u0241\u024c\u0257\u0262\u026d\u0275")
        buf.write("\u027b\u027d\u0286\u0291\u029d\u02ac\u02b7\u02bc\u02c5")
        buf.write("\u02d0")
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
                     "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'.'", "':'", "':='", "'_'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
                      "GREATER", "GREATER_OR_EQUAL", "AND", "OR", "NOT", 
                      "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", "SHORT_ASSIGN", 
                      "UNDERSCORE", "LP", "RP", "LB", "RB", "LSB", "RSB", 
                      "COMMA", "SEMI", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "NEWLINE", "WS", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_newlines = 1
    RULE_more_declared = 2
    RULE_declared = 3
    RULE_list_statement = 4
    RULE_statement = 5
    RULE_variables_declared = 6
    RULE_var_decl_list = 7
    RULE_var_decl = 8
    RULE_constants_declared = 9
    RULE_const_decl_list = 10
    RULE_const_decl = 11
    RULE_function_declared = 12
    RULE_receiver = 13
    RULE_method_declared = 14
    RULE_method_params = 15
    RULE_method_param = 16
    RULE_params_list = 17
    RULE_param = 18
    RULE_struct_declared = 19
    RULE_struct_type_list = 20
    RULE_struct_field = 21
    RULE_more_ids = 22
    RULE_struct_end = 23
    RULE_struct_type = 24
    RULE_interface_declared = 25
    RULE_interface_type = 26
    RULE_interface_method = 27
    RULE_optional_params = 28
    RULE_optional_type = 29
    RULE_optional_semi = 30
    RULE_declared_statement = 31
    RULE_assign_statement = 32
    RULE_assign_op = 33
    RULE_assign_lhs = 34
    RULE_if_statement = 35
    RULE_for_statement = 36
    RULE_for_init = 37
    RULE_for_update = 38
    RULE_break_statement = 39
    RULE_continue_statement = 40
    RULE_return_statement = 41
    RULE_call_statement = 42
    RULE_block_stmt = 43
    RULE_expr_list = 44
    RULE_expression = 45
    RULE_expression1 = 46
    RULE_expression2 = 47
    RULE_expression3 = 48
    RULE_expression4 = 49
    RULE_expression5 = 50
    RULE_expression6 = 51
    RULE_expression7 = 52
    RULE_operand = 53
    RULE_element_access = 54
    RULE_field_access = 55
    RULE_call_expr = 56
    RULE_literal = 57
    RULE_array_literal = 58
    RULE_array_type = 59
    RULE_type_name = 60
    RULE_struct_literal = 61
    RULE_field_list = 62
    RULE_field_init = 63
    RULE_list_expression = 64

    ruleNames =  [ "program", "newlines", "more_declared", "declared", "list_statement", 
                   "statement", "variables_declared", "var_decl_list", "var_decl", 
                   "constants_declared", "const_decl_list", "const_decl", 
                   "function_declared", "receiver", "method_declared", "method_params", 
                   "method_param", "params_list", "param", "struct_declared", 
                   "struct_type_list", "struct_field", "more_ids", "struct_end", 
                   "struct_type", "interface_declared", "interface_type", 
                   "interface_method", "optional_params", "optional_type", 
                   "optional_semi", "declared_statement", "assign_statement", 
                   "assign_op", "assign_lhs", "if_statement", "for_statement", 
                   "for_init", "for_update", "break_statement", "continue_statement", 
                   "return_statement", "call_statement", "block_stmt", "expr_list", 
                   "expression", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7", 
                   "operand", "element_access", "field_access", "call_expr", 
                   "literal", "array_literal", "array_type", "type_name", 
                   "struct_literal", "field_list", "field_init", "list_expression" ]

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
    EQUAL=26
    NOT_EQUAL=27
    LESS=28
    LESS_OR_EQUAL=29
    GREATER=30
    GREATER_OR_EQUAL=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    ADD_ASSIGN=36
    SUB_ASSIGN=37
    MUL_ASSIGN=38
    DIV_ASSIGN=39
    MOD_ASSIGN=40
    DOT=41
    COLON=42
    SHORT_ASSIGN=43
    UNDERSCORE=44
    LP=45
    RP=46
    LB=47
    RB=48
    LSB=49
    RSB=50
    COMMA=51
    SEMI=52
    ID=53
    INT_LIT=54
    FLOAT_LIT=55
    STRING_LIT=56
    NEWLINE=57
    WS=58
    BLOCK_COMMENT=59
    LINE_COMMENT=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlines(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlinesContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlinesContext,i)


        def declared(self):
            return self.getTypedRuleContext(MiniGoParser.DeclaredContext,0)


        def more_declared(self):
            return self.getTypedRuleContext(MiniGoParser.More_declaredContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.newlines()
            self.state = 131
            self.declared()
            self.state = 132
            self.more_declared()
            self.state = 133
            self.newlines()
            self.state = 134
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_newlines

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlines" ):
                return visitor.visitNewlines(self)
            else:
                return visitor.visitChildren(self)




    def newlines(self):

        localctx = MiniGoParser.NewlinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_newlines)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.EOF, MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.RB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(MiniGoParser.NEWLINE)
                self.state = 138
                self.newlines()
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


    class More_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


        def declared(self):
            return self.getTypedRuleContext(MiniGoParser.DeclaredContext,0)


        def more_declared(self):
            return self.getTypedRuleContext(MiniGoParser.More_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore_declared" ):
                return visitor.visitMore_declared(self)
            else:
                return visitor.visitChildren(self)




    def more_declared(self):

        localctx = MiniGoParser.More_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_more_declared)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.newlines()
                self.state = 143
                self.declared()
                self.state = 144
                self.more_declared()
                pass


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

        def variables_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_declaredContext,0)


        def constants_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Constants_declaredContext,0)


        def function_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Function_declaredContext,0)


        def method_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declaredContext,0)


        def struct_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declaredContext,0)


        def interface_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declaredContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = MiniGoParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 148
                self.variables_declared()
                pass

            elif la_ == 2:
                self.state = 149
                self.constants_declared()
                pass

            elif la_ == 3:
                self.state = 150
                self.function_declared()
                pass

            elif la_ == 4:
                self.state = 151
                self.method_declared()
                pass

            elif la_ == 5:
                self.state = 152
                self.struct_declared()
                pass

            elif la_ == 6:
                self.state = 153
                self.interface_declared()
                pass


            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 156
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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


        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


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
        self.enterRule(localctx, 8, self.RULE_list_statement)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.statement()
                self.state = 164
                self.newlines()
                self.state = 165
                self.list_statement()
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
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.declared_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 172
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 173
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 174
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 175
                self.call_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 176
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variables_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def var_decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_listContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_variables_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables_declared" ):
                return visitor.visitVariables_declared(self)
            else:
                return visitor.visitChildren(self)




    def variables_declared(self):

        localctx = MiniGoParser.Variables_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variables_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(MiniGoParser.VAR)
            self.state = 180
            self.var_decl_list()
            self.state = 181
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def var_decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_list" ):
                return visitor.visitVar_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_list(self):

        localctx = MiniGoParser.Var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_decl_list)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.var_decl()
                self.state = 185
                self.match(MiniGoParser.COMMA)
                self.state = 186
                self.var_decl_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(MiniGoParser.ID)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 191
                    self.type_name()


                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 194
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 195
                    self.expression(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.match(MiniGoParser.ID)
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 199
                        self.match(MiniGoParser.COMMA)
                        self.state = 200
                        self.match(MiniGoParser.ID) 
                    self.state = 205
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 206
                    self.type_name()


                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 209
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 210
                    self.expr_list()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constants_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def const_decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Const_decl_listContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_constants_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstants_declared" ):
                return visitor.visitConstants_declared(self)
            else:
                return visitor.visitChildren(self)




    def constants_declared(self):

        localctx = MiniGoParser.Constants_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constants_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MiniGoParser.CONST)
            self.state = 216
            self.const_decl_list()
            self.state = 217
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NEWLINE):
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


    class Const_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def const_decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Const_decl_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl_list" ):
                return visitor.visitConst_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def const_decl_list(self):

        localctx = MiniGoParser.Const_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_const_decl_list)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.const_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.const_decl()
                self.state = 221
                self.match(MiniGoParser.COMMA)
                self.state = 222
                self.const_decl_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(MiniGoParser.ID)
            self.state = 227
            self.match(MiniGoParser.ASSIGN)
            self.state = 228
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LP)
            else:
                return self.getToken(MiniGoParser.LP, i)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RP)
            else:
                return self.getToken(MiniGoParser.RP, i)

        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Params_listContext,0)


        def type_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Type_nameContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Type_nameContext,i)


        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_function_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declared" ):
                return visitor.visitFunction_declared(self)
            else:
                return visitor.visitChildren(self)




    def function_declared(self):

        localctx = MiniGoParser.Function_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_function_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(MiniGoParser.FUNC)
            self.state = 231
            self.match(MiniGoParser.ID)
            self.state = 232
            self.match(MiniGoParser.LP)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 233
                self.params_list()


            self.state = 236
            self.match(MiniGoParser.RP)
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LP]:
                self.state = 237
                self.match(MiniGoParser.LP)
                self.state = 238
                self.type_name()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 239
                    self.match(MiniGoParser.COMMA)
                    self.state = 240
                    self.type_name()
                    self.state = 245
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 246
                self.match(MiniGoParser.RP)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.state = 248
                self.type_name()
                pass
            elif token in [MiniGoParser.LB, MiniGoParser.NEWLINE]:
                pass
            else:
                pass
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 251
                self.match(MiniGoParser.NEWLINE)


            self.state = 254
            self.block_stmt()
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 255
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_receiver)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(MiniGoParser.ID)
            self.state = 259
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRUCT) | (1 << MiniGoParser.INTERFACE) | (1 << MiniGoParser.ID))) != 0)):
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


    class Method_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LP)
            else:
                return self.getToken(MiniGoParser.LP, i)

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RP)
            else:
                return self.getToken(MiniGoParser.RP, i)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def method_params(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paramsContext,0)


        def type_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Type_nameContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Type_nameContext,i)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declared" ):
                return visitor.visitMethod_declared(self)
            else:
                return visitor.visitChildren(self)




    def method_declared(self):

        localctx = MiniGoParser.Method_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_method_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(MiniGoParser.FUNC)
            self.state = 262
            self.match(MiniGoParser.LP)
            self.state = 263
            self.receiver()
            self.state = 264
            self.match(MiniGoParser.RP)
            self.state = 265
            self.match(MiniGoParser.ID)
            self.state = 266
            self.match(MiniGoParser.LP)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 267
                self.method_params()


            self.state = 270
            self.match(MiniGoParser.RP)
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LP]:
                self.state = 271
                self.match(MiniGoParser.LP)
                self.state = 272
                self.type_name()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 273
                    self.match(MiniGoParser.COMMA)
                    self.state = 274
                    self.type_name()
                    self.state = 279
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 280
                self.match(MiniGoParser.RP)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.state = 282
                self.type_name()
                pass
            elif token in [MiniGoParser.LB, MiniGoParser.NEWLINE]:
                pass
            else:
                pass
            self.state = 285
            self.block_stmt()
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 286
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_param(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paramContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def method_params(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paramsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_params" ):
                return visitor.visitMethod_params(self)
            else:
                return visitor.visitChildren(self)




    def method_params(self):

        localctx = MiniGoParser.Method_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_method_params)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.method_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.method_param()
                self.state = 291
                self.match(MiniGoParser.COMMA)
                self.state = 292
                self.method_params()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_param" ):
                return visitor.visitMethod_param(self)
            else:
                return visitor.visitChildren(self)




    def method_param(self):

        localctx = MiniGoParser.Method_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_method_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(MiniGoParser.ID)
            self.state = 297
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Params_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_params_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list" ):
                return visitor.visitParams_list(self)
            else:
                return visitor.visitChildren(self)




    def params_list(self):

        localctx = MiniGoParser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_params_list)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.param()
                self.state = 301
                self.match(MiniGoParser.COMMA)
                self.state = 302
                self.params_list()
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

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 306
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 307
                self.match(MiniGoParser.ID)
                self.state = 308
                self.match(MiniGoParser.COMMA)
                self.state = 309
                self.match(MiniGoParser.ID)
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 310
                    self.match(MiniGoParser.COMMA)
                    self.state = 311
                    self.match(MiniGoParser.ID)
                    self.state = 316
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


            self.state = 319
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declaredContext(ParserRuleContext):
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

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def struct_type_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_type_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declared" ):
                return visitor.visitStruct_declared(self)
            else:
                return visitor.visitChildren(self)




    def struct_declared(self):

        localctx = MiniGoParser.Struct_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_struct_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(MiniGoParser.TYPE)
            self.state = 322
            self.match(MiniGoParser.ID)
            self.state = 323
            self.match(MiniGoParser.STRUCT)
            self.state = 324
            self.match(MiniGoParser.LB)
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 325
                self.match(MiniGoParser.NEWLINE)
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 331
            self.struct_type_list()
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 332
                self.match(MiniGoParser.NEWLINE)
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 338
            self.match(MiniGoParser.RB)
            self.state = 339
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NEWLINE):
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


    class Struct_type_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_fieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type_list" ):
                return visitor.visitStruct_type_list(self)
            else:
                return visitor.visitChildren(self)




    def struct_type_list(self):

        localctx = MiniGoParser.Struct_type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_struct_type_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.struct_field()
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 345
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==MiniGoParser.NEWLINE:
                        self.state = 342
                        self.match(MiniGoParser.NEWLINE)
                        self.state = 347
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 348
                    self.struct_field() 
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def more_ids(self):
            return self.getTypedRuleContext(MiniGoParser.More_idsContext,0)


        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def struct_end(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_endContext,0)


        def method_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_struct_field)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(MiniGoParser.ID)
                self.state = 355
                self.more_ids()
                self.state = 356
                self.type_name()
                self.state = 357
                self.struct_end()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.method_declared()
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


    class More_idsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def more_ids(self):
            return self.getTypedRuleContext(MiniGoParser.More_idsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_ids

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore_ids" ):
                return visitor.visitMore_ids(self)
            else:
                return visitor.visitChildren(self)




    def more_ids(self):

        localctx = MiniGoParser.More_idsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_more_ids)
        try:
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.match(MiniGoParser.COMMA)
                self.state = 364
                self.match(MiniGoParser.ID)
                self.state = 365
                self.more_ids()
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


    class Struct_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_end

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_end" ):
                return visitor.visitStruct_end(self)
            else:
                return visitor.visitChildren(self)




    def struct_end(self):

        localctx = MiniGoParser.Struct_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_struct_end)
        self._la = 0 # Token type
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SEMI:
                    self.state = 369
                    self.match(MiniGoParser.SEMI)


                self.state = 372
                self.match(MiniGoParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,0)


        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_struct_type)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.struct_field()
                self.state = 377
                self.struct_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declaredContext(ParserRuleContext):
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

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declared" ):
                return visitor.visitInterface_declared(self)
            else:
                return visitor.visitChildren(self)




    def interface_declared(self):

        localctx = MiniGoParser.Interface_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_interface_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(MiniGoParser.TYPE)
            self.state = 382
            self.match(MiniGoParser.ID)
            self.state = 383
            self.match(MiniGoParser.INTERFACE)
            self.state = 384
            self.match(MiniGoParser.LB)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 385
                self.match(MiniGoParser.NEWLINE)
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 391
            self.interface_type()
            self.state = 392
            self.match(MiniGoParser.RB)
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 393
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type" ):
                return visitor.visitInterface_type(self)
            else:
                return visitor.visitChildren(self)




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_interface_type)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.interface_method()
                self.state = 398
                self.interface_type()
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


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def optional_params(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_paramsContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def optional_type(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_typeContext,0)


        def optional_semi(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_semiContext,0)


        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method" ):
                return visitor.visitInterface_method(self)
            else:
                return visitor.visitChildren(self)




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_interface_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(MiniGoParser.ID)
            self.state = 403
            self.match(MiniGoParser.LP)
            self.state = 404
            self.optional_params()
            self.state = 405
            self.match(MiniGoParser.RP)
            self.state = 406
            self.optional_type()
            self.state = 407
            self.optional_semi()
            self.state = 408
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Params_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_params" ):
                return visitor.visitOptional_params(self)
            else:
                return visitor.visitChildren(self)




    def optional_params(self):

        localctx = MiniGoParser.Optional_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_optional_params)
        try:
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RP]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.params_list()
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


    class Optional_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_type" ):
                return visitor.visitOptional_type(self)
            else:
                return visitor.visitChildren(self)




    def optional_type(self):

        localctx = MiniGoParser.Optional_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_optional_type)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.type_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_semiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_semi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_semi" ):
                return visitor.visitOptional_semi(self)
            else:
                return visitor.visitChildren(self)




    def optional_semi(self):

        localctx = MiniGoParser.Optional_semiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_optional_semi)
        try:
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RB, MiniGoParser.ID, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.match(MiniGoParser.SEMI)
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


    class Declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_declaredContext,0)


        def constants_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Constants_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement" ):
                return visitor.visitDeclared_statement(self)
            else:
                return visitor.visitChildren(self)




    def declared_statement(self):

        localctx = MiniGoParser.Declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_declared_statement)
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.variables_declared()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.constants_declared()
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


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_lhsContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assign_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.assign_lhs()
            self.state = 427
            self.assign_op()
            self.state = 428
            self.expression(0)
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 429
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

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

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_op" ):
                return visitor.visitAssign_op(self)
            else:
                return visitor.visitChildren(self)




    def assign_op(self):

        localctx = MiniGoParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN) | (1 << MiniGoParser.SHORT_ASSIGN))) != 0)):
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


    class Assign_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def field_access(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Field_accessContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Field_accessContext,i)


        def element_access(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Element_accessContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Element_accessContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs" ):
                return visitor.visitAssign_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_lhs(self):

        localctx = MiniGoParser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_assign_lhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(MiniGoParser.ID)
            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.DOT or _la==MiniGoParser.LSB:
                self.state = 437
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.DOT]:
                    self.state = 435
                    self.field_access()
                    pass
                elif token in [MiniGoParser.LSB]:
                    self.state = 436
                    self.element_access()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 441
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(MiniGoParser.IF)
            self.state = 443
            self.match(MiniGoParser.LP)
            self.state = 444
            self.expression(0)
            self.state = 445
            self.match(MiniGoParser.RP)
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 446
                self.match(MiniGoParser.NEWLINE)


            self.state = 449
            self.block_stmt()
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 450
                self.match(MiniGoParser.NEWLINE)


            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 453
                self.match(MiniGoParser.ELSE)
                self.state = 454
                self.if_statement()

            elif la_ == 2:
                self.state = 455
                self.match(MiniGoParser.ELSE)
                self.state = 456
                self.block_stmt()


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

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def for_init(self):
            return self.getTypedRuleContext(MiniGoParser.For_initContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def for_update(self):
            return self.getTypedRuleContext(MiniGoParser.For_updateContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def UNDERSCORE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.UNDERSCORE)
            else:
                return self.getToken(MiniGoParser.UNDERSCORE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(MiniGoParser.FOR)
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 460
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 461
                self.match(MiniGoParser.COMMA)
                self.state = 462
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 463
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 464
                self.match(MiniGoParser.RANGE)
                self.state = 465
                self.expression(0)
                self.state = 466
                self.block_stmt()
                pass

            elif la_ == 2:
                self.state = 468
                self.for_init()
                self.state = 469
                self.match(MiniGoParser.SEMI)
                self.state = 470
                self.expression(0)
                self.state = 471
                self.match(MiniGoParser.SEMI)
                self.state = 472
                self.for_update()
                self.state = 473
                self.block_stmt()
                pass

            elif la_ == 3:
                self.state = 475
                self.expression(0)
                self.state = 476
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_lhsContext,0)


        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_init" ):
                return visitor.visitFor_init(self)
            else:
                return visitor.visitChildren(self)




    def for_init(self):

        localctx = MiniGoParser.For_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_for_init)
        self._la = 0 # Token type
        try:
            self.state = 495
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.assign_lhs()
                self.state = 481
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 482
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
                self.assign_lhs()
                self.state = 485
                self.assign_op()
                self.state = 486
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 488
                self.match(MiniGoParser.VAR)
                self.state = 489
                self.match(MiniGoParser.ID)
                self.state = 491
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 490
                    self.type_name()


                self.state = 493
                self.match(MiniGoParser.ASSIGN)
                self.state = 494
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_updateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_lhsContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_update" ):
                return visitor.visitFor_update(self)
            else:
                return visitor.visitChildren(self)




    def for_update(self):

        localctx = MiniGoParser.For_updateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_for_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.assign_lhs()
            self.state = 498
            self.assign_op()
            self.state = 499
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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(MiniGoParser.BREAK)
            self.state = 502
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NEWLINE):
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


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(MiniGoParser.CONTINUE)
            self.state = 505
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NEWLINE):
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


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

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
            self.state = 507
            self.match(MiniGoParser.RETURN)
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 509
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 508
                    self.expression(0)


                self.state = 511
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.state = 513
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 512
                    self.expression(0)


                self.state = 515
                self.match(MiniGoParser.NEWLINE)
                pass


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

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assign_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_lhsContext,0)


        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 518
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 519
                self.assign_lhs()
                pass


            self.state = 522
            self.match(MiniGoParser.LP)
            self.state = 524
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 523
                self.list_expression()


            self.state = 526
            self.match(MiniGoParser.RP)
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 527
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = MiniGoParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 530
                self.match(MiniGoParser.NEWLINE)


            self.state = 533
            self.match(MiniGoParser.LB)
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 534
                self.match(MiniGoParser.NEWLINE)


            self.state = 541
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 539
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                        self.state = 537
                        self.statement()
                        pass
                    elif token in [MiniGoParser.NEWLINE]:
                        self.state = 538
                        self.match(MiniGoParser.NEWLINE)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 543
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 544
                self.match(MiniGoParser.NEWLINE)


            self.state = 547
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr_list)
        try:
            self.state = 554
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 549
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 550
                self.expression(0)
                self.state = 551
                self.match(MiniGoParser.COMMA)
                self.state = 552
                self.expr_list()
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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 564
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 559
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 560
                    self.match(MiniGoParser.OR)
                    self.state = 561
                    self.expression1(0) 
                self.state = 566
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 575
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 570
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 571
                    self.match(MiniGoParser.AND)
                    self.state = 572
                    self.expression2(0) 
                self.state = 577
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

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


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MiniGoParser.NOT_EQUAL, 0)

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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 586
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 581
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 582
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.EQUAL or _la==MiniGoParser.NOT_EQUAL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 583
                    self.expression3(0) 
                self.state = 588
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

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


        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(MiniGoParser.LESS_OR_EQUAL, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(MiniGoParser.GREATER_OR_EQUAL, 0)

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
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 597
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 592
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 593
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESS_OR_EQUAL) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 594
                    self.expression4(0) 
                self.state = 599
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

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


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

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
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 608
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,68,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 603
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 604
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 605
                    self.expression5(0) 
                self.state = 610
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

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

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)



    def expression5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_expression5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 619
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 614
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 615
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 616
                    self.expression6() 
                self.state = 621
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = MiniGoParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_expression6)
        try:
            self.state = 627
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 622
                self.match(MiniGoParser.NOT)
                self.state = 623
                self.expression6()
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 624
                self.match(MiniGoParser.SUB)
                self.state = 625
                self.expression6()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 626
                self.expression7()
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


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def element_access(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Element_accessContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Element_accessContext,i)


        def field_access(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Field_accessContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Field_accessContext,i)


        def call_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Call_exprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Call_exprContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_expression7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.operand()
            self.state = 635
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,72,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 633
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSB]:
                        self.state = 630
                        self.element_access()
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 631
                        self.field_access()
                        pass
                    elif token in [MiniGoParser.LP]:
                        self.state = 632
                        self.call_expr()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 637
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_operand)
        try:
            self.state = 644
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 638
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 639
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 640
                self.match(MiniGoParser.LP)
                self.state = 641
                self.expression(0)
                self.state = 642
                self.match(MiniGoParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_element_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_access" ):
                return visitor.visitElement_access(self)
            else:
                return visitor.visitChildren(self)




    def element_access(self):

        localctx = MiniGoParser.Element_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_element_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            self.match(MiniGoParser.LSB)
            self.state = 647
            self.expression(0)
            self.state = 648
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_field_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_access" ):
                return visitor.visitField_access(self)
            else:
                return visitor.visitChildren(self)




    def field_access(self):

        localctx = MiniGoParser.Field_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_field_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 650
            self.match(MiniGoParser.DOT)
            self.state = 651
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_expr" ):
                return visitor.visitCall_expr(self)
            else:
                return visitor.visitChildren(self)




    def call_expr(self):

        localctx = MiniGoParser.Call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_call_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 653
            self.match(MiniGoParser.LP)
            self.state = 655
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 654
                self.list_expression()


            self.state = 657
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
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

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

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
        self.enterRule(localctx, 114, self.RULE_literal)
        try:
            self.state = 667
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 659
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 660
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 661
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 662
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 663
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 664
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 665
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 666
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


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 669
            self.array_type()
            self.state = 670
            self.match(MiniGoParser.LB)
            self.state = 671
            self.list_expression()
            self.state = 672
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LSB)
            else:
                return self.getToken(MiniGoParser.LSB, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INT_LIT)
            else:
                return self.getToken(MiniGoParser.INT_LIT, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RSB)
            else:
                return self.getToken(MiniGoParser.RSB, i)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 674
            self.match(MiniGoParser.LSB)
            self.state = 675
            self.match(MiniGoParser.INT_LIT)
            self.state = 676
            self.match(MiniGoParser.RSB)
            self.state = 682
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,76,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 677
                    self.match(MiniGoParser.LSB)
                    self.state = 678
                    self.match(MiniGoParser.INT_LIT)
                    self.state = 679
                    self.match(MiniGoParser.RSB) 
                self.state = 684
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,76,self._ctx)

            self.state = 685
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = MiniGoParser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_type_name)
        try:
            self.state = 693
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 687
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 688
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 689
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 690
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 691
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 692
                self.array_type()
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


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 695
            self.match(MiniGoParser.ID)
            self.state = 696
            self.match(MiniGoParser.LB)
            self.state = 698
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 697
                self.field_list()


            self.state = 700
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_init(self):
            return self.getTypedRuleContext(MiniGoParser.Field_initContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_list" ):
                return visitor.visitField_list(self)
            else:
                return visitor.visitChildren(self)




    def field_list(self):

        localctx = MiniGoParser.Field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_field_list)
        try:
            self.state = 707
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 702
                self.field_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 703
                self.field_init()
                self.state = 704
                self.match(MiniGoParser.COMMA)
                self.state = 705
                self.field_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_initContext(ParserRuleContext):
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
            return MiniGoParser.RULE_field_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_init" ):
                return visitor.visitField_init(self)
            else:
                return visitor.visitChildren(self)




    def field_init(self):

        localctx = MiniGoParser.Field_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_field_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 709
            self.match(MiniGoParser.ID)
            self.state = 710
            self.match(MiniGoParser.COLON)
            self.state = 711
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
        self.enterRule(localctx, 128, self.RULE_list_expression)
        try:
            self.state = 718
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 713
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 714
                self.expression(0)
                self.state = 715
                self.match(MiniGoParser.COMMA)
                self.state = 716
                self.list_expression()
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
        self._predicates[45] = self.expression_sempred
        self._predicates[46] = self.expression1_sempred
        self._predicates[47] = self.expression2_sempred
        self._predicates[48] = self.expression3_sempred
        self._predicates[49] = self.expression4_sempred
        self._predicates[50] = self.expression5_sempred
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
         

    def expression5_sempred(self, localctx:Expression5Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         





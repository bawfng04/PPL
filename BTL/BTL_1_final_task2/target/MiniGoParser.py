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
        buf.write("\u033a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\5\3\u009a\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u00a1\n")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00a9\n\5\3\5\7\5\u00ac")
        buf.write("\n\5\f\5\16\5\u00af\13\5\3\6\3\6\3\6\3\6\3\6\5\6\u00b6")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00c0\n\7\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t\u00cb\n\t\3\n\3\n")
        buf.write("\3\n\3\n\5\n\u00d1\n\n\3\n\3\n\3\n\7\n\u00d6\n\n\f\n\16")
        buf.write("\n\u00d9\13\n\3\n\3\n\3\n\5\n\u00de\n\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\7\n\u00e6\n\n\f\n\16\n\u00e9\13\n\3\n\3\n\5")
        buf.write("\n\u00ed\n\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u00f8\n\f\3\r\3\r\3\r\3\r\3\16\5\16\u00ff\n\16\3\16")
        buf.write("\3\16\5\16\u0103\n\16\3\16\3\16\3\16\7\16\u0108\n\16\f")
        buf.write("\16\16\16\u010b\13\16\3\16\5\16\u010e\n\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u0116\n\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u011d\n\17\f\17\16\17\u0120\13\17\3\17\3\17")
        buf.write("\3\17\5\17\u0125\n\17\3\17\5\17\u0128\n\17\3\17\3\17\5")
        buf.write("\17\u012c\n\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u0138\n\21\3\21\3\21\5\21\u013c\n\21\3")
        buf.write("\21\5\21\u013f\n\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\5\22\u0149\n\22\3\23\3\23\3\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\7\24\u0153\n\24\f\24\16\24\u0156\13\24\3\24\3")
        buf.write("\24\3\24\3\24\7\24\u015c\n\24\f\24\16\24\u015f\13\24\5")
        buf.write("\24\u0161\n\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u0169")
        buf.write("\n\25\f\25\16\25\u016c\13\25\5\25\u016e\n\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\7\26\u0177\n\26\f\26\16\26\u017a")
        buf.write("\13\26\3\26\3\26\7\26\u017e\n\26\f\26\16\26\u0181\13\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\7\27\u0188\n\27\f\27\16\27\u018b")
        buf.write("\13\27\6\27\u018d\n\27\r\27\16\27\u018e\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\5\30\u0197\n\30\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u019d\n\31\3\32\3\32\5\32\u01a1\n\32\3\32\5\32\u01a4")
        buf.write("\n\32\3\33\3\33\3\33\3\33\5\33\u01aa\n\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\7\34\u01b1\n\34\f\34\16\34\u01b4\13\34\3")
        buf.write("\34\3\34\7\34\u01b8\n\34\f\34\16\34\u01bb\13\34\3\34\3")
        buf.write("\34\3\34\3\35\6\35\u01c1\n\35\r\35\16\35\u01c2\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u01c9\n\36\3\37\3\37\3\37\5\37\u01ce")
        buf.write("\n\37\3\37\3\37\5\37\u01d2\n\37\3\37\3\37\3\37\3\37\5")
        buf.write("\37\u01d8\n\37\3\37\3\37\5\37\u01dc\n\37\3\37\5\37\u01df")
        buf.write("\n\37\3 \3 \5 \u01e3\n \3!\3!\5!\u01e7\n!\3\"\3\"\5\"")
        buf.write("\u01eb\n\"\3#\3#\5#\u01ef\n#\3$\3$\3$\3$\5$\u01f5\n$\3")
        buf.write("%\3%\3&\3&\3&\7&\u01fc\n&\f&\16&\u01ff\13&\3\'\3\'\3\'")
        buf.write("\3\'\3\'\5\'\u0206\n\'\3\'\3\'\5\'\u020a\n\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u0210\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write("\3(\3(\3(\3(\3(\3(\3(\3(\5(\u0225\n(\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\5)\u0232\n)\3)\3)\5)\u0236\n)\3*\3*\3")
        buf.write("*\3*\3+\3+\3+\3,\3,\3,\3-\3-\5-\u0244\n-\3-\3-\5-\u0248")
        buf.write("\n-\3-\5-\u024b\n-\3.\3.\5.\u024f\n.\3.\3.\5.\u0253\n")
        buf.write(".\3.\3.\5.\u0257\n.\3/\5/\u025a\n/\3/\3/\5/\u025e\n/\3")
        buf.write("/\3/\7/\u0262\n/\f/\16/\u0265\13/\3/\5/\u0268\n/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\5\60\u0271\n\60\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\7\61\u0279\n\61\f\61\16\61\u027c\13")
        buf.write("\61\3\62\3\62\3\62\3\62\3\62\3\62\7\62\u0284\n\62\f\62")
        buf.write("\16\62\u0287\13\62\3\63\3\63\3\63\3\63\3\63\3\63\7\63")
        buf.write("\u028f\n\63\f\63\16\63\u0292\13\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\7\64\u029a\n\64\f\64\16\64\u029d\13\64\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\7\65\u02a5\n\65\f\65\16\65\u02a8")
        buf.write("\13\65\3\66\3\66\3\66\3\66\3\66\3\66\7\66\u02b0\n\66\f")
        buf.write("\66\16\66\u02b3\13\66\3\67\3\67\3\67\3\67\3\67\5\67\u02ba")
        buf.write("\n\67\38\38\38\38\78\u02c0\n8\f8\168\u02c3\138\39\39\3")
        buf.write("9\39\39\39\59\u02cb\n9\3:\3:\3:\3:\3;\3;\3;\3<\3<\5<\u02d6")
        buf.write("\n<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\5=\u02e3\n=\3>\3")
        buf.write(">\3>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u02f7")
        buf.write("\n@\3A\3A\3A\7A\u02fc\nA\fA\16A\u02ff\13A\3B\3B\3B\3B")
        buf.write("\3B\3B\3B\3B\3B\5B\u030a\nB\3C\3C\3C\3C\3C\3C\7C\u0312")
        buf.write("\nC\fC\16C\u0315\13C\3C\3C\3D\3D\3D\3D\3D\3D\5D\u031f")
        buf.write("\nD\3E\3E\3E\5E\u0324\nE\3E\3E\3F\3F\3F\3F\3F\5F\u032d")
        buf.write("\nF\3G\3G\3G\3G\3H\3H\3H\3H\3H\5H\u0338\nH\3H\2\b`bdf")
        buf.write("hjI\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\2\n\4\2\66\66;;\4")
        buf.write("\2\t\n\67\67\4\2%*--\4\2..\67\67\3\2\34\35\3\2\36!\3\2")
        buf.write("\27\30\3\2\31\33\2\u0377\2\u0090\3\2\2\2\4\u0099\3\2\2")
        buf.write("\2\6\u00a0\3\2\2\2\b\u00a8\3\2\2\2\n\u00b5\3\2\2\2\f\u00bf")
        buf.write("\3\2\2\2\16\u00c1\3\2\2\2\20\u00ca\3\2\2\2\22\u00ec\3")
        buf.write("\2\2\2\24\u00ee\3\2\2\2\26\u00f7\3\2\2\2\30\u00f9\3\2")
        buf.write("\2\2\32\u00fe\3\2\2\2\34\u0111\3\2\2\2\36\u012d\3\2\2")
        buf.write("\2 \u0130\3\2\2\2\"\u0148\3\2\2\2$\u014a\3\2\2\2&\u0160")
        buf.write("\3\2\2\2(\u016d\3\2\2\2*\u0171\3\2\2\2,\u018c\3\2\2\2")
        buf.write(".\u0196\3\2\2\2\60\u019c\3\2\2\2\62\u01a3\3\2\2\2\64\u01a9")
        buf.write("\3\2\2\2\66\u01ab\3\2\2\28\u01c0\3\2\2\2:\u01c8\3\2\2")
        buf.write("\2<\u01de\3\2\2\2>\u01e2\3\2\2\2@\u01e6\3\2\2\2B\u01ea")
        buf.write("\3\2\2\2D\u01ee\3\2\2\2F\u01f0\3\2\2\2H\u01f6\3\2\2\2")
        buf.write("J\u01f8\3\2\2\2L\u0200\3\2\2\2N\u0211\3\2\2\2P\u0235\3")
        buf.write("\2\2\2R\u0237\3\2\2\2T\u023b\3\2\2\2V\u023e\3\2\2\2X\u0241")
        buf.write("\3\2\2\2Z\u024e\3\2\2\2\\\u0259\3\2\2\2^\u0270\3\2\2\2")
        buf.write("`\u0272\3\2\2\2b\u027d\3\2\2\2d\u0288\3\2\2\2f\u0293\3")
        buf.write("\2\2\2h\u029e\3\2\2\2j\u02a9\3\2\2\2l\u02b9\3\2\2\2n\u02bb")
        buf.write("\3\2\2\2p\u02ca\3\2\2\2r\u02cc\3\2\2\2t\u02d0\3\2\2\2")
        buf.write("v\u02d3\3\2\2\2x\u02e2\3\2\2\2z\u02e4\3\2\2\2|\u02e9\3")
        buf.write("\2\2\2~\u02f6\3\2\2\2\u0080\u02f8\3\2\2\2\u0082\u0309")
        buf.write("\3\2\2\2\u0084\u030b\3\2\2\2\u0086\u031e\3\2\2\2\u0088")
        buf.write("\u0320\3\2\2\2\u008a\u032c\3\2\2\2\u008c\u032e\3\2\2\2")
        buf.write("\u008e\u0337\3\2\2\2\u0090\u0091\5\4\3\2\u0091\u0092\5")
        buf.write("\b\5\2\u0092\u0093\5\6\4\2\u0093\u0094\5\4\3\2\u0094\u0095")
        buf.write("\7\2\2\3\u0095\3\3\2\2\2\u0096\u009a\3\2\2\2\u0097\u0098")
        buf.write("\7;\2\2\u0098\u009a\5\4\3\2\u0099\u0096\3\2\2\2\u0099")
        buf.write("\u0097\3\2\2\2\u009a\5\3\2\2\2\u009b\u00a1\3\2\2\2\u009c")
        buf.write("\u009d\5\4\3\2\u009d\u009e\5\b\5\2\u009e\u009f\5\6\4\2")
        buf.write("\u009f\u00a1\3\2\2\2\u00a0\u009b\3\2\2\2\u00a0\u009c\3")
        buf.write("\2\2\2\u00a1\7\3\2\2\2\u00a2\u00a9\5\16\b\2\u00a3\u00a9")
        buf.write("\5\24\13\2\u00a4\u00a9\5\34\17\2\u00a5\u00a9\5 \21\2\u00a6")
        buf.write("\u00a9\5*\26\2\u00a7\u00a9\5\66\34\2\u00a8\u00a2\3\2\2")
        buf.write("\2\u00a8\u00a3\3\2\2\2\u00a8\u00a4\3\2\2\2\u00a8\u00a5")
        buf.write("\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9")
        buf.write("\u00ad\3\2\2\2\u00aa\u00ac\7;\2\2\u00ab\u00aa\3\2\2\2")
        buf.write("\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3")
        buf.write("\2\2\2\u00ae\t\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b6")
        buf.write("\5\f\7\2\u00b1\u00b2\5\f\7\2\u00b2\u00b3\5\4\3\2\u00b3")
        buf.write("\u00b4\5\n\6\2\u00b4\u00b6\3\2\2\2\u00b5\u00b0\3\2\2\2")
        buf.write("\u00b5\u00b1\3\2\2\2\u00b6\13\3\2\2\2\u00b7\u00c0\5D#")
        buf.write("\2\u00b8\u00c0\5F$\2\u00b9\u00c0\5L\'\2\u00ba\u00c0\5")
        buf.write("N(\2\u00bb\u00c0\5T+\2\u00bc\u00c0\5V,\2\u00bd\u00c0\5")
        buf.write("Z.\2\u00be\u00c0\5X-\2\u00bf\u00b7\3\2\2\2\u00bf\u00b8")
        buf.write("\3\2\2\2\u00bf\u00b9\3\2\2\2\u00bf\u00ba\3\2\2\2\u00bf")
        buf.write("\u00bb\3\2\2\2\u00bf\u00bc\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00bf\u00be\3\2\2\2\u00c0\r\3\2\2\2\u00c1\u00c2\7\20")
        buf.write("\2\2\u00c2\u00c3\5\20\t\2\u00c3\u00c4\t\2\2\2\u00c4\17")
        buf.write("\3\2\2\2\u00c5\u00cb\5\22\n\2\u00c6\u00c7\5\22\n\2\u00c7")
        buf.write("\u00c8\7\65\2\2\u00c8\u00c9\5\20\t\2\u00c9\u00cb\3\2\2")
        buf.write("\2\u00ca\u00c5\3\2\2\2\u00ca\u00c6\3\2\2\2\u00cb\21\3")
        buf.write("\2\2\2\u00cc\u00cd\7\67\2\2\u00cd\u00d0\5\u0086D\2\u00ce")
        buf.write("\u00cf\7%\2\2\u00cf\u00d1\5`\61\2\u00d0\u00ce\3\2\2\2")
        buf.write("\u00d0\u00d1\3\2\2\2\u00d1\u00ed\3\2\2\2\u00d2\u00d7\7")
        buf.write("\67\2\2\u00d3\u00d4\7\65\2\2\u00d4\u00d6\7\67\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2")
        buf.write("\u00d7\u00d8\3\2\2\2\u00d8\u00da\3\2\2\2\u00d9\u00d7\3")
        buf.write("\2\2\2\u00da\u00dd\5\u0086D\2\u00db\u00dc\7%\2\2\u00dc")
        buf.write("\u00de\5^\60\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write("\u00de\u00ed\3\2\2\2\u00df\u00e0\7\67\2\2\u00e0\u00e1")
        buf.write("\7%\2\2\u00e1\u00ed\5`\61\2\u00e2\u00e7\7\67\2\2\u00e3")
        buf.write("\u00e4\7\65\2\2\u00e4\u00e6\7\67\2\2\u00e5\u00e3\3\2\2")
        buf.write("\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8")
        buf.write("\3\2\2\2\u00e8\u00ea\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea")
        buf.write("\u00eb\7%\2\2\u00eb\u00ed\5^\60\2\u00ec\u00cc\3\2\2\2")
        buf.write("\u00ec\u00d2\3\2\2\2\u00ec\u00df\3\2\2\2\u00ec\u00e2\3")
        buf.write("\2\2\2\u00ed\23\3\2\2\2\u00ee\u00ef\7\17\2\2\u00ef\u00f0")
        buf.write("\5\26\f\2\u00f0\u00f1\t\2\2\2\u00f1\25\3\2\2\2\u00f2\u00f8")
        buf.write("\5\30\r\2\u00f3\u00f4\5\30\r\2\u00f4\u00f5\7\65\2\2\u00f5")
        buf.write("\u00f6\5\26\f\2\u00f6\u00f8\3\2\2\2\u00f7\u00f2\3\2\2")
        buf.write("\2\u00f7\u00f3\3\2\2\2\u00f8\27\3\2\2\2\u00f9\u00fa\7")
        buf.write("\67\2\2\u00fa\u00fb\7%\2\2\u00fb\u00fc\5`\61\2\u00fc\31")
        buf.write("\3\2\2\2\u00fd\u00ff\7;\2\2\u00fe\u00fd\3\2\2\2\u00fe")
        buf.write("\u00ff\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0102\7\61\2")
        buf.write("\2\u0101\u0103\7;\2\2\u0102\u0101\3\2\2\2\u0102\u0103")
        buf.write("\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0109\5\f\7\2\u0105")
        buf.write("\u0108\5\f\7\2\u0106\u0108\7;\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0107\u0106\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3")
        buf.write("\2\2\2\u0109\u010a\3\2\2\2\u010a\u010d\3\2\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010c\u010e\7;\2\2\u010d\u010c\3\2\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\7\62\2")
        buf.write("\2\u0110\33\3\2\2\2\u0111\u0112\7\7\2\2\u0112\u0113\7")
        buf.write("\67\2\2\u0113\u0115\7/\2\2\u0114\u0116\5&\24\2\u0115\u0114")
        buf.write("\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write("\u0124\7\60\2\2\u0118\u0119\7/\2\2\u0119\u011e\5\u0086")
        buf.write("D\2\u011a\u011b\7\65\2\2\u011b\u011d\5\u0086D\2\u011c")
        buf.write("\u011a\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c\3\2\2\2")
        buf.write("\u011e\u011f\3\2\2\2\u011f\u0121\3\2\2\2\u0120\u011e\3")
        buf.write("\2\2\2\u0121\u0122\7\60\2\2\u0122\u0125\3\2\2\2\u0123")
        buf.write("\u0125\5\u0086D\2\u0124\u0118\3\2\2\2\u0124\u0123\3\2")
        buf.write("\2\2\u0124\u0125\3\2\2\2\u0125\u0127\3\2\2\2\u0126\u0128")
        buf.write("\7;\2\2\u0127\u0126\3\2\2\2\u0127\u0128\3\2\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129\u012b\5\32\16\2\u012a\u012c\7\66")
        buf.write("\2\2\u012b\u012a\3\2\2\2\u012b\u012c\3\2\2\2\u012c\35")
        buf.write("\3\2\2\2\u012d\u012e\7\67\2\2\u012e\u012f\t\3\2\2\u012f")
        buf.write("\37\3\2\2\2\u0130\u0131\7\7\2\2\u0131\u0132\7/\2\2\u0132")
        buf.write("\u0133\5\36\20\2\u0133\u0134\7\60\2\2\u0134\u0135\7\67")
        buf.write("\2\2\u0135\u0137\7/\2\2\u0136\u0138\5&\24\2\u0137\u0136")
        buf.write("\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0139\3\2\2\2\u0139")
        buf.write("\u013b\7\60\2\2\u013a\u013c\5\u0086D\2\u013b\u013a\3\2")
        buf.write("\2\2\u013b\u013c\3\2\2\2\u013c\u013e\3\2\2\2\u013d\u013f")
        buf.write("\7;\2\2\u013e\u013d\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u0141\5\\/\2\u0141\u0142\t\2\2\2")
        buf.write("\u0142!\3\2\2\2\u0143\u0149\5$\23\2\u0144\u0145\5$\23")
        buf.write("\2\u0145\u0146\7\65\2\2\u0146\u0147\5\"\22\2\u0147\u0149")
        buf.write("\3\2\2\2\u0148\u0143\3\2\2\2\u0148\u0144\3\2\2\2\u0149")
        buf.write("#\3\2\2\2\u014a\u014b\7\67\2\2\u014b\u014c\5\u0086D\2")
        buf.write("\u014c%\3\2\2\2\u014d\u014e\7\67\2\2\u014e\u0161\5\u0086")
        buf.write("D\2\u014f\u0154\7\67\2\2\u0150\u0151\7\65\2\2\u0151\u0153")
        buf.write("\7\67\2\2\u0152\u0150\3\2\2\2\u0153\u0156\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0157\3\2\2\2")
        buf.write("\u0156\u0154\3\2\2\2\u0157\u0161\5\u0086D\2\u0158\u015d")
        buf.write("\5(\25\2\u0159\u015a\7\65\2\2\u015a\u015c\5(\25\2\u015b")
        buf.write("\u0159\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2")
        buf.write("\u015d\u015e\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d\3")
        buf.write("\2\2\2\u0160\u014d\3\2\2\2\u0160\u014f\3\2\2\2\u0160\u0158")
        buf.write("\3\2\2\2\u0161\'\3\2\2\2\u0162\u016e\7\67\2\2\u0163\u0164")
        buf.write("\7\67\2\2\u0164\u0165\7\65\2\2\u0165\u016a\7\67\2\2\u0166")
        buf.write("\u0167\7\65\2\2\u0167\u0169\7\67\2\2\u0168\u0166\3\2\2")
        buf.write("\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b")
        buf.write("\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016d")
        buf.write("\u0162\3\2\2\2\u016d\u0163\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u0170\5\u0086D\2\u0170)\3\2\2\2\u0171\u0172\7\b")
        buf.write("\2\2\u0172\u0173\7\67\2\2\u0173\u0174\7\t\2\2\u0174\u0178")
        buf.write("\7\61\2\2\u0175\u0177\7;\2\2\u0176\u0175\3\2\2\2\u0177")
        buf.write("\u017a\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179\u017b\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017f\5")
        buf.write(",\27\2\u017c\u017e\7;\2\2\u017d\u017c\3\2\2\2\u017e\u0181")
        buf.write("\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0182\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0183\7\62\2")
        buf.write("\2\u0183\u0184\t\2\2\2\u0184+\3\2\2\2\u0185\u0189\5.\30")
        buf.write("\2\u0186\u0188\7;\2\2\u0187\u0186\3\2\2\2\u0188\u018b")
        buf.write("\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u0185\3\2\2\2")
        buf.write("\u018d\u018e\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3")
        buf.write("\2\2\2\u018f-\3\2\2\2\u0190\u0191\7\67\2\2\u0191\u0192")
        buf.write("\5\60\31\2\u0192\u0193\5\u0086D\2\u0193\u0194\5\62\32")
        buf.write("\2\u0194\u0197\3\2\2\2\u0195\u0197\5 \21\2\u0196\u0190")
        buf.write("\3\2\2\2\u0196\u0195\3\2\2\2\u0197/\3\2\2\2\u0198\u019d")
        buf.write("\3\2\2\2\u0199\u019a\7\65\2\2\u019a\u019b\7\67\2\2\u019b")
        buf.write("\u019d\5\60\31\2\u019c\u0198\3\2\2\2\u019c\u0199\3\2\2")
        buf.write("\2\u019d\61\3\2\2\2\u019e\u01a4\7\66\2\2\u019f\u01a1\7")
        buf.write("\66\2\2\u01a0\u019f\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a4\7;\2\2\u01a3\u019e\3\2\2\2")
        buf.write("\u01a3\u01a0\3\2\2\2\u01a4\63\3\2\2\2\u01a5\u01aa\3\2")
        buf.write("\2\2\u01a6\u01a7\5.\30\2\u01a7\u01a8\5\64\33\2\u01a8\u01aa")
        buf.write("\3\2\2\2\u01a9\u01a5\3\2\2\2\u01a9\u01a6\3\2\2\2\u01aa")
        buf.write("\65\3\2\2\2\u01ab\u01ac\7\b\2\2\u01ac\u01ad\7\67\2\2\u01ad")
        buf.write("\u01ae\7\n\2\2\u01ae\u01b2\7\61\2\2\u01af\u01b1\7;\2\2")
        buf.write("\u01b0\u01af\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3")
        buf.write("\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01b2")
        buf.write("\3\2\2\2\u01b5\u01b9\58\35\2\u01b6\u01b8\7;\2\2\u01b7")
        buf.write("\u01b6\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2")
        buf.write("\u01b9\u01ba\3\2\2\2\u01ba\u01bc\3\2\2\2\u01bb\u01b9\3")
        buf.write("\2\2\2\u01bc\u01bd\7\62\2\2\u01bd\u01be\t\2\2\2\u01be")
        buf.write("\67\3\2\2\2\u01bf\u01c1\5<\37\2\u01c0\u01bf\3\2\2\2\u01c1")
        buf.write("\u01c2\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2")
        buf.write("\u01c39\3\2\2\2\u01c4\u01c9\3\2\2\2\u01c5\u01c6\5<\37")
        buf.write("\2\u01c6\u01c7\5:\36\2\u01c7\u01c9\3\2\2\2\u01c8\u01c4")
        buf.write("\3\2\2\2\u01c8\u01c5\3\2\2\2\u01c9;\3\2\2\2\u01ca\u01cb")
        buf.write("\7\67\2\2\u01cb\u01cd\7/\2\2\u01cc\u01ce\5&\24\2\u01cd")
        buf.write("\u01cc\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\3\2\2\2")
        buf.write("\u01cf\u01d1\7\60\2\2\u01d0\u01d2\5\u0086D\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3")
        buf.write("\u01df\t\2\2\2\u01d4\u01d5\7\67\2\2\u01d5\u01d7\7/\2\2")
        buf.write("\u01d6\u01d8\5&\24\2\u01d7\u01d6\3\2\2\2\u01d7\u01d8\3")
        buf.write("\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01db\7\60\2\2\u01da")
        buf.write("\u01dc\5\u0086D\2\u01db\u01da\3\2\2\2\u01db\u01dc\3\2")
        buf.write("\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\t\2\2\2\u01de\u01ca")
        buf.write("\3\2\2\2\u01de\u01d4\3\2\2\2\u01df=\3\2\2\2\u01e0\u01e3")
        buf.write("\3\2\2\2\u01e1\u01e3\5&\24\2\u01e2\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e1\3\2\2\2\u01e3?\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5")
        buf.write("\u01e7\5\u0086D\2\u01e6\u01e4\3\2\2\2\u01e6\u01e5\3\2")
        buf.write("\2\2\u01e7A\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01eb\7")
        buf.write("\66\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01e9\3\2\2\2\u01eb")
        buf.write("C\3\2\2\2\u01ec\u01ef\5\16\b\2\u01ed\u01ef\5\24\13\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ed\3\2\2\2\u01efE\3\2\2\2\u01f0")
        buf.write("\u01f1\5J&\2\u01f1\u01f2\5H%\2\u01f2\u01f4\5`\61\2\u01f3")
        buf.write("\u01f5\7\66\2\2\u01f4\u01f3\3\2\2\2\u01f4\u01f5\3\2\2")
        buf.write("\2\u01f5G\3\2\2\2\u01f6\u01f7\t\4\2\2\u01f7I\3\2\2\2\u01f8")
        buf.write("\u01fd\7\67\2\2\u01f9\u01fc\5t;\2\u01fa\u01fc\5r:\2\u01fb")
        buf.write("\u01f9\3\2\2\2\u01fb\u01fa\3\2\2\2\u01fc\u01ff\3\2\2\2")
        buf.write("\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01feK\3\2\2")
        buf.write("\2\u01ff\u01fd\3\2\2\2\u0200\u0201\7\3\2\2\u0201\u0202")
        buf.write("\7/\2\2\u0202\u0203\5`\61\2\u0203\u0205\7\60\2\2\u0204")
        buf.write("\u0206\7;\2\2\u0205\u0204\3\2\2\2\u0205\u0206\3\2\2\2")
        buf.write("\u0206\u0207\3\2\2\2\u0207\u0209\5\\/\2\u0208\u020a\7")
        buf.write(";\2\2\u0209\u0208\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020f")
        buf.write("\3\2\2\2\u020b\u020c\7\4\2\2\u020c\u0210\5L\'\2\u020d")
        buf.write("\u020e\7\4\2\2\u020e\u0210\5\\/\2\u020f\u020b\3\2\2\2")
        buf.write("\u020f\u020d\3\2\2\2\u020f\u0210\3\2\2\2\u0210M\3\2\2")
        buf.write("\2\u0211\u0224\7\5\2\2\u0212\u0213\t\5\2\2\u0213\u0214")
        buf.write("\7\65\2\2\u0214\u0215\t\5\2\2\u0215\u0216\7-\2\2\u0216")
        buf.write("\u0217\7\23\2\2\u0217\u0218\5`\61\2\u0218\u0219\5\\/\2")
        buf.write("\u0219\u0225\3\2\2\2\u021a\u021b\5P)\2\u021b\u021c\7\66")
        buf.write("\2\2\u021c\u021d\5`\61\2\u021d\u021e\7\66\2\2\u021e\u021f")
        buf.write("\5R*\2\u021f\u0220\5\\/\2\u0220\u0225\3\2\2\2\u0221\u0222")
        buf.write("\5`\61\2\u0222\u0223\5\\/\2\u0223\u0225\3\2\2\2\u0224")
        buf.write("\u0212\3\2\2\2\u0224\u021a\3\2\2\2\u0224\u0221\3\2\2\2")
        buf.write("\u0225O\3\2\2\2\u0226\u0227\5J&\2\u0227\u0228\7-\2\2\u0228")
        buf.write("\u0229\5`\61\2\u0229\u0236\3\2\2\2\u022a\u022b\5J&\2\u022b")
        buf.write("\u022c\5H%\2\u022c\u022d\5`\61\2\u022d\u0236\3\2\2\2\u022e")
        buf.write("\u022f\7\20\2\2\u022f\u0231\7\67\2\2\u0230\u0232\5\u0086")
        buf.write("D\2\u0231\u0230\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0233")
        buf.write("\3\2\2\2\u0233\u0234\7%\2\2\u0234\u0236\5`\61\2\u0235")
        buf.write("\u0226\3\2\2\2\u0235\u022a\3\2\2\2\u0235\u022e\3\2\2\2")
        buf.write("\u0236Q\3\2\2\2\u0237\u0238\5J&\2\u0238\u0239\5H%\2\u0239")
        buf.write("\u023a\5`\61\2\u023aS\3\2\2\2\u023b\u023c\7\22\2\2\u023c")
        buf.write("\u023d\t\2\2\2\u023dU\3\2\2\2\u023e\u023f\7\21\2\2\u023f")
        buf.write("\u0240\t\2\2\2\u0240W\3\2\2\2\u0241\u024a\7\6\2\2\u0242")
        buf.write("\u0244\5`\61\2\u0243\u0242\3\2\2\2\u0243\u0244\3\2\2\2")
        buf.write("\u0244\u0245\3\2\2\2\u0245\u024b\7\66\2\2\u0246\u0248")
        buf.write("\5`\61\2\u0247\u0246\3\2\2\2\u0247\u0248\3\2\2\2\u0248")
        buf.write("\u0249\3\2\2\2\u0249\u024b\7;\2\2\u024a\u0243\3\2\2\2")
        buf.write("\u024a\u0247\3\2\2\2\u024bY\3\2\2\2\u024c\u024f\7\67\2")
        buf.write("\2\u024d\u024f\5J&\2\u024e\u024c\3\2\2\2\u024e\u024d\3")
        buf.write("\2\2\2\u024f\u0250\3\2\2\2\u0250\u0252\7/\2\2\u0251\u0253")
        buf.write("\5\u008eH\2\u0252\u0251\3\2\2\2\u0252\u0253\3\2\2\2\u0253")
        buf.write("\u0254\3\2\2\2\u0254\u0256\7\60\2\2\u0255\u0257\7\66\2")
        buf.write("\2\u0256\u0255\3\2\2\2\u0256\u0257\3\2\2\2\u0257[\3\2")
        buf.write("\2\2\u0258\u025a\7;\2\2\u0259\u0258\3\2\2\2\u0259\u025a")
        buf.write("\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u025d\7\61\2\2\u025c")
        buf.write("\u025e\7;\2\2\u025d\u025c\3\2\2\2\u025d\u025e\3\2\2\2")
        buf.write("\u025e\u0263\3\2\2\2\u025f\u0262\5\f\7\2\u0260\u0262\7")
        buf.write(";\2\2\u0261\u025f\3\2\2\2\u0261\u0260\3\2\2\2\u0262\u0265")
        buf.write("\3\2\2\2\u0263\u0261\3\2\2\2\u0263\u0264\3\2\2\2\u0264")
        buf.write("\u0267\3\2\2\2\u0265\u0263\3\2\2\2\u0266\u0268\7;\2\2")
        buf.write("\u0267\u0266\3\2\2\2\u0267\u0268\3\2\2\2\u0268\u0269\3")
        buf.write("\2\2\2\u0269\u026a\7\62\2\2\u026a]\3\2\2\2\u026b\u0271")
        buf.write("\5`\61\2\u026c\u026d\5`\61\2\u026d\u026e\7\65\2\2\u026e")
        buf.write("\u026f\5^\60\2\u026f\u0271\3\2\2\2\u0270\u026b\3\2\2\2")
        buf.write("\u0270\u026c\3\2\2\2\u0271_\3\2\2\2\u0272\u0273\b\61\1")
        buf.write("\2\u0273\u0274\5b\62\2\u0274\u027a\3\2\2\2\u0275\u0276")
        buf.write("\f\4\2\2\u0276\u0277\7#\2\2\u0277\u0279\5b\62\2\u0278")
        buf.write("\u0275\3\2\2\2\u0279\u027c\3\2\2\2\u027a\u0278\3\2\2\2")
        buf.write("\u027a\u027b\3\2\2\2\u027ba\3\2\2\2\u027c\u027a\3\2\2")
        buf.write("\2\u027d\u027e\b\62\1\2\u027e\u027f\5d\63\2\u027f\u0285")
        buf.write("\3\2\2\2\u0280\u0281\f\4\2\2\u0281\u0282\7\"\2\2\u0282")
        buf.write("\u0284\5d\63\2\u0283\u0280\3\2\2\2\u0284\u0287\3\2\2\2")
        buf.write("\u0285\u0283\3\2\2\2\u0285\u0286\3\2\2\2\u0286c\3\2\2")
        buf.write("\2\u0287\u0285\3\2\2\2\u0288\u0289\b\63\1\2\u0289\u028a")
        buf.write("\5f\64\2\u028a\u0290\3\2\2\2\u028b\u028c\f\4\2\2\u028c")
        buf.write("\u028d\t\6\2\2\u028d\u028f\5f\64\2\u028e\u028b\3\2\2\2")
        buf.write("\u028f\u0292\3\2\2\2\u0290\u028e\3\2\2\2\u0290\u0291\3")
        buf.write("\2\2\2\u0291e\3\2\2\2\u0292\u0290\3\2\2\2\u0293\u0294")
        buf.write("\b\64\1\2\u0294\u0295\5h\65\2\u0295\u029b\3\2\2\2\u0296")
        buf.write("\u0297\f\4\2\2\u0297\u0298\t\7\2\2\u0298\u029a\5h\65\2")
        buf.write("\u0299\u0296\3\2\2\2\u029a\u029d\3\2\2\2\u029b\u0299\3")
        buf.write("\2\2\2\u029b\u029c\3\2\2\2\u029cg\3\2\2\2\u029d\u029b")
        buf.write("\3\2\2\2\u029e\u029f\b\65\1\2\u029f\u02a0\5j\66\2\u02a0")
        buf.write("\u02a6\3\2\2\2\u02a1\u02a2\f\4\2\2\u02a2\u02a3\t\b\2\2")
        buf.write("\u02a3\u02a5\5j\66\2\u02a4\u02a1\3\2\2\2\u02a5\u02a8\3")
        buf.write("\2\2\2\u02a6\u02a4\3\2\2\2\u02a6\u02a7\3\2\2\2\u02a7i")
        buf.write("\3\2\2\2\u02a8\u02a6\3\2\2\2\u02a9\u02aa\b\66\1\2\u02aa")
        buf.write("\u02ab\5l\67\2\u02ab\u02b1\3\2\2\2\u02ac\u02ad\f\4\2\2")
        buf.write("\u02ad\u02ae\t\t\2\2\u02ae\u02b0\5l\67\2\u02af\u02ac\3")
        buf.write("\2\2\2\u02b0\u02b3\3\2\2\2\u02b1\u02af\3\2\2\2\u02b1\u02b2")
        buf.write("\3\2\2\2\u02b2k\3\2\2\2\u02b3\u02b1\3\2\2\2\u02b4\u02b5")
        buf.write("\7$\2\2\u02b5\u02ba\5l\67\2\u02b6\u02b7\7\30\2\2\u02b7")
        buf.write("\u02ba\5l\67\2\u02b8\u02ba\5n8\2\u02b9\u02b4\3\2\2\2\u02b9")
        buf.write("\u02b6\3\2\2\2\u02b9\u02b8\3\2\2\2\u02bam\3\2\2\2\u02bb")
        buf.write("\u02c1\5p9\2\u02bc\u02c0\5r:\2\u02bd\u02c0\5t;\2\u02be")
        buf.write("\u02c0\5v<\2\u02bf\u02bc\3\2\2\2\u02bf\u02bd\3\2\2\2\u02bf")
        buf.write("\u02be\3\2\2\2\u02c0\u02c3\3\2\2\2\u02c1\u02bf\3\2\2\2")
        buf.write("\u02c1\u02c2\3\2\2\2\u02c2o\3\2\2\2\u02c3\u02c1\3\2\2")
        buf.write("\2\u02c4\u02cb\5x=\2\u02c5\u02cb\7\67\2\2\u02c6\u02c7")
        buf.write("\7/\2\2\u02c7\u02c8\5`\61\2\u02c8\u02c9\7\60\2\2\u02c9")
        buf.write("\u02cb\3\2\2\2\u02ca\u02c4\3\2\2\2\u02ca\u02c5\3\2\2\2")
        buf.write("\u02ca\u02c6\3\2\2\2\u02cbq\3\2\2\2\u02cc\u02cd\7\63\2")
        buf.write("\2\u02cd\u02ce\5`\61\2\u02ce\u02cf\7\64\2\2\u02cfs\3\2")
        buf.write("\2\2\u02d0\u02d1\7+\2\2\u02d1\u02d2\7\67\2\2\u02d2u\3")
        buf.write("\2\2\2\u02d3\u02d5\7/\2\2\u02d4\u02d6\5\u008eH\2\u02d5")
        buf.write("\u02d4\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6\u02d7\3\2\2\2")
        buf.write("\u02d7\u02d8\7\60\2\2\u02d8w\3\2\2\2\u02d9\u02e3\78\2")
        buf.write("\2\u02da\u02e3\79\2\2\u02db\u02e3\7:\2\2\u02dc\u02e3\7")
        buf.write("\25\2\2\u02dd\u02e3\7\26\2\2\u02de\u02e3\7\24\2\2\u02df")
        buf.write("\u02e3\5z>\2\u02e0\u02e3\5|?\2\u02e1\u02e3\5\u0088E\2")
        buf.write("\u02e2\u02d9\3\2\2\2\u02e2\u02da\3\2\2\2\u02e2\u02db\3")
        buf.write("\2\2\2\u02e2\u02dc\3\2\2\2\u02e2\u02dd\3\2\2\2\u02e2\u02de")
        buf.write("\3\2\2\2\u02e2\u02df\3\2\2\2\u02e2\u02e0\3\2\2\2\u02e2")
        buf.write("\u02e1\3\2\2\2\u02e3y\3\2\2\2\u02e4\u02e5\5\u0084C\2\u02e5")
        buf.write("\u02e6\7\61\2\2\u02e6\u02e7\5\u0080A\2\u02e7\u02e8\7\62")
        buf.write("\2\2\u02e8{\3\2\2\2\u02e9\u02ea\7\61\2\2\u02ea\u02eb\5")
        buf.write("\u0080A\2\u02eb\u02ec\7\62\2\2\u02ec}\3\2\2\2\u02ed\u02ee")
        buf.write("\5\u0084C\2\u02ee\u02ef\7\61\2\2\u02ef\u02f0\5\u0080A")
        buf.write("\2\u02f0\u02f1\7\62\2\2\u02f1\u02f7\3\2\2\2\u02f2\u02f3")
        buf.write("\7\61\2\2\u02f3\u02f4\5\u0080A\2\u02f4\u02f5\7\62\2\2")
        buf.write("\u02f5\u02f7\3\2\2\2\u02f6\u02ed\3\2\2\2\u02f6\u02f2\3")
        buf.write("\2\2\2\u02f7\177\3\2\2\2\u02f8\u02fd\5\u0082B\2\u02f9")
        buf.write("\u02fa\7\65\2\2\u02fa\u02fc\5\u0082B\2\u02fb\u02f9\3\2")
        buf.write("\2\2\u02fc\u02ff\3\2\2\2\u02fd\u02fb\3\2\2\2\u02fd\u02fe")
        buf.write("\3\2\2\2\u02fe\u0081\3\2\2\2\u02ff\u02fd\3\2\2\2\u0300")
        buf.write("\u030a\5|?\2\u0301\u030a\5\u0088E\2\u0302\u030a\78\2\2")
        buf.write("\u0303\u030a\79\2\2\u0304\u030a\7:\2\2\u0305\u030a\7\25")
        buf.write("\2\2\u0306\u030a\7\26\2\2\u0307\u030a\7\24\2\2\u0308\u030a")
        buf.write("\7\67\2\2\u0309\u0300\3\2\2\2\u0309\u0301\3\2\2\2\u0309")
        buf.write("\u0302\3\2\2\2\u0309\u0303\3\2\2\2\u0309\u0304\3\2\2\2")
        buf.write("\u0309\u0305\3\2\2\2\u0309\u0306\3\2\2\2\u0309\u0307\3")
        buf.write("\2\2\2\u0309\u0308\3\2\2\2\u030a\u0083\3\2\2\2\u030b\u030c")
        buf.write("\7\63\2\2\u030c\u030d\78\2\2\u030d\u0313\7\64\2\2\u030e")
        buf.write("\u030f\7\63\2\2\u030f\u0310\78\2\2\u0310\u0312\7\64\2")
        buf.write("\2\u0311\u030e\3\2\2\2\u0312\u0315\3\2\2\2\u0313\u0311")
        buf.write("\3\2\2\2\u0313\u0314\3\2\2\2\u0314\u0316\3\2\2\2\u0315")
        buf.write("\u0313\3\2\2\2\u0316\u0317\5\u0086D\2\u0317\u0085\3\2")
        buf.write("\2\2\u0318\u031f\7\f\2\2\u0319\u031f\7\r\2\2\u031a\u031f")
        buf.write("\7\13\2\2\u031b\u031f\7\16\2\2\u031c\u031f\7\67\2\2\u031d")
        buf.write("\u031f\5\u0084C\2\u031e\u0318\3\2\2\2\u031e\u0319\3\2")
        buf.write("\2\2\u031e\u031a\3\2\2\2\u031e\u031b\3\2\2\2\u031e\u031c")
        buf.write("\3\2\2\2\u031e\u031d\3\2\2\2\u031f\u0087\3\2\2\2\u0320")
        buf.write("\u0321\7\67\2\2\u0321\u0323\7\61\2\2\u0322\u0324\5\u008a")
        buf.write("F\2\u0323\u0322\3\2\2\2\u0323\u0324\3\2\2\2\u0324\u0325")
        buf.write("\3\2\2\2\u0325\u0326\7\62\2\2\u0326\u0089\3\2\2\2\u0327")
        buf.write("\u032d\5\u008cG\2\u0328\u0329\5\u008cG\2\u0329\u032a\7")
        buf.write("\65\2\2\u032a\u032b\5\u008aF\2\u032b\u032d\3\2\2\2\u032c")
        buf.write("\u0327\3\2\2\2\u032c\u0328\3\2\2\2\u032d\u008b\3\2\2\2")
        buf.write("\u032e\u032f\7\67\2\2\u032f\u0330\7,\2\2\u0330\u0331\5")
        buf.write("`\61\2\u0331\u008d\3\2\2\2\u0332\u0338\5`\61\2\u0333\u0334")
        buf.write("\5`\61\2\u0334\u0335\7\65\2\2\u0335\u0336\5\u008eH\2\u0336")
        buf.write("\u0338\3\2\2\2\u0337\u0332\3\2\2\2\u0337\u0333\3\2\2\2")
        buf.write("\u0338\u008f\3\2\2\2a\u0099\u00a0\u00a8\u00ad\u00b5\u00bf")
        buf.write("\u00ca\u00d0\u00d7\u00dd\u00e7\u00ec\u00f7\u00fe\u0102")
        buf.write("\u0107\u0109\u010d\u0115\u011e\u0124\u0127\u012b\u0137")
        buf.write("\u013b\u013e\u0148\u0154\u015d\u0160\u016a\u016d\u0178")
        buf.write("\u017f\u0189\u018e\u0196\u019c\u01a0\u01a3\u01a9\u01b2")
        buf.write("\u01b9\u01c2\u01c8\u01cd\u01d1\u01d7\u01db\u01de\u01e2")
        buf.write("\u01e6\u01ea\u01ee\u01f4\u01fb\u01fd\u0205\u0209\u020f")
        buf.write("\u0224\u0231\u0235\u0243\u0247\u024a\u024e\u0252\u0256")
        buf.write("\u0259\u025d\u0261\u0263\u0267\u0270\u027a\u0285\u0290")
        buf.write("\u029b\u02a6\u02b1\u02b9\u02bf\u02c1\u02ca\u02d5\u02e2")
        buf.write("\u02f6\u02fd\u0309\u0313\u031e\u0323\u032c\u0337")
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
    RULE_function_block_statement = 12
    RULE_function_declared = 13
    RULE_receiver = 14
    RULE_method_declared = 15
    RULE_method_params = 16
    RULE_method_param = 17
    RULE_params_list = 18
    RULE_param = 19
    RULE_struct_declared = 20
    RULE_struct_type_list = 21
    RULE_struct_field = 22
    RULE_more_ids = 23
    RULE_struct_end = 24
    RULE_struct_type = 25
    RULE_interface_declared = 26
    RULE_interface_type_list = 27
    RULE_interface_type = 28
    RULE_interface_method = 29
    RULE_optional_params = 30
    RULE_optional_type = 31
    RULE_optional_semi = 32
    RULE_declared_statement = 33
    RULE_assign_statement = 34
    RULE_assign_op = 35
    RULE_assign_lhs = 36
    RULE_if_statement = 37
    RULE_for_statement = 38
    RULE_for_init = 39
    RULE_for_update = 40
    RULE_break_statement = 41
    RULE_continue_statement = 42
    RULE_return_statement = 43
    RULE_call_statement = 44
    RULE_block_stmt = 45
    RULE_expr_list = 46
    RULE_expression = 47
    RULE_expression1 = 48
    RULE_expression2 = 49
    RULE_expression3 = 50
    RULE_expression4 = 51
    RULE_expression5 = 52
    RULE_expression6 = 53
    RULE_expression7 = 54
    RULE_operand = 55
    RULE_element_access = 56
    RULE_field_access = 57
    RULE_call_expr = 58
    RULE_literal = 59
    RULE_typed_array_literal = 60
    RULE_untyped_array_literal = 61
    RULE_array_literal = 62
    RULE_literal_list = 63
    RULE_literal_item = 64
    RULE_array_type = 65
    RULE_type_name = 66
    RULE_struct_literal = 67
    RULE_field_list = 68
    RULE_field_init = 69
    RULE_list_expression = 70

    ruleNames =  [ "program", "newlines", "more_declared", "declared", "list_statement", 
                   "statement", "variables_declared", "var_decl_list", "var_decl", 
                   "constants_declared", "const_decl_list", "const_decl", 
                   "function_block_statement", "function_declared", "receiver", 
                   "method_declared", "method_params", "method_param", "params_list", 
                   "param", "struct_declared", "struct_type_list", "struct_field", 
                   "more_ids", "struct_end", "struct_type", "interface_declared", 
                   "interface_type_list", "interface_type", "interface_method", 
                   "optional_params", "optional_type", "optional_semi", 
                   "declared_statement", "assign_statement", "assign_op", 
                   "assign_lhs", "if_statement", "for_statement", "for_init", 
                   "for_update", "break_statement", "continue_statement", 
                   "return_statement", "call_statement", "block_stmt", "expr_list", 
                   "expression", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7", 
                   "operand", "element_access", "field_access", "call_expr", 
                   "literal", "typed_array_literal", "untyped_array_literal", 
                   "array_literal", "literal_list", "literal_item", "array_type", 
                   "type_name", "struct_literal", "field_list", "field_init", 
                   "list_expression" ]

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
            self.state = 142
            self.newlines()
            self.state = 143
            self.declared()
            self.state = 144
            self.more_declared()
            self.state = 145
            self.newlines()
            self.state = 146
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
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.EOF, MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(MiniGoParser.NEWLINE)
                self.state = 150
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
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.newlines()
                self.state = 155
                self.declared()
                self.state = 156
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
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 160
                self.variables_declared()
                pass

            elif la_ == 2:
                self.state = 161
                self.constants_declared()
                pass

            elif la_ == 3:
                self.state = 162
                self.function_declared()
                pass

            elif la_ == 4:
                self.state = 163
                self.method_declared()
                pass

            elif la_ == 5:
                self.state = 164
                self.struct_declared()
                pass

            elif la_ == 6:
                self.state = 165
                self.interface_declared()
                pass


            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 168
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 173
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
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.statement()
                self.state = 176
                self.newlines()
                self.state = 177
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
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.declared_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 184
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 185
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 186
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 187
                self.call_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 188
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

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(MiniGoParser.VAR)
            self.state = 192
            self.var_decl_list()
            self.state = 193
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
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.var_decl()
                self.state = 197
                self.match(MiniGoParser.COMMA)
                self.state = 198
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
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(MiniGoParser.ID)
                self.state = 203
                self.type_name()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 204
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 205
                    self.expression(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(MiniGoParser.ID)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 209
                    self.match(MiniGoParser.COMMA)
                    self.state = 210
                    self.match(MiniGoParser.ID)
                    self.state = 215
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 216
                self.type_name()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 217
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 218
                    self.expr_list()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.match(MiniGoParser.ID)

                self.state = 222
                self.match(MiniGoParser.ASSIGN)
                self.state = 223
                self.expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 224
                self.match(MiniGoParser.ID)
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 225
                    self.match(MiniGoParser.COMMA)
                    self.state = 226
                    self.match(MiniGoParser.ID)
                    self.state = 231
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 232
                self.match(MiniGoParser.ASSIGN)
                self.state = 233
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
            self.state = 236
            self.match(MiniGoParser.CONST)
            self.state = 237
            self.const_decl_list()
            self.state = 238
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
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.const_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.const_decl()
                self.state = 242
                self.match(MiniGoParser.COMMA)
                self.state = 243
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
            self.state = 247
            self.match(MiniGoParser.ID)
            self.state = 248
            self.match(MiniGoParser.ASSIGN)
            self.state = 249
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_function_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_block_statement" ):
                return visitor.visitFunction_block_statement(self)
            else:
                return visitor.visitChildren(self)




    def function_block_statement(self):

        localctx = MiniGoParser.Function_block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_function_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 251
                self.match(MiniGoParser.NEWLINE)


            self.state = 254
            self.match(MiniGoParser.LB)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 255
                self.match(MiniGoParser.NEWLINE)


            self.state = 258
            self.statement()
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 261
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                        self.state = 259
                        self.statement()
                        pass
                    elif token in [MiniGoParser.NEWLINE]:
                        self.state = 260
                        self.match(MiniGoParser.NEWLINE)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 266
                self.match(MiniGoParser.NEWLINE)


            self.state = 269
            self.match(MiniGoParser.RB)
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

        def function_block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Function_block_statementContext,0)


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
        self.enterRule(localctx, 26, self.RULE_function_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(MiniGoParser.FUNC)
            self.state = 272
            self.match(MiniGoParser.ID)
            self.state = 273
            self.match(MiniGoParser.LP)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 274
                self.params_list()


            self.state = 277
            self.match(MiniGoParser.RP)
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LP]:
                self.state = 278
                self.match(MiniGoParser.LP)
                self.state = 279
                self.type_name()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 280
                    self.match(MiniGoParser.COMMA)
                    self.state = 281
                    self.type_name()
                    self.state = 286
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 287
                self.match(MiniGoParser.RP)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.state = 289
                self.type_name()
                pass
            elif token in [MiniGoParser.LB, MiniGoParser.NEWLINE]:
                pass
            else:
                pass
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 292
                self.match(MiniGoParser.NEWLINE)


            self.state = 295
            self.function_block_statement()
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 296
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
        self.enterRule(localctx, 28, self.RULE_receiver)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(MiniGoParser.ID)
            self.state = 300
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


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Params_listContext,0)


        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declared" ):
                return visitor.visitMethod_declared(self)
            else:
                return visitor.visitChildren(self)




    def method_declared(self):

        localctx = MiniGoParser.Method_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_method_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(MiniGoParser.FUNC)
            self.state = 303
            self.match(MiniGoParser.LP)
            self.state = 304
            self.receiver()
            self.state = 305
            self.match(MiniGoParser.RP)
            self.state = 306
            self.match(MiniGoParser.ID)
            self.state = 307
            self.match(MiniGoParser.LP)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 308
                self.params_list()


            self.state = 311
            self.match(MiniGoParser.RP)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 312
                self.type_name()


            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 315
                self.match(MiniGoParser.NEWLINE)


            self.state = 318
            self.block_stmt()
            self.state = 319
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
        self.enterRule(localctx, 32, self.RULE_method_params)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.method_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.method_param()
                self.state = 323
                self.match(MiniGoParser.COMMA)
                self.state = 324
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
        self.enterRule(localctx, 34, self.RULE_method_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(MiniGoParser.ID)
            self.state = 329
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParamContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParamContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_params_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list" ):
                return visitor.visitParams_list(self)
            else:
                return visitor.visitChildren(self)




    def params_list(self):

        localctx = MiniGoParser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.match(MiniGoParser.ID)
                self.state = 332
                self.type_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.match(MiniGoParser.ID)
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 334
                    self.match(MiniGoParser.COMMA)
                    self.state = 335
                    self.match(MiniGoParser.ID)
                    self.state = 340
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 341
                self.type_name()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 342
                self.param()
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 343
                    self.match(MiniGoParser.COMMA)
                    self.state = 344
                    self.param()
                    self.state = 349
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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
        self.enterRule(localctx, 38, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 352
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 353
                self.match(MiniGoParser.ID)
                self.state = 354
                self.match(MiniGoParser.COMMA)
                self.state = 355
                self.match(MiniGoParser.ID)
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 356
                    self.match(MiniGoParser.COMMA)
                    self.state = 357
                    self.match(MiniGoParser.ID)
                    self.state = 362
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


            self.state = 365
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
        self.enterRule(localctx, 40, self.RULE_struct_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(MiniGoParser.TYPE)
            self.state = 368
            self.match(MiniGoParser.ID)
            self.state = 369
            self.match(MiniGoParser.STRUCT)
            self.state = 370
            self.match(MiniGoParser.LB)
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 371
                self.match(MiniGoParser.NEWLINE)
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 377
            self.struct_type_list()
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 378
                self.match(MiniGoParser.NEWLINE)
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 384
            self.match(MiniGoParser.RB)
            self.state = 385
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
        self.enterRule(localctx, 42, self.RULE_struct_type_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 387
                self.struct_field()
                self.state = 391
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 388
                        self.match(MiniGoParser.NEWLINE) 
                    self.state = 393
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

                self.state = 396 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.FUNC or _la==MiniGoParser.ID):
                    break

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
        self.enterRule(localctx, 44, self.RULE_struct_field)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(MiniGoParser.ID)
                self.state = 399
                self.more_ids()
                self.state = 400
                self.type_name()
                self.state = 401
                self.struct_end()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
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
        self.enterRule(localctx, 46, self.RULE_more_ids)
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.match(MiniGoParser.COMMA)
                self.state = 408
                self.match(MiniGoParser.ID)
                self.state = 409
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
        self.enterRule(localctx, 48, self.RULE_struct_end)
        self._la = 0 # Token type
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SEMI:
                    self.state = 413
                    self.match(MiniGoParser.SEMI)


                self.state = 416
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
        self.enterRule(localctx, 50, self.RULE_struct_type)
        try:
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.struct_field()
                self.state = 421
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

        def interface_type_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_type_listContext,0)


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
            return MiniGoParser.RULE_interface_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declared" ):
                return visitor.visitInterface_declared(self)
            else:
                return visitor.visitChildren(self)




    def interface_declared(self):

        localctx = MiniGoParser.Interface_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_interface_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(MiniGoParser.TYPE)
            self.state = 426
            self.match(MiniGoParser.ID)
            self.state = 427
            self.match(MiniGoParser.INTERFACE)
            self.state = 428
            self.match(MiniGoParser.LB)
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 429
                self.match(MiniGoParser.NEWLINE)
                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 435
            self.interface_type_list()
            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 436
                self.match(MiniGoParser.NEWLINE)
                self.state = 441
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 442
            self.match(MiniGoParser.RB)
            self.state = 443
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


    class Interface_type_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Interface_methodContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type_list" ):
                return visitor.visitInterface_type_list(self)
            else:
                return visitor.visitChildren(self)




    def interface_type_list(self):

        localctx = MiniGoParser.Interface_type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_interface_type_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 445
                self.interface_method()
                self.state = 448 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

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
        self.enterRule(localctx, 56, self.RULE_interface_type)
        try:
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.interface_method()
                self.state = 452
                self.interface_type()
                pass


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

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Params_listContext,0)


        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method" ):
                return visitor.visitInterface_method(self)
            else:
                return visitor.visitChildren(self)




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.match(MiniGoParser.ID)
                self.state = 457
                self.match(MiniGoParser.LP)
                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 458
                    self.params_list()


                self.state = 461
                self.match(MiniGoParser.RP)
                self.state = 463
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 462
                    self.type_name()


                self.state = 465
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NEWLINE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.match(MiniGoParser.ID)
                self.state = 467
                self.match(MiniGoParser.LP)
                self.state = 469
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 468
                    self.params_list()


                self.state = 471
                self.match(MiniGoParser.RP)
                self.state = 473
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 472
                    self.type_name()


                self.state = 475
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NEWLINE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


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
        self.enterRule(localctx, 60, self.RULE_optional_params)
        try:
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
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
        self.enterRule(localctx, 62, self.RULE_optional_type)
        try:
            self.state = 484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.type_name()
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
        self.enterRule(localctx, 64, self.RULE_optional_semi)
        try:
            self.state = 488
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
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
        self.enterRule(localctx, 66, self.RULE_declared_statement)
        try:
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.variables_declared()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
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
        self.enterRule(localctx, 68, self.RULE_assign_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.assign_lhs()
            self.state = 495
            self.assign_op()
            self.state = 496
            self.expression(0)
            self.state = 498
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 497
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
        self.enterRule(localctx, 70, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
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
        self.enterRule(localctx, 72, self.RULE_assign_lhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(MiniGoParser.ID)
            self.state = 507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.DOT or _la==MiniGoParser.LSB:
                self.state = 505
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.DOT]:
                    self.state = 503
                    self.field_access()
                    pass
                elif token in [MiniGoParser.LSB]:
                    self.state = 504
                    self.element_access()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 509
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
        self.enterRule(localctx, 74, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(MiniGoParser.IF)
            self.state = 511
            self.match(MiniGoParser.LP)
            self.state = 512
            self.expression(0)
            self.state = 513
            self.match(MiniGoParser.RP)
            self.state = 515
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 514
                self.match(MiniGoParser.NEWLINE)


            self.state = 517
            self.block_stmt()
            self.state = 519
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.state = 518
                self.match(MiniGoParser.NEWLINE)


            self.state = 525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 521
                self.match(MiniGoParser.ELSE)
                self.state = 522
                self.if_statement()

            elif la_ == 2:
                self.state = 523
                self.match(MiniGoParser.ELSE)
                self.state = 524
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
        self.enterRule(localctx, 76, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(MiniGoParser.FOR)
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 528
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 529
                self.match(MiniGoParser.COMMA)
                self.state = 530
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 531
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 532
                self.match(MiniGoParser.RANGE)
                self.state = 533
                self.expression(0)
                self.state = 534
                self.block_stmt()
                pass

            elif la_ == 2:
                self.state = 536
                self.for_init()
                self.state = 537
                self.match(MiniGoParser.SEMI)
                self.state = 538
                self.expression(0)
                self.state = 539
                self.match(MiniGoParser.SEMI)
                self.state = 540
                self.for_update()
                self.state = 541
                self.block_stmt()
                pass

            elif la_ == 3:
                self.state = 543
                self.expression(0)
                self.state = 544
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
        self.enterRule(localctx, 78, self.RULE_for_init)
        self._la = 0 # Token type
        try:
            self.state = 563
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.assign_lhs()
                self.state = 549
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 550
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.assign_lhs()
                self.state = 553
                self.assign_op()
                self.state = 554
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 556
                self.match(MiniGoParser.VAR)
                self.state = 557
                self.match(MiniGoParser.ID)
                self.state = 559
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 558
                    self.type_name()


                self.state = 561
                self.match(MiniGoParser.ASSIGN)
                self.state = 562
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
        self.enterRule(localctx, 80, self.RULE_for_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.assign_lhs()
            self.state = 566
            self.assign_op()
            self.state = 567
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
        self.enterRule(localctx, 82, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(MiniGoParser.BREAK)
            self.state = 570
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
        self.enterRule(localctx, 84, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.match(MiniGoParser.CONTINUE)
            self.state = 573
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
        self.enterRule(localctx, 86, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.match(MiniGoParser.RETURN)
            self.state = 584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 577
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 576
                    self.expression(0)


                self.state = 579
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.state = 581
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 580
                    self.expression(0)


                self.state = 583
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
        self.enterRule(localctx, 88, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.state = 586
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 587
                self.assign_lhs()
                pass


            self.state = 590
            self.match(MiniGoParser.LP)
            self.state = 592
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 591
                self.list_expression()


            self.state = 594
            self.match(MiniGoParser.RP)
            self.state = 596
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 595
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
        self.enterRule(localctx, 90, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 598
                self.match(MiniGoParser.NEWLINE)


            self.state = 601
            self.match(MiniGoParser.LB)
            self.state = 603
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.state = 602
                self.match(MiniGoParser.NEWLINE)


            self.state = 609
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,72,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 607
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                        self.state = 605
                        self.statement()
                        pass
                    elif token in [MiniGoParser.NEWLINE]:
                        self.state = 606
                        self.match(MiniGoParser.NEWLINE)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 611
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

            self.state = 613
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 612
                self.match(MiniGoParser.NEWLINE)


            self.state = 615
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
        self.enterRule(localctx, 92, self.RULE_expr_list)
        try:
            self.state = 622
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 617
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 618
                self.expression(0)
                self.state = 619
                self.match(MiniGoParser.COMMA)
                self.state = 620
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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 632
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 627
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 628
                    self.match(MiniGoParser.OR)
                    self.state = 629
                    self.expression1(0) 
                self.state = 634
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,75,self._ctx)

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
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 636
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 643
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,76,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 638
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 639
                    self.match(MiniGoParser.AND)
                    self.state = 640
                    self.expression2(0) 
                self.state = 645
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,76,self._ctx)

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
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 654
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,77,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 649
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 650
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.EQUAL or _la==MiniGoParser.NOT_EQUAL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 651
                    self.expression3(0) 
                self.state = 656
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,77,self._ctx)

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
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 665
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,78,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 660
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 661
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESS_OR_EQUAL) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 662
                    self.expression4(0) 
                self.state = 667
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,78,self._ctx)

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
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 669
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 676
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 671
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 672
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 673
                    self.expression5(0) 
                self.state = 678
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

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
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_expression5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 680
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 687
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 682
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 683
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 684
                    self.expression6() 
                self.state = 689
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

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
        self.enterRule(localctx, 106, self.RULE_expression6)
        try:
            self.state = 695
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 690
                self.match(MiniGoParser.NOT)
                self.state = 691
                self.expression6()
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 692
                self.match(MiniGoParser.SUB)
                self.state = 693
                self.expression6()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LP, MiniGoParser.LB, MiniGoParser.LSB, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 694
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
        self.enterRule(localctx, 108, self.RULE_expression7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 697
            self.operand()
            self.state = 703
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,83,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 701
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSB]:
                        self.state = 698
                        self.element_access()
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 699
                        self.field_access()
                        pass
                    elif token in [MiniGoParser.LP]:
                        self.state = 700
                        self.call_expr()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 705
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,83,self._ctx)

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
        self.enterRule(localctx, 110, self.RULE_operand)
        try:
            self.state = 712
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 706
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 707
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 708
                self.match(MiniGoParser.LP)
                self.state = 709
                self.expression(0)
                self.state = 710
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
        self.enterRule(localctx, 112, self.RULE_element_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
            self.match(MiniGoParser.LSB)
            self.state = 715
            self.expression(0)
            self.state = 716
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
        self.enterRule(localctx, 114, self.RULE_field_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 718
            self.match(MiniGoParser.DOT)
            self.state = 719
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
        self.enterRule(localctx, 116, self.RULE_call_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 721
            self.match(MiniGoParser.LP)
            self.state = 723
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 722
                self.list_expression()


            self.state = 725
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

        def typed_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Typed_array_literalContext,0)


        def untyped_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Untyped_array_literalContext,0)


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
        self.enterRule(localctx, 118, self.RULE_literal)
        try:
            self.state = 736
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 727
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 728
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 729
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 730
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 731
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 732
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 733
                self.typed_array_literal()
                pass
            elif token in [MiniGoParser.LB]:
                self.enterOuterAlt(localctx, 8)
                self.state = 734
                self.untyped_array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 9)
                self.state = 735
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


    class Typed_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def literal_list(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_typed_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyped_array_literal" ):
                return visitor.visitTyped_array_literal(self)
            else:
                return visitor.visitChildren(self)




    def typed_array_literal(self):

        localctx = MiniGoParser.Typed_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_typed_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 738
            self.array_type()
            self.state = 739
            self.match(MiniGoParser.LB)
            self.state = 740
            self.literal_list()
            self.state = 741
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Untyped_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def literal_list(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_untyped_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUntyped_array_literal" ):
                return visitor.visitUntyped_array_literal(self)
            else:
                return visitor.visitChildren(self)




    def untyped_array_literal(self):

        localctx = MiniGoParser.Untyped_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_untyped_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 743
            self.match(MiniGoParser.LB)
            self.state = 744
            self.literal_list()
            self.state = 745
            self.match(MiniGoParser.RB)
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

        def literal_list(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_listContext,0)


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
        self.enterRule(localctx, 124, self.RULE_array_literal)
        try:
            self.state = 756
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 747
                self.array_type()
                self.state = 748
                self.match(MiniGoParser.LB)
                self.state = 749
                self.literal_list()
                self.state = 750
                self.match(MiniGoParser.RB)
                pass
            elif token in [MiniGoParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 752
                self.match(MiniGoParser.LB)
                self.state = 753
                self.literal_list()
                self.state = 754
                self.match(MiniGoParser.RB)
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


    class Literal_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Literal_itemContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Literal_itemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_list" ):
                return visitor.visitLiteral_list(self)
            else:
                return visitor.visitChildren(self)




    def literal_list(self):

        localctx = MiniGoParser.Literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_literal_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 758
            self.literal_item()
            self.state = 763
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 759
                self.match(MiniGoParser.COMMA)
                self.state = 760
                self.literal_item()
                self.state = 765
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def untyped_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Untyped_array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_item" ):
                return visitor.visitLiteral_item(self)
            else:
                return visitor.visitChildren(self)




    def literal_item(self):

        localctx = MiniGoParser.Literal_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_literal_item)
        try:
            self.state = 775
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 766
                self.untyped_array_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 767
                self.struct_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 768
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 769
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 770
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 771
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 772
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 773
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 774
                self.match(MiniGoParser.ID)
                pass


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
        self.enterRule(localctx, 130, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 777
            self.match(MiniGoParser.LSB)
            self.state = 778
            self.match(MiniGoParser.INT_LIT)
            self.state = 779
            self.match(MiniGoParser.RSB)
            self.state = 785
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,90,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 780
                    self.match(MiniGoParser.LSB)
                    self.state = 781
                    self.match(MiniGoParser.INT_LIT)
                    self.state = 782
                    self.match(MiniGoParser.RSB) 
                self.state = 787
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,90,self._ctx)

            self.state = 788
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
        self.enterRule(localctx, 132, self.RULE_type_name)
        try:
            self.state = 796
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 790
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 791
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 792
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 793
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 794
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 795
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
        self.enterRule(localctx, 134, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 798
            self.match(MiniGoParser.ID)
            self.state = 799
            self.match(MiniGoParser.LB)
            self.state = 801
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 800
                self.field_list()


            self.state = 803
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
        self.enterRule(localctx, 136, self.RULE_field_list)
        try:
            self.state = 810
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 805
                self.field_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 806
                self.field_init()
                self.state = 807
                self.match(MiniGoParser.COMMA)
                self.state = 808
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
        self.enterRule(localctx, 138, self.RULE_field_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 812
            self.match(MiniGoParser.ID)
            self.state = 813
            self.match(MiniGoParser.COLON)
            self.state = 814
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
        self.enterRule(localctx, 140, self.RULE_list_expression)
        try:
            self.state = 821
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 816
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 817
                self.expression(0)
                self.state = 818
                self.match(MiniGoParser.COMMA)
                self.state = 819
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
        self._predicates[47] = self.expression_sempred
        self._predicates[48] = self.expression1_sempred
        self._predicates[49] = self.expression2_sempred
        self._predicates[50] = self.expression3_sempred
        self._predicates[51] = self.expression4_sempred
        self._predicates[52] = self.expression5_sempred
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
         





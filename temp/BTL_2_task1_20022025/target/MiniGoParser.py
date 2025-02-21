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
        buf.write("\u02d0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\5\3\u00a0\n\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4\u00a7\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00af")
        buf.write("\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\u00b8\n\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00c2\n\7\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\5\t\u00cc\n\t\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u00d3\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00dd\n")
        buf.write("\t\3\n\3\n\3\n\3\n\5\n\u00e3\n\n\3\13\3\13\3\13\3\13\5")
        buf.write("\13\u00e9\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5\r")
        buf.write("\u00f4\n\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\5\17")
        buf.write("\u00fe\n\17\3\17\3\17\5\17\u0102\n\17\3\17\5\17\u0105")
        buf.write("\n\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u0110\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u0117\n\21\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u0123\n\23\3\23\3\23\5\23\u0127\n\23\3\23\5\23\u012a")
        buf.write("\n\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u013a\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u0142\n\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u0149\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u015e\n\31\3\32\3\32\3\32\5\32\u0163\n\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u016e")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\5\37\u0181\n\37\3")
        buf.write(" \3 \3 \5 \u0186\n \3 \3 \5 \u018a\n \3 \3 \3!\3!\5!\u0190")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\5%\u019f")
        buf.write("\n%\3%\3%\5%\u01a3\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01ae")
        buf.write("\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01c3\n\'\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\5(\u01cf\n(\3(\3(\5(\u01d3\n(\3)\3)\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3+\3,\3,\5,\u01e1\n,\3,\3,\5,\u01e5")
        buf.write("\n,\3,\5,\u01e8\n,\3-\3-\5-\u01ec\n-\3-\3-\5-\u01f0\n")
        buf.write("-\3-\3-\3-\3.\3.\5.\u01f7\n.\3.\3.\5.\u01fb\n.\3.\3.\5")
        buf.write(".\u01ff\n.\3/\3/\3/\3/\3/\3/\5/\u0207\n/\3\60\3\60\3\60")
        buf.write("\3\60\3\60\5\60\u020e\n\60\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\7\61\u0216\n\61\f\61\16\61\u0219\13\61\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\7\62\u0221\n\62\f\62\16\62\u0224\13")
        buf.write("\62\3\63\3\63\3\63\3\63\3\63\3\63\7\63\u022c\n\63\f\63")
        buf.write("\16\63\u022f\13\63\3\64\3\64\3\64\3\64\3\64\3\64\7\64")
        buf.write("\u0237\n\64\f\64\16\64\u023a\13\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\7\65\u0242\n\65\f\65\16\65\u0245\13\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\7\66\u024d\n\66\f\66\16\66\u0250")
        buf.write("\13\66\3\67\3\67\3\67\3\67\3\67\5\67\u0257\n\67\38\38")
        buf.write("\38\39\39\39\39\59\u0260\n9\39\39\59\u0264\n9\3:\3:\3")
        buf.write(":\3:\3:\3:\5:\u026c\n:\3;\3;\3;\3;\3<\3<\3<\3=\3=\5=\u0277")
        buf.write("\n=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\5>\u0283\n>\3?\3?\3")
        buf.write("?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3A\3A\5A\u0293\nA\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\5B\u029e\nB\3C\3C\3C\3C\3C\3C\3D\3")
        buf.write("D\3D\3D\3D\5D\u02ab\nD\3E\3E\3E\3E\3E\3E\5E\u02b3\nE\3")
        buf.write("F\3F\3F\3F\3F\3G\3G\5G\u02bc\nG\3H\3H\3H\3H\3H\5H\u02c3")
        buf.write("\nH\3I\3I\3I\3I\3J\3J\3J\3J\3J\5J\u02ce\nJ\3J\2\b`bdf")
        buf.write("hjK\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\2\13")
        buf.write("\4\2\66\66;;\4\2\t\n\67\67\4\2%*--\4\2..\67\67\3\2\34")
        buf.write("\35\3\2\36!\3\2\27\30\3\2\31\33\4\2\67\6799\2\u02ec\2")
        buf.write("\u0094\3\2\2\2\4\u009f\3\2\2\2\6\u00a6\3\2\2\2\b\u00ae")
        buf.write("\3\2\2\2\n\u00b7\3\2\2\2\f\u00c1\3\2\2\2\16\u00c3\3\2")
        buf.write("\2\2\20\u00dc\3\2\2\2\22\u00e2\3\2\2\2\24\u00e8\3\2\2")
        buf.write("\2\26\u00ea\3\2\2\2\30\u00f3\3\2\2\2\32\u00f5\3\2\2\2")
        buf.write("\34\u00f9\3\2\2\2\36\u010f\3\2\2\2 \u0116\3\2\2\2\"\u0118")
        buf.write("\3\2\2\2$\u011b\3\2\2\2&\u0139\3\2\2\2(\u0141\3\2\2\2")
        buf.write("*\u0148\3\2\2\2,\u014a\3\2\2\2.\u0154\3\2\2\2\60\u015d")
        buf.write("\3\2\2\2\62\u0162\3\2\2\2\64\u0164\3\2\2\2\66\u016d\3")
        buf.write("\2\2\28\u016f\3\2\2\2:\u0179\3\2\2\2<\u0180\3\2\2\2>\u0182")
        buf.write("\3\2\2\2@\u018f\3\2\2\2B\u0191\3\2\2\2D\u0196\3\2\2\2")
        buf.write("F\u0198\3\2\2\2H\u01a2\3\2\2\2J\u01a4\3\2\2\2L\u01af\3")
        buf.write("\2\2\2N\u01d2\3\2\2\2P\u01d4\3\2\2\2R\u01d8\3\2\2\2T\u01db")
        buf.write("\3\2\2\2V\u01de\3\2\2\2X\u01eb\3\2\2\2Z\u01f4\3\2\2\2")
        buf.write("\\\u0206\3\2\2\2^\u020d\3\2\2\2`\u020f\3\2\2\2b\u021a")
        buf.write("\3\2\2\2d\u0225\3\2\2\2f\u0230\3\2\2\2h\u023b\3\2\2\2")
        buf.write("j\u0246\3\2\2\2l\u0256\3\2\2\2n\u0258\3\2\2\2p\u0263\3")
        buf.write("\2\2\2r\u026b\3\2\2\2t\u026d\3\2\2\2v\u0271\3\2\2\2x\u0274")
        buf.write("\3\2\2\2z\u0282\3\2\2\2|\u0284\3\2\2\2~\u0289\3\2\2\2")
        buf.write("\u0080\u0292\3\2\2\2\u0082\u029d\3\2\2\2\u0084\u029f\3")
        buf.write("\2\2\2\u0086\u02aa\3\2\2\2\u0088\u02b2\3\2\2\2\u008a\u02b4")
        buf.write("\3\2\2\2\u008c\u02bb\3\2\2\2\u008e\u02c2\3\2\2\2\u0090")
        buf.write("\u02c4\3\2\2\2\u0092\u02cd\3\2\2\2\u0094\u0095\7\17\2")
        buf.write("\2\u0095\u0096\7\67\2\2\u0096\u0097\7%\2\2\u0097\u0098")
        buf.write("\5`\61\2\u0098\u0099\7\66\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u009b\7\2\2\3\u009b\3\3\2\2\2\u009c\u00a0\3\2\2\2\u009d")
        buf.write("\u009e\7;\2\2\u009e\u00a0\5\4\3\2\u009f\u009c\3\2\2\2")
        buf.write("\u009f\u009d\3\2\2\2\u00a0\5\3\2\2\2\u00a1\u00a7\3\2\2")
        buf.write("\2\u00a2\u00a3\5\4\3\2\u00a3\u00a4\5\b\5\2\u00a4\u00a5")
        buf.write("\5\6\4\2\u00a5\u00a7\3\2\2\2\u00a6\u00a1\3\2\2\2\u00a6")
        buf.write("\u00a2\3\2\2\2\u00a7\7\3\2\2\2\u00a8\u00af\5\16\b\2\u00a9")
        buf.write("\u00af\5\26\f\2\u00aa\u00af\5\34\17\2\u00ab\u00af\5$\23")
        buf.write("\2\u00ac\u00af\5,\27\2\u00ad\u00af\58\35\2\u00ae\u00a8")
        buf.write("\3\2\2\2\u00ae\u00a9\3\2\2\2\u00ae\u00aa\3\2\2\2\u00ae")
        buf.write("\u00ab\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2")
        buf.write("\u00af\u00b0\3\2\2\2\u00b0\u00b1\5\4\3\2\u00b1\t\3\2\2")
        buf.write("\2\u00b2\u00b8\5\f\7\2\u00b3\u00b4\5\f\7\2\u00b4\u00b5")
        buf.write("\5\4\3\2\u00b5\u00b6\5\n\6\2\u00b6\u00b8\3\2\2\2\u00b7")
        buf.write("\u00b2\3\2\2\2\u00b7\u00b3\3\2\2\2\u00b8\13\3\2\2\2\u00b9")
        buf.write("\u00c2\5@!\2\u00ba\u00c2\5B\"\2\u00bb\u00c2\5J&\2\u00bc")
        buf.write("\u00c2\5L\'\2\u00bd\u00c2\5R*\2\u00be\u00c2\5T+\2\u00bf")
        buf.write("\u00c2\5X-\2\u00c0\u00c2\5V,\2\u00c1\u00b9\3\2\2\2\u00c1")
        buf.write("\u00ba\3\2\2\2\u00c1\u00bb\3\2\2\2\u00c1\u00bc\3\2\2\2")
        buf.write("\u00c1\u00bd\3\2\2\2\u00c1\u00be\3\2\2\2\u00c1\u00bf\3")
        buf.write("\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\r\3\2\2\2\u00c3\u00c4")
        buf.write("\7\20\2\2\u00c4\u00c5\5\20\t\2\u00c5\u00c6\t\2\2\2\u00c6")
        buf.write("\17\3\2\2\2\u00c7\u00c8\7\67\2\2\u00c8\u00cb\5\u0088E")
        buf.write("\2\u00c9\u00ca\7%\2\2\u00ca\u00cc\5`\61\2\u00cb\u00c9")
        buf.write("\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00dd\3\2\2\2\u00cd")
        buf.write("\u00ce\7\67\2\2\u00ce\u00cf\5\22\n\2\u00cf\u00d2\5\u0088")
        buf.write("E\2\u00d0\u00d1\7%\2\2\u00d1\u00d3\5^\60\2\u00d2\u00d0")
        buf.write("\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00dd\3\2\2\2\u00d4")
        buf.write("\u00d5\7\67\2\2\u00d5\u00d6\7%\2\2\u00d6\u00dd\5`\61\2")
        buf.write("\u00d7\u00d8\7\67\2\2\u00d8\u00d9\5\24\13\2\u00d9\u00da")
        buf.write("\7%\2\2\u00da\u00db\5^\60\2\u00db\u00dd\3\2\2\2\u00dc")
        buf.write("\u00c7\3\2\2\2\u00dc\u00cd\3\2\2\2\u00dc\u00d4\3\2\2\2")
        buf.write("\u00dc\u00d7\3\2\2\2\u00dd\21\3\2\2\2\u00de\u00e3\3\2")
        buf.write("\2\2\u00df\u00e0\7\65\2\2\u00e0\u00e1\7\67\2\2\u00e1\u00e3")
        buf.write("\5\22\n\2\u00e2\u00de\3\2\2\2\u00e2\u00df\3\2\2\2\u00e3")
        buf.write("\23\3\2\2\2\u00e4\u00e9\3\2\2\2\u00e5\u00e6\7\65\2\2\u00e6")
        buf.write("\u00e7\7\67\2\2\u00e7\u00e9\5\24\13\2\u00e8\u00e4\3\2")
        buf.write("\2\2\u00e8\u00e5\3\2\2\2\u00e9\25\3\2\2\2\u00ea\u00eb")
        buf.write("\7\17\2\2\u00eb\u00ec\5\30\r\2\u00ec\u00ed\t\2\2\2\u00ed")
        buf.write("\27\3\2\2\2\u00ee\u00f4\5\32\16\2\u00ef\u00f0\5\32\16")
        buf.write("\2\u00f0\u00f1\7\65\2\2\u00f1\u00f2\5\30\r\2\u00f2\u00f4")
        buf.write("\3\2\2\2\u00f3\u00ee\3\2\2\2\u00f3\u00ef\3\2\2\2\u00f4")
        buf.write("\31\3\2\2\2\u00f5\u00f6\7\67\2\2\u00f6\u00f7\7%\2\2\u00f7")
        buf.write("\u00f8\5`\61\2\u00f8\33\3\2\2\2\u00f9\u00fa\7\7\2\2\u00fa")
        buf.write("\u00fb\7\67\2\2\u00fb\u00fd\7/\2\2\u00fc\u00fe\5&\24\2")
        buf.write("\u00fd\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\3")
        buf.write("\2\2\2\u00ff\u0101\7\60\2\2\u0100\u0102\5\36\20\2\u0101")
        buf.write("\u0100\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0104\3\2\2\2")
        buf.write("\u0103\u0105\7;\2\2\u0104\u0103\3\2\2\2\u0104\u0105\3")
        buf.write("\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107\5Z.\2\u0107\u0108")
        buf.write("\t\2\2\2\u0108\35\3\2\2\2\u0109\u010a\7/\2\2\u010a\u010b")
        buf.write("\5\u0088E\2\u010b\u010c\5 \21\2\u010c\u010d\7\60\2\2\u010d")
        buf.write("\u0110\3\2\2\2\u010e\u0110\5\u0088E\2\u010f\u0109\3\2")
        buf.write("\2\2\u010f\u010e\3\2\2\2\u0110\37\3\2\2\2\u0111\u0117")
        buf.write("\3\2\2\2\u0112\u0113\7\65\2\2\u0113\u0114\5\u0088E\2\u0114")
        buf.write("\u0115\5 \21\2\u0115\u0117\3\2\2\2\u0116\u0111\3\2\2\2")
        buf.write("\u0116\u0112\3\2\2\2\u0117!\3\2\2\2\u0118\u0119\7\67\2")
        buf.write("\2\u0119\u011a\t\3\2\2\u011a#\3\2\2\2\u011b\u011c\7\7")
        buf.write("\2\2\u011c\u011d\7/\2\2\u011d\u011e\5\"\22\2\u011e\u011f")
        buf.write("\7\60\2\2\u011f\u0120\7\67\2\2\u0120\u0122\7/\2\2\u0121")
        buf.write("\u0123\5&\24\2\u0122\u0121\3\2\2\2\u0122\u0123\3\2\2\2")
        buf.write("\u0123\u0124\3\2\2\2\u0124\u0126\7\60\2\2\u0125\u0127")
        buf.write("\5\u0088E\2\u0126\u0125\3\2\2\2\u0126\u0127\3\2\2\2\u0127")
        buf.write("\u0129\3\2\2\2\u0128\u012a\7;\2\2\u0129\u0128\3\2\2\2")
        buf.write("\u0129\u012a\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\5")
        buf.write("Z.\2\u012c\u012d\t\2\2\2\u012d%\3\2\2\2\u012e\u012f\7")
        buf.write("\67\2\2\u012f\u013a\5\u0088E\2\u0130\u0131\7\67\2\2\u0131")
        buf.write("\u0132\5\24\13\2\u0132\u0133\5\u0088E\2\u0133\u013a\3")
        buf.write("\2\2\2\u0134\u013a\5(\25\2\u0135\u0136\5(\25\2\u0136\u0137")
        buf.write("\7\65\2\2\u0137\u0138\5&\24\2\u0138\u013a\3\2\2\2\u0139")
        buf.write("\u012e\3\2\2\2\u0139\u0130\3\2\2\2\u0139\u0134\3\2\2\2")
        buf.write("\u0139\u0135\3\2\2\2\u013a\'\3\2\2\2\u013b\u013c\7\67")
        buf.write("\2\2\u013c\u0142\5\u0088E\2\u013d\u013e\7\67\2\2\u013e")
        buf.write("\u013f\5*\26\2\u013f\u0140\5\u0088E\2\u0140\u0142\3\2")
        buf.write("\2\2\u0141\u013b\3\2\2\2\u0141\u013d\3\2\2\2\u0142)\3")
        buf.write("\2\2\2\u0143\u0144\7\65\2\2\u0144\u0149\7\67\2\2\u0145")
        buf.write("\u0146\7\65\2\2\u0146\u0147\7\67\2\2\u0147\u0149\5*\26")
        buf.write("\2\u0148\u0143\3\2\2\2\u0148\u0145\3\2\2\2\u0149+\3\2")
        buf.write("\2\2\u014a\u014b\7\b\2\2\u014b\u014c\7\67\2\2\u014c\u014d")
        buf.write("\7\t\2\2\u014d\u014e\7\61\2\2\u014e\u014f\5\62\32\2\u014f")
        buf.write("\u0150\5.\30\2\u0150\u0151\5\62\32\2\u0151\u0152\7\62")
        buf.write("\2\2\u0152\u0153\t\2\2\2\u0153-\3\2\2\2\u0154\u0155\5")
        buf.write("\64\33\2\u0155\u0156\5\62\32\2\u0156\u0157\5\60\31\2\u0157")
        buf.write("/\3\2\2\2\u0158\u015e\3\2\2\2\u0159\u015a\5\64\33\2\u015a")
        buf.write("\u015b\5\62\32\2\u015b\u015c\5\60\31\2\u015c\u015e\3\2")
        buf.write("\2\2\u015d\u0158\3\2\2\2\u015d\u0159\3\2\2\2\u015e\61")
        buf.write("\3\2\2\2\u015f\u0163\3\2\2\2\u0160\u0161\7;\2\2\u0161")
        buf.write("\u0163\5\62\32\2\u0162\u015f\3\2\2\2\u0162\u0160\3\2\2")
        buf.write("\2\u0163\63\3\2\2\2\u0164\u0165\7\67\2\2\u0165\u0166\5")
        buf.write("\66\34\2\u0166\u0167\5\u0088E\2\u0167\u0168\t\2\2\2\u0168")
        buf.write("\65\3\2\2\2\u0169\u016e\3\2\2\2\u016a\u016b\7\65\2\2\u016b")
        buf.write("\u016c\7\67\2\2\u016c\u016e\5\66\34\2\u016d\u0169\3\2")
        buf.write("\2\2\u016d\u016a\3\2\2\2\u016e\67\3\2\2\2\u016f\u0170")
        buf.write("\7\b\2\2\u0170\u0171\7\67\2\2\u0171\u0172\7\n\2\2\u0172")
        buf.write("\u0173\7\61\2\2\u0173\u0174\5\62\32\2\u0174\u0175\5:\36")
        buf.write("\2\u0175\u0176\5\62\32\2\u0176\u0177\7\62\2\2\u0177\u0178")
        buf.write("\t\2\2\2\u01789\3\2\2\2\u0179\u017a\5> \2\u017a\u017b")
        buf.write("\5<\37\2\u017b;\3\2\2\2\u017c\u0181\3\2\2\2\u017d\u017e")
        buf.write("\5> \2\u017e\u017f\5<\37\2\u017f\u0181\3\2\2\2\u0180\u017c")
        buf.write("\3\2\2\2\u0180\u017d\3\2\2\2\u0181=\3\2\2\2\u0182\u0183")
        buf.write("\7\67\2\2\u0183\u0185\7/\2\2\u0184\u0186\5&\24\2\u0185")
        buf.write("\u0184\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write("\u0187\u0189\7\60\2\2\u0188\u018a\5\u0088E\2\u0189\u0188")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u018c\t\2\2\2\u018c?\3\2\2\2\u018d\u0190\5\16\b\2\u018e")
        buf.write("\u0190\5\26\f\2\u018f\u018d\3\2\2\2\u018f\u018e\3\2\2")
        buf.write("\2\u0190A\3\2\2\2\u0191\u0192\5F$\2\u0192\u0193\5D#\2")
        buf.write("\u0193\u0194\5`\61\2\u0194\u0195\t\2\2\2\u0195C\3\2\2")
        buf.write("\2\u0196\u0197\t\4\2\2\u0197E\3\2\2\2\u0198\u0199\7\67")
        buf.write("\2\2\u0199\u019a\5H%\2\u019aG\3\2\2\2\u019b\u01a3\3\2")
        buf.write("\2\2\u019c\u019f\5v<\2\u019d\u019f\5t;\2\u019e\u019c\3")
        buf.write("\2\2\2\u019e\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1")
        buf.write("\5H%\2\u01a1\u01a3\3\2\2\2\u01a2\u019b\3\2\2\2\u01a2\u019e")
        buf.write("\3\2\2\2\u01a3I\3\2\2\2\u01a4\u01a5\7\3\2\2\u01a5\u01a6")
        buf.write("\7/\2\2\u01a6\u01a7\5`\61\2\u01a7\u01a8\7\60\2\2\u01a8")
        buf.write("\u01ad\5Z.\2\u01a9\u01aa\7\4\2\2\u01aa\u01ae\5J&\2\u01ab")
        buf.write("\u01ac\7\4\2\2\u01ac\u01ae\5Z.\2\u01ad\u01a9\3\2\2\2\u01ad")
        buf.write("\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01aeK\3\2\2\2\u01af")
        buf.write("\u01c2\7\5\2\2\u01b0\u01b1\t\5\2\2\u01b1\u01b2\7\65\2")
        buf.write("\2\u01b2\u01b3\t\5\2\2\u01b3\u01b4\7-\2\2\u01b4\u01b5")
        buf.write("\7\23\2\2\u01b5\u01b6\5`\61\2\u01b6\u01b7\5Z.\2\u01b7")
        buf.write("\u01c3\3\2\2\2\u01b8\u01b9\5N(\2\u01b9\u01ba\t\2\2\2\u01ba")
        buf.write("\u01bb\5`\61\2\u01bb\u01bc\t\2\2\2\u01bc\u01bd\5P)\2\u01bd")
        buf.write("\u01be\5Z.\2\u01be\u01c3\3\2\2\2\u01bf\u01c0\5`\61\2\u01c0")
        buf.write("\u01c1\5Z.\2\u01c1\u01c3\3\2\2\2\u01c2\u01b0\3\2\2\2\u01c2")
        buf.write("\u01b8\3\2\2\2\u01c2\u01bf\3\2\2\2\u01c3M\3\2\2\2\u01c4")
        buf.write("\u01c5\7\67\2\2\u01c5\u01c6\7-\2\2\u01c6\u01d3\5`\61\2")
        buf.write("\u01c7\u01c8\7\67\2\2\u01c8\u01c9\5D#\2\u01c9\u01ca\5")
        buf.write("`\61\2\u01ca\u01d3\3\2\2\2\u01cb\u01cc\7\20\2\2\u01cc")
        buf.write("\u01ce\7\67\2\2\u01cd\u01cf\5\u0088E\2\u01ce\u01cd\3\2")
        buf.write("\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1")
        buf.write("\7%\2\2\u01d1\u01d3\5`\61\2\u01d2\u01c4\3\2\2\2\u01d2")
        buf.write("\u01c7\3\2\2\2\u01d2\u01cb\3\2\2\2\u01d3O\3\2\2\2\u01d4")
        buf.write("\u01d5\7\67\2\2\u01d5\u01d6\5D#\2\u01d6\u01d7\5`\61\2")
        buf.write("\u01d7Q\3\2\2\2\u01d8\u01d9\7\22\2\2\u01d9\u01da\t\2\2")
        buf.write("\2\u01daS\3\2\2\2\u01db\u01dc\7\21\2\2\u01dc\u01dd\t\2")
        buf.write("\2\2\u01ddU\3\2\2\2\u01de\u01e7\7\6\2\2\u01df\u01e1\5")
        buf.write("`\61\2\u01e0\u01df\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e2")
        buf.write("\3\2\2\2\u01e2\u01e8\7\66\2\2\u01e3\u01e5\5`\61\2\u01e4")
        buf.write("\u01e3\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6\3\2\2\2")
        buf.write("\u01e6\u01e8\7;\2\2\u01e7\u01e0\3\2\2\2\u01e7\u01e4\3")
        buf.write("\2\2\2\u01e8W\3\2\2\2\u01e9\u01ec\7\67\2\2\u01ea\u01ec")
        buf.write("\5F$\2\u01eb\u01e9\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec\u01ed")
        buf.write("\3\2\2\2\u01ed\u01ef\7/\2\2\u01ee\u01f0\5\u0092J\2\u01ef")
        buf.write("\u01ee\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\3\2\2\2")
        buf.write("\u01f1\u01f2\7\60\2\2\u01f2\u01f3\t\2\2\2\u01f3Y\3\2\2")
        buf.write("\2\u01f4\u01f6\7\61\2\2\u01f5\u01f7\7;\2\2\u01f6\u01f5")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8")
        buf.write("\u01fa\5\\/\2\u01f9\u01fb\7;\2\2\u01fa\u01f9\3\2\2\2\u01fa")
        buf.write("\u01fb\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fe\7\62\2")
        buf.write("\2\u01fd\u01ff\7\66\2\2\u01fe\u01fd\3\2\2\2\u01fe\u01ff")
        buf.write("\3\2\2\2\u01ff[\3\2\2\2\u0200\u0207\3\2\2\2\u0201\u0202")
        buf.write("\5\f\7\2\u0202\u0203\5\\/\2\u0203\u0207\3\2\2\2\u0204")
        buf.write("\u0205\7;\2\2\u0205\u0207\5\\/\2\u0206\u0200\3\2\2\2\u0206")
        buf.write("\u0201\3\2\2\2\u0206\u0204\3\2\2\2\u0207]\3\2\2\2\u0208")
        buf.write("\u020e\5`\61\2\u0209\u020a\5`\61\2\u020a\u020b\7\65\2")
        buf.write("\2\u020b\u020c\5^\60\2\u020c\u020e\3\2\2\2\u020d\u0208")
        buf.write("\3\2\2\2\u020d\u0209\3\2\2\2\u020e_\3\2\2\2\u020f\u0210")
        buf.write("\b\61\1\2\u0210\u0211\5b\62\2\u0211\u0217\3\2\2\2\u0212")
        buf.write("\u0213\f\4\2\2\u0213\u0214\7#\2\2\u0214\u0216\5b\62\2")
        buf.write("\u0215\u0212\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0215\3")
        buf.write("\2\2\2\u0217\u0218\3\2\2\2\u0218a\3\2\2\2\u0219\u0217")
        buf.write("\3\2\2\2\u021a\u021b\b\62\1\2\u021b\u021c\5d\63\2\u021c")
        buf.write("\u0222\3\2\2\2\u021d\u021e\f\4\2\2\u021e\u021f\7\"\2\2")
        buf.write("\u021f\u0221\5d\63\2\u0220\u021d\3\2\2\2\u0221\u0224\3")
        buf.write("\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223c")
        buf.write("\3\2\2\2\u0224\u0222\3\2\2\2\u0225\u0226\b\63\1\2\u0226")
        buf.write("\u0227\5f\64\2\u0227\u022d\3\2\2\2\u0228\u0229\f\4\2\2")
        buf.write("\u0229\u022a\t\6\2\2\u022a\u022c\5f\64\2\u022b\u0228\3")
        buf.write("\2\2\2\u022c\u022f\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022e")
        buf.write("\3\2\2\2\u022ee\3\2\2\2\u022f\u022d\3\2\2\2\u0230\u0231")
        buf.write("\b\64\1\2\u0231\u0232\5h\65\2\u0232\u0238\3\2\2\2\u0233")
        buf.write("\u0234\f\4\2\2\u0234\u0235\t\7\2\2\u0235\u0237\5h\65\2")
        buf.write("\u0236\u0233\3\2\2\2\u0237\u023a\3\2\2\2\u0238\u0236\3")
        buf.write("\2\2\2\u0238\u0239\3\2\2\2\u0239g\3\2\2\2\u023a\u0238")
        buf.write("\3\2\2\2\u023b\u023c\b\65\1\2\u023c\u023d\5j\66\2\u023d")
        buf.write("\u0243\3\2\2\2\u023e\u023f\f\4\2\2\u023f\u0240\t\b\2\2")
        buf.write("\u0240\u0242\5j\66\2\u0241\u023e\3\2\2\2\u0242\u0245\3")
        buf.write("\2\2\2\u0243\u0241\3\2\2\2\u0243\u0244\3\2\2\2\u0244i")
        buf.write("\3\2\2\2\u0245\u0243\3\2\2\2\u0246\u0247\b\66\1\2\u0247")
        buf.write("\u0248\5l\67\2\u0248\u024e\3\2\2\2\u0249\u024a\f\4\2\2")
        buf.write("\u024a\u024b\t\t\2\2\u024b\u024d\5l\67\2\u024c\u0249\3")
        buf.write("\2\2\2\u024d\u0250\3\2\2\2\u024e\u024c\3\2\2\2\u024e\u024f")
        buf.write("\3\2\2\2\u024fk\3\2\2\2\u0250\u024e\3\2\2\2\u0251\u0252")
        buf.write("\7$\2\2\u0252\u0257\5l\67\2\u0253\u0254\7\30\2\2\u0254")
        buf.write("\u0257\5l\67\2\u0255\u0257\5n8\2\u0256\u0251\3\2\2\2\u0256")
        buf.write("\u0253\3\2\2\2\u0256\u0255\3\2\2\2\u0257m\3\2\2\2\u0258")
        buf.write("\u0259\5r:\2\u0259\u025a\5p9\2\u025ao\3\2\2\2\u025b\u0264")
        buf.write("\3\2\2\2\u025c\u0260\5t;\2\u025d\u0260\5v<\2\u025e\u0260")
        buf.write("\5x=\2\u025f\u025c\3\2\2\2\u025f\u025d\3\2\2\2\u025f\u025e")
        buf.write("\3\2\2\2\u0260\u0261\3\2\2\2\u0261\u0262\5p9\2\u0262\u0264")
        buf.write("\3\2\2\2\u0263\u025b\3\2\2\2\u0263\u025f\3\2\2\2\u0264")
        buf.write("q\3\2\2\2\u0265\u026c\5z>\2\u0266\u026c\7\67\2\2\u0267")
        buf.write("\u0268\7/\2\2\u0268\u0269\5`\61\2\u0269\u026a\7\60\2\2")
        buf.write("\u026a\u026c\3\2\2\2\u026b\u0265\3\2\2\2\u026b\u0266\3")
        buf.write("\2\2\2\u026b\u0267\3\2\2\2\u026cs\3\2\2\2\u026d\u026e")
        buf.write("\7\63\2\2\u026e\u026f\5`\61\2\u026f\u0270\7\64\2\2\u0270")
        buf.write("u\3\2\2\2\u0271\u0272\7+\2\2\u0272\u0273\7\67\2\2\u0273")
        buf.write("w\3\2\2\2\u0274\u0276\7/\2\2\u0275\u0277\5\u0092J\2\u0276")
        buf.write("\u0275\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u0278\3\2\2\2")
        buf.write("\u0278\u0279\7\60\2\2\u0279y\3\2\2\2\u027a\u0283\79\2")
        buf.write("\2\u027b\u0283\78\2\2\u027c\u0283\7:\2\2\u027d\u0283\7")
        buf.write("\25\2\2\u027e\u0283\7\26\2\2\u027f\u0283\7\24\2\2\u0280")
        buf.write("\u0283\5|?\2\u0281\u0283\5\u008aF\2\u0282\u027a\3\2\2")
        buf.write("\2\u0282\u027b\3\2\2\2\u0282\u027c\3\2\2\2\u0282\u027d")
        buf.write("\3\2\2\2\u0282\u027e\3\2\2\2\u0282\u027f\3\2\2\2\u0282")
        buf.write("\u0280\3\2\2\2\u0282\u0281\3\2\2\2\u0283{\3\2\2\2\u0284")
        buf.write("\u0285\5\u0084C\2\u0285\u0286\7\61\2\2\u0286\u0287\5\u0080")
        buf.write("A\2\u0287\u0288\7\62\2\2\u0288}\3\2\2\2\u0289\u028a\7")
        buf.write("\61\2\2\u028a\u028b\5\u0080A\2\u028b\u028c\7\62\2\2\u028c")
        buf.write("\177\3\2\2\2\u028d\u0293\5\u0082B\2\u028e\u028f\5\u0082")
        buf.write("B\2\u028f\u0290\7\65\2\2\u0290\u0291\5\u0080A\2\u0291")
        buf.write("\u0293\3\2\2\2\u0292\u028d\3\2\2\2\u0292\u028e\3\2\2\2")
        buf.write("\u0293\u0081\3\2\2\2\u0294\u029e\5~@\2\u0295\u029e\5\u008a")
        buf.write("F\2\u0296\u029e\79\2\2\u0297\u029e\78\2\2\u0298\u029e")
        buf.write("\7:\2\2\u0299\u029e\7\25\2\2\u029a\u029e\7\26\2\2\u029b")
        buf.write("\u029e\7\24\2\2\u029c\u029e\7\67\2\2\u029d\u0294\3\2\2")
        buf.write("\2\u029d\u0295\3\2\2\2\u029d\u0296\3\2\2\2\u029d\u0297")
        buf.write("\3\2\2\2\u029d\u0298\3\2\2\2\u029d\u0299\3\2\2\2\u029d")
        buf.write("\u029a\3\2\2\2\u029d\u029b\3\2\2\2\u029d\u029c\3\2\2\2")
        buf.write("\u029e\u0083\3\2\2\2\u029f\u02a0\7\63\2\2\u02a0\u02a1")
        buf.write("\t\n\2\2\u02a1\u02a2\7\64\2\2\u02a2\u02a3\5\u0086D\2\u02a3")
        buf.write("\u02a4\5\u0088E\2\u02a4\u0085\3\2\2\2\u02a5\u02ab\3\2")
        buf.write("\2\2\u02a6\u02a7\7\63\2\2\u02a7\u02a8\t\n\2\2\u02a8\u02a9")
        buf.write("\7\64\2\2\u02a9\u02ab\5\u0086D\2\u02aa\u02a5\3\2\2\2\u02aa")
        buf.write("\u02a6\3\2\2\2\u02ab\u0087\3\2\2\2\u02ac\u02b3\7\f\2\2")
        buf.write("\u02ad\u02b3\7\r\2\2\u02ae\u02b3\7\13\2\2\u02af\u02b3")
        buf.write("\7\16\2\2\u02b0\u02b3\7\67\2\2\u02b1\u02b3\5\u0084C\2")
        buf.write("\u02b2\u02ac\3\2\2\2\u02b2\u02ad\3\2\2\2\u02b2\u02ae\3")
        buf.write("\2\2\2\u02b2\u02af\3\2\2\2\u02b2\u02b0\3\2\2\2\u02b2\u02b1")
        buf.write("\3\2\2\2\u02b3\u0089\3\2\2\2\u02b4\u02b5\7\67\2\2\u02b5")
        buf.write("\u02b6\7\61\2\2\u02b6\u02b7\5\u008cG\2\u02b7\u02b8\7\62")
        buf.write("\2\2\u02b8\u008b\3\2\2\2\u02b9\u02bc\3\2\2\2\u02ba\u02bc")
        buf.write("\5\u008eH\2\u02bb\u02b9\3\2\2\2\u02bb\u02ba\3\2\2\2\u02bc")
        buf.write("\u008d\3\2\2\2\u02bd\u02c3\5\u0090I\2\u02be\u02bf\5\u0090")
        buf.write("I\2\u02bf\u02c0\7\65\2\2\u02c0\u02c1\5\u008eH\2\u02c1")
        buf.write("\u02c3\3\2\2\2\u02c2\u02bd\3\2\2\2\u02c2\u02be\3\2\2\2")
        buf.write("\u02c3\u008f\3\2\2\2\u02c4\u02c5\7\67\2\2\u02c5\u02c6")
        buf.write("\7,\2\2\u02c6\u02c7\5`\61\2\u02c7\u0091\3\2\2\2\u02c8")
        buf.write("\u02ce\5`\61\2\u02c9\u02ca\5`\61\2\u02ca\u02cb\7\65\2")
        buf.write("\2\u02cb\u02cc\5\u0092J\2\u02cc\u02ce\3\2\2\2\u02cd\u02c8")
        buf.write("\3\2\2\2\u02cd\u02c9\3\2\2\2\u02ce\u0093\3\2\2\2B\u009f")
        buf.write("\u00a6\u00ae\u00b7\u00c1\u00cb\u00d2\u00dc\u00e2\u00e8")
        buf.write("\u00f3\u00fd\u0101\u0104\u010f\u0116\u0122\u0126\u0129")
        buf.write("\u0139\u0141\u0148\u015d\u0162\u016d\u0180\u0185\u0189")
        buf.write("\u018f\u019e\u01a2\u01ad\u01c2\u01ce\u01d2\u01e0\u01e4")
        buf.write("\u01e7\u01eb\u01ef\u01f6\u01fa\u01fe\u0206\u020d\u0217")
        buf.write("\u0222\u022d\u0238\u0243\u024e\u0256\u025f\u0263\u026b")
        buf.write("\u0276\u0282\u0292\u029d\u02aa\u02b2\u02bb\u02c2\u02cd")
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
                      "COMMA", "SEMI", "ID", "FLOAT_LIT", "INT_LIT", "STRING_LIT", 
                      "NEWLINE", "WS", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_newlines = 1
    RULE_more_declared = 2
    RULE_declared = 3
    RULE_list_statement = 4
    RULE_statement = 5
    RULE_variables_declared = 6
    RULE_var_decl = 7
    RULE_type_name_ids = 8
    RULE_comma_ids = 9
    RULE_constants_declared = 10
    RULE_const_decl_list = 11
    RULE_const_decl = 12
    RULE_function_declared = 13
    RULE_return_type = 14
    RULE_more_types = 15
    RULE_receiver = 16
    RULE_method_declared = 17
    RULE_params_list = 18
    RULE_param = 19
    RULE_comma_param_ids = 20
    RULE_struct_declared = 21
    RULE_struct_type_list = 22
    RULE_more_struct_fields = 23
    RULE_opt_newlines = 24
    RULE_struct_field = 25
    RULE_more_ids = 26
    RULE_interface_declared = 27
    RULE_interface_type_list = 28
    RULE_more_interface_methods = 29
    RULE_interface_method = 30
    RULE_declared_statement = 31
    RULE_assign_statement = 32
    RULE_assign_op = 33
    RULE_assign_lhs = 34
    RULE_more_access = 35
    RULE_if_statement = 36
    RULE_for_statement = 37
    RULE_for_init = 38
    RULE_for_update = 39
    RULE_break_statement = 40
    RULE_continue_statement = 41
    RULE_return_statement = 42
    RULE_call_statement = 43
    RULE_block_stmt = 44
    RULE_block_content = 45
    RULE_expr_list = 46
    RULE_expression = 47
    RULE_expression1 = 48
    RULE_expression2 = 49
    RULE_expression3 = 50
    RULE_expression4 = 51
    RULE_expression5 = 52
    RULE_expression6 = 53
    RULE_expression7 = 54
    RULE_more_access_expr = 55
    RULE_operand = 56
    RULE_element_access = 57
    RULE_field_access = 58
    RULE_call_expr = 59
    RULE_literal = 60
    RULE_typed_array_literal = 61
    RULE_untyped_array_literal = 62
    RULE_literal_list = 63
    RULE_literal_item = 64
    RULE_array_type = 65
    RULE_more_dimensions = 66
    RULE_type_name = 67
    RULE_struct_literal = 68
    RULE_optional_field_list = 69
    RULE_field_list = 70
    RULE_field_init = 71
    RULE_list_expression = 72

    ruleNames =  [ "program", "newlines", "more_declared", "declared", "list_statement", 
                   "statement", "variables_declared", "var_decl", "type_name_ids", 
                   "comma_ids", "constants_declared", "const_decl_list", 
                   "const_decl", "function_declared", "return_type", "more_types", 
                   "receiver", "method_declared", "params_list", "param", 
                   "comma_param_ids", "struct_declared", "struct_type_list", 
                   "more_struct_fields", "opt_newlines", "struct_field", 
                   "more_ids", "interface_declared", "interface_type_list", 
                   "more_interface_methods", "interface_method", "declared_statement", 
                   "assign_statement", "assign_op", "assign_lhs", "more_access", 
                   "if_statement", "for_statement", "for_init", "for_update", 
                   "break_statement", "continue_statement", "return_statement", 
                   "call_statement", "block_stmt", "block_content", "expr_list", 
                   "expression", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7", 
                   "more_access_expr", "operand", "element_access", "field_access", 
                   "call_expr", "literal", "typed_array_literal", "untyped_array_literal", 
                   "literal_list", "literal_item", "array_type", "more_dimensions", 
                   "type_name", "struct_literal", "optional_field_list", 
                   "field_list", "field_init", "list_expression" ]

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
    FLOAT_LIT=54
    INT_LIT=55
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

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

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
            self.state = 146
            self.match(MiniGoParser.CONST)
            self.state = 147
            self.match(MiniGoParser.ID)
            self.state = 148
            self.match(MiniGoParser.ASSIGN)
            self.state = 149
            self.expression(0)
            self.state = 150
            self.match(MiniGoParser.SEMI)
            self.state = 152
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(MiniGoParser.NEWLINE)
                self.state = 156
                self.newlines()
                pass


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
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.newlines()
                self.state = 161
                self.declared()
                self.state = 162
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

        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


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
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 166
                self.variables_declared()
                pass

            elif la_ == 2:
                self.state = 167
                self.constants_declared()
                pass

            elif la_ == 3:
                self.state = 168
                self.function_declared()
                pass

            elif la_ == 4:
                self.state = 169
                self.method_declared()
                pass

            elif la_ == 5:
                self.state = 170
                self.struct_declared()
                pass

            elif la_ == 6:
                self.state = 171
                self.interface_declared()
                pass


            self.state = 174
            self.newlines()
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
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.statement()
                self.state = 178
                self.newlines()
                self.state = 179
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
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.declared_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 187
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 188
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 189
                self.call_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 190
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

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


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
            self.state = 193
            self.match(MiniGoParser.VAR)
            self.state = 194
            self.var_decl()
            self.state = 195
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


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def type_name_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Type_name_idsContext,0)


        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def comma_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Comma_idsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(MiniGoParser.ID)
                self.state = 198
                self.type_name()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 199
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 200
                    self.expression(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(MiniGoParser.ID)
                self.state = 204
                self.type_name_ids()
                self.state = 205
                self.type_name()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 206
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 207
                    self.expr_list()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.match(MiniGoParser.ID)

                self.state = 211
                self.match(MiniGoParser.ASSIGN)
                self.state = 212
                self.expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 213
                self.match(MiniGoParser.ID)
                self.state = 214
                self.comma_ids()

                self.state = 215
                self.match(MiniGoParser.ASSIGN)
                self.state = 216
                self.expr_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_name_idsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_name_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Type_name_idsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_name_ids

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name_ids" ):
                return visitor.visitType_name_ids(self)
            else:
                return visitor.visitChildren(self)




    def type_name_ids(self):

        localctx = MiniGoParser.Type_name_idsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_type_name_ids)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(MiniGoParser.COMMA)
                self.state = 222
                self.match(MiniGoParser.ID)
                self.state = 223
                self.type_name_ids()
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


    class Comma_idsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def comma_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Comma_idsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_comma_ids

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma_ids" ):
                return visitor.visitComma_ids(self)
            else:
                return visitor.visitChildren(self)




    def comma_ids(self):

        localctx = MiniGoParser.Comma_idsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comma_ids)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ASSIGN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(MiniGoParser.COMMA)
                self.state = 228
                self.match(MiniGoParser.ID)
                self.state = 229
                self.comma_ids()
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
        self.enterRule(localctx, 20, self.RULE_constants_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(MiniGoParser.CONST)
            self.state = 233
            self.const_decl_list()
            self.state = 234
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
        self.enterRule(localctx, 22, self.RULE_const_decl_list)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.const_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.const_decl()
                self.state = 238
                self.match(MiniGoParser.COMMA)
                self.state = 239
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
        self.enterRule(localctx, 24, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(MiniGoParser.ID)
            self.state = 244
            self.match(MiniGoParser.ASSIGN)
            self.state = 245
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

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

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


        def return_type(self):
            return self.getTypedRuleContext(MiniGoParser.Return_typeContext,0)


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
            self.state = 247
            self.match(MiniGoParser.FUNC)
            self.state = 248
            self.match(MiniGoParser.ID)
            self.state = 249
            self.match(MiniGoParser.LP)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 250
                self.params_list()


            self.state = 253
            self.match(MiniGoParser.RP)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 254
                self.return_type()


            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 257
                self.match(MiniGoParser.NEWLINE)


            self.state = 260
            self.block_stmt()
            self.state = 261
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


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def more_types(self):
            return self.getTypedRuleContext(MiniGoParser.More_typesContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_return_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_type" ):
                return visitor.visitReturn_type(self)
            else:
                return visitor.visitChildren(self)




    def return_type(self):

        localctx = MiniGoParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_return_type)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(MiniGoParser.LP)
                self.state = 264
                self.type_name()
                self.state = 265
                self.more_types()
                self.state = 266
                self.match(MiniGoParser.RP)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
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


    class More_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def more_types(self):
            return self.getTypedRuleContext(MiniGoParser.More_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore_types" ):
                return visitor.visitMore_types(self)
            else:
                return visitor.visitChildren(self)




    def more_types(self):

        localctx = MiniGoParser.More_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_more_types)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RP]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.match(MiniGoParser.COMMA)
                self.state = 273
                self.type_name()
                self.state = 274
                self.more_types()
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
        self.enterRule(localctx, 32, self.RULE_receiver)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(MiniGoParser.ID)
            self.state = 279
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
        self.enterRule(localctx, 34, self.RULE_method_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(MiniGoParser.FUNC)
            self.state = 282
            self.match(MiniGoParser.LP)
            self.state = 283
            self.receiver()
            self.state = 284
            self.match(MiniGoParser.RP)
            self.state = 285
            self.match(MiniGoParser.ID)
            self.state = 286
            self.match(MiniGoParser.LP)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 287
                self.params_list()


            self.state = 290
            self.match(MiniGoParser.RP)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 291
                self.type_name()


            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 294
                self.match(MiniGoParser.NEWLINE)


            self.state = 297
            self.block_stmt()
            self.state = 298
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


    class Params_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def comma_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Comma_idsContext,0)


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
        self.enterRule(localctx, 36, self.RULE_params_list)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(MiniGoParser.ID)
                self.state = 301
                self.type_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.match(MiniGoParser.ID)
                self.state = 303
                self.comma_ids()
                self.state = 304
                self.type_name()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 306
                self.param()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 307
                self.param()
                self.state = 308
                self.match(MiniGoParser.COMMA)
                self.state = 309
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def comma_param_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Comma_param_idsContext,0)


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
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(MiniGoParser.ID)
                self.state = 314
                self.type_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.match(MiniGoParser.ID)
                self.state = 316
                self.comma_param_ids()
                self.state = 317
                self.type_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comma_param_idsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def comma_param_ids(self):
            return self.getTypedRuleContext(MiniGoParser.Comma_param_idsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_comma_param_ids

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma_param_ids" ):
                return visitor.visitComma_param_ids(self)
            else:
                return visitor.visitChildren(self)




    def comma_param_ids(self):

        localctx = MiniGoParser.Comma_param_idsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_comma_param_ids)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.match(MiniGoParser.COMMA)
                self.state = 322
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.match(MiniGoParser.COMMA)
                self.state = 324
                self.match(MiniGoParser.ID)
                self.state = 325
                self.comma_param_ids()
                pass


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

        def opt_newlines(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Opt_newlinesContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Opt_newlinesContext,i)


        def struct_type_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_type_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declared" ):
                return visitor.visitStruct_declared(self)
            else:
                return visitor.visitChildren(self)




    def struct_declared(self):

        localctx = MiniGoParser.Struct_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_struct_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(MiniGoParser.TYPE)
            self.state = 329
            self.match(MiniGoParser.ID)
            self.state = 330
            self.match(MiniGoParser.STRUCT)
            self.state = 331
            self.match(MiniGoParser.LB)
            self.state = 332
            self.opt_newlines()
            self.state = 333
            self.struct_type_list()
            self.state = 334
            self.opt_newlines()
            self.state = 335
            self.match(MiniGoParser.RB)
            self.state = 336
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

        def struct_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,0)


        def opt_newlines(self):
            return self.getTypedRuleContext(MiniGoParser.Opt_newlinesContext,0)


        def more_struct_fields(self):
            return self.getTypedRuleContext(MiniGoParser.More_struct_fieldsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type_list" ):
                return visitor.visitStruct_type_list(self)
            else:
                return visitor.visitChildren(self)




    def struct_type_list(self):

        localctx = MiniGoParser.Struct_type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_struct_type_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.struct_field()
            self.state = 339
            self.opt_newlines()
            self.state = 340
            self.more_struct_fields()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_struct_fieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,0)


        def opt_newlines(self):
            return self.getTypedRuleContext(MiniGoParser.Opt_newlinesContext,0)


        def more_struct_fields(self):
            return self.getTypedRuleContext(MiniGoParser.More_struct_fieldsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_struct_fields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore_struct_fields" ):
                return visitor.visitMore_struct_fields(self)
            else:
                return visitor.visitChildren(self)




    def more_struct_fields(self):

        localctx = MiniGoParser.More_struct_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_more_struct_fields)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RB, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.struct_field()
                self.state = 344
                self.opt_newlines()
                self.state = 345
                self.more_struct_fields()
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


    class Opt_newlinesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def opt_newlines(self):
            return self.getTypedRuleContext(MiniGoParser.Opt_newlinesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_opt_newlines

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpt_newlines" ):
                return visitor.visitOpt_newlines(self)
            else:
                return visitor.visitChildren(self)




    def opt_newlines(self):

        localctx = MiniGoParser.Opt_newlinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_opt_newlines)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.match(MiniGoParser.NEWLINE)
                self.state = 351
                self.opt_newlines()
                pass


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


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_struct_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(MiniGoParser.ID)
            self.state = 355
            self.more_ids()
            self.state = 356
            self.type_name()
            self.state = 357
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
        self.enterRule(localctx, 52, self.RULE_more_ids)
        try:
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.match(MiniGoParser.COMMA)
                self.state = 361
                self.match(MiniGoParser.ID)
                self.state = 362
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

        def opt_newlines(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Opt_newlinesContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Opt_newlinesContext,i)


        def interface_type_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_type_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declared" ):
                return visitor.visitInterface_declared(self)
            else:
                return visitor.visitChildren(self)




    def interface_declared(self):

        localctx = MiniGoParser.Interface_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_interface_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MiniGoParser.TYPE)
            self.state = 366
            self.match(MiniGoParser.ID)
            self.state = 367
            self.match(MiniGoParser.INTERFACE)
            self.state = 368
            self.match(MiniGoParser.LB)
            self.state = 369
            self.opt_newlines()
            self.state = 370
            self.interface_type_list()
            self.state = 371
            self.opt_newlines()
            self.state = 372
            self.match(MiniGoParser.RB)
            self.state = 373
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

        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def more_interface_methods(self):
            return self.getTypedRuleContext(MiniGoParser.More_interface_methodsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type_list" ):
                return visitor.visitInterface_type_list(self)
            else:
                return visitor.visitChildren(self)




    def interface_type_list(self):

        localctx = MiniGoParser.Interface_type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_interface_type_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.interface_method()
            self.state = 376
            self.more_interface_methods()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_interface_methodsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def more_interface_methods(self):
            return self.getTypedRuleContext(MiniGoParser.More_interface_methodsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_interface_methods

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore_interface_methods" ):
                return visitor.visitMore_interface_methods(self)
            else:
                return visitor.visitChildren(self)




    def more_interface_methods(self):

        localctx = MiniGoParser.More_interface_methodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_more_interface_methods)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RB, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.interface_method()
                self.state = 380
                self.more_interface_methods()
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
        self.enterRule(localctx, 60, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MiniGoParser.ID)
            self.state = 385
            self.match(MiniGoParser.LP)
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 386
                self.params_list()


            self.state = 389
            self.match(MiniGoParser.RP)
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 390
                self.type_name()


            self.state = 393
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
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.variables_declared()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
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

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

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
            self.state = 399
            self.assign_lhs()
            self.state = 400
            self.assign_op()
            self.state = 401
            self.expression(0)
            self.state = 402
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
            self.state = 404
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

        def more_access(self):
            return self.getTypedRuleContext(MiniGoParser.More_accessContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(MiniGoParser.ID)
            self.state = 407
            self.more_access()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def more_access(self):
            return self.getTypedRuleContext(MiniGoParser.More_accessContext,0)


        def field_access(self):
            return self.getTypedRuleContext(MiniGoParser.Field_accessContext,0)


        def element_access(self):
            return self.getTypedRuleContext(MiniGoParser.Element_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore_access" ):
                return visitor.visitMore_access(self)
            else:
                return visitor.visitChildren(self)




    def more_access(self):

        localctx = MiniGoParser.More_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_more_access)
        try:
            self.state = 416
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ASSIGN, MiniGoParser.ADD_ASSIGN, MiniGoParser.SUB_ASSIGN, MiniGoParser.MUL_ASSIGN, MiniGoParser.DIV_ASSIGN, MiniGoParser.MOD_ASSIGN, MiniGoParser.SHORT_ASSIGN, MiniGoParser.LP]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.DOT, MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.DOT]:
                    self.state = 410
                    self.field_access()
                    pass
                elif token in [MiniGoParser.LSB]:
                    self.state = 411
                    self.element_access()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 414
                self.more_access()
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
        self.enterRule(localctx, 72, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(MiniGoParser.IF)
            self.state = 419
            self.match(MiniGoParser.LP)
            self.state = 420
            self.expression(0)
            self.state = 421
            self.match(MiniGoParser.RP)
            self.state = 422
            self.block_stmt()
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 423
                self.match(MiniGoParser.ELSE)
                self.state = 424
                self.if_statement()

            elif la_ == 2:
                self.state = 425
                self.match(MiniGoParser.ELSE)
                self.state = 426
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

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(MiniGoParser.FOR)
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 430
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 431
                self.match(MiniGoParser.COMMA)
                self.state = 432
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 433
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 434
                self.match(MiniGoParser.RANGE)
                self.state = 435
                self.expression(0)
                self.state = 436
                self.block_stmt()
                pass

            elif la_ == 2:
                self.state = 438
                self.for_init()
                self.state = 439
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NEWLINE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 440
                self.expression(0)
                self.state = 441
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NEWLINE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 442
                self.for_update()
                self.state = 443
                self.block_stmt()
                pass

            elif la_ == 3:
                self.state = 445
                self.expression(0)
                self.state = 446
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

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
        self.enterRule(localctx, 76, self.RULE_for_init)
        self._la = 0 # Token type
        try:
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.match(MiniGoParser.ID)
                self.state = 451
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 452
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.match(MiniGoParser.ID)
                self.state = 454
                self.assign_op()
                self.state = 455
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 457
                self.match(MiniGoParser.VAR)
                self.state = 458
                self.match(MiniGoParser.ID)
                self.state = 460
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 459
                    self.type_name()


                self.state = 462
                self.match(MiniGoParser.ASSIGN)
                self.state = 463
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

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
        self.enterRule(localctx, 78, self.RULE_for_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(MiniGoParser.ID)
            self.state = 467
            self.assign_op()
            self.state = 468
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
        self.enterRule(localctx, 80, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(MiniGoParser.BREAK)
            self.state = 471
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
        self.enterRule(localctx, 82, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(MiniGoParser.CONTINUE)
            self.state = 474
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
        self.enterRule(localctx, 84, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(MiniGoParser.RETURN)
            self.state = 485
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 478
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 477
                    self.expression(0)


                self.state = 480
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 481
                    self.expression(0)


                self.state = 484
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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assign_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_lhsContext,0)


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
        self.enterRule(localctx, 86, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 487
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 488
                self.assign_lhs()
                pass


            self.state = 491
            self.match(MiniGoParser.LP)
            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 492
                self.list_expression()


            self.state = 495
            self.match(MiniGoParser.RP)
            self.state = 496
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


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def block_content(self):
            return self.getTypedRuleContext(MiniGoParser.Block_contentContext,0)


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
            return MiniGoParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = MiniGoParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(MiniGoParser.LB)
            self.state = 500
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 499
                self.match(MiniGoParser.NEWLINE)


            self.state = 502
            self.block_content()
            self.state = 504
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 503
                self.match(MiniGoParser.NEWLINE)


            self.state = 506
            self.match(MiniGoParser.RB)
            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 507
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def block_content(self):
            return self.getTypedRuleContext(MiniGoParser.Block_contentContext,0)


        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_content" ):
                return visitor.visitBlock_content(self)
            else:
                return visitor.visitChildren(self)




    def block_content(self):

        localctx = MiniGoParser.Block_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_block_content)
        try:
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
                self.statement()
                self.state = 512
                self.block_content()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 514
                self.match(MiniGoParser.NEWLINE)
                self.state = 515
                self.block_content()
                pass


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
            self.state = 523
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 519
                self.expression(0)
                self.state = 520
                self.match(MiniGoParser.COMMA)
                self.state = 521
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
            self.state = 526
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 533
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 528
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 529
                    self.match(MiniGoParser.OR)
                    self.state = 530
                    self.expression1(0) 
                self.state = 535
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
            self.state = 537
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 544
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 539
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 540
                    self.match(MiniGoParser.AND)
                    self.state = 541
                    self.expression2(0) 
                self.state = 546
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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
            self.state = 548
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 555
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 550
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 551
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.EQUAL or _la==MiniGoParser.NOT_EQUAL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 552
                    self.expression3(0) 
                self.state = 557
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
            self.state = 559
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 566
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 561
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 562
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESS_OR_EQUAL) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 563
                    self.expression4(0) 
                self.state = 568
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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
            self.state = 570
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 577
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 572
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 573
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 574
                    self.expression5(0) 
                self.state = 579
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

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
            self.state = 581
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 588
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 583
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 584
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 585
                    self.expression6() 
                self.state = 590
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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
            self.state = 596
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 591
                self.match(MiniGoParser.NOT)
                self.state = 592
                self.expression6()
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 593
                self.match(MiniGoParser.SUB)
                self.state = 594
                self.expression6()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.ID, MiniGoParser.FLOAT_LIT, MiniGoParser.INT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 595
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


        def more_access_expr(self):
            return self.getTypedRuleContext(MiniGoParser.More_access_exprContext,0)


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
            self.state = 598
            self.operand()
            self.state = 599
            self.more_access_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_access_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def more_access_expr(self):
            return self.getTypedRuleContext(MiniGoParser.More_access_exprContext,0)


        def element_access(self):
            return self.getTypedRuleContext(MiniGoParser.Element_accessContext,0)


        def field_access(self):
            return self.getTypedRuleContext(MiniGoParser.Field_accessContext,0)


        def call_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Call_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_more_access_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore_access_expr" ):
                return visitor.visitMore_access_expr(self)
            else:
                return visitor.visitChildren(self)




    def more_access_expr(self):

        localctx = MiniGoParser.More_access_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_more_access_expr)
        try:
            self.state = 609
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 605
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.LSB]:
                    self.state = 602
                    self.element_access()
                    pass
                elif token in [MiniGoParser.DOT]:
                    self.state = 603
                    self.field_access()
                    pass
                elif token in [MiniGoParser.LP]:
                    self.state = 604
                    self.call_expr()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 607
                self.more_access_expr()
                pass


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
        self.enterRule(localctx, 112, self.RULE_operand)
        try:
            self.state = 617
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 611
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 612
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 613
                self.match(MiniGoParser.LP)
                self.state = 614
                self.expression(0)
                self.state = 615
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
        self.enterRule(localctx, 114, self.RULE_element_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self.match(MiniGoParser.LSB)
            self.state = 620
            self.expression(0)
            self.state = 621
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
        self.enterRule(localctx, 116, self.RULE_field_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.match(MiniGoParser.DOT)
            self.state = 624
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
        self.enterRule(localctx, 118, self.RULE_call_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
            self.match(MiniGoParser.LP)
            self.state = 628
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 627
                self.list_expression()


            self.state = 630
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
        self.enterRule(localctx, 120, self.RULE_literal)
        try:
            self.state = 640
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 632
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 633
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 634
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 635
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 636
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 637
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 638
                self.typed_array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 639
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
        self.enterRule(localctx, 122, self.RULE_typed_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 642
            self.array_type()
            self.state = 643
            self.match(MiniGoParser.LB)
            self.state = 644
            self.literal_list()
            self.state = 645
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
        self.enterRule(localctx, 124, self.RULE_untyped_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.match(MiniGoParser.LB)
            self.state = 648
            self.literal_list()
            self.state = 649
            self.match(MiniGoParser.RB)
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

        def literal_item(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_itemContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def literal_list(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_listContext,0)


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
        try:
            self.state = 656
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 651
                self.literal_item()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 652
                self.literal_item()
                self.state = 653
                self.match(MiniGoParser.COMMA)
                self.state = 654
                self.literal_list()
                pass


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
            self.state = 667
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 658
                self.untyped_array_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 659
                self.struct_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 660
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 661
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 662
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 663
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 664
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 665
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 666
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

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def more_dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.More_dimensionsContext,0)


        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 669
            self.match(MiniGoParser.LSB)
            self.state = 670
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 671
            self.match(MiniGoParser.RSB)
            self.state = 672
            self.more_dimensions()
            self.state = 673
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_dimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def more_dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.More_dimensionsContext,0)


        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_more_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore_dimensions" ):
                return visitor.visitMore_dimensions(self)
            else:
                return visitor.visitChildren(self)




    def more_dimensions(self):

        localctx = MiniGoParser.More_dimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_more_dimensions)
        self._la = 0 # Token type
        try:
            self.state = 680
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 676
                self.match(MiniGoParser.LSB)
                self.state = 677
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 678
                self.match(MiniGoParser.RSB)
                self.state = 679
                self.more_dimensions()
                pass


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
        self.enterRule(localctx, 134, self.RULE_type_name)
        try:
            self.state = 688
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 682
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 683
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 684
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 685
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 686
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 687
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

        def optional_field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_field_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 690
            self.match(MiniGoParser.ID)
            self.state = 691
            self.match(MiniGoParser.LB)
            self.state = 692
            self.optional_field_list()
            self.state = 693
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_field_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_field_list" ):
                return visitor.visitOptional_field_list(self)
            else:
                return visitor.visitChildren(self)




    def optional_field_list(self):

        localctx = MiniGoParser.Optional_field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_optional_field_list)
        try:
            self.state = 697
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 696
                self.field_list()
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
        self.enterRule(localctx, 140, self.RULE_field_list)
        try:
            self.state = 704
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 699
                self.field_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 700
                self.field_init()
                self.state = 701
                self.match(MiniGoParser.COMMA)
                self.state = 702
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
        self.enterRule(localctx, 142, self.RULE_field_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(MiniGoParser.ID)
            self.state = 707
            self.match(MiniGoParser.COLON)
            self.state = 708
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
        self.enterRule(localctx, 144, self.RULE_list_expression)
        try:
            self.state = 715
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 710
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 711
                self.expression(0)
                self.state = 712
                self.match(MiniGoParser.COMMA)
                self.state = 713
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
         





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
        buf.write("\u02b8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\3\3\3")
        buf.write("\3\3\5\3\u0088\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u008f\n\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\5\u0097\n\5\3\5\7\5\u009a\n\5")
        buf.write("\f\5\16\5\u009d\13\5\3\6\3\6\3\6\3\6\3\6\5\6\u00a4\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00ae\n\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t\u00b9\n\t\3\n\3\n\5\n")
        buf.write("\u00bd\n\n\3\n\3\n\5\n\u00c1\n\n\3\n\3\n\3\n\7\n\u00c6")
        buf.write("\n\n\f\n\16\n\u00c9\13\n\3\n\5\n\u00cc\n\n\3\n\3\n\5\n")
        buf.write("\u00d0\n\n\5\n\u00d2\n\n\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\5\f\u00dd\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00e7\n\16\3\16\3\16\3\16\3\16\3\16\7\16\u00ee")
        buf.write("\n\16\f\16\16\16\u00f1\13\16\3\16\3\16\3\16\5\16\u00f6")
        buf.write("\n\16\3\16\5\16\u00f9\n\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0107\n\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\7\20\u010e\n\20\f\20\16\20\u0111")
        buf.write("\13\20\3\20\3\20\3\20\5\20\u0116\n\20\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u011f\n\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u0129\n\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\7\24\u0131\n\24\f\24\16\24\u0134\13\24\5")
        buf.write("\24\u0136\n\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\7\25")
        buf.write("\u013f\n\25\f\25\16\25\u0142\13\25\3\25\3\25\7\25\u0146")
        buf.write("\n\25\f\25\16\25\u0149\13\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u0152\n\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\30\3\30\3\30\3\30\5\30\u015d\n\30\3\31\3\31\5\31\u0161")
        buf.write("\n\31\3\31\5\31\u0164\n\31\3\32\3\32\3\32\3\32\3\32\7")
        buf.write("\32\u016b\n\32\f\32\16\32\u016e\13\32\3\32\3\32\3\32\5")
        buf.write("\32\u0173\n\32\3\33\3\33\3\33\3\33\5\33\u0179\n\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\5\35\u0185")
        buf.write("\n\35\3\36\3\36\5\36\u0189\n\36\3\37\3\37\5\37\u018d\n")
        buf.write("\37\3 \3 \5 \u0191\n \3!\3!\3!\3!\5!\u0197\n!\3\"\3\"")
        buf.write("\3#\3#\3#\7#\u019e\n#\f#\16#\u01a1\13#\3$\3$\3$\3$\3$")
        buf.write("\5$\u01a8\n$\3$\3$\5$\u01ac\n$\3$\3$\3$\3$\5$\u01b2\n")
        buf.write("$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\5%\u01c7\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01d3")
        buf.write("\n&\3&\3&\5&\u01d7\n&\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\5*\u01e5\n*\3*\3*\5*\u01e9\n*\3*\5*\u01ec\n*\3")
        buf.write("+\3+\5+\u01f0\n+\3+\3+\5+\u01f4\n+\3+\3+\5+\u01f8\n+\3")
        buf.write(",\5,\u01fb\n,\3,\3,\5,\u01ff\n,\3,\3,\7,\u0203\n,\f,\16")
        buf.write(",\u0206\13,\3,\5,\u0209\n,\3,\3,\3-\3-\3-\3-\3-\5-\u0212")
        buf.write("\n-\3.\3.\3.\3.\3.\3.\7.\u021a\n.\f.\16.\u021d\13.\3/")
        buf.write("\3/\3/\3/\3/\3/\7/\u0225\n/\f/\16/\u0228\13/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\7\60\u0230\n\60\f\60\16\60\u0233")
        buf.write("\13\60\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u023b\n\61\f")
        buf.write("\61\16\61\u023e\13\61\3\62\3\62\3\62\3\62\3\62\3\62\7")
        buf.write("\62\u0246\n\62\f\62\16\62\u0249\13\62\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\7\63\u0251\n\63\f\63\16\63\u0254\13\63\3")
        buf.write("\64\3\64\3\64\3\64\3\64\5\64\u025b\n\64\3\65\3\65\3\65")
        buf.write("\3\65\7\65\u0261\n\65\f\65\16\65\u0264\13\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\5\66\u026c\n\66\3\67\3\67\3\67\3")
        buf.write("\67\38\38\38\39\39\59\u0277\n9\39\39\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\5:\u0283\n:\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\7")
        buf.write("<\u0290\n<\f<\16<\u0293\13<\3<\3<\3=\3=\3=\3=\3=\3=\5")
        buf.write("=\u029d\n=\3>\3>\3>\5>\u02a2\n>\3>\3>\3?\3?\3?\3?\3?\5")
        buf.write("?\u02ab\n?\3@\3@\3@\3@\3A\3A\3A\3A\3A\5A\u02b6\nA\3A\2")
        buf.write("\bZ\\^`bdB\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|")
        buf.write("~\u0080\2\n\4\2\66\66<<\4\2\t\n\67\67\4\2%*--\4\2..\67")
        buf.write("\67\3\2\34\35\3\2\36!\3\2\27\30\3\2\31\33\2\u02df\2\u0082")
        buf.write("\3\2\2\2\4\u0087\3\2\2\2\6\u008e\3\2\2\2\b\u0096\3\2\2")
        buf.write("\2\n\u00a3\3\2\2\2\f\u00ad\3\2\2\2\16\u00af\3\2\2\2\20")
        buf.write("\u00b8\3\2\2\2\22\u00d1\3\2\2\2\24\u00d3\3\2\2\2\26\u00dc")
        buf.write("\3\2\2\2\30\u00de\3\2\2\2\32\u00e2\3\2\2\2\34\u00fc\3")
        buf.write("\2\2\2\36\u00ff\3\2\2\2 \u011e\3\2\2\2\"\u0120\3\2\2\2")
        buf.write("$\u0128\3\2\2\2&\u0135\3\2\2\2(\u0139\3\2\2\2*\u0151\3")
        buf.write("\2\2\2,\u0153\3\2\2\2.\u015c\3\2\2\2\60\u0163\3\2\2\2")
        buf.write("\62\u0165\3\2\2\2\64\u0178\3\2\2\2\66\u017a\3\2\2\28\u0184")
        buf.write("\3\2\2\2:\u0188\3\2\2\2<\u018c\3\2\2\2>\u0190\3\2\2\2")
        buf.write("@\u0192\3\2\2\2B\u0198\3\2\2\2D\u019a\3\2\2\2F\u01a2\3")
        buf.write("\2\2\2H\u01b3\3\2\2\2J\u01d6\3\2\2\2L\u01d8\3\2\2\2N\u01dc")
        buf.write("\3\2\2\2P\u01df\3\2\2\2R\u01e2\3\2\2\2T\u01ef\3\2\2\2")
        buf.write("V\u01fa\3\2\2\2X\u0211\3\2\2\2Z\u0213\3\2\2\2\\\u021e")
        buf.write("\3\2\2\2^\u0229\3\2\2\2`\u0234\3\2\2\2b\u023f\3\2\2\2")
        buf.write("d\u024a\3\2\2\2f\u025a\3\2\2\2h\u025c\3\2\2\2j\u026b\3")
        buf.write("\2\2\2l\u026d\3\2\2\2n\u0271\3\2\2\2p\u0274\3\2\2\2r\u0282")
        buf.write("\3\2\2\2t\u0284\3\2\2\2v\u0289\3\2\2\2x\u029c\3\2\2\2")
        buf.write("z\u029e\3\2\2\2|\u02aa\3\2\2\2~\u02ac\3\2\2\2\u0080\u02b5")
        buf.write("\3\2\2\2\u0082\u0083\5\u0080A\2\u0083\3\3\2\2\2\u0084")
        buf.write("\u0088\3\2\2\2\u0085\u0086\7<\2\2\u0086\u0088\5\4\3\2")
        buf.write("\u0087\u0084\3\2\2\2\u0087\u0085\3\2\2\2\u0088\5\3\2\2")
        buf.write("\2\u0089\u008f\3\2\2\2\u008a\u008b\5\4\3\2\u008b\u008c")
        buf.write("\5\b\5\2\u008c\u008d\5\6\4\2\u008d\u008f\3\2\2\2\u008e")
        buf.write("\u0089\3\2\2\2\u008e\u008a\3\2\2\2\u008f\7\3\2\2\2\u0090")
        buf.write("\u0097\5\16\b\2\u0091\u0097\5\24\13\2\u0092\u0097\5\32")
        buf.write("\16\2\u0093\u0097\5\36\20\2\u0094\u0097\5(\25\2\u0095")
        buf.write("\u0097\5\62\32\2\u0096\u0090\3\2\2\2\u0096\u0091\3\2\2")
        buf.write("\2\u0096\u0092\3\2\2\2\u0096\u0093\3\2\2\2\u0096\u0094")
        buf.write("\3\2\2\2\u0096\u0095\3\2\2\2\u0097\u009b\3\2\2\2\u0098")
        buf.write("\u009a\7<\2\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2")
        buf.write("\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\t\3\2\2")
        buf.write("\2\u009d\u009b\3\2\2\2\u009e\u00a4\5\f\7\2\u009f\u00a0")
        buf.write("\5\f\7\2\u00a0\u00a1\5\4\3\2\u00a1\u00a2\5\n\6\2\u00a2")
        buf.write("\u00a4\3\2\2\2\u00a3\u009e\3\2\2\2\u00a3\u009f\3\2\2\2")
        buf.write("\u00a4\13\3\2\2\2\u00a5\u00ae\5> \2\u00a6\u00ae\5@!\2")
        buf.write("\u00a7\u00ae\5F$\2\u00a8\u00ae\5H%\2\u00a9\u00ae\5N(\2")
        buf.write("\u00aa\u00ae\5P)\2\u00ab\u00ae\5T+\2\u00ac\u00ae\5R*\2")
        buf.write("\u00ad\u00a5\3\2\2\2\u00ad\u00a6\3\2\2\2\u00ad\u00a7\3")
        buf.write("\2\2\2\u00ad\u00a8\3\2\2\2\u00ad\u00a9\3\2\2\2\u00ad\u00aa")
        buf.write("\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae")
        buf.write("\r\3\2\2\2\u00af\u00b0\7\20\2\2\u00b0\u00b1\5\20\t\2\u00b1")
        buf.write("\u00b2\7\66\2\2\u00b2\17\3\2\2\2\u00b3\u00b9\5\22\n\2")
        buf.write("\u00b4\u00b5\5\22\n\2\u00b5\u00b6\7\65\2\2\u00b6\u00b7")
        buf.write("\5\20\t\2\u00b7\u00b9\3\2\2\2\u00b8\u00b3\3\2\2\2\u00b8")
        buf.write("\u00b4\3\2\2\2\u00b9\21\3\2\2\2\u00ba\u00bc\7\67\2\2\u00bb")
        buf.write("\u00bd\5x=\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00bf\7%\2\2\u00bf\u00c1\5Z.\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00d2\3\2\2\2")
        buf.write("\u00c2\u00c7\7\67\2\2\u00c3\u00c4\7\65\2\2\u00c4\u00c6")
        buf.write("\7\67\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00cb\3\2\2\2")
        buf.write("\u00c9\u00c7\3\2\2\2\u00ca\u00cc\5x=\2\u00cb\u00ca\3\2")
        buf.write("\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00ce")
        buf.write("\7%\2\2\u00ce\u00d0\5X-\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00ba\3\2\2\2\u00d1")
        buf.write("\u00c2\3\2\2\2\u00d2\23\3\2\2\2\u00d3\u00d4\7\17\2\2\u00d4")
        buf.write("\u00d5\5\26\f\2\u00d5\u00d6\t\2\2\2\u00d6\25\3\2\2\2\u00d7")
        buf.write("\u00dd\5\30\r\2\u00d8\u00d9\5\30\r\2\u00d9\u00da\7\65")
        buf.write("\2\2\u00da\u00db\5\26\f\2\u00db\u00dd\3\2\2\2\u00dc\u00d7")
        buf.write("\3\2\2\2\u00dc\u00d8\3\2\2\2\u00dd\27\3\2\2\2\u00de\u00df")
        buf.write("\7\67\2\2\u00df\u00e0\7%\2\2\u00e0\u00e1\5Z.\2\u00e1\31")
        buf.write("\3\2\2\2\u00e2\u00e3\7\7\2\2\u00e3\u00e4\7\67\2\2\u00e4")
        buf.write("\u00e6\7/\2\2\u00e5\u00e7\5$\23\2\u00e6\u00e5\3\2\2\2")
        buf.write("\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00f5\7")
        buf.write("\60\2\2\u00e9\u00ea\7/\2\2\u00ea\u00ef\5x=\2\u00eb\u00ec")
        buf.write("\7\65\2\2\u00ec\u00ee\5x=\2\u00ed\u00eb\3\2\2\2\u00ee")
        buf.write("\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write("\u00f0\u00f2\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\7")
        buf.write("\60\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f6\5x=\2\u00f5\u00e9")
        buf.write("\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6")
        buf.write("\u00f8\3\2\2\2\u00f7\u00f9\7<\2\2\u00f8\u00f7\3\2\2\2")
        buf.write("\u00f8\u00f9\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\5")
        buf.write("V,\2\u00fb\33\3\2\2\2\u00fc\u00fd\7\67\2\2\u00fd\u00fe")
        buf.write("\t\3\2\2\u00fe\35\3\2\2\2\u00ff\u0100\7\7\2\2\u0100\u0101")
        buf.write("\7/\2\2\u0101\u0102\5\34\17\2\u0102\u0103\7\60\2\2\u0103")
        buf.write("\u0104\7\67\2\2\u0104\u0106\7/\2\2\u0105\u0107\5 \21\2")
        buf.write("\u0106\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\3")
        buf.write("\2\2\2\u0108\u0115\7\60\2\2\u0109\u010a\7/\2\2\u010a\u010f")
        buf.write("\5x=\2\u010b\u010c\7\65\2\2\u010c\u010e\5x=\2\u010d\u010b")
        buf.write("\3\2\2\2\u010e\u0111\3\2\2\2\u010f\u010d\3\2\2\2\u010f")
        buf.write("\u0110\3\2\2\2\u0110\u0112\3\2\2\2\u0111\u010f\3\2\2\2")
        buf.write("\u0112\u0113\7\60\2\2\u0113\u0116\3\2\2\2\u0114\u0116")
        buf.write("\5x=\2\u0115\u0109\3\2\2\2\u0115\u0114\3\2\2\2\u0115\u0116")
        buf.write("\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\5V,\2\u0118\37")
        buf.write("\3\2\2\2\u0119\u011f\5\"\22\2\u011a\u011b\5\"\22\2\u011b")
        buf.write("\u011c\7\65\2\2\u011c\u011d\5 \21\2\u011d\u011f\3\2\2")
        buf.write("\2\u011e\u0119\3\2\2\2\u011e\u011a\3\2\2\2\u011f!\3\2")
        buf.write("\2\2\u0120\u0121\7\67\2\2\u0121\u0122\5x=\2\u0122#\3\2")
        buf.write("\2\2\u0123\u0129\5&\24\2\u0124\u0125\5&\24\2\u0125\u0126")
        buf.write("\7\65\2\2\u0126\u0127\5$\23\2\u0127\u0129\3\2\2\2\u0128")
        buf.write("\u0123\3\2\2\2\u0128\u0124\3\2\2\2\u0129%\3\2\2\2\u012a")
        buf.write("\u0136\7\67\2\2\u012b\u012c\7\67\2\2\u012c\u012d\7\65")
        buf.write("\2\2\u012d\u0132\7\67\2\2\u012e\u012f\7\65\2\2\u012f\u0131")
        buf.write("\7\67\2\2\u0130\u012e\3\2\2\2\u0131\u0134\3\2\2\2\u0132")
        buf.write("\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0136\3\2\2\2")
        buf.write("\u0134\u0132\3\2\2\2\u0135\u012a\3\2\2\2\u0135\u012b\3")
        buf.write("\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\5x=\2\u0138\'\3")
        buf.write("\2\2\2\u0139\u013a\7\b\2\2\u013a\u013b\7\67\2\2\u013b")
        buf.write("\u013c\7\t\2\2\u013c\u0140\7\61\2\2\u013d\u013f\7<\2\2")
        buf.write("\u013e\u013d\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u013e\3")
        buf.write("\2\2\2\u0140\u0141\3\2\2\2\u0141\u0143\3\2\2\2\u0142\u0140")
        buf.write("\3\2\2\2\u0143\u0147\5*\26\2\u0144\u0146\7<\2\2\u0145")
        buf.write("\u0144\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145\3\2\2\2")
        buf.write("\u0147\u0148\3\2\2\2\u0148\u014a\3\2\2\2\u0149\u0147\3")
        buf.write("\2\2\2\u014a\u014b\7\62\2\2\u014b\u014c\t\2\2\2\u014c")
        buf.write(")\3\2\2\2\u014d\u0152\3\2\2\2\u014e\u014f\5,\27\2\u014f")
        buf.write("\u0150\5*\26\2\u0150\u0152\3\2\2\2\u0151\u014d\3\2\2\2")
        buf.write("\u0151\u014e\3\2\2\2\u0152+\3\2\2\2\u0153\u0154\7\67\2")
        buf.write("\2\u0154\u0155\5.\30\2\u0155\u0156\5x=\2\u0156\u0157\5")
        buf.write("\60\31\2\u0157-\3\2\2\2\u0158\u015d\3\2\2\2\u0159\u015a")
        buf.write("\7\65\2\2\u015a\u015b\7\67\2\2\u015b\u015d\5.\30\2\u015c")
        buf.write("\u0158\3\2\2\2\u015c\u0159\3\2\2\2\u015d/\3\2\2\2\u015e")
        buf.write("\u0164\7\66\2\2\u015f\u0161\7\66\2\2\u0160\u015f\3\2\2")
        buf.write("\2\u0160\u0161\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0164")
        buf.write("\7<\2\2\u0163\u015e\3\2\2\2\u0163\u0160\3\2\2\2\u0164")
        buf.write("\61\3\2\2\2\u0165\u0166\7\b\2\2\u0166\u0167\7\67\2\2\u0167")
        buf.write("\u0168\7\n\2\2\u0168\u016c\7\61\2\2\u0169\u016b\7<\2\2")
        buf.write("\u016a\u0169\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3")
        buf.write("\2\2\2\u016c\u016d\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u016c")
        buf.write("\3\2\2\2\u016f\u0170\5\64\33\2\u0170\u0172\7\62\2\2\u0171")
        buf.write("\u0173\7\66\2\2\u0172\u0171\3\2\2\2\u0172\u0173\3\2\2")
        buf.write("\2\u0173\63\3\2\2\2\u0174\u0179\3\2\2\2\u0175\u0176\5")
        buf.write("\66\34\2\u0176\u0177\5\64\33\2\u0177\u0179\3\2\2\2\u0178")
        buf.write("\u0174\3\2\2\2\u0178\u0175\3\2\2\2\u0179\65\3\2\2\2\u017a")
        buf.write("\u017b\7\67\2\2\u017b\u017c\7/\2\2\u017c\u017d\58\35\2")
        buf.write("\u017d\u017e\7\60\2\2\u017e\u017f\5:\36\2\u017f\u0180")
        buf.write("\5<\37\2\u0180\u0181\5\4\3\2\u0181\67\3\2\2\2\u0182\u0185")
        buf.write("\3\2\2\2\u0183\u0185\5$\23\2\u0184\u0182\3\2\2\2\u0184")
        buf.write("\u0183\3\2\2\2\u01859\3\2\2\2\u0186\u0189\3\2\2\2\u0187")
        buf.write("\u0189\5x=\2\u0188\u0186\3\2\2\2\u0188\u0187\3\2\2\2\u0189")
        buf.write(";\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u018d\7\66\2\2\u018c")
        buf.write("\u018a\3\2\2\2\u018c\u018b\3\2\2\2\u018d=\3\2\2\2\u018e")
        buf.write("\u0191\5\16\b\2\u018f\u0191\5\24\13\2\u0190\u018e\3\2")
        buf.write("\2\2\u0190\u018f\3\2\2\2\u0191?\3\2\2\2\u0192\u0193\5")
        buf.write("D#\2\u0193\u0194\5B\"\2\u0194\u0196\5Z.\2\u0195\u0197")
        buf.write("\7\66\2\2\u0196\u0195\3\2\2\2\u0196\u0197\3\2\2\2\u0197")
        buf.write("A\3\2\2\2\u0198\u0199\t\4\2\2\u0199C\3\2\2\2\u019a\u019f")
        buf.write("\7\67\2\2\u019b\u019e\5n8\2\u019c\u019e\5l\67\2\u019d")
        buf.write("\u019b\3\2\2\2\u019d\u019c\3\2\2\2\u019e\u01a1\3\2\2\2")
        buf.write("\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0E\3\2\2")
        buf.write("\2\u01a1\u019f\3\2\2\2\u01a2\u01a3\7\3\2\2\u01a3\u01a4")
        buf.write("\7/\2\2\u01a4\u01a5\5Z.\2\u01a5\u01a7\7\60\2\2\u01a6\u01a8")
        buf.write("\7<\2\2\u01a7\u01a6\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write("\u01a9\3\2\2\2\u01a9\u01ab\5V,\2\u01aa\u01ac\7<\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01b1\3\2\2\2")
        buf.write("\u01ad\u01ae\7\4\2\2\u01ae\u01b2\5F$\2\u01af\u01b0\7\4")
        buf.write("\2\2\u01b0\u01b2\5V,\2\u01b1\u01ad\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2G\3\2\2\2\u01b3\u01c6")
        buf.write("\7\5\2\2\u01b4\u01b5\t\5\2\2\u01b5\u01b6\7\65\2\2\u01b6")
        buf.write("\u01b7\t\5\2\2\u01b7\u01b8\7-\2\2\u01b8\u01b9\7\23\2\2")
        buf.write("\u01b9\u01ba\5Z.\2\u01ba\u01bb\5V,\2\u01bb\u01c7\3\2\2")
        buf.write("\2\u01bc\u01bd\5J&\2\u01bd\u01be\7\66\2\2\u01be\u01bf")
        buf.write("\5Z.\2\u01bf\u01c0\7\66\2\2\u01c0\u01c1\5L\'\2\u01c1\u01c2")
        buf.write("\5V,\2\u01c2\u01c7\3\2\2\2\u01c3\u01c4\5Z.\2\u01c4\u01c5")
        buf.write("\5V,\2\u01c5\u01c7\3\2\2\2\u01c6\u01b4\3\2\2\2\u01c6\u01bc")
        buf.write("\3\2\2\2\u01c6\u01c3\3\2\2\2\u01c7I\3\2\2\2\u01c8\u01c9")
        buf.write("\7\67\2\2\u01c9\u01ca\7-\2\2\u01ca\u01d7\5Z.\2\u01cb\u01cc")
        buf.write("\7\67\2\2\u01cc\u01cd\5B\"\2\u01cd\u01ce\5Z.\2\u01ce\u01d7")
        buf.write("\3\2\2\2\u01cf\u01d0\7\20\2\2\u01d0\u01d2\7\67\2\2\u01d1")
        buf.write("\u01d3\5x=\2\u01d2\u01d1\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3")
        buf.write("\u01d4\3\2\2\2\u01d4\u01d5\7%\2\2\u01d5\u01d7\5Z.\2\u01d6")
        buf.write("\u01c8\3\2\2\2\u01d6\u01cb\3\2\2\2\u01d6\u01cf\3\2\2\2")
        buf.write("\u01d7K\3\2\2\2\u01d8\u01d9\5D#\2\u01d9\u01da\5B\"\2\u01da")
        buf.write("\u01db\5Z.\2\u01dbM\3\2\2\2\u01dc\u01dd\7\22\2\2\u01dd")
        buf.write("\u01de\t\2\2\2\u01deO\3\2\2\2\u01df\u01e0\7\21\2\2\u01e0")
        buf.write("\u01e1\t\2\2\2\u01e1Q\3\2\2\2\u01e2\u01eb\7\6\2\2\u01e3")
        buf.write("\u01e5\5Z.\2\u01e4\u01e3\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5")
        buf.write("\u01e6\3\2\2\2\u01e6\u01ec\7\66\2\2\u01e7\u01e9\5Z.\2")
        buf.write("\u01e8\u01e7\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ea\3")
        buf.write("\2\2\2\u01ea\u01ec\7<\2\2\u01eb\u01e4\3\2\2\2\u01eb\u01e8")
        buf.write("\3\2\2\2\u01ecS\3\2\2\2\u01ed\u01f0\7\67\2\2\u01ee\u01f0")
        buf.write("\5D#\2\u01ef\u01ed\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0\u01f1")
        buf.write("\3\2\2\2\u01f1\u01f3\7/\2\2\u01f2\u01f4\5\u0080A\2\u01f3")
        buf.write("\u01f2\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f5\3\2\2\2")
        buf.write("\u01f5\u01f7\7\60\2\2\u01f6\u01f8\7\66\2\2\u01f7\u01f6")
        buf.write("\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8U\3\2\2\2\u01f9\u01fb")
        buf.write("\7<\2\2\u01fa\u01f9\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb")
        buf.write("\u01fc\3\2\2\2\u01fc\u01fe\7\61\2\2\u01fd\u01ff\7<\2\2")
        buf.write("\u01fe\u01fd\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0204\3")
        buf.write("\2\2\2\u0200\u0203\5\f\7\2\u0201\u0203\7<\2\2\u0202\u0200")
        buf.write("\3\2\2\2\u0202\u0201\3\2\2\2\u0203\u0206\3\2\2\2\u0204")
        buf.write("\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0208\3\2\2\2")
        buf.write("\u0206\u0204\3\2\2\2\u0207\u0209\7<\2\2\u0208\u0207\3")
        buf.write("\2\2\2\u0208\u0209\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020b")
        buf.write("\7\62\2\2\u020bW\3\2\2\2\u020c\u0212\5Z.\2\u020d\u020e")
        buf.write("\5Z.\2\u020e\u020f\7\65\2\2\u020f\u0210\5X-\2\u0210\u0212")
        buf.write("\3\2\2\2\u0211\u020c\3\2\2\2\u0211\u020d\3\2\2\2\u0212")
        buf.write("Y\3\2\2\2\u0213\u0214\b.\1\2\u0214\u0215\5\\/\2\u0215")
        buf.write("\u021b\3\2\2\2\u0216\u0217\f\4\2\2\u0217\u0218\7#\2\2")
        buf.write("\u0218\u021a\5\\/\2\u0219\u0216\3\2\2\2\u021a\u021d\3")
        buf.write("\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c[")
        buf.write("\3\2\2\2\u021d\u021b\3\2\2\2\u021e\u021f\b/\1\2\u021f")
        buf.write("\u0220\5^\60\2\u0220\u0226\3\2\2\2\u0221\u0222\f\4\2\2")
        buf.write("\u0222\u0223\7\"\2\2\u0223\u0225\5^\60\2\u0224\u0221\3")
        buf.write("\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2\2\u0226\u0227")
        buf.write("\3\2\2\2\u0227]\3\2\2\2\u0228\u0226\3\2\2\2\u0229\u022a")
        buf.write("\b\60\1\2\u022a\u022b\5`\61\2\u022b\u0231\3\2\2\2\u022c")
        buf.write("\u022d\f\4\2\2\u022d\u022e\t\6\2\2\u022e\u0230\5`\61\2")
        buf.write("\u022f\u022c\3\2\2\2\u0230\u0233\3\2\2\2\u0231\u022f\3")
        buf.write("\2\2\2\u0231\u0232\3\2\2\2\u0232_\3\2\2\2\u0233\u0231")
        buf.write("\3\2\2\2\u0234\u0235\b\61\1\2\u0235\u0236\5b\62\2\u0236")
        buf.write("\u023c\3\2\2\2\u0237\u0238\f\4\2\2\u0238\u0239\t\7\2\2")
        buf.write("\u0239\u023b\5b\62\2\u023a\u0237\3\2\2\2\u023b\u023e\3")
        buf.write("\2\2\2\u023c\u023a\3\2\2\2\u023c\u023d\3\2\2\2\u023da")
        buf.write("\3\2\2\2\u023e\u023c\3\2\2\2\u023f\u0240\b\62\1\2\u0240")
        buf.write("\u0241\5d\63\2\u0241\u0247\3\2\2\2\u0242\u0243\f\4\2\2")
        buf.write("\u0243\u0244\t\b\2\2\u0244\u0246\5d\63\2\u0245\u0242\3")
        buf.write("\2\2\2\u0246\u0249\3\2\2\2\u0247\u0245\3\2\2\2\u0247\u0248")
        buf.write("\3\2\2\2\u0248c\3\2\2\2\u0249\u0247\3\2\2\2\u024a\u024b")
        buf.write("\b\63\1\2\u024b\u024c\5f\64\2\u024c\u0252\3\2\2\2\u024d")
        buf.write("\u024e\f\4\2\2\u024e\u024f\t\t\2\2\u024f\u0251\5f\64\2")
        buf.write("\u0250\u024d\3\2\2\2\u0251\u0254\3\2\2\2\u0252\u0250\3")
        buf.write("\2\2\2\u0252\u0253\3\2\2\2\u0253e\3\2\2\2\u0254\u0252")
        buf.write("\3\2\2\2\u0255\u0256\7$\2\2\u0256\u025b\5f\64\2\u0257")
        buf.write("\u0258\7\30\2\2\u0258\u025b\5f\64\2\u0259\u025b\5h\65")
        buf.write("\2\u025a\u0255\3\2\2\2\u025a\u0257\3\2\2\2\u025a\u0259")
        buf.write("\3\2\2\2\u025bg\3\2\2\2\u025c\u0262\5j\66\2\u025d\u0261")
        buf.write("\5l\67\2\u025e\u0261\5n8\2\u025f\u0261\5p9\2\u0260\u025d")
        buf.write("\3\2\2\2\u0260\u025e\3\2\2\2\u0260\u025f\3\2\2\2\u0261")
        buf.write("\u0264\3\2\2\2\u0262\u0260\3\2\2\2\u0262\u0263\3\2\2\2")
        buf.write("\u0263i\3\2\2\2\u0264\u0262\3\2\2\2\u0265\u026c\5r:\2")
        buf.write("\u0266\u026c\7\67\2\2\u0267\u0268\7/\2\2\u0268\u0269\5")
        buf.write("Z.\2\u0269\u026a\7\60\2\2\u026a\u026c\3\2\2\2\u026b\u0265")
        buf.write("\3\2\2\2\u026b\u0266\3\2\2\2\u026b\u0267\3\2\2\2\u026c")
        buf.write("k\3\2\2\2\u026d\u026e\7\63\2\2\u026e\u026f\5Z.\2\u026f")
        buf.write("\u0270\7\64\2\2\u0270m\3\2\2\2\u0271\u0272\7+\2\2\u0272")
        buf.write("\u0273\7\67\2\2\u0273o\3\2\2\2\u0274\u0276\7/\2\2\u0275")
        buf.write("\u0277\5\u0080A\2\u0276\u0275\3\2\2\2\u0276\u0277\3\2")
        buf.write("\2\2\u0277\u0278\3\2\2\2\u0278\u0279\7\60\2\2\u0279q\3")
        buf.write("\2\2\2\u027a\u0283\78\2\2\u027b\u0283\79\2\2\u027c\u0283")
        buf.write("\7:\2\2\u027d\u0283\7\25\2\2\u027e\u0283\7\26\2\2\u027f")
        buf.write("\u0283\7\24\2\2\u0280\u0283\5t;\2\u0281\u0283\5z>\2\u0282")
        buf.write("\u027a\3\2\2\2\u0282\u027b\3\2\2\2\u0282\u027c\3\2\2\2")
        buf.write("\u0282\u027d\3\2\2\2\u0282\u027e\3\2\2\2\u0282\u027f\3")
        buf.write("\2\2\2\u0282\u0280\3\2\2\2\u0282\u0281\3\2\2\2\u0283s")
        buf.write("\3\2\2\2\u0284\u0285\5v<\2\u0285\u0286\7\61\2\2\u0286")
        buf.write("\u0287\5\u0080A\2\u0287\u0288\7\62\2\2\u0288u\3\2\2\2")
        buf.write("\u0289\u028a\7\63\2\2\u028a\u028b\78\2\2\u028b\u0291\7")
        buf.write("\64\2\2\u028c\u028d\7\63\2\2\u028d\u028e\78\2\2\u028e")
        buf.write("\u0290\7\64\2\2\u028f\u028c\3\2\2\2\u0290\u0293\3\2\2")
        buf.write("\2\u0291\u028f\3\2\2\2\u0291\u0292\3\2\2\2\u0292\u0294")
        buf.write("\3\2\2\2\u0293\u0291\3\2\2\2\u0294\u0295\5x=\2\u0295w")
        buf.write("\3\2\2\2\u0296\u029d\7\f\2\2\u0297\u029d\7\r\2\2\u0298")
        buf.write("\u029d\7\13\2\2\u0299\u029d\7\16\2\2\u029a\u029d\7\67")
        buf.write("\2\2\u029b\u029d\5v<\2\u029c\u0296\3\2\2\2\u029c\u0297")
        buf.write("\3\2\2\2\u029c\u0298\3\2\2\2\u029c\u0299\3\2\2\2\u029c")
        buf.write("\u029a\3\2\2\2\u029c\u029b\3\2\2\2\u029dy\3\2\2\2\u029e")
        buf.write("\u029f\7\67\2\2\u029f\u02a1\7\61\2\2\u02a0\u02a2\5|?\2")
        buf.write("\u02a1\u02a0\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2\u02a3\3")
        buf.write("\2\2\2\u02a3\u02a4\7\62\2\2\u02a4{\3\2\2\2\u02a5\u02ab")
        buf.write("\5~@\2\u02a6\u02a7\5~@\2\u02a7\u02a8\7\65\2\2\u02a8\u02a9")
        buf.write("\5|?\2\u02a9\u02ab\3\2\2\2\u02aa\u02a5\3\2\2\2\u02aa\u02a6")
        buf.write("\3\2\2\2\u02ab}\3\2\2\2\u02ac\u02ad\7\67\2\2\u02ad\u02ae")
        buf.write("\7,\2\2\u02ae\u02af\5Z.\2\u02af\177\3\2\2\2\u02b0\u02b6")
        buf.write("\5Z.\2\u02b1\u02b2\5Z.\2\u02b2\u02b3\7\65\2\2\u02b3\u02b4")
        buf.write("\5\u0080A\2\u02b4\u02b6\3\2\2\2\u02b5\u02b0\3\2\2\2\u02b5")
        buf.write("\u02b1\3\2\2\2\u02b6\u0081\3\2\2\2N\u0087\u008e\u0096")
        buf.write("\u009b\u00a3\u00ad\u00b8\u00bc\u00c0\u00c7\u00cb\u00cf")
        buf.write("\u00d1\u00dc\u00e6\u00ef\u00f5\u00f8\u0106\u010f\u0115")
        buf.write("\u011e\u0128\u0132\u0135\u0140\u0147\u0151\u015c\u0160")
        buf.write("\u0163\u016c\u0172\u0178\u0184\u0188\u018c\u0190\u0196")
        buf.write("\u019d\u019f\u01a7\u01ab\u01b1\u01c6\u01d2\u01d6\u01e4")
        buf.write("\u01e8\u01eb\u01ef\u01f3\u01f7\u01fa\u01fe\u0202\u0204")
        buf.write("\u0208\u0211\u021b\u0226\u0231\u023c\u0247\u0252\u025a")
        buf.write("\u0260\u0262\u026b\u0276\u0282\u0291\u029c\u02a1\u02aa")
        buf.write("\u02b5")
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
                      "WS", "NEWLINE", "BLOCK_COMMENT", "LINE_COMMENT", 
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
    RULE_struct_type = 20
    RULE_struct_field = 21
    RULE_more_ids = 22
    RULE_struct_end = 23
    RULE_interface_declared = 24
    RULE_interface_type = 25
    RULE_interface_method = 26
    RULE_optional_params = 27
    RULE_optional_type = 28
    RULE_optional_semi = 29
    RULE_declared_statement = 30
    RULE_assign_statement = 31
    RULE_assign_op = 32
    RULE_assign_lhs = 33
    RULE_if_statement = 34
    RULE_for_statement = 35
    RULE_for_init = 36
    RULE_for_update = 37
    RULE_break_statement = 38
    RULE_continue_statement = 39
    RULE_return_statement = 40
    RULE_call_statement = 41
    RULE_block_stmt = 42
    RULE_expr_list = 43
    RULE_expression = 44
    RULE_expression1 = 45
    RULE_expression2 = 46
    RULE_expression3 = 47
    RULE_expression4 = 48
    RULE_expression5 = 49
    RULE_expression6 = 50
    RULE_expression7 = 51
    RULE_operand = 52
    RULE_element_access = 53
    RULE_field_access = 54
    RULE_call_expr = 55
    RULE_literal = 56
    RULE_array_literal = 57
    RULE_array_type = 58
    RULE_type_name = 59
    RULE_struct_literal = 60
    RULE_field_list = 61
    RULE_field_init = 62
    RULE_list_expression = 63

    ruleNames =  [ "program", "newlines", "more_declared", "declared", "list_statement", 
                   "statement", "variables_declared", "var_decl_list", "var_decl", 
                   "constants_declared", "const_decl_list", "const_decl", 
                   "function_declared", "receiver", "method_declared", "method_params", 
                   "method_param", "params_list", "param", "struct_declared", 
                   "struct_type", "struct_field", "more_ids", "struct_end", 
                   "interface_declared", "interface_type", "interface_method", 
                   "optional_params", "optional_type", "optional_semi", 
                   "declared_statement", "assign_statement", "assign_op", 
                   "assign_lhs", "if_statement", "for_statement", "for_init", 
                   "for_update", "break_statement", "continue_statement", 
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
    WS=57
    NEWLINE=58
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

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


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
            self.state = 128
            self.list_expression()
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
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.RB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(MiniGoParser.NEWLINE)
                self.state = 132
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
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.newlines()
                self.state = 137
                self.declared()
                self.state = 138
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
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 142
                self.variables_declared()
                pass

            elif la_ == 2:
                self.state = 143
                self.constants_declared()
                pass

            elif la_ == 3:
                self.state = 144
                self.function_declared()
                pass

            elif la_ == 4:
                self.state = 145
                self.method_declared()
                pass

            elif la_ == 5:
                self.state = 146
                self.struct_declared()
                pass

            elif la_ == 6:
                self.state = 147
                self.interface_declared()
                pass


            self.state = 153
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 150
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 155
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
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.statement()
                self.state = 158
                self.newlines()
                self.state = 159
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
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.declared_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 168
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 169
                self.call_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 170
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
            self.state = 173
            self.match(MiniGoParser.VAR)
            self.state = 174
            self.var_decl_list()
            self.state = 175
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
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.var_decl()
                self.state = 179
                self.match(MiniGoParser.COMMA)
                self.state = 180
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
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(MiniGoParser.ID)
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 185
                    self.type_name()


                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 188
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 189
                    self.expression(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(MiniGoParser.ID)
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 193
                        self.match(MiniGoParser.COMMA)
                        self.state = 194
                        self.match(MiniGoParser.ID) 
                    self.state = 199
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 200
                    self.type_name()


                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 203
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 204
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
            self.state = 209
            self.match(MiniGoParser.CONST)
            self.state = 210
            self.const_decl_list()
            self.state = 211
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
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.const_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.const_decl()
                self.state = 215
                self.match(MiniGoParser.COMMA)
                self.state = 216
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
            self.state = 220
            self.match(MiniGoParser.ID)
            self.state = 221
            self.match(MiniGoParser.ASSIGN)
            self.state = 222
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
            self.state = 224
            self.match(MiniGoParser.FUNC)
            self.state = 225
            self.match(MiniGoParser.ID)
            self.state = 226
            self.match(MiniGoParser.LP)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 227
                self.params_list()


            self.state = 230
            self.match(MiniGoParser.RP)
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LP]:
                self.state = 231
                self.match(MiniGoParser.LP)
                self.state = 232
                self.type_name()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 233
                    self.match(MiniGoParser.COMMA)
                    self.state = 234
                    self.type_name()
                    self.state = 239
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 240
                self.match(MiniGoParser.RP)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.state = 242
                self.type_name()
                pass
            elif token in [MiniGoParser.LB, MiniGoParser.NEWLINE]:
                pass
            else:
                pass
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 245
                self.match(MiniGoParser.NEWLINE)


            self.state = 248
            self.block_stmt()
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
            self.state = 250
            self.match(MiniGoParser.ID)
            self.state = 251
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
            self.state = 253
            self.match(MiniGoParser.FUNC)
            self.state = 254
            self.match(MiniGoParser.LP)
            self.state = 255
            self.receiver()
            self.state = 256
            self.match(MiniGoParser.RP)
            self.state = 257
            self.match(MiniGoParser.ID)
            self.state = 258
            self.match(MiniGoParser.LP)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 259
                self.method_params()


            self.state = 262
            self.match(MiniGoParser.RP)
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LP]:
                self.state = 263
                self.match(MiniGoParser.LP)
                self.state = 264
                self.type_name()
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 265
                    self.match(MiniGoParser.COMMA)
                    self.state = 266
                    self.type_name()
                    self.state = 271
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 272
                self.match(MiniGoParser.RP)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.state = 274
                self.type_name()
                pass
            elif token in [MiniGoParser.LB, MiniGoParser.NEWLINE]:
                pass
            else:
                pass
            self.state = 277
            self.block_stmt()
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
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.method_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.method_param()
                self.state = 281
                self.match(MiniGoParser.COMMA)
                self.state = 282
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
            self.state = 286
            self.match(MiniGoParser.ID)
            self.state = 287
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
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.param()
                self.state = 291
                self.match(MiniGoParser.COMMA)
                self.state = 292
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
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 296
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 297
                self.match(MiniGoParser.ID)
                self.state = 298
                self.match(MiniGoParser.COMMA)
                self.state = 299
                self.match(MiniGoParser.ID)
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 300
                    self.match(MiniGoParser.COMMA)
                    self.state = 301
                    self.match(MiniGoParser.ID)
                    self.state = 306
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


            self.state = 309
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

        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


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
            self.state = 311
            self.match(MiniGoParser.TYPE)
            self.state = 312
            self.match(MiniGoParser.ID)
            self.state = 313
            self.match(MiniGoParser.STRUCT)
            self.state = 314
            self.match(MiniGoParser.LB)
            self.state = 318
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 315
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 320
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 321
            self.struct_type()
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 322
                self.match(MiniGoParser.NEWLINE)
                self.state = 327
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 328
            self.match(MiniGoParser.RB)
            self.state = 329
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
        self.enterRule(localctx, 40, self.RULE_struct_type)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RB, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.struct_field()
                self.state = 333
                self.struct_type()
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
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(MiniGoParser.ID)
            self.state = 338
            self.more_ids()
            self.state = 339
            self.type_name()
            self.state = 340
            self.struct_end()
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
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.match(MiniGoParser.COMMA)
                self.state = 344
                self.match(MiniGoParser.ID)
                self.state = 345
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
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SEMI:
                    self.state = 349
                    self.match(MiniGoParser.SEMI)


                self.state = 352
                self.match(MiniGoParser.NEWLINE)
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
        self.enterRule(localctx, 48, self.RULE_interface_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(MiniGoParser.TYPE)
            self.state = 356
            self.match(MiniGoParser.ID)
            self.state = 357
            self.match(MiniGoParser.INTERFACE)
            self.state = 358
            self.match(MiniGoParser.LB)
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 359
                self.match(MiniGoParser.NEWLINE)
                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 365
            self.interface_type()
            self.state = 366
            self.match(MiniGoParser.RB)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 367
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
        self.enterRule(localctx, 50, self.RULE_interface_type)
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.interface_method()
                self.state = 372
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
        self.enterRule(localctx, 52, self.RULE_interface_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(MiniGoParser.ID)
            self.state = 377
            self.match(MiniGoParser.LP)
            self.state = 378
            self.optional_params()
            self.state = 379
            self.match(MiniGoParser.RP)
            self.state = 380
            self.optional_type()
            self.state = 381
            self.optional_semi()
            self.state = 382
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
        self.enterRule(localctx, 54, self.RULE_optional_params)
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RP]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
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
        self.enterRule(localctx, 56, self.RULE_optional_type)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
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
        self.enterRule(localctx, 58, self.RULE_optional_semi)
        try:
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RB, MiniGoParser.ID, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
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
        self.enterRule(localctx, 60, self.RULE_declared_statement)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.variables_declared()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
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
        self.enterRule(localctx, 62, self.RULE_assign_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.assign_lhs()
            self.state = 401
            self.assign_op()
            self.state = 402
            self.expression(0)
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 403
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
        self.enterRule(localctx, 64, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
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
        self.enterRule(localctx, 66, self.RULE_assign_lhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(MiniGoParser.ID)
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.DOT or _la==MiniGoParser.LSB:
                self.state = 411
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.DOT]:
                    self.state = 409
                    self.field_access()
                    pass
                elif token in [MiniGoParser.LSB]:
                    self.state = 410
                    self.element_access()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 415
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
        self.enterRule(localctx, 68, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(MiniGoParser.IF)
            self.state = 417
            self.match(MiniGoParser.LP)
            self.state = 418
            self.expression(0)
            self.state = 419
            self.match(MiniGoParser.RP)
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 420
                self.match(MiniGoParser.NEWLINE)


            self.state = 423
            self.block_stmt()
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 424
                self.match(MiniGoParser.NEWLINE)


            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 427
                self.match(MiniGoParser.ELSE)
                self.state = 428
                self.if_statement()

            elif la_ == 2:
                self.state = 429
                self.match(MiniGoParser.ELSE)
                self.state = 430
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
        self.enterRule(localctx, 70, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(MiniGoParser.FOR)
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 434
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 435
                self.match(MiniGoParser.COMMA)
                self.state = 436
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 437
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 438
                self.match(MiniGoParser.RANGE)
                self.state = 439
                self.expression(0)
                self.state = 440
                self.block_stmt()
                pass

            elif la_ == 2:
                self.state = 442
                self.for_init()
                self.state = 443
                self.match(MiniGoParser.SEMI)
                self.state = 444
                self.expression(0)
                self.state = 445
                self.match(MiniGoParser.SEMI)
                self.state = 446
                self.for_update()
                self.state = 447
                self.block_stmt()
                pass

            elif la_ == 3:
                self.state = 449
                self.expression(0)
                self.state = 450
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
        self.enterRule(localctx, 72, self.RULE_for_init)
        self._la = 0 # Token type
        try:
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.match(MiniGoParser.ID)
                self.state = 455
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 456
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.match(MiniGoParser.ID)
                self.state = 458
                self.assign_op()
                self.state = 459
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 461
                self.match(MiniGoParser.VAR)
                self.state = 462
                self.match(MiniGoParser.ID)
                self.state = 464
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 463
                    self.type_name()


                self.state = 466
                self.match(MiniGoParser.ASSIGN)
                self.state = 467
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
        self.enterRule(localctx, 74, self.RULE_for_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.assign_lhs()
            self.state = 471
            self.assign_op()
            self.state = 472
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
        self.enterRule(localctx, 76, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(MiniGoParser.BREAK)
            self.state = 475
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
        self.enterRule(localctx, 78, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(MiniGoParser.CONTINUE)
            self.state = 478
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
        self.enterRule(localctx, 80, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(MiniGoParser.RETURN)
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 481
                    self.expression(0)


                self.state = 484
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.state = 486
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 485
                    self.expression(0)


                self.state = 488
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
        self.enterRule(localctx, 82, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 491
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 492
                self.assign_lhs()
                pass


            self.state = 495
            self.match(MiniGoParser.LP)
            self.state = 497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 496
                self.list_expression()


            self.state = 499
            self.match(MiniGoParser.RP)
            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 500
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
        self.enterRule(localctx, 84, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 503
                self.match(MiniGoParser.NEWLINE)


            self.state = 506
            self.match(MiniGoParser.LB)
            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 507
                self.match(MiniGoParser.NEWLINE)


            self.state = 514
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 512
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                        self.state = 510
                        self.statement()
                        pass
                    elif token in [MiniGoParser.NEWLINE]:
                        self.state = 511
                        self.match(MiniGoParser.NEWLINE)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 516
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

            self.state = 518
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 517
                self.match(MiniGoParser.NEWLINE)


            self.state = 520
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
        self.enterRule(localctx, 86, self.RULE_expr_list)
        try:
            self.state = 527
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 522
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 523
                self.expression(0)
                self.state = 524
                self.match(MiniGoParser.COMMA)
                self.state = 525
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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 537
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 532
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 533
                    self.match(MiniGoParser.OR)
                    self.state = 534
                    self.expression1(0) 
                self.state = 539
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 548
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 543
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 544
                    self.match(MiniGoParser.AND)
                    self.state = 545
                    self.expression2(0) 
                self.state = 550
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 559
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 554
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 555
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.EQUAL or _la==MiniGoParser.NOT_EQUAL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 556
                    self.expression3(0) 
                self.state = 561
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 570
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 565
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 566
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESS_OR_EQUAL) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 567
                    self.expression4(0) 
                self.state = 572
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

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
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 581
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,63,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 576
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 577
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 578
                    self.expression5(0) 
                self.state = 583
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,63,self._ctx)

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
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_expression5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 592
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 587
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 588
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 589
                    self.expression6() 
                self.state = 594
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

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
        self.enterRule(localctx, 100, self.RULE_expression6)
        try:
            self.state = 600
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 595
                self.match(MiniGoParser.NOT)
                self.state = 596
                self.expression6()
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 597
                self.match(MiniGoParser.SUB)
                self.state = 598
                self.expression6()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 599
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
        self.enterRule(localctx, 102, self.RULE_expression7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.operand()
            self.state = 608
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 606
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSB]:
                        self.state = 603
                        self.element_access()
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 604
                        self.field_access()
                        pass
                    elif token in [MiniGoParser.LP]:
                        self.state = 605
                        self.call_expr()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 610
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

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
        self.enterRule(localctx, 104, self.RULE_operand)
        try:
            self.state = 617
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
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
        self.enterRule(localctx, 106, self.RULE_element_access)
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
        self.enterRule(localctx, 108, self.RULE_field_access)
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
        self.enterRule(localctx, 110, self.RULE_call_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
            self.match(MiniGoParser.LP)
            self.state = 628
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
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
        self.enterRule(localctx, 112, self.RULE_literal)
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
                self.array_literal()
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
        self.enterRule(localctx, 114, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 642
            self.array_type()
            self.state = 643
            self.match(MiniGoParser.LB)
            self.state = 644
            self.list_expression()
            self.state = 645
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
        self.enterRule(localctx, 116, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.match(MiniGoParser.LSB)
            self.state = 648
            self.match(MiniGoParser.INT_LIT)
            self.state = 649
            self.match(MiniGoParser.RSB)
            self.state = 655
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,71,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 650
                    self.match(MiniGoParser.LSB)
                    self.state = 651
                    self.match(MiniGoParser.INT_LIT)
                    self.state = 652
                    self.match(MiniGoParser.RSB) 
                self.state = 657
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,71,self._ctx)

            self.state = 658
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
        self.enterRule(localctx, 118, self.RULE_type_name)
        try:
            self.state = 666
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 660
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 661
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 662
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 663
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 664
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 665
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
        self.enterRule(localctx, 120, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
            self.match(MiniGoParser.ID)
            self.state = 669
            self.match(MiniGoParser.LB)
            self.state = 671
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 670
                self.field_list()


            self.state = 673
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
        self.enterRule(localctx, 122, self.RULE_field_list)
        try:
            self.state = 680
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 675
                self.field_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 676
                self.field_init()
                self.state = 677
                self.match(MiniGoParser.COMMA)
                self.state = 678
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
        self.enterRule(localctx, 124, self.RULE_field_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 682
            self.match(MiniGoParser.ID)
            self.state = 683
            self.match(MiniGoParser.COLON)
            self.state = 684
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
        self.enterRule(localctx, 126, self.RULE_list_expression)
        try:
            self.state = 691
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 686
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 687
                self.expression(0)
                self.state = 688
                self.match(MiniGoParser.COMMA)
                self.state = 689
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
        self._predicates[44] = self.expression_sempred
        self._predicates[45] = self.expression1_sempred
        self._predicates[46] = self.expression2_sempred
        self._predicates[47] = self.expression3_sempred
        self._predicates[48] = self.expression4_sempred
        self._predicates[49] = self.expression5_sempred
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
         





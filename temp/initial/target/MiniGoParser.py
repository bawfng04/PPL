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
        buf.write("\u02f3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\5\3\u00aa\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u00b1\n\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5\u00b9\n\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\5\6\u00c2\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\5\7\u00cc\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u00d6")
        buf.write("\n\t\3\t\3\t\3\t\3\t\3\t\5\t\u00dd\n\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\5\t\u00e7\n\t\3\n\3\n\3\n\3\n\5\n\u00ed")
        buf.write("\n\n\3\13\3\13\3\13\3\13\5\13\u00f3\n\13\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\5\r\u00fe\n\r\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\5\17\u0108\n\17\3\17\3\17\5\17")
        buf.write("\u010c\n\17\3\17\5\17\u010f\n\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\5\20\u011a\n\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u0121\n\21\3\22\3\22\3\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u012d\n\23\3\23\3\23\5\23")
        buf.write("\u0131\n\23\3\23\5\23\u0134\n\23\3\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u0144\n\24\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u014c\n")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\5\26\u0153\n\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u0168\n\31\3\32\3")
        buf.write("\32\3\32\5\32\u016d\n\32\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u0178\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u018b\n\37\3 \3 \3 \5 \u0190\n \3 \3 ")
        buf.write("\5 \u0194\n \3 \3 \3!\3!\5!\u019a\n!\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3$\3$\3$\3$\3$\7$\u01aa\n$\f$\16$\u01ad")
        buf.write("\13$\3%\3%\3%\5%\u01b2\n%\3%\3%\5%\u01b6\n%\3&\3&\3&\3")
        buf.write("&\3&\3&\5&\u01be\n&\3&\5&\u01c1\n&\3\'\3\'\3\'\3\'\5\'")
        buf.write("\u01c7\n\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3*\3*\3*\5*\u01d6")
        buf.write("\n*\3+\3+\3+\3+\3,\3,\3,\5,\u01df\n,\3,\3,\3,\3,\3,\3")
        buf.write(",\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\5.\u01f3\n.\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3")
        buf.write("\62\5\62\u0204\n\62\3\62\3\62\5\62\u0208\n\62\3\62\5\62")
        buf.write("\u020b\n\62\3\63\3\63\5\63\u020f\n\63\3\63\3\63\5\63\u0213")
        buf.write("\n\63\3\63\3\63\3\63\3\64\3\64\5\64\u021a\n\64\3\64\3")
        buf.write("\64\5\64\u021e\n\64\3\64\3\64\5\64\u0222\n\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\5\65\u022a\n\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\5\66\u0231\n\66\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\7\67\u0239\n\67\f\67\16\67\u023c\13\67\38\38\38\38\3")
        buf.write("8\38\78\u0244\n8\f8\168\u0247\138\39\39\39\39\39\39\7")
        buf.write("9\u024f\n9\f9\169\u0252\139\3:\3:\3:\3:\3:\3:\7:\u025a")
        buf.write("\n:\f:\16:\u025d\13:\3;\3;\3;\3;\3;\3;\7;\u0265\n;\f;")
        buf.write("\16;\u0268\13;\3<\3<\3<\3<\3<\3<\7<\u0270\n<\f<\16<\u0273")
        buf.write("\13<\3=\3=\3=\3=\3=\5=\u027a\n=\3>\3>\3>\3?\3?\3?\3?\5")
        buf.write("?\u0283\n?\3?\3?\5?\u0287\n?\3@\3@\3@\3@\3@\3@\5@\u028f")
        buf.write("\n@\3A\3A\3A\3A\3B\3B\3B\3C\3C\5C\u029a\nC\3C\3C\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\3D\5D\u02a6\nD\3E\3E\3E\3E\3E\3F\3F\3")
        buf.write("F\3F\3G\3G\3G\3G\3G\5G\u02b6\nG\3H\3H\3H\3H\3H\3H\3H\3")
        buf.write("H\3H\5H\u02c1\nH\3I\3I\3I\3I\3I\3I\3J\3J\3J\3J\3J\5J\u02ce")
        buf.write("\nJ\3K\3K\3K\3K\3K\3K\5K\u02d6\nK\3L\3L\3L\3L\3L\3M\3")
        buf.write("M\5M\u02df\nM\3N\3N\3N\3N\3N\5N\u02e6\nN\3O\3O\3O\3O\3")
        buf.write("P\3P\3P\3P\3P\5P\u02f1\nP\3P\2\tFlnprtvQ\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098")
        buf.write("\u009a\u009c\u009e\2\13\4\2\66\66;;\4\2\t\n\67\67\4\2")
        buf.write("%*--\4\2..\67\67\3\2\34\35\3\2\36!\3\2\27\30\3\2\31\33")
        buf.write("\4\2\67\6799\2\u030b\2\u00a0\3\2\2\2\4\u00a9\3\2\2\2\6")
        buf.write("\u00b0\3\2\2\2\b\u00b8\3\2\2\2\n\u00c1\3\2\2\2\f\u00cb")
        buf.write("\3\2\2\2\16\u00cd\3\2\2\2\20\u00e6\3\2\2\2\22\u00ec\3")
        buf.write("\2\2\2\24\u00f2\3\2\2\2\26\u00f4\3\2\2\2\30\u00fd\3\2")
        buf.write("\2\2\32\u00ff\3\2\2\2\34\u0103\3\2\2\2\36\u0119\3\2\2")
        buf.write("\2 \u0120\3\2\2\2\"\u0122\3\2\2\2$\u0125\3\2\2\2&\u0143")
        buf.write("\3\2\2\2(\u014b\3\2\2\2*\u0152\3\2\2\2,\u0154\3\2\2\2")
        buf.write(".\u015e\3\2\2\2\60\u0167\3\2\2\2\62\u016c\3\2\2\2\64\u016e")
        buf.write("\3\2\2\2\66\u0177\3\2\2\28\u0179\3\2\2\2:\u0183\3\2\2")
        buf.write("\2<\u018a\3\2\2\2>\u018c\3\2\2\2@\u0199\3\2\2\2B\u019b")
        buf.write("\3\2\2\2D\u01a0\3\2\2\2F\u01a2\3\2\2\2H\u01b5\3\2\2\2")
        buf.write("J\u01b7\3\2\2\2L\u01c6\3\2\2\2N\u01c8\3\2\2\2P\u01cf\3")
        buf.write("\2\2\2R\u01d5\3\2\2\2T\u01d7\3\2\2\2V\u01db\3\2\2\2X\u01e6")
        buf.write("\3\2\2\2Z\u01ef\3\2\2\2\\\u01f7\3\2\2\2^\u01fb\3\2\2\2")
        buf.write("`\u01fe\3\2\2\2b\u0201\3\2\2\2d\u020e\3\2\2\2f\u0217\3")
        buf.write("\2\2\2h\u0229\3\2\2\2j\u0230\3\2\2\2l\u0232\3\2\2\2n\u023d")
        buf.write("\3\2\2\2p\u0248\3\2\2\2r\u0253\3\2\2\2t\u025e\3\2\2\2")
        buf.write("v\u0269\3\2\2\2x\u0279\3\2\2\2z\u027b\3\2\2\2|\u0286\3")
        buf.write("\2\2\2~\u028e\3\2\2\2\u0080\u0290\3\2\2\2\u0082\u0294")
        buf.write("\3\2\2\2\u0084\u0297\3\2\2\2\u0086\u02a5\3\2\2\2\u0088")
        buf.write("\u02a7\3\2\2\2\u008a\u02ac\3\2\2\2\u008c\u02b5\3\2\2\2")
        buf.write("\u008e\u02c0\3\2\2\2\u0090\u02c2\3\2\2\2\u0092\u02cd\3")
        buf.write("\2\2\2\u0094\u02d5\3\2\2\2\u0096\u02d7\3\2\2\2\u0098\u02de")
        buf.write("\3\2\2\2\u009a\u02e5\3\2\2\2\u009c\u02e7\3\2\2\2\u009e")
        buf.write("\u02f0\3\2\2\2\u00a0\u00a1\5\4\3\2\u00a1\u00a2\5\b\5\2")
        buf.write("\u00a2\u00a3\5\6\4\2\u00a3\u00a4\5\4\3\2\u00a4\u00a5\7")
        buf.write("\2\2\3\u00a5\3\3\2\2\2\u00a6\u00aa\3\2\2\2\u00a7\u00a8")
        buf.write("\7;\2\2\u00a8\u00aa\5\4\3\2\u00a9\u00a6\3\2\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00aa\5\3\2\2\2\u00ab\u00b1\3\2\2\2\u00ac")
        buf.write("\u00ad\5\4\3\2\u00ad\u00ae\5\b\5\2\u00ae\u00af\5\6\4\2")
        buf.write("\u00af\u00b1\3\2\2\2\u00b0\u00ab\3\2\2\2\u00b0\u00ac\3")
        buf.write("\2\2\2\u00b1\7\3\2\2\2\u00b2\u00b9\5\16\b\2\u00b3\u00b9")
        buf.write("\5\26\f\2\u00b4\u00b9\5\34\17\2\u00b5\u00b9\5$\23\2\u00b6")
        buf.write("\u00b9\5,\27\2\u00b7\u00b9\58\35\2\u00b8\u00b2\3\2\2\2")
        buf.write("\u00b8\u00b3\3\2\2\2\u00b8\u00b4\3\2\2\2\u00b8\u00b5\3")
        buf.write("\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\u00bb\5\4\3\2\u00bb\t\3\2\2\2\u00bc\u00c2")
        buf.write("\5\f\7\2\u00bd\u00be\5\f\7\2\u00be\u00bf\5\4\3\2\u00bf")
        buf.write("\u00c0\5\n\6\2\u00c0\u00c2\3\2\2\2\u00c1\u00bc\3\2\2\2")
        buf.write("\u00c1\u00bd\3\2\2\2\u00c2\13\3\2\2\2\u00c3\u00cc\5@!")
        buf.write("\2\u00c4\u00cc\5B\"\2\u00c5\u00cc\5J&\2\u00c6\u00cc\5")
        buf.write("R*\2\u00c7\u00cc\5^\60\2\u00c8\u00cc\5`\61\2\u00c9\u00cc")
        buf.write("\5d\63\2\u00ca\u00cc\5b\62\2\u00cb\u00c3\3\2\2\2\u00cb")
        buf.write("\u00c4\3\2\2\2\u00cb\u00c5\3\2\2\2\u00cb\u00c6\3\2\2\2")
        buf.write("\u00cb\u00c7\3\2\2\2\u00cb\u00c8\3\2\2\2\u00cb\u00c9\3")
        buf.write("\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\r\3\2\2\2\u00cd\u00ce")
        buf.write("\7\20\2\2\u00ce\u00cf\5\20\t\2\u00cf\u00d0\t\2\2\2\u00d0")
        buf.write("\17\3\2\2\2\u00d1\u00d2\7\67\2\2\u00d2\u00d5\5\u0094K")
        buf.write("\2\u00d3\u00d4\7%\2\2\u00d4\u00d6\5l\67\2\u00d5\u00d3")
        buf.write("\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00e7\3\2\2\2\u00d7")
        buf.write("\u00d8\7\67\2\2\u00d8\u00d9\5\22\n\2\u00d9\u00dc\5\u0094")
        buf.write("K\2\u00da\u00db\7%\2\2\u00db\u00dd\5j\66\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e7\3\2\2\2\u00de")
        buf.write("\u00df\7\67\2\2\u00df\u00e0\7%\2\2\u00e0\u00e7\5l\67\2")
        buf.write("\u00e1\u00e2\7\67\2\2\u00e2\u00e3\5\24\13\2\u00e3\u00e4")
        buf.write("\7%\2\2\u00e4\u00e5\5j\66\2\u00e5\u00e7\3\2\2\2\u00e6")
        buf.write("\u00d1\3\2\2\2\u00e6\u00d7\3\2\2\2\u00e6\u00de\3\2\2\2")
        buf.write("\u00e6\u00e1\3\2\2\2\u00e7\21\3\2\2\2\u00e8\u00ed\3\2")
        buf.write("\2\2\u00e9\u00ea\7\65\2\2\u00ea\u00eb\7\67\2\2\u00eb\u00ed")
        buf.write("\5\22\n\2\u00ec\u00e8\3\2\2\2\u00ec\u00e9\3\2\2\2\u00ed")
        buf.write("\23\3\2\2\2\u00ee\u00f3\3\2\2\2\u00ef\u00f0\7\65\2\2\u00f0")
        buf.write("\u00f1\7\67\2\2\u00f1\u00f3\5\24\13\2\u00f2\u00ee\3\2")
        buf.write("\2\2\u00f2\u00ef\3\2\2\2\u00f3\25\3\2\2\2\u00f4\u00f5")
        buf.write("\7\17\2\2\u00f5\u00f6\5\30\r\2\u00f6\u00f7\t\2\2\2\u00f7")
        buf.write("\27\3\2\2\2\u00f8\u00fe\5\32\16\2\u00f9\u00fa\5\32\16")
        buf.write("\2\u00fa\u00fb\7\65\2\2\u00fb\u00fc\5\30\r\2\u00fc\u00fe")
        buf.write("\3\2\2\2\u00fd\u00f8\3\2\2\2\u00fd\u00f9\3\2\2\2\u00fe")
        buf.write("\31\3\2\2\2\u00ff\u0100\7\67\2\2\u0100\u0101\7%\2\2\u0101")
        buf.write("\u0102\5l\67\2\u0102\33\3\2\2\2\u0103\u0104\7\7\2\2\u0104")
        buf.write("\u0105\7\67\2\2\u0105\u0107\7/\2\2\u0106\u0108\5&\24\2")
        buf.write("\u0107\u0106\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\3")
        buf.write("\2\2\2\u0109\u010b\7\60\2\2\u010a\u010c\5\36\20\2\u010b")
        buf.write("\u010a\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010e\3\2\2\2")
        buf.write("\u010d\u010f\7;\2\2\u010e\u010d\3\2\2\2\u010e\u010f\3")
        buf.write("\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\5f\64\2\u0111\u0112")
        buf.write("\t\2\2\2\u0112\35\3\2\2\2\u0113\u0114\7/\2\2\u0114\u0115")
        buf.write("\5\u0094K\2\u0115\u0116\5 \21\2\u0116\u0117\7\60\2\2\u0117")
        buf.write("\u011a\3\2\2\2\u0118\u011a\5\u0094K\2\u0119\u0113\3\2")
        buf.write("\2\2\u0119\u0118\3\2\2\2\u011a\37\3\2\2\2\u011b\u0121")
        buf.write("\3\2\2\2\u011c\u011d\7\65\2\2\u011d\u011e\5\u0094K\2\u011e")
        buf.write("\u011f\5 \21\2\u011f\u0121\3\2\2\2\u0120\u011b\3\2\2\2")
        buf.write("\u0120\u011c\3\2\2\2\u0121!\3\2\2\2\u0122\u0123\7\67\2")
        buf.write("\2\u0123\u0124\t\3\2\2\u0124#\3\2\2\2\u0125\u0126\7\7")
        buf.write("\2\2\u0126\u0127\7/\2\2\u0127\u0128\5\"\22\2\u0128\u0129")
        buf.write("\7\60\2\2\u0129\u012a\7\67\2\2\u012a\u012c\7/\2\2\u012b")
        buf.write("\u012d\5&\24\2\u012c\u012b\3\2\2\2\u012c\u012d\3\2\2\2")
        buf.write("\u012d\u012e\3\2\2\2\u012e\u0130\7\60\2\2\u012f\u0131")
        buf.write("\5\u0094K\2\u0130\u012f\3\2\2\2\u0130\u0131\3\2\2\2\u0131")
        buf.write("\u0133\3\2\2\2\u0132\u0134\7;\2\2\u0133\u0132\3\2\2\2")
        buf.write("\u0133\u0134\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\5")
        buf.write("f\64\2\u0136\u0137\t\2\2\2\u0137%\3\2\2\2\u0138\u0139")
        buf.write("\7\67\2\2\u0139\u0144\5\u0094K\2\u013a\u013b\7\67\2\2")
        buf.write("\u013b\u013c\5\24\13\2\u013c\u013d\5\u0094K\2\u013d\u0144")
        buf.write("\3\2\2\2\u013e\u0144\5(\25\2\u013f\u0140\5(\25\2\u0140")
        buf.write("\u0141\7\65\2\2\u0141\u0142\5&\24\2\u0142\u0144\3\2\2")
        buf.write("\2\u0143\u0138\3\2\2\2\u0143\u013a\3\2\2\2\u0143\u013e")
        buf.write("\3\2\2\2\u0143\u013f\3\2\2\2\u0144\'\3\2\2\2\u0145\u0146")
        buf.write("\7\67\2\2\u0146\u014c\5\u0094K\2\u0147\u0148\7\67\2\2")
        buf.write("\u0148\u0149\5*\26\2\u0149\u014a\5\u0094K\2\u014a\u014c")
        buf.write("\3\2\2\2\u014b\u0145\3\2\2\2\u014b\u0147\3\2\2\2\u014c")
        buf.write(")\3\2\2\2\u014d\u014e\7\65\2\2\u014e\u0153\7\67\2\2\u014f")
        buf.write("\u0150\7\65\2\2\u0150\u0151\7\67\2\2\u0151\u0153\5*\26")
        buf.write("\2\u0152\u014d\3\2\2\2\u0152\u014f\3\2\2\2\u0153+\3\2")
        buf.write("\2\2\u0154\u0155\7\b\2\2\u0155\u0156\7\67\2\2\u0156\u0157")
        buf.write("\7\t\2\2\u0157\u0158\7\61\2\2\u0158\u0159\5\62\32\2\u0159")
        buf.write("\u015a\5.\30\2\u015a\u015b\5\62\32\2\u015b\u015c\7\62")
        buf.write("\2\2\u015c\u015d\t\2\2\2\u015d-\3\2\2\2\u015e\u015f\5")
        buf.write("\64\33\2\u015f\u0160\5\62\32\2\u0160\u0161\5\60\31\2\u0161")
        buf.write("/\3\2\2\2\u0162\u0168\3\2\2\2\u0163\u0164\5\64\33\2\u0164")
        buf.write("\u0165\5\62\32\2\u0165\u0166\5\60\31\2\u0166\u0168\3\2")
        buf.write("\2\2\u0167\u0162\3\2\2\2\u0167\u0163\3\2\2\2\u0168\61")
        buf.write("\3\2\2\2\u0169\u016d\3\2\2\2\u016a\u016b\7;\2\2\u016b")
        buf.write("\u016d\5\62\32\2\u016c\u0169\3\2\2\2\u016c\u016a\3\2\2")
        buf.write("\2\u016d\63\3\2\2\2\u016e\u016f\7\67\2\2\u016f\u0170\5")
        buf.write("\66\34\2\u0170\u0171\5\u0094K\2\u0171\u0172\t\2\2\2\u0172")
        buf.write("\65\3\2\2\2\u0173\u0178\3\2\2\2\u0174\u0175\7\65\2\2\u0175")
        buf.write("\u0176\7\67\2\2\u0176\u0178\5\66\34\2\u0177\u0173\3\2")
        buf.write("\2\2\u0177\u0174\3\2\2\2\u0178\67\3\2\2\2\u0179\u017a")
        buf.write("\7\b\2\2\u017a\u017b\7\67\2\2\u017b\u017c\7\n\2\2\u017c")
        buf.write("\u017d\7\61\2\2\u017d\u017e\5\62\32\2\u017e\u017f\5:\36")
        buf.write("\2\u017f\u0180\5\62\32\2\u0180\u0181\7\62\2\2\u0181\u0182")
        buf.write("\t\2\2\2\u01829\3\2\2\2\u0183\u0184\5> \2\u0184\u0185")
        buf.write("\5<\37\2\u0185;\3\2\2\2\u0186\u018b\3\2\2\2\u0187\u0188")
        buf.write("\5> \2\u0188\u0189\5<\37\2\u0189\u018b\3\2\2\2\u018a\u0186")
        buf.write("\3\2\2\2\u018a\u0187\3\2\2\2\u018b=\3\2\2\2\u018c\u018d")
        buf.write("\7\67\2\2\u018d\u018f\7/\2\2\u018e\u0190\5&\24\2\u018f")
        buf.write("\u018e\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\3\2\2\2")
        buf.write("\u0191\u0193\7\60\2\2\u0192\u0194\5\u0094K\2\u0193\u0192")
        buf.write("\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0195\3\2\2\2\u0195")
        buf.write("\u0196\t\2\2\2\u0196?\3\2\2\2\u0197\u019a\5\16\b\2\u0198")
        buf.write("\u019a\5\26\f\2\u0199\u0197\3\2\2\2\u0199\u0198\3\2\2")
        buf.write("\2\u019aA\3\2\2\2\u019b\u019c\5F$\2\u019c\u019d\5D#\2")
        buf.write("\u019d\u019e\5l\67\2\u019e\u019f\t\2\2\2\u019fC\3\2\2")
        buf.write("\2\u01a0\u01a1\t\4\2\2\u01a1E\3\2\2\2\u01a2\u01a3\b$\1")
        buf.write("\2\u01a3\u01a4\7\67\2\2\u01a4\u01ab\3\2\2\2\u01a5\u01a6")
        buf.write("\f\4\2\2\u01a6\u01aa\5\u0082B\2\u01a7\u01a8\f\3\2\2\u01a8")
        buf.write("\u01aa\5\u0080A\2\u01a9\u01a5\3\2\2\2\u01a9\u01a7\3\2")
        buf.write("\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac")
        buf.write("\3\2\2\2\u01acG\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01b6")
        buf.write("\3\2\2\2\u01af\u01b2\5\u0082B\2\u01b0\u01b2\5\u0080A\2")
        buf.write("\u01b1\u01af\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b3\3")
        buf.write("\2\2\2\u01b3\u01b4\5H%\2\u01b4\u01b6\3\2\2\2\u01b5\u01ae")
        buf.write("\3\2\2\2\u01b5\u01b1\3\2\2\2\u01b6I\3\2\2\2\u01b7\u01b8")
        buf.write("\7\3\2\2\u01b8\u01b9\7/\2\2\u01b9\u01ba\5l\67\2\u01ba")
        buf.write("\u01bb\7\60\2\2\u01bb\u01bd\5f\64\2\u01bc\u01be\5L\'\2")
        buf.write("\u01bd\u01bc\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c0\3")
        buf.write("\2\2\2\u01bf\u01c1\5P)\2\u01c0\u01bf\3\2\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1K\3\2\2\2\u01c2\u01c7\5N(\2\u01c3\u01c4")
        buf.write("\5N(\2\u01c4\u01c5\5L\'\2\u01c5\u01c7\3\2\2\2\u01c6\u01c2")
        buf.write("\3\2\2\2\u01c6\u01c3\3\2\2\2\u01c7M\3\2\2\2\u01c8\u01c9")
        buf.write("\7\4\2\2\u01c9\u01ca\7\3\2\2\u01ca\u01cb\7/\2\2\u01cb")
        buf.write("\u01cc\5l\67\2\u01cc\u01cd\7\60\2\2\u01cd\u01ce\5f\64")
        buf.write("\2\u01ceO\3\2\2\2\u01cf\u01d0\7\4\2\2\u01d0\u01d1\5f\64")
        buf.write("\2\u01d1Q\3\2\2\2\u01d2\u01d6\5T+\2\u01d3\u01d6\5V,\2")
        buf.write("\u01d4\u01d6\5X-\2\u01d5\u01d2\3\2\2\2\u01d5\u01d3\3\2")
        buf.write("\2\2\u01d5\u01d4\3\2\2\2\u01d6S\3\2\2\2\u01d7\u01d8\7")
        buf.write("\5\2\2\u01d8\u01d9\5l\67\2\u01d9\u01da\5f\64\2\u01daU")
        buf.write("\3\2\2\2\u01db\u01de\7\5\2\2\u01dc\u01df\5\\/\2\u01dd")
        buf.write("\u01df\5Z.\2\u01de\u01dc\3\2\2\2\u01de\u01dd\3\2\2\2\u01df")
        buf.write("\u01e0\3\2\2\2\u01e0\u01e1\t\2\2\2\u01e1\u01e2\5l\67\2")
        buf.write("\u01e2\u01e3\t\2\2\2\u01e3\u01e4\5\\/\2\u01e4\u01e5\5")
        buf.write("f\64\2\u01e5W\3\2\2\2\u01e6\u01e7\7\5\2\2\u01e7\u01e8")
        buf.write("\t\5\2\2\u01e8\u01e9\7\65\2\2\u01e9\u01ea\t\5\2\2\u01ea")
        buf.write("\u01eb\7-\2\2\u01eb\u01ec\7\23\2\2\u01ec\u01ed\5l\67\2")
        buf.write("\u01ed\u01ee\5f\64\2\u01eeY\3\2\2\2\u01ef\u01f0\7\20\2")
        buf.write("\2\u01f0\u01f2\7\67\2\2\u01f1\u01f3\5\u0094K\2\u01f2\u01f1")
        buf.write("\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4")
        buf.write("\u01f5\7%\2\2\u01f5\u01f6\5l\67\2\u01f6[\3\2\2\2\u01f7")
        buf.write("\u01f8\7\67\2\2\u01f8\u01f9\5D#\2\u01f9\u01fa\5l\67\2")
        buf.write("\u01fa]\3\2\2\2\u01fb\u01fc\7\22\2\2\u01fc\u01fd\t\2\2")
        buf.write("\2\u01fd_\3\2\2\2\u01fe\u01ff\7\21\2\2\u01ff\u0200\t\2")
        buf.write("\2\2\u0200a\3\2\2\2\u0201\u020a\7\6\2\2\u0202\u0204\5")
        buf.write("l\67\2\u0203\u0202\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205")
        buf.write("\3\2\2\2\u0205\u020b\7\66\2\2\u0206\u0208\5l\67\2\u0207")
        buf.write("\u0206\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0209\3\2\2\2")
        buf.write("\u0209\u020b\7;\2\2\u020a\u0203\3\2\2\2\u020a\u0207\3")
        buf.write("\2\2\2\u020bc\3\2\2\2\u020c\u020f\7\67\2\2\u020d\u020f")
        buf.write("\5F$\2\u020e\u020c\3\2\2\2\u020e\u020d\3\2\2\2\u020f\u0210")
        buf.write("\3\2\2\2\u0210\u0212\7/\2\2\u0211\u0213\5\u009eP\2\u0212")
        buf.write("\u0211\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u0214\3\2\2\2")
        buf.write("\u0214\u0215\7\60\2\2\u0215\u0216\t\2\2\2\u0216e\3\2\2")
        buf.write("\2\u0217\u0219\7\61\2\2\u0218\u021a\7;\2\2\u0219\u0218")
        buf.write("\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u021b\3\2\2\2\u021b")
        buf.write("\u021d\5h\65\2\u021c\u021e\7;\2\2\u021d\u021c\3\2\2\2")
        buf.write("\u021d\u021e\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0221\7")
        buf.write("\62\2\2\u0220\u0222\7\66\2\2\u0221\u0220\3\2\2\2\u0221")
        buf.write("\u0222\3\2\2\2\u0222g\3\2\2\2\u0223\u022a\3\2\2\2\u0224")
        buf.write("\u0225\5\f\7\2\u0225\u0226\5h\65\2\u0226\u022a\3\2\2\2")
        buf.write("\u0227\u0228\7;\2\2\u0228\u022a\5h\65\2\u0229\u0223\3")
        buf.write("\2\2\2\u0229\u0224\3\2\2\2\u0229\u0227\3\2\2\2\u022ai")
        buf.write("\3\2\2\2\u022b\u0231\5l\67\2\u022c\u022d\5l\67\2\u022d")
        buf.write("\u022e\7\65\2\2\u022e\u022f\5j\66\2\u022f\u0231\3\2\2")
        buf.write("\2\u0230\u022b\3\2\2\2\u0230\u022c\3\2\2\2\u0231k\3\2")
        buf.write("\2\2\u0232\u0233\b\67\1\2\u0233\u0234\5n8\2\u0234\u023a")
        buf.write("\3\2\2\2\u0235\u0236\f\4\2\2\u0236\u0237\7#\2\2\u0237")
        buf.write("\u0239\5n8\2\u0238\u0235\3\2\2\2\u0239\u023c\3\2\2\2\u023a")
        buf.write("\u0238\3\2\2\2\u023a\u023b\3\2\2\2\u023bm\3\2\2\2\u023c")
        buf.write("\u023a\3\2\2\2\u023d\u023e\b8\1\2\u023e\u023f\5p9\2\u023f")
        buf.write("\u0245\3\2\2\2\u0240\u0241\f\4\2\2\u0241\u0242\7\"\2\2")
        buf.write("\u0242\u0244\5p9\2\u0243\u0240\3\2\2\2\u0244\u0247\3\2")
        buf.write("\2\2\u0245\u0243\3\2\2\2\u0245\u0246\3\2\2\2\u0246o\3")
        buf.write("\2\2\2\u0247\u0245\3\2\2\2\u0248\u0249\b9\1\2\u0249\u024a")
        buf.write("\5r:\2\u024a\u0250\3\2\2\2\u024b\u024c\f\4\2\2\u024c\u024d")
        buf.write("\t\6\2\2\u024d\u024f\5r:\2\u024e\u024b\3\2\2\2\u024f\u0252")
        buf.write("\3\2\2\2\u0250\u024e\3\2\2\2\u0250\u0251\3\2\2\2\u0251")
        buf.write("q\3\2\2\2\u0252\u0250\3\2\2\2\u0253\u0254\b:\1\2\u0254")
        buf.write("\u0255\5t;\2\u0255\u025b\3\2\2\2\u0256\u0257\f\4\2\2\u0257")
        buf.write("\u0258\t\7\2\2\u0258\u025a\5t;\2\u0259\u0256\3\2\2\2\u025a")
        buf.write("\u025d\3\2\2\2\u025b\u0259\3\2\2\2\u025b\u025c\3\2\2\2")
        buf.write("\u025cs\3\2\2\2\u025d\u025b\3\2\2\2\u025e\u025f\b;\1\2")
        buf.write("\u025f\u0260\5v<\2\u0260\u0266\3\2\2\2\u0261\u0262\f\4")
        buf.write("\2\2\u0262\u0263\t\b\2\2\u0263\u0265\5v<\2\u0264\u0261")
        buf.write("\3\2\2\2\u0265\u0268\3\2\2\2\u0266\u0264\3\2\2\2\u0266")
        buf.write("\u0267\3\2\2\2\u0267u\3\2\2\2\u0268\u0266\3\2\2\2\u0269")
        buf.write("\u026a\b<\1\2\u026a\u026b\5x=\2\u026b\u0271\3\2\2\2\u026c")
        buf.write("\u026d\f\4\2\2\u026d\u026e\t\t\2\2\u026e\u0270\5x=\2\u026f")
        buf.write("\u026c\3\2\2\2\u0270\u0273\3\2\2\2\u0271\u026f\3\2\2\2")
        buf.write("\u0271\u0272\3\2\2\2\u0272w\3\2\2\2\u0273\u0271\3\2\2")
        buf.write("\2\u0274\u0275\7$\2\2\u0275\u027a\5x=\2\u0276\u0277\7")
        buf.write("\30\2\2\u0277\u027a\5x=\2\u0278\u027a\5z>\2\u0279\u0274")
        buf.write("\3\2\2\2\u0279\u0276\3\2\2\2\u0279\u0278\3\2\2\2\u027a")
        buf.write("y\3\2\2\2\u027b\u027c\5~@\2\u027c\u027d\5|?\2\u027d{\3")
        buf.write("\2\2\2\u027e\u0287\3\2\2\2\u027f\u0283\5\u0080A\2\u0280")
        buf.write("\u0283\5\u0082B\2\u0281\u0283\5\u0084C\2\u0282\u027f\3")
        buf.write("\2\2\2\u0282\u0280\3\2\2\2\u0282\u0281\3\2\2\2\u0283\u0284")
        buf.write("\3\2\2\2\u0284\u0285\5|?\2\u0285\u0287\3\2\2\2\u0286\u027e")
        buf.write("\3\2\2\2\u0286\u0282\3\2\2\2\u0287}\3\2\2\2\u0288\u028f")
        buf.write("\5\u0086D\2\u0289\u028f\7\67\2\2\u028a\u028b\7/\2\2\u028b")
        buf.write("\u028c\5l\67\2\u028c\u028d\7\60\2\2\u028d\u028f\3\2\2")
        buf.write("\2\u028e\u0288\3\2\2\2\u028e\u0289\3\2\2\2\u028e\u028a")
        buf.write("\3\2\2\2\u028f\177\3\2\2\2\u0290\u0291\7\63\2\2\u0291")
        buf.write("\u0292\5l\67\2\u0292\u0293\7\64\2\2\u0293\u0081\3\2\2")
        buf.write("\2\u0294\u0295\7+\2\2\u0295\u0296\7\67\2\2\u0296\u0083")
        buf.write("\3\2\2\2\u0297\u0299\7/\2\2\u0298\u029a\5\u009eP\2\u0299")
        buf.write("\u0298\3\2\2\2\u0299\u029a\3\2\2\2\u029a\u029b\3\2\2\2")
        buf.write("\u029b\u029c\7\60\2\2\u029c\u0085\3\2\2\2\u029d\u02a6")
        buf.write("\79\2\2\u029e\u02a6\78\2\2\u029f\u02a6\7:\2\2\u02a0\u02a6")
        buf.write("\7\25\2\2\u02a1\u02a6\7\26\2\2\u02a2\u02a6\7\24\2\2\u02a3")
        buf.write("\u02a6\5\u0088E\2\u02a4\u02a6\5\u0096L\2\u02a5\u029d\3")
        buf.write("\2\2\2\u02a5\u029e\3\2\2\2\u02a5\u029f\3\2\2\2\u02a5\u02a0")
        buf.write("\3\2\2\2\u02a5\u02a1\3\2\2\2\u02a5\u02a2\3\2\2\2\u02a5")
        buf.write("\u02a3\3\2\2\2\u02a5\u02a4\3\2\2\2\u02a6\u0087\3\2\2\2")
        buf.write("\u02a7\u02a8\5\u0090I\2\u02a8\u02a9\7\61\2\2\u02a9\u02aa")
        buf.write("\5\u008cG\2\u02aa\u02ab\7\62\2\2\u02ab\u0089\3\2\2\2\u02ac")
        buf.write("\u02ad\7\61\2\2\u02ad\u02ae\5\u008cG\2\u02ae\u02af\7\62")
        buf.write("\2\2\u02af\u008b\3\2\2\2\u02b0\u02b6\5\u008eH\2\u02b1")
        buf.write("\u02b2\5\u008eH\2\u02b2\u02b3\7\65\2\2\u02b3\u02b4\5\u008c")
        buf.write("G\2\u02b4\u02b6\3\2\2\2\u02b5\u02b0\3\2\2\2\u02b5\u02b1")
        buf.write("\3\2\2\2\u02b6\u008d\3\2\2\2\u02b7\u02c1\5\u008aF\2\u02b8")
        buf.write("\u02c1\5\u0096L\2\u02b9\u02c1\79\2\2\u02ba\u02c1\78\2")
        buf.write("\2\u02bb\u02c1\7:\2\2\u02bc\u02c1\7\25\2\2\u02bd\u02c1")
        buf.write("\7\26\2\2\u02be\u02c1\7\24\2\2\u02bf\u02c1\7\67\2\2\u02c0")
        buf.write("\u02b7\3\2\2\2\u02c0\u02b8\3\2\2\2\u02c0\u02b9\3\2\2\2")
        buf.write("\u02c0\u02ba\3\2\2\2\u02c0\u02bb\3\2\2\2\u02c0\u02bc\3")
        buf.write("\2\2\2\u02c0\u02bd\3\2\2\2\u02c0\u02be\3\2\2\2\u02c0\u02bf")
        buf.write("\3\2\2\2\u02c1\u008f\3\2\2\2\u02c2\u02c3\7\63\2\2\u02c3")
        buf.write("\u02c4\t\n\2\2\u02c4\u02c5\7\64\2\2\u02c5\u02c6\5\u0092")
        buf.write("J\2\u02c6\u02c7\5\u0094K\2\u02c7\u0091\3\2\2\2\u02c8\u02ce")
        buf.write("\3\2\2\2\u02c9\u02ca\7\63\2\2\u02ca\u02cb\t\n\2\2\u02cb")
        buf.write("\u02cc\7\64\2\2\u02cc\u02ce\5\u0092J\2\u02cd\u02c8\3\2")
        buf.write("\2\2\u02cd\u02c9\3\2\2\2\u02ce\u0093\3\2\2\2\u02cf\u02d6")
        buf.write("\7\f\2\2\u02d0\u02d6\7\r\2\2\u02d1\u02d6\7\13\2\2\u02d2")
        buf.write("\u02d6\7\16\2\2\u02d3\u02d6\7\67\2\2\u02d4\u02d6\5\u0090")
        buf.write("I\2\u02d5\u02cf\3\2\2\2\u02d5\u02d0\3\2\2\2\u02d5\u02d1")
        buf.write("\3\2\2\2\u02d5\u02d2\3\2\2\2\u02d5\u02d3\3\2\2\2\u02d5")
        buf.write("\u02d4\3\2\2\2\u02d6\u0095\3\2\2\2\u02d7\u02d8\7\67\2")
        buf.write("\2\u02d8\u02d9\7\61\2\2\u02d9\u02da\5\u0098M\2\u02da\u02db")
        buf.write("\7\62\2\2\u02db\u0097\3\2\2\2\u02dc\u02df\3\2\2\2\u02dd")
        buf.write("\u02df\5\u009aN\2\u02de\u02dc\3\2\2\2\u02de\u02dd\3\2")
        buf.write("\2\2\u02df\u0099\3\2\2\2\u02e0\u02e6\5\u009cO\2\u02e1")
        buf.write("\u02e2\5\u009cO\2\u02e2\u02e3\7\65\2\2\u02e3\u02e4\5\u009a")
        buf.write("N\2\u02e4\u02e6\3\2\2\2\u02e5\u02e0\3\2\2\2\u02e5\u02e1")
        buf.write("\3\2\2\2\u02e6\u009b\3\2\2\2\u02e7\u02e8\7\67\2\2\u02e8")
        buf.write("\u02e9\7,\2\2\u02e9\u02ea\5l\67\2\u02ea\u009d\3\2\2\2")
        buf.write("\u02eb\u02f1\5l\67\2\u02ec\u02ed\5l\67\2\u02ed\u02ee\7")
        buf.write("\65\2\2\u02ee\u02ef\5\u009eP\2\u02ef\u02f1\3\2\2\2\u02f0")
        buf.write("\u02eb\3\2\2\2\u02f0\u02ec\3\2\2\2\u02f1\u009f\3\2\2\2")
        buf.write("F\u00a9\u00b0\u00b8\u00c1\u00cb\u00d5\u00dc\u00e6\u00ec")
        buf.write("\u00f2\u00fd\u0107\u010b\u010e\u0119\u0120\u012c\u0130")
        buf.write("\u0133\u0143\u014b\u0152\u0167\u016c\u0177\u018a\u018f")
        buf.write("\u0193\u0199\u01a9\u01ab\u01b1\u01b5\u01bd\u01c0\u01c6")
        buf.write("\u01d5\u01de\u01f2\u0203\u0207\u020a\u020e\u0212\u0219")
        buf.write("\u021d\u0221\u0229\u0230\u023a\u0245\u0250\u025b\u0266")
        buf.write("\u0271\u0279\u0282\u0286\u028e\u0299\u02a5\u02b5\u02c0")
        buf.write("\u02cd\u02d5\u02de\u02e5\u02f0")
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
    RULE_else_if_chain = 37
    RULE_else_if_branch = 38
    RULE_else_clause = 39
    RULE_for_statement = 40
    RULE_for_condition = 41
    RULE_for_three_parts = 42
    RULE_for_range = 43
    RULE_for_declaration = 44
    RULE_for_assign = 45
    RULE_break_statement = 46
    RULE_continue_statement = 47
    RULE_return_statement = 48
    RULE_call_statement = 49
    RULE_block_stmt = 50
    RULE_block_content = 51
    RULE_expr_list = 52
    RULE_expression = 53
    RULE_expression1 = 54
    RULE_expression2 = 55
    RULE_expression3 = 56
    RULE_expression4 = 57
    RULE_expression5 = 58
    RULE_expression6 = 59
    RULE_expression7 = 60
    RULE_more_access_expr = 61
    RULE_operand = 62
    RULE_element_access = 63
    RULE_field_access = 64
    RULE_call_expr = 65
    RULE_literal = 66
    RULE_typed_array_literal = 67
    RULE_untyped_array_literal = 68
    RULE_literal_list = 69
    RULE_literal_item = 70
    RULE_array_type = 71
    RULE_more_dimensions = 72
    RULE_type_name = 73
    RULE_struct_literal = 74
    RULE_optional_field_list = 75
    RULE_field_list = 76
    RULE_field_init = 77
    RULE_list_expression = 78

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
                   "if_statement", "else_if_chain", "else_if_branch", "else_clause", 
                   "for_statement", "for_condition", "for_three_parts", 
                   "for_range", "for_declaration", "for_assign", "break_statement", 
                   "continue_statement", "return_statement", "call_statement", 
                   "block_stmt", "block_content", "expr_list", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "more_access_expr", 
                   "operand", "element_access", "field_access", "call_expr", 
                   "literal", "typed_array_literal", "untyped_array_literal", 
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
            self.state = 158
            self.newlines()
            self.state = 159
            self.declared()
            self.state = 160
            self.more_declared()
            self.state = 161
            self.newlines()
            self.state = 162
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
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(MiniGoParser.NEWLINE)
                self.state = 166
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
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.newlines()
                self.state = 171
                self.declared()
                self.state = 172
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
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 176
                self.variables_declared()
                pass

            elif la_ == 2:
                self.state = 177
                self.constants_declared()
                pass

            elif la_ == 3:
                self.state = 178
                self.function_declared()
                pass

            elif la_ == 4:
                self.state = 179
                self.method_declared()
                pass

            elif la_ == 5:
                self.state = 180
                self.struct_declared()
                pass

            elif la_ == 6:
                self.state = 181
                self.interface_declared()
                pass


            self.state = 184
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
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.statement()
                self.state = 188
                self.newlines()
                self.state = 189
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
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.declared_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 197
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 198
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 199
                self.call_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 200
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
            self.state = 203
            self.match(MiniGoParser.VAR)
            self.state = 204
            self.var_decl()
            self.state = 205
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
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.match(MiniGoParser.ID)
                self.state = 208
                self.type_name()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 209
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 210
                    self.expression(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(MiniGoParser.ID)
                self.state = 214
                self.type_name_ids()
                self.state = 215
                self.type_name()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 216
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 217
                    self.expr_list()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.match(MiniGoParser.ID)

                self.state = 221
                self.match(MiniGoParser.ASSIGN)
                self.state = 222
                self.expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 223
                self.match(MiniGoParser.ID)
                self.state = 224
                self.comma_ids()

                self.state = 225
                self.match(MiniGoParser.ASSIGN)
                self.state = 226
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
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.match(MiniGoParser.COMMA)
                self.state = 232
                self.match(MiniGoParser.ID)
                self.state = 233
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
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ASSIGN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(MiniGoParser.COMMA)
                self.state = 238
                self.match(MiniGoParser.ID)
                self.state = 239
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
            self.state = 242
            self.match(MiniGoParser.CONST)
            self.state = 243
            self.const_decl_list()
            self.state = 244
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
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.const_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.const_decl()
                self.state = 248
                self.match(MiniGoParser.COMMA)
                self.state = 249
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
            self.state = 253
            self.match(MiniGoParser.ID)
            self.state = 254
            self.match(MiniGoParser.ASSIGN)
            self.state = 255
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
            self.state = 257
            self.match(MiniGoParser.FUNC)
            self.state = 258
            self.match(MiniGoParser.ID)
            self.state = 259
            self.match(MiniGoParser.LP)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 260
                self.params_list()


            self.state = 263
            self.match(MiniGoParser.RP)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 264
                self.return_type()


            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 267
                self.match(MiniGoParser.NEWLINE)


            self.state = 270
            self.block_stmt()
            self.state = 271
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
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(MiniGoParser.LP)
                self.state = 274
                self.type_name()
                self.state = 275
                self.more_types()
                self.state = 276
                self.match(MiniGoParser.RP)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
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
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RP]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(MiniGoParser.COMMA)
                self.state = 283
                self.type_name()
                self.state = 284
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
            self.state = 288
            self.match(MiniGoParser.ID)
            self.state = 289
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
            self.state = 291
            self.match(MiniGoParser.FUNC)
            self.state = 292
            self.match(MiniGoParser.LP)
            self.state = 293
            self.receiver()
            self.state = 294
            self.match(MiniGoParser.RP)
            self.state = 295
            self.match(MiniGoParser.ID)
            self.state = 296
            self.match(MiniGoParser.LP)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 297
                self.params_list()


            self.state = 300
            self.match(MiniGoParser.RP)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 301
                self.type_name()


            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 304
                self.match(MiniGoParser.NEWLINE)


            self.state = 307
            self.block_stmt()
            self.state = 308
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
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.match(MiniGoParser.ID)
                self.state = 311
                self.type_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.match(MiniGoParser.ID)
                self.state = 313
                self.comma_ids()
                self.state = 314
                self.type_name()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 316
                self.param()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 317
                self.param()
                self.state = 318
                self.match(MiniGoParser.COMMA)
                self.state = 319
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
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(MiniGoParser.ID)
                self.state = 324
                self.type_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(MiniGoParser.ID)
                self.state = 326
                self.comma_param_ids()
                self.state = 327
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
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.match(MiniGoParser.COMMA)
                self.state = 332
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.match(MiniGoParser.COMMA)
                self.state = 334
                self.match(MiniGoParser.ID)
                self.state = 335
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
            self.state = 338
            self.match(MiniGoParser.TYPE)
            self.state = 339
            self.match(MiniGoParser.ID)
            self.state = 340
            self.match(MiniGoParser.STRUCT)
            self.state = 341
            self.match(MiniGoParser.LB)
            self.state = 342
            self.opt_newlines()
            self.state = 343
            self.struct_type_list()
            self.state = 344
            self.opt_newlines()
            self.state = 345
            self.match(MiniGoParser.RB)
            self.state = 346
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
            self.state = 348
            self.struct_field()
            self.state = 349
            self.opt_newlines()
            self.state = 350
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
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RB, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.struct_field()
                self.state = 354
                self.opt_newlines()
                self.state = 355
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
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.match(MiniGoParser.NEWLINE)
                self.state = 361
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
            self.state = 364
            self.match(MiniGoParser.ID)
            self.state = 365
            self.more_ids()
            self.state = 366
            self.type_name()
            self.state = 367
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
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSB, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(MiniGoParser.COMMA)
                self.state = 371
                self.match(MiniGoParser.ID)
                self.state = 372
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
            self.state = 375
            self.match(MiniGoParser.TYPE)
            self.state = 376
            self.match(MiniGoParser.ID)
            self.state = 377
            self.match(MiniGoParser.INTERFACE)
            self.state = 378
            self.match(MiniGoParser.LB)
            self.state = 379
            self.opt_newlines()
            self.state = 380
            self.interface_type_list()
            self.state = 381
            self.opt_newlines()
            self.state = 382
            self.match(MiniGoParser.RB)
            self.state = 383
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
            self.state = 385
            self.interface_method()
            self.state = 386
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
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RB, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.interface_method()
                self.state = 390
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
            self.state = 394
            self.match(MiniGoParser.ID)
            self.state = 395
            self.match(MiniGoParser.LP)
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 396
                self.params_list()


            self.state = 399
            self.match(MiniGoParser.RP)
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 400
                self.type_name()


            self.state = 403
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
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.variables_declared()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
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
            self.state = 409
            self.assign_lhs(0)
            self.state = 410
            self.assign_op()
            self.state = 411
            self.expression(0)
            self.state = 412
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
            self.state = 414
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

        def assign_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_lhsContext,0)


        def field_access(self):
            return self.getTypedRuleContext(MiniGoParser.Field_accessContext,0)


        def element_access(self):
            return self.getTypedRuleContext(MiniGoParser.Element_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs" ):
                return visitor.visitAssign_lhs(self)
            else:
                return visitor.visitChildren(self)



    def assign_lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Assign_lhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_assign_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 423
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Assign_lhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_assign_lhs)
                        self.state = 419
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 420
                        self.field_access()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Assign_lhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_assign_lhs)
                        self.state = 421
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 422
                        self.element_access()
                        pass

             
                self.state = 427
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.DOT]:
                    self.state = 429
                    self.field_access()
                    pass
                elif token in [MiniGoParser.LSB]:
                    self.state = 430
                    self.element_access()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 433
                self.more_access()
                pass


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

        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def else_if_chain(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_chainContext,0)


        def else_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Else_clauseContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(MiniGoParser.IF)
            self.state = 438
            self.match(MiniGoParser.LP)
            self.state = 439
            self.expression(0)
            self.state = 440
            self.match(MiniGoParser.RP)
            self.state = 441
            self.block_stmt()
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 442
                self.else_if_chain()


            self.state = 446
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 445
                self.else_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_chainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if_branch(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_branchContext,0)


        def else_if_chain(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_chainContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_chain

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_chain" ):
                return visitor.visitElse_if_chain(self)
            else:
                return visitor.visitChildren(self)




    def else_if_chain(self):

        localctx = MiniGoParser.Else_if_chainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_else_if_chain)
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.else_if_branch()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                self.else_if_branch()
                self.state = 450
                self.else_if_chain()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_branchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_branch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_branch" ):
                return visitor.visitElse_if_branch(self)
            else:
                return visitor.visitChildren(self)




    def else_if_branch(self):

        localctx = MiniGoParser.Else_if_branchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_else_if_branch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(MiniGoParser.ELSE)
            self.state = 455
            self.match(MiniGoParser.IF)
            self.state = 456
            self.match(MiniGoParser.LP)
            self.state = 457
            self.expression(0)
            self.state = 458
            self.match(MiniGoParser.RP)
            self.state = 459
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_clause" ):
                return visitor.visitElse_clause(self)
            else:
                return visitor.visitChildren(self)




    def else_clause(self):

        localctx = MiniGoParser.Else_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_else_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(MiniGoParser.ELSE)
            self.state = 462
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

        def for_condition(self):
            return self.getTypedRuleContext(MiniGoParser.For_conditionContext,0)


        def for_three_parts(self):
            return self.getTypedRuleContext(MiniGoParser.For_three_partsContext,0)


        def for_range(self):
            return self.getTypedRuleContext(MiniGoParser.For_rangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_for_statement)
        try:
            self.state = 467
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.for_condition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.for_three_parts()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 466
                self.for_range()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_condition" ):
                return visitor.visitFor_condition(self)
            else:
                return visitor.visitChildren(self)




    def for_condition(self):

        localctx = MiniGoParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(MiniGoParser.FOR)
            self.state = 470
            self.expression(0)
            self.state = 471
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_three_partsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def for_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.For_assignContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.For_assignContext,i)


        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


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

        def for_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.For_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_three_parts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_three_parts" ):
                return visitor.visitFor_three_parts(self)
            else:
                return visitor.visitChildren(self)




    def for_three_parts(self):

        localctx = MiniGoParser.For_three_partsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_for_three_parts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(MiniGoParser.FOR)
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 474
                self.for_assign()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 475
                self.for_declaration()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 478
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 479
            self.expression(0)
            self.state = 480
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 481
            self.for_assign()
            self.state = 482
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_rangeContext(ParserRuleContext):
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
            return MiniGoParser.RULE_for_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_range" ):
                return visitor.visitFor_range(self)
            else:
                return visitor.visitChildren(self)




    def for_range(self):

        localctx = MiniGoParser.For_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_for_range)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(MiniGoParser.FOR)
            self.state = 485
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 486
            self.match(MiniGoParser.COMMA)
            self.state = 487
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 488
            self.match(MiniGoParser.SHORT_ASSIGN)
            self.state = 489
            self.match(MiniGoParser.RANGE)
            self.state = 490
            self.expression(0)
            self.state = 491
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_declarationContext(ParserRuleContext):
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


        def type_name(self):
            return self.getTypedRuleContext(MiniGoParser.Type_nameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_declaration" ):
                return visitor.visitFor_declaration(self)
            else:
                return visitor.visitChildren(self)




    def for_declaration(self):

        localctx = MiniGoParser.For_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_for_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.match(MiniGoParser.VAR)
            self.state = 494
            self.match(MiniGoParser.ID)
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 495
                self.type_name()


            self.state = 498
            self.match(MiniGoParser.ASSIGN)
            self.state = 499
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_assignContext(ParserRuleContext):
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
            return MiniGoParser.RULE_for_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_assign" ):
                return visitor.visitFor_assign(self)
            else:
                return visitor.visitChildren(self)




    def for_assign(self):

        localctx = MiniGoParser.For_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_for_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(MiniGoParser.ID)
            self.state = 502
            self.assign_op()
            self.state = 503
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
        self.enterRule(localctx, 92, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(MiniGoParser.BREAK)
            self.state = 506
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
        self.enterRule(localctx, 94, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(MiniGoParser.CONTINUE)
            self.state = 509
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
        self.enterRule(localctx, 96, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(MiniGoParser.RETURN)
            self.state = 520
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 513
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 512
                    self.expression(0)


                self.state = 515
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.state = 517
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 516
                    self.expression(0)


                self.state = 519
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
        self.enterRule(localctx, 98, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 522
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 523
                self.assign_lhs(0)
                pass


            self.state = 526
            self.match(MiniGoParser.LP)
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 527
                self.list_expression()


            self.state = 530
            self.match(MiniGoParser.RP)
            self.state = 531
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
        self.enterRule(localctx, 100, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(MiniGoParser.LB)
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 534
                self.match(MiniGoParser.NEWLINE)


            self.state = 537
            self.block_content()
            self.state = 539
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 538
                self.match(MiniGoParser.NEWLINE)


            self.state = 541
            self.match(MiniGoParser.RB)
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 542
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
        self.enterRule(localctx, 102, self.RULE_block_content)
        try:
            self.state = 551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 546
                self.statement()
                self.state = 547
                self.block_content()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 549
                self.match(MiniGoParser.NEWLINE)
                self.state = 550
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
        self.enterRule(localctx, 104, self.RULE_expr_list)
        try:
            self.state = 558
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 553
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 554
                self.expression(0)
                self.state = 555
                self.match(MiniGoParser.COMMA)
                self.state = 556
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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 568
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 563
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 564
                    self.match(MiniGoParser.OR)
                    self.state = 565
                    self.expression1(0) 
                self.state = 570
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

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
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 579
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 574
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 575
                    self.match(MiniGoParser.AND)
                    self.state = 576
                    self.expression2(0) 
                self.state = 581
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 590
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 585
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 586
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.EQUAL or _la==MiniGoParser.NOT_EQUAL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 587
                    self.expression3(0) 
                self.state = 592
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

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
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 601
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 596
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 597
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESS_OR_EQUAL) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 598
                    self.expression4(0) 
                self.state = 603
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

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
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 612
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 607
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 608
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 609
                    self.expression5(0) 
                self.state = 614
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

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
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_expression5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 623
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 618
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 619
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 620
                    self.expression6() 
                self.state = 625
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

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
        self.enterRule(localctx, 118, self.RULE_expression6)
        try:
            self.state = 631
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 626
                self.match(MiniGoParser.NOT)
                self.state = 627
                self.expression6()
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 628
                self.match(MiniGoParser.SUB)
                self.state = 629
                self.expression6()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.ID, MiniGoParser.FLOAT_LIT, MiniGoParser.INT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 630
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
        self.enterRule(localctx, 120, self.RULE_expression7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self.operand()
            self.state = 634
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
        self.enterRule(localctx, 122, self.RULE_more_access_expr)
        try:
            self.state = 644
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 640
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.LSB]:
                    self.state = 637
                    self.element_access()
                    pass
                elif token in [MiniGoParser.DOT]:
                    self.state = 638
                    self.field_access()
                    pass
                elif token in [MiniGoParser.LP]:
                    self.state = 639
                    self.call_expr()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 642
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
        self.enterRule(localctx, 124, self.RULE_operand)
        try:
            self.state = 652
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 646
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 647
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 648
                self.match(MiniGoParser.LP)
                self.state = 649
                self.expression(0)
                self.state = 650
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
        self.enterRule(localctx, 126, self.RULE_element_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.match(MiniGoParser.LSB)
            self.state = 655
            self.expression(0)
            self.state = 656
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
        self.enterRule(localctx, 128, self.RULE_field_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
            self.match(MiniGoParser.DOT)
            self.state = 659
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
        self.enterRule(localctx, 130, self.RULE_call_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.match(MiniGoParser.LP)
            self.state = 663
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 662
                self.list_expression()


            self.state = 665
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
        self.enterRule(localctx, 132, self.RULE_literal)
        try:
            self.state = 675
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 667
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 668
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 669
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 670
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 671
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 672
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 673
                self.typed_array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 674
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
        self.enterRule(localctx, 134, self.RULE_typed_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 677
            self.array_type()
            self.state = 678
            self.match(MiniGoParser.LB)
            self.state = 679
            self.literal_list()
            self.state = 680
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
        self.enterRule(localctx, 136, self.RULE_untyped_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 682
            self.match(MiniGoParser.LB)
            self.state = 683
            self.literal_list()
            self.state = 684
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
        self.enterRule(localctx, 138, self.RULE_literal_list)
        try:
            self.state = 691
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 686
                self.literal_item()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 687
                self.literal_item()
                self.state = 688
                self.match(MiniGoParser.COMMA)
                self.state = 689
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
        self.enterRule(localctx, 140, self.RULE_literal_item)
        try:
            self.state = 702
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 693
                self.untyped_array_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 694
                self.struct_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 695
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 696
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 697
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 698
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 699
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 700
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 701
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
        self.enterRule(localctx, 142, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 704
            self.match(MiniGoParser.LSB)
            self.state = 705
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 706
            self.match(MiniGoParser.RSB)
            self.state = 707
            self.more_dimensions()
            self.state = 708
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
        self.enterRule(localctx, 144, self.RULE_more_dimensions)
        self._la = 0 # Token type
        try:
            self.state = 715
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 711
                self.match(MiniGoParser.LSB)
                self.state = 712
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 713
                self.match(MiniGoParser.RSB)
                self.state = 714
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
        self.enterRule(localctx, 146, self.RULE_type_name)
        try:
            self.state = 723
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 717
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 718
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 719
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 720
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 721
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 722
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
        self.enterRule(localctx, 148, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 725
            self.match(MiniGoParser.ID)
            self.state = 726
            self.match(MiniGoParser.LB)
            self.state = 727
            self.optional_field_list()
            self.state = 728
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
        self.enterRule(localctx, 150, self.RULE_optional_field_list)
        try:
            self.state = 732
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 731
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
        self.enterRule(localctx, 152, self.RULE_field_list)
        try:
            self.state = 739
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 734
                self.field_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 735
                self.field_init()
                self.state = 736
                self.match(MiniGoParser.COMMA)
                self.state = 737
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
        self.enterRule(localctx, 154, self.RULE_field_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
            self.match(MiniGoParser.ID)
            self.state = 742
            self.match(MiniGoParser.COLON)
            self.state = 743
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
        self.enterRule(localctx, 156, self.RULE_list_expression)
        try:
            self.state = 750
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 745
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 746
                self.expression(0)
                self.state = 747
                self.match(MiniGoParser.COMMA)
                self.state = 748
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
        self._predicates[34] = self.assign_lhs_sempred
        self._predicates[53] = self.expression_sempred
        self._predicates[54] = self.expression1_sempred
        self._predicates[55] = self.expression2_sempred
        self._predicates[56] = self.expression3_sempred
        self._predicates[57] = self.expression4_sempred
        self._predicates[58] = self.expression5_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def assign_lhs_sempred(self, localctx:Assign_lhsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def expression5_sempred(self, localctx:Expression5Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         





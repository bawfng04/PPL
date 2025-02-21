"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
import sys
import os
import unittest
import inspect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
        def test_001(self):
                """Keywords"""
                self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

        def test_002(self):
                """Operators"""
                self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))

        def test_003(self):
                """Separators"""
                self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))

        def test_004(self):
                """Identifiers"""
                self.assertTrue(TestLexer.test("_VOTien","_VOTien,<EOF>", inspect.stack()[0].function))

        def test_005(self):
                """Literals INT"""
                self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))

        def test_006(self):
                """Literals INT 16*1 + 1 = 17"""
                self.assertTrue(TestLexer.test("0x11","0x11,<EOF>", inspect.stack()[0].function))

        def test_007(self):
                """Literals FLOAT"""
                self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))

        def test_008(self):
                """Literals String"""
                self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","\"VOTIEN \\r\",<EOF>", inspect.stack()[0].function))

        def test_009(self):
                """COMEMENTS"""
                self.assertTrue(TestLexer.test("// VOTIEN","<EOF>", inspect.stack()[0].function))

        def test_010(self):
                """COMEMENTS"""
                self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

        def test_011(self):
                """ERROR_CHAR"""
                self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

        def test_012(self):
                """UNCLOSE_STRING"""
                self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: \"VOTIEN", inspect.stack()[0].function))

        def test_013(self):
                """ILLEGAL_ESCAPE"""
                self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: \"VOTIEN\\f", inspect.stack()[0].function))

        #!!! 87 test yêu cầu code chấm sau
        def test_014(self):
                """Keywords"""
                self.assertTrue(TestLexer.test("else for return func type struct interface string int float boolean const var continue break range nil true false", "else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>", inspect.stack()[0].function))

        def test_015(self):
                """Operators"""
                self.assertTrue(TestLexer.test("+ - * / % == != > < <= >= && || ! = += -= *= /= %= :=", "+,-,*,/,%,==,!=,>,<,<=,>=,&&,||,!,=,+=,-=,*=,/=,%=,:=,<EOF>", inspect.stack()[0].function))

        def test_016(self):
                """Separators"""
                self.assertTrue(TestLexer.test("{}[](),;", "{,},[,],(,),,,;,<EOF>", inspect.stack()[0].function))

        def test_017(self):
                """skip"""
                self.assertTrue(TestLexer.test("\t\f\r ", "<EOF>", inspect.stack()[0].function))

        def test_018(self):
                """skip"""
                self.assertTrue(TestLexer.test("// tesst //", "<EOF>", inspect.stack()[0].function))

        def test_019(self):
                """skip"""
                self.assertTrue(TestLexer.test("/**///", "<EOF>", inspect.stack()[0].function))

        def test_020(self):
                """Identifiers"""
                self.assertTrue(TestLexer.test("2_bA", "2,_bA,<EOF>", inspect.stack()[0].function))

        def test_021(self):
                """Identifiers"""
                self.assertTrue(TestLexer.test("_", "_,<EOF>", inspect.stack()[0].function))

        def test_022(self):
                """Identifiers"""
                self.assertTrue(TestLexer.test("2b", "2,b,<EOF>", inspect.stack()[0].function))

        def test_023(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("-0120", "-,0,120,<EOF>", inspect.stack()[0].function))

        def test_024(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0b000", "0b000,<EOF>", inspect.stack()[0].function))

        def test_025(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0b1e", "0b1,e,<EOF>", inspect.stack()[0].function))

        def test_026(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("-0O72", "-,0O72,<EOF>", inspect.stack()[0].function))

        def test_027(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0xae2", "0xae2,<EOF>", inspect.stack()[0].function))

        def test_028(self):
                """FLOAT_LIT"""
                self.assertTrue(TestLexer.test("010.010e-020", "010.010e-020,<EOF>", inspect.stack()[0].function))

        def test_029(self):
                """FLOAT_LIT"""
                self.assertTrue(TestLexer.test("1.2Ee2", "1.2,Ee2,<EOF>", inspect.stack()[0].function))

        def test_030(self):
                """FLOAT_LIT"""
                self.assertTrue(TestLexer.test("00.1e2", "00.1e2,<EOF>", inspect.stack()[0].function))

        def test_031(self):
                """STRING_LIT"""
                self.assertTrue(TestLexer.test(""" "votien" """, "\"votien\",<EOF>", inspect.stack()[0].function))

        def test_032(self):
                """STRING_LIT"""
                self.assertTrue(TestLexer.test(""" "\\r" """, "\"\\r\",<EOF>", inspect.stack()[0].function))

        def test_033(self):
                """STRING_LIT"""
                self.assertTrue(TestLexer.test(""" "\\r \\r \\r" """, "\"\\r \\r \\r\",<EOF>", inspect.stack()[0].function))

        def test_034(self):
                """Keywords"""
                self.assertTrue(TestLexer.test(""" ^ """, "ErrorToken ^", inspect.stack()[0].function))

        def test_035(self):
                """BOOL_LIT"""
                self.assertTrue(TestLexer.test("true", "true,<EOF>", inspect.stack()[0].function))

        def test_036(self):
                """BOOL_LIT"""
                self.assertTrue(TestLexer.test("false", "false,<EOF>", inspect.stack()[0].function))

        def test_037(self):
                """NIL_LIT"""
                self.assertTrue(TestLexer.test("nil", "nil,<EOF>", inspect.stack()[0].function))

        def test_038(self):
                """ERROR_CHAR"""
                self.assertTrue(TestLexer.test("?", "ErrorToken ?", inspect.stack()[0].function))

        def test_039(self):
                """ERROR_CHAR"""
                self.assertTrue(TestLexer.test("@", "ErrorToken @", inspect.stack()[0].function))

        def test_040(self):
                """UNCLOSE_STRING"""
                self.assertTrue(TestLexer.test(""" 123" """, "123,Unclosed string: \" ", inspect.stack()[0].function))

        def test_041(self):
                """UNCLOSE_STRING"""
                self.assertTrue(TestLexer.test(""" "123
                " """, "Unclosed string: \"123", inspect.stack()[0].function))

        def test_042(self):
                """ILLEGAL_ESCAPE"""
                self.assertTrue(TestLexer.test(""" "&\\&" """, "Illegal escape in string: \"&\\&", inspect.stack()[0].function))

        def test_043(self):
                """ILLEGAL_ESCAPE"""
                self.assertTrue(TestLexer.test(""" "\\z" """, "Illegal escape in string: \"\\z", inspect.stack()[0].function))

        def test_044(self):
                """Literals String"""
                self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","\"VOTIEN \\r\",<EOF>", inspect.stack()[0].function))

        def test_045(self):
                """UNCLOSE_STRING"""
                self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: \"VOTIEN", inspect.stack()[0].function))

        def test_046(self):
                """Keywords"""
                self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

        def test_047(self):
                """Operators"""
                self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))

        def test_048(self):
                """Separators"""
                self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))

        def test_049(self):
                """Identifiers"""
                self.assertTrue(TestLexer.test("_VOTien","_VOTien,<EOF>", inspect.stack()[0].function))

        def test_050(self):
                """Literals INT"""
                self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))

        def test_051(self):
                """Literals INT 16*1 + 1 = 17"""
                self.assertTrue(TestLexer.test("0x11","0x11,<EOF>", inspect.stack()[0].function))

        def test_052(self):
                """Literals FLOAT"""
                self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))

        def test_053(self):
                """Literals String"""
                self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","\"VOTIEN \\r\",<EOF>", inspect.stack()[0].function))

        def test_054(self):
                """COMEMENTS"""
                self.assertTrue(TestLexer.test("// VOTIEN","<EOF>", inspect.stack()[0].function))

        def test_055(self):
                """COMEMENTS"""
                self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

        def test_056(self):
                """ERROR_CHAR"""
                self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

        def test_057(self):
                """UNCLOSE_STRING"""
                self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: \"VOTIEN", inspect.stack()[0].function))

        def test_058(self):
                """ILLEGAL_ESCAPE"""
                self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: \"VOTIEN\\f", inspect.stack()[0].function))

        def test_059(self):
                """Keywords"""
                self.assertTrue(TestLexer.test("else for return func type struct interface string int float boolean const var continue break range nil true false", "else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>", inspect.stack()[0].function))

        def test_060(self):
                """Operators"""
                self.assertTrue(TestLexer.test("+ - * / % == != > < <= >= && || ! = += -= *= /= %= :=", "+,-,*,/,%,==,!=,>,<,<=,>=,&&,||,!,=,+=,-=,*=,/=,%=,:=,<EOF>", inspect.stack()[0].function))

        def test_061(self):
                """Separators"""
                self.assertTrue(TestLexer.test("{}[](),;", "{,},[,],(,),,,;,<EOF>", inspect.stack()[0].function))

        def test_062(self):
                """skip"""
                self.assertTrue(TestLexer.test("\t\f\r ", "<EOF>", inspect.stack()[0].function))

        def test_063(self):
                """skip"""
                self.assertTrue(TestLexer.test("// tesst //", "<EOF>", inspect.stack()[0].function))

        def test_064(self):
                """skip"""
                self.assertTrue(TestLexer.test(""" /*
                /* a */ /* b */
                // 321231
                */ if /* */ /* */""", "if,<EOF>", inspect.stack()[0].function))

        def test_065(self):
                """skip"""
                self.assertTrue(TestLexer.test(""" /*
                /* a /* b /* b */  */  */
                */""", "<EOF>", inspect.stack()[0].function))

        def test_066(self):
                """skip"""
                self.assertTrue(TestLexer.test(""" /* //123312
                /* a /* b /* b */  */  */
                */""", "<EOF>", inspect.stack()[0].function))

        def test_067(self):
                """skip"""
                self.assertTrue(TestLexer.test("/*", "/,*,<EOF>", inspect.stack()[0].function))

        def test_068(self):
                """skip"""
                self.assertTrue(TestLexer.test("/**///", "<EOF>", inspect.stack()[0].function))

        def test_069(self):
                """Identifiers"""
                self.assertTrue(TestLexer.test("2_bA", "2,_bA,<EOF>", inspect.stack()[0].function))

        def test_070(self):
                """Identifiers"""
                self.assertTrue(TestLexer.test("_", "_,<EOF>", inspect.stack()[0].function))

        def test_071(self):
                """Identifiers"""
                self.assertTrue(TestLexer.test("2b", "2,b,<EOF>", inspect.stack()[0].function))

        def test_072(self):
                """Identifiers"""
                self.assertTrue(TestLexer.test("A_2b_3", "A_2b_3,<EOF>", inspect.stack()[0].function))

        def test_073(self):
                """Identifiers"""
                self.assertTrue(TestLexer.test("_a__", "_a__,<EOF>", inspect.stack()[0].function))

        def test_074(self):
                """Identifiers"""
                self.assertTrue(TestLexer.test("u_2_bB", "u_2_bB,<EOF>", inspect.stack()[0].function))

        def test_075(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0452.", "0452.,<EOF>", inspect.stack()[0].function))

        def test_076(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("-0120", "-,0,120,<EOF>", inspect.stack()[0].function))

        def test_077(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("012", "0,12,<EOF>", inspect.stack()[0].function))

        def test_078(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("1_2", "1,_2,<EOF>", inspect.stack()[0].function))

        def test_079(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("12", "12,<EOF>", inspect.stack()[0].function))

        def test_080(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("-12", "-,12,<EOF>", inspect.stack()[0].function))

        def test_081(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0b000", "0b000,<EOF>", inspect.stack()[0].function))

        def test_082(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0b1e", "0b1,e,<EOF>", inspect.stack()[0].function))

        def test_083(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0b12", "0b1,2,<EOF>", inspect.stack()[0].function))

        def test_084(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0b1101", "0b1101,<EOF>", inspect.stack()[0].function))

        def test_085(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0B111", "0B111,<EOF>", inspect.stack()[0].function))

        def test_086(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("00O72", "0,0O72,<EOF>", inspect.stack()[0].function))

        def test_087(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("-0O72", "-,0O72,<EOF>", inspect.stack()[0].function))

        def test_088(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0o18", "0o1,8,<EOF>", inspect.stack()[0].function))

        def test_089(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0o12", "0o12,<EOF>", inspect.stack()[0].function))

        def test_090(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0Oo1", "0,Oo1,<EOF>", inspect.stack()[0].function))

        def test_091(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("-0x2g", "-,0x2,g,<EOF>", inspect.stack()[0].function))

        def test_092(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0X0cb", "0X0cb,<EOF>", inspect.stack()[0].function))

        def test_093(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0xae2", "0xae2,<EOF>", inspect.stack()[0].function))

        def test_094(self):
                """INT_LIT"""
                self.assertTrue(TestLexer.test("0Xx2", "0,Xx2,<EOF>", inspect.stack()[0].function))

        def test_095(self):
                """FLOAT_LIT"""
                self.assertTrue(TestLexer.test("010.010e-020", "010.010e-020,<EOF>", inspect.stack()[0].function))

        def test_096(self):
                """FLOAT_LIT"""
                self.assertTrue(TestLexer.test("1.2e+-2", "1.2,e,+,-,2,<EOF>", inspect.stack()[0].function))

        def test_097(self):
                """FLOAT_LIT"""
                self.assertTrue(TestLexer.test("1.2Ee2", "1.2,Ee2,<EOF>", inspect.stack()[0].function))

        def test_098(self):
                """FLOAT_LIT"""
                self.assertTrue(TestLexer.test("09.e-002", "09.e-002,<EOF>", inspect.stack()[0].function))

        def test_099(self):
                """FLOAT_LIT"""
                self.assertTrue(TestLexer.test("1.e-2", "1.e-2,<EOF>", inspect.stack()[0].function))

        def test_100(self):
                """FLOAT_LIT"""
                self.assertTrue(TestLexer.test("1.e2", "1.e2,<EOF>", inspect.stack()[0].function))

        def test_101(self):
                """FLOAT_LIT"""
                self.assertTrue(TestLexer.test("1.e", "1.,e,<EOF>", inspect.stack()[0].function))

        def test_102(self):
                """FLOAT_LIT"""
                self.assertTrue(TestLexer.test("1.", "1.,<EOF>", inspect.stack()[0].function))

        def test_103(self):
                """FLOAT_LIT"""
                self.assertTrue(TestLexer.test("00.1e2", "00.1e2,<EOF>", inspect.stack()[0].function))

        def test_104(self):
                """FLOAT_LIT"""
                self.assertTrue(TestLexer.test(".e+2", ".,e,+,2,<EOF>", inspect.stack()[0].function))

        def test_105(self):
                """STRING_LIT"""
                self.assertTrue(TestLexer.test("if", "if,<EOF>", inspect.stack()[0].function))

        def test_106(self):
                """STRING_LIT"""
                self.assertTrue(TestLexer.test(""" "votien" """, "\"votien\",<EOF>", inspect.stack()[0].function))

        def test_107(self):
                """STRING_LIT"""
                self.assertTrue(TestLexer.test(""" "\\r" """, "\"\\r\",<EOF>", inspect.stack()[0].function))

        def test_108(self):
                """STRING_LIT"""
                self.assertTrue(TestLexer.test(""" "\\n" """, "\"\\n\",<EOF>", inspect.stack()[0].function))

        def test_109(self):
                """STRING_LIT"""
                self.assertTrue(TestLexer.test(""" "\\\\" """, "\"\\\\\",<EOF>", inspect.stack()[0].function))

        def test_110(self):
                """STRING_LIT"""
                self.assertTrue(TestLexer.test(""" "\\"" """, "\"\\\"\",<EOF>", inspect.stack()[0].function))

        def test_111(self):
                """STRING_LIT"""
                self.assertTrue(TestLexer.test(""" "a \\r a" """, "\"a \\r a\",<EOF>", inspect.stack()[0].function))

        def test_112(self):
                """STRING_LIT"""
                self.assertTrue(TestLexer.test(""" "\\r \\r \\r" """, "\"\\r \\r \\r\",<EOF>", inspect.stack()[0].function))

        def test_113(self):
                """Keywords"""
                self.assertTrue(TestLexer.test(""" "" """, "\"\",<EOF>", inspect.stack()[0].function))

        def test_114(self):
                """Keywords"""
                self.assertTrue(TestLexer.test(""" ^ """, "ErrorToken ^", inspect.stack()[0].function))

        def test_115(self):
                """Keywords"""
                self.assertTrue(TestLexer.test(""" /* @@ * */ """, "<EOF>", inspect.stack()[0].function))

        def test_116(self):
                """Keywords"""
                self.assertTrue(TestLexer.test("""
                /* a * */
        """, "<EOF>", inspect.stack()[0].function))

        def test_117(self):
                """Keywords"""
                self.assertTrue(TestLexer.test(""" // /* */  """, "<EOF>", inspect.stack()[0].function))

        def test_118(self):
                """Keywords"""
                self.assertTrue(TestLexer.test(""" // /*
                                        */""", "*,/,<EOF>", inspect.stack()[0].function))

        def test_119(self):
                """COMMENT"""
                self.assertTrue(TestLexer.test("""
                /* */ /* */ /*a // */ b""", "b,<EOF>", inspect.stack()[0].function))

        def test_120(self):
                """COMMENT"""
                self.assertTrue(TestLexer.test(""" /* a */ */ b """, "*,/,b,<EOF>", inspect.stack()[0].function))

        def test_121(self):
                """COMMENT"""
                self.assertTrue(TestLexer.test(""" /* /* */ a """, "a,<EOF>", inspect.stack()[0].function))

        def test_122(self):
                """COMMENT"""
                self.assertTrue(TestLexer.test(""" /* a /* b */ */ c /* */""", "c,<EOF>", inspect.stack()[0].function))

        def test_123(self):
                """COMMENT"""
                self.assertTrue(TestLexer.test(""" /* test */ a /* */ """, "a,<EOF>", inspect.stack()[0].function))

        def test_124(self):
                """COMMENT"""
                self.assertTrue(TestLexer.test("""
                /* test
                */ a /* */
        """, "a,;,<EOF>", inspect.stack()[0].function))

        def test_125(self):
                """COMMENT"""
                self.assertTrue(TestLexer.test("""
        // // //
        """, "<EOF>", inspect.stack()[0].function))

        def test_126(self):
                """COMMENT"""
                self.assertTrue(TestLexer.test("""
        // // // """, "<EOF>", inspect.stack()[0].function))

        def test_127(self):
                """COMMENT"""
                self.assertTrue(TestLexer.test(""" // // // """, "<EOF>", inspect.stack()[0].function))

        def test_128(self):
                """BOOL_LIT"""
                self.assertTrue(TestLexer.test("true", "true,<EOF>", inspect.stack()[0].function))

        def test_129(self):
                """BOOL_LIT"""
                self.assertTrue(TestLexer.test("false", "false,<EOF>", inspect.stack()[0].function))

        def test_130(self):
                """NIL_LIT"""
                self.assertTrue(TestLexer.test("nil", "nil,<EOF>", inspect.stack()[0].function))

        def test_131(self):
                """ERROR_CHAR"""
                self.assertTrue(TestLexer.test("?", "ErrorToken ?", inspect.stack()[0].function))

        def test_132(self):
                """ERROR_CHAR"""
                self.assertTrue(TestLexer.test("@", "ErrorToken @", inspect.stack()[0].function))

        def test_133(self):
                """ERROR_CHAR"""
                self.assertTrue(TestLexer.test("#", "ErrorToken #", inspect.stack()[0].function))

        def test_134(self):
                """ERROR_CHAR"""
                self.assertTrue(TestLexer.test("\\", "ErrorToken \\", inspect.stack()[0].function))

        def test_135(self):
                """ERROR_CHAR"""
                self.assertTrue(TestLexer.test("&", "ErrorToken &", inspect.stack()[0].function))

        def test_136(self):
                """UNCLOSE_STRING"""
                self.assertTrue(TestLexer.test(""" 123" """, "123,Unclosed string: \" ", inspect.stack()[0].function))

        def test_137(self):
                """UNCLOSE_STRING"""
                self.assertTrue(TestLexer.test(""" "123""", "Unclosed string: \"123", inspect.stack()[0].function))

        def test_138(self):
                """UNCLOSE_STRING"""
                self.assertTrue(TestLexer.test(""" "123 \\n \n" """, "Unclosed string: \"123 \\n ", inspect.stack()[0].function))

        def test_139(self):
                """UNCLOSE_STRING"""
                self.assertTrue(TestLexer.test(""" "123
                " """, "Unclosed string: \"123", inspect.stack()[0].function))

        def test_140(self):
                """UNCLOSE_STRING"""
                self.assertTrue(TestLexer.test(""" "123\n" """, "Unclosed string: \"123", inspect.stack()[0].function))

        def test_141(self):
                """ILLEGAL_ESCAPE"""
                self.assertTrue(TestLexer.test(""" "\\" \\\\ \\q" """, "Illegal escape in string: \"\\\" \\\\ \\q", inspect.stack()[0].function))

        def test_142(self):
                """ILLEGAL_ESCAPE"""
                self.assertTrue(TestLexer.test(""" "&\\&" """, "Illegal escape in string: \"&\\&", inspect.stack()[0].function))

        def test_143(self):
                """ILLEGAL_ESCAPE"""
                self.assertTrue(TestLexer.test(""" "\\z" """, "Illegal escape in string: \"\\z", inspect.stack()[0].function))

        def test_144(self):
                """ILLEGAL_ESCAPE"""
                self.assertTrue(TestLexer.test(""" "\\0" """, "Illegal escape in string: \"\\0", inspect.stack()[0].function))

        def test_145(self):
                """ILLEGAL_ESCAPE"""
                self.assertTrue(TestLexer.test(""" "\\b" """, "Illegal escape in string: \"\\b", inspect.stack()[0].function))

        def test_146(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                1
        """, "1,;,<EOF>", inspect.stack()[0].function))

        def test_147(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                0x1
        """, "0x1,;,<EOF>", inspect.stack()[0].function))

        def test_148(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                "s"
        """, "\"s\",;,<EOF>", inspect.stack()[0].function))

        def test_149(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                true
        """, "true,;,<EOF>", inspect.stack()[0].function))

        def test_150(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                2.
        """, "2.,;,<EOF>", inspect.stack()[0].function))

        def test_151(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                ID
        """, "ID,;,<EOF>", inspect.stack()[0].function))


        def test_152(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                return
        """, "return,;,<EOF>", inspect.stack()[0].function))

        def test_153(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                continue
                break
        """, "continue,;,break,;,<EOF>", inspect.stack()[0].function))

        def test_154(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                if
                }
                ]
                )
        """, "if,},;,],;,),;,<EOF>", inspect.stack()[0].function))

        def test_155(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                nil
        """, "nil,;,<EOF>", inspect.stack()[0].function))

        def test_156(self):
                self.assertTrue(TestLexer.test("""
                1e+7
        """, "1,e,+,7,;,<EOF>", inspect.stack()[0].function))

        def test_157(self):
                self.assertTrue(TestLexer.test("""
                \"12\"\"
        """, "\"12\",Unclosed string: \"", inspect.stack()[0].function))

        def test_158(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                nil
        """, "nil,;,<EOF>", inspect.stack()[0].function))

        def test_159(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                nil
        """, "nil,;,<EOF>", inspect.stack()[0].function))

        def test_160(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                nil
        """, "nil,;,<EOF>", inspect.stack()[0].function))

        def test_161(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                nil
        """, "nil,;,<EOF>", inspect.stack()[0].function))

        def test_162(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                nil
        """, "nil,;,<EOF>", inspect.stack()[0].function))

        def test_163(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                nil\n/*
        */""", "nil,;,<EOF>", inspect.stack()[0].function))

        def test_164(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                nil/*
        */\n""", "nil,;,<EOF>", inspect.stack()[0].function))

        def test_165(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                nil/*
        */""", "nil,<EOF>", inspect.stack()[0].function))

        def test_166(self):
                """NEW_LINE"""
                self.assertTrue(TestLexer.test("""
                nil
        """, "nil,;,<EOF>", inspect.stack()[0].function))

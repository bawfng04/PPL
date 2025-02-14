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


# testcase cũ
#     def test_001(self):
#         """Keywords"""
#         self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

#     def test_002(self):
#         """Operators"""
#         self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))

#     def test_003(self):
#         """Separators"""
#         self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))

#     def test_004(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.test("_VOTien","_VOTien,<EOF>", inspect.stack()[0].function))

#     def test_005(self):
#         """Literals INT"""
#         self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))

#     def test_006(self):
#         """Literals INT 16*1 + 1 = 17"""
#         self.assertTrue(TestLexer.test("0x11","17,<EOF>", inspect.stack()[0].function))

#     def test_007(self):
#         """Literals FLOAT"""
#         self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))

#     def test_008(self):
#         """Literals String"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","VOTIEN \\r,<EOF>", inspect.stack()[0].function))

#     def test_009(self):
#         """COMEMENTS"""
#         self.assertTrue(TestLexer.test("// VOTIEN","<EOF>", inspect.stack()[0].function))

#     def test_010(self):
#         """COMEMENTS"""
#         self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

#     def test_011(self):
#         """ERROR_CHAR"""
#         self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

#     def test_012(self):
#         """UNCLOSE_STRING"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: VOTIEN", inspect.stack()[0].function))

#     def test_013(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: VOTIEN\\f", inspect.stack()[0].function))

#     def test_014(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test("""
#             const a = 2;
# ""","\n,const,a,=,2,;,\n,<EOF>", inspect.stack()[0].function))

#     def test_015(self):
#         """Keywords"""
#         self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

#     def test_016(self):
#         """Operators"""
#         self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))

#     def test_017(self):
#         """Separators"""
#         self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))

#     def test_018(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.test("_VOTien","_VOTien,<EOF>", inspect.stack()[0].function))

#     def test_019(self):
#         """Literals INT"""
#         self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))

#     def test_020(self):
#         """Literals INT 16*1 + 1 = 17"""
#         self.assertTrue(TestLexer.test("0x11","17,<EOF>", inspect.stack()[0].function))

#     def test_021(self):
#         """Literals FLOAT"""
#         self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))

#     def test_022(self):
#         """Literals String"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","VOTIEN \\r,<EOF>", inspect.stack()[0].function))

#     def test_023(self):
#         """COMEMENTS"""
#         self.assertTrue(TestLexer.test("// VOTIEN","<EOF>", inspect.stack()[0].function))

#     def test_024(self):
#         """COMEMENTS"""
#         self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

#     def test_025(self):
#         """ERROR_CHAR"""
#         self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

#     def test_26(self):
#         """UNCLOSE_STRING"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: VOTIEN", inspect.stack()[0].function))

#     def test_027(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: VOTIEN\\f", inspect.stack()[0].function))

#     def test_028(self):
#         """INT_LIT"""
#         self.assertTrue(TestLexer.test("0452.", "0,452.,<EOF>", inspect.stack()[0].function))

#     def test_029(self):
#         """FLOAT_LIT"""
#         self.assertTrue(TestLexer.test("09.e-002", "0,9.e-0,0,2,<EOF>", inspect.stack()[0].function))

#     def test_030(self):
#         """INT_LIT"""
#         self.assertTrue(TestLexer.test("0452.", "0,452.,<EOF>", inspect.stack()[0].function))

#     def test_031(self):
#         """FLOAT_LIT"""
#         self.assertTrue(TestLexer.test(".e+2", ".,e,+,2,<EOF>", inspect.stack()[0].function))

#     def test_032(self):
#         """Keywords"""
#         self.assertTrue(TestLexer.test("""
#         /* a * */
#  """, "\n,\n,<EOF>", inspect.stack()[0].function))

#     def test_033(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test("""
#             const a = 2;
# ""","\n,const,a,=,2,;,\n,<EOF>", inspect.stack()[0].function))

#     def test_034(self):
#         """skip"""
#         self.assertTrue(TestLexer.test("\t\f\r ", "<EOF>", inspect.stack()[0].function))

#     def test_035(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test(""" "\\b" """, "Illegal escape in string: \\b", inspect.stack()[0].function))

#     def test_036(self):
#         """Keywords"""
#         self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

#     def test_037(self):
#         """Operators"""
#         self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))

#     def test_038(self):
#         """Separators"""
#         self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))

#     def test_039(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.test("_VOTien","_VOTien,<EOF>", inspect.stack()[0].function))

#     def test_040(self):
#         """Literals INT"""
#         self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))

#     def test_041(self):
#         """Literals INT 16*1 + 1 = 17"""
#         self.assertTrue(TestLexer.test("0x11","17,<EOF>", inspect.stack()[0].function))

#     def test_042(self):
#         """Literals FLOAT"""
#         self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))

#     def test_043(self):
#         """Literals String"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","VOTIEN \\r,<EOF>", inspect.stack()[0].function))

#     def test_044(self):
#         """COMEMENTS"""
#         self.assertTrue(TestLexer.test("// VOTIEN","<EOF>", inspect.stack()[0].function))

#     def test_045(self):
#         """COMEMENTS"""
#         self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

#     def test_046(self):
#         """ERROR_CHAR"""
#         self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

#     def test_047(self):
#         """UNCLOSE_STRING"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: VOTIEN", inspect.stack()[0].function))

#     def test_048(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: VOTIEN\\f", inspect.stack()[0].function))

#     def test_049(self):
#         """INT_LIT"""
#         self.assertTrue(TestLexer.test("0452.", "0,452.,<EOF>", inspect.stack()[0].function))

#     def test_050(self):
#         """FLOAT_LIT"""
#         self.assertTrue(TestLexer.test("09.e-002", "0,9.e-0,0,2,<EOF>", inspect.stack()[0].function))

#     def test_051(self):
#         """INT_LIT"""
#         self.assertTrue(TestLexer.test("0452.", "0,452.,<EOF>", inspect.stack()[0].function))

#     def test_052(self):
#         """FLOAT_LIT"""
#         self.assertTrue(TestLexer.test(".e+2", ".,e,+,2,<EOF>", inspect.stack()[0].function))

#     def test_053(self):
#         """Keywords"""
#         self.assertTrue(TestLexer.test("""
#         /* a * */
#  """, "\n,\n,<EOF>", inspect.stack()[0].function))

#     def test_054(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test("""
#             const a = 2;
# ""","\n,const,a,=,2,;,\n,<EOF>", inspect.stack()[0].function))

#     def test_055(self):
#         """skip"""
#         self.assertTrue(TestLexer.test("\t\f\r ", "<EOF>", inspect.stack()[0].function))

#     def test_056(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test(""" "\\b" """, "Illegal escape in string: \\b", inspect.stack()[0].function))

#     def test_057(self):
#             """ILLEGAL_ESCAPE"""
#             self.assertTrue(TestLexer.test("const a = 2;", "const,a,=,2,;,<EOF>", inspect.stack()[0].function))

#     def test_058(self):
#         """Operators"""
#         self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))

#     def test_059(self):
#         """Separators"""
#         self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))

#     def test_060(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.test("_VOTien","_VOTien,<EOF>", inspect.stack()[0].function))

#     def test_061(self):
#         """Literals INT"""
#         self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))

#     def test_062(self):
#         """Literals INT 16*1 + 1 = 17"""
#         self.assertTrue(TestLexer.test("0x11","17,<EOF>", inspect.stack()[0].function))

#     def test_063(self):
#         """Literals FLOAT"""
#         self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))

#     def test_064(self):
#         """Literals String"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","VOTIEN \\r,<EOF>", inspect.stack()[0].function))

#     def test_065(self):
#         """COMEMENTS"""
#         self.assertTrue(TestLexer.test("// VOTIEN","<EOF>", inspect.stack()[0].function))

#     def test_066(self):
#         """COMEMENTS"""
#         self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

#     def test_067(self):
#         """ERROR_CHAR"""
#         self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

#     def test_068(self):
#         """UNCLOSE_STRING"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: VOTIEN", inspect.stack()[0].function))

#     def test_069(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: VOTIEN\\f", inspect.stack()[0].function))

#     def test_070(self):
#         """INT_LIT"""
#         self.assertTrue(TestLexer.test("0452.", "0,452.,<EOF>", inspect.stack()[0].function))

#     def test_071(self):
#         """FLOAT_LIT"""
#         self.assertTrue(TestLexer.test("09.e-002", "0,9.e-0,0,2,<EOF>", inspect.stack()[0].function))

#     def test_072(self):
#         """INT_LIT"""
#         self.assertTrue(TestLexer.test("0452.", "0,452.,<EOF>", inspect.stack()[0].function))

#     def test_073(self):
#         """FLOAT_LIT"""
#         self.assertTrue(TestLexer.test(".e+2", ".,e,+,2,<EOF>", inspect.stack()[0].function))

#     def test_074(self):
#         """Keywords"""
#         self.assertTrue(TestLexer.test("""
#         /* a * */
#  """, "\n,\n,<EOF>", inspect.stack()[0].function))

#     def test_075(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test("""
#             const a = 2;
# ""","\n,const,a,=,2,;,\n,<EOF>", inspect.stack()[0].function))

#     def test_076(self):
#         """skip"""
#         self.assertTrue(TestLexer.test("\t\f\r ", "<EOF>", inspect.stack()[0].function))

#     def test_077(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test(""" "\\b" """, "Illegal escape in string: \\b", inspect.stack()[0].function))

#     def test_078(self):
#         """Keywords"""
#         self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

#     def test_079(self):
#         """Operators"""
#         self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))

#     def test_080(self):
#         """Separators"""
#         self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))

#     def test_081(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.test("_VOTien","_VOTien,<EOF>", inspect.stack()[0].function))

#     def test_082(self):
#         """Literals INT"""
#         self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))

#     def test_083(self):
#         """Literals INT 16*1 + 1 = 17"""
#         self.assertTrue(TestLexer.test("0x11","17,<EOF>", inspect.stack()[0].function))

#     def test_084(self):
#         """Literals FLOAT"""
#         self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))

#     def test_085(self):
#         """Literals String"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","VOTIEN \\r,<EOF>", inspect.stack()[0].function))

#     def test_086(self):
#         """COMEMENTS"""
#         self.assertTrue(TestLexer.test("// VOTIEN","<EOF>", inspect.stack()[0].function))

#     def test_087(self):
#         """COMEMENTS"""
#         self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

#     def test_088(self):
#         """ERROR_CHAR"""
#         self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

#     def test_089(self):
#         """UNCLOSE_STRING"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: VOTIEN", inspect.stack()[0].function))

#     def test_090(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: VOTIEN\\f", inspect.stack()[0].function))

#     def test_091(self):
#         """INT_LIT"""
#         self.assertTrue(TestLexer.test("0452.", "0,452.,<EOF>", inspect.stack()[0].function))

#     def test_092(self):
#         """FLOAT_LIT"""
#         self.assertTrue(TestLexer.test("09.e-002", "0,9.e-0,0,2,<EOF>", inspect.stack()[0].function))

#     def test_093(self):
#         """INT_LIT"""
#         self.assertTrue(TestLexer.test("0452.", "0,452.,<EOF>", inspect.stack()[0].function))

#     def test_094(self):
#         """FLOAT_LIT"""
#         self.assertTrue(TestLexer.test(".e+2", ".,e,+,2,<EOF>", inspect.stack()[0].function))

#     def test_095(self):
#         """Keywords"""
#         self.assertTrue(TestLexer.test("""
#         /* a * */
#  """, "\n,\n,<EOF>", inspect.stack()[0].function))

#     def test_096(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test("""
#             const a = 2;
# ""","\n,const,a,=,2,;,\n,<EOF>", inspect.stack()[0].function))

#     def test_097(self):
#         """skip"""
#         self.assertTrue(TestLexer.test("\t\f\r ", "<EOF>", inspect.stack()[0].function))

#     def test_098(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test(""" "\\b" """, "Illegal escape in string: \\b", inspect.stack()[0].function))

#     def test_099(self):
#         """Keywords"""
#         self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

#     def test_100(self):
#         """Operators"""
#         self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))

#testcase mới

#     def test_001(self):
#         """Keywords"""
#         self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

#     def test_002(self):
#         """Operators"""
#         self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))

#     def test_003(self):
#         """Separators"""
#         self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))

#     def test_004(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.test("_VOTien","_VOTien,<EOF>", inspect.stack()[0].function))

#     def test_005(self):
#         """Literals INT"""
#         self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))

#     def test_006(self):
#         """Literals INT 16*1 + 1 = 17"""
#         self.assertTrue(TestLexer.test("0x11","0x11,<EOF>", inspect.stack()[0].function))

#     def test_007(self):
#         """Literals FLOAT"""
#         self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))

#     def test_008(self):
#         """Literals String"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","VOTIEN \\r,<EOF>", inspect.stack()[0].function))

#     def test_009(self):
#         """COMEMENTS"""
#         self.assertTrue(TestLexer.test("// VOTIEN","<EOF>", inspect.stack()[0].function))

#     def test_010(self):
#         """COMEMENTS"""
#         self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

#     def test_011(self):
#         """ERROR_CHAR"""
#         self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

#     def test_012(self):
#         """UNCLOSE_STRING"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: VOTIEN", inspect.stack()[0].function))

#     def test_013(self):
#         """ILLEGAL_ESCAPE"""
#         self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: VOTIEN\\f", inspect.stack()[0].function))

#     def test_014(self):
#             """INT_LIT"""
#             self.assertTrue(TestLexer.test("0452.", "0452.,<EOF>", inspect.stack()[0].function))


#     def test_015(self):
#         """NEW_LINE"""
#         self.assertTrue(TestLexer.test("""
#             if
#             }
#             ]
#             )
# """, "if,},;,],;,),;,<EOF>", inspect.stack()[0].function))

#     def test_016(self):
#         """NEW_LINE"""
#         self.assertTrue(TestLexer.test("""
#             nil
# """, "nil,;,<EOF>", inspect.stack()[0].function))

#     def test_017(self):
#         """INT_LIT"""
#         self.assertTrue(TestLexer.test("-0120", "-,0,120,<EOF>", inspect.stack()[0].function))

#     def test_018(self):
#             """FLOAT_LIT"""
#             self.assertTrue(TestLexer.test("010.010e-020", "010.010e-020,<EOF>", inspect.stack()[0].function))

#     def test_019(self):
#             """Keywords"""
#             self.assertTrue(TestLexer.test("""
#             /* a * */
#     """, "<EOF>", inspect.stack()[0].function))

#     def test_020(self):
#             """COMMENT"""
#             self.assertTrue(TestLexer.test("""
#             /* test
#             */ a /* */
#     """, "a,;,<EOF>", inspect.stack()[0].function))

#     def test_021(self):
#         """Keywords"""
#         self.assertTrue(TestLexer.test("""
#         /* a * */
#  """, "<EOF>", inspect.stack()[0].function))

#     def test_022(self):
#         """INT_LIT"""
#         self.assertTrue(TestLexer.test("0452.", "0452.,<EOF>", inspect.stack()[0].function))

#     def test_023(self):
#         """FLOAT_LIT"""
#         self.assertTrue(TestLexer.test("010.010e-020", "010.010e-020,<EOF>", inspect.stack()[0].function))

#     def test_110(self):
#         """NEW_LINE"""
#         self.assertTrue(TestLexer.test("""
#             nil
# """, "nil,;,<EOF>", inspect.stack()[0].function))


#testcase mới 13/02/2025
        def test_001(self):
                """UNCLOSE_STRING"""
                self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: \"VOTIEN", inspect.stack()[0].function))

        def test_002(self):
                """ILLEGAL_ESCAPE"""
                self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: \"VOTIEN\\f", inspect.stack()[0].function))

        def test_003(self):
                """ILLEGAL_ESCAPE"""
                self.assertTrue(TestLexer.test(""" "\\" \\\\ \\q" """, "Illegal escape in string: \"\\\" \\\\ \\q", inspect.stack()[0].function))


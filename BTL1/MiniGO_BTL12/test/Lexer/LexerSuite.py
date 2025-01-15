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
        self.assertTrue(TestLexer.test("0x11","17,<EOF>", inspect.stack()[0].function))

    def test_007(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))

    def test_008(self):
        """Literals String"""
        self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","VOTIEN \\r,<EOF>", inspect.stack()[0].function))

    def test_009(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.test("// VOTIEN\n","<EOF>", inspect.stack()[0].function))

    def test_010(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

    def test_011(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

    def test_012(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: VOTIEN", inspect.stack()[0].function))

    def test_013(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: VOTIEN\\f", inspect.stack()[0].function))


    #testcases của Bằng
    def test_014(self):
        """Test keyword 'if'"""
        self.assertTrue(TestLexer.test("if", "if,<EOF>", inspect.stack()[0].function))

    def test_015(self):
        """Test operator '+'"""
        self.assertTrue(TestLexer.test("+", "+,<EOF>", inspect.stack()[0].function))

    def test_016(self):
        """Test integer literal"""
        self.assertTrue(TestLexer.test("123", "123,<EOF>", inspect.stack()[0].function))

    def test_017(self):
        """Test string literal"""
        self.assertTrue(TestLexer.test('"hello"', "hello,<EOF>", inspect.stack()[0].function))

    def test_018(self):
        """Test unclosed string"""
        self.assertTrue(TestLexer.test('"hello', "Unclosed string: hello", inspect.stack()[0].function))

    def test_019(self):
        """Test illegal escape"""
        self.assertTrue(TestLexer.test('"hello\\x"', "Illegal escape in string: hello\\x", inspect.stack()[0].function))

    def test_020(self):
        """Test line comment"""
        self.assertTrue(TestLexer.test("// this is a comment\n", "<EOF>", inspect.stack()[0].function))

    def test_021(self):
        """Test block comment"""
        self.assertTrue(TestLexer.test("/* this is a comment */", "<EOF>", inspect.stack()[0].function))

    def test_022(self):
        """Test identifier"""
        self.assertTrue(TestLexer.test("_identifier", "_identifier,<EOF>", inspect.stack()[0].function))

    def test_023(self):
        """Test error character"""
        self.assertTrue(TestLexer.test("@", "ErrorToken @", inspect.stack()[0].function))

    #!!! 87 test yêu cầu code chấm sau
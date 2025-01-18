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

    def test_024(self):
        """Test valid integer literals"""
        self.assertTrue(TestLexer.test("123456789", "123456789,<EOF>", inspect.stack()[0].function))

        #hex -> convert qua int
    def test_025(self):
        """Test valid hexadecimal literals"""
        self.assertTrue(TestLexer.test("0x1A3F", "6719,<EOF>", inspect.stack()[0].function))

    def test_026(self):
        """Test valid binary literals"""
        self.assertTrue(TestLexer.test("0b1101", "13,<EOF>", inspect.stack()[0].function))

    def test_027(self):
        """Test valid octal literals"""
        self.assertTrue(TestLexer.test("0o755", "493,<EOF>", inspect.stack()[0].function))

    def test_028(self):
        """Test valid floating-point literals"""
        self.assertTrue(TestLexer.test("123.456e-10", "123.456e-10,<EOF>", inspect.stack()[0].function))

    def test_029(self):
        """Test string literals with escape sequences"""
        self.assertTrue(TestLexer.test('"Hello\\nWorld"', "Hello\\nWorld,<EOF>", inspect.stack()[0].function))

    def test_030(self):
        """Test string literals with valid escapes"""
        self.assertTrue(TestLexer.test('"MiniGo\\tLanguage"', "MiniGo\\tLanguage,<EOF>", inspect.stack()[0].function))

    def test_031(self):
        """Test unclosed string literals"""
        self.assertTrue(TestLexer.test('"Unclosed string', "Unclosed string: Unclosed string", inspect.stack()[0].function))

    def test_032(self):
        """Test illegal escape in string"""
        self.assertTrue(TestLexer.test('"Illegal\\xEscape"', "Illegal escape in string: Illegal\\x", inspect.stack()[0].function))

    def test_033(self):
        """Test single-line comments"""
        self.assertTrue(TestLexer.test("// This is a comment\n", "<EOF>", inspect.stack()[0].function))

    def test_034(self):
        """Test multi-line comments"""
        self.assertTrue(TestLexer.test("/* Comment spanning \n multiple lines */", "<EOF>", inspect.stack()[0].function))

    def test_035(self):
        """Test nested multi-line comments"""
        self.assertTrue(TestLexer.test("/* Outer /* Inner */ Outer */", "<EOF>", inspect.stack()[0].function))

    def test_036(self):
        """Test valid identifiers"""
        self.assertTrue(TestLexer.test("_validIdentifier123", "_validIdentifier123,<EOF>", inspect.stack()[0].function))

    def test_037(self):
        """Test invalid identifiers starting with digits"""
        self.assertTrue(TestLexer.test("123invalid", "123,invalid,<EOF>", inspect.stack()[0].function))

    def test_038(self):
        """Test keywords"""
        self.assertTrue(TestLexer.test("func", "func,<EOF>", inspect.stack()[0].function))

    def test_039(self):
        """Test all operators"""
        self.assertTrue(TestLexer.test("+-*/%&&||!", "+,-,*,/,%,&&,||,!,<EOF>", inspect.stack()[0].function))

    def test_040(self):
        """Test all relational operators"""
        self.assertTrue(TestLexer.test("==!=<><=>=", "==,!=,<,>,<=,>=,<EOF>", inspect.stack()[0].function))

    def test_041(self):
        """Test separators"""
        self.assertTrue(TestLexer.test("(){},;", "(,),{,},,,;,<EOF>", inspect.stack()[0].function))

    def test_042(self):
        """Test array declaration"""
        self.assertTrue(TestLexer.test("[5]int", "[,5,],int,<EOF>", inspect.stack()[0].function))

    def test_043(self):
        """Test struct declaration"""
        self.assertTrue(TestLexer.test("type Person struct { name string; age int; }", "type,Person,struct,{,name,string,;,age,int,;,},<EOF>", inspect.stack()[0].function))

    def test_044(self):
        """Test function declaration"""
        self.assertTrue(TestLexer.test("func add(a int, b int) int { return a + b; }", "func,add,(,a,int,,,b,int,),int,{,return,a,+,b,;,},<EOF>", inspect.stack()[0].function))

    def test_045(self):
        """Test boolean literals"""
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", inspect.stack()[0].function))

    def test_046(self):
        """Test nil literal"""
        self.assertTrue(TestLexer.test("nil", "nil,<EOF>", inspect.stack()[0].function))

    def test_047(self):
        """Test array indexing"""
        self.assertTrue(TestLexer.test("arr[10]", "arr,[,10,],<EOF>", inspect.stack()[0].function))

    def test_048(self):
        """Test dot operator with struct"""
        self.assertTrue(TestLexer.test("person.name", "person,.,name,<EOF>", inspect.stack()[0].function))

    def test_049(self):
        """Test call statement"""
        self.assertTrue(TestLexer.test("foo(10, 20);", "foo,(,10,,,20,),;,<EOF>", inspect.stack()[0].function))

    def test_050(self):
        """Test return statement"""
        self.assertTrue(TestLexer.test("return a + b;", "return,a,+,b,;,<EOF>", inspect.stack()[0].function))

    def test_051(self):
        """Test unclosed string only"""
        self.assertTrue(TestLexer.test("\"Unclosed string", "Unclosed string: Unclosed string", inspect.stack()[0].function))

    def test_052(self):
        """Test multi-line strings"""
        self.assertTrue(TestLexer.test('"This is a multi-line\\nstring."', "This is a multi-line\\nstring.,<EOF>", inspect.stack()[0].function))

    def test_053(self):
        """Test invalid characters"""
        self.assertTrue(TestLexer.test("@#$%", "ErrorToken @", inspect.stack()[0].function))

    def test_054(self):
        """Test mixed valid and invalid tokens"""
        self.assertTrue(TestLexer.test("var x = 10; @", "var,x,=,10,;,ErrorToken @", inspect.stack()[0].function))

    def test_055(self):
        """Test empty program"""
        self.assertTrue(TestLexer.test("", "<EOF>", inspect.stack()[0].function))

    def test_056(self):
        """Test invalid floating-point literals"""
        self.assertTrue(TestLexer.test("1.2.3", "1.2,.3,<EOF>", inspect.stack()[0].function))

    def test_057(self):
        """Test nested array declaration"""
        self.assertTrue(TestLexer.test("[3][5]int", "[,3,],[,5,],int,<EOF>", inspect.stack()[0].function))

    def test_058(self):
        """Test float with exponent"""
        self.assertTrue(TestLexer.test("2e10", "2e10,<EOF>", inspect.stack()[0].function))

    def test_059(self):
        """Test keyword within identifier"""
        self.assertTrue(TestLexer.test("forLoop", "forLoop,<EOF>", inspect.stack()[0].function))

    def test_060(self):
        """Test missing closing bracket"""
        self.assertTrue(TestLexer.test("[3][5]int{1, 2, 3", "[,3,],[,5,],int,{,1,,,2,,,3,<EOF>", inspect.stack()[0].function))

    def test_061(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("0452.", "0,452.,<EOF>", inspect.stack()[0].function))

    def test_062(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("09.e-002", "0,9.e-0,0,2,<EOF>", inspect.stack()[0].function))


    #!!! 87 test yêu cầu code chấm sau
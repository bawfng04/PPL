"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""

import unittest
from TestUtils import TestParser
import inspect

class ParserSuite(unittest.TestCase):
    def test_001(self):
        input = """
            int a = 2;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))

    def test_002(self):
        input = """
            a = a;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))

    def test_003(self):
        input = """
            a, b = a, 1;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))

    def test_004(self):
        input = """
            int a, b = a;
            int a, b;
            a, b = a, 1;
            int a;
            int a,b,c = 1,2;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))

    def test_005(self):
        input = """
            int a = a, b;
        """
        expect = "Error on line 2 col 21: ,"
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))


    def test_006(self):
        input = """
            a = a, b;
        """
        expect = "Error on line 2 col 17: ,"
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))

    def test_007(self):
        input = """
            int a = ;
        """
        expect = "Error on line 2 col 20: ;"
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))

    def test_008(self):
        input = """
            a = 1 + 2 * b / 7 - c ** 3;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))

    def test_009(self):
        input = """
            a = 4 ** 3 ** c;
        """
        expect = "Error on line 2 col 23: **"
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))

    def test_010(self):
        input = """
            a = 4 ** 3 + (4 ** c);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))

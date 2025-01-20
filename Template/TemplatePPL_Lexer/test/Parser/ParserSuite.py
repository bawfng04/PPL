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
        input = """int a = 1;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))
        
    def test_002(self):
        input = """print(1 + 2 + a);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))

    def test_003(self):
        input = """print(a=1);
        """
        expect = "Error on line 1 col 7: ="
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))

    def test_004(self):
        input = """print(a=1);
        """
        expect = "successful="
        self.assertTrue(TestParser.test(input, expect,  inspect.stack()[0].function))
        

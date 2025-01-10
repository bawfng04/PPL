"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 02.01.2025
"""

import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """int a = 1;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
        
    def test_2(self):
        input = """print(1 + 2 + a);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_3(self):
        input = """print(a=1);
        """
        expect = "Error on line 1 col 7: ="
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_4(self):
        input = """print(a=1);
        """
        expect = "successful="
        self.assertTrue(TestParser.test(input, expect, 204))
        

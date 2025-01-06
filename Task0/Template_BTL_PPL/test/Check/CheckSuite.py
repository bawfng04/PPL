"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 02.01.2025
"""
import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_1(self):
        input = """
            int a = 1;
            int a = 2;
        """
        expect = "Redeclared(Variable: a)"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test_2(self):
        input = """
            int a = 1;
            print(a + 2)
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 402))
        
    def test_3(self):
        input = """
            int a = 1;
            print(b + 2)
        """
        expect = "Undeclared(Identifier: b)"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_4(self):
        input = """
            int a = 1;
            print(b + 2)
        """
        expect = "Undeclared(Identifier: a)"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test_5(self):
        input = """
            int a = 1;
            print(b + 2)
        """
        expect1 = "Undeclared(Identifier: a)"
        self.assertTrue(TestChecker.test(input, expect, 404))
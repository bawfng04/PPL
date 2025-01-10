"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 02.01.2025
"""
import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_1(self):
        """test simple"""
        self.assertTrue(TestLexer.test("Votien10cham","Votien10cham,<EOF>",101))

    def test_2(self):
        """test complex"""
        self.assertTrue(TestLexer.test("int Votien = 10 + 10;","int,Votien,=,10,+,10,;,<EOF>",102))

    def test_3(self):
        """test complex error"""
        self.assertTrue(TestLexer.test(".","Error Token .",103))

    def test_4(self):
        """test complex fail1"""
        self.assertTrue(TestLexer.test("int","int,<EOF>",104))

    def test_5(self):
        """test complex fail2"""
        self.assertTrue(TestLexer.test("int","int,<EOF>",105))


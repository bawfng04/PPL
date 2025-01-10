"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 02.01.2025
"""
import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """int a = 1 + b; 
        """
        expect = str(Program([VarDecl('a', IntType(), BinaryOp('+', IntLiteral(1), Id('b')))]))
        self.assertTrue(TestAST.test(input, expect, 300))
        
        
    def test_2(self):
        input = """
            int a = 1;
            print(a)
        """
        expect = str(Program([VarDecl('a', IntType(), IntLiteral(1)), CallStmt('print', Id('a'))]))
        self.assertTrue(TestAST.test(input, expect, 301))
        
    def test_3(self):
        input = """
            int a = 1;
        """
        expect = str(Program([VarDecl('a', IntType(), IntLiteral(2))]))
        self.assertTrue(TestAST.test(input, expect, 302))

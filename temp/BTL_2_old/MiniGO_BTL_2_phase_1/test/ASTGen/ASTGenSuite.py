"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 20.01.2025
"""
import unittest
from TestUtils import TestAST
from AST import *
import inspect

##! continue update
class ASTGenSuite(unittest.TestCase):
    def test_001(self):
        input = """1"""
        expect = str(Program([IntLiteral(1)]))
        self.assertTrue(TestAST.test(input, expect, inspect.stack()[0].function))

    def test_002(self):
        input = """1.0,true,false,nil,\"votien\""""
        expect = str(Program([FloatLiteral(1.0),BooleanLiteral(True),BooleanLiteral(False),NilLiteral(),StringLiteral("votien")]))
        self.assertTrue(TestAST.test(input, expect, inspect.stack()[0].function))

    def test_003(self):
        input = """id"""
        expect = str(Program([Id("id")]))
        self.assertTrue(TestAST.test(input, expect, inspect.stack()[0].function))

    def test_004(self):
        input = """1+2-3&&5--1"""
        expect = str(Program([BinaryOp("&&",BinaryOp("-",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),BinaryOp("-",IntLiteral(5),UnaryOp("-",IntLiteral(1))))]))
        self.assertTrue(TestAST.test(input, expect, inspect.stack()[0].function))

    def test_005(self):
        input = """a > b <= c"""
        expect = str(Program([BinaryOp("<=",BinaryOp(">",Id("a"),Id("b")),Id("c"))]))
        self.assertTrue(TestAST.test(input, expect, inspect.stack()[0].function))

    def test_006(self):
        input = """a[2][3]"""
        expect = str(Program([ArrayCell(ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(3))]))
        self.assertTrue(TestAST.test(input, expect, inspect.stack()[0].function))

    def test_007(self):
        input = """a.b.c"""
        expect = str(Program([FieldAccess(FieldAccess(Id("a"),Id("b")),Id("c"))]))
        self.assertTrue(TestAST.test(input, expect, inspect.stack()[0].function))

    def test_008(self):
        input = """a(),b.a(2, 3)"""
        expect = str(Program([CallExpr(None,Id("a"),[]),CallExpr(Id("b"),Id("a"),[IntLiteral(2),IntLiteral(3)])]))
        self.assertTrue(TestAST.test(input, expect, inspect.stack()[0].function))

    def test_009(self):
        input = """a * (1+2)"""
        expect = str(Program([BinaryOp("*",Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))]))
        self.assertTrue(TestAST.test(input, expect, inspect.stack()[0].function))

    def test_010(self):
        input = """Votien {}, Votien {a: 1}"""
        expect = str(Program([StructLiteral(Id("Votien"), []),StructLiteral(Id("Votien"), [(Id("a"),IntLiteral(1))])]))
        self.assertTrue(TestAST.test(input, expect, inspect.stack()[0].function))

    def test_011(self):
        input = """[1]int{1}, [1][1]int{2}"""
        expect = str(Program([ArrayLiteral(IntType(), [], value=[IntLiteral(1)]),ArrayLiteral(IntType(), [1], value=[IntLiteral(2)])]))
        self.assertTrue(TestAST.test(input, expect, inspect.stack()[0].function))


"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
import unittest
from TestUtils import TestAST
from AST import *
import inspect


##! continue update
class ASTGenSuite(unittest.TestCase):
    def test_001(self):
        input = """const VoTien = 1; """
        expect = ConstDecl("VoTien", None, IntLiteral(1))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_002(self):
        """ chuyển đổi sang kiểu int hết """
        input = """const VoTien = 0b11; """
        expect = ConstDecl("VoTien", None, IntLiteral(3))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_003(self):
        input = """const VoTien = 0o70; """
        expect = ConstDecl("VoTien", None, IntLiteral(56))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_004(self):
        input = """const VoTien = 0Xa1; """
        expect = ConstDecl("VoTien", None, IntLiteral(161))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_005(self):
        input = """const VoTien = 01.e-1; """
        expect = ConstDecl("VoTien", None, FloatLiteral(0.1))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_006(self):
        """ đầu vào là giá trị True False chứ không phải string """
        input = """const VoTien = true; """
        expect = ConstDecl("VoTien", None, BooleanLiteral(True))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_007(self):
        input = """const VoTien = false; """
        expect = ConstDecl("VoTien", None, BooleanLiteral(False))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_008(self):
        """ loại bỏ "" ở trước và sau string """
        input = """const VoTien = "votien"; """
        expect = ConstDecl("VoTien", None, StringLiteral("votien"))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_009(self):
        input = """const VoTien = nil; """
        expect = ConstDecl("VoTien", None, NilLiteral())
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_010(self):
        input = """const VoTien = STRUCT {}; """
        expect = ConstDecl("VoTien", None, StructLiteral("STRUCT",[]))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_011(self):
        input = """const VoTien = STRUCT {
            a : 1,
            b : false}; """
        expect = ConstDecl("VoTien", None, StructLiteral("STRUCT",[("a",IntLiteral(1)),("b",BooleanLiteral(False))]))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_012(self):
        input = """const VoTien = [ID] int {1}; """
        expect = ConstDecl("VoTien", None, ArrayLiteral([Id("ID")],IntType(),[IntLiteral(1)]))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_013(self):
        input = """const VoTien = [1][2] int {1., STRUCT{}, nil}; """
        expect = ConstDecl("VoTien", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],IntType(),[FloatLiteral(1.0),StructLiteral("STRUCT",[]),NilLiteral()]))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_014(self):
        input = """const VoTien = [1][2] STRUCT {{1, {3}}, {2}}; """
        expect = ConstDecl("VoTien", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],Id("STRUCT"),[[IntLiteral(1), [IntLiteral(3)]],[IntLiteral(2)]]))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_015(self):
        input = """const VoTien = 1 || 2 || 3; """
        expect = ConstDecl("VoTien", None, BinaryOp("||", BinaryOp("||", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_016(self):
        input = """const VoTien = 1 && 2 && 3; """
        expect = ConstDecl("VoTien", None, BinaryOp("&&", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_017(self):
        input = """const VoTien = 1 >= 2 <= 3 > 4 < 5 == 6 != 7; """
        expect = ConstDecl("VoTien", None, BinaryOp("!=", BinaryOp("==", BinaryOp("<", BinaryOp(">", BinaryOp("<=", BinaryOp(">=", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)), IntLiteral(7)))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_018(self):
        input = """const VoTien = 1 + 2 - 3; """
        expect = ConstDecl("VoTien", None, BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_019(self):
        input = """const VoTien = 1 * 2 / 3 % 4; """
        expect = ConstDecl("VoTien", None, BinaryOp("%", BinaryOp("/", BinaryOp("*", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_020(self):
        input = """const VoTien = ! - 1; """
        expect = ConstDecl("VoTien", None, UnaryOp("!",UnaryOp("-",IntLiteral(1))))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_021(self):
        input = """const VoTien = a; """
        expect = ConstDecl("VoTien", None, Id("a"))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_022(self):
        input = """const VoTien = (1+2)*3; """
        expect = ConstDecl("VoTien", None, BinaryOp("*", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_023(self):
        input = """const VoTien = foo(); """
        expect = ConstDecl("VoTien", None, FuncCall("foo",[]))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_024(self):
        input = """const VoTien = foo(1, 2); """
        expect = ConstDecl("VoTien", None, FuncCall("foo",[IntLiteral(1),IntLiteral(2)]))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_025(self):
        input = """const VoTien = a[2][3]; """
        expect = ConstDecl("VoTien", None, ArrayCell(ArrayCell(Id("a"),[IntLiteral(2)]),[IntLiteral(3)]))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_026(self):
        input = """const VoTien = a.b.c; """
        expect = ConstDecl("VoTien", None, FieldAccess(FieldAccess(Id("a"),"b"),"c"))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_027(self):
        input = """const VoTien = a.b().c(1, 2); """
        expect = ConstDecl("VoTien", None, MethCall(MethCall(Id("a"),"b",[]),"c",[IntLiteral(1),IntLiteral(2)]))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_028(self):
        input = """const VoTien = a.b[2].c.d(); """
        expect = ConstDecl("VoTien", None, MethCall(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),"d",[]))
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
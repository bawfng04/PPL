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
        expect = Program([ConstDecl("VoTien", None, IntLiteral(1))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_002(self):
        """ chuyển đổi sang kiểu int hết """
        input = """const VoTien = 0b11; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(3))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_003(self):
        input = """const VoTien = 0o70; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(56))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_004(self):
        input = """const VoTien = 0Xa1; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(161))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_005(self):
        input = """const VoTien = 01.e-1; """
        expect = Program([ConstDecl("VoTien", None, FloatLiteral(0.1))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_006(self):
        """ đầu vào là giá trị True False chứ không phải string """
        input = """const VoTien = true; """
        expect = Program([ConstDecl("VoTien", None, BooleanLiteral(True))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_007(self):
        input = """const VoTien = false; """
        expect = Program([ConstDecl("VoTien", None, BooleanLiteral(False))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_008(self):
        """ loại bỏ "" ở trước và sau string """
        input = """const VoTien = "votien"; """
        expect = Program([ConstDecl("VoTien", None, StringLiteral("votien"))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_009(self):
        input = """const VoTien = nil; """
        expect = Program([ConstDecl("VoTien", None, NilLiteral())])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_010(self):
        input = """const VoTien = STRUCT {}; """
        expect = Program([ConstDecl("VoTien", None, StructLiteral("STRUCT",[]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_011(self):
        input = """const VoTien = STRUCT {
            a : 1,
            b : false}; """
        expect = Program([ConstDecl("VoTien", None, StructLiteral("STRUCT",[("a",IntLiteral(1)),("b",BooleanLiteral(False))]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_012(self):
        input = """const VoTien = [ID] int {1}; """
        expect = Program([ConstDecl("VoTien", None, ArrayLiteral([Id("ID")],IntType(),[IntLiteral(1)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_013(self):
        input = """const VoTien = [1][2] int {1., STRUCT{}, nil}; """
        expect = Program([ConstDecl("VoTien", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],IntType(),[FloatLiteral(1.0),StructLiteral("STRUCT",[]),NilLiteral()]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_014(self):
        input = """const VoTien = [1][2] STRUCT {{1, {3}}, {2}}; """
        expect = Program([ConstDecl("VoTien", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],Id("STRUCT"),[[IntLiteral(1), [IntLiteral(3)]],[IntLiteral(2)]]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_015(self):
        input = """const VoTien = 1 || 2 || 3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("||", BinaryOp("||", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_016(self):
        input = """const VoTien = 1 && 2 && 3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("&&", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_017(self):
        input = """const VoTien = 1 >= 2 <= 3 > 4 < 5 == 6 != 7; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("!=", BinaryOp("==", BinaryOp("<", BinaryOp(">", BinaryOp("<=", BinaryOp(">=", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)), IntLiteral(7)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_018(self):
        input = """const VoTien = 1 + 2 - 3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_019(self):
        input = """const VoTien = 1 * 2 / 3 % 4; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("%", BinaryOp("/", BinaryOp("*", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_020(self):
        input = """const VoTien = ! - 1; """
        expect = Program([ConstDecl("VoTien", None, UnaryOp("!",UnaryOp("-",IntLiteral(1))))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_021(self):
        input = """const VoTien = a; """
        expect = Program([ConstDecl("VoTien", None, Id("a"))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_022(self):
        input = """const VoTien = (1+2)*3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("*", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_023(self):
        input = """const VoTien = foo(); """
        expect = Program([ConstDecl("VoTien", None, FuncCall("foo",[]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_024(self):
        input = """const VoTien = foo(1, 2); """
        expect = Program([ConstDecl("VoTien", None, FuncCall("foo",[IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_025(self):
        input = """const VoTien = a[2][3]; """
        expect = Program([ConstDecl("VoTien", None, ArrayCell(ArrayCell(Id("a"),[IntLiteral(2)]),[IntLiteral(3)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_026(self):
        input = """const VoTien = a.b.c; """
        expect = Program([ConstDecl("VoTien", None, FieldAccess(FieldAccess(Id("a"),"b"),"c"))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_027(self):
        input = """const VoTien = a.b().c(1, 2); """
        expect = Program([ConstDecl("VoTien", None, MethCall(MethCall(Id("a"),"b",[]),"c",[IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_028(self):
        input = """const VoTien = a.b[2].c.d(); """
        expect = Program([ConstDecl("VoTien", None, MethCall(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),"d",[]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_029(self):
        input = """
    var a int = 1;
    var a float = 1;
    var a boolean;
    var a string = 1;
    var a = 1;
    var a ID = 1;
    var a [ID][1] int = 1;
"""
        expect = Program([VarDecl("a",IntType(),IntLiteral(1)),
			VarDecl("a",FloatType(),IntLiteral(1)),
			VarDecl("a",BoolType(), None),
			VarDecl("a",StringType(),IntLiteral(1)),
			VarDecl("a", None,IntLiteral(1)),
			VarDecl("a",Id("ID"),IntLiteral(1)),
			VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_030(self):
        input = """
    const a = 1;
"""
        expect = Program([ConstDecl("a",None,IntLiteral(1))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_031(self):
        input = """
    type ID struct {
        a int;
        b ID;
        c [2]int;
    }
"""
        expect = Program([StructType("ID",[("a",IntType()),("b",Id("ID")),("c",ArrayType([IntLiteral(2)],IntType()))],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_032(self):
        input = """
    func foo () {var a = 1;}
    func foo () int {var a = 1;}
    func foo () [2] ID {var a = 1;}
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_033(self):
        input = """
    func foo (a int) {var a = 1;}
    func foo (a int, b ID) {var a = 1;}
    func foo (a, b int) {var a = 1;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_034(self):
        input = """
    func (ID ID) foo () {var a = 1;}
    func (ID ID) foo () int {var a = 1;}
    func (ID ID) foo () [2] ID {var a = 1;}
"""
        expect = Program([MethodDecl("ID",Id("ID"),FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_035(self):
        input = """
    func (ID ID) foo (a int) {var a = 1;}
    func (ID ID) foo (a int, b ID) {var a = 1;}
    func (ID ID) foo (a, b int) {var a = 1;}
"""
        expect = Program([MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_036(self):
        input = """
        type INTERFACE interface {
            foo();
            foo() int;
            foo() [2]ID;
            foo(a int);
            foo(a int, b int);
            foo(a, b int);
        }
"""
        expect = Program([InterfaceType("INTERFACE",[
            Prototype("foo",[],VoidType()),Prototype("foo",[],IntType()),
            Prototype("foo",[],ArrayType([IntLiteral(2)],Id("ID"))),
            Prototype("foo",[IntType()],VoidType()),
            Prototype("foo",[IntType(),IntType()],VoidType()),
            Prototype("foo",[IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


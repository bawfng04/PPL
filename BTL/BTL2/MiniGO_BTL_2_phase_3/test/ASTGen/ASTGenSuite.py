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
        input = """const VoTien = foo( 1 ); """
        expect = Program([ConstDecl(Id("VoTien"),CallExpr(None,Id("foo"),[IntLiteral(1)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_002(self):
        input = """const VoTien = foo( 1.0,true,false,nil,\"votien\" ); """
        expect = Program([ConstDecl(Id("VoTien"),CallExpr(None,Id("foo"),[FloatLiteral(1.0),BooleanLiteral(True),BooleanLiteral(False),NilLiteral(),StringLiteral("votien")]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_003(self):
        input = """const VoTien = foo( id ); """
        expect = Program([ConstDecl(Id("VoTien"),CallExpr(None,Id("foo"),[Id("id")]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_004(self):
        input = """const VoTien = foo( 1+2-3&&5--1 ); """
        expect = Program([ConstDecl(Id("VoTien"),CallExpr(None,Id("foo"),[BinaryOp("&&",BinaryOp("-",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),BinaryOp("-",IntLiteral(5),UnaryOp("-",IntLiteral(1))))]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_005(self):
        input = """const VoTien = foo( a > b <= c ); """
        expect = Program([ConstDecl(Id("VoTien"),CallExpr(None,Id("foo"),[BinaryOp("<=",BinaryOp(">",Id("a"),Id("b")),Id("c"))]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_006(self):
        input = """const VoTien = foo( a[2][3] ); """
        expect = Program([ConstDecl(Id("VoTien"),CallExpr(None,Id("foo"),[ArrayCell(ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(3))]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_007(self):
        input = """const VoTien = foo( a.b.c ); """
        expect = Program([ConstDecl(Id("VoTien"),CallExpr(None,Id("foo"),[FieldAccess(FieldAccess(Id("a"),Id("b")),Id("c"))]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_008(self):
        input = """const VoTien = foo( a(),b.a(2, 3) ); """
        expect = Program([ConstDecl(Id("VoTien"),CallExpr(None,Id("foo"),[CallExpr(None,Id("a"),[]),CallExpr(Id("b"),Id("a"),[IntLiteral(2),IntLiteral(3)])]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_009(self):
        input = """const VoTien = foo( a * (1+2) ); """
        expect = Program([ConstDecl(Id("VoTien"),CallExpr(None,Id("foo"),[BinaryOp("*",Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_010(self):
        input = """const VoTien = foo( Votien {}, Votien {a: 1} ); """
        expect = Program([ConstDecl(Id("VoTien"),CallExpr(None,Id("foo"),[StructLiteral(Id("Votien"), []),StructLiteral(Id("Votien"), [(Id("a"),IntLiteral(1))])]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_011(self):
        input = """const VoTien = foo( [1]int{1}, [1][1]int{2} ); """
        expect = Program([ConstDecl(Id("VoTien"),CallExpr(None,Id("foo"),[ArrayLiteral(IntType(), [], value=[IntLiteral(1)]),ArrayLiteral(IntType(), [1], value=[IntLiteral(2)])]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_012(self):
        input = """
            var Votien = 1;
            var Votien int;
            var Votine int = 1;
"""
        expect = Program([
			VariablesDecl(Id("Votien"), None, IntLiteral(1)),
			VariablesDecl(Id("Votien"), IntType(), None),
			VariablesDecl(Id("Votine"), IntType(), IntLiteral(1))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_013(self):
        input = """
            func foo() int {}
            func foo(a int, b int) {}
"""
        expect = Program([
			FunctionDecl(Id("foo"), IntType(), None,[], []),
			FunctionDecl(Id("foo"), VoidType(), None,[VariablesDecl(Id("a"), IntType(), None), VariablesDecl(Id("b"), IntType(), None)], [])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_014(self):
        input = """
            func (Votien v) foo(Votien int) {}
"""
        expect = Program([
			FunctionDecl(Id("foo"), VoidType(), VariablesDecl(Id("Votien"), ClassType(Id("v")), None),[VariablesDecl(Id("Votien"), IntType(), None)], [])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_015(self):
        input = """
            type Votien struct {
                a int;
            }
"""
        expect = Program([
			StructDecl(Id("Votien"),[VariablesDecl(Id("a"), IntType(), None)])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_016(self):
        input = """
            type Votien struct {
                a int;
            }
"""
        expect = Program([
			StructDecl(Id("Votien"),[VariablesDecl(Id("a"), IntType(), None)])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_017(self):
        input = """
            type Votien interface {
                Add(x, y int) int;
            }
"""
        expect = Program([
			InterfaceDecl(Id("Votien"),[FunctionDecl(Id("Add"), IntType(), None,[VariablesDecl(Id("x"), IntType(), None),VariablesDecl(Id("y"), IntType(), None)], [])])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_018(self):
        input = """
            func votien() {
                var a int;
                const a = nil;
            }
"""
        expect = Program([
			FunctionDecl(Id("votien"), VoidType(), None,[],[
				VariablesDecl(Id("a"), IntType(), None),
				ConstDecl(Id("a"),NilLiteral())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_019(self):
        input = """
            func votien() {
                a += 1;
            }
"""
        expect = Program([
			FunctionDecl(Id("votien"), VoidType(), None,[],[
				AssignStmt(Id("a"),"+=",IntLiteral(1))])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_020(self):
        input = """
            func votien() {
                break;
                continue;
            }
"""
        expect = Program([
			FunctionDecl(Id("votien"), VoidType(), None,[],[
				Break(),
                Continue()])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_021(self):
        input = """
            func votien() {
                if(1) {}
            }
"""
        expect = Program([
			FunctionDecl(Id("votien"), VoidType(), None,[],[
				If(IntLiteral(1), [], None, None)])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_022(self):
        input = """
            func votien() {
                if(1) {
                    a := 1;
                }
                else {
                    a := 1;
                }
            }
"""
        expect = Program([
			FunctionDecl(Id("votien"), VoidType(), None,[],[
				If(IntLiteral(1), [AssignStmt(Id("a"),":=",IntLiteral(1))], None, [AssignStmt(Id("a"),":=",IntLiteral(1))])])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_023(self):
        input = """
            func votien() {
                if(1) {
                }else if(1) {
                    a := 1;
                }else if(2) {
                }
            }
"""
        expect = Program([
			FunctionDecl(Id("votien"), VoidType(), None,[],[
				If(IntLiteral(1), [], [
                    (IntLiteral(1),[AssignStmt(Id("a"),":=",IntLiteral(1))]),
                    (IntLiteral(2),[])]
                    , None)])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_024(self):
        input = """
            func votien() {
                for i < 10 {}
                for var i = 0; i < 10; i += 1  {}
            }
"""
        expect = Program([
			FunctionDecl(Id("votien"), VoidType(), None,[],[
				For(None,BinaryOp("<",Id("i"),IntLiteral(10)),None,[]),
				For(VariablesDecl(Id("i"), None, IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),AssignStmt(Id("i"),"+=",IntLiteral(1)),[])])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_025(self):
        input = """
            func votien() {
                for index, value := range array[2] {}
            }
"""
        expect = Program([
			FunctionDecl(Id("votien"), VoidType(), None,[],[
				For(Id("index"),Id("value"),ArrayCell(Id("array"),IntLiteral(2)),[])])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_026(self):
        input = """
            func votien() {
                foo(1, 2);
                a[2].foo(1,3);
            }
"""
        expect = Program([
			FunctionDecl(Id("votien"), VoidType(), None,[],[
				CallStmt(None,Id("foo"),[IntLiteral(1),IntLiteral(2)]),
				CallStmt(ArrayCell(Id("a"),IntLiteral(2)),Id("foo"),[IntLiteral(1),IntLiteral(3)])])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
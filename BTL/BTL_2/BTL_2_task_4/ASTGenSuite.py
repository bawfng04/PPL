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

"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
import sys
from antlr4 import *
import unittest
import inspect
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_001(self):
        input = """const VoTien = foo( 1 ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[IntLiteral(1)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_002(self):
        input = """const VoTien = foo( 1.0,true,false,nil,\"votien\" ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[FloatLiteral(1.0),BooleanLiteral(True),BooleanLiteral(False),NilLiteral(),StringLiteral("votien")]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_003(self):
        input = """const VoTien = foo( id ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[Id("id")]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_004(self):
        input = """const VoTien = foo( 1+2-3&&5--1 ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[BinaryOp("&&", BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), BinaryOp("-", IntLiteral(5), UnaryOp("-",IntLiteral(1))))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_005(self):
        input = """const VoTien = foo( a > b <= c ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[BinaryOp("<=", BinaryOp(">", Id("a"), Id("b")), Id("c"))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_006(self):
        input = """const VoTien = foo( a[2][3] ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[ArrayCell(ArrayCell(Id("a"),[IntLiteral(2)]),[IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_007(self):
        input = """const VoTien = foo( a.b.c ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[FieldAccess(FieldAccess(Id("a"),"b"),"c")]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_008(self):
        input = """const VoTien = foo( a(),b.a(2, 3) ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[FuncCall("a",[]),MethCall(Id("b"),"a",[IntLiteral(2),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_009(self):
        input = """const VoTien = foo( a * (1+2) ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[BinaryOp("*", Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_010(self):
        input = """const VoTien = foo( Votien {}, Votien {a: 1} ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[StructLiteral("Votien",[]),StructLiteral("Votien",[("a",IntLiteral(1))])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_011(self):
        input = """const VoTien = foo( [1]int{1}, [1][1]int{2} ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]),ArrayLiteral([IntLiteral(1),IntLiteral(1)],IntType(),[IntLiteral(2)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_012(self):
        input = """
            var Votien = 1;
            var Votien int;
            var Votine int = 1;
"""
        expect = Program([VarDecl("Votien", None,IntLiteral(1)),
			VarDecl("Votien",IntType(), None),
			VarDecl("Votine",IntType(),IntLiteral(1))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_013(self):
        input = """
            func foo() int {return;}
            func foo(a int, b int) {return;}
"""
        expect = Program([FuncDecl("foo",[],IntType(),Block([Return(None)])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_014(self):
        input = """
            func (Votien v) foo(Votien int) {return;}
"""
        expect = Program([MethodDecl("Votien",Id("v"),FuncDecl("foo",[ParamDecl("Votien",IntType())],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_015(self):
        input = """
            type Votien struct {
                a int;
            }
"""
        expect = Program([StructType("Votien",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_016(self):
        input = """
            type Votien struct {
                a int;
            }
"""
        expect = Program([StructType("Votien",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_017(self):
        input = """
            type Votien interface {
                Add(x, y int) int;
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([VarDecl("a",IntType(), None),ConstDecl("a",None,NilLiteral())]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_017(self):
        input = """
            func votien() {
                var a int;
                const a = nil;
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([VarDecl("a",IntType(), None),ConstDecl("a",None,NilLiteral())]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_018(self):
        input = """
            func votien() {
                a += 1;
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_019(self):
        input = """
            func votien() {
                break;
                continue;
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([Break(),Continue()]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_020(self):
        input = """
            func votien() {
                foo(1, 2);
                a[2].foo(1,3);
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([FuncCall("foo",[IntLiteral(1),IntLiteral(2)]),MethCall(ArrayCell(Id("a"),[IntLiteral(2)]),"foo",[IntLiteral(1),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_021(self):
        input = """
            func votien() {
                if(1) {return;}
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([If(IntLiteral(1), Block([Return(None)]), None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_022(self):
        input = """
            func votien() {
                if(1) {
                    a := 1;
                } else {
                    a := 1;
                }
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([If(IntLiteral(1), Block([Assign(Id("a"),IntLiteral(1))]), Block([Assign(Id("a"),IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_023(self):
        input = """
            func votien() {
                if(1) { return;
                }else if(1) {
                    a := 1;
                }else if(2) {
                    a := 1;
                }
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]),
                If(IntLiteral(1), Block([Assign(Id("a"),IntLiteral(1))]),
                    If(IntLiteral(2), Block([Assign(Id("a"),IntLiteral(1))]), None)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_024(self):
        input = """
            func votien() {
                for i < 10 {return;}
                for var i = 0; i < 10; i += 1  {return;}
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)),Block([Return(None)])),ForStep(VarDecl("i", None,IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_025(self):
        input = """
            func votien() {
                for index, value := range array[2] {return;}
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayCell(Id("array"),[IntLiteral(2)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_026(self):
        input = """
            const a = true + false - true;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", BooleanLiteral(True), BooleanLiteral(False)), BooleanLiteral(True)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_027(self):
        input = """
            const a = 1 && 2 || 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_028(self):
        input = """
            const a = 1 + 2 && 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("&&", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_029(self):
        input = """
            const a = 1 - 2 % 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", IntLiteral(1), BinaryOp("%", IntLiteral(2), IntLiteral(3))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_030(self):
        input = """
            const a = 1 + -2 - 1;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", IntLiteral(1), UnaryOp("-",IntLiteral(2))), IntLiteral(1)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_031(self):
        input = """
            const a = [1]ID{Votien{}};
"""
        expect = Program([ConstDecl("a",None,ArrayLiteral([IntLiteral(1)],Id("ID"),[StructLiteral("Votien",[])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_032(self):
        input = """
            const a = [1][3]float{1.};
"""
        expect = Program([ConstDecl("a",None,ArrayLiteral([IntLiteral(1),IntLiteral(3)],FloatType(),[FloatLiteral(1.0)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_033(self):
        input = """
            const a = ID{a: 1, b: true};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("a",IntLiteral(1)),("b",BooleanLiteral(True))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_034(self):
        input = """
            const a = ID{a: [1]int{1}};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("a",ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_035(self):
        input = """
            const a = ID{b: true};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("b",BooleanLiteral(True))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_036(self):
        input = """
            const a = 0 && 1 && 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("&&", BinaryOp("&&", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_037(self):
        input = """
            const a = 0 || 1 || 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("||", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_038(self):
        input = """
            const a = 0 >= 1 <= 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("<=", BinaryOp(">=", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_039(self):
        input = """
            const a = 0 + 1 - 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_040(self):
        input = """
            const a = 0 * 1 / 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("/", BinaryOp("*", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_041(self):
        input = """
            const a = !-!2;
"""
        expect = Program([ConstDecl("a",None,UnaryOp("!",UnaryOp("-",UnaryOp("!",IntLiteral(2)))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_042(self):
        input = """
            const a = 1 && 2 || 3 >= 4 + 5 * -6;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), BinaryOp(">=", IntLiteral(3), BinaryOp("+", IntLiteral(4), BinaryOp("*", IntLiteral(5), UnaryOp("-",IntLiteral(6)))))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_043(self):
        input = """
            const a = 1 > 2 < 3 >= 4 <=5 == 6;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("==", BinaryOp("<=", BinaryOp(">=", BinaryOp("<", BinaryOp(">", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_044(self):
        input = """
            const a = 1 >= 2 + 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp(">=", IntLiteral(1), BinaryOp("+", IntLiteral(2), IntLiteral(3))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_045(self):
        input = """
            const a = a[1][2][3][4];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(ArrayCell(ArrayCell(ArrayCell(Id("a"),[IntLiteral(1)]),[IntLiteral(2)]),[IntLiteral(3)]),[IntLiteral(4)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_046(self):
        input = """
            const a = a[1 + 2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_047(self):
        input = """
            const a = a.b.c.d.e;
"""
        expect = Program([ConstDecl("a",None,FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_048(self):
        input = """
            const a = ID {}.a;
"""
        expect = Program([ConstDecl("a",None,FieldAccess(StructLiteral("ID",[]),"a"))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_049(self):
        input = """
            const a = ID {}.a[2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(FieldAccess(StructLiteral("ID",[]),"a"),[IntLiteral(2)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_050(self):
        input = """
            const a = a.b().c().d();
"""
        expect = Program([ConstDecl("a",None,MethCall(MethCall(MethCall(Id("a"),"b",[]),"c",[]),"d",[]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_051(self):
        input = """
            const a = a().d();
"""
        expect = Program([ConstDecl("a",None,MethCall(FuncCall("a",[]),"d",[]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_052(self):
        input = """
            const a = a[1].b.c()[2].d.e();
"""
        expect = Program([ConstDecl("a",None,MethCall(FieldAccess(ArrayCell(MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1)]),"b"),"c",[]),[IntLiteral(2)]),"d"),"e",[]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_053(self):
        input = """
            const a = a * (nil - "a");
"""
        expect = Program([ConstDecl("a",None,BinaryOp("*", Id("a"), BinaryOp("-", NilLiteral(), StringLiteral("a"))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_054(self):
        input = """
            const a = f() + f(1 + 2, 3.);
"""
        expect = Program([ConstDecl("a",None,BinaryOp("+", FuncCall("f",[]), FuncCall("f",[BinaryOp("+", IntLiteral(1), IntLiteral(2)),FloatLiteral(3.0)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_055(self):
        input = """
            const a = foo()[2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(FuncCall("foo",[]),[IntLiteral(2)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_056(self):
        input = """
            const a = a;
"""
        expect = Program([ConstDecl("a",None,Id("a"))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_057(self):
        input = """
            var a Votien = 1.;
"""
        expect = Program([VarDecl("a",Id("Votien"),FloatLiteral(1.0))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_058(self):
        "thêm type array vào AST anh có thông bao trong nhóm task 3"
        input = """
            var a [2][3]int;
"""
        expect = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None)
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_059(self):
        input = """
            var a = 1;
"""
        expect = Program([VarDecl("a", None,IntLiteral(1))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_060(self):
        input = """
            type Votien struct {
                a int;
            }
"""
        expect = Program([StructType("Votien",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_061(self):
        input = """
            type Votien struct {
                a int;
            }
"""
        expect = Program([StructType("Votien",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_062(self):
        input = """
            type Votien struct {
                a  int;
                b  boolean;

            }
"""
        expect = Program([StructType("Votien",[("a",IntType()),("b",BoolType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_063(self):
        input = """
            type Votien struct {
                a  int;
                b  boolean;
                c  [2]Votien;
            }
"""
        expect = Program([StructType("Votien",[("a",IntType()),("b",BoolType()),("c",ArrayType([IntLiteral(2)],Id("Votien")))],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_064(self):
        input = """
            type Votien interface {
                Add() ;
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_065(self):
        input = """
            type Votien interface {
                Add(a int) ;
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[IntType()],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_066(self):
        input = """
            type Votien interface {
                Add(a int, b int) ;
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_067(self):
        input = """
            type Votien interface {
                Add(a, c int, b int) ;
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[IntType(),IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_068(self):
        input = """
            type Votien interface {
                Add(a, c int, b int) [2]string;
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[IntType(),IntType(),IntType()],ArrayType([IntLiteral(2)],StringType()))])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_069(self):
        input = """
            type Votien interface {
                Add() [2]string;
                Add() ID;
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[],ArrayType([IntLiteral(2)],StringType())),Prototype("Add",[],Id("ID"))])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_070(self):
        input = """
            type Votien interface {
                Add();
            }
"""
        expect = Program([InterfaceType("Votien",[Prototype("Add",[],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_071(self):
        input = """
            func foo() {return;}
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_072(self):
        input = """
            func foo(a [2]ID) {return;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],Id("ID")))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_073(self):
        input = """
            func foo(a int, b [1]int) {return;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",ArrayType([IntLiteral(1)],IntType()))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_074(self):
        input = """
            func foo() [2]int {return;}
"""
        expect = Program([FuncDecl("foo",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_075(self):
        input = """
            func (Cat c) foo() {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_076(self):
        input = """
            func  (Cat c) foo(a [2]ID) {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],Id("ID")))],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_077(self):
        input = """
            func  (Cat c) foo(a int, b [1]int) {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",ArrayType([IntLiteral(1)],IntType()))],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_078(self):
        input = """
            func  (Cat c) foo() [2]int {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_079(self):
        input = """
            var a = 1;
            const b = 2;
            type a struct{a float;}
            type b interface {foo();}
            func foo(){return;}
            func  (Cat c) foo() [2]int {return;}
"""
        expect = Program([VarDecl("a", None,IntLiteral(1)),
			ConstDecl("b",None,IntLiteral(2)),
			StructType("a",[("a",FloatType())],[]),
			InterfaceType("b",[Prototype("foo",[],VoidType())]),
			FuncDecl("foo",[],VoidType(),Block([Return(None)])),
			MethodDecl("Cat",Id("c"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_080(self):
        input = """
            func foo(a,b,c,d [ID][2][c] ID ){return;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("b",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("c",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("d",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID")))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_081(self):
        input = """
            func foo(){
                const a = 1.;
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,FloatLiteral(1.0))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_082(self):
        input = """
            func foo(){
                var a = 1.;
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,FloatLiteral(1.0))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_083(self):
        input = """
            func foo(){
                var a [1]int = 1;
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",ArrayType([IntLiteral(1)],IntType()),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_084(self):
        input = """
            func foo(){
                var a int;
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(), None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_085(self):
        input = """
            func foo(){
                a += 1;
                a -= 1;
                a *= 1;
                a /= 1;
                a %= 1;
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_086(self):
        input = """
            func foo(){
                a[1 + 1] := 1;
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(1))]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_087(self):
        input = """
            func foo(){
                a[2].b.c[2] := 1;
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b"),"c"),[IntLiteral(2)]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_088(self):
        input = """
            func foo(){
                a["s"][foo()] := 1;
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(ArrayCell(Id("a"),[StringLiteral("s")]),[FuncCall("foo",[])]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_089(self):
        input = """
            func foo(){
                a.b := 1;
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(Id("a"),"b"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_090(self):
        input = """
            func foo(){
                a.b[2].c := 1;
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_091(self):
        input = """
            func foo(){
                break;
                continue;
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Break(),Continue()]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_092(self):
        input = """
            func foo(){
                return;
                return foo() + 2;
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(None),Return(BinaryOp("+", FuncCall("foo",[]), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_093(self):
        input = """
            func foo(){
                foo();
                foo(foo(), 2);
                a.foo();
                a[2].c.foo(foo(), 2);
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("foo",[]),FuncCall("foo",[FuncCall("foo",[]),IntLiteral(2)]),MethCall(Id("a"),"foo",[]),MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"c"),"foo",[FuncCall("foo",[]),IntLiteral(2)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_094(self):
        input = """
            func foo(){
                if(1) {return;}
                if(1 + 1) {
                    return 1;
                    return;
                }
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), None),
            If(BinaryOp("+", IntLiteral(1), IntLiteral(1)), Block([Return(IntLiteral(1)),Return(None)]), None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_095(self):
        input = """
            func foo(){
                if(1) { return;
                }else if(1) {
                    return 1;
                    return ;
                } else {return;}

                if(1) {return;
                }  else {
                    return 1;
                    return ;
                }

            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]),
                If(IntLiteral(1), Block([Return(IntLiteral(1)),Return(None)]), Block([Return(None)]))),
            If(IntLiteral(1), Block([Return(None)]), Block([Return(IntLiteral(1)),Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_096(self):
        input = """
            func foo(){
                if(1) {
                    return 1;
                }else if(2) {
                    return 2;
                } else if(3) {
                    return 3;
                } else if(4) {
                    return 4;
                }

            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(IntLiteral(1))]),
                If(IntLiteral(2), Block([Return(IntLiteral(2))]),
                    If(IntLiteral(3), Block([Return(IntLiteral(3))]),
                        If(IntLiteral(4), Block([Return(IntLiteral(4))]), None))))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_097(self):
        input = """
            func votien() {
                for a.i[8] {
                    return;
                    return 1;
                }
                for i := 0; i[1] < 10; i *= 2+3  {
                    return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([ForBasic(ArrayCell(FieldAccess(Id("a"),"i"),[IntLiteral(8)]),Block([Return(None),Return(IntLiteral(1))])),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", ArrayCell(Id("i"),[IntLiteral(1)]), IntLiteral(10)),Assign(Id("i"),BinaryOp("*", Id("i"), BinaryOp("+", IntLiteral(2), IntLiteral(3)))),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_098(self):
        input = """
            func votien() {
                for index, value := range [2]int{1,2} {
                     return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_099(self):
        input = """
            func votien() {
                a.b.c[2].d()
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([MethCall(ArrayCell(FieldAccess(FieldAccess(Id("a"),"b"),"c"),[IntLiteral(2)]),"d",[])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_100(self):
        input = """
            func votien() {
                return [2] ID { {1}, {"2"}, {nil}, {struc{}} };
                return "THANKS YOU, PPL1 ";
            };
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([Return(ArrayLiteral([IntLiteral(2)],Id("ID"),[[IntLiteral(1)],[StringLiteral("2")],[NilLiteral()],[StructLiteral("struc",[])]])),Return(StringLiteral("THANKS YOU, PPL1 "))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_101(self):  # was test_001
        input = """const VoTien = 1; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(1))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_102(self):  # was test_002
        """ chuyển đổi sang kiểu int hết """
        input = """const VoTien = 0b11; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(3))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_103(self):  # was test_003
        input = """const VoTien = 0o70; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(56))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_104(self):  # was test_004
        input = """const VoTien = 0Xa1; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(161))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_105(self):  # was test_005
        input = """const VoTien = 01.e-1; """
        expect = Program([ConstDecl("VoTien", None, FloatLiteral(0.1))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_106(self):  # was test_006
        """ đầu vào là giá trị True False chứ không phải string """
        input = """const VoTien = true; """
        expect = Program([ConstDecl("VoTien", None, BooleanLiteral(True))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_107(self):  # was test_007
        input = """const VoTien = false; """
        expect = Program([ConstDecl("VoTien", None, BooleanLiteral(False))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_108(self):  # was test_008
        """ loại bỏ "" ở trước và sau string """
        input = """const VoTien = "votien"; """
        expect = Program([ConstDecl("VoTien", None, StringLiteral("votien"))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_109(self):  # was test_009
        input = """const VoTien = nil; """
        expect = Program([ConstDecl("VoTien", None, NilLiteral())])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_110(self):  # was test_010
        input = """const VoTien = STRUCT {}; """
        expect = Program([ConstDecl("VoTien", None, StructLiteral("STRUCT",[]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_111(self):  # was test_011
        input = """const VoTien = STRUCT {
            a : 1,
            b : false}; """
        expect = Program([ConstDecl("VoTien", None, StructLiteral("STRUCT",[("a",IntLiteral(1)),("b",BooleanLiteral(False))]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_112(self):  # was test_012
        input = """const VoTien = [ID] int {1}; """
        expect = Program([ConstDecl("VoTien", None, ArrayLiteral([Id("ID")],IntType(),[IntLiteral(1)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_113(self):  # was test_013
        input = """const VoTien = [1][2] int {1., STRUCT{}, nil}; """
        expect = Program([ConstDecl("VoTien", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],IntType(),[FloatLiteral(1.0),StructLiteral("STRUCT",[]),NilLiteral()]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_114(self):  # was test_014
        input = """const VoTien = [1][2] STRUCT {{1, {3}}, {2}}; """
        expect = Program([ConstDecl("VoTien", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],Id("STRUCT"),[[IntLiteral(1), [IntLiteral(3)]],[IntLiteral(2)]]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_115(self):  # was test_015
        input = """const VoTien = 1 || 2 || 3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("||", BinaryOp("||", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_116(self):  # was test_016
        input = """const VoTien = 1 && 2 && 3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("&&", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_117(self):  # was test_017
        input = """const VoTien = 1 >= 2 <= 3 > 4 < 5 == 6 != 7; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("!=", BinaryOp("==", BinaryOp("<", BinaryOp(">", BinaryOp("<=", BinaryOp(">=", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)), IntLiteral(7)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_118(self):  # was test_018
        input = """const VoTien = 1 + 2 - 3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_119(self):  # was test_019
        input = """const VoTien = 1 * 2 / 3 % 4; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("%", BinaryOp("/", BinaryOp("*", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_120(self):  # was test_020
        input = """const VoTien = ! - 1; """
        expect = Program([ConstDecl("VoTien", None, UnaryOp("!",UnaryOp("-",IntLiteral(1))))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_121(self):  # was test_021
        input = """const VoTien = a; """
        expect = Program([ConstDecl("VoTien", None, Id("a"))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_122(self):  # was test_022
        input = """const VoTien = (1+2)*3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("*", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_123(self):  # was test_023
        input = """const VoTien = foo(); """
        expect = Program([ConstDecl("VoTien", None, FuncCall("foo",[]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_124(self):  # was test_024
        input = """const VoTien = foo(1, 2); """
        expect = Program([ConstDecl("VoTien", None, FuncCall("foo",[IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_125(self):  # was test_025
        input = """const VoTien = a[2][3]; """
        expect = Program([ConstDecl("VoTien", None, ArrayCell(ArrayCell(Id("a"),[IntLiteral(2)]),[IntLiteral(3)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_126(self):  # was test_026
        input = """const VoTien = a.b.c; """
        expect = Program([ConstDecl("VoTien", None, FieldAccess(FieldAccess(Id("a"),"b"),"c"))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_127(self):  # was test_027
        input = """const VoTien = a.b().c(1, 2); """
        expect = Program([ConstDecl("VoTien", None, MethCall(MethCall(Id("a"),"b",[]),"c",[IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_128(self):  # was test_028
        input = """const VoTien = a.b[2].c.d(); """
        expect = Program([ConstDecl("VoTien", None, MethCall(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),"d",[]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_129(self):  # was test_029
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


    def test_130(self):  # was test_030
        input = """
    const a = 1;
"""
        expect = Program([ConstDecl("a",None,IntLiteral(1))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_131(self):  # was test_031
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

    def test_132(self):  # was test_032
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

    def test_133(self):  # was test_033
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


    def test_134(self):  # was test_033
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

    def test_135(self):  # was test_034
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

    def test_136(self):  # was test_035
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

    def test_137(self):  # was test_036
        input = """
    func foo () {
        continue;
        break;
        return;
        return 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Continue(),Break(),Return(None),Return(IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_138(self):  # was test_037
        input = """
    func foo () {
        var a int = 1;
        var a float = 1;
        var a boolean;
        var a string = 1;
        var a = 1;
        var a ID = 1;
        var a [ID][1] int = 1;
        const a = 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            VarDecl("a",IntType(),IntLiteral(1)),
            VarDecl("a",FloatType(),IntLiteral(1)),
            VarDecl("a",BoolType(), None),
            VarDecl("a",StringType(),IntLiteral(1)),
            VarDecl("a", None,IntLiteral(1)),
            VarDecl("a",Id("ID"),IntLiteral(1)),
            VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1)),
            ConstDecl("a",None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_139(self):  # was test_038
        input = """
    func foo () {
        var a int = 1;
        var a float = 1;
        var a boolean;
        var a string = 1;
        var a = 1;
        var a ID = 1;
        var a [ID][1] int = 1;
        const a = 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            VarDecl("a",IntType(),IntLiteral(1)),
            VarDecl("a",FloatType(),IntLiteral(1)),
            VarDecl("a",BoolType(), None),
            VarDecl("a",StringType(),IntLiteral(1)),
            VarDecl("a", None,IntLiteral(1)),
            VarDecl("a",Id("ID"),IntLiteral(1)),
            VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1)),
            ConstDecl("a",None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_140(self):  # was test_039
        input = """
    func foo () {
        a := 1;
        a += 1;
        a -= 1;
        a *= 1;
        a /= 1;
        a %= 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(Id("a"),IntLiteral(1)),
            Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_141(self):  # was test_040
        input = """
    func foo () {
        a[1] := 2;
        a[2][1+1] += 3;
        a.b -= 5;
        b.b[a + b].b.c[2] := 4;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[IntLiteral(1)]),IntLiteral(2)),
            Assign(ArrayCell(ArrayCell(Id("a"),[IntLiteral(2)]),[BinaryOp("+", IntLiteral(1), IntLiteral(1))]),BinaryOp("+", ArrayCell(ArrayCell(Id("a"),[IntLiteral(2)]),[BinaryOp("+", IntLiteral(1), IntLiteral(1))]), IntLiteral(3))),
            Assign(FieldAccess(Id("a"),"b"),BinaryOp("-", FieldAccess(Id("a"),"b"), IntLiteral(5))),
            Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(FieldAccess(Id("b"),"b"),[BinaryOp("+", Id("a"), Id("b"))]),"b"),"c"),[IntLiteral(2)]),IntLiteral(4))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_142(self):  # was test_041
        input = """
    func foo () {
        a();
        a(1, 2);
        a(1);
        b.a.a();
        b.a.a(1, 2);
        b.a.a(1);
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            FuncCall("a",[]),
            FuncCall("a",[IntLiteral(1),IntLiteral(2)]),
            FuncCall("a",[IntLiteral(1)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1),IntLiteral(2)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_143(self):  # was test_042
        input = """
        func foo () {
            if (a) {return;}
            if (b) {return;} else {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(Id("a"),Block([Return(None)]), None),
            If(Id("b"),Block([Return(None)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_144(self):  # was test_043
        input = """
        func foo () {
            for(1) {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_145(self):  # was test_044
        input = """
        func foo () {
            for a, b := range 2 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_146(self):  # was test_045
        input = """
        func foo () {
            for a, b := range 2 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_147(self):  # was test_047
        input = """
        func foo () {
            if (1){return;} else if (2){return;} else if (3){return;} else {return;}
            if (1){return;} else if (2){return;} else if (3){return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]),
               If(IntLiteral(2), Block([Return(None)]),
                  If(IntLiteral(3), Block([Return(None)]), Block([Return(None)])))),
            If(IntLiteral(1), Block([Return(None)]),
               If(IntLiteral(2), Block([Return(None)]),
                  If(IntLiteral(3), Block([Return(None)]), None)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

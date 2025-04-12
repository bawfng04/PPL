import unittest
from TestUtils import TestChecker
from AST import *
import inspect

class CheckSuite(unittest.TestCase):
    def test_001(self):
        """
var VoTien = 1;
var VoTien = 2;
        """
        input = Program([VarDecl("VoTien", None,IntLiteral(1)),VarDecl("VoTien", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VoTien", inspect.stack()[0].function))

    def test_002(self):
        """
var VoTien = 1;
const VoTien = 2;
        """
        input = Program([VarDecl("VoTien", None,IntLiteral(1)),ConstDecl("VoTien",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: VoTien", inspect.stack()[0].function))

    def test_003(self):
        """
const VoTien = 1;
var VoTien = 2;
        """
        input = Program([ConstDecl("VoTien",None,IntLiteral(1)),VarDecl("VoTien", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VoTien", inspect.stack()[0].function))

    def test_004(self):
        """
const VoTien = 1;
func VoTien () {return;}
        """
        input = Program([ConstDecl("VoTien",None,IntLiteral(1)),FuncDecl("VoTien",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: VoTien", inspect.stack()[0].function))

    def test_005(self):
        """
func VoTien () {return;}
var VoTien = 1;
        """
        input = Program([FuncDecl("VoTien",[],VoidType(),Block([Return(None)])),VarDecl("VoTien", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VoTien", inspect.stack()[0].function))

    def test_006(self):
        """
var getInt = 1;
        """
        input = Program([VarDecl("getInt", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: getInt", inspect.stack()[0].function))

    def test_007(self):
        """
type Votien struct {
    Votien int;
}
type TIEN struct {
    Votien string;
    TIEN int;
    TIEN float;
}
        """
        input = Program([StructType("Votien",[("Votien",IntType())],[]),StructType("TIEN",[("Votien",StringType()),("TIEN",IntType()),("TIEN",FloatType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: TIEN", inspect.stack()[0].function))

    def test_008(self):
        """
func (v TIEN) putIntLn () {return;}
func (v TIEN) getInt () {return;}
func (v TIEN) getInt () {return;}
type TIEN struct {
    Votien int;
}
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))), StructType("TIEN",[("Votien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: getInt", inspect.stack()[0].function))

    def test_009(self):
        """
type VoTien interface {
    VoTien ();
    VoTien (a int);
}
        """
        input = Program([InterfaceType("VoTien",[Prototype("VoTien",[],VoidType()),Prototype("VoTien",[IntType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: VoTien", inspect.stack()[0].function))

    def test_010(self):
        """
func Votien (a, a int) {return;}
        """
        input = Program([FuncDecl("Votien",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a", inspect.stack()[0].function))

    def test_011(self):
        """
func Votien (b int) {
    var b = 1;
    var a = 1;
    const a = 1;
}
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a", inspect.stack()[0].function))

    def test_012(self):
        """
        var VoTien = 1;
        var VoTien = 2;
        """
        input = Program([VarDecl("VoTien", None,IntLiteral(1)),VarDecl("VoTien", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VoTien", inspect.stack()[0].function))

    def test_013(self):
        """
var a = 1;
var b = a;
var c = d;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,Id("a")),VarDecl("c", None,Id("d"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: d", inspect.stack()[0].function))

    def test_014(self):
        """
func Votien () int {return 1;}
func foo () {
    var b = Votien();
    foo_votine();
    return;
}
        """
        input = Program([FuncDecl("Votien",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,FuncCall("Votien",[])),FuncCall("foo_votine",[]),Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo_votine", inspect.stack()[0].function))

    def test_015(self):
        """
type TIEN struct {
    Votien int;
}
func (v TIEN) getInt () {
    const c = v.Votien;
    var d = v.tien;
}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([ConstDecl("c",None,FieldAccess(Id("v"),"Votien")),VarDecl("d", None,FieldAccess(Id("v"),"tien"))])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: tien", inspect.stack()[0].function))

    def test_016(self):
        """
type TIEN struct {
    Votien int;
}
func (v TIEN) getInt () {
    v.getInt ();
    v.putInt ();
}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([MethCall(Id("v"),"getInt",[]),MethCall(Id("v"),"putInt",[])])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: putInt", inspect.stack()[0].function))

    def test_017(self):
        """
type TIEN struct {Votien int;}
type TIEN interface {VoTien ();}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),InterfaceType("TIEN",[Prototype("VoTien",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: TIEN", inspect.stack()[0].function))

    def test_018(self):
        """
var VoTien = 1;
var VoTien = 2;
        """
        input = Program([VarDecl("VoTien", None,IntLiteral(1)),VarDecl("VoTien", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VoTien", inspect.stack()[0].function))

    def test_019(self):
        """
var VoTien = 1;
const VoTien = 2;
        """
        input = Program([VarDecl("VoTien", None,IntLiteral(1)),ConstDecl("VoTien",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: VoTien", inspect.stack()[0].function))

    def test_020(self):
        """
const VoTien = 1;
var VoTien = 2;
        """
        input = Program([ConstDecl("VoTien",None,IntLiteral(1)),VarDecl("VoTien", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VoTien", inspect.stack()[0].function))

    def test_021(self):
        """
const VoTien = 1;
func VoTien () {return;}
        """
        input = Program([ConstDecl("VoTien",None,IntLiteral(1)),FuncDecl("VoTien",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: VoTien", inspect.stack()[0].function))

    def test_022(self):
        """
func VoTien () {return;}
var VoTien = 1;
        """
        input = Program([FuncDecl("VoTien",[],VoidType(),Block([Return(None)])),VarDecl("VoTien", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VoTien", inspect.stack()[0].function))

    def test_023(self):
        """
var getInt = 1;
        """
        input = Program([VarDecl("getInt", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: getInt", inspect.stack()[0].function))

    def test_024(self):
        """
type  Votien struct {
    Votien int;
}
type TIEN struct {
    Votien string;
    TIEN int;
    TIEN float;
}
        """
        input = Program([StructType("Votien",[("Votien",IntType())],[]),StructType("TIEN",[("Votien",StringType()),("TIEN",IntType()),("TIEN",FloatType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: TIEN", inspect.stack()[0].function))

    def test_025(self):
        """
func (v TIEN) putIntLn () {return;}
func (v TIEN) getInt () {return;}
func (v TIEN) getInt () {return;}
type TIEN struct {
    Votien int;
}
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))), StructType("TIEN",[("Votien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: getInt", inspect.stack()[0].function))

    def test_026(self):
        """
type VoTien interface {
    VoTien ();
    VoTien (a int);
}
        """
        input = Program([InterfaceType("VoTien",[Prototype("VoTien",[],VoidType()),Prototype("VoTien",[IntType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: VoTien", inspect.stack()[0].function))

    def test_027(self):
        """
func Votien (a, a int) {return;}
        """
        input = Program([FuncDecl("Votien",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a", inspect.stack()[0].function))

    def test_028(self):
        """
func Votien (b int) {
    var b = 1;
    var a = 1;
    const a = 1;
}
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a", inspect.stack()[0].function))

    def test_029(self):
        """
        const a = 2;
        func foo () {
            const a = 1;
            for var a = 1; a < 1; b += 2 {
                const b = 1;
            }
        }
        """
        input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),Block([ConstDecl("a",None,IntLiteral(1)),ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),Block([ConstDecl("a",None,IntLiteral(1)),ConstDecl("b",None,IntLiteral(1))])),ConstDecl("b",None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a", inspect.stack()[0].function))

    def test_030(self):
        """
var a = 1;
var b = a;
var c = d;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,Id("a")),VarDecl("c", None,Id("d"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: d", inspect.stack()[0].function))

    def test_031(self):
        """
func Votien () int {return 1;}
fun foo () {
    var b = Votien();
    foo_votine();
    return;
}
        """
        input = Program([FuncDecl("Votien",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,FuncCall("Votien",[])),FuncCall("foo_votine",[]),Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo_votine", inspect.stack()[0].function))

    def test_032(self):
        """
type TIEN struct {
    Votien int;
}
func (v TIEN) getInt () {
    const c = v.Votien;
    var d = v.tien;
}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([ConstDecl("c",None,FieldAccess(Id("v"),"Votien")),VarDecl("d", None,FieldAccess(Id("v"),"tien"))])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: tien", inspect.stack()[0].function))

    def test_033(self):
        """
type TIEN struct {
    Votien int;
}
func (v TIEN) getInt () {
    v.getInt ();
    v.putInt ();
}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([MethCall(Id("v"),"getInt",[]),MethCall(Id("v"),"putInt",[])])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: putInt", inspect.stack()[0].function))

    def test_034(self):
        """
type TIEN struct {Votien int;}
type TIEN interface {VoTien ();}

        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),InterfaceType("TIEN",[Prototype("VoTien",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: TIEN", inspect.stack()[0].function))

    def test_035(self):
        """
        func getString() {return;}
        """
        input = Program([FuncDecl("getString",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: getString", inspect.stack()[0].function))

    def test_036(self):
        """
        func putStringLn() {return;}
        """
        input = Program([FuncDecl("putStringLn",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: putStringLn", inspect.stack()[0].function))

    def test_037(self):
        """
        type TIEN struct {
        Votien int;
        }
        func (v TIEN) foo (v int) {return;}
        func foo () {return;}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_038(self):
        """
        var v TIEN;
        type TIEN struct {
            a int;
        }
        type VO interface {
            foo() int;
        }

        func (v TIEN) foo() int {return 1;}
        func (b TIEN) koo() {b.koo();}
        func foo() {
            var x VO;
            const b = x.foo();
            x.koo();
        }
        """
        input = Program([VarDecl("v",Id("TIEN"), None),StructType("TIEN",[("a",IntType())],[]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("TIEN"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",Id("VO"), None),ConstDecl("b",None,MethCall(Id("x"),"foo",[])),MethCall(Id("x"),"koo",[])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: koo", inspect.stack()[0].function))

    def test_039(self):
        """
        func Votien (b int) {
            for var a = 1; a < 1; a += 1 {
                const a = 2;
            }
        }
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a", inspect.stack()[0].function))

    def test_040(self):
        """
        const a = 2;
        func foo () {
            const a = 1;
            for var a = 1; a < 1; b := 2 {
                const b = 1;
            }
        }
        """
        input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("b"),IntLiteral(2)),Block([ConstDecl("b",None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: b", inspect.stack()[0].function))

    def test_041(self):
        """
        func Votien (b int) {
            for var a = 1; a < 1; a += 1 {
                const a = 2;
            }
        }
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a", inspect.stack()[0].function))

    ##############

    def test_042(self):
        """
        type S1 struct {votien int;}
        type S2 struct {votien int;}
        type I1 interface {votien() S1;}
        type I2 interface {votien() S2;}

        func (s S1) votien() S1 {return s;}

        var a S1;
        var c I1 = a;
        var d I2 = a;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),VarDecl("v",Id("S1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("S1"),Id("x")),VarDecl("k",Id("S2"),Id("x"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(k,Id(S2),Id(x))", inspect.stack()[0].function))

    def test_043(self):
        """
        type S1 struct {votien int;}
        type S2 struct {votien int;}
        type I1 interface {votien() S1;}
        type I2 interface {votien() S2;}

        func (s S1) votien() S1 {return s;}

        var a S1;
        var c I1 = a;
        var d I2 = a;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],Id("S1"))]),InterfaceType("I2",[Prototype("votien",[],Id("S2"))]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,Id(I2),Id(a))", inspect.stack()[0].function))

    def test_044(self):
        """
        var a = [2] int {1, 2}
        var c [3] int = a
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_045(self):
        """
        var a = [2] int {1, 2}
        var c [3] float = a
        """
        input = Program([
            VarDecl("a", None, ArrayLiteral([IntLiteral(2)], IntType(), [IntLiteral(1), IntLiteral(2)])),
            VarDecl("c", ArrayType([IntLiteral(3)], FloatType()), Id("a"))
        ])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_046(self):
        """
        type I1 interface {votien();}
        type I2 interface {votien();}


        var v I1;
        const x = v;
        var z I1 = x;
        var k I2 = x;
        """
        input = Program([InterfaceType("I1",[Prototype("votien",[],VoidType())]),InterfaceType("I2",[Prototype("votien",[],VoidType())]),VarDecl("v",Id("I1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("I1"),Id("x")),VarDecl("k",Id("I2"),Id("x"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(k,Id(I2),Id(x))", inspect.stack()[0].function))

    def test_047(self):
        """
        var a = [2] int {1, 2}
        var c [3][2] int = a
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3),IntLiteral(2)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(3),IntLiteral(2)]),Id(a))", inspect.stack()[0].function))

    def test_048(self):
        """
        type S1 struct {votien int;}
        type I1 interface {votien();}
        var a I1;
        var c I1 = nil;
        var d S1 = nil;
        func foo(){
            c := a;
            a := nil;
        }
        var e int = nil;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),VarDecl("a",Id("I1"), None),VarDecl("c",Id("I1"),NilLiteral()),VarDecl("d",Id("S1"),NilLiteral()),FuncDecl("foo",[],VoidType(),Block([Assign(Id("c"),Id("a")),Assign(Id("a"),NilLiteral())])),VarDecl("e",IntType(),NilLiteral())])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(e,IntType,Nil)", inspect.stack()[0].function))

    def test_049(self):
        """
        func foo(){
            if (true) {
                var a float = 1.2;
            } else {
                var a int = 1.2;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([If(BooleanLiteral(True), Block([VarDecl("a",FloatType(),FloatLiteral(1.2))]), Block([VarDecl("a",IntType(),FloatLiteral(1.2))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))", inspect.stack()[0].function))

    def test_050(self):
        """
        var a int = 1 % 2;
        var b int = 1 % 2.0;
        """
        input = Program([VarDecl("a",IntType(),BinaryOp("%", IntLiteral(1), IntLiteral(2))),VarDecl("b",IntType(),BinaryOp("%", IntLiteral(1), FloatLiteral(2.0)))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(IntLiteral(1),%,FloatLiteral(2.0))", inspect.stack()[0].function))

    def test_051(self):
        """
        var a boolean = 1 > 2;
        var b boolean = 1.0 < 2.0;
        var c boolean = "1" == "2";
        var d boolean = 1 > 2.0;
        """
        input = Program([VarDecl("a", BoolType(), BinaryOp(">", IntLiteral(1), IntLiteral(2))),
                         VarDecl("b", BoolType(), BinaryOp("<", FloatLiteral(1.0), FloatLiteral(2.0))),
                         VarDecl("c", BoolType(), BinaryOp("==", StringLiteral("1"), StringLiteral("2"))),
                         VarDecl("d", BoolType(), BinaryOp(">", IntLiteral(1), FloatLiteral(2.0)))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(IntLiteral(1),>,FloatLiteral(2.0))", inspect.stack()[0].function))

    def test_052(self):
        """
        func foo(){
            for var i int = 1; i < 10; i := 1. {
                return;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),FloatLiteral(1.)),Block([Return(None)]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Assign(Id(i),FloatLiteral(1.0))", inspect.stack()[0].function))

    def test_053(self):
        """
        func foo(){
            for var i int = 1; a < 10; i := 1. {
                var a = 1;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("i"),FloatLiteral(1.)),Block([VarDecl("a", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: a", inspect.stack()[0].function))

    def test_054(self):
        """
        func foo(){
            for var i int = 1; i; i := 1. {
                var a = 1;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),Id("i"),Assign(Id("i"),FloatLiteral(1.)),Block([VarDecl("a", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: For(VarDecl(i,IntType,IntLiteral(1)),Id(i),Assign(Id(i),FloatLiteral(1.0)),Block([VarDecl(a,IntLiteral(1))]))", inspect.stack()[0].function))

    def test_055(self):
        """
        func foo(){
            var arr [2][3] int;
            for a, b := range arr {
                var c int = a;
                var d [2]int = b;
                var e [2]string = a;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",ArrayType([IntLiteral(2)],IntType()),Id("b")),VarDecl("e",ArrayType([IntLiteral(2)],StringType()),Id("a"))]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: a", inspect.stack()[0].function))

    def test_056(self):
        """
        func foo(){
            return
        }
        func foo1() int{
            return 1
        }
        func foo2() float{
            return 2
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("foo1",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo2",[],FloatType(),Block([Return(IntLiteral(2))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(IntLiteral(2))", inspect.stack()[0].function))

    def test_057(self):
        """
        func foo()  {return ;}
        func  votien()  {
        foo();
        return votien();
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("votien",[],VoidType(),Block([FuncCall("foo",[]),Return(FuncCall("votien",[]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(votien,[])", inspect.stack()[0].function))

    def test_058(self):
        """
        type S1 struct {votien int;}
        type S2 struct {votien int;}
        type I1 interface {votien();}
        type I2 interface {votien();}

        func (s S1) votien() {return;}

        var a S1;
        var b S2;
        var c I1 = a;
        var d I2 = b;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),InterfaceType("I2",[Prototype("votien",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,Id(I2),Id(b))", inspect.stack()[0].function))

    def test_059(self):
        """
        var a = [2] int {1, 2}
        var c [2] float = a
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(2)],FloatType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_060(self):
        """
        func putLn() {return ;}
        """
        input = Program([FuncDecl("putLn",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: putLn", inspect.stack()[0].function))

    def test_061(self):
        """
        type putLn interface {foo();};
        """
        input = Program([InterfaceType("putLn",[Prototype("foo",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: putLn", inspect.stack()[0].function))

    def test_062(self):
        """
        type putLn struct {a int;};
        """
        input = Program([StructType("putLn",[("a",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: putLn", inspect.stack()[0].function))

    def test_063(self):
        """
        var a int = getBool();
        """
        input = Program([VarDecl("a",IntType(),FuncCall("getBool",[]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(a,IntType,FuncCall(getBool,[]))", inspect.stack()[0].function))

    def test_064(self):
        """
        func foo() {
            putFloat(getInt());
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("putFloat",[FuncCall("getInt",[])])]))])
        # wrong at putFloat(getInt())
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(putFloat,[FuncCall(getInt,[])])", inspect.stack()[0].function))

    def test_065(self):
        """
        type TIEN struct {a [2]int;}
        type VO interface {foo() int;}

        func (v TIEN) foo() int {return 1;}

        func foo(a VO) {
            var b = TIEN{a: [2]int{1, 2}};
            foo(b)
        }
        """
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("VO"))],VoidType(),Block([VarDecl("b", None,StructLiteral("TIEN",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),FuncCall("foo",[Id("b")])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(foo,[Id(b)])", inspect.stack()[0].function))

    def test_066(self):
        """
        type TIEN struct {a [2]int;}
        type VO interface {foo() int;}

        func (v TIEN) foo() int {return 1;}

        func foo(a VO) {
            var b = nil;
            foo(nil)
        }
        """
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("VO"))],VoidType(),Block([VarDecl("b", None,NilLiteral()),FuncCall("foo",[NilLiteral()])]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_067(self):
        """
        type TIEN struct {a [2]int;}

        func foo() TIEN {
            return nil
        }
        """
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),FuncDecl("foo",[],Id("TIEN"),Block([Return(NilLiteral())]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_068(self):
        """
        func foo() int {
            var a = 1;
            if (a < 3) {
                var a = 1;
            } else if(a > 2) {
                var a = 2;
            }
            return a;
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1)),If(BinaryOp("<", Id("a"), IntLiteral(3)), Block([VarDecl("a", None,IntLiteral(1))]), If(BinaryOp(">", Id("a"), IntLiteral(2)), Block([VarDecl("a", None,IntLiteral(2))]), None)),Return(Id("a"))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_069(self):
        """
        func foo() {const b = 1; const b = 1;}
        """
        input = Program([FuncDecl("foo", [], VoidType(), Block([ConstDecl("b", None, IntLiteral(1)), ConstDecl("b", None, IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: b", inspect.stack()[0].function))

    def test_070(self):
        """
        func Votien (b int) {
            var b = 1;
            var a = 1;
            const a = 1;
        }
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a", inspect.stack()[0].function))

    def test_071(self):
        """
        const a = 2;
        func foo () {
            const a = 1;
            for var a = 1; a < 1; b := 2 {
                const a = 1;
                for var a = 1; a < 1; b := 2 {
                    const a = 1;
                    const b = 1;
                }
                const b = 1;
                var a = 1;
            }
        }
        """
        input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),Block([ConstDecl("a",None,IntLiteral(1)),ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),Block([ConstDecl("a",None,IntLiteral(1)),ConstDecl("b",None,IntLiteral(1))])),ConstDecl("b",None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a", inspect.stack()[0].function))

    def test_072(self):
        """
        var a = 1;
        var b = a;
        var c = d;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,Id("a")),VarDecl("c", None,Id("d"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: d", inspect.stack()[0].function))

    def test_073(self):
        """
        func Votien () int {return 1;}
        func foo () {
            var b = Votien();
            foo_votine();
            return;
        }
        """
        input = Program([FuncDecl("Votien",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,FuncCall("Votien",[])),FuncCall("foo_votine",[]),Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo_votine", inspect.stack()[0].function))

    def test_074(self):
        """
        type TIEN struct {
            Votien int;
        }
        func (v TIEN) getInt () {
            const c = v.Votien;
            var d = v.tien;
        }
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([ConstDecl("c",None,FieldAccess(Id("v"),"Votien")),VarDecl("d", None,FieldAccess(Id("v"),"tien"))])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: tien", inspect.stack()[0].function))

    def test_075(self):
        """
        type TIEN struct {
            Votien int;
        }
        func (v TIEN) getInt () {
            v.getInt ();
            v.putInt ();
        }
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([MethCall(Id("v"),"getInt",[]),MethCall(Id("v"),"putInt",[])])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: putInt", inspect.stack()[0].function))

    def test_076(self):
        """
        type TIEN struct {Votien int;}
        type TIEN interface {VoTien ();}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),InterfaceType("TIEN",[Prototype("VoTien",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: TIEN", inspect.stack()[0].function))

    def test_077(self):
        """
        func getString() {return;}
        """
        input = Program([FuncDecl("getString",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: getString", inspect.stack()[0].function))

    def test_078(self):
        """
        func putStringLn() {return;}
        """
        input = Program([FuncDecl("putStringLn",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: putStringLn", inspect.stack()[0].function))

    def test_079(self):
        """
        type TIEN struct {
            Votien int;
        }
        func (v TIEN) foo (v int) {return;}
        func foo () {return;}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_080(self):
        """
        var v TIEN;
        type TIEN struct {
            a int;
        }
        type VO interface {
            foo() int;
        }

        func (v TIEN) foo() int {return 1;}
        func (b TIEN) koo() {b.koo();}
        func foo() {
            var x VO;
            const b = x.foo();
            x.koo();
        }
        """
        input = Program([VarDecl("v",Id("TIEN"), None),StructType("TIEN",[("a",IntType())],[]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("TIEN"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",Id("VO"), None),ConstDecl("b",None,MethCall(Id("x"),"foo",[])),MethCall(Id("x"),"koo",[])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: koo", inspect.stack()[0].function))

    def test_081(self):
        """
        func Votien (b int) {
            for var a = 1; a < 1; a += 1 {
                const a = 2;
            }
        }
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a", inspect.stack()[0].function))

    def test_082(self):
        """
        const a = 2;
        func foo () {
            const a = 1;
            for var a = 1; a < 1; b := 2 {
                const b = 1;
            }
        }
        """
        input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("b"),IntLiteral(2)),Block([ConstDecl("b",None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: b", inspect.stack()[0].function))

    def test_083(self):
        """
        type I1 interface {votien();}
        type I2 interface {votien();}

        var v I1;
        const x = v;
        var z I1 = x;
        var k I2 = x;
        """
        input = Program([InterfaceType("I1",[Prototype("votien",[],VoidType())]),InterfaceType("I2",[Prototype("votien",[],VoidType())]),VarDecl("v",Id("I1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("I1"),Id("x")),VarDecl("k",Id("I2"),Id("x"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(k,Id(I2),Id(x))", inspect.stack()[0].function))

    def test_084(self):
        """
        func foo(){
            if (true) {
                var a float = 1.2;
            } else {
                var a int = 1.2;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([If(BooleanLiteral(True), Block([VarDecl("a",FloatType(),FloatLiteral(1.2))]), Block([VarDecl("a",IntType(),FloatLiteral(1.2))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))", inspect.stack()[0].function))

    def test_085(self):
        """
        func foo(){
            for var i int = 1; i < 10; i := 1. {
                return;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),FloatLiteral(1.)),Block([Return(None)]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Assign(Id(i),FloatLiteral(1.0))", inspect.stack()[0].function))

    def test_086(self):
        """
        func foo(){
            for var i int = 1; i; i := 1. {
                var a = 1;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),Id("i"),Assign(Id("i"),FloatLiteral(1.)),Block([VarDecl("a", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: For(VarDecl(i,IntType,IntLiteral(1)),Id(i),Assign(Id(i),FloatLiteral(1.0)),Block([VarDecl(a,IntLiteral(1))]))", inspect.stack()[0].function))

    def test_087(self):
        """
        var a = [2] int {1, 2}
        var c [2] float = a
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(2)],FloatType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_088(self):
        """
        var a int = getBool();
        """
        input = Program([VarDecl("a",IntType(),FuncCall("getBool",[]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(a,IntType,FuncCall(getBool,[]))", inspect.stack()[0].function))

    def test_089(self):
        """
        type TIEN struct {a [2]int;}
        type VO interface {foo() int;}

        func (v TIEN) foo() int {return 1;}

        func foo(a VO) {
            var b = nil;
            foo(nil)
        }
        """
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("VO"))],VoidType(),Block([VarDecl("b", None,NilLiteral()),FuncCall("foo",[NilLiteral()])]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_090(self):
        """
        var a = [2] int {1, 2}
        var c [3][2] int = a
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3),IntLiteral(2)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(3),IntLiteral(2)]),Id(a))", inspect.stack()[0].function))

    def test_091(self):
        """
        func foo(){
            var arr [2][3] int;
            for a, b := range arr {
                var c int = a;
                var d [3]int = b;
                var e [2]string = a;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",ArrayType([IntLiteral(3)],IntType()),Id("b")),VarDecl("e",ArrayType([IntLiteral(2)],StringType()),Id("a"))]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: a", inspect.stack()[0].function))

    def test_092(self):
        """
        func foo(){
            putFloat(getInt());
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("putFloat",[FuncCall("getInt",[])])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(putFloat,[FuncCall(getInt,[])])", inspect.stack()[0].function))

    def test_093(self):
        """
        type S1 struct {votien int;}
        type S2 struct {votien int;}
        type I1 interface {votien() S1;}
        type I2 interface {votien() S2;}

        func (s S1) votien() S1 {return s;}

        var a S1;
        var c I1 = a;
        var d I2 = a;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],Id("S1"))]),InterfaceType("I2",[Prototype("votien",[],Id("S2"))]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,Id(I2),Id(a))", inspect.stack()[0].function))

    def test_094(self):
        """
        type S1 struct {votien int;}
        type S2 struct {votien int;}
        type I1 interface {votien();}
        type I2 interface {votien();}

        func (s S1) votien() {return;}

        var a S1;
        var b S2;
        var c I1 = a;
        var d I2 = b;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),InterfaceType("I2",[Prototype("votien",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,Id(I2),Id(b))", inspect.stack()[0].function))

    def test_095(self):
        """
        const a = 2;
        func foo () {
            const a = 1;
            var a = 1;
            const b = 1;
        }
        """
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1))])),ConstDecl("b",None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_096(self):
        """
        type TIEN struct {a int; b int; a float;}
        """
        input = Program([StructType("TIEN",[("a",IntType()),("b",IntType()),("a",FloatType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: a", inspect.stack()[0].function))

    def test_097(self):
        """
        type TIEN struct {c float; b int; a int; b int;}
        """
        input = Program([StructType("TIEN",[("c",FloatType()),("b",IntType()),("a",IntType()),("b",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: b", inspect.stack()[0].function))

    def test_098(self):
        """
        type VO struct {d int; d int;}
        """
        input = Program([StructType("VO",[("d",IntType()),("d",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: d", inspect.stack()[0].function))

    def test_099(self):
        """
        type TIEN interface {foo(); foo(a int, b int);}
        """
        input = Program([InterfaceType("TIEN",[Prototype("foo",[],VoidType()),Prototype("foo",[IntType(),IntType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: foo", inspect.stack()[0].function))

    def test_100(self):
        """
        func putInt() {return;}
        """
        input = Program([FuncDecl("putInt",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: putInt", inspect.stack()[0].function))

    def test_101(self):
        """
        type TIEN struct {a int; b int; a float;}
        """
        input = Program([StructType("TIEN",[("a",IntType()),("b",IntType()),("a",FloatType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: a", inspect.stack()[0].function))

    def test_102(self):
        """
        type TIEN struct {a int; b int; c float; b int;}
        """
        input = Program([StructType("TIEN",[("a",IntType()),("b",IntType()),("c",FloatType()),("b",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: b", inspect.stack()[0].function))

    def test_103(self):
        """
        type TIEN struct {c float; b int; a int;}
        type VO struct {d int; d int;}
        """
        input = Program([StructType("TIEN",[("c",FloatType()),("b",IntType()),("a",IntType())],[]),StructType("VO",[("d",IntType()),("d",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: d", inspect.stack()[0].function))

    def test_104(self):
        """
        type TIEN struct {a int;}
        type VO struct {a int;}
        type TIEN struct {a int;}
        """
        input = Program([StructType("TIEN",[("a",IntType())],[]),StructType("VO",[("a",IntType())],[]),StructType("TIEN",[("a",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: TIEN", inspect.stack()[0].function))

    def test_105(self):
        """
        type TIEN interface {foo();}
        type TIEN interface {foo();}
        """
        input = Program([InterfaceType("TIEN",[Prototype("foo",[],VoidType())]),InterfaceType("TIEN",[Prototype("foo",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: TIEN", inspect.stack()[0].function))

    def test_106(self):
        """
        type TIEN interface {foo();}
        type VO interface {foo();}
        type TIEN interface {foo();}
        """
        input = Program([InterfaceType("TIEN",[Prototype("foo",[],VoidType())]),InterfaceType("VO",[Prototype("foo",[],VoidType())]),InterfaceType("TIEN",[Prototype("foo",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: TIEN", inspect.stack()[0].function))

    def test_107(self):
        """
        type TIEN struct {a int;}
        type VO struct {a int;}
        type TIEN interface {foo();}
        """
        input = Program([StructType("TIEN",[("a",IntType())],[]),StructType("VO",[("a",IntType())],[]),InterfaceType("TIEN",[Prototype("foo",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: TIEN", inspect.stack()[0].function))

    def test_108(self):
        """
        type TIEN interface {foo(); foo(a int, b int);}
        """
        input = Program([InterfaceType("TIEN",[Prototype("foo",[],VoidType()),Prototype("foo",[IntType(),IntType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: foo", inspect.stack()[0].function))

    def test_109(self):
        """
        type TIEN interface {foo(); foo1(); foo(a int, b int);}
        """
        input = Program([InterfaceType("TIEN",[Prototype("foo",[],VoidType()),Prototype("foo1",[],VoidType()),Prototype("foo",[IntType(),IntType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: foo", inspect.stack()[0].function))

    def test_110(self):
        """
        type TIEN interface {foo1(); foo();}
        type VO interface {foo(); foo(a int, b int);}
        """
        input = Program([InterfaceType("TIEN",[Prototype("foo1",[],VoidType()),Prototype("foo",[],VoidType())]),InterfaceType("VO",[Prototype("foo",[],VoidType()),Prototype("foo",[IntType(),IntType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: foo", inspect.stack()[0].function))

    def test_111(self):
        """
        type TIEN interface {foo();}
        func TIEN() {return;}
        func foo() {return;}
        func TIEN() {return;}
        """
        input = Program([InterfaceType("TIEN",[Prototype("foo",[],VoidType())]),FuncDecl("TIEN",[],VoidType(),Block([Return(None)])),FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("TIEN",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: TIEN", inspect.stack()[0].function))

    def test_112(self):
        """
        func getInt() {return;}
        """
        input = Program([FuncDecl("getInt",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: getInt", inspect.stack()[0].function))

    def test_113(self):
        """
        func putInt() {return;}
        """
        input = Program([FuncDecl("putInt",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: putInt", inspect.stack()[0].function))

    def test_114(self):
        """
        func putIntLn() {return;}
        """
        input = Program([FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: putIntLn", inspect.stack()[0].function))

    def test_115(self):
        """
        func getString() {return;}
        """
        input = Program([FuncDecl("getString",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: getString", inspect.stack()[0].function))

    def test_116(self):
        """
        func putStringLn() {return;}
        """
        input = Program([FuncDecl("putStringLn",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: putStringLn", inspect.stack()[0].function))

    def test_117(self):
        """
        var foo = 1;
        func foo() {return;}
        """
        input = Program([VarDecl("foo", None, IntLiteral(1)), FuncDecl("foo", [], VoidType(), Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: foo", inspect.stack()[0].function))

    def test_118(self):
        """
        func foo() {return;}
        var foo = 1;
        """
        input = Program([FuncDecl("foo", [], VoidType(), Block([Return(None)])), VarDecl("foo", None, IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: foo", inspect.stack()[0].function))

    def test_119(self):
        """
        func foo() {return;}
        const foo = 1;
        """
        input = Program([FuncDecl("foo", [], VoidType(), Block([Return(None)])), ConstDecl("foo", None, IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: foo", inspect.stack()[0].function))

    def test_120(self):
        """
        const foo = 1;
        func foo() {return;}
        """
        input = Program([ConstDecl("foo", None, IntLiteral(1)), FuncDecl("foo", [], VoidType(), Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: foo", inspect.stack()[0].function))

    def test_121(self):
        """
        const a = 1;
        func foo() {var a = 1;}
        """
        input = Program([ConstDecl("a", None, IntLiteral(1)), FuncDecl("foo", [], VoidType(), Block([VarDecl("a", None, IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_122(self):
        """
        const a = 1;
        func foo() {const b = 1;}
        var a = 1;
        """
        input = Program([ConstDecl("a", None, IntLiteral(1)), FuncDecl("foo", [], VoidType(), Block([ConstDecl("b", None, IntLiteral(1))])), VarDecl("a", None, IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a", inspect.stack()[0].function))

    def test_123(self):
        """
        const a = 1;
        func foo() {const b = 1;}
        const b = 1;
        """
        input = Program([ConstDecl("a", None, IntLiteral(1)), FuncDecl("foo", [], VoidType(), Block([ConstDecl("b", None, IntLiteral(1))])), ConstDecl("b", None, IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_124(self):
        """
        var a = 1;
        func foo() {const b = 1;}
        const a = 1;
        """
        input = Program([VarDecl("a", None, IntLiteral(1)), FuncDecl("foo", [], VoidType(), Block([ConstDecl("b", None, IntLiteral(1))])), ConstDecl("a", None, IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a", inspect.stack()[0].function))

    def test_125(self):
        """
        func foo(a int) int {
            return 1;
        }
        var a int = foo(1 + 1);
        var b = foo(1.0);
        """
        input = Program([FuncDecl("foo", [ParamDecl("a", IntType())], IntType(), Block([Return(IntLiteral(1))])), VarDecl("a", IntType(), FuncCall("foo", [BinaryOp("+", IntLiteral(1), IntLiteral(1))])), VarDecl("b", None, FuncCall("foo", [FloatLiteral(1.0)]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(foo,[FloatLiteral(1.0)])", inspect.stack()[0].function))

    def test_126(self):
        """
        type TIEN struct {Votien int;}
        func (v TIEN) foo(a int, b int, a int) {return;}
        func foo() {return;}
        """
        input = Program([StructType("TIEN", [("Votien", IntType())], [MethodDecl("v", Id("TIEN"), FuncDecl("foo", [ParamDecl("a", IntType()), ParamDecl("b", IntType()), ParamDecl("a", IntType())], VoidType(), Block([Return(None)])))]), MethodDecl("v", Id("TIEN"), FuncDecl("foo", [ParamDecl("a", IntType()), ParamDecl("b", IntType()), ParamDecl("a", IntType())], VoidType(), Block([Return(None)]))), FuncDecl("foo", [], VoidType(), Block([Return(None)]))])
        # self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a", inspect.stack()[0].function))

    def test_127(self):
        """
        func (v TIEN) foo(a int, b int) {var a = 1;}
        type TIEN struct {Votien int;}
        type VO struct {Votien int;}
        func (v VO) foo(a int, b int) {var a = 1;}
        """
        input = Program([MethodDecl("v", Id("TIEN"), FuncDecl("foo", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], VoidType(), Block([VarDecl("a", None, IntLiteral(1))]))), StructType("TIEN", [("Votien", IntType())], [MethodDecl("v", Id("TIEN"), FuncDecl("foo", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], VoidType(), Block([VarDecl("a", None, IntLiteral(1))])))]), StructType("VO", [("Votien", IntType())], [MethodDecl("v", Id("VO"), FuncDecl("foo", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], VoidType(), Block([VarDecl("a", None, IntLiteral(1))])))]), MethodDecl("v", Id("VO"), FuncDecl("foo", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], VoidType(), Block([VarDecl("a", None, IntLiteral(1))])))])
        # self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_128(self):
        """
        const a = 2;
        func foo() {
            const a = 1;
            for var a = 1; a < 1; {
                const a = 1;
                for var a = 1; a < 1; {
                    const a = 1;
                    const b = 1;
                }
                const b = 1;
                var a = 1;
            }
        }
        """
        input = Program([ConstDecl("a", None, IntLiteral(2)), FuncDecl("foo", [], VoidType(), Block([ConstDecl("a", None, IntLiteral(1)), ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)), Block([ConstDecl("a", None, IntLiteral(1)), ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)), Block([ConstDecl("a", None, IntLiteral(1)), ConstDecl("b", None, IntLiteral(1))])), ConstDecl("b", None, IntLiteral(1)), VarDecl("a", None, IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a", inspect.stack()[0].function))

    def test_129(self):
        """
        var a = 1;
        func foo() {
            const b = 1;
            for a, b := range [3]int{1, 2, 3} {
                var d = b;
            }
            var d = b;
            var a = 1;
        }
        var d = a;
        """
        input = Program([VarDecl("a", None, IntLiteral(1)), FuncDecl("foo", [], VoidType(), Block([ConstDecl("b", None, IntLiteral(1)), ForEach(Id("a"), Id("b"), ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), Block([VarDecl("d", None, Id("b"))])), VarDecl("d", None, Id("b")), VarDecl("a", None, IntLiteral(1))])), VarDecl("d", None, Id("a"))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_130(self):
        """
        var a = 1;
        func foo() {
            const b = 1;
            for a, c := range [3]int{1, 2, 3} {
                var d = c;
            }
            var d = a;
            var a = 1;
        }
        var d = b;
        """
        input = Program([VarDecl("a", None, IntLiteral(1)), FuncDecl("foo", [], VoidType(), Block([ConstDecl("b", None, IntLiteral(1)), ForEach(Id("a"), Id("c"), ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), Block([VarDecl("d", None, Id("c"))])), VarDecl("d", None, Id("a")), VarDecl("a", None, IntLiteral(1))])), VarDecl("d", None, Id("b"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: c", inspect.stack()[0].function))

    def test_131(self):
        """
        var a = foo();
        func foo() int {return 1;}
        var d = koo();
        """
        input = Program([VarDecl("a", None, FuncCall("foo", [])), FuncDecl("foo", [], IntType(), Block([Return(IntLiteral(1))])), VarDecl("d", None, FuncCall("koo", []))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: koo", inspect.stack()[0].function))

    def test_132(self):
        """
        var v TIEN;
        func foo() {
            const a = v.a;
            const e = v.e;
        }
        type TIEN struct {c int; b int; a int;}
        """
        input = Program([VarDecl("v", Id("TIEN"), None), FuncDecl("foo", [], VoidType(), Block([ConstDecl("a", None, FieldAccess(Id("v"), "a")), ConstDecl("e", None, FieldAccess(Id("v"), "e"))])), StructType("TIEN", [("c", IntType()), ("b", IntType()), ("a", IntType())], [])])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: e", inspect.stack()[0].function))

    def test_133(self):
        """
        var v TIEN;
        type TIEN struct {a int;}
        func (v TIEN) foo() int {return 1;}
        func (b TIEN) koo() {b.koo();}
        func foo() {
            var x = v;
            const b = x.foo();
            x.koo();
            const d = x.zoo();
        }
        """
        input = Program([VarDecl("v", Id("TIEN"), None), StructType("TIEN", [("a", IntType())], [MethodDecl("v", Id("TIEN"), FuncDecl("foo", [], IntType(), Block([Return(IntLiteral(1))]))), MethodDecl("b", Id("TIEN"), FuncDecl("koo", [], VoidType(), Block([MethCall(Id("b"), "koo", [])])))]), MethodDecl("v", Id("TIEN"), FuncDecl("foo", [], IntType(), Block([Return(IntLiteral(1))]))), MethodDecl("b", Id("TIEN"), FuncDecl("koo", [], VoidType(), Block([MethCall(Id("b"), "koo", [])]))), FuncDecl("foo", [], VoidType(), Block([VarDecl("x", None, Id("v")), ConstDecl("b", None, MethCall(Id("x"), "foo", [])), MethCall(Id("x"), "koo", []), ConstDecl("d", None, MethCall(Id("x"), "zoo", []))]))])
        # self.assertTrue(TestChecker.test(input, "Redeclared Method: foo", inspect.stack()[0].function))

    def test_134(self):
        """
        var v float = 1;
        """
        input = Program([VarDecl("v", FloatType(), IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_135(self):
        """
        type I1 interface {votien();}
        type I2 interface {votien();}
        var v I1;
        const x = v;
        var z I1 = x;
        var k I2 = x;
        """
        input = Program([InterfaceType("I1", [Prototype("votien", [], VoidType())]), InterfaceType("I2", [Prototype("votien", [], VoidType())]), VarDecl("v", Id("I1"), None), ConstDecl("x", None, Id("v")), VarDecl("z", Id("I1"), Id("x")), VarDecl("k", Id("I2"), Id("x"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(k,Id(I2),Id(x))", inspect.stack()[0].function))

    def test_136(self):
        """
        type S1 struct {votien int;}
        type S2 struct {votien int;}
        type I1 interface {votien() S1;}
        type I2 interface {votien() S2;}
        func (s S1) votien() S1 {return s;}
        var a S1;
        var c I1 = a;
        var d I2 = a;
        """
        input = Program([StructType("S1", [("votien", IntType())], [MethodDecl("s", Id("S1"), FuncDecl("votien", [], Id("S1"), Block([Return(Id("s"))])))]), StructType("S2", [("votien", IntType())], []), InterfaceType("I1", [Prototype("votien", [], Id("S1"))]), InterfaceType("I2", [Prototype("votien", [], Id("S2"))]), MethodDecl("s", Id("S1"), FuncDecl("votien", [], Id("S1"), Block([Return(Id("s"))]))), VarDecl("a", Id("S1"), None), VarDecl("c", Id("I1"), Id("a")), VarDecl("d", Id("I2"), Id("a"))])
        # self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,Id(I2),Id(a))", inspect.stack()[0].function))

    def test_137(self):
        """
        type S1 struct {votien int;}
        type S2 struct {votien int;}
        type I1 interface {votien(a int, b int) S1;}
        type I2 interface {votien(a int, b float) S1;}
        func (s S1) votien(a int, b int) S1 {return s;}
        func foo() {
            var a S1;
            var c I1 = a;
            var d I2 = a;
        }
        """
        input = Program([StructType("S1", [("votien", IntType())], [MethodDecl("s", Id("S1"), FuncDecl("votien", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], Id("S1"), Block([Return(Id("s"))])))]), StructType("S2", [("votien", IntType())], []), InterfaceType("I1", [Prototype("votien", [IntType(), IntType()], Id("S1"))]), InterfaceType("I2", [Prototype("votien", [IntType(), FloatType()], Id("S1"))]), MethodDecl("s", Id("S1"), FuncDecl("votien", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], Id("S1"), Block([Return(Id("s"))]))), FuncDecl("foo", [], VoidType(), Block([VarDecl("a", Id("S1"), None), VarDecl("c", Id("I1"), Id("a")), VarDecl("d", Id("I2"), Id("a"))]))])
        # self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,Id(I2),Id(a))", inspect.stack()[0].function))

    def test_138(self):
        """
        func foo() {
            if 1 {
                var a float = 1.02;
            }
        }
        """
        input = Program([FuncDecl("foo", [], VoidType(), Block([If(IntLiteral(1), Block([VarDecl("a", FloatType(), FloatLiteral(1.02))]), None)]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: If(IntLiteral(1),Block([VarDecl(a,FloatType,FloatLiteral(1.02))]))", inspect.stack()[0].function))

    def test_139(self):
        """
        type TIEN struct {v int;}
        var v TIEN;
        func foo() {
            for 1 {
                var a int = 1.02;
            }
        }
        """
        input = Program([StructType("TIEN", [("v", IntType())], []), VarDecl("v", Id("TIEN"), None), FuncDecl("foo", [], VoidType(), Block([ForBasic(IntLiteral(1), Block([VarDecl("a", IntType(), FloatLiteral(1.02))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: For(IntLiteral(1),Block([VarDecl(a,IntType,FloatLiteral(1.02))]))", inspect.stack()[0].function))

    def test_140(self):
        """
        type S1 struct {t int; v int;}
        var a = S1{v: 1, t: 2};
        var b S1 = a;
        var c int = b;
        """
        input = Program([StructType("S1", [("t", IntType()), ("v", IntType())], []), VarDecl("a", None, StructLiteral("S1", [("v", IntLiteral(1)), ("t", IntLiteral(2))])), VarDecl("b", Id("S1"), Id("a")), VarDecl("c", IntType(), Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,IntType,Id(b))", inspect.stack()[0].function))

    def test_141(self):
        """
        var a = [2]float{1, 2};
        var c [3]int = a;
        """
        input = Program([VarDecl("a", None, ArrayLiteral([IntLiteral(2)], FloatType(), [IntLiteral(1), IntLiteral(2)])), VarDecl("c", ArrayType([IntLiteral(3)], IntType()), Id("a"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(3)]),Id(a))", inspect.stack()[0].function))

    def test_142(self):
        """
        type S1 struct {v int;}
        var a = [1]S1{S1{v: z}};
        """
        input = Program([StructType("S1", [("v", IntType())], []), VarDecl("a", None, ArrayLiteral([IntLiteral(1)], Id("S1"), [StructLiteral("S1", [("v", Id("z"))])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: z", inspect.stack()[0].function))

    def test_143(self):
        """
        var a [2][3]int;
        var b = a[1.0];
        """
        input = Program([VarDecl("a", ArrayType([IntLiteral(2), IntLiteral(3)], IntType()), None), VarDecl("b", None, ArrayCell(Id("a"), [FloatLiteral(1.0)]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ArrayCell(Id(a),[FloatLiteral(1.0)])", inspect.stack()[0].function))

    def test_144(self):
        """
        type S1 struct {votien int;}
        type I1 interface {votien();}
        var a I1;
        var c I1 = nil;
        var d S1 = nil;
        func foo() {
            c := a;
            a := nil;
        }
        var e int = nil;
        """
        input = Program([StructType("S1", [("votien", IntType())], []), InterfaceType("I1", [Prototype("votien", [], VoidType())]), VarDecl("a", Id("I1"), None), VarDecl("c", Id("I1"), NilLiteral()), VarDecl("d", Id("S1"), NilLiteral()), FuncDecl("foo", [], VoidType(), Block([Assign(Id("c"), Id("a")), Assign(Id("a"), NilLiteral())])), VarDecl("e", IntType(), NilLiteral())])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(e,IntType,Nil)", inspect.stack()[0].function))

    def test_145(self):
        """
        var a = 1 + 2.0;
        var b = 1 + 1;
        func foo() int {
            return b;
            return a;
        }
        """
        input = Program([VarDecl("a", None, BinaryOp("+", IntLiteral(1), FloatLiteral(2.0))), VarDecl("b", None, BinaryOp("+", IntLiteral(1), IntLiteral(1))), FuncDecl("foo", [], IntType(), Block([Return(Id("b")), Return(Id("a"))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(Id(a))", inspect.stack()[0].function))

    def test_146(self):
        """
        var a int = 1 % 2;
        var b int = 1 % 2.0;
        """
        input = Program([VarDecl("a", IntType(), BinaryOp("%", IntLiteral(1), IntLiteral(2))), VarDecl("b", IntType(), BinaryOp("%", IntLiteral(1), FloatLiteral(2.0)))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(IntLiteral(1),%,FloatLiteral(2.0))", inspect.stack()[0].function))

    def test_147(self):
        """
        var a boolean = 1 >= 2;
        var b boolean = 1.0 <= 2.0;
        var c boolean = "1" != "2";
        var d boolean = 1 > true;
        """
        input = Program([VarDecl("a", BoolType(), BinaryOp(">=", IntLiteral(1), IntLiteral(2))), VarDecl("b", BoolType(), BinaryOp("<=", FloatLiteral(1.0), FloatLiteral(2.0))), VarDecl("c", BoolType(), BinaryOp("!=", StringLiteral("1"), StringLiteral("2"))), VarDecl("d", BoolType(), BinaryOp(">", IntLiteral(1), BooleanLiteral(True)))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(IntLiteral(1),>,BooleanLiteral(true))", inspect.stack()[0].function))

    def test_148(self):
        """
        func foo() {
            for var i int = 1; i; i := 1.0 {
                var a = 1;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),Id("i"),Assign(Id("i"),FloatLiteral(1.0)),Block([VarDecl("a", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: For(VarDecl(i,IntType,IntLiteral(1)),Id(i),Assign(Id(i),FloatLiteral(1.0)),Block([VarDecl(a,IntLiteral(1))]))", inspect.stack()[0].function))

    def test_149(self):
        """
        func foo() {
            var arr [2]int;
            for a, b := range arr {
                var c int = a;
                var d int = b;
                var e string = a;
            }
        }
        """
        input = Program([FuncDecl("foo", [], VoidType(), Block([VarDecl("arr", ArrayType([IntLiteral(2)], IntType()), None), ForEach(Id("a"), Id("b"), Id("arr"), Block([VarDecl("c", IntType(), Id("a")), VarDecl("d", IntType(), Id("b")), VarDecl("e", StringType(), Id("a"))]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: a", inspect.stack()[0].function))

    def test_150(self):
        """
        var A = 1;
        type A struct {a int;}
        """
        input = Program([VarDecl("A", None, IntLiteral(1)), StructType("A", [("a", IntType())], [])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: A", inspect.stack()[0].function))

    def test_151(self):
        """
        const A = 2;
        type A interface {foo();}
        """
        input = Program([ConstDecl("A",None,IntLiteral(2)),InterfaceType("A",[Prototype("foo",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: A", inspect.stack()[0].function))

    def test_152(self):
        """
        type A interface {foo();}
        const A = 2;
        """
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]),ConstDecl("A",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: A", inspect.stack()[0].function))

    def test_153(self):
        """
        type A interface {foo();}
        var A = 1;
        """
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]),VarDecl("A", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: A", inspect.stack()[0].function))

    def test_154(self):
        """
        func A() {
            return A;
        }
        """
        input = Program([FuncDecl("A",[],VoidType(),Block([Return(Id("A"))]))])
        # output is NOT "Type Mismatch: Return(Id(A))"
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: A", inspect.stack()[0].function))

    def test_155(self):
        """
        type S1 struct {votien int;}
        type I1 interface {votien();}

        func (s S1) votien() {return;}

        var b [2] S1;
        var a [2] I1 = b;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([Return(None)]))),VarDecl("b",ArrayType([IntLiteral(2)],Id("S1")), None),VarDecl("a",ArrayType([IntLiteral(2)],Id("I1")),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(a,ArrayType(Id(I1),[IntLiteral(2)]),Id(b))", inspect.stack()[0].function))

    def test_156(self):
        """
        func votien(a  [2]int ) {
            votien([3] int {1,2,3})
        }
        """
        input = Program([FuncDecl("votien",[ParamDecl("a",ArrayType([IntLiteral(2)],IntType()))],VoidType(),Block([FuncCall("votien",[ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(votien,[ArrayLiteral([IntLiteral(3)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])", inspect.stack()[0].function))

    def test_157(self):
        """
        func foo() {
            a := 1;
            var a = 1;
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a", inspect.stack()[0].function))

    def test_158(self):
        """
        const a = 2;
        type STRUCT struct {x [a] int;}
        func (s STRUCT) foo(x [a] int) [a] int {return s.x;}
        func foo(x [a] int) [a] int  {
            const a = 3;
            return [a] int {1,2};
        }
        """
        input = Program([ConstDecl("a",None,IntLiteral(2)),StructType("STRUCT",[("x",ArrayType([Id("a")],IntType()))],[]),MethodDecl("s",Id("STRUCT"),FuncDecl("foo",[ParamDecl("x",ArrayType([Id("a")],IntType()))],ArrayType([Id("a")],IntType()),Block([Return(FieldAccess(Id("s"),"x"))]))),FuncDecl("foo",[ParamDecl("x",ArrayType([Id("a")],IntType()))],ArrayType([Id("a")],IntType()),Block([ConstDecl("a",None,IntLiteral(3)),Return(ArrayLiteral([Id("a")],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_159(self):
        """
func foo() {
    a := 1;
    var a = 1;
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: a""", inspect.stack()[0].function))

    def test_160(self):
        """
func Votien (b int) {
    for var a = 1; c < 1; a += c {
        const c = 2;
    }
}
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("c"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), Id("c"))),Block([ConstDecl("c",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: c""", inspect.stack()[0].function))

    def test_161(self):
        """
        type TIEN struct {
            Votien int;
        }
        func (v TIEN) foo (v int) {return;}
        func foo () {return;}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_162(self):
        """
        var v TIEN;
        func (v TIEN) foo (v int) int {
            return v;
        }
        """
        input = Program([VarDecl("v",Id("TIEN"), None),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],IntType(),Block([Return(Id("v"))]))),StructType("TIEN",[("Votien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_163(self):
        """
        type A interface {foo();}
        var A = 1;
        """
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]),VarDecl("A", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: A", inspect.stack()[0].function))

    def test_164(self):
        """
        func (v TIEN) VO () {return ;}
        func (v TIEN) Tien () {return ;}
        type TIEN struct {
            Votien int;
            Tien int;
        }
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("VO",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Votien",IntType()),("Tien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: Tien", inspect.stack()[0].function))

    def test_165(self):
        """
        func foo(a int) {
            foo(1);
            var foo = 1;
            foo(2); // error
        }
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([FuncCall("foo",[IntLiteral(1)]),VarDecl("foo", None,IntLiteral(1)),FuncCall("foo",[IntLiteral(2)])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo", inspect.stack()[0].function))

    def test_166(self):
        """
        type TIEN struct {
            Votien int;
        }
        func (v TIEN) Votien () {return ;}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("Votien",[],VoidType(),Block([Return(None)])))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: Votien", inspect.stack()[0].function))

    def test_167(self):
        """
        func (v TIEN) Votien () {return ;}
        type TIEN struct {
            Votien int;
        }
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("Votien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Votien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: Votien", inspect.stack()[0].function))

    def test_168(self):
        """
        func foo(a int) {
            foo(1);
            var foo = 1;
            foo(2);
        }
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([FuncCall("foo",[IntLiteral(1)]),VarDecl("foo", None,IntLiteral(1)),FuncCall("foo",[IntLiteral(2)])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo", inspect.stack()[0].function))

    def test_169(self):
        """
        type TIEN struct {Votien int;}
        type TIEN struct {v int;}
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),StructType("TIEN",[("v",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: TIEN", inspect.stack()[0].function))

    def test_170(self):
        """
        func (v TIEN) VO () {return ;}
        func (v TIEN) Tien () {return ;}
        type TIEN struct {
            Votien int;
            Tien int;
        }
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("VO",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Votien",IntType()),("Tien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: Tien", inspect.stack()[0].function))

    def test_171(self):
        """
        func foo() {
            foo := 1;
            foo()
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("foo"),IntLiteral(1)),FuncCall("foo",[])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo", inspect.stack()[0].function))

    def test_172(self):
        """
        func (v TIEN) VO () {return ;}
        func (v TIEN) Tien () {return ;}
        type TIEN struct {
            Votien int;
            Tien int;
        }
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("VO",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Votien",IntType()),("Tien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Redeclared Method: Tien""", inspect.stack()[0].function))

    def test_173(self):
        """
        func foo() int {
            const foo = 1;
            return foo()
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo""", inspect.stack()[0].function))

    def test_174(self):
        """
        func foo() int {
            const foo = 1;
            return foo()
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo""", inspect.stack()[0].function))

    def test_175(self):
        """Assign struct to incompatible interface (missing method)"""
        input = Program([
            StructType("MyStruct", [], [MethodDecl("s", Id("MyStruct"), FuncDecl("methodA", [], VoidType(), Block([])))]),
            InterfaceType("MyInterface", [Prototype("methodA", [], VoidType()), Prototype("methodB", [], IntType())]), # Needs methodB
            VarDecl("s", Id("MyStruct"), None),
            VarDecl("i", Id("MyInterface"), Id("s")) # Error: MyStruct doesn't implement methodB
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(i,Id(MyInterface),Id(s))", inspect.stack()[0].function))

    def test_176(self):
        """Assign struct to incompatible interface (wrong method signature - param type)"""
        input = Program([
            StructType("MyStruct", [], [MethodDecl("s", Id("MyStruct"), FuncDecl("methodA", [ParamDecl("p", IntType())], VoidType(), Block([])))]), # Takes int param
            InterfaceType("MyInterface", [Prototype("methodA", [FloatType()], VoidType())]), # Expects float param
            VarDecl("s", Id("MyStruct"), None),
            VarDecl("i", Id("MyInterface"), Id("s")) # Error: methodA signature mismatch
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(i,Id(MyInterface),Id(s))", inspect.stack()[0].function))

    def test_177(self):
        """
        func foo() int {
            const foo = 1;
            return foo()
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo""", inspect.stack()[0].function))

    def test_178(self):
        """Type mismatch in for loop update statement (assign float to int)"""
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("i", IntType(), IntLiteral(0)), # Declare i beforehand
                ForStep(Assign(Id("i"), IntLiteral(0)), # Init part needs Stmt, Assign is Stmt
                        BinaryOp("<", Id("i"), IntLiteral(10)),
                        Assign(Id("i"), FloatLiteral(1.0)), # Update part: Assign float to int 'i'
                        Block([]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Assign(Id(i),FloatLiteral(1.0))", inspect.stack()[0].function))

    def test_179(self):
        """Array cell access on a non-array type (string)"""
        input = Program([
            VarDecl("s", StringType(), StringLiteral("hello")),
            VarDecl("c", None, ArrayCell(Id("s"), [IntLiteral(0)])) # Error: s is string
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ArrayCell(Id(s),[IntLiteral(0)])", inspect.stack()[0].function))

    def test_180(self):
        """
        func foo() int {
            const foo = 1;
            return foo()
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo""", inspect.stack()[0].function))

    def test_181(self):
        """
        func foo() int {
            const foo = 1;
            return foo()
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo""", inspect.stack()[0].function))

    def test_182(self):
        """Accessing field on a non-struct type (int)"""
        input = Program([
            VarDecl("x", IntType(), IntLiteral(10)),
            VarDecl("y", None, FieldAccess(Id("x"), "someField")) # Error: x is int
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FieldAccess(Id(x),someField)", inspect.stack()[0].function))

    def test_183(self):
        """Redeclaring a built-in function (putIntLn)"""
        input = Program([
            FuncDecl("putIntLn", [ParamDecl("i", IntType())], VoidType(), Block([]))
        ])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: putIntLn", inspect.stack()[0].function))

    def test_184(self):
        """Type mismatch calling built-in function (putBool with int)"""
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("putBool", [IntLiteral(1)]) # Error: expected boolean
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(putBool,[IntLiteral(1)])", inspect.stack()[0].function))

    def test_185(self):
        """Using result of void built-in function (putLn) in expression"""
        input = Program([
            VarDecl("x", IntType(), FuncCall("putLn", [])) # Error: putLn returns void
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(putLn,[])", inspect.stack()[0].function))

    def test_186(self):
        """Assigning nil to a string variable"""
        input = Program([
            VarDecl("s", StringType(), NilLiteral()) # Error: cannot assign nil to string
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(s,StringType,Nil)", inspect.stack()[0].function))

    def test_187(self):
        """Assigning nil to an array variable"""
        input = Program([
            VarDecl("a", ArrayType([IntLiteral(5)], IntType()), NilLiteral()) # Error: cannot assign nil to array
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(a,ArrayType(IntType,[IntLiteral(5)]),Nil)", inspect.stack()[0].function))

    def test_188(self):
        """Comparing incompatible types (string and int) with =="""
        input = Program([
            VarDecl("res", BoolType(), BinaryOp("==", StringLiteral("1"), IntLiteral(1))) # Error
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(StringLiteral(1),==,IntLiteral(1))", inspect.stack()[0].function))

    def test_189(self):
        """Using logical operator '&&' with non-boolean types (int)"""
        input = Program([
            VarDecl("res", BoolType(), BinaryOp("&&", IntLiteral(1), IntLiteral(0))) # Error
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(IntLiteral(1),&&,IntLiteral(0))", inspect.stack()[0].function))

    def test_190(self):
        """Using unary '!' operator with non-boolean type (float)"""
        input = Program([
            VarDecl("res", BoolType(), UnaryOp("!", FloatLiteral(0.0))) # Error
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: UnaryOp(!,FloatLiteral(0.0))", inspect.stack()[0].function))

    def test_191(self):
        """Return statement with expression in a void function"""
        input = Program([
            FuncDecl("doNothing", [], VoidType(), Block([
                Return(IntLiteral(0)) # Error: void function cannot return a value
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(IntLiteral(0))", inspect.stack()[0].function))

    def test_192(self):
        """Return statement without expression in a non-void function"""
        input = Program([
            FuncDecl("getValue", [], IntType(), Block([
                Return(None) # Error: int function must return an int value
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return()", inspect.stack()[0].function)) # Or Return(None) depending on AST structure

    def test_193(self):
        """Redeclared struct type"""
        input = Program([
            StructType("Point", [("x", IntType())], []),
            StructType("Point", [("y", FloatType())], []) # Error
        ])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: Point", inspect.stack()[0].function))

    def test_194(self):
        """Redeclared interface type"""
        input = Program([
            InterfaceType("Shape", [Prototype("Area", [], FloatType())]),
            InterfaceType("Shape", [Prototype("Perimeter", [], FloatType())]) # Error
        ])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: Shape", inspect.stack()[0].function))

    def test_195(self):
        """Using range on a non-array type in ForEach"""
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("notAnArray", IntType(), IntLiteral(10)),
                VarDecl("idx", IntType(), IntLiteral(0)),
                VarDecl("val", IntType(), IntLiteral(0)),
                ForEach(Id("idx"), Id("val"), Id("notAnArray"), Block([])) # Error: notAnArray is int
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ForEach(Id(idx),Id(val),Id(notAnArray),Block([]))", inspect.stack()[0].function))

    def test_196(self):
        """Redeclared variable in the same block"""
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", IntType(), IntLiteral(1)),
                VarDecl("a", StringType(), StringLiteral("hello")) # Error
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a", inspect.stack()[0].function))

    def test_197(self):
        """Redeclared constant in the same block"""
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                ConstDecl("C", IntType(), IntLiteral(1)),
                ConstDecl("C", FloatType(), FloatLiteral(1.0)) # Error
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: C", inspect.stack()[0].function))

    def test_198(self):
        """VarDecl shadowing a global constant"""
        input = Program([
            ConstDecl("G", IntType(), IntLiteral(10)),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("G", StringType(), StringLiteral("shadow")) # This is allowed (shadowing)
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function)) # Should pass

    def test_199(self):
        """Accessing a shadowed global variable"""
        input = Program([
            VarDecl("x", IntType(), IntLiteral(1)),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("x", StringType(), StringLiteral("local")),
                FuncCall("putInt", [Id("x")])
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(putInt,[Id(x)])", inspect.stack()[0].function))

    def test_200(self):
        """Nested scopes and redeclaration"""
        input = Program([
            VarDecl("x", IntType(), IntLiteral(1)),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("x", IntType(), IntLiteral(2)),
                If(BooleanLiteral(True), Block([
                    VarDecl("x", IntType(), IntLiteral(3))
                ]), None),
                VarDecl("x", IntType(), IntLiteral(4))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: x", inspect.stack()[0].function))

    def test_201(self):
        """Interface method implementation check (return type mismatch)"""
        input = Program([
            StructType("MyStruct", [], [MethodDecl("s", Id("MyStruct"), FuncDecl("methodA", [], IntType(), Block([Return(IntLiteral(1))])))]), # Returns int
            InterfaceType("MyInterface", [Prototype("methodA", [], FloatType())]), # Expects float
            VarDecl("s", Id("MyStruct"), None),
            VarDecl("i", Id("MyInterface"), Id("s"))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(i,Id(MyInterface),Id(s))", inspect.stack()[0].function))

    def test_202(self):
        """Using undeclared variable in update part of for loop"""
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                 VarDecl("i", IntType(), IntLiteral(0)),
                ForStep(Assign(Id("i"), IntLiteral(0)),
                        BinaryOp("<", Id("i"), IntLiteral(10)),
                        Assign(Id("i"), BinaryOp("+", Id("i"), Id("step"))), # Error: 'step' undeclared
                        Block([]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: step", inspect.stack()[0].function))

    def test_203(self):
        """Empty program"""
        input = Program([])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))
    def test_204(self):
        input = Program([])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_205(self):
        input = Program([
            ConstDecl("ZERO", IntType(), IntLiteral(0)),
            ConstDecl("RESULT", IntType(), BinaryOp("/", IntLiteral(1), Id("ZERO")))
        ])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_206(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_207(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(FuncCall("foo",[])),Assign(Id("foo"),IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_208(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo", inspect.stack()[0].function))

    def test_209(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([VarDecl("foo", None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo", inspect.stack()[0].function))

    def test_210(self):
        """
        var v TIEN;
        func (v TIEN) foo (v int) int { return v;}
        type TIEN struct {
            Votien int;
        }
        func (v TIEN) foo (v int) int { return v;}
        """
        input = Program([VarDecl("v",Id("TIEN"), None),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],IntType(),Block([Return(Id("v"))]))),StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],IntType(),Block([Return(Id("v"))])))])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: foo", inspect.stack()[0].function))

    def test_211(self):
        """
        var a int;
        func (v TIEN) foo () int { return a; return v; }
        type TIEN struct {
            Votien int;
        }
        func (v TIEN) foo () int { return a; return v; }
        """
        input = Program([VarDecl("a",IntType(), None),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(Id("a")),Return(Id("v"))]))),StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(Id("a")),Return(Id("v"))])))])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: foo", inspect.stack()[0].function))

    def test_212(self):
        """
        func (v TIEN) Votien () { return; }
        type TIEN struct {
            Votien int;
        }
        func (v TIEN) Votien () { return; }
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("Votien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("Votien",[],VoidType(),Block([Return(None)])))])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: Votien", inspect.stack()[0].function))

    def test_213(self):
        """
        type TIEN struct {
            Votien int;
        }
        func (v TIEN) Votien () { return; }
        func (v TIEN) Votien () { return; }
        """
        input = Program([StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("Votien",[],VoidType(),Block([Return(None)])))]),MethodDecl("v",Id("TIEN"),FuncDecl("Votien",[],VoidType(),Block([Return(None)])))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: Votien", inspect.stack()[0].function))

    def test_214(self):
        """
        func (v TIEN) Tien () { return; }
        type TIEN struct {
            Tien int;
            Votien int;
        }
        func (v TIEN) Tien () { return; }
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Tien",IntType()),("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)])))])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: Tien", inspect.stack()[0].function))

    def test_215(self):
        """
        type TIEN struct {
            Tien int;
            Votien int;
        }
        func (v TIEN) Tien () { return; }
        func (v TIEN) Tien () { return; }
        """
        input = Program([StructType("TIEN",[("Tien",IntType()),("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)])))]),MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)])))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: Tien", inspect.stack()[0].function))

    def test_216(self):
        """
        func (v TIEN) VO () { return; }
        func (v TIEN) Tien () { return; }
        type TIEN struct {
            Tien int;
            Votien int;
        }
        func (v TIEN) VO () { return; }
        func (v TIEN) Tien () { return; }
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("VO",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Tien",IntType()),("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("VO",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)])))])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: VO", inspect.stack()[0].function))

    def test_217(self):
        """
        func foo (a int) {
        foo(1);
        var foo = 1;
        }
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([FuncCall("foo",[IntLiteral(1)]),VarDecl("foo", None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_218(self):
        """
        func foo () int { return 1;}
        func foo1 () int {
        return foo();
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo1",[],IntType(),Block([Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_219(self):
        """
        var foo = 1;
        func foo1 () int {
        return foo();
        }
        """
        input = Program([VarDecl("foo", None,IntLiteral(1)),FuncDecl("foo1",[],IntType(),Block([Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo", inspect.stack()[0].function))

    def test_220(self):
        """
        func foo () {
        var a = 1.0 == 1;
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,BinaryOp("==", FloatLiteral(1.0), IntLiteral(1)))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(FloatLiteral(1.0),==,IntLiteral(1))", inspect.stack()[0].function))

    def test_221(self):
        """
        var a = 1;
        func foo () {
        a = 3;
        var a = 1.0;
        for var a = 1; a > 1; a = 1 { return; }
        }
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(3)),VarDecl("a", None,FloatLiteral(1.0)),ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp(">", Id("a"), IntLiteral(1)),Assign(Id("a"),IntLiteral(1)),Block([Return(None)]))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_222(self):
        """
        func foo () {
        for var a = 1; a > 1; b = b + 1 { return; }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp(">", Id("a"), IntLiteral(1)),Assign(Id("b"),BinaryOp("+", Id("b"), IntLiteral(1))),Block([Return(None)]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: b", inspect.stack()[0].function))

    def test_223(self):
        """
        func foo () int {
        return foo;
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(Id("foo"))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: foo", inspect.stack()[0].function))

    def test_224(self):
        """
        func foo () {
        foo = 1;
        var foo = 1;
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("foo"),IntLiteral(1)),VarDecl("foo", None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: foo", inspect.stack()[0].function))

    def test_225(self):
        """
        func foo () {
        foo = 1;
        foo();
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("foo"),IntLiteral(1)),FuncCall("foo",[])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo", inspect.stack()[0].function))

    def test_226(self):
        """
        func foo () int {
        foo = 1;
        return foo();
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([Assign(Id("foo"),IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo", inspect.stack()[0].function))

    def test_227(self):
        """
        func foo () int {
        var foo = 1;
        return foo();
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([VarDecl("foo", None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo", inspect.stack()[0].function))

    def test_228(self):
        """
        func foo () int {
        const foo = 1;
        return foo();
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo", inspect.stack()[0].function))

    def test_229(self):
        """
        func foo () int {
        return foo();
        foo = 1;
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(FuncCall("foo",[])),Assign(Id("foo"),IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_230(self):
        """
        func foo () { return; }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_231(self):
        """
        func A () int { return A; }
        """
        input = Program([FuncDecl("A",[],IntType(),Block([Return(Id("A"))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: A", inspect.stack()[0].function))

    def test_232(self):
        """
        type A interface { foo (); }
        func foo () int { return A; }
        """
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]),FuncDecl("foo",[],IntType(),Block([Return(Id("A"))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: A", inspect.stack()[0].function))

    def test_233(self):
        """
        type putLn struct { a int; }
        """
        input = Program([StructType("putLn",[("a",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: putLn", inspect.stack()[0].function))

    def test_234(self):
        """
        func foo (a [2]float) {
        foo([2]float{1.0,2.0});
        foo([2]int{1,2});
        }
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],FloatType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])]),FuncCall("foo",[ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(foo,[ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2)])])", inspect.stack()[0].function))

    def test_235(self):
        """
        type S1 struct { votien int; }
        func (s S1) votien1 () { return; }
        type I1 interface { votien1 (); }
        func (s S1) votien1 () { return; }
        var b [2]S1;
        var a [2]I1 = b;
        """
        input = Program([StructType("S1",[("votien",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien1",[],VoidType(),Block([Return(None)])))]),InterfaceType("I1",[Prototype("votien1",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien1",[],VoidType(),Block([Return(None)]))),VarDecl("b",ArrayType([IntLiteral(2)],Id("S1")), None),VarDecl("a",ArrayType([IntLiteral(2)],Id("I1")),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: votien1", inspect.stack()[0].function))

    def test_236(self):
        """
        func votien (a [2]int) {
        votien([3]int{1,2,3});
        }
        """
        input = Program([FuncDecl("votien",[ParamDecl("a",ArrayType([IntLiteral(2)],IntType()))],VoidType(),Block([FuncCall("votien",[ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(votien,[ArrayLiteral([IntLiteral(3)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])", inspect.stack()[0].function))

    def test_237(self):
        """
        var a [1+9]int;
        var b [10]int = a;
        """
        input = Program([VarDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(9))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(10)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_238(self):
        """
        var a [2*5]int;
        var b [10]int = a;
        """
        input = Program([VarDecl("a",ArrayType([BinaryOp("*", IntLiteral(2), IntLiteral(5))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(10)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_239(self):
        """
        var a [5/2]int;
        var b [2]int = a;
        """
        input = Program([VarDecl("a",ArrayType([BinaryOp("/", IntLiteral(5), IntLiteral(2))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(2)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_240(self):
        """
        var a [5%2]int;
        var b [1]int = a;
        """
        input = Program([VarDecl("a",ArrayType([BinaryOp("%", IntLiteral(5), IntLiteral(2))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(1)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_241(self):
        """
        var a [5-2]int;
        var b [3]int = a;
        """
        input = Program([VarDecl("a",ArrayType([BinaryOp("-", IntLiteral(5), IntLiteral(2))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(3)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_242(self):
        """
        const a = 2 + 3;
        var b [a*2 + a]int;
        var c [15]int = b;
        """
        input = Program([ConstDecl("a",None,BinaryOp("+", IntLiteral(2), IntLiteral(3))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(15)],IntType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_243(self):
        """
        const v = 3;
        const a = v + v;
        var b [a*2 + a]int;
        var c [18]int = b;
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("a",None,BinaryOp("+", Id("v"), Id("v"))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(18)],IntType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_244(self):
        """
        const v = 3;
        var c [3]int = [v*1]int {1,2,3};
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),ArrayLiteral([BinaryOp("*", Id("v"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_245(self):
        """
        const v = 3;
        const k = v + 1;
        func foo (a [1+2]int) {
        foo([k-1]int{1,2,3});
        }
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("k",None,BinaryOp("+", Id("v"), IntLiteral(1))),FuncDecl("foo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([BinaryOp("-", Id("k"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_246(self):
        """
        type K struct { a int; }
        func (k K) koo (a [1+2]int) { return; }
        func (k K) koo (a [1+2]int) { return; }
        const c = 4;
        func foo () {
        var k K;
        k.koo([c-1]int{1,2,3});
        }
        """
        input = Program([StructType("K",[("a",IntType())],[MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([Return(None)])))]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([Return(None)]))),ConstDecl("c",None,IntLiteral(4)),FuncDecl("foo",[],VoidType(),Block([VarDecl("k",Id("K"), None),MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: koo", inspect.stack()[0].function))

    def test_247(self):
        """
        type K struct { a int; }
        func (k K) koo (a [1+2]int) { return; }
        func (k K) koo (a [1+2]int) { return; }
        type H interface { koo(a [1+2]int); }
        const c = 4;
        func foo () {
        var k H;
        k.koo([c-1]int{1,2,3});
        }
        """
        input = Program([StructType("K",[("a",IntType())],[MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([Return(None)])))]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([Return(None)]))),InterfaceType("H",[Prototype("koo",[ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType())],VoidType())]),ConstDecl("c",None,IntLiteral(4)),FuncDecl("foo",[],VoidType(),Block([VarDecl("k",Id("H"), None),MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: koo", inspect.stack()[0].function))

    def test_248(self):
        """
        type K struct { a int; }
        func (k K) koo (a [1+2]int) [1+2]int { return [3*1]int{1,2,3}; }
        func (k K) koo (a [1+2]int) [1+2]int { return [3*1]int{1,2,3}; }
        type H interface { koo(a [1+2]int) [1+2]int; }
        const c = 4;
        func foo () [1+2]int {
        return Func...
        }
        """
        input = Program([StructType("K",[("a",IntType())],[MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()),Block([Return(ArrayLiteral([BinaryOp("*", IntLiteral(3), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])))]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()),Block([Return(ArrayLiteral([BinaryOp("*", IntLiteral(3), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))),InterfaceType("H",[Prototype("koo",[ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType())],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))]),ConstDecl("c",None,IntLiteral(4)),FuncDecl("foo",[],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()),Block([Return(FuncCall("Func...",[]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: koo", inspect.stack()[0].function))

    def test_249(self):
        """
        const a = "2" + "#";
        const b = a * 5;
        """
        input = Program([ConstDecl("a",None,BinaryOp("+", StringLiteral('"2"'), StringLiteral('"#"'))),ConstDecl("b",None,BinaryOp("*", Id("a"), IntLiteral(5)))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(Id(a),*,IntLiteral(5))", inspect.stack()[0].function))

    def test_250(self):
        """
        var v = 2 * 3;
        const a = v + 1;
        const b = a * 5;
        const c = !(b > 3);
        """
        input = Program([VarDecl("v", None,BinaryOp("*", IntLiteral(2), IntLiteral(3))),ConstDecl("a",None,BinaryOp("+", Id("v"), IntLiteral(1))),ConstDecl("b",None,BinaryOp("*", Id("a"), IntLiteral(5))),ConstDecl("c",None,UnaryOp("!",BinaryOp(">", Id("b"), IntLiteral(3))))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_251(self):
        """
        var a [2][3][4]int;
        var b [3][4]int = a[1];
        var c [4]int = a[1][1];
        var d int = a[1][1][1];
        """
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3),IntLiteral(4)],IntType()), None),VarDecl("b",ArrayType([IntLiteral(3),IntLiteral(4)],IntType()),ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(4)],IntType()),ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(1)])),VarDecl("d",IntType(),ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(1),IntLiteral(1)]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_252(self):
        """
        const a = 3;
        const b = -a;
        const c = -b;
        var d [c]int = [3]int{1,2,3};
        """
        input = Program([ConstDecl("a",None,IntLiteral(3)),ConstDecl("b",None,UnaryOp("-",Id("a"))),ConstDecl("c",None,UnaryOp("-",Id("b"))),VarDecl("d",ArrayType([Id("c")],IntType()),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_253(self):
        """
        func foo () { a[3] = 1; }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[IntLiteral(3)]),IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: a", inspect.stack()[0].function))

    def test_254(self):
        """
        func foo () { a.c = 1; }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(Id("a"),"c"),IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: a", inspect.stack()[0].function))

    def test_255(self):
        """
        func foo () {
        a = 1;
        var a = 1;
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a", inspect.stack()[0].function))

    def test_256(self):
        """
        func foo () {
        a = 1;
        const a = 1;
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a", inspect.stack()[0].function))

    def test_257(self):
        """
        const a = 1;
        func foo () {
        a = 1.0;
        }
        """
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),FloatLiteral(1.0))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Assign(Id(a),FloatLiteral(1.0))", inspect.stack()[0].function))

    def test_258(self):
        """
        func foo () {
        a = 1.0;
        var b = a;
        b = 1;
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),FloatLiteral(1.0)),VarDecl("b", None,Id("a")),Assign(Id("b"),IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_259(self):
        """
        func foo () { var a = foo; }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,Id("foo"))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: foo", inspect.stack()[0].function))

    def test_260(self):
        """
        func Votien (b int) {
        for var a = 1; c < 1; a = a + 1 {
        const c = 2;
        }
        }
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("c"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("c",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: c", inspect.stack()[0].function))

    def test_261(self):
        """
        func Votien (b int) {
        for var a = 1; c < 1; a = a + c {
        const c = 2;
        }
        }
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("c"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), Id("c"))),Block([ConstDecl("c",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: c", inspect.stack()[0].function))

    def test_262(self):
        """
        func Votien (b int) {
        var array = [2]int{1,2};
        foreach index in value array {
        foreach index in value brray {
        var brray = [2]int{1,2};
        }
        }
        }
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("array", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),ForEach(Id("index"),Id("value"),Id("array"),Block([ForEach(Id("index"),Id("value"),Id("brray"),Block([VarDecl("brray", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))]))]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: index", inspect.stack()[0].function))

    def test_263(self):
        """
        type S1 struct { votien1 int; }
        func (s S1) vo () { return; }
        func (s S1) votien () {
        s.votien();
        var a = s.vo();
        }
        func (s S1) vo () { return; }
        func (s S1) votien () {
        s.votien();
        var a = s.vo();
        }
        """
        input = Program([StructType("S1",[("votien1",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("vo",[],VoidType(),Block([Return(None)]))),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([MethCall(Id("s"),"votien",[]),VarDecl("a", None,MethCall(Id("s"),"vo",[]))])))]),MethodDecl("s",Id("S1"),FuncDecl("vo",[],VoidType(),Block([Return(None)]))),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([MethCall(Id("s"),"votien",[]),VarDecl("a", None,MethCall(Id("s"),"vo",[]))])))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: vo", inspect.stack()[0].function))

    def test_264(self):
        """
        func foo () int { return 1;}
        func votien () int {
        return votien();
        foo();
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("votien",[],IntType(),Block([Return(FuncCall("votien",[])),FuncCall("foo",[])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(foo,[])", inspect.stack()[0].function))

    def test_265(self):
        """
        func foo () { return; }
        func votien () int {
        foo();
        return foo();
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("votien",[],IntType(),Block([FuncCall("foo",[]),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(foo,[])", inspect.stack()[0].function))

    def test_266(self):
        """
        func votien () {
        break;
        continue;
        }
        """
        input = Program([FuncDecl("votien",[],VoidType(),Block([Break(),Continue()]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_267(self):
        """
        type Person struct { age int; name string; }
        func (p Person) Greet () string { return "Hello, " + p.name; }
        func votien () {
        var person = Person { name = "Alice", age = 30 };
        person.name = "John";
        person.age = 30;
        putStringLn(person.name);
        putStringLn(person.Greet());
        }
        func (p Person) Greet () string { return "Hello, " + p.name; }
        """
        input = Program([StructType("Person",[("age",IntType()),("name",StringType())],[MethodDecl("p",Id("Person"),FuncDecl("Greet",[],StringType(),Block([Return(BinaryOp("+", StringLiteral('"Hello, "'), FieldAccess(Id("p"),"name")))])))]),FuncDecl("votien",[],VoidType(),Block([VarDecl("person", None,StructLiteral("Person",[("name",StringLiteral('"Alice"')),("age",IntLiteral(30))])),Assign(FieldAccess(Id("person"),"name"),StringLiteral('"John"')),Assign(FieldAccess(Id("person"),"age"),IntLiteral(30)),FuncCall("putStringLn",[FieldAccess(Id("person"),"name")]),FuncCall("putStringLn",[MethCall(Id("person"),"Greet",[])])])),MethodDecl("p",Id("Person"),FuncDecl("Greet",[],StringType(),Block([Return(BinaryOp("+", StringLiteral('"Hello, "'), FieldAccess(Id("p"),"name")))])))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: Greet", inspect.stack()[0].function))

    def test_268(self):
        """
        var a string;
        func foo () {
        var a int = 2;
        putIntLn(a);
        }
        """
        input = Program([VarDecl("a",StringType(), None),FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(2)),FuncCall("putIntLn",[Id("a")])]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_269(self):
        """
        var a string;
        func foo () {
        putIntLn(a);
        var a int = 2;
        }
        """
        input = Program([VarDecl("a",StringType(), None),FuncDecl("foo",[],VoidType(),Block([FuncCall("putIntLn",[Id("a")]),VarDecl("a",IntType(),IntLiteral(2))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(putIntLn,[Id(a)])", inspect.stack()[0].function))

    def test_270(self):
        """
        var a TIEN;
        func foo () {
        a.tien = a.tien + 2;
        putIntLn(a.tien);
        foo();
        }
        var b = foo();
        type TIEN struct { tien int; }
        """
        input = Program([VarDecl("a",Id("TIEN"), None),FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(Id("a"),"tien"),BinaryOp("+", FieldAccess(Id("a"),"tien"), IntLiteral(2))),FuncCall("putIntLn",[FieldAccess(Id("a"),"tien")]),FuncCall("foo",[])])),VarDecl("b", None,FuncCall("foo",[])),StructType("TIEN",[("tien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(foo,[])", inspect.stack()[0].function))

    def test_271(self):
        """
        var a TIEN;
        func foo () TIEN {
        return a;
        return TIEN;
        }
        type TIEN struct { tien int; }
        """
        input = Program([VarDecl("a",Id("TIEN"), None),FuncDecl("foo",[],Id("TIEN"),Block([Return(Id("a")),Return(Id("TIEN"))])),StructType("TIEN",[("tien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: TIEN", inspect.stack()[0].function))

    def test_272(self):
        """
        func foo () int {
        return [2]int{1,2}[a];
        }
        var a = foo();
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(ArrayCell(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),[Id("a")]))])),VarDecl("a", None,FuncCall("foo",[]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: a", inspect.stack()[0].function))

    def test_273(self):
        """
        var a = 1;
        func foo () float {
        return [2]int{1,2}[a];
        }
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],FloatType(),Block([Return(ArrayCell(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),[Id("a")]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(ArrayCell(ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2)]),[Id(a)]))", inspect.stack()[0].function))

    def test_274(self):
        """
        var a = 1;
        func foo () {
        return a;
        }
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Return(Id("a"))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(Id(a))", inspect.stack()[0].function))

    def test_275(self):
        """
        func foo () { return; }
        func foo () int { return 1;}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: foo", inspect.stack()[0].function))

    def test_276(self):
        """
        func foo () { return; }
        func koo () int {
        return foo();
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("koo",[],IntType(),Block([Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(foo,[])", inspect.stack()[0].function))

    def test_277(self):
        """
        func putLn () { return; }
        """
        input = Program([FuncDecl("putLn",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: putLn", inspect.stack()[0].function))

    def test_278(self):
        """
        var putLn int;
        """
        input = Program([VarDecl("putLn",IntType(), None)])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: putLn", inspect.stack()[0].function))

    def test_279(self):
        """
        type putLn struct { a int; }
        """
        input = Program([StructType("putLn",[("a",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: putLn", inspect.stack()[0].function))

    def test_280(self):
        """
        type putLn interface { foo (); }
        """
        input = Program([InterfaceType("putLn",[Prototype("foo",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: putLn", inspect.stack()[0].function))

    def test_281(self):
        """
        var a int = getBool();
        """
        input = Program([VarDecl("a",IntType(),FuncCall("getBool",[]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(a,IntType,FuncCall(getBool,[]))", inspect.stack()[0].function))

    def test_282(self):
        """
        func foo () { putFloat(getInt()); }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("putFloat",[FuncCall("getInt",[])])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(putFloat,[FuncCall(getInt,[])])", inspect.stack()[0].function))

    def test_283(self):
        """
        func foo () { putLn(getInt()); }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("putLn",[FuncCall("getInt",[])])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(putLn,[FuncCall(getInt,[])])", inspect.stack()[0].function))

    def test_284(self):
        """
        func foo () { putIntLn(); }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("putIntLn",[])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(putIntLn,[])", inspect.stack()[0].function))

    def test_285(self):
        """
        func foo () {
        putFloat(1.0);
        putIntLn(1, 2);
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("putFloat",[FloatLiteral(1.0)]),FuncCall("putIntLn",[IntLiteral(1),IntLiteral(2)])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(putIntLn,[IntLiteral(1),IntLiteral(2)])", inspect.stack()[0].function))

    def test_286(self):
        """
        func foo () [2]float {
        return [2]float{1.0, 2.0};
        return [2]int{1, 2};
        }
        """
        input = Program([FuncDecl("foo",[],ArrayType([IntLiteral(2)],FloatType()),Block([Return(ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])),Return(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2)]))", inspect.stack()[0].function))

    def test_287(self):
        """
        type TIEN struct { a [2]int; }
        func (v TIEN) foo () int { return 1; }
        type VO interface { foo () int; }
        func (v TIEN) foo () int { return 1; }
        func foo () TIEN { return TIEN { a = [2]int{1,2} }; }
        func coco () TIEN {
        var a VO = foo();
        return a;
        }
        """
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[],Id("TIEN"),Block([Return(StructLiteral("TIEN",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])),FuncDecl("coco",[],Id("TIEN"),Block([VarDecl("a",Id("VO"),FuncCall("foo",[])),Return(Id("a"))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: foo", inspect.stack()[0].function))

    def test_288(self):
        """
        type TIEN struct { a [2]int; }
        func (v TIEN) foo () int { return 1; }
        type VO interface { foo () int; }
        func (v TIEN) foo () int { return 1; }
        func foo () {
        var b VO = TIEN { a = [2]int{1,2} };
        var a TIEN = b;
        }
        """
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("b",Id("VO"),StructLiteral("TIEN",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),VarDecl("a",Id("TIEN"),Id("b"))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: foo", inspect.stack()[0].function))

    def test_289(self):
        """
        type TIEN struct { a [2]int; }
        func (v TIEN) foo () int { return 1; }
        type VO interface { foo () int; }
        func (v TIEN) foo () int { return 1; }
        func foo () {
        var b = TIEN { a = [2]int{1,2} };
        var a int = b.a[1];
        }
        """
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,StructLiteral("TIEN",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),VarDecl("a",IntType(),ArrayCell(FieldAccess(Id("b"),"a"),[IntLiteral(1)]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: foo", inspect.stack()[0].function))

    def test_290(self):
        """
        type TIEN struct { a [2]int; }
        func (v TIEN) foo () int { return 1; }
        type VO interface { foo () int; }
        func (v TIEN) foo () int { return 1; }
        func foo (a VO) {
        var b VO = TIEN { a = [2]int{1,2} };
        foo(b);
        }
        """
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("VO"))],VoidType(),Block([VarDecl("b",Id("VO"),StructLiteral("TIEN",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),FuncCall("foo",[Id("b")])]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: foo", inspect.stack()[0].function))

    def test_291(self):
        """
        type TIEN struct { a [2]int; }
        func (v TIEN) foo () int { return 1; }
        type VO interface { foo () int; }
        func (v TIEN) foo () int { return 1; }
        func foo (a VO) {
        var b = TIEN { a = [2]int{1,2} };
        foo(b);
        }
        """
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("VO"))],VoidType(),Block([VarDecl("b", None,StructLiteral("TIEN",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),FuncCall("foo",[Id("b")])]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: foo", inspect.stack()[0].function))

    def test_292(self):
        """
        type TIEN struct { a [2]int; }
        func (v TIEN) foo () int { return 1; }
        type VO interface { foo () int; }
        func (v TIEN) foo () int { return 1; }
        func foo (a VO) {
        var b = nil;
        foo(nil);
        }
        """
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("VO"))],VoidType(),Block([VarDecl("b", None,NilLiteral()),FuncCall("foo",[NilLiteral()])]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: foo", inspect.stack()[0].function))

    def test_293(self):
        """
        type TIEN struct { a [2]int; }
        func foo () TIEN { return nil; }
        """
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),FuncDecl("foo",[],Id("TIEN"),Block([Return(NilLiteral())]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_294(self):
        """
        func foo () int {
        if true { var a = 1; } else { var a = 2;}
        return a;
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([If(BooleanLiteral(True), Block([VarDecl("a", None,IntLiteral(1))]), Block([VarDecl("a", None,IntLiteral(2))])),Return(Id("a"))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: a", inspect.stack()[0].function))

    def test_295(self):
        """
        func foo () int {
        var a = 1;
        if a < 3 { var a = 1; } else if a > 2 { var a = 2; }
        return a;
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1)),If(BinaryOp("<", Id("a"), IntLiteral(3)), Block([VarDecl("a", None,IntLiteral(1))]), If(BinaryOp(">", Id("a"), IntLiteral(2)), Block([VarDecl("a", None,IntLiteral(2))]), None)),Return(Id("a"))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_296(self):
        """
        func foo () {
        var a int = 2.0 * 1;
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(),BinaryOp("*", FloatLiteral(2.0), IntLiteral(1)))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(a,IntType,BinaryOp(FloatLiteral(2.0),*,IntLiteral(1)))", inspect.stack()[0].function))

    def test_297(self):
        """
func foo() {
    var a = foo
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,Id("foo"))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: foo""", inspect.stack()[0].function))

    def test_297(self):
        """
func foo() {
    var a = foo
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,Id("foo"))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: foo""", inspect.stack()[0].function))

    def test_298(self):
        """
        func foo () {
            var a = 1;
            var b = 1;
            for a, b := range [3]int {1, 2, 3} {
                var b = 1;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("b", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_299(self):
        """
        var a = 1;
        func foo () {
            const b = 1;
            for a, c := range [3]int{1, 2, 3} {
                var d = c;
            }
            var d = a;
            var a = 1;
        }
        var d = b;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("c"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("d", None,Id("c"))])),VarDecl("d", None,Id("a")),VarDecl("a", None,IntLiteral(1))])),VarDecl("d", None,Id("b"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: c", inspect.stack()[0].function))

    def test_300(self):
        """
        func Votien () {
            var array = [2] int {1,2}
            var index int;
            var value float;
            for index, value := range array {
                return;
            }
        }
        """
        input = Program([FuncDecl("Votien",[],VoidType(),Block([VarDecl("array", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("index",IntType(), None),VarDecl("value",FloatType(), None),ForEach(Id("index"),Id("value"),Id("array"),Block([Return(None)]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ForEach(Id(index),Id(value),Id(array),Block([Return()]))", inspect.stack()[0].function))

    def test_301(self):
        """
        func Votien () {
            var array [2][3] int;
            var index int;
            var value [3] int;
            for index, value := range array {
                var value [2] int;
                for index, value := range array {
                    return
                }
            }


        }
        """
        input = Program([FuncDecl("Votien",[],VoidType(),Block([VarDecl("array",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("index",IntType(), None),VarDecl("value",ArrayType([IntLiteral(3)],IntType()), None),ForEach(Id("index"),Id("value"),Id("array"),Block([VarDecl("value",ArrayType([IntLiteral(2)],IntType()), None),ForEach(Id("index"),Id("value"),Id("array"),Block([Return(None)]))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ForEach(Id(index),Id(value),Id(array),Block([Return()]))", inspect.stack()[0].function))

    def test_302(self):
        """
        const v = 3;
        const k = v + 1;
        func foo(a [1 + 2] int) {
            foo([k - 1] int {1,2,3})
        }
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("k",None,BinaryOp("+", Id("v"), IntLiteral(1))),FuncDecl("foo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([BinaryOp("-", Id("k"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input, "VOTIEN", inspect.stack()[0].function))

    def test_303(self):
        """
        type TIEN struct {
            a int;
        }
        type VO interface {
            fooA();

        }
        func (v TIEN) fooA() {return ;}

        func Votien () {
            var array [3] TIEN;
            var index int;
            var value VO;
            for index, value := range array {
                return;
            }
        }
        """
        input = Program([StructType("TIEN",[("a",IntType())],[]),InterfaceType("VO",[Prototype("fooA",[],VoidType())]),MethodDecl("v",Id("TIEN"),FuncDecl("fooA",[],VoidType(),Block([Return(None)]))),FuncDecl("Votien",[],VoidType(),Block([VarDecl("array",ArrayType([IntLiteral(3)],Id("TIEN")), None),VarDecl("index",IntType(), None),VarDecl("value",Id("VO"), None),ForEach(Id("index"),Id("value"),Id("array"),Block([Return(None)]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ForEach(Id(index),Id(value),Id(array),Block([Return()]))", inspect.stack()[0].function))

    def test_304(self):
        """
        type TIEN struct {
            a int;
        }
        type VO interface {
            fooA();

        }
        func (v TIEN) fooA() {return ;}

        func Votien () {
            var array [3][3] TIEN;
            var index int;
            var value [3]VO;
            for index, value := range array {
                return;
            }
        }
        """
        input = Program([StructType("TIEN",[("a",IntType())],[]),InterfaceType("VO",[Prototype("fooA",[],VoidType())]),MethodDecl("v",Id("TIEN"),FuncDecl("fooA",[],VoidType(),Block([Return(None)]))),FuncDecl("Votien",[],VoidType(),Block([VarDecl("array",ArrayType([IntLiteral(3),IntLiteral(3)],Id("TIEN")), None),VarDecl("index",IntType(), None),VarDecl("value",ArrayType([IntLiteral(3)],Id("VO")), None),ForEach(Id("index"),Id("value"),Id("array"),Block([Return(None)]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ForEach(Id(index),Id(value),Id(array),Block([Return()]))", inspect.stack()[0].function))

    def test_305(self):
        """
        type S1 struct {votien int;}
        type S2 struct {votien int;}
        type I1 interface {votien() S1;}
        type I2 interface {votien() S2;}

        func (s S1) votien() S1 {return s;}

        var a S1;
        var c I1 = a;
        var d I2 = a;
        """
        input = Program(
            [
                StructType("S1", [("votien", IntType())], []),
                StructType("S2", [("votien", IntType())], []),
                InterfaceType("I1", [Prototype("votien", [], Id("S1"))]),
                InterfaceType("I2", [Prototype("votien", [], Id("S2"))]),
                MethodDecl(
                    "s",
                    Id("S1"),
                    FuncDecl("votien", [], Id("S1"), Block([Return(Id("s"))])),
                ),
                VarDecl("a", Id("S1"), None),
                VarDecl("c", Id("I1"), Id("a")),
                VarDecl("d", Id("I2"), Id("a")),
            ]
        )
        self.assertTrue(
            TestChecker.test(
                input,
                "Type Mismatch: VarDecl(d,Id(I2),Id(a))",
                inspect.stack()[0].function,
            )
        )

    def test_306(self):
        input = Program([VarDecl("VoTien", None, IntLiteral(1)), VarDecl("VoTien", None, IntLiteral(2))])
        expect = "Redeclared Variable: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 306))

    def test_307(self):
        input = Program([VarDecl("VoTien", None, IntLiteral(1)), ConstDecl("VoTien", None, IntLiteral(2))])
        expect = "Redeclared Constant: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 307))

    def test_308(self):
        input = Program([ConstDecl("VoTien", None, IntLiteral(1)), VarDecl("VoTien", None, IntLiteral(2))])
        expect = "Redeclared Variable: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 308))

    def test_309(self):
        input = Program([ConstDecl("VoTien", None, IntLiteral(1)), FuncDecl("VoTien", [], VoidType(), Block([Return(None)]))])
        expect = "Redeclared Function: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 309))

    def test_310(self):
        input = Program([FuncDecl("VoTien", [], VoidType(), Block([Return(None)])), VarDecl("VoTien", None, IntLiteral(1))])
        expect = "Redeclared Variable: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 310))

    def test_311(self):
        input = Program([VarDecl("getInt", None, IntLiteral(1))])
        expect = "Redeclared Variable: getInt"
        self.assertTrue(TestChecker.test(input, expect, 311))

    def test_312(self):
        input = Program([
            StructType("Votien", [("Votien", IntType())], []),
            StructType("TIEN", [("Votien", StringType()), ("TIEN", IntType()), ("TIEN", FloatType())], [])
        ])
        expect = "Redeclared Field: TIEN"
        self.assertTrue(TestChecker.test(input, expect, 312))

    def test_313(self):
        input = Program([
            MethodDecl("v", Id("TIEN"), FuncDecl("putIntLn", [], VoidType(), Block([Return(None)]))),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))),
            StructType("TIEN", [("Votien", IntType())], [])
        ])
        expect = "Redeclared Method: getInt"
        self.assertTrue(TestChecker.test(input, expect, 313))

    def test_314(self):
        input = Program([
            InterfaceType("VoTien", [
                Prototype("VoTien", [], VoidType()),
                Prototype("VoTien", [IntType()], VoidType())
            ])
        ])
        expect = "Redeclared Prototype: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 314))

    def test_315(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("a", IntType()), ParamDecl("a", IntType())], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 315))

    def test_316(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("b", IntType())], VoidType(), Block([
                VarDecl("b", None, IntLiteral(1)),
                VarDecl("a", None, IntLiteral(1)),
                ConstDecl("a", None, IntLiteral(1))
            ]))
        ])
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 316))

    def test_317(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("b", IntType())], VoidType(), Block([
                ForStep(
                    VarDecl("a", None, IntLiteral(1)),
                    BinaryOp("<", Id("a"), IntLiteral(1)),
                    Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))),
                    Block([ConstDecl("a", None, IntLiteral(2))])
                )
            ]))
        ])
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 317))

    def test_318(self):
        input = Program([
            VarDecl("a", None, IntLiteral(1)),
            VarDecl("b", None, Id("a")),
            VarDecl("c", None, Id("d"))
        ])
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 318))

    def test_319(self):
        input = Program([
            FuncDecl("Votien", [], IntType(), Block([Return(IntLiteral(1))])),
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("b", None, FuncCall("Votien", [])),
                FuncCall("foo_votine", []),
                Return(None)
            ]))
        ])
        expect = "Undeclared Function: foo_votine"
        self.assertTrue(TestChecker.test(input, expect, 319))

    def test_320(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                ConstDecl("c", None, FieldAccess(Id("v"), "Votien")),
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien"
        self.assertTrue(TestChecker.test(input, expect, 320))

    def test_321(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                MethCall(Id("v"), "getInt", []),
                MethCall(Id("v"), "putInt", [])
            ])))
        ])
        expect = "Undeclared Method: putInt"
        self.assertTrue(TestChecker.test(input, expect, 321))

    def test_322(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien"
        self.assertTrue(TestChecker.test(input, expect, 322))

    def test_323(self):
        input = Program([
            StructType("TIEN", [("a", IntType())], []),
            StructType("VO", [("a", IntType())], []),
            InterfaceType("TIEN", [Prototype("foo", [], VoidType())])
        ])
        expect = "Redeclared Type: TIEN"
        self.assertTrue(TestChecker.test(input, expect, 323))

    def test_324(self):
        input = Program([
            InterfaceType("TIEN", [
                Prototype("foo", [], VoidType()),
                Prototype("foo", [IntType(), IntType()], VoidType())
            ])
        ])
        expect = "Redeclared Prototype: foo"
        self.assertTrue(TestChecker.test(input, expect, 324))

    def test_325(self):
        input = Program([
            FuncDecl("putInt", [], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input, expect, 325))

    def test_326(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 326))

    def test_327(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                ConstDecl("c", None, FieldAccess(Id("v"), "Votien")),
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien"
        self.assertTrue(TestChecker.test(input, expect, 327))

    def test_328(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                MethCall(Id("v"), "getInt", []),
                MethCall(Id("v"), "putInt", [])
            ])))
        ])
        expect = "Undeclared Method: putInt"
        self.assertTrue(TestChecker.test(input, expect, 328))

    def test_329(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien"
        self.assertTrue(TestChecker.test(input, expect, 329))

    def test_330(self):
        input = Program([
            StructType("TIEN", [("a", IntType())], []),
            StructType("VO", [("a", IntType())], []),
            InterfaceType("TIEN", [Prototype("foo", [], VoidType())])
        ])
        expect = "Redeclared Type: TIEN"
        self.assertTrue(TestChecker.test(input, expect, 330))

    def test_331(self):
        input = Program([
            InterfaceType("TIEN", [
                Prototype("foo", [], VoidType()),
                Prototype("foo", [IntType(), IntType()], VoidType())
            ])
        ])
        expect = "Redeclared Prototype: foo"
        self.assertTrue(TestChecker.test(input, expect, 331))

    def test_332(self):
        input = Program([
            FuncDecl("putInt", [], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input, expect, 332))

    def test_333(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 333))

    def test_335(self):
        input = Program([VarDecl("VoTien", None, IntLiteral(1)), VarDecl("VoTien", None, IntLiteral(2))])
        expect = "Redeclared Variable: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 335))

    def test_336(self):
        input = Program([VarDecl("VoTien", None, IntLiteral(1)), ConstDecl("VoTien", None, IntLiteral(2))])
        expect = "Redeclared Constant: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 336))

    def test_337(self):
        input = Program([ConstDecl("VoTien", None, IntLiteral(1)), VarDecl("VoTien", None, IntLiteral(2))])
        expect = "Redeclared Variable: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 337))

    def test_338(self):
        input = Program([ConstDecl("VoTien", None, IntLiteral(1)), FuncDecl("VoTien", [], VoidType(), Block([Return(None)]))])
        expect = "Redeclared Function: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 338))

    def test_339(self):
        input = Program([FuncDecl("VoTien", [], VoidType(), Block([Return(None)])), VarDecl("VoTien", None, IntLiteral(1))])
        expect = "Redeclared Variable: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 339))

    def test_340(self):
        input = Program([VarDecl("getInt", None, IntLiteral(1))])
        expect = "Redeclared Variable: getInt"
        self.assertTrue(TestChecker.test(input, expect, 340))

    def test_341(self):
        input = Program([
            StructType("Votien", [("Votien", IntType())], []),
            StructType("TIEN", [("Votien", StringType()), ("TIEN", IntType()), ("TIEN", FloatType())], [])
        ])
        expect = "Redeclared Field: TIEN"
        self.assertTrue(TestChecker.test(input, expect, 341))

    def test_342(self):
        input = Program([
            MethodDecl("v", Id("TIEN"), FuncDecl("putIntLn", [], VoidType(), Block([Return(None)]))),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))),
            StructType("TIEN", [("Votien", IntType())], [])
        ])
        expect = "Redeclared Method: getInt"
        self.assertTrue(TestChecker.test(input, expect, 342))

    def test_343(self):
        input = Program([
            InterfaceType("VoTien", [
                Prototype("VoTien", [], VoidType()),
                Prototype("VoTien", [IntType()], VoidType())
            ])
        ])
        expect = "Redeclared Prototype: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 343))

    def test_344(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("a", IntType()), ParamDecl("a", IntType())], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 344))

    def test_345(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("b", IntType())], VoidType(), Block([
                VarDecl("b", None, IntLiteral(1)),
                VarDecl("a", None, IntLiteral(1)),
                ConstDecl("a", None, IntLiteral(1))
            ]))
        ])
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 345))

    def test_346(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("b", IntType())], VoidType(), Block([
                ForStep(
                    VarDecl("a", None, IntLiteral(1)),
                    BinaryOp("<", Id("a"), IntLiteral(1)),
                    Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))),
                    Block([ConstDecl("a", None, IntLiteral(2))])
                )
            ]))
        ])
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 346))

    def test_347(self):
        input = Program([
            VarDecl("a", None, IntLiteral(1)),
            VarDecl("b", None, Id("a")),
            VarDecl("c", None, Id("d"))
        ])
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 347))

    def test_348(self):
        input = Program([
            FuncDecl("Votien", [], IntType(), Block([Return(IntLiteral(1))])),
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("b", None, FuncCall("Votien", [])),
                FuncCall("foo_votine", []),
                Return(None)
            ]))
        ])
        expect = "Undeclared Function: foo_votine"
        self.assertTrue(TestChecker.test(input, expect, 348))

    def test_349(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                ConstDecl("c", None, FieldAccess(Id("v"), "Votien")),
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien"
        self.assertTrue(TestChecker.test(input, expect, 349))

    def test_350(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                MethCall(Id("v"), "getInt", []),
                MethCall(Id("v"), "putInt", [])
            ])))
        ])
        expect = "Undeclared Method: putInt"
        self.assertTrue(TestChecker.test(input, expect, 350))

    def test_351(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien"
        self.assertTrue(TestChecker.test(input, expect, 351))

    def test_352(self):
        input = Program([
            StructType("TIEN", [("a", IntType())], []),
            StructType("VO", [("a", IntType())], []),
            InterfaceType("TIEN", [Prototype("foo", [], VoidType())])
        ])
        expect = "Redeclared Type: TIEN"
        self.assertTrue(TestChecker.test(input, expect, 352))

    def test_353(self):
        input = Program([
            InterfaceType("TIEN", [
                Prototype("foo", [], VoidType()),
                Prototype("foo", [IntType(), IntType()], VoidType())
            ])
        ])
        expect = "Redeclared Prototype: foo"
        self.assertTrue(TestChecker.test(input, expect, 353))

    def test_354(self):
        input = Program([
            FuncDecl("putInt", [], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input, expect, 354))

    def test_355(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 355))

    def test_356(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                ConstDecl("c", None, FieldAccess(Id("v"), "Votien")),
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien"
        self.assertTrue(TestChecker.test(input, expect, 356))

    def test_357(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                MethCall(Id("v"), "getInt", []),
                MethCall(Id("v"), "putInt", [])
            ])))
        ])
        expect = "Undeclared Method: putInt"
        self.assertTrue(TestChecker.test(input, expect, 357))

    def test_358(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien"
        self.assertTrue(TestChecker.test(input, expect, 358))

    def test_359(self):
        input = Program([
            StructType("TIEN", [("a", IntType())], []),
            StructType("VO", [("a", IntType())], []),
            InterfaceType("TIEN", [Prototype("foo", [], VoidType())])
        ])
        expect = "Redeclared Type: TIEN"
        self.assertTrue(TestChecker.test(input, expect, 359))

    def test_360(self):
        input = Program([
            InterfaceType("TIEN", [
                Prototype("foo", [], VoidType()),
                Prototype("foo", [IntType(), IntType()], VoidType())
            ])
        ])
        expect = "Redeclared Prototype: foo"
        self.assertTrue(TestChecker.test(input, expect, 360))

    def test_361(self):
        input = Program([
            FuncDecl("putInt", [], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input, expect, 361))

    def test_362(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 362))

    def test_363(self):
        input = Program([VarDecl("VoTien", None, IntLiteral(1)), VarDecl("VoTien", None, IntLiteral(2))])
        expect = "Redeclared Variable: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 363))

    def test_364(self):
        input = Program([VarDecl("VoTien", None, IntLiteral(1)), ConstDecl("VoTien", None, IntLiteral(2))])
        expect = "Redeclared Constant: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 364))

    def test_365(self):
        input = Program([ConstDecl("VoTien", None, IntLiteral(1)), VarDecl("VoTien", None, IntLiteral(2))])
        expect = "Redeclared Variable: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 365))

    def test_366(self):
        input = Program([ConstDecl("VoTien", None, IntLiteral(1)), FuncDecl("VoTien", [], VoidType(), Block([Return(None)]))])
        expect = "Redeclared Function: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 366))

    def test_367(self):
        input = Program([FuncDecl("VoTien", [], VoidType(), Block([Return(None)])), VarDecl("VoTien", None, IntLiteral(1))])
        expect = "Redeclared Variable: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 367))

    def test_368(self):
        input = Program([VarDecl("getInt", None, IntLiteral(1))])
        expect = "Redeclared Variable: getInt"
        self.assertTrue(TestChecker.test(input, expect, 368))

    def test_369(self):
        input = Program([ConstDecl("VoTien", None, IntLiteral(1)), VarDecl("VoTien", None, IntLiteral(2))])
        expect = "Redeclared Variable: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 369))

    def test_370(self):
        input = Program([ConstDecl("VoTien", None, IntLiteral(1)), FuncDecl("VoTien", [], VoidType(), Block([Return(None)]))])
        expect = "Redeclared Function: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 370))

    def test_371(self):
        input = Program([FuncDecl("VoTien", [], VoidType(), Block([Return(None)])), VarDecl("VoTien", None, IntLiteral(1))])
        expect = "Redeclared Variable: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 371))

    def test_372(self):
        input = Program([VarDecl("getInt", None, IntLiteral(1))])
        expect = "Redeclared Variable: getInt"
        self.assertTrue(TestChecker.test(input, expect, 372))

    def test_373(self):
        input = Program([
            StructType("Votien", [("Votien", IntType())], []),
            StructType("TIEN", [("Votien", StringType()), ("TIEN", IntType()), ("TIEN", FloatType())], [])
        ])
        expect = "Redeclared Field: TIEN"
        self.assertTrue(TestChecker.test(input, expect, 373))

    def test_374(self):
        input = Program([
            MethodDecl("v", Id("TIEN"), FuncDecl("putIntLn", [], VoidType(), Block([Return(None)]))),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))),
            StructType("TIEN", [("Votien", IntType())], [])
        ])
        expect = "Redeclared Method: getInt"
        self.assertTrue(TestChecker.test(input, expect, 374))

    def test_375(self):
        input = Program([
            InterfaceType("VoTien", [
                Prototype("VoTien", [], VoidType()),
                Prototype("VoTien", [IntType()], VoidType())
            ])
        ])
        expect = "Redeclared Prototype: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 375))

    def test_376(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("a", IntType()), ParamDecl("a", IntType())], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 376))

    def test_377(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("b", IntType())], VoidType(), Block([
                VarDecl("b", None, IntLiteral(1)),
                VarDecl("a", None, IntLiteral(1)),
                ConstDecl("a", None, IntLiteral(1))
            ]))
        ])
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 377))

    def test_378(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("b", IntType())], VoidType(), Block([
                ForStep(
                    VarDecl("a", None, IntLiteral(1)),
                    BinaryOp("<", Id("a"), IntLiteral(1)),
                    Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))),
                    Block([ConstDecl("a", None, IntLiteral(2))])
                )
            ]))
        ])
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 378))

    def test_379(self):
        input = Program([
            VarDecl("a", None, IntLiteral(1)),
            VarDecl("b", None, Id("a")),
            VarDecl("c", None, Id("d"))
        ])
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 379))

    def test_380(self):
        input = Program([
            FuncDecl("Votien", [], IntType(), Block([Return(IntLiteral(1))])),
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("b", None, FuncCall("Votien", [])),
                FuncCall("foo_votine", []),
                Return(None)
            ]))
        ])
        expect = "Undeclared Function: foo_votine"
        self.assertTrue(TestChecker.test(input, expect, 380))

    def test_381(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                ConstDecl("c", None, FieldAccess(Id("v"), "Votien")),
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien"
        self.assertTrue(TestChecker.test(input, expect, 381))

    def test_382(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                MethCall(Id("v"), "getInt", []),
                MethCall(Id("v"), "putInt", [])
            ])))
        ])
        expect = "Undeclared Method: putInt"
        self.assertTrue(TestChecker.test(input, expect, 382))

    def test_383(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien"
        self.assertTrue(TestChecker.test(input, expect, 383))

    def test_384(self):
        input = Program([
            StructType("TIEN", [("a", IntType())], []),
            StructType("VO", [("a", IntType())], []),
            InterfaceType("TIEN", [Prototype("foo", [], VoidType())])
        ])
        expect = "Redeclared Type: TIEN"
        self.assertTrue(TestChecker.test(input, expect, 384))

    def test_385(self):
        input = Program([
            InterfaceType("TIEN", [
                Prototype("foo", [], VoidType()),
                Prototype("foo", [IntType(), IntType()], VoidType())
            ])
        ])
        expect = "Redeclared Prototype: foo"
        self.assertTrue(TestChecker.test(input, expect, 385))

    def test_386(self):
        input = Program([
            FuncDecl("putInt", [], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input, expect, 386))

    def test_387(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 387))

    def test_388(self):
        input = Program([
            InterfaceType("VoTien", [
                Prototype("VoTien", [], VoidType()),
                Prototype("VoTien", [IntType()], VoidType())
            ])
        ])
        expect = "Redeclared Prototype: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 388))

    def test_389(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("a", IntType()), ParamDecl("a", IntType())], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 389))

    def test_390(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("b", IntType())], VoidType(), Block([
                VarDecl("b", None, IntLiteral(1)),
                VarDecl("a", None, IntLiteral(1)),
                ConstDecl("a", None, IntLiteral(1))
            ]))
        ])
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 390))

    def test_391(self):
        input = Program([
            FuncDecl("Votien", [ParamDecl("b", IntType())], VoidType(), Block([
                ForStep(
                    VarDecl("a", None, IntLiteral(1)),
                    BinaryOp("<", Id("a"), IntLiteral(1)),
                    Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))),
                    Block([ConstDecl("a", None, IntLiteral(2))])
                )
            ]))
        ])
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 391))

    def test_392(self):
        input = Program([
            VarDecl("a", None, IntLiteral(1)),
            VarDecl("b", None, Id("a")),
            VarDecl("c", None, Id("d"))
        ])
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 392))

    def test_393(self):
        input = Program([
            FuncDecl("Votien", [], IntType(), Block([Return(IntLiteral(1))])),
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("b", None, FuncCall("Votien", [])),
                FuncCall("foo_votine", []),
                Return(None)
            ]))
        ])
        expect = "Undeclared Function: foo_votine"
        self.assertTrue(TestChecker.test(input, expect, 393))

    def test_394(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                ConstDecl("c", None, FieldAccess(Id("v"), "Votien")),
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien"
        self.assertTrue(TestChecker.test(input, expect, 394))

    def test_395(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                MethCall(Id("v"), "getInt", []),
                MethCall(Id("v"), "putInt", [])
            ])))
        ])
        expect = "Undeclared Method: putInt"
        self.assertTrue(TestChecker.test(input, expect, 395))

    def test_396(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        expect = "Undeclared Field: tien"
        self.assertTrue(TestChecker.test(input, expect, 396))

    def test_397(self):
        input = Program([
            StructType("TIEN", [("a", IntType())], []),
            StructType("VO", [("a", IntType())], []),
            InterfaceType("TIEN", [Prototype("foo", [], VoidType())])
        ])
        expect = "Redeclared Type: TIEN"
        self.assertTrue(TestChecker.test(input, expect, 397))

    def test_398(self):
        input = Program([
            InterfaceType("TIEN", [
                Prototype("foo", [], VoidType()),
                Prototype("foo", [IntType(), IntType()], VoidType())
            ])
        ])
        expect = "Redeclared Prototype: foo"
        self.assertTrue(TestChecker.test(input, expect, 398))

    def test_399(self):
        input = Program([
            FuncDecl("putInt", [], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input, expect, 399))

    def test_400(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_401(self):
        input = Program([
            FuncDecl("putInt", [], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_402(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_403(self):
        input = Program([
            FuncDecl("putInt", [], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_405(self):
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [
                ParamDecl("a", IntType()),
                ParamDecl("a", IntType())
            ], VoidType(), Block([Return(None)]))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406(self):
        """
            type S1 struct {votien int;}
            type I1 interface {votien();}

            func (s S1) votien() {return;}

            var b [2] S1;
            var a [2] I1 = b;
            """
        input = Program(
            [
                StructType("S1", [("votien", IntType())], []),
                InterfaceType("I1", [Prototype("votien", [], VoidType())]),
                MethodDecl(
                    "s",
                    Id("S1"),
                    FuncDecl("votien", [], VoidType(), Block([Return(None)])),
                ),
                VarDecl("b", ArrayType([IntLiteral(2)], Id("S1")), None),
                VarDecl("a", ArrayType([IntLiteral(2)], Id("I1")), Id("b")),
            ]
        )
        self.assertTrue(
            TestChecker.test(
                input,
                "Type Mismatch: VarDecl(a,ArrayType(Id(I1),[IntLiteral(2)]),Id(b))",
                inspect.stack()[0].function,
            )
        )

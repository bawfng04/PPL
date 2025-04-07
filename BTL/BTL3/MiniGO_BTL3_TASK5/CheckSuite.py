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
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(e,ArrayType(StringType,[IntLiteral(2)]),Id(a))", inspect.stack()[0].function))

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
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(e,ArrayType(StringType,[IntLiteral(2)]),Id(a))", inspect.stack()[0].function))

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
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: b", inspect.stack()[0].function))

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
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(e,StringType,Id(a))", inspect.stack()[0].function))

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
        input = """
        func foo() int {
            const foo = 1;
            return foo()
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo""", inspect.stack()[0].function))






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
func Votien (b int) {
    for var a = 1; a < 1; a += 1 {
        const a = 2;
    }
}
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a", inspect.stack()[0].function))


import unittest
from TestUtils import TestChecker
from AST import * # Import all AST node types
import inspect

class CheckSuite(unittest.TestCase):

    def test_001(self):
        input = Program([VarDecl("VoTien", None,IntLiteral(1)),VarDecl("VoTien", None,IntLiteral(2))])
        expect = "Redeclared Variable: VoTien" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_002(self):
        input = Program([VarDecl("VoTien", None,IntLiteral(1)),ConstDecl("VoTien",None,IntLiteral(2))])
        expect = "Redeclared Constant: VoTien" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_003(self):
        input = Program([ConstDecl("VoTien",None,IntLiteral(1)),VarDecl("VoTien", None,IntLiteral(2))])
        expect = "Redeclared Variable: VoTien" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_004(self):
        input = Program([ConstDecl("VoTien",None,IntLiteral(1)),FuncDecl("VoTien",[],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Function: VoTien" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_005(self):
        input = Program([FuncDecl("VoTien",[],VoidType(),Block([Return(None)])),VarDecl("VoTien", None,IntLiteral(1))])
        expect = "Redeclared Variable: VoTien" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_006(self):
        input = Program([VarDecl("getInt", None,IntLiteral(1))])
        expect = "Redeclared Variable: getInt" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_007(self):
        input = Program([StructType("Votien",[("Votien",IntType())],[]),StructType("TIEN",[("Votien",StringType()),("TIEN",IntType()),("TIEN",FloatType())],[])])
        expect = "Redeclared Field: TIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_008(self):
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([Return(None)])))])])
        expect = "Redeclared Method: getInt" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_009(self):
        input = Program([InterfaceType("VoTien",[Prototype("VoTien",[],VoidType()),Prototype("VoTien",[IntType()],VoidType())])])
        expect = "Redeclared Prototype: VoTien" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_010(self):
        input = Program([FuncDecl("Votien",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Parameter: a" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_011(self):
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        expect = "Redeclared Constant: a" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_012(self):
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
        expect = "Redeclared Constant: a" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_013(self):
        input = Program([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,Id("a")),VarDecl("c", None,Id("d"))])
        expect = "Undeclared Identifier: d" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_014(self):
        input = Program([FuncDecl("Votien",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,FuncCall("Votien",[])),FuncCall("foo_votien",[]),Return(None)]))])
        expect = "Undeclared Function: foo_votien" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_015(self):
        input = Program([StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([ConstDecl("c",None,FieldAccess(Id("v"),"Votien")),VarDecl("d", None,FieldAccess(Id("v"),"tien"))])))]),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([ConstDecl("c",None,FieldAccess(Id("v"),"Votien")),VarDecl("d", None,FieldAccess(Id("v"),"tien"))])))])
        expect = "Undeclared Field: tien" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_016(self):
        input = Program([StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([MethCall(Id("v"),"getInt",[]),MethCall(Id("v"),"putInt",[])])))]),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([MethCall(Id("v"),"getInt",[]),MethCall(Id("v"),"putInt",[])])))])
        expect = "Undeclared Method: putInt" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_017(self):
        input = Program([StructType("TIEN",[("Votien",IntType())],[]),StructType("TIEN",[("v",IntType())],[])])
        expect = "Redeclared Type: TIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_018(self):
        input = Program([StructType("TIEN",[("a",IntType()),("b",IntType()),("a",FloatType())],[])])
        expect = "Redeclared Field: a" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_019(self):
        input = Program([StructType("TIEN",[("a",IntType()),("b",IntType()),("c",FloatType()),("b",IntType())],[])])
        expect = "Redeclared Field: b" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_020(self):
        input = Program([StructType("TIEN",[("c",FloatType()),("b",IntType()),("a",IntType())],[]),StructType("VO",[("d",IntType()),("d",IntType())],[])])
        expect = "Redeclared Field: d" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_021(self):
        input = Program([StructType("TIEN",[("a",IntType())],[]),StructType("VO",[("a",IntType())],[]),StructType("TIEN",[("a",IntType())],[])])
        expect = "Redeclared Type: TIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_022(self):
        input = Program([InterfaceType("TIEN",[Prototype("foo",[],VoidType())]),InterfaceType("TIEN",[Prototype("foo",[],VoidType())])])
        expect = "Redeclared Type: TIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_023(self):
        input = Program([InterfaceType("TIEN",[Prototype("foo",[],VoidType())]),InterfaceType("VO",[Prototype("foo",[],VoidType())]),InterfaceType("TIEN",[Prototype("foo",[],VoidType())])])
        expect = "Redeclared Type: TIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_024(self):
        input = Program([StructType("TIEN",[("a",IntType())],[]),StructType("VO",[("a",IntType())],[]),InterfaceType("TIEN",[Prototype("foo",[],VoidType())])])
        expect = "Redeclared Type: TIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_025(self):
        input = Program([InterfaceType("TIEN",[Prototype("foo",[],VoidType()),Prototype("foo",[IntType(),IntType()],VoidType())])])
        expect = "Redeclared Prototype: foo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_026(self):
        input = Program([InterfaceType("TIEN",[Prototype("foo",[],VoidType()),Prototype("foo1",[],VoidType()),Prototype("foo",[IntType(),IntType()],VoidType())])])
        expect = "Redeclared Prototype: foo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_027(self):
        input = Program([InterfaceType("TIEN",[Prototype("foo1",[],VoidType()),Prototype("foo",[],VoidType())]),InterfaceType("VO",[Prototype("foo",[],VoidType()),Prototype("foo",[IntType(),IntType()],VoidType())])])
        expect = "Redeclared Prototype: foo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_028(self):
        input = Program([InterfaceType("TIEN",[Prototype("foo",[],VoidType())]),FuncDecl("TIEN",[],VoidType(),Block([Return(None)])),FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("TIEN",[],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Function: TIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_029(self):
        input = Program([FuncDecl("getInt",[],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Function: getInt" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_030(self):
        input = Program([FuncDecl("putInt",[],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Function: putInt" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_031(self):
        input = Program([FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Function: putIntLn" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_032(self):
        input = Program([FuncDecl("getString",[],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Function: getString" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_033(self):
        input = Program([FuncDecl("putStringLn",[],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Function: putStringLn" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_034(self):
        input = Program([VarDecl("foo", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Function: foo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_035(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),VarDecl("foo", None,IntLiteral(1))])
        expect = "Redeclared Variable: foo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_036(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),ConstDecl("foo",None,IntLiteral(1))])
        expect = "Redeclared Constant: foo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_037(self):
        input = Program([ConstDecl("foo",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Function: foo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_038(self):
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_039(self):
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1))])),VarDecl("a", None,IntLiteral(1))])
        expect = "Redeclared Variable: a" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_040(self):
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1))])),ConstDecl("b",None,IntLiteral(1))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_041(self):
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1))])),ConstDecl("a",None,IntLiteral(1))])
        expect = "Redeclared Constant: a" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_042(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ConstDecl("b",None,IntLiteral(1))]))])
        expect = "Redeclared Constant: b" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_043(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),VarDecl("b", None,IntLiteral(1))]))])
        expect = "Redeclared Variable: b" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_044(self):
        input = Program([StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],VoidType(),Block([Return(None)])))]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_045(self):
        input = Program([StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)])))]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Parameter: a" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_046(self):
        input = Program([StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)])))]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Parameter: a" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_047(self):
        input = Program([StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)])))]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType()),ParamDecl("a",FloatType())],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Parameter: a" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_048(self):
        input = Program([StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))]),VarDecl("a", None,IntLiteral(1)),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_049(self):
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))]),StructType("VO",[("Votien",IntType())],[MethodDecl("v",Id("VO"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))]),MethodDecl("v",Id("VO"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_050(self):
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([ConstDecl("v",None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))),StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([ConstDecl("v",None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))])))]),MethodDecl("v",Id("VO"),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1))]))),StructType("VO",[("Votien",IntType())],[MethodDecl("v",Id("VO"),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1))])))]),MethodDecl("v",Id("VO"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([ConstDecl("a",None,IntLiteral(1))])))])
        expect = "Redeclared Method: foo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_051(self):
        input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("b"),IntLiteral(2)),Block([ConstDecl("b",None,IntLiteral(1))]))]))])
        expect = "Redeclared Constant: b" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_052(self):
        input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),Block([ConstDecl("a",None,IntLiteral(1)),ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),Block([ConstDecl("a",None,IntLiteral(1)),ConstDecl("b",None,IntLiteral(1))])),ConstDecl("b",None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))]))])
        expect = "Redeclared Variable: a" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_053(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("b", None,IntLiteral(1))]))]))])
        expect = "Redeclared Variable: b" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_054(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("a", None,IntLiteral(1))]))]))])
        expect = "Redeclared Variable: a" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_055(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("c", None,IntLiteral(1))])),VarDecl("a", None,IntLiteral(1))]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_056(self):
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("d", None,Id("b"))])),VarDecl("d", None,Id("b")),VarDecl("a", None,IntLiteral(1))])),VarDecl("d", None,Id("a"))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_057(self):
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("c"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("d", None,Id("e"))])),VarDecl("d", None,Id("b")),VarDecl("a", None,IntLiteral(1))])),VarDecl("d", None,Id("a"))])
        expect = "Undeclared Identifier: e" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_058(self):
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("c"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("d", None,Id("c"))])),VarDecl("d", None,Id("c")),VarDecl("a", None,IntLiteral(1))])),VarDecl("d", None,Id("a"))])
        expect = "Undeclared Identifier: c" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_059(self):
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("c"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("d", None,Id("c"))])),VarDecl("d", None,Id("a")),VarDecl("a", None,IntLiteral(1))])),VarDecl("d", None,Id("b"))])
        expect = "Undeclared Identifier: b" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_060(self):
        input = Program([VarDecl("a", None,Id("d")),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("c"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("d", None,Id("c"))])),VarDecl("d", None,Id("a")),VarDecl("a", None,IntLiteral(1))])),VarDecl("d", None,Id("a"))])
        expect = "Undeclared Identifier: d" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_061(self):
        input = Program([VarDecl("a", None,FuncCall("foo",[])),FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,FuncCall("koo",[])),VarDecl("c", None,FuncCall("getInt",[])),FuncCall("putInt",[Id("c")]),FuncCall("putIntLn",[Id("c")]),Return(IntLiteral(1))])),VarDecl("d", None,FuncCall("foo",[])),FuncDecl("koo",[],IntType(),Block([VarDecl("a", None,FuncCall("foo",[])),Return(IntLiteral(1))]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_062(self):
        input = Program([VarDecl("a", None,FuncCall("foo",[])),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])),VarDecl("d", None,FuncCall("koo",[]))])
        expect = "Undeclared Function: koo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_063(self):
        input = Program([VarDecl("a", None,FuncCall("foo",[])),FuncDecl("foo",[],IntType(),Block([VarDecl("d", None,FuncCall("koo",[])),Return(IntLiteral(1))]))])
        expect = "Undeclared Function: koo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_064(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,FuncCall("foo",[])),VarDecl("d",IntType(),Id("a")),Return(IntLiteral(1))]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_065(self):
        input = Program([VarDecl("v",Id("TIEN"), None),ConstDecl("b",None,FieldAccess(Id("v"),"b")),StructType("TIEN",[("c",IntType()),("b",IntType()),("a",IntType())],[]),ConstDecl("a",None,FieldAccess(Id("v"),"a")),ConstDecl("e",None,FieldAccess(Id("v"),"e"))])
        expect = "Undeclared Field: e" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_066(self):
        input = Program([VarDecl("v",Id("TIEN"), None),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,FieldAccess(Id("v"),"a")),ConstDecl("e",None,FieldAccess(Id("v"),"e"))])),StructType("TIEN",[("c",IntType()),("b",IntType()),("a",IntType())],[])])
        expect = "Undeclared Field: e" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_067(self):
        input = Program([VarDecl("v",Id("TIEN"), None),FuncDecl("foo",[],VoidType(),Block([VarDecl("x", None,Id("v")),ConstDecl("a",None,FieldAccess(Id("x"),"a")),ConstDecl("e",None,FieldAccess(Id("x"),"e"))])),StructType("TIEN",[("c",IntType()),("b",IntType()),("a",IntType())],[])])
        expect = "Undeclared Field: e" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_068(self):
        input = Program([VarDecl("v",Id("TIEN"), None),ConstDecl("b",None,MethCall(Id("v"),"foo",[])),StructType("TIEN",[("a",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("v",Id("TIEN"),FuncDecl("koo",[],IntType(),Block([Return(IntLiteral(1))])))]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("v",Id("TIEN"),FuncDecl("koo",[],IntType(),Block([Return(IntLiteral(1))]))),ConstDecl("c",None,MethCall(Id("v"),"koo",[])),ConstDecl("d",None,MethCall(Id("v"),"zoo",[]))])
        expect = "Undeclared Method: zoo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_069(self):
        input = Program([VarDecl("v",Id("TIEN"), None),StructType("TIEN",[("a",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("TIEN"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])])))]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("TIEN"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,MethCall(Id("v"),"foo",[])),MethCall(Id("v"),"koo",[]),ConstDecl("d",None,MethCall(Id("v"),"zoo",[]))]))])
        expect = "Undeclared Method: zoo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_070(self):
        input = Program([VarDecl("v",Id("TIEN"), None),StructType("TIEN",[("a",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("TIEN"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])])))]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("TIEN"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x", None,Id("v")),ConstDecl("b",None,MethCall(Id("x"),"foo",[])),MethCall(Id("x"),"koo",[]),ConstDecl("d",None,MethCall(Id("x"),"zoo",[]))]))])
        expect = "Undeclared Method: zoo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_071(self):
        input = Program([VarDecl("v",Id("TIEN"), None),StructType("TIEN",[("a",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("TIEN"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])])))]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("TIEN"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",Id("VO"), None),ConstDecl("b",None,MethCall(Id("x"),"foo",[])),MethCall(Id("x"),"koo",[])]))])
        expect = "Undeclared Method: koo" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_072(self):
        input = Program([VarDecl("v",IntType(),FloatLiteral(1.02))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_073(self):
        input = Program([VarDecl("v",FloatType(),IntLiteral(1))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_074(self):
        input = Program([VarDecl("v",StringType(),BooleanLiteral(true))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_075(self):
        input = Program([VarDecl("v",StringType(),StringLiteral(""1"")),ConstDecl("x",None,Id("v")),VarDecl("k",StringType(),Id("x")),VarDecl("y",BoolType(),Id("x"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_076(self):
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),VarDecl("v",Id("S1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("S1"),Id("x")),VarDecl("k",Id("S2"),Id("x"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_077(self):
        input = Program([InterfaceType("I1",[Prototype("votien",[],VoidType())]),InterfaceType("I2",[Prototype("votien",[],VoidType())]),VarDecl("v",Id("I1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("I1"),Id("x")),VarDecl("k",Id("I2"),Id("x"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_078(self):
        input = Program([StructType("S1",[("votien",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien1",[],VoidType(),Block([Return(None)])))]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien1",[],VoidType())]),InterfaceType("I2",[Prototype("votien1",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien1",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("b"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_079(self):
        input = Program([StructType("S1",[("votien",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien1",[],VoidType(),Block([Return(None)])))]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien1",[],VoidType())]),InterfaceType("I2",[Prototype("votien1",[],IntType())]),MethodDecl("s",Id("S1"),FuncDecl("votien1",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I2"),Id("a"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_080(self):
        input = Program([StructType("S1",[("votien",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien1",[],Id("S1"),Block([Return(Id("s"))])))]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien1",[],Id("S1"))]),InterfaceType("I2",[Prototype("votien1",[],Id("S2"))]),MethodDecl("s",Id("S1"),FuncDecl("votien1",[],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_081(self):
        input = Program([StructType("S1",[("votien",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien1",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))])))]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien1",[IntType(),IntType()],Id("S1"))]),InterfaceType("I2",[Prototype("votien1",[IntType()],Id("S1"))]),MethodDecl("s",Id("S1"),FuncDecl("votien1",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_082(self):
        input = Program([StructType("S1",[("votien",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien1",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))])))]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien1",[IntType(),IntType()],Id("S1"))]),InterfaceType("I2",[Prototype("votien1",[IntType(),FloatType()],Id("S1"))]),MethodDecl("s",Id("S1"),FuncDecl("votien1",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_083(self):
        input = Program([StructType("S1",[("votien",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien1",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))])))]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien1",[IntType(),IntType()],Id("S1"))]),InterfaceType("I2",[Prototype("votien1",[IntType(),FloatType()],Id("S1"))]),MethodDecl("s",Id("S1"),FuncDecl("votien1",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_084(self):
        input = Program([StructType("S1",[("votien",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien1",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))])))]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien1",[IntType(),IntType()],Id("S1"))]),InterfaceType("I2",[Prototype("votien1",[IntType(),FloatType()],Id("S1"))]),MethodDecl("s",Id("S1"),FuncDecl("votien1",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_085(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("v",IntType(), None),ConstDecl("x",None,Id("v")),VarDecl("k",FloatType(),Id("x")),VarDecl("y",BoolType(),Id("x"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_086(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([If(BooleanLiteral(true), Block([VarDecl("a",FloatType(),FloatLiteral(1.02))]), Block([VarDecl("a",IntType(),FloatLiteral(1.02))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_087(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([If(IntLiteral(1), Block([VarDecl("a",FloatType(),FloatLiteral(1.02))]), None)]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_088(self):
        input = Program([StructType("TIEN",[("v",IntType())],[]),VarDecl("v",Id("TIEN"), None),FuncDecl("foo",[],VoidType(),Block([If(Id("v"), Block([VarDecl("a",FloatType(),FloatLiteral(1.02))]), None)]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_089(self):
        input = Program([StructType("TIEN",[("v",IntType())],[]),VarDecl("v",Id("TIEN"), None),FuncDecl("foo",[],VoidType(),Block([ForBasic(BooleanLiteral(true),Block([VarDecl("a",IntType(),FloatLiteral(1.02))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_090(self):
        input = Program([StructType("TIEN",[("v",IntType())],[]),VarDecl("v",Id("TIEN"), None),FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([VarDecl("a",IntType(),FloatLiteral(1.02))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_091(self):
        input = Program([StructType("TIEN",[("v",IntType())],[]),VarDecl("v",Id("TIEN"), None),FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([VarDecl("a",IntType(),FloatLiteral(1.02))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_092(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("foo1",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo2",[],FloatType(),Block([Return(IntLiteral(2))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_093(self):
        input = Program([StructType("S1",[("votien1",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([Return(None)])))]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],Id("S1"),Block([VarDecl("a",Id("S1"), None),Return(Id("a"))])),FuncDecl("foo1",[],Id("I1"),Block([VarDecl("a",Id("I1"), None),Return(Id("a"))])),FuncDecl("foo2",[],Id("S1"),Block([VarDecl("b",Id("I1"), None),Return(Id("b"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_094(self):
        input = Program([StructType("S1",[("t",IntType()),("v",IntType())],[]),VarDecl("a", None,StructLiteral("S1",[("v",IntLiteral(1)),("t",IntLiteral(2))])),VarDecl("b",Id("S1"),Id("a")),VarDecl("c",IntType(),Id("b"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_095(self):
        input = Program([StructType("S1",[("v",IntType())],[]),VarDecl("a", None,StructLiteral("S1",[("v",Id("z"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_096(self):
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(2)],FloatType()),Id("a"))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_097(self):
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],FloatType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("a"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_098(self):
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3),IntLiteral(2)],IntType()),Id("a"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_099(self):
        input = Program([StructType("S1",[("v",IntType())],[]),VarDecl("a", None,ArrayLiteral([IntLiteral(1)],Id("S1"),[StructLiteral("S1",[("v",Id("z"))])]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_100(self):
        input = Program([StructType("S1",[("v",IntType())],[]),VarDecl("a", None,ArrayLiteral([IntLiteral(1)],Id("S1"),[StructLiteral("S1",[("v",Id("z"))])]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_101(self):
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",IntType(),Id("b")),VarDecl("d",ArrayType([IntLiteral(1)],StringType()),Id("b"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_102(self):
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("b")),VarDecl("d",ArrayType([IntLiteral(3)],StringType()),Id("b"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_103(self):
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[FloatLiteral(1.0)]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_104(self):
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[FloatLiteral(1.0)]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_105(self):
        input = Program([StructType("S1",[("x",Id("S1")),("v",IntType())],[]),VarDecl("b",Id("S1"), None),VarDecl("c", None,FieldAccess(FieldAccess(Id("b"),"x"),"v")),VarDecl("d", None,FieldAccess(Id("c"),"x"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_106(self):
        input = Program([StructType("S1",[("votien1",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([Return(None)])))]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([Return(None)]))),VarDecl("c",Id("I1"), None),VarDecl("d", None,FieldAccess(Id("c"),"votien"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_107(self):
        input = Program([StructType("S1",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),VarDecl("a",Id("I1"), None),VarDecl("c",Id("I1"),NilLiteral()),VarDecl("d",Id("S1"),NilLiteral()),FuncDecl("foo",[],VoidType(),Block([Assign(Id("c"),Id("a")),Assign(Id("a"),NilLiteral())])),VarDecl("e",IntType(),NilLiteral())])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_108(self):
        input = Program([VarDecl("a", None,UnaryOp("-",IntLiteral(1))),VarDecl("b", None,UnaryOp("-",FloatLiteral(1.02))),VarDecl("c", None,UnaryOp("-",BooleanLiteral(true)))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_109(self):
        input = Program([VarDecl("a", None,UnaryOp("!",BooleanLiteral(true))),VarDecl("b", None,UnaryOp("!",IntLiteral(1)))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_110(self):
        input = Program([VarDecl("a", None,BinaryOp("+", StringLiteral(""1""), StringLiteral(""2""))),VarDecl("c",StringType(),Id("a")),VarDecl("b", None,BinaryOp("+", StringLiteral(""1""), IntLiteral(1)))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_111(self):
        input = Program([VarDecl("a", None,BinaryOp("+", IntLiteral(1), FloatLiteral(2.0))),VarDecl("b", None,BinaryOp("+", IntLiteral(1), IntLiteral(1))),FuncDecl("foo",[],IntType(),Block([Return(Id("b")),Return(Id("a"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_112(self):
        input = Program([VarDecl("a", None,BinaryOp("+", IntLiteral(1), BooleanLiteral(true)))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_113(self):
        input = Program([VarDecl("a",FloatType(),BinaryOp("*", IntLiteral(1), FloatLiteral(2.0))),VarDecl("b",IntType(),BinaryOp("/", IntLiteral(1), IntLiteral(2))),VarDecl("c",FloatType(),BinaryOp("/", IntLiteral(1), IntLiteral(2))),FuncDecl("foo",[],IntType(),Block([Return(Id("b")),Return(Id("c"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_114(self):
        input = Program([VarDecl("a", None,BinaryOp("*", IntLiteral(1), StringLiteral(""a"")))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_115(self):
        input = Program([VarDecl("a",IntType(),BinaryOp("%", IntLiteral(1), IntLiteral(2))),VarDecl("b",IntType(),BinaryOp("%", IntLiteral(1), FloatLiteral(2.0)))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_116(self):
        input = Program([VarDecl("a",BoolType(),BinaryOp("||", BinaryOp("&&", BooleanLiteral(true), BooleanLiteral(false)), BooleanLiteral(true))),VarDecl("b",BoolType(),BinaryOp("&&", BooleanLiteral(true), IntLiteral(1)))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_117(self):
        input = Program([VarDecl("a",BoolType(),BinaryOp(">", IntLiteral(1), IntLiteral(2))),VarDecl("b",BoolType(),BinaryOp("<", FloatLiteral(1.0), FloatLiteral(2.0))),VarDecl("c",BoolType(),BinaryOp("==", StringLiteral(""1""), StringLiteral(""2""))),VarDecl("d",BoolType(),BinaryOp(">", IntLiteral(1), FloatLiteral(2.0)))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_118(self):
        input = Program([VarDecl("a",BoolType(),BinaryOp(">=", IntLiteral(1), IntLiteral(2))),VarDecl("b",BoolType(),BinaryOp("<=", FloatLiteral(1.0), FloatLiteral(2.0))),VarDecl("c",BoolType(),BinaryOp("!=", StringLiteral(""1""), StringLiteral(""2""))),VarDecl("d",BoolType(),BinaryOp(">", IntLiteral(1), BooleanLiteral(true)))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_119(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("z"),BinaryOp("+", Id("z"), IntLiteral(1))),Block([Return(None)]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_120(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),FloatLiteral(1.0)),Block([Return(None)]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_121(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("i"),FloatLiteral(1.0)),Block([VarDecl("a", None,IntLiteral(1))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_122(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),Id("i"),Assign(Id("i"),FloatLiteral(1.0)),Block([VarDecl("a", None,IntLiteral(1))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_123(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),Id("i"),Assign(Id("i"),FloatLiteral(1.0)),Block([VarDecl("a", None,IntLiteral(1))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_124(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2)],IntType()), None),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",IntType(),Id("b")),VarDecl("e",StringType(),Id("a"))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_125(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2)],IntType()), None),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",IntType(),Id("b")),VarDecl("e",StringType(),Id("a"))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_126(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",ArrayType([IntLiteral(3)],IntType()),Id("b")),VarDecl("e",ArrayType([IntLiteral(2)],StringType()),Id("a"))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_127(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",ArrayType([IntLiteral(3)],FloatType()),Id("b")),VarDecl("e",ArrayType([IntLiteral(2)],StringType()),Id("a"))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_128(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])),VarDecl("a",FloatType(),FuncCall("foo",[BinaryOp("+", IntLiteral(1), IntLiteral(1))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_129(self):
        input = Program([FuncDecl("foo",[ParamDecl("a",IntType())],IntType(),Block([Return(IntLiteral(1))])),VarDecl("a",IntType(),FuncCall("foo",[BinaryOp("+", IntLiteral(1), IntLiteral(1))])),VarDecl("b", None,FuncCall("foo",[FloatLiteral(1.0)]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_130(self):
        input = Program([StructType("S1",[("votien1",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("I1",[Prototype("votien",[],IntType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],IntType(),Block([Return(IntLiteral(1))]))),VarDecl("i",Id("I1"), None),VarDecl("s",Id("S1"), None),VarDecl("a",IntType(),MethCall(Id("i"),"votien",[])),VarDecl("b",IntType(),MethCall(Id("s"),"votien",[])),VarDecl("c",IntType(),MethCall(Id("a"),"votien",[]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_131(self):
        input = Program([StructType("S1",[("votien1",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("I1",[Prototype("votien",[],IntType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],IntType(),Block([Return(IntLiteral(1))]))),VarDecl("s",Id("S1"), None),VarDecl("a",IntType(),MethCall(Id("s"),"votien",[IntLiteral(1)]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_132(self):
        input = Program([StructType("S1",[("votien1",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien",[ParamDecl("a",IntType())],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("I1",[Prototype("votien",[IntType()],IntType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[ParamDecl("a",IntType())],IntType(),Block([Return(IntLiteral(1))]))),VarDecl("s",Id("S1"), None),VarDecl("a",IntType(),MethCall(Id("s"),"votien",[IntLiteral(1)])),VarDecl("b",IntType(),MethCall(Id("s"),"votien",[FloatLiteral(1.0)]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_133(self):
        input = Program([StructType("S1",[("votien1",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("I1",[Prototype("votien",[],IntType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],IntType(),Block([Return(IntLiteral(1))]))),VarDecl("i",Id("I1"), None),VarDecl("a",IntType(),MethCall(Id("i"),"votien",[IntLiteral(1)]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_134(self):
        input = Program([StructType("S1",[("votien1",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien",[],IntType(),Block([MethCall(Id("s"),"votien",[]),Return(IntLiteral(1))])))]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],IntType(),Block([MethCall(Id("s"),"votien",[]),Return(IntLiteral(1))])))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_135(self):
        input = Program([StructType("S1",[("votien1",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("vo",[],VoidType(),Block([Return(None)]))),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([MethCall(Id("s"),"votien",[]),VarDecl("a", None,MethCall(Id("s"),"vo",[]))])))]),MethodDecl("s",Id("S1"),FuncDecl("vo",[],VoidType(),Block([Return(None)]))),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([MethCall(Id("s"),"votien",[]),VarDecl("a", None,MethCall(Id("s"),"vo",[]))])))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_136(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("votien",[],IntType(),Block([Return(FuncCall("votien",[])),FuncCall("foo",[])]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_137(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("votien",[],IntType(),Block([FuncCall("foo",[]),Return(FuncCall("foo",[]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_138(self):
        input = Program([FuncDecl("votien",[],VoidType(),Block([Break(),Continue()]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_139(self):
        input = Program([StructType("Person",[("age",IntType()),("name",StringType())],[MethodDecl("p",Id("Person"),FuncDecl("Greet",[],StringType(),Block([Return(BinaryOp("+", StringLiteral(""Hello, ""), FieldAccess(Id("p"),"name")))])))]),FuncDecl("votien",[],VoidType(),Block([VarDecl("person", None,StructLiteral("Person",[("name",StringLiteral(""Alice"")),("age",IntLiteral(30))])),Assign(FieldAccess(Id("person"),"name"),StringLiteral(""John"")),Assign(FieldAccess(Id("person"),"age"),IntLiteral(30)),FuncCall("putStringLn",[FieldAccess(Id("person"),"name")]),FuncCall("putStringLn",[MethCall(Id("person"),"Greet",[])])])),MethodDecl("p",Id("Person"),FuncDecl("Greet",[],StringType(),Block([Return(BinaryOp("+", StringLiteral(""Hello, ""), FieldAccess(Id("p"),"name")))])))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_140(self):
        input = Program([VarDecl("a",StringType(), None),FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(2)),FuncCall("putIntLn",[Id("a")])]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_141(self):
        input = Program([VarDecl("a",StringType(), None),FuncDecl("foo",[],VoidType(),Block([FuncCall("putIntLn",[Id("a")]),VarDecl("a",IntType(),IntLiteral(2))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_142(self):
        input = Program([VarDecl("a",Id("TIEN"), None),FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(Id("a"),"tien"),BinaryOp("+", FieldAccess(Id("a"),"tien"), IntLiteral(2))),FuncCall("putIntLn",[FieldAccess(Id("a"),"tien")]),FuncCall("foo",[])])),VarDecl("b", None,FuncCall("foo",[])),StructType("TIEN",[("tien",IntType())],[])])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_143(self):
        input = Program([VarDecl("a",Id("TIEN"), None),FuncDecl("foo",[],Id("TIEN"),Block([Return(Id("a")),Return(Id("TIEN"))])),StructType("TIEN",[("tien",IntType())],[])])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_144(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(ArrayCell(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),[Id("a")]))])),VarDecl("a", None,FuncCall("foo",[]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_145(self):
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],FloatType(),Block([Return(ArrayCell(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),[Id("a")]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_146(self):
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Return(Id("a"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_147(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_148(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("koo",[],IntType(),Block([Return(FuncCall("foo",[]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_149(self):
        input = Program([FuncDecl("putLn",[],VoidType(),Block([Return(None)]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_150(self):
        input = Program([VarDecl("putLn",IntType(), None)])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_151(self):
        input = Program([StructType("putLn",[("a",IntType())],[])])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_152(self):
        input = Program([InterfaceType("putLn",[Prototype("foo",[],VoidType())])])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_153(self):
        input = Program([VarDecl("a",IntType(),FuncCall("getBool",[]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_154(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("putFloat",[FuncCall("getInt",[])])]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_155(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("putLn",[FuncCall("getInt",[])])]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_156(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("putIntLn",[])]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_157(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("putFloat",[FloatLiteral(1.0)]),FuncCall("putIntLn",[IntLiteral(1),IntLiteral(2)])]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_158(self):
        input = Program([FuncDecl("foo",[],ArrayType([IntLiteral(2)],FloatType()),Block([Return(ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])),Return(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_159(self):
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[],Id("TIEN"),Block([Return(StructLiteral("TIEN",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])),FuncDecl("coco",[],Id("TIEN"),Block([VarDecl("a",Id("VO"),FuncCall("foo",[])),Return(Id("a"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_160(self):
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("b",Id("VO"),StructLiteral("TIEN",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),VarDecl("a",Id("TIEN"),Id("b"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_161(self):
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,StructLiteral("TIEN",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),VarDecl("a",IntType(),ArrayCell(FieldAccess(Id("b"),"a"),[IntLiteral(1)]))]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_162(self):
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("VO"))],VoidType(),Block([VarDecl("b",Id("VO"),StructLiteral("TIEN",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),FuncCall("foo",[Id("b")])]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_163(self):
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("VO"))],VoidType(),Block([VarDecl("b", None,StructLiteral("TIEN",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),FuncCall("foo",[Id("b")])]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_164(self):
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])))]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("VO"))],VoidType(),Block([VarDecl("b", None,NilLiteral()),FuncCall("foo",[NilLiteral()])]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_165(self):
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),FuncDecl("foo",[],Id("TIEN"),Block([Return(NilLiteral())]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_166(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([If(BooleanLiteral(true), Block([VarDecl("a", None,IntLiteral(1))]), Block([VarDecl("a", None,IntLiteral(2))])),Return(Id("a"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_167(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1)),If(BinaryOp("<", Id("a"), IntLiteral(3)), Block([VarDecl("a", None,IntLiteral(1))]), If(BinaryOp(">", Id("a"), IntLiteral(2)), Block([VarDecl("a", None,IntLiteral(2))]), None)),Return(Id("a"))]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_168(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(),BinaryOp("*", FloatLiteral(2.0), IntLiteral(1)))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_169(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",ArrayType([IntLiteral(5),IntLiteral(6)],IntType()), None),VarDecl("b",ArrayType([IntLiteral(2)],FloatType()), None),Assign(ArrayCell(Id("b"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)])),Assign(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)]),BinaryOp("+", ArrayCell(Id("b"),[IntLiteral(2)]), IntLiteral(1)))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_170(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([VarDecl("arr",ArrayType([IntLiteral(3)],IntType()), None),VarDecl("marr",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),Assign(Id("arr"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(10),IntLiteral(20),IntLiteral(30)])),Assign(Id("marr"),ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType(),[[IntLiteral(1),IntLiteral(2),IntLiteral(3)],[IntLiteral(4),IntLiteral(5),IntLiteral(6)]])),Return(BinaryOp("+", ArrayCell(Id("arr"),[IntLiteral(2)]), ArrayCell(Id("marr"),[IntLiteral(1),IntLiteral(2)])))]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_171(self):
        input = Program([StructType("Person",[("age",IntType()),("name",StringType())],[MethodDecl("p",Id("Person"),FuncDecl("getAge",[],IntType(),Block([Assign(Id("p"),StructLiteral("Person",[("name",StringLiteral(""Alice"")),("age",IntLiteral(30))])),VarDecl("q", None,StructLiteral("Person",[])),Return(FieldAccess(Id("p"),"age"))])))]),MethodDecl("p",Id("Person"),FuncDecl("getAge",[],IntType(),Block([Assign(Id("p"),StructLiteral("Person",[("name",StringLiteral(""Alice"")),("age",IntLiteral(30))])),VarDecl("q", None,StructLiteral("Person",[])),Return(FieldAccess(Id("p"),"age"))])))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_172(self):
        input = Program([StructType("Person",[("age",IntType()),("name",StringType())],[MethodDecl("p",Id("Person"),FuncDecl("getAge",[],IntType(),Block([Assign(Id("p"),StructLiteral("Person",[("name",StringLiteral(""Alice"")),("age",IntLiteral(30))])),Return(FieldAccess(Id("p"),"age"))])))]),MethodDecl("p",Id("Person"),FuncDecl("getAge",[],IntType(),Block([Assign(Id("p"),StructLiteral("Person",[("name",StringLiteral(""Alice"")),("age",IntLiteral(30))])),Return(FieldAccess(Id("p"),"age"))])))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_173(self):
        input = Program([VarDecl("a",ArrayType([IntLiteral(2)],IntType()),ArrayLiteral([IntLiteral(2),IntLiteral(2)],IntType(),[[IntLiteral(1),IntLiteral(2)],[IntLiteral(2),IntLiteral(2)]]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_174(self):
        input = Program([VarDecl("A", None,IntLiteral(1)),StructType("A",[("a",IntType())],[])])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_175(self):
        input = Program([ConstDecl("A",None,IntLiteral(2)),InterfaceType("A",[Prototype("foo",[],VoidType())])])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_176(self):
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]),ConstDecl("A",None,IntLiteral(2))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_177(self):
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]),VarDecl("A", None,IntLiteral(1))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_178(self):
        input = Program([FuncDecl("A",[],IntType(),Block([Return(Id("A"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_179(self):
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]),FuncDecl("foo",[],IntType(),Block([Return(Id("A"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_180(self):
        input = Program([StructType("putLn",[("a",IntType())],[])])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_181(self):
        input = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],FloatType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])]),FuncCall("foo",[ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])])]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_182(self):
        input = Program([StructType("S1",[("votien",IntType())],[MethodDecl("s",Id("S1"),FuncDecl("votien1",[],VoidType(),Block([Return(None)])))]),InterfaceType("I1",[Prototype("votien1",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien1",[],VoidType(),Block([Return(None)]))),VarDecl("b",ArrayType([IntLiteral(2)],Id("S1")), None),VarDecl("a",ArrayType([IntLiteral(2)],Id("I1")),Id("b"))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_183(self):
        input = Program([FuncDecl("votien",[ParamDecl("a",ArrayType([IntLiteral(2)],IntType()))],VoidType(),Block([FuncCall("votien",[ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_184(self):
        input = Program([VarDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(9))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(10)],IntType()),Id("a"))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_185(self):
        input = Program([VarDecl("a",ArrayType([BinaryOp("*", IntLiteral(2), IntLiteral(5))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(10)],IntType()),Id("a"))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_186(self):
        input = Program([VarDecl("a",ArrayType([BinaryOp("/", IntLiteral(5), IntLiteral(2))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(2)],IntType()),Id("a"))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_187(self):
        input = Program([VarDecl("a",ArrayType([BinaryOp("%", IntLiteral(5), IntLiteral(2))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(1)],IntType()),Id("a"))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_188(self):
        input = Program([VarDecl("a",ArrayType([BinaryOp("-", IntLiteral(5), IntLiteral(2))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(3)],IntType()),Id("a"))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_189(self):
        input = Program([ConstDecl("a",None,BinaryOp("+", IntLiteral(2), IntLiteral(3))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(15)],IntType()),Id("b"))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_190(self):
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("a",None,BinaryOp("+", Id("v"), Id("v"))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(18)],IntType()),Id("b"))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_191(self):
        input = Program([ConstDecl("v",None,IntLiteral(3)),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),ArrayLiteral([BinaryOp("*", Id("v"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_192(self):
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("k",None,BinaryOp("+", Id("v"), IntLiteral(1))),FuncDecl("foo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([BinaryOp("-", Id("k"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_193(self):
        input = Program([StructType("K",[("a",IntType())],[MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([Return(None)])))]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([Return(None)]))),ConstDecl("c",None,IntLiteral(4)),FuncDecl("foo",[],VoidType(),Block([VarDecl("k",Id("K"), None),MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_194(self):
        input = Program([StructType("K",[("a",IntType())],[MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([Return(None)])))]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([Return(None)]))),InterfaceType("H",[Prototype("koo",[ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType())],VoidType())]),ConstDecl("c",None,IntLiteral(4)),FuncDecl("foo",[],VoidType(),Block([VarDecl("k",Id("H"), None),MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_196(self):
        input = Program([ConstDecl("a",None,BinaryOp("+", StringLiteral(""2""), StringLiteral(""#""))),ConstDecl("b",None,BinaryOp("*", Id("a"), IntLiteral(5)))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_197(self):
        input = Program([VarDecl("v", None,BinaryOp("*", IntLiteral(2), IntLiteral(3))),ConstDecl("a",None,BinaryOp("+", Id("v"), IntLiteral(1))),ConstDecl("b",None,BinaryOp("*", Id("a"), IntLiteral(5))),ConstDecl("c",None,UnaryOp("!",BinaryOp(">", Id("b"), IntLiteral(3))))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_198(self):
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3),IntLiteral(4)],IntType()), None),VarDecl("b",ArrayType([IntLiteral(3),IntLiteral(4)],IntType()),ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(4)],IntType()),ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(1)])),VarDecl("d",IntType(),ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(1),IntLiteral(1)]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_199(self):
        input = Program([ConstDecl("a",None,IntLiteral(3)),ConstDecl("b",None,UnaryOp("-",Id("a"))),ConstDecl("c",None,UnaryOp("-",Id("b"))),VarDecl("d",ArrayType([Id("c")],IntType()),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_200(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[IntLiteral(3)]),IntLiteral(1))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_201(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(Id("a"),"c"),IntLiteral(1))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_202(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_203(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_204(self):
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),FloatLiteral(1.0))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_205(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),FloatLiteral(1.0)),VarDecl("b", None,Id("a")),Assign(Id("b"),IntLiteral(1))]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_206(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,Id("foo"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_207(self):
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("c"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("c",None,IntLiteral(2))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_208(self):
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("c"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), Id("c"))),Block([ConstDecl("c",None,IntLiteral(2))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_209(self):
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("array", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),ForEach(Id("index"),Id("value"),Id("array"),Block([ForEach(Id("index"),Id("value"),Id("brray"),Block([VarDecl("brray", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))]))]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_210(self):
        input = Program([VarDecl("v",Id("TIEN"), None),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],IntType(),Block([Return(Id("v"))]))),StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],IntType(),Block([Return(Id("v"))])))])])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_211(self):
        input = Program([VarDecl("a",IntType(), None),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(Id("a")),Return(Id("v"))]))),StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(Id("a")),Return(Id("v"))])))])])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_212(self):
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("Votien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("Votien",[],VoidType(),Block([Return(None)])))])])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_213(self):
        input = Program([StructType("TIEN",[("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("Votien",[],VoidType(),Block([Return(None)])))]),MethodDecl("v",Id("TIEN"),FuncDecl("Votien",[],VoidType(),Block([Return(None)])))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_214(self):
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Tien",IntType()),("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)])))])])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_215(self):
        input = Program([StructType("TIEN",[("Tien",IntType()),("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)])))]),MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)])))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_216(self):
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("VO",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Tien",IntType()),("Votien",IntType())],[MethodDecl("v",Id("TIEN"),FuncDecl("VO",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)])))])])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_217(self):
        input = Program([FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([FuncCall("foo",[IntLiteral(1)]),VarDecl("foo", None,IntLiteral(1))]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_218(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo1",[],IntType(),Block([Return(FuncCall("foo",[]))]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_219(self):
        input = Program([VarDecl("foo", None,IntLiteral(1)),FuncDecl("foo1",[],IntType(),Block([Return(FuncCall("foo",[]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_220(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,BinaryOp("==", FloatLiteral(1.0), IntLiteral(1)))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_221(self):
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(3)),VarDecl("a", None,FloatLiteral(1.0)),ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp(">", Id("a"), IntLiteral(1)),Assign(Id("a"),IntLiteral(1)),Block([Return(None)]))]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_222(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp(">", Id("a"), IntLiteral(1)),Assign(Id("b"),BinaryOp("+", Id("b"), IntLiteral(1))),Block([Return(None)]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_223(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(Id("foo"))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_224(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("foo"),IntLiteral(1)),VarDecl("foo", None,IntLiteral(1))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_225(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("foo"),IntLiteral(1)),FuncCall("foo",[])]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_226(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([Assign(Id("foo"),IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_227(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([VarDecl("foo", None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_228(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        expect = "" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_229(self):
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(FuncCall("foo",[])),Assign(Id("foo"),IntLiteral(1))]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_230(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        expect = "VOTIEN" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
import sys
import os
import unittest
import inspect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    ## Keywords
    def test_001(self):
        self.assertTrue(TestLexer.test("T","T,<EOF>", inspect.stack()[0].function))

    ## Keywords
    def test_002(self):
        self.assertTrue(TestLexer.test("continue F if else for bool number return string func endfunc call","continue,F,if,else,for,bool,number,return,string,func,endfunc,call,<EOF>", inspect.stack()[0].function))

    ## Operators
    def test_003(self):
        self.assertTrue(TestLexer.test("+-*=><**#<-","+,-,*,=,>,<,**,#,<-,<EOF>", inspect.stack()[0].function))

    ## Separators
    def test_004(self):
        self.assertTrue(TestLexer.test("[]{}(),;:<>","[,],{,},(,),,,;,:,<,>,<EOF>", inspect.stack()[0].function))

    ## Identifiers
    def test_005(self):
        self.assertTrue(TestLexer.test("_1 _b _A_ b A21","_1,_b,_A_,b,A21,<EOF>", inspect.stack()[0].function))

    ## Identifiers
    def test_006(self):
        self.assertTrue(TestLexer.test("@_ @a @13","@_,@a,@13,<EOF>", inspect.stack()[0].function))

    ## Literal
    def test_007(self):
        self.assertTrue(TestLexer.test("10 10.2e-6 0 10e6","10,10.2e-6,0,10e6,<EOF>", inspect.stack()[0].function))

    ## Literal
    def test_008(self):
        self.assertTrue(TestLexer.test("""
            "VOTIEN"
        ""","VOTIEN,<EOF>", inspect.stack()[0].function))

    ## Literal
    def test_009(self):
        self.assertTrue(TestLexer.test("""
            "VOTIEN \t \\b \\f \\r \\n \\t \\\" \\\\"
        ""","VOTIEN \t \\b \\f \\r \\n \\t \\\" \\\\,<EOF>", inspect.stack()[0].function))

    ## Literal
    def test_010(self):
        self.assertTrue(TestLexer.test("""
            "'VOTIEN'"
        ""","'VOTIEN',<EOF>", inspect.stack()[0].function))

    ## Skip
    def test_017(self):
        self.assertTrue(TestLexer.test("""
            // VOTIEN
            /*
                VOTIEN
                /* VOTIEN
                // VOTIEN
            */
            /* // VOTIEN */
            // VOTIEN
        ""","<EOF>", inspect.stack()[0].function))

    ## ErrorToken
    def test_011(self):
        self.assertTrue(TestLexer.test("^","Error Token ^", inspect.stack()[0].function))

    ## ErrorToken
    def test_016(self):
        self.assertTrue(TestLexer.test("!","Error Token !", inspect.stack()[0].function))

    ## UNCLOSE_STRING
    def test_012(self):
        self.assertTrue(TestLexer.test("""
            "VOTIEN \n"
        ""","Unclosed String: VOTIEN ", inspect.stack()[0].function))

    ## UNCLOSE_STRING
    def test_013(self):
        self.assertTrue(TestLexer.test("""
            "VOTIEN \\n
            "
        ""","Unclosed String: VOTIEN \\n", inspect.stack()[0].function))

    ## ILLEGAL_ESCAPE
    def test_014(self):
        self.assertTrue(TestLexer.test("""
            "VOTIEN \\z
            "
        ""","Illegal Escape In String: VOTIEN \\z", inspect.stack()[0].function))

    ##
    def test_015(self):
        self.assertTrue(TestLexer.test("""
number @array = <1, 0, -1>;
func number foo(a : number, b : bool):
a <- a + 1;
for (number c <- 2; > 3; #2) {
if c = 2 {
b <- [0]@array * 2 > a;
continue;
}
}
return a;
endfunc
func void main():
number a <- 0;
a = a ** call foo <- a, T;
call printNumber <- a;
endfunc
        ""","number,@array,=,<,1,,,0,,,-,1,>,;,func,number,foo,(,a,:,number,,,b,:,bool,),:,a,<-,a,+,1,;,for,(,number,c,<-,2,;,>,3,;,#,2,),{,if,c,=,2,{,b,<-,[,0,],@array,*,2,>,a,;,continue,;,},},return,a,;,endfunc,func,void,main,(,),:,number,a,<-,0,;,a,=,a,**,call,foo,<-,a,,,T,;,call,printNumber,<-,a,;,endfunc,<EOF>", inspect.stack()[0].function))
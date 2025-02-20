"""
 * Initial code for Assignment 1, 2
 * file : testunile.py
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""

from antlr4 import *
from MiniGoLexer import MiniGoLexer
from MiniGoParser import MiniGoParser
from ASTGeneration import ASTGeneration

class TestUtil:
    @staticmethod
    def makeSource(inputStr, inputfile):
        file = open(inputfile, "w")
        file.write(inputStr)
        file.close()
        return FileStream(inputfile)

class TestAST:
    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, 'input/' + str(num) + ".txt")
        TestAST.check('output/' + str(num) + ".txt", inputfile)
        dest = open('output/' + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputfile):
        dest = open(soldir, "w")
        lexer = MiniGoLexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = MiniGoParser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()
"""
 * Initial code for Assignment 1, 2
 * file : testunile.py
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""


import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
if not './main/' in sys.path:
    sys.path.append('./main/')
if os.path.isdir('./target/') and not './target/' in sys.path:
    sys.path.append('./target/')
from MiniGoLexer import MiniGoLexer
from MiniGoParser import MiniGoParser
from lexererr import *

JASMIN_JAR = "./test/CodeGen/external/jasmin.jar"
TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/"
Lexer = MiniGoLexer
Parser = MiniGoParser


class TestUtil:
    @staticmethod
    def makeSource(inputStr, inputfile):
        file = open(inputfile, "w")
        file.write(inputStr)
        file.close()
        return FileStream(inputfile)

class TestLexer:
    _DIR = './test/Lexer/'
    
    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, TestLexer._DIR + 'input/' + str(num) + ".txt")
        TestLexer.check(TestLexer._DIR + 'output/' + str(num) + ".txt", inputfile)
        dest = open(TestLexer._DIR + 'output/' + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputfile):
        dest = open(soldir, "w")
        lexer = Lexer(inputfile)
        try:
            TestLexer.printLexeme(dest, lexer)
        except (ErrorToken, UncloseString, IllegalEscape) as err:
            dest.write(err.message)
        finally:
            dest.close()

    @staticmethod
    def printLexeme(dest, lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+",")
            TestLexer.printLexeme(dest, lexer)
        else:
            dest.write("<EOF>")

class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)

NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg

class TestParser:
    
    _DIR = './test/Parser/'
    
    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE

    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, TestParser._DIR + 'input/' + str(num) + ".txt")
        TestParser.check(TestParser._DIR + 'output/' + str(num) + ".txt", inputfile)
        dest = open(TestParser._DIR + 'output/' + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect
        
    @staticmethod
    def check(soldir, inputfile):
        dest = open(soldir, "w")
        lexer = Lexer(inputfile)
        listener = TestParser.createErrorListener()
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()

class TestAST:
    _DIR = './test/ASTGen/'
    
    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, TestAST._DIR + 'input/' + str(num) + ".txt")
        TestAST.check(TestAST._DIR + 'output/' + str(num) + ".txt", inputfile)
        dest = open(TestAST._DIR + 'output/' + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputfile):
        dest = open(soldir, "w")
        lexer = Lexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()

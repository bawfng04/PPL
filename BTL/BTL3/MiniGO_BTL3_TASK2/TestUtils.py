"""
 * Initial code for Assignment 3
 * file : testunile.py
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""

from antlr4 import *
from StaticError import *
from StaticCheck import StaticChecker

class TestUtil:
    @staticmethod
    def makeSource(inputStr, inputfile):
        file = open(inputfile, "w")
        file.write(inputStr)
        file.close()
        return FileStream(inputfile)

class TestChecker:
    @staticmethod
    def test(input, expect, num):
        TestChecker.check('output/' + str(num) + ".txt", input)
        dest = open('output/' + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, asttree):
        dest = open(soldir, "w")
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            dest.write("VOTIEN")
            # dest.write(str(list(res)))
        except StaticError as e:
            dest.write(str(e))
        finally:
            dest.close()
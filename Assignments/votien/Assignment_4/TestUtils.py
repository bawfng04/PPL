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
from CodeGenerator import CodeGenerator
import sys
import os
import subprocess
from MiniGoLexer import MiniGoLexer
from MiniGoParser import MiniGoParser
from lexererr import *
from ASTGeneration import ASTGeneration
from CodeGenError import *


class TestUtil:
    @staticmethod
    def makeSource(inputStr,num):
        filename = "./testcases/" + str(num) + ".txt"
        file = open(filename,"w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)

class TestCodeGen:
    @staticmethod
    def test(input,expect,num):
        return TestCodeGen.checkStatic(input,expect,num)
    @staticmethod
    def checkStatic(input,expect,num):
        dest = open("./solutions/" + str(num) + ".txt","w")

        if type(input) is str:
            inputfile = TestUtil.makeSource(input,num)
            lexer = MiniGoLexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = MiniGoParser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
            x = open("./AST/" + str(num) + ".txt","w")
            x.write(str(asttree))
        else:
            inputfile = TestUtil.makeSource(str(input),num)
            asttree = input


        codeGen = CodeGenerator()
        path = "java_byte_code/" +  num
        if not os.path.isdir(path):
            os.mkdir(path)

        base_path = f"java_byte_code/{num}"
        jasmin_jar = "../jasmin.jar"
        miniGO_class = "MiniGoClass"
        output_file = f"solutions/{num}.txt"

        f = open(output_file, "w")
        codeGen.gen(asttree, path)
        try:
            subprocess.run(
                ["java", "-jar", jasmin_jar, f"{miniGO_class}.j"],
                cwd=base_path,
                stderr=subprocess.STDOUT,
                check=True
            )

            subprocess.run(
                ["java", "-cp", "../_io;.", miniGO_class],
                cwd=base_path,
                stdout=f,
                stderr=subprocess.STDOUT,
                timeout=10,
                check=True
            )
        except IllegalOperandException as e:
            f.write(str(e) + "\n")
        except IllegalRuntimeException as e:
            f.write(str(e) + "\n")
        except subprocess.CalledProcessError as e:
            f.write(f"Subprocess error: {e}\n")
        except subprocess.TimeoutExpired as e:
            f.write(f"Timeout error: {e}\n")
        except Exception as e:
            f.write(f"Unexpected error: {e}\n")

        dest = open("./solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect















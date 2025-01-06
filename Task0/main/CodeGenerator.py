"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 02.01.2025
"""
from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *
from Utils import *
from CodeGenError import *



class CodeGenerator:
    
    def gen(self, ast, path):
        gc = CodeGenVisitor(ast, path)
        gc.visit(ast, None)
        
class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, path):
        self.astTree = astTree
        self.emit = Emitter(path + "/VoTien.j")

        
    def visitProgram(self, ast:Program, o):
        
        self.emit.printout("""

; VoTien.j

.bytecode 61.0
.source VoTien.java
.class public VoTien
.super java/lang/Object

.method public <init>()V
  .limit stack 1
  .limit locals 1
  .line 6
  0: aload_0
  1: invokespecial java/lang/Object/<init>()V
  4: return
.end method

.method public static main([Ljava/lang/String;)V
  .limit stack 2
  .limit locals 1
  .line 8
  0: getstatic java/lang/System/err Ljava/io/PrintStream;
  3: ldc "VoTien"
  5: invokestatic io/writeString(Ljava/lang/String;)V
  .line 9
  8: return
.end method
                           """)
        
        
        self.emit.emitEPILOG()
    

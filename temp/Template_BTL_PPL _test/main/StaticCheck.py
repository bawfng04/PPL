"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 02.01.2025
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class VarVoTien:
    def __init__(self, name):
        self.name = name
        

class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.ast = ast

    def check(self):
        self.visit(self.ast,None)
        return "successful" 
    
    
    #* ast
        #* decl: List[Decl]
    def visitProgram(self, ast, param):
        param = []
        [self.visit(i, param) for i in ast.decl]


    #* ast
        #* name: string
        #* varType: Type
        #* varInit: Expr 
    def visitVarDecl(self, ast, param):
        for i in param:
            if i.name == ast.name:
                raise Redeclared(Variable(), ast.name)
        param.append(VarVoTien(ast.name))
        self.visit(ast.varInit, param)
                

    #* ast
        #* op: str
        #* left: Expr
        #* right: Expr
    def visitBinaryOp(self, ast, param):
        self.visit(ast.left, param)
        self.visit(ast.right, param)


    #* ast
        #* name: str
    def visitId(self, ast, param):
        for i in param:
                    if i.name == ast.name:
                        return
        raise Undeclared(Identifier(), ast.name)


    #* ast
        #* name: name
        #* args: Expr
    def visitCallStmt(self, ast, param):
        self.visit(ast.args, param)

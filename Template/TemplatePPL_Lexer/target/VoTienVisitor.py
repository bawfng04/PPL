# Generated from main/VoTien.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VoTienParser import VoTienParser
else:
    from VoTienParser import VoTienParser

# This class defines a complete generic visitor for a parse tree produced by VoTienParser.

class VoTienVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VoTienParser#program.
    def visitProgram(self, ctx:VoTienParser.ProgramContext):
        return self.visitChildren(ctx)



del VoTienParser
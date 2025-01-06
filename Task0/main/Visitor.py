from abc import ABC, abstractmethod, ABCMeta


class Visitor(ABC):

    def visit(self, ast, param):
        return ast.accept(self, param)

    @abstractmethod
    def visitProgram(self, ast, param):
        pass

    @abstractmethod
    def visitVarDecl(self, ast, param):
        pass

    @abstractmethod
    def visitBinaryOp(self, ast, param):
        pass

    @abstractmethod
    def visitId(self, ast, param):
        pass

    @abstractmethod
    def visitCallStmt(self, ast, param):
        pass
    
    @abstractmethod
    def visitIntLiteral(self, ast, param):
        pass


class BaseVisitor(Visitor):

    def visitProgram(self, ast, param):
        pass

    def visitVarDecl(self, ast, param):
        pass

    def visitBinaryOp(self, ast, param):
        pass

    def visitId(self, ast, param):
        pass

    def visitCallStmt(self, ast, param):
        pass
    
    def visitIntLiteral(self, ast, param):
        pass


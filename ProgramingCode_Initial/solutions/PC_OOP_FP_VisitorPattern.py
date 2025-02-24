from abc import ABC, abstractmethod

class Exp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class BinExp(Exp):
    def __init__(self, o1, op, o2):
        self.left = o1
        self.op = op
        self.right = o2

    def accept(self, visitor):
        return visitor.visitBinExp(self)

class UnExp(Exp):
    def __init__(self, op, o1):
        self.op = op
        self.operand = o1

    def accept(self, visitor):
        return visitor.visitUnExp(self)

class IntLit(Exp):
    def __init__(self, v):
        self.value = v

    def accept(self, visitor):
        return visitor.visitIntLit(self)

class FloatLit(Exp):
    def __init__(self, v):
        self.value = v

    def accept(self, visitor):
        return visitor.visitFloatLit(self)

class Visitor(ABC):
    def visit(self, exp):
        return exp.accept(self)

    @abstractmethod
    def visitBinExp(self, exp): pass

    @abstractmethod
    def visitUnExp(self, exp): pass

    @abstractmethod
    def visitIntLit(self, exp): pass

    @abstractmethod
    def visitFloatLit(self, exp): pass


class Eval(Visitor):
    def visitBinExp(self, exp):
        left_val = exp.left.accept(self)
        right_val = exp.right.accept(self)
        if exp.op == "+": return left_val + right_val
        elif exp.op == "-": return left_val - right_val
        elif exp.op == "*": return left_val * right_val
        elif exp.op == "/": return left_val / right_val
        else: return None

    def visitUnExp(self, exp):
        val = exp.operand.accept(self)
        if exp.op == "+": return val
        elif exp.op == "-": return -val
        else: return None

    def visitIntLit(self, exp):
        return exp.value

    def visitFloatLit(self, exp):
        return exp.value

class PrintPrefix(Visitor):
    def visitBinExp(self, exp):
        return f"{exp.op} {exp.left.accept(self)}{exp.right.accept(self)}"

    def visitUnExp(self, exp):
        op = "+." if exp.op == "+" else "-."
        return f"{op} {exp.operand.accept(self)}"

    def visitIntLit(self, exp):
        return f"{exp.value} "

    def visitFloatLit(self, exp):
        return f"{exp.value} "
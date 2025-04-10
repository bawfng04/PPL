# 1
def lstSquare(n: int) -> list:
    if n == 0:
        return []
    else:
        return lstSquare(n - 1) + [n * n]


# 2
def lstSquare(n: int) -> list:
    return [i * i for i in range(1, n + 1)]

# 3
def lstSquare(n: int) -> list:
    return list(map(lambda i: i * i, range(1, n + 1)))

# 4
def dist(lst: list, n: int) -> list:
    if not lst:
        return []
    else:
        return [(lst[0], n)] + dist(lst[1:], n)


# 5
def dist(lst: list, n: int) -> list:
    return [(i, n) for i in lst]

# 6
def dist(lst: list, n: int) -> list:
    return list(map(lambda i: (i, n), lst))

# 7
def lessThan(lst: list, n: int) -> list:
    if not lst:
        return []
    elif lst[0] < n:
        return [lst[0]] + lessThan(lst[1:], n)
    else:
        return lessThan(lst[1:], n)

# 8
def lessThan(lst: list, n: int) -> list:
    return [i for i in lst if i < n]

# 9
def lessThan(lst: list, n: int) -> list:
    return list(filter(lambda i: i < n, lst))

# 10
def flatten(lst: list) -> list:
    if not lst:
        return []
    elif isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst[0]] + flatten(lst[1:])


# 11
def flatten(lst: list) -> list:
    return [element for sublist in lst for element in sublist]

# 12
from functools import reduce

def flatten(lst):
    return reduce(lambda x, y: x + y, lst, [])

# 13
class Exp:
    def eval(self):
        pass

class BinExp(Exp):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()

        if self.operator == "+":
            return left_val + right_val
        elif self.operator == "-":
            return left_val - right_val
        elif self.operator == "*":
            return left_val * right_val
        elif self.operator == "/":
            return left_val / right_val
        else:
            return None

class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def eval(self):
        value = self.operand.eval()
        if self.operator == "+":
            return value
        elif self.operator == "-":
            return -value
        else:
            return None

class IntLit(Exp):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class FloatLit(Exp):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

# 14
class Exp:
    def eval(self):
        pass

    def printPrefix(self):
        pass

class BinExp(Exp):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()

        if self.operator == "+":
            return left_val + right_val
        elif self.operator == "-":
            return left_val - right_val
        elif self.operator == "*":
            return left_val * right_val
        elif self.operator == "/":
            return left_val / right_val
        else:
            return None

    def printPrefix(self):
        return f"{self.operator} {self.left.printPrefix()}{self.right.printPrefix()}"

class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def eval(self):
        value = self.operand.eval()
        if self.operator == "+":
            return value
        elif self.operator == "-":
            return -value
        else:
            return None

    def printPrefix(self):
        operator = "+." if self.operator == "+" else "-."
        return f"{operator} {self.operand.printPrefix()}"

class IntLit(Exp):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

    def printPrefix(self):
        return f"{self.value} "

class FloatLit(Exp):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

    def printPrefix(self):
        return f"{self.value} "

# 15
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
        return visitor.visit(self)

class UnExp(Exp):
    def __init__(self, op, o1):
        self.op = op
        self.operand = o1

    def accept(self, visitor):
        return visitor.visit(self)

class IntLit(Exp):
    def __init__(self, v):
        self.value = v

    def accept(self, visitor):
        return visitor.visit(self)

class FloatLit(Exp):
    def __init__(self, v):
        self.value = v

    def accept(self, visitor):
        return visitor.visit(self)

class Visitor(ABC):
    @abstractmethod
    def visit(self, exp): pass

class Eval(Visitor):
    def visit(self, exp):
        if isinstance(exp, IntLit) or isinstance(exp, FloatLit):
            return exp.value
        elif isinstance(exp, BinExp):
            left_val = exp.left.accept(self)
            right_val = exp.right.accept(self)
            if exp.op == "+": return left_val + right_val
            elif exp.op == "-": return left_val - right_val
            elif exp.op == "*": return left_val * right_val
            elif exp.op == "/": return left_val / right_val
            else: return None
        elif isinstance(exp, UnExp):
            val = exp.operand.accept(self)
            if exp.op == "+": return val
            elif exp.op == "-": return -val
            else: return None

class PrintPrefix(Visitor):
    def visit(self, exp):
        if isinstance(exp, IntLit) or isinstance(exp, FloatLit):
            return f"{exp.value} "
        elif isinstance(exp, BinExp):
            return f"{exp.op} {exp.left.accept(self)}{exp.right.accept(self)}"
        elif isinstance(exp, UnExp):
            op = "+." if exp.op == "+" else "-."
            return f"{op} {exp.operand.accept(self)}"

# 16
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

# 17
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

class PrintPostfix(Visitor):
    def visitBinExp(self, exp):
        return f"{exp.left.accept(self)}{exp.right.accept(self)}{exp.op} "

    def visitUnExp(self, exp):
        op = "+." if exp.op == "+" else "-."
        return f"{exp.operand.accept(self)}{op} "

    def visitIntLit(self, exp):
        return f"{exp.value} "

    def visitFloatLit(self, exp):
        return f"{exp.value} "




# temp
def lstSquare(n: int) -> list:
    return list(map(lambda i: i * i, range(1, n + 1)))


print(lstSquare(3))


def lessThan(lst: list, n: int) -> list:
    return [i for i in lst if i < n]

print(lessThan([1, 2, 3, 4, 5], 4))


def flatten1(lst: list) -> list:
    if not lst:
        return []
    elif isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst[0]] + flatten(lst[1:])


def flatten2(lst: list) -> list:
    return [element for sublist in lst for element in sublist]


print(flatten2([[1, 2, 3], [4, 5], [6, 7]]))


# Let lst be a list of a list of element, use high-order function approach to write function flatten(lst) that returns the list of all elements


def flatten3(lst: list) -> list:
    return reduce(lambda x, y: x + y, lst)

print(flatten3([[1, 2, 3], [4, 5], [6, 7]]))
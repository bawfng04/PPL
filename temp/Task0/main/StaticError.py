# update: 6/04/2019
from abc import ABC
from dataclasses import dataclass
from AST import *


class Kind(ABC):
    pass


class Identifier(Kind):
    def __str__(self):
        return "Identifier"


class Variable(Kind):
    def __str__(self):
        return "Variable"


class StaticError(Exception):
    pass


class Redeclared(StaticError):
    # kind: Kind
    # name: str

    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f"Redeclared({str(self.kind)}: {self.name})"


class Undeclared(StaticError):
    # kind: Kind
    # name: str
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name
        
    def __str__(self):
        return f"Undeclared({str(self.kind)}: {self.name})"
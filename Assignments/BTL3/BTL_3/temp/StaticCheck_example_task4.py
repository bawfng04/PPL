from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Tuple, Union

from StaticError import Type as StaticErrorType
from AST import Type

class FuntionType(Type):
    def __str__(self):
        return "FuntionType"

    def accept(self, v, param):
        return v.visitFuntionType(self, v, param)


class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):


    def __init__(self,ast):
        self.ast = ast
        self.list_type: List[Union[StructType, InterfaceType]] = []
        self.list_function: List[FuncDecl] =  [
                FuncDecl("getInt", [], IntType(), Block([])),
                FuncDecl("putInt", [ParamDecl("VOTIEN", IntType())], VoidType(), Block([])),
                FuncDecl("putIntLn", [ParamDecl("VOTIEN", IntType())], VoidType(), Block([])),
                FuncDecl("getString", [], IntType(), Block([])),
                FuncDecl("putString", [ParamDecl("VOTIEN", IntType())], VoidType(), Block([])),
                FuncDecl("putStringLn", [ParamDecl("VOTIEN", StringType())], VoidType(), Block([]))
            ]
        self.function_current: FuncDecl = None

    def check(self):
        self.visit(self.ast, None)

    def checkType(self, LSH_type: Type, RHS_type: Type, list_type_permission: List[Tuple[Type, Type]] = []) -> bool:
        if type(RHS_type) == StructType and RHS_type.name == "":
            return type(LSH_type) == StructType  # nil can be assigned to any struct type

        LSH_type = self.lookup(LSH_type.name, self.list_type, lambda x: x.name) if isinstance(LSH_type, Id) else LSH_type
        RHS_type = self.lookup(RHS_type.name, self.list_type, lambda x: x.name) if isinstance(RHS_type, Id) else RHS_type
        if (type(LSH_type), type(RHS_type)) in list_type_permission:
            if isinstance(LSH_type, InterfaceType) and isinstance(RHS_type, StructType):
                # Check if struct implements all methods in interface
                for proto in LSH_type.methods:
                    found = False
                    for method in RHS_type.methods:
                        if method.fun.name == proto.name:
                            # Check return type and parameter types match
                            if type(method.fun.retType) != type(proto.retType):
                                return False
                            if len(method.fun.params) != len(proto.params):
                                return False
                            for i in range(len(proto.params)):
                                if type(method.fun.params[i].parType) != type(proto.params[i]):
                                    return False
                            found = True
                            break
                    if not found:
                        return False
                return True
            return True

        if isinstance(LSH_type, StructType) and isinstance(RHS_type, StructType) or \
        isinstance(LSH_type, InterfaceType) and isinstance(RHS_type, InterfaceType):
            return LSH_type.name == RHS_type.name

        if isinstance(LSH_type, ArrayType) and isinstance(RHS_type, ArrayType):
            return len(LSH_type.dimens) == len(RHS_type.dimens) and self.checkType(LSH_type.eleType, RHS_type.eleType, list_type_permission)
        return type(LSH_type) == type(RHS_type)


    def visitProgram(self, ast: Program,c : None):
        def visitMethodDecl(ast: MethodDecl, c: StructType) -> MethodDecl:
            # Check if struct exists
            if not c:
                raise Undeclared(Type(), ast.recType.name)

            # Check if method already exists in struct
            for method in c.methods:
                if method.fun.name == ast.fun.name:
                    raise Redeclared(Method(), ast.fun.name)

            # Add method to struct
            c.methods.append(ast)
            return ast


        self.list_type = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc if isinstance(ele, Type) else acc, ast.decl, [])
        self.list_function = self.list_function + list(filter(lambda item: isinstance(item, FuncDecl), ast.decl))

        list(map(
            lambda item: visitMethodDecl(item, self.lookup(item.recType.name, self.list_type, lambda x: x.name)),
            list(filter(lambda item: isinstance(item, MethodDecl), ast.decl))
        ))

        reduce(
            lambda acc, ele: [
                ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
            ] + acc[1:],
            filter(lambda item: isinstance(item, Decl), ast.decl),
            [[
                Symbol("getInt", FuntionType()),
                Symbol("putInt", FuntionType()),
                Symbol("putIntLn", FuntionType()),
                Symbol("getString", FuntionType()),
                Symbol("putStringLn", FuntionType())
            ]]
        )

    def visitStructType(self, ast: StructType, c : List[Union[StructType, InterfaceType]]) -> StructType:
        # First check if the struct name conflicts with an existing function
        func_res = self.lookup(ast.name, self.list_function, lambda x: x.name)
        if func_res is not None:
            raise Redeclared(StaticErrorType(), ast.name)

        # Then check if it conflicts with other types
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)

        def visitElements(element: Tuple[str,Type], c: List[Tuple[str,Type]]) -> Tuple[str,Type]:
            fieldName, fieldType = element
            for name, _ in c:
                if name == fieldName:
                    raise Redeclared(Field(), fieldName)
            return element

        ast.elements = reduce(lambda acc,ele: [visitElements(ele,acc)] + acc , ast.elements , [])
        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        for proto in c:
            if proto.name == ast.name:
                raise Redeclared(Prototype(), ast.name)
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c : List[Union[StructType, InterfaceType]]) -> InterfaceType:
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)
        ast.methods = reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.methods , [])
        return ast

    def visitFuncDecl(self, ast: FuncDecl, c : List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)

        old_function = self.function_current
        self.function_current = ast

        self.visit(ast.body, [list(reduce(lambda acc,ele: [self.visit(ele,acc)] + acc, ast.params, []))] + c)

        self.function_current = old_function
        return Symbol(ast.name, FuntionType())

    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        res = self.lookup(ast.parName, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast: MethodDecl, c : List[List[Symbol]]) -> None:
        # First check if the receiver type exists
        if isinstance(ast.recType, Id):
            struct = self.lookup(ast.recType.name, self.list_type, lambda x: x.name)
            if struct is None:
                raise Undeclared(Type(), ast.recType.name)

        # Save current function context
        old_function = self.function_current
        self.function_current = ast.fun

        # Create parameter scope with the receiver
        receiver_symbol = Symbol(ast.receiver, ast.recType, None)
        param_symbols = [receiver_symbol]  # Add receiver to param list first

        # Process parameters
        for param in ast.fun.params:
            # Check against the receiver name
            if param.parName == ast.receiver:
                raise Redeclared(Parameter(), param.parName)

            # Add parameter
            sym = self.visit(param, param_symbols)
            param_symbols.append(sym)

        # Visit function body with new scope
        self.visit(ast.fun.body, [param_symbols] + c)

        # Restore function context
        self.function_current = old_function

    def visitVarDecl(self, ast: VarDecl, c : List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName)

        LHS_type = ast.varType if ast.varType else None
        RHS_type = self.visit(ast.varInit, c) if ast.varInit else None

        if RHS_type is None:
            return Symbol(ast.varName, LHS_type, None)
        elif LHS_type is None:
            return Symbol(ast.varName, RHS_type, None)
        elif self.checkType(LHS_type, RHS_type, [(FloatType, IntType), (InterfaceType, StructType)]):
            return Symbol(ast.varName, LHS_type, None)
        raise TypeMismatch(ast)


    def visitConstDecl(self, ast: ConstDecl, c : List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Constant(), ast.conName)

        LHS_type = ast.conType if ast.conType else None
        RHS_type = self.visit(ast.iniExpr, c) if ast.iniExpr else None

        if RHS_type is None:
            raise TypeMismatch(ast)
        elif LHS_type is None:
            return Symbol(ast.conName, RHS_type, ast.iniExpr)
        elif self.checkType(LHS_type, RHS_type, [(FloatType, IntType), (InterfaceType, StructType)]):
            return Symbol(ast.conName, LHS_type, ast.iniExpr)
        raise TypeMismatch(ast)

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        acc = [[]] + c

        for ele in ast.member:
            result = self.visit(ele, (acc, True)) if isinstance(ele, (FuncCall, MethCall)) else self.visit(ele, acc)
            if isinstance(result, Symbol):
                acc[0] = [result] + acc[0]

    def visitForBasic(self, ast: ForBasic, c : List[List[Symbol]]) -> None:
        if not isinstance(self.visit(ast.cond, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
        symbol = self.visit(ast.init, [[]] + c)
        if not isinstance(self.visit(ast.cond, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(Block([ast.init] + ast.loop.member + [ast.upda]), c)

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None:
        type_array = self.visit(ast.arr, c)
        if not isinstance(type_array, ArrayType):
            raise TypeMismatch(ast)

        self.visit(Block([VarDecl(ast.idx.name, IntType(), None),
                        VarDecl(ast.value.name,
                                type_array.eleType,
                                None)] + ast.loop.member)
                        , c)

    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        res = next(filter(None, (self.lookup(ast.name, scope, lambda x: x.name) for scope in c)), None)
        if res and not isinstance(res.mtype, Function):
            return res.mtype if not isinstance(res.mtype, Id) else self.lookup(res.mtype.name, self.list_type, lambda x: x.name)
        raise Undeclared(Identifier(), ast.name)

    def visitFuncCall(self, ast: FuncCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c

        res = self.lookup(ast.funName, self.list_function, lambda x: x.name)
        if res:
            if len(res.params) != len(ast.args):
                raise TypeMismatch(ast)
            for param, arg in zip(res.params, ast.args):
                arg_type = self.visit(arg, c)
                if not self.checkType(param.parType, arg_type, [(FloatType, IntType)]):
                    raise TypeMismatch(ast)

            if is_stmt and not isinstance(res.retType, VoidType):
                raise TypeMismatch(ast)
            if not is_stmt and isinstance(res.retType, VoidType):
                raise TypeMismatch(ast)
            return res.retType
        raise Undeclared(Function(), ast.funName)

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        receiver_type = self.visit(ast.receiver, c)
        receiver_type = self.lookup(receiver_type.name, self.list_type, lambda x: x.name) if isinstance(receiver_type, Id) else receiver_type
        if not isinstance(receiver_type, StructType):
            raise TypeMismatch(ast)

        res = self.lookup(ast.field, receiver_type.elements, lambda x: x[0])
        if res is None:
            raise Undeclared(Field(), ast.field)
        return res[1]

    def visitMethCall(self, ast: MethCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c

        receiver_type = self.visit(ast.receiver, c)
        receiver_type = self.lookup(receiver_type.name, self.list_type, lambda x: x.name) if isinstance(receiver_type, Id) else receiver_type
        if not (isinstance(receiver_type, StructType) or isinstance(receiver_type, InterfaceType)):
            raise TypeMismatch(ast)

        res = self.lookup(ast.metName, receiver_type.methods, lambda x: x.fun.name) if isinstance(receiver_type, StructType) else self.lookup(ast.metName, receiver_type.methods, lambda x: x.name)
        if res:
            if type(receiver_type) == StructType:
                if len(res.fun.params) != len(ast.args):
                    raise TypeMismatch(ast)

                for param, arg in zip(res.fun.params, ast.args):
                    arg_type = self.visit(arg, c)
                    if not self.checkType(param.parType, arg_type, [(FloatType, IntType)]):
                        raise TypeMismatch(ast)

                if is_stmt and not isinstance(res.fun.retType, VoidType):
                    raise TypeMismatch(ast)
                if not is_stmt and isinstance(res.fun.retType, VoidType):
                    raise TypeMismatch(ast)
                return res.fun.retType

            if type(receiver_type) == InterfaceType:
                if len(res.params) != len(ast.args):
                    raise TypeMismatch(ast)

                for param, arg in zip(res.params, ast.args):
                    if not self.checkType(param, self.visit(arg, c), [(FloatType, IntType)]):
                        raise TypeMismatch(ast)

                if is_stmt and isinstance(res.retType, VoidType) == False:
                    raise TypeMismatch(ast)
                if not is_stmt and isinstance(res.retType, VoidType):
                    raise TypeMismatch(ast)
                return res.retType
        raise Undeclared(Method(), ast.metName)


    def visitIntType(self, ast, c: List[List[Symbol]]) -> Type: return ast

    def visitFloatType(self, ast, c: List[List[Symbol]])-> Type: return ast

    def visitBoolType(self, ast, c: List[List[Symbol]])-> Type: return ast

    def visitStringType(self, ast, c: List[List[Symbol]]) -> Type: return ast

    def visitVoidType(self, ast, c: List[List[Symbol]]) -> Type: return ast

    def visitArrayType(self, ast: ArrayType, c: List[List[Symbol]]):
        list(map(lambda item: self.visit(item, c), ast.dimens))
        return ast

    def visitAssign(self, ast: Assign, c: List[List[Symbol]]) -> None:
        LHS_type = self.visit(ast.lhs, c)
        RHS_type = self.visit(ast.rhs, c)
        if not self.checkType(LHS_type, RHS_type, [(FloatType, IntType), (InterfaceType, StructType)]):
            raise TypeMismatch(ast)

    def visitIf(self, ast: If, c: List[List[Symbol]]) -> None:
        if not isinstance(self.visit(ast.expr, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(Block(ast.thenStmt.member), c)
        if ast.elseStmt:
            self.visit(Block(ast.elseStmt.member), c)

    def visitContinue(self, ast, c: List[List[Symbol]]) -> None: return None

    def visitBreak(self, ast, c: List[List[Symbol]]) -> None: return None

    def visitReturn(self, ast, c: List[List[Symbol]]) -> None:
        if ast.expr is None:
            if not isinstance(self.function_current.retType, VoidType):
                raise TypeMismatch(ast)
        else:
            expr_type = self.visit(ast.expr, c)
            if not self.checkType(self.function_current.retType, expr_type, [(FloatType, IntType)]):
                raise TypeMismatch(ast)
        return None

    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]):
        LHS_type = self.visit(ast.left, c)
        RHS_type = self.visit(ast.right, c)

        if ast.op in ['+', '-', '*', '/', '%']:
            if self.checkType(LHS_type, RHS_type, [(IntType, FloatType), (FloatType, IntType)]):
                if isinstance(LHS_type, StringType) and ast.op == '+':
                    return StringType()
                elif isinstance(LHS_type, FloatType) or isinstance(RHS_type, FloatType):
                    return FloatType()
                return IntType()
        elif ast.op in ['==', '!=']:
            if (isinstance(LHS_type, IntType) and isinstance(RHS_type, IntType)) or \
            (isinstance(LHS_type, BoolType) and isinstance(RHS_type, BoolType)):
                return BoolType()
        elif ast.op in ['<', '>', '<=', '>=']:
            if (isinstance(LHS_type, IntType) or isinstance(LHS_type, FloatType)) and \
            (isinstance(RHS_type, IntType) or isinstance(RHS_type, FloatType)):
                return BoolType()
        elif ast.op in ['&&', '||']:
            if isinstance(LHS_type, BoolType) and isinstance(RHS_type, BoolType):
                return BoolType()
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]):
        unary_type = self.visit(ast.body, c)
        if ast.op == '!' and isinstance(unary_type, BoolType):
            return BoolType()
        if ast.op == '-' and (isinstance(unary_type, IntType) or isinstance(unary_type, FloatType)):
            return unary_type
        raise TypeMismatch(ast)

    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]):
        array_type = self.visit(ast.arr, c)
        if not isinstance(array_type, ArrayType):
            raise TypeMismatch(ast)

        if not all(map(lambda item: isinstance(self.visit(item, c), IntType), ast.idx)):
            raise TypeMismatch(ast)
        if len(array_type.dimens) == len(ast.idx):
            return array_type.eleType
        elif len(array_type.dimens) > len(ast.idx):
            return ArrayType(array_type.dimens[len(ast.idx):], array_type.eleType)
        raise TypeMismatch(ast)

    def visitIntLiteral(self, ast, c: List[List[Symbol]]) -> Type: return IntType()
    def visitFloatLiteral(self, ast, c: List[List[Symbol]]) -> Type: return FloatType()
    def visitBooleanLiteral(self, ast, c: List[List[Symbol]]) -> Type: return BoolType()
    def visitStringLiteral(self, ast, c: List[List[Symbol]]) -> Type: return StringType()

    def visitArrayLiteral(self, ast:ArrayLiteral, c: List[List[Symbol]]) -> Type:
        def nested2recursive(dat: Union[Literal, list['NestedList']], c: List[List[Symbol]]):
            if isinstance(dat,list):
                list(map(lambda value: nested2recursive(value, c), dat))
            else:
                self.visit(dat, c)
        nested2recursive(ast.value, c)
        return ArrayType(ast.dimens, ast.eleType)

    def visitStructLiteral(self, ast:StructLiteral, c: List[List[Symbol]]) -> Type:
        list(map(lambda value: self.visit(value[1], c), ast.elements))
        return self.lookup(ast.name, self.list_type, lambda x: x.name)

    def visitNilLiteral(self, ast:NilLiteral, c: List[List[Symbol]]) -> Type: return StructType("", [], [])
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
        return v.visitFuntionType(self, param)


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
                FuncDecl("getString", [], StringType(), Block([])),
                FuncDecl("putStringLn", [ParamDecl("VOTIEN", StringType())], VoidType(), Block([])),
            ]
        self.function_current: FuncDecl = None

    def check(self):
        return self.visit(self.ast, [
            [
                Symbol("getInt", FuntionType()),
                Symbol("putInt", FuntionType()),
                Symbol("putIntLn", FuntionType()),
                Symbol("getString", FuntionType()),
                Symbol("putStringLn", FuntionType())
            ]
        ])

    def visitProgram(self, ast: Program, c: List[List[Symbol]]):
        # First pass: collect all structs and interfaces
        for decl in ast.decl:
            if isinstance(decl, StructType) or isinstance(decl, InterfaceType):
                self.list_type.append(self.visit(decl, self.list_type))

        # Second pass: check method declarations for structs
        for decl in ast.decl:
            if isinstance(decl, MethodDecl):
                # Find the struct for this method
                struct = None
                if isinstance(decl.recType, Id):
                    struct = self.lookup(decl.recType.name, self.list_type, lambda x: x.name)
                    if struct is None:
                        raise Undeclared(Type(), decl.recType.name)

                    # Check if the method is already declared
                    method_name = decl.fun.name
                    for method in struct.methods:
                        if method.fun.name == method_name:
                            raise Redeclared(Method(), method_name)

                    # Add the method to the struct
                    struct.methods.append(decl)

        # Third pass: visit all other declarations
        for decl in ast.decl:
            if isinstance(decl, (VarDecl, ConstDecl, FuncDecl)):
                sym = self.visit(decl, c)
                if sym is not None:
                    c[0].insert(0, sym)
            elif isinstance(decl, MethodDecl):
                self.visit(decl, c)

        return c

    def visitStructType(self, ast: StructType, c: List[Union[StructType, InterfaceType]]) -> StructType:
        # Tìm kiếm xem type đã tồn lại trong c hay chưa
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)

        # Check for redeclared fields
        field_set = set()
        for field_name, _ in ast.elements:
            if field_name in field_set:
                raise Redeclared(Field(), field_name)
            field_set.add(field_name)

        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        # Check for redeclared prototype
        for proto in c:
            if proto.name == ast.name:
                # Check if params and return types are different
                raise Redeclared(Prototype(), ast.name)
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c: List[Union[StructType, InterfaceType]]) -> InterfaceType:
        # Check if interface name is already declared
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)

        # Check for redeclared prototypes
        proto_set = set()
        for proto in ast.methods:
            if proto.name in proto_set:
                raise Redeclared(Prototype(), proto.name)
            proto_set.add(proto.name)

        return ast

    def visitFuncDecl(self, ast: FuncDecl, c: List[List[Symbol]]) -> Symbol:
        # Tìm kiếm xem có biến nào đã được khai báo trong tầm vực hiện tại không c[0]
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        # không co thì lỗi
        if not res is None:
            raise Redeclared(Function(), ast.name)

        # Save current function context
        old_function = self.function_current
        self.function_current = ast

        # Create parameter scope
        param_symbols = []
        for param in ast.params:
            sym = self.visit(param, param_symbols)
            param_symbols.append(sym)

        # duyệt qua param và gọi block
        self.visit(ast.body, [param_symbols] + c)

        # Restore function context
        self.function_current = old_function

        return Symbol(ast.name, FuntionType())

    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        # Check for redeclared parameter in the same function signature
        res = self.lookup(ast.parName, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)

        return Symbol(ast.parName, ast.parType)

    def visitMethodDecl(self, ast: MethodDecl, c: List[List[Symbol]]) -> None:
        # First check if the receiver type exists
        if isinstance(ast.recType, Id):
            struct = self.lookup(ast.recType.name, self.list_type, lambda x: x.name)
            if struct is None:
                raise Undeclared(Type(), ast.recType.name)

        # Save current function context
        old_function = self.function_current
        self.function_current = ast.fun

        # Create a new scope with the receiver
        receiver_scope = [Symbol(ast.receiver, ast.recType, None)]

        # Create parameter scope
        param_symbols = []
        for param in ast.fun.params:
            sym = self.visit(param, param_symbols)
            param_symbols.append(sym)

        # Visit function body with new scope
        self.visit(ast.fun.body, [param_symbols + receiver_scope] + c)

        # Restore function context
        self.function_current = old_function

    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]) -> Symbol:
        # Tìm kiếm xem có biến nào đã được khai báo trong tầm vực hiện tại không c[0]
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        # không co thì lỗi
        if not res is None:
            raise Redeclared(Variable(), ast.varName)

        # If there's an initialization, check its type
        if ast.varInit is not None:
            init_type = self.visit(ast.varInit, c)
            if ast.varType is None:
                ast.varType = init_type
            elif not isinstance(ast.varType, type(init_type)):
                raise TypeMismatch(ast)

        # có thì trả về Symbol
        return Symbol(ast.varName, ast.varType, None)

    def visitConstDecl(self, ast: ConstDecl, c: List[List[Symbol]]) -> Symbol:
        # Check for redeclared constant
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Constant(), ast.conName)

        # Check initialization
        if ast.iniExpr is None:
            raise TypeMismatch(ast)

        # Check type
        init_type = self.visit(ast.iniExpr, c)
        if ast.conType is None:
            ast.conType = init_type
        elif not isinstance(ast.conType, type(init_type)):
            raise TypeMismatch(ast)

        return Symbol(ast.conName, ast.conType, ast.iniExpr)

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        # // tăng tầm vực lên
        reduce(
            lambda acc, ele: [
                ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
            ] + acc[1:],
            ast.member,
            [[]] + c
        )

    def visitForBasic(self, ast: ForBasic, c: List[List[Symbol]]) -> None:
        # Check condition
        cond_type = self.visit(ast.cond, c)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)

        # Visit loop body with a new scope
        self.visit(ast.loop, [[]] + c)
        return None

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
        # // chuyển init và upda vào trong block của for vì 2 này trong tầm vực block for
        self.visit(Block([ast.init] + ast.loop.member + [ast.upda]), c)

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None:
        # Get array type
        arr_type = self.visit(ast.arr, c)
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatch(ast)

        # Create new scope with index and value variables
        new_scope = [
            Symbol(ast.idx.name, IntType(), None),
            Symbol(ast.value.name, arr_type.eleType, None)
        ]

        # Visit loop body with new scope
        self.visit(ast.loop, [new_scope] + c)
        return None

    def visitReturn(self, ast, c):
        if ast.expr is not None:
            expr_type = self.visit(ast.expr, c)
            if self.function_current is not None:
                ret_type = self.function_current.retType
                if not isinstance(ret_type, type(expr_type)):
                    raise TypeMismatch(ast)
        return None

    # Expression visitor methods

    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        # Search all scopes for the identifier
        for scope in c:
            res = self.lookup(ast.name, scope, lambda x: x.name)
            if res is not None:
                return res.mtype

        # If not found, raise undeclared
        raise Undeclared(Identifier(), ast.name)

    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]) -> Type:
        left_type = self.visit(ast.left, c)
        right_type = self.visit(ast.right, c)

        if ast.op in ['+', '-', '*', '/', '%']:
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()
            elif (isinstance(left_type, IntType) or isinstance(left_type, FloatType)) and \
                 (isinstance(right_type, IntType) or isinstance(right_type, FloatType)):
                return FloatType()
            else:
                raise TypeMismatch(ast)

        elif ast.op in ['&&', '||']:
            if isinstance(left_type, BoolType) and isinstance(right_type, BoolType):
                return BoolType()
            else:
                raise TypeMismatch(ast)

        elif ast.op in ['==', '!=']:
            if (isinstance(left_type, IntType) and isinstance(right_type, IntType)) or \
               (isinstance(left_type, BoolType) and isinstance(right_type, BoolType)):
                return BoolType()
            else:
                raise TypeMismatch(ast)

        elif ast.op in ['<', '>', '<=', '>=']:
            if (isinstance(left_type, IntType) or isinstance(left_type, FloatType)) and \
               (isinstance(right_type, IntType) or isinstance(right_type, FloatType)):
                return BoolType()
            else:
                raise TypeMismatch(ast)

        else:  # String concatenation '+'
            if isinstance(left_type, StringType) and isinstance(right_type, StringType):
                return StringType()
            else:
                raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]) -> Type:
        expr_type = self.visit(ast.expr, c)

        if ast.op == '!':
            if isinstance(expr_type, BoolType):
                return BoolType()
            else:
                raise TypeMismatch(ast)

        elif ast.op == '-':
            if isinstance(expr_type, IntType):
                return IntType()
            elif isinstance(expr_type, FloatType):
                return FloatType()
            else:
                raise TypeMismatch(ast)

        else:
            raise TypeMismatch(ast)

    def visitFuncCall(self, ast: FuncCall, c: List[List[Symbol]]) -> Type:
        # Find the function in all scopes or builtin functions
        for func in self.list_function:
            if func.name == ast.funName:
                # Check param count
                if len(func.params) != len(ast.args):
                    raise TypeMismatch(ast)

                # Check param types
                for i, arg in enumerate(ast.args):
                    arg_type = self.visit(arg, c)
                    param_type = func.params[i].parType
                    if not isinstance(arg_type, type(param_type)):
                        raise TypeMismatch(ast)

                return func.retType

        # Check in the scope chain
        for scope in c:
            res = self.lookup(ast.funName, scope, lambda x: x.name)
            if res is not None and isinstance(res.mtype, FuntionType):
                # Should also check parameters but we don't have that info in Symbol
                return res.mtype

        # If not found, raise undeclared
        raise Undeclared(Function(), ast.funName)

    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]) -> Type:
        arr_type = self.visit(ast.arr, c)
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatch(ast)

        idx_type = self.visit(ast.idx, c)
        if not isinstance(idx_type, IntType):
            raise TypeMismatch(ast)

        return arr_type.eleType

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        # Get the object type
        obj_type = self.visit(ast.receiver, c)

        # Find the struct with this field
        for struct in self.list_type:
            if isinstance(struct, StructType) and struct.name == obj_type.name:
                # Search for the field in the struct
                for field_name, field_type in struct.elements:
                    if field_name == ast.field:
                        return field_type

                # Field not found in struct
                raise Undeclared(Field(), ast.field)

        # Not a struct or struct not found
        raise TypeMismatch(ast)

    def visitIntLiteral(self, ast: IntLiteral, c) -> Type:
        return IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, c) -> Type:
        return FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, c) -> Type:
        return BoolType()

    def visitStringLiteral(self, ast: StringLiteral, c) -> Type:
        return StringType()

    def visitArrayLiteral(self, ast: ArrayLiteral, c) -> Type:
        if not ast.value:
            return ArrayType(0, None)

        # Check that all elements have the same type
        ele_type = self.visit(ast.value[0], c)
        for i in range(1, len(ast.value)):
            this_type = self.visit(ast.value[i], c)
            if not isinstance(this_type, type(ele_type)):
                raise TypeMismatch(ast)

        return ArrayType(len(ast.value), ele_type)

    def visitMethCall(self, ast: MethCall, c: List[List[Symbol]]) -> Type:
        # Get the object type
        obj_type = self.visit(ast.receiver, c)

        # Find the struct with this method
        for struct in self.list_type:
            if isinstance(struct, StructType) and struct.name == obj_type.name:
                # Search for the method in the struct
                for method in struct.methods:
                    if method.fun.name == ast.metName:
                        # Check parameters if needed
                        return method.fun.retType

                # Method not found in struct
                raise Undeclared(Method(), ast.metName)

        # Not a struct or struct not found
        raise TypeMismatch(ast)

    def visitNilLiteral(self, ast, c) -> Type:
        return None  # NilLiteral has no type
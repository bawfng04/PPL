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
                FuncDecl("putInt", [ParamDecl("LU923", IntType())], VoidType(), Block([])),
                FuncDecl("putIntLn", [ParamDecl("LU923", IntType())], VoidType(), Block([])),
                FuncDecl("getFloat", [], FloatType(), Block([])),
                FuncDecl("putFloat", [ParamDecl("LU923", FloatType())], VoidType(), Block([])),
                FuncDecl("putFloatLn", [ParamDecl("LU923", FloatType())], VoidType(), Block([])),
                FuncDecl("getString", [], IntType(), Block([])),
                FuncDecl("putString", [ParamDecl("LU923", IntType())], VoidType(), Block([])),
                FuncDecl("putStringLn", [ParamDecl("LU923", StringType())], VoidType(), Block([])),
                FuncDecl("getBool", [], BoolType(), Block([])),
                FuncDecl("putBool", [ParamDecl("LU923", BoolType())], VoidType(), Block([])),
                FuncDecl("putBoolLn", [ParamDecl("LU923", BoolType())], VoidType(), Block([])),
                FuncDecl("putLn", [], VoidType(), Block([])),
            ]
        self.function_current: FuncDecl = None

    def check(self):
        self.visit(self.ast, None)

    def checkType(
        self,
        Bailu_type: Type,
        lulu_type: Type,
        list_type_permission: List[Tuple[Type, Type]] = [],
    ) -> bool:
        if isinstance(lulu_type, NilLiteral):
            # Nil can be assigned to interface or struct types
            return isinstance(Bailu_type, (StructType, InterfaceType)) or (
                isinstance(Bailu_type, Id) and
                self.lookup(Bailu_type.name, self.list_type, lambda x: x.name) is not None
            )
        if type(lulu_type) == StructType and lulu_type.name == "":
            return isinstance(Bailu_type, StructType)

        Bailu_type = (
            self.lookup(Bailu_type.name, self.list_type, lambda x: x.name)
            if isinstance(Bailu_type, Id)
            else Bailu_type
        )
        lulu_type = (
            self.lookup(lulu_type.name, self.list_type, lambda x: x.name)
            if isinstance(lulu_type, Id)
            else lulu_type
        )

        if (type(Bailu_type), type(lulu_type)) in list_type_permission:
            # Interface-struct compatibility check
            if isinstance(Bailu_type, InterfaceType) and isinstance(lulu_type, StructType):
                # Check if struct implements all interface methods
                for inter_method in Bailu_type.methods:
                    struct_method = self.lookup(
                        inter_method.name, lulu_type.methods, lambda x: x.fun.name
                    )
                    if struct_method is None:
                        return False

                    # Compare return types
                    inter_return = inter_method.retType
                    struct_return = struct_method.fun.retType

                    # Resolve Id types if needed
                    if isinstance(inter_return, Id):
                        inter_return = (
                            self.lookup(inter_return.name, self.list_type, lambda x: x.name)
                            or inter_return
                        )
                    if isinstance(struct_return, Id):
                        struct_return = (
                            self.lookup(
                                struct_return.name, self.list_type, lambda x: x.name
                            )
                            or struct_return
                        )

                    # Compare types directly without allowing conversions
                    if not self.checkType(inter_return, struct_return, []):
                        return False

                    # Check method parameters match
                    if len(inter_method.params) != len(struct_method.fun.params):
                        return False

                    for i, inter_param in enumerate(inter_method.params):
                        struct_param = struct_method.fun.params[i].parType
                        if not self.checkType(inter_param, struct_param, []):
                            return False

                return True
            return True

        if isinstance(Bailu_type, (StructType, InterfaceType)) and isinstance(
            lulu_type, (StructType, InterfaceType)
        ):
            return Bailu_type.name == lulu_type.name

        if isinstance(Bailu_type, ArrayType) and isinstance(lulu_type, ArrayType):
            if len(Bailu_type.dimens) != len(lulu_type.dimens):
                return False

            return self.checkType(Bailu_type.eleType, lulu_type.eleType, [(FloatType, IntType)])

        return type(Bailu_type) == type(lulu_type)

    def visitProgram(self, ast: Program,c : None):

        def visitMethodDecl(ast: MethodDecl, c: StructType) -> MethodDecl:
            if not c:
                raise Undeclared(Type(), ast.recType.name)
            for meth in c.methods:
                if meth.fun.name == ast.fun.name and isinstance(c, StructType) and c.name == ast.recType.name:
                    raise Redeclared(Method(), ast.fun.name)

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
                Symbol("getFloat", FuntionType()),
                Symbol("putFloat", FuntionType()),
                Symbol("putFloatLn", FuntionType()),
                Symbol("getString", FuntionType()),
                Symbol("putString", FuntionType()),
                Symbol("putStringLn", FuntionType()),
                Symbol("getBool", FuntionType()),
                Symbol("putBool", FuntionType()),
                Symbol("putBoolLn", FuntionType()),
                Symbol("putLn", FuntionType()),
            ]]
        )

    def visitStructType(self, ast: StructType, c : List[Union[StructType, InterfaceType]]) -> StructType:
        fres = self.lookup(ast.name, self.list_function, lambda x: x.name)
        if fres is not None:
            raise Redeclared(StaticErrorType(), ast.name)

        sres = self.lookup(ast.name, c, lambda x: x.name)
        if not sres is None:
            raise Redeclared(StaticErrorType(), ast.name)

        for dec in self.ast.decl:
            if isinstance(dec, VarDecl) and dec.varName == ast.name:
                raise Redeclared(StaticErrorType(), ast.name)
            elif isinstance(dec, ConstDecl) and dec.conName == ast.name:
                raise Redeclared(StaticErrorType(), ast.name)

        def visitElements(element: Tuple[str,Type], c: List[Tuple[str,Type]]) -> Tuple[str,Type]:
            if self.lookup(element[0], c, lambda x: x[0]):
                raise Redeclared(Field(), element[0])
            return element

        ast.elements = reduce(lambda acc,ele: [visitElements(ele,acc)] + acc , ast.elements , [])
        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        for prototype in c:
            if prototype.name == ast.name:
                raise Redeclared(Prototype(), ast.name)
        return ast

    def visitInterfaceType(
        self, ast: InterfaceType, c: List[Union[StructType, InterfaceType]]
    ) -> InterfaceType:
        fres = self.lookup(ast.name, self.list_function, lambda x: x.name)
        if fres is not None:
            raise Redeclared(StaticErrorType(), ast.name)

        sres = self.lookup(ast.name, c, lambda x: x.name)
        if not sres is None:
            raise Redeclared(StaticErrorType(), ast.name)

        # Add this check for variable and constant declarations
        for dec in self.ast.decl:
            if isinstance(dec, VarDecl) and dec.varName == ast.name:
                raise Redeclared(StaticErrorType(), ast.name)
            elif isinstance(dec, ConstDecl) and dec.conName == ast.name:
                raise Redeclared(StaticErrorType(), ast.name)
            elif dec == ast:
                break

        ast.methods = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.methods, [])
        return ast

    def visitFuncDecl(self, ast: FuncDecl, c : List[List[Symbol]]) -> Symbol:
        fres = self.lookup(ast.name, c[0], lambda x: x.name)
        if not fres is None:
            raise Redeclared(Function(), ast.name)

        self.function_current = ast
        self.visit(ast.body, [list(reduce(lambda acc,ele: [self.visit(ele,acc)] + acc, ast.params, []))] + c)
        self.function_current = None
        return Symbol(ast.name, FuntionType())

    # def visitParamDecl(self, ast: ParamDecl, c: List[Symbol]) -> Symbol:
    #     if self.lookup(ast.parName, c, lambda x: x.name):
    #         raise Redeclared(Parameter(), ast.parName)
    #     return Symbol(ast.parName, ast.parType, None)

    # def visitMethodDecl(self, ast: MethodDecl, c : List[List[Symbol]]) -> None:
    #     if isinstance(ast.recType, Id):
    #         ctr = self.lookup(ast.recType.name, self.list_type, lambda x: x.name)
    #         if ctr is None:
    #             raise Undeclared(Type(), ast.recType.name)

    #     o_func = self.function_current
    #     self.function_current = ast.fun
    #     # Create parameter scope with the receiver
    #     symbol_rev = Symbol(ast.receiver, ast.recType, None)
    #     symbol_param = [symbol_rev]

    #     for par in ast.fun.params:
    #         if par.parName == ast.receiver:
    #             raise Redeclared(Parameter(), ast.receiver)

    #         bt = self.visit(par, symbol_param)
    #         symbol_param.append(bt)

    #     self.visit(ast.fun.body, [symbol_param] + c)
    #     self.function_current = o_func
    # Inside StaticChecker class in StaticCheck.py

    def visitMethodDecl(self, ast: MethodDecl, c: List[List[Symbol]]) -> None:
        # Resolve the receiver type
        rec_type_node = ast.recType
        resolved_rec_type = (
            self.lookup(rec_type_node.name, self.list_type, lambda x: x.name)
            if isinstance(rec_type_node, Id)
            else rec_type_node
        )
        if isinstance(rec_type_node, Id) and resolved_rec_type is None:
            raise Undeclared(Type(), rec_type_node.name)

        # Check field–method conflict only if the field is exported (first letter uppercase)
        if isinstance(resolved_rec_type, StructType):
            for field_name, _ in resolved_rec_type.elements:
                if field_name == ast.fun.name and field_name[0].isupper():
                    raise Redeclared(Method(), ast.fun.name)

        # Store current function context and set the new one
        o_func = self.function_current
        self.function_current = ast.fun

        # Process parameters
        param_symbols = []
        for par in ast.fun.params:
            param_symbol = self.visit(par, param_symbols)
            param_symbols.append(param_symbol)

        # Create receiver symbol
        receiver_symbol = Symbol(ast.receiver, resolved_rec_type, None)

        # Parameters should come FIRST in the scope
        inner_scope = param_symbols + [receiver_symbol]

        # Visit method body with the correct scope ordering
        self.visit(ast.fun.body, [inner_scope] + c)

        # Restore original function context
        self.function_current = o_func

    # Ensure visitParamDecl uses the passed list correctly for checking duplicates
    def visitParamDecl(self, ast: ParamDecl, c: List[Symbol]) -> Symbol:
        # c is the list of parameters processed *so far* in the current declaration
        if self.lookup(ast.parName, c, lambda x: x.name):
            raise Redeclared(Parameter(), ast.parName)

        # Resolve parameter type if it's an Id
        param_type = self.lookup(ast.parType.name, self.list_type, lambda x: x.name) if isinstance(ast.parType, Id) else ast.parType
        if isinstance(ast.parType, Id) and param_type is None:
            raise Undeclared(Type(), ast.parType.name)
        # You might want to add a check here if param_type resolved to VoidType, which is usually invalid for parameters

        return Symbol(ast.parName, param_type, None) # Use the resolved type

    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]) -> Symbol:
        # First check if the variable name conflicts with any type name
        tres = self.lookup(ast.varName, self.list_type, lambda x: x.name)
        if tres is not None:
            # Check if the conflict is with a type declared *before* this VarDecl
            # This logic might need refinement based on exact scoping rules
            is_predeclared_type = False
            for dec in self.ast.decl:
                if dec == ast:  # Stop checking once we reach the current VarDecl
                    break
                if (
                    isinstance(dec, (StructType, InterfaceType))
                    and dec.name == ast.varName
                ):
                    is_predeclared_type = True
                    break
            if is_predeclared_type:
                raise Redeclared(Variable(), ast.varName)
            # If it's a type declared later, it might be okay depending on rules,
            # but raising Redeclared is safer for now.
            # Consider if MiniGo allows forward declaration implicitly.
            # raise Redeclared(Variable(), ast.varName) # Keep this if forward decl not allowed

        # Then check for conflicts in the current scope
        vres = self.lookup(ast.varName, c[0], lambda x: x.name)
        if vres is not None:
            raise Redeclared(Variable(), ast.varName)

        Bailu_type = ast.varType if ast.varType else None
        lulu_type = None
        if ast.varInit:
            # Pass context (c, True) if initializer is a function/method call
            if isinstance(ast.varInit, (FuncCall, MethCall)):
                lulu_type = self.visit(
                    ast.varInit, (c, True)
                )  # Pass True for expression context
            else:
                # For other initializers, visit normally (context depends on the expression itself)
                # If the initializer contains function calls, *those* visits need the context.
                # A more robust approach might involve passing the context down recursively.
                # For now, let's assume non-call initializers are handled correctly by their respective visitors.
                lulu_type = self.visit(ast.varInit, c)  # Pass original context

        # Resolve Bailu_type if it's an Id *before* using it
        resolved_bailu_type = None
        if isinstance(Bailu_type, Id):
            resolved_bailu_type = self.lookup(
                Bailu_type.name, self.list_type, lambda x: x.name
            )
            if resolved_bailu_type is None:
                raise Undeclared(Type(), Bailu_type.name)
            Bailu_type = resolved_bailu_type  # Use the resolved type

        if lulu_type is None:
            # Type is explicit, no initializer
            return Symbol(ast.varName, Bailu_type, None)

        elif Bailu_type is None:  # Type inference from initializer
            # Check if initializer itself resulted in VoidType (should be caught by visitFuncCall now)
            if isinstance(lulu_type, VoidType):
                raise TypeMismatch(ast)  # Cannot infer type from void expression result
            return Symbol(ast.varName, lulu_type, None)
        else:  # Both type and initializer exist
            # We already resolved Bailu_type if it was an Id
            if self.checkType(
                Bailu_type,
                lulu_type,
                [(FloatType, IntType), (InterfaceType, StructType)],
            ):
                return Symbol(ast.varName, Bailu_type, None)

        # If checkType failed
        raise TypeMismatch(ast)

    def visitConstDecl(self, ast: ConstDecl, c : List[List[Symbol]]) -> Symbol:
        tres = self.lookup(ast.conName, self.list_type, lambda x: x.name)
        if tres is not None:
            for dec in self.ast.decl:
                if isinstance(dec, (StructType, InterfaceType)) and dec.name == ast.conName:
                    raise Redeclared(Constant(), ast.conName)
                elif dec == ast:
                    break
            raise Redeclared(Constant(), ast.conName)

        cres = self.lookup(ast.conName, c[0], lambda x: x.name)
        if cres is not None:
            raise Redeclared(Constant(), ast.conName)

        Bailu_type = ast.conType if ast.conType else None
        lulu_type = self.visit(ast.iniExpr, c) if ast.iniExpr else None

        if lulu_type is None:
            raise TypeMismatch(ast)
        elif Bailu_type is None:
            return Symbol(ast.conName, lulu_type, ast.iniExpr)
        elif self.checkType(Bailu_type, lulu_type, [(FloatType, IntType), (InterfaceType, StructType)]):
            return Symbol(ast.conName, Bailu_type, ast.iniExpr)
        raise TypeMismatch(ast)

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        scope_moi = [[]] + c
        for ele in ast.member:
            rst = self.visit(ele, scope_moi)
            if isinstance(rst, Symbol):
                scope_moi[0] = [rst] + scope_moi[0]

    def visitForBasic(self, ast: ForBasic, c : List[List[Symbol]]) -> None:
        type_condition = self.visit(ast.cond, c)
        if not isinstance(type_condition, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
        scopes = [[]] + c
        if isinstance(ast.init, VarDecl):
            sym_new = self.visit(ast.init, scopes)
            if isinstance(sym_new, Symbol):
                scopes[0] = [sym_new] + scopes[0]
        else:
            self.visit(ast.init, scopes)

        type_condition = self.visit(ast.cond, scopes)

        if not isinstance(type_condition, BoolType):
            raise TypeMismatch(ast)

        self.visit(ast.upda, scopes)

        # Now process the loop body
        if isinstance(ast.loop, Block):
            for mtst in ast.loop.member:
                kq = self.visit(mtst, scopes)
                if isinstance(kq, Symbol):
                    scopes[0] = [kq] + scopes[0]
        else:
            if isinstance(self.visit(ast.loop, scopes), Symbol):
                scopes[0] = [self.visit(ast.loop, scopes)] + scopes[0]

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None:
        mang = self.visit(ast.arr, c)
        if not isinstance(mang, ArrayType):
            raise TypeMismatch(ast)

        mang_idx = self.visit(ast.idx, c)
        if not isinstance(mang_idx, IntType):
            raise TypeMismatch(ast)

        type_value = self.visit(ast.value, c)
        if not self.checkType(type_value, mang.eleType ):
            raise TypeMismatch(ast)

        self.visit(Block(ast.loop.member), c)

    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        res_id = next(filter(None, (self.lookup(ast.name, scope, lambda x: x.name) for scope in c)), None)
        if res_id and not isinstance(res_id.mtype, Function):
            return res_id.mtype
        raise Undeclared(Identifier(), ast.name)

    # def visitFuncCall(self, ast: FuncCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
    #     stmt_right = False
    #     if isinstance(c, tuple):
    #         c, stmt_right = c
    #     for scope in c:
    #         local_symbol = self.lookup(ast.funName, scope, lambda x: x.name)
    #         if local_symbol is not None:
    #             raise Undeclared(Function(), ast.funName)

    #     res_call = self.lookup(ast.funName, self.list_function, lambda x: x.name)

    #     if res_call:
    #         if len(res_call.params) != len(ast.args):
    #             raise TypeMismatch(ast)
    #         for par, (par, argg) in enumerate(zip(res_call.params, ast.args)):
    #             if isinstance(argg, NilLiteral):
    #                 # Check if parameter type is an interface or struct (reference type)
    #                 type_par = self.lookup(par.parType.name, self.list_type, lambda x: x.name) if isinstance(par.parType, Id) else par.parType
    #                 if not (isinstance(type_par, (StructType, InterfaceType))):
    #                     raise TypeMismatch(ast)
    #                 continue

    #             argType = self.visit(argg, c)

    #             if isinstance(par.parType, Id) and isinstance(argg, Id):
    #                 type_par = self.lookup(par.parType.name, self.list_type, lambda x: x.name)
    #                 if type_par and isinstance(type_par, InterfaceType):
    #                     if argType and isinstance(argType, StructType):
    #                         raise TypeMismatch(ast)

    #             if isinstance(par.parType, ArrayType) and isinstance(argType, ArrayType):
    #                 if len(par.parType.dimens) != len(argType.dimens):
    #                     raise TypeMismatch(ast)
    #                 for i in range(len(par.parType.dimens)):
    #                     if isinstance(par.parType.dimens[i], IntLiteral) and isinstance(argType.dimens[i], IntLiteral):
    #                         if par.parType.dimens[i].value != argType.dimens[i].value:
    #                             raise TypeMismatch(ast)

    #             if not self.checkType(par.parType, argType, []):
    #                 raise TypeMismatch(ast)

    #         if stmt_right and isinstance(res_call.retType, VoidType):
    #             raise TypeMismatch(ast)
    #         if not stmt_right and isinstance(res_call.retType, VoidType):
    #             raise TypeMismatch(ast)
    #         return res_call.retType

    #     raise Undeclared(Function(), ast.funName)

    def visitFuncCall(
        self, ast: FuncCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]
    ) -> Type:
        stmt_right = False
        if isinstance(c, tuple):
            c, stmt_right = c

        for scope in c:
            var = self.lookup(ast.funName, scope, lambda x: x.name)
            if var is not None and not isinstance(var.mtype, FuntionType):
                raise Undeclared(Function(), ast.funName)

        res_call = self.lookup(ast.funName, self.list_function, lambda x: x.name)

        if res_call is None:
            raise Undeclared(Function(), ast.funName)

        if len(res_call.params) != len(ast.args):
            raise TypeMismatch(ast)

        for par, arg in zip(res_call.params, ast.args):
            if isinstance(arg, NilLiteral):
                par_type = (
                    self.lookup(par.parType.name, self.list_type, lambda x: x.name)
                    if isinstance(par.parType, Id)
                    else par.parType
                )
                if not isinstance(par_type, (StructType, InterfaceType)):
                    raise TypeMismatch(ast)
                continue

            arg_type = self.visit(arg, c)

            if isinstance(par.parType, ArrayType) and isinstance(arg_type, ArrayType):
                # Check dimensions
                if len(par.parType.dimens) != len(arg_type.dimens):
                    raise TypeMismatch(ast)

                for i in range(len(par.parType.dimens)):
                    if isinstance(par.parType.dimens[i], IntLiteral) and isinstance(
                        arg_type.dimens[i], IntLiteral
                    ):
                        if par.parType.dimens[i].value != arg_type.dimens[i].value:
                            raise TypeMismatch(ast)

                if type(par.parType.eleType) != type(arg_type.eleType):
                    raise TypeMismatch(ast)

            # Regular type check
            if not self.checkType(par.parType, arg_type, []):
                raise TypeMismatch(ast)

        if stmt_right and isinstance(res_call.retType, VoidType):
            raise TypeMismatch(ast)

        return res_call.retType

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        type_ren = self.visit(ast.receiver, c)
        type_ren = self.lookup(type_ren.name, self.list_type, lambda x: x.name) if isinstance(type_ren, Id) else type_ren

        if not isinstance(type_ren, StructType):
            raise TypeMismatch(ast)

        Fieldres = self.lookup(ast.field, type_ren.elements, lambda x: x[0])
        if Fieldres is None:
            raise Undeclared(Field(), ast.field)
        return Fieldres[1]

    def visitMethCall(self, ast: MethCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        stmt_right = False
        if isinstance(c, tuple):
            c, stmt_right = c
        type_ren = self.visit(ast.receiver, c)
        type_ren = self.lookup(type_ren.name, self.list_type, lambda x: x.name) if isinstance(type_ren, Id) else type_ren
        if not isinstance(type_ren, (StructType, InterfaceType)):
            raise TypeMismatch(ast)

        resMeth = self.lookup(ast.metName, type_ren.methods, lambda x: x.fun.name) if isinstance(type_ren, StructType) else self.lookup(ast.metName, type_ren.methods, lambda x: x.name)

        if resMeth:
            if type(type_ren) == StructType:
                if len(resMeth.fun.params) != len(ast.args):
                    raise TypeMismatch(ast)
                for bien, argg in zip(resMeth.fun.params, ast.args):
                    argg_type = self.visit(argg, c)
                    if not self.checkType(bien.parType, argg_type, [(FloatType, IntType)]):
                        raise TypeMismatch(ast)
                if stmt_right and not isinstance(resMeth.fun.retType, VoidType):
                    raise TypeMismatch(ast)
                if not stmt_right and not isinstance(resMeth.fun.retType, VoidType):
                    raise TypeMismatch(ast)
                return resMeth.fun.retType
            if type(type_ren) == InterfaceType:
                if len(resMeth.params) != len(ast.args):
                    raise TypeMismatch(ast)

                for bien, argg in zip(resMeth.params, ast.args):
                    if not self.checkType(bien.parType, self.visit(argg,c), [(FloatType, IntType)]):
                        raise TypeMismatch(ast)

                if stmt_right and  isinstance(resMeth.retType, VoidType) == False:
                    raise TypeMismatch(ast)
                if not stmt_right and isinstance(resMeth.retType, VoidType):
                    raise TypeMismatch(ast)
                return resMeth.retType
        raise Undeclared(Method(), ast.metName)

    def visitIntType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitFloatType(self, ast, c: List[List[Symbol]])-> Type: return ast
    def visitBoolType(self, ast, c: List[List[Symbol]])-> Type: return ast
    def visitStringType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitVoidType(self, ast, c: List[List[Symbol]]) -> Type: return ast

    def visitArrayType(self, ast: ArrayType, c: List[List[Symbol]]):
        list(map(lambda item: IntType() if not isinstance(self.visit(item, c), IntType()) else item, ast.dimens))
        return ast

    def visitAssign(self, ast: Assign, c: List[List[Symbol]]) -> None:
        try:
            lhs_type = self.visit(ast.lhs, c)
            rhs_type = self.visit(ast.rhs, c)

            # Only allow int->float conversion (widening), not float->int (narrowing)
            # Remove (IntType, FloatType) from the list of permitted conversions
            if not self.checkType(lhs_type, rhs_type, [(FloatType, IntType)]):
                raise TypeMismatch(ast)
        except Undeclared:
            # If the left-hand side is an undeclared Id, treat it as an implicit declaration
            if isinstance(ast.lhs, Id):
                lulu_type = self.visit(ast.rhs, c)
                # Add the new symbol to the innermost scope
                c[0].insert(0, Symbol(ast.lhs.name, lulu_type, None))
            else:
                # For other expressions (array access, etc.), propagate the error
                raise

    def visitIf(self, ast: If, c: List[List[Symbol]]) -> None:
        condition_type = self.visit(ast.expr, c)
        if not isinstance(condition_type, BoolType):
            raise TypeMismatch(ast)
        self.visit(Block(ast.thenStmt.member), c)
        if ast.elseStmt:
            if isinstance(ast.elseStmt, Block):
                self.visit(Block(ast.elseStmt.member), c)
            else:
                self.visit(ast.elseStmt, c)

    def visitContinue(self, ast, c: List[List[Symbol]]) -> None: return None
    def visitBreak(self, ast, c: List[List[Symbol]]) -> None: return None

    def visitReturn(self, ast, c: List[List[Symbol]]) -> None:
        if ast.expr is None:
            if not isinstance(self.function_current.retType, VoidType):
                raise TypeMismatch(ast)
            return None

        # Set stmt_right to True for function calls in return statements
        if isinstance(ast.expr, (FuncCall, MethCall)):
            return_type = self.visit(ast.expr, (c, True))
        else:
            return_type = self.visit(ast.expr, c)

        if isinstance(ast.expr, NilLiteral) and isinstance(
            self.function_current.retType, (StructType, Id)
        ):
            return None

        if not self.checkType(self.function_current.retType, return_type, []):
            raise TypeMismatch(ast)

        return None

    # def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]):
    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]):
        Bailu_type = self.visit(ast.left, c)
        lulu_type = self.visit(ast.right, c)
        op = ast.op

        # Modulo: only integer operands
        if op == '%':
            if isinstance(Bailu_type, IntType) and isinstance(lulu_type, IntType):
                return IntType()
            raise TypeMismatch(ast)

        # Logical operators: only boolean operands
        if op in ['&&', '||']:
            if isinstance(Bailu_type, BoolType) and isinstance(lulu_type, BoolType):
                return BoolType()
            raise TypeMismatch(ast)

        # Equality operators
        if op in ['==', '!=']:
            if not self.checkType(Bailu_type, lulu_type):
                raise TypeMismatch(ast)
            if isinstance(Bailu_type, (IntType, FloatType, BoolType, StringType)):
                return BoolType()
            raise TypeMismatch(ast)

        # Relational operators
        if op in ['<', '>', '<=', '>=']:
            if not self.checkType(Bailu_type, lulu_type):
                raise TypeMismatch(ast)
            if isinstance(Bailu_type, (IntType, FloatType, StringType)):
                return BoolType()
            raise TypeMismatch(ast)

        # Arithmetic operators
        if op in ['+', '-', '*', '/']:
            if self.checkType(Bailu_type, lulu_type, [(IntType, FloatType), (FloatType, IntType)]):
                if op == '+' and isinstance(Bailu_type, StringType) and isinstance(lulu_type, StringType):
                    return StringType()
                if isinstance(Bailu_type, FloatType) or isinstance(lulu_type, FloatType):
                    return FloatType()
                return IntType()
            raise TypeMismatch(ast)

        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]):
        type_una = self.visit(ast.body, c)
        if ast.op == '-':
            if isinstance(type_una, IntType):
                return IntType()
            if isinstance(type_una, FloatType):
                return FloatType()
        if ast.op == '!':
            if isinstance(type_una, BoolType):
                return BoolType()
        raise TypeMismatch(ast)

    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]):
        mang_type = self.visit(ast.arr, c)
        if not isinstance(mang_type, ArrayType):
            raise TypeMismatch(ast)
        if not all(isinstance(self.visit(item, c), IntType) for item in ast.idx):
            raise TypeMismatch(ast)

        if len(mang_type.dimens) == len(ast.idx):
            return mang_type.eleType
        elif len(mang_type.dimens) > len(ast.idx):
            remaining_dims = mang_type.dimens[len(ast.idx) :]
            return ArrayType(remaining_dims, mang_type.eleType)
        raise TypeMismatch(ast)

    def visitIntLiteral(self, ast, c: List[List[Symbol]]) -> Type: return IntType()

    def visitFloatLiteral(self, ast, c: List[List[Symbol]]) -> Type: return FloatType()

    def visitBooleanLiteral(self, ast, c: List[List[Symbol]]) -> Type: return BoolType()

    def visitStringLiteral(self, ast, c: List[List[Symbol]]) -> Type: return StringType()

    def visitArrayLiteral(self, ast:ArrayLiteral , c: List[List[Symbol]]) -> Type:
        def dequy2(dat: Union[Literal, list['NestedList']], c: List[List[Symbol]]):
            if isinstance(dat,list):
                list(map(lambda value: dequy2(value, c), dat))
            else:
                self.visit(dat, c)
        dequy2(ast.value, c)
        return ArrayType(ast.dimens, ast.eleType)

    def visitStructLiteral(self, ast:StructLiteral, c: List[List[Symbol]]) -> Type:
        list(map(lambda value: self.visit(value[1], c), ast.elements))
        return self.lookup(ast.name, self.list_type, lambda x: x.name)

    def visitNilLiteral(self, ast:NilLiteral, c: List[List[Symbol]]) -> Type:
        return NilLiteral()

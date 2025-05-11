from Utils import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *

# 11/05/2025
# 2210298

class CodeGenerator(BaseVisitor, Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.function = None
        self.list_function = []
        self.arrayCell = None
        self.arrayCellType = None
        self.struct: StructType = None
        self.list_type = {}

    def init(self):
        initial_symbols = [
            Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("getInt", MType([], IntType()), CName("io", True)),
            Symbol("getFloat", MType([], FloatType()), CName("io", True)),
            Symbol("getBool", MType([], BoolType()), CName("io", True)),
            Symbol("getString", MType([], StringType()), CName("io", True)),
        ]
        return initial_symbols

    def gen(self, ast_tree_node, output_directory):
        global_scope_symbols = self.init()
        self.astTree = ast_tree_node
        self.path = output_directory
        self.emit = Emitter(output_directory + "/" + self.className + ".j")
        self.visit(ast_tree_node, global_scope_symbols)

    def emitObjectInit(self):
        constructor_frame = Frame("<init>", VoidType())
        self.emit.printout(
            self.emit.emitMETHOD(
                "<init>", MType([], VoidType()), False, constructor_frame
            )
        )
        constructor_frame.enterScope(True)

        this_var_index = constructor_frame.getNewIndex()
        this_var_name = "this"
        this_var_type = Id(self.className)
        start_label = constructor_frame.getStartLabel()
        end_label = constructor_frame.getEndLabel()

        self.emit.printout(
            self.emit.emitVAR(
                this_var_index,
                this_var_name,
                this_var_type,
                start_label,
                end_label,
                constructor_frame,
            )
        )
        self.emit.printout(self.emit.emitLABEL(start_label, constructor_frame))
        self.emit.printout(
            self.emit.emitREADVAR(
                this_var_name, this_var_type, this_var_index, constructor_frame
            )
        )
        self.emit.printout(self.emit.emitINVOKESPECIAL(constructor_frame))
        self.emit.printout(self.emit.emitLABEL(end_label, constructor_frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), constructor_frame))
        self.emit.printout(self.emit.emitENDMETHOD(constructor_frame))
        constructor_frame.exitScope()

    def emitObjectCInit(self, ast: Program, env):
        frame = Frame("<clinit>", VoidType())
        self.emit.printout(
            self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame)
        )
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env["frame"] = frame

        assigns = [
            Assign(Id(item.varName), item.varInit)
            for item in ast.decl
            if isinstance(item, VarDecl) and item.varInit is not None
        ] + [
            Assign(Id(item.conName), item.iniExpr)
            for item in ast.decl
            if isinstance(item, ConstDecl) and item.iniExpr is not None
        ]

        self.visit(Block(assigns), env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitProgram(self, ast: Program, c):
        for decl in ast.decl:
            if isinstance(decl, StructType):
                self.list_type[decl.name] = decl
            elif isinstance(decl, InterfaceType):
                self.list_type[decl.name] = decl

        for decl in ast.decl:
            if isinstance(decl, MethodDecl) and decl.receiver:
                receiver_type_name = decl.receiver.parType.name
                if receiver_type_name in self.list_type:
                    struct_type = self.list_type[receiver_type_name]
                    if isinstance(struct_type, StructType):
                        struct_type.methods.append(decl)

        self.list_function = c + [Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)), item.retType), CName(self.className)) for item in ast.decl if isinstance(item, FuncDecl)]
        env = {}
        env['env'] = [c]

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        env = reduce(lambda a, x: self.visit(x, a) if isinstance(x, VarDecl) or  isinstance(x, ConstDecl) else a, ast.decl, env)
        g = env['env'][0]
        env['env'] = [[]]
        for decl in ast.decl:
            if isinstance(decl, (VarDecl)):
                var_sym = next((sym for sym in g if sym.name == decl.varName), None)
                if var_sym:
                    env['env'][0].append(var_sym)

            if isinstance(decl, (ConstDecl)):
                const_sym = next((sym for sym in g if sym.name == decl.conName), None)
                if const_sym:
                    env['env'][0].append(const_sym)

            if isinstance(decl, FuncDecl):
                self.visit(decl, env)

        self.emitObjectInit()
        self.emitObjectCInit(ast, env)

        self.emit.printout(self.emit.emitEPILOG())

        for item in self.list_type.values():
            self.struct = item
            self.emit = Emitter(self.path + "/" + item.name + ".j")
            self.visit(item, {
                'env': env['env']
            })

        return env

    def visitFuncDecl(self, ast: FuncCall, o: dict) -> dict:
        self.function = ast
        current_frame = Frame(ast.name, ast.retType)
        is_main = ast.name == "main"

        if not is_main:
            parameter_types = [param.parType for param in ast.params]
            method_type = MType(parameter_types, ast.retType)
        else:
            method_type = MType([ArrayType([None], StringType())], VoidType())

        env_for_method = o.copy()
        env_for_method["frame"] = current_frame
        self.emit.printout(
            self.emit.emitMETHOD(ast.name, method_type, True, current_frame)
        )

        current_frame.enterScope(True)
        self.emit.printout(
            self.emit.emitLABEL(current_frame.getStartLabel(), current_frame)
        )
        env_for_method["env"] = [[]] + env_for_method["env"]

        if is_main:
            self.emit.printout(
                self.emit.emitVAR(
                    current_frame.getNewIndex(),
                    "args",
                    ArrayType([None], StringType()),
                    current_frame.getStartLabel(),
                    current_frame.getEndLabel(),
                    current_frame,
                )
            )
        else:
            updated_env = env_for_method
            for param_declaration in ast.params:
                updated_env = self.visit(param_declaration, updated_env)
            env_for_method = updated_env

        self.visit(ast.body, env_for_method)
        self.emit.printout(
            self.emit.emitLABEL(current_frame.getEndLabel(), current_frame)
        )

        if isinstance(ast.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), current_frame))

        self.emit.printout(self.emit.emitENDMETHOD(current_frame))
        current_frame.exitScope()
        return o

    def visitParamDecl(self, ast: ParamDecl, o: dict) -> dict:
        current_frame = o['frame']
        new_index = current_frame.getNewIndex()

        param_symbol = Symbol(ast.parName, ast.parType, Index(new_index))
        o['env'][0].append(param_symbol)

        var_code = self.emit.emitVAR(new_index, ast.parName, ast.parType, current_frame.getStartLabel(), current_frame.getEndLabel(), current_frame)
        self.emit.printout(var_code)

        return o

    def visitVarDecl(self, ast: VarDecl, o: dict) -> dict:
        def create_init(varType: Type, o_local: dict):
            if isinstance(varType, IntType):
                return IntLiteral(0)
            if isinstance(varType, FloatType):
                return FloatLiteral(0.0)
            if isinstance(varType, StringType):
                return StringLiteral('""')
            if isinstance(varType, BoolType):
                return BooleanLiteral(False)
            if isinstance(varType, ArrayType):
                dim_are_literals = True
                for dim_item in varType.dimens:
                    if not isinstance(dim_item, IntLiteral):
                        dim_are_literals = False
                        break

                if dim_are_literals:
                    def create_default_array(dimens, eleType):
                        if not dimens:
                            return create_init(eleType, o_local)

                        current_dim_size = dimens[0].value
                        arr = []
                        idx = 0
                        while idx < current_dim_size:
                            arr.append(create_default_array(dimens[1:], eleType))
                            idx += 1
                        return arr

                    default_values = create_default_array(
                        varType.dimens, varType.eleType
                    )
                    return ArrayLiteral(default_values, varType.eleType, varType.dimens)

                return None

            if isinstance(varType, StructType):
                struct_name = varType.name
                structs_map = o_local.get("structs", {})
                struct_def = structs_map.get(struct_name)

                if struct_def is None:
                    return None

                default_fields_list = []
                for field_name_item, field_type_item in struct_def.elements:
                    default_fields_list.append( (field_name_item, create_init(field_type_item, o_local)) )

                return StructLiteral(struct_name, default_fields_list)
            return None

        current_var_init = ast.varInit
        current_var_type = ast.varType

        if current_var_init is None:
            if isinstance(current_var_type, ArrayType):
                current_var_init = ArrayLiteral(current_var_type.dimens, current_var_type.dimens, current_var_type)
            else:
                current_var_init = create_init(current_var_type, o)
            ast.varInit = current_var_init

        rhs_code_gen, rhs_type_info = ("", current_var_type)

        if current_var_init is not None:
            temp_env = o.copy()
            temp_env["frame"] = Frame("<template_VT>", VoidType())
            rhs_code_gen, rhs_type_info = self.visit(current_var_init, temp_env)

        if current_var_type is None:
            current_var_type = rhs_type_info

        is_local_declaration = "frame" in o

        if not is_local_declaration:
            o["env"][0].append(Symbol(ast.varName, current_var_type, CName(self.className)))
            self.emit.printout(
                self.emit.emitATTRIBUTE(ast.varName, current_var_type, True, False, None)
            )
        else:
            frame_obj = o["frame"]
            new_idx = frame_obj.getNewIndex()
            o["env"][0].append(Symbol(ast.varName, current_var_type, Index(new_idx)))
            self.emit.printout(
                self.emit.emitVAR(
                    new_idx,
                    ast.varName,
                    current_var_type,
                    frame_obj.getStartLabel(),
                    frame_obj.getEndLabel(),
                    frame_obj,
                )
            )

            if ast.varInit is not None:
                actual_init_code, actual_init_type = self.visit(ast.varInit, o)

                if isinstance(current_var_type, FloatType) and isinstance(actual_init_type, IntType):
                    actual_init_code += self.emit.emitI2F(frame_obj)

                self.emit.printout(actual_init_code)

                last_symbol_added = o["env"][0][-1]
                if isinstance(last_symbol_added.value, Index) and not isinstance(current_var_type, StructType):
                    self.emit.printout(
                        self.emit.emitWRITEVAR(ast.varName, current_var_type, new_idx, frame_obj)
                    )
        return o

    def visitFuncCall(self, ast: FuncCall, o: dict) -> dict:
        sym = None
        for func_symbol in self.list_function:
            if func_symbol.name == ast.funName:
                sym = func_symbol
                break

        is_statement_call = o.get('stmt', False)

        if is_statement_call:
            o["stmt"] = False

            all_args_code = ""
            for arg_node in ast.args:
                arg_code, _ = self.visit(arg_node, o)
                all_args_code += arg_code

            self.emit.printout(all_args_code)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame']))
            return o
        else:
            generated_code = ""
            for arg_node in ast.args:
                arg_code, _ = self.visit(arg_node, o)
                generated_code += arg_code

            generated_code += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame'])
            return generated_code, sym.mtype.rettype

    def visitBlock(self, ast: Block, o: dict) -> dict:
        env_copy = o.copy()
        env_copy['env'] = [[]] + env_copy['env']
        current_frame = env_copy['frame']

        current_frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(current_frame.getStartLabel(), current_frame))

        idx = 0
        num_members = len(ast.member)
        while idx < num_members:
            item = ast.member[idx]
            if isinstance(item, (FuncCall, MethCall)):
                env_copy["stmt"] = True

            env_copy = self.visit(item, env_copy)

            if "stmt" in env_copy and isinstance(item, (FuncCall, MethCall)):
                del env_copy["stmt"]
            idx += 1

        self.emit.printout(self.emit.emitLABEL(current_frame.getEndLabel(), current_frame))
        current_frame.exitScope()
        return o

    def visitId(self, ast: Id, o: dict) -> dict:
        symbol_found = None
        for scope in o['env']:
            for sym_in_scope in scope:
                if sym_in_scope.name == ast.name:
                    symbol_found = sym_in_scope
                    break
            if symbol_found:
                break

        frame_obj = o['frame']
        is_left_operand = o.get('isLeft', False)

        if symbol_found is None:
            if is_left_operand:
                return self.emit.emitWRITEVAR(ast.name, self.struct, 0, frame_obj), self.struct
            else:
                return self.emit.emitREADVAR(ast.name, self.struct, 0, frame_obj), self.struct

        symbol_type = symbol_found.mtype
        symbol_value = symbol_found.value

        if is_left_operand:
            if isinstance(symbol_value, Index):
                return self.emit.emitWRITEVAR(symbol_found.name, symbol_type, symbol_value.value, frame_obj), symbol_type
            else: # CName
                return self.emit.emitPUTSTATIC(f"{self.className}/{symbol_found.name}", symbol_type, frame_obj), symbol_type
        else: # isRight or not an assignment context
            if isinstance(symbol_value, Index):
                return self.emit.emitREADVAR(symbol_found.name, symbol_type, symbol_value.value, frame_obj), symbol_type
            else: # CName
                return self.emit.emitGETSTATIC(f"{self.className}/{symbol_found.name}", symbol_type, frame_obj), symbol_type

    def visitAssign(self, ast: Assign, o: dict) -> dict:
        is_lhs_id = isinstance(ast.lhs, Id)
        lhs_id_name = ast.lhs.name if is_lhs_id else None

        symbol_exists = False
        if is_lhs_id:
            for scope in o['env']:
                for sym_in_scope in scope:
                    if sym_in_scope.name == lhs_id_name:
                        symbol_exists = True
                        break
                if symbol_exists:
                    break

        if is_lhs_id and not symbol_exists:
            undeclared_var_decl = VarDecl(lhs_id_name, None, None)
            self.visit(undeclared_var_decl, o)
            return o

        rhs_instructions, rhs_type_info = self.visit(ast.rhs, o)

        o_for_lhs = o.copy()
        o_for_lhs['isLeft'] = True
        lhs_instructions, lhs_type_info = self.visit(ast.lhs, o_for_lhs)

        final_rhs_instructions = rhs_instructions
        if isinstance(lhs_type_info, FloatType) and isinstance(rhs_type_info, IntType):
            final_rhs_instructions += self.emit.emitI2F(o['frame'])

        o['frame'].push()

        if isinstance(ast.lhs, ArrayCell):
            self.emit.printout(lhs_instructions)
            self.emit.printout(final_rhs_instructions)
            self.emit.printout(self.emit.emitASTORE(self.arrayCellType, o['frame']))
        else:
            self.emit.printout(final_rhs_instructions)
            self.emit.printout(lhs_instructions)

        return o

    def visitReturn(self, ast: Return, o: dict) -> dict:
        current_frame = o['frame']
        expected_return_type = self.function.retType

        if ast.expr is not None:
            expression_code, actual_expression_type = self.visit(ast.expr, o)
            self.emit.printout(expression_code)

            is_expected_float = isinstance(expected_return_type, FloatType)
            is_actual_int = isinstance(actual_expression_type, IntType)

            if is_expected_float and is_actual_int:
                conversion_instruction = self.emit.emitI2F(current_frame)
                self.emit.printout(conversion_instruction)

        return_instruction_code = self.emit.emitRETURN(expected_return_type, current_frame)
        self.emit.printout(return_instruction_code)
        return o

    def visitBinaryOp(self, ast: BinaryOp, o: dict) -> tuple[str, Type]:
        operator_symbol = ast.op
        current_frame = o['frame']

        left_code, left_type = self.visit(ast.left, o)
        right_code, right_type = self.visit(ast.right, o)

        if operator_symbol in ('+', '-', '*', '/') and \
           isinstance(left_type, (IntType, FloatType)) and \
           isinstance(right_type, (IntType, FloatType)):

            return_type = FloatType()
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return_type = IntType()

            processed_left_code = left_code
            processed_right_code = right_code

            if isinstance(return_type, FloatType):
                if isinstance(left_type, IntType):
                    processed_left_code += self.emit.emitI2F(current_frame)
                if isinstance(right_type, IntType):
                    processed_right_code += self.emit.emitI2F(current_frame)

            final_code_sequence = processed_left_code + processed_right_code
            if operator_symbol == '+' or operator_symbol == '-':
                return final_code_sequence + self.emit.emitADDOP(operator_symbol, return_type, current_frame), return_type
            else:
                return final_code_sequence + self.emit.emitMULOP(operator_symbol, return_type, current_frame), return_type

        if operator_symbol == '%' and isinstance(left_type, IntType) and isinstance(right_type, IntType):
            return left_code + right_code + self.emit.emitMOD(current_frame), IntType()

        if operator_symbol in ('==', '!=', '<', '>', '>=', '<=') and \
           isinstance(left_type, (IntType, FloatType)) and \
           isinstance(right_type, (IntType, FloatType)):

            comparison_type = FloatType()
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                comparison_type = IntType()

            processed_left_code = left_code
            processed_right_code = right_code

            if isinstance(left_type, IntType) and not isinstance(right_type, IntType):
                processed_left_code += self.emit.emitI2F(current_frame)
            elif isinstance(right_type, IntType) and not isinstance(left_type, IntType):
                processed_right_code += self.emit.emitI2F(current_frame)

            return processed_left_code + processed_right_code + self.emit.emitREOP(operator_symbol, comparison_type, current_frame), BoolType()

        if operator_symbol == '&&':
            return left_code + right_code + self.emit.emitANDOP(current_frame), BoolType()
        if operator_symbol == '||':
            return left_code + right_code + self.emit.emitOROP(current_frame), BoolType()

        if operator_symbol == '+' and isinstance(left_type, StringType) and isinstance(right_type, StringType):
            return left_code + right_code + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), current_frame), StringType()

        if operator_symbol in ('==', '!=', '<', '>', '>=', '<=') and \
           isinstance(left_type, StringType) and \
           isinstance(right_type, StringType):

            generated_code = left_code + right_code
            generated_code += self.emit.emitINVOKEVIRTUAL("java/lang/String/compareTo", MType([StringType()], IntType()), current_frame)
            generated_code += self.emit.emitPUSHICONST(0, current_frame)
            generated_code += self.emit.emitREOP(operator_symbol, IntType(), current_frame)
            return generated_code, BoolType()

        return "", VoidType()

    def visitUnaryOp(self, ast: UnaryOp, o: dict) -> tuple[str, Type]:
        current_frame = o['frame']
        operand_code, operand_type = self.visit(ast.body, o)
        op_char = ast.op

        if op_char == '!':
            return operand_code + self.emit.emitNOT(BoolType(), current_frame), BoolType()

        if op_char == '-':
            return operand_code + self.emit.emitNEGOP(operand_type, current_frame), operand_type

        return "", VoidType()

    def visitIntLiteral(self, ast: IntLiteral, o: dict) -> tuple[str, Type]:
        frame_obj = o['frame']
        literal_val = ast.value
        instruction_code = self.emit.emitPUSHICONST(literal_val, frame_obj)
        return instruction_code, IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o: dict) -> tuple[str, Type]:
        frame_obj = o['frame']
        literal_val = ast.value
        instruction_code = self.emit.emitPUSHFCONST(literal_val, frame_obj)
        return instruction_code, FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: dict) -> tuple[str, Type]:
        frame_obj = o['frame']
        literal_val = ast.value
        instruction_code = self.emit.emitPUSHICONST(literal_val, frame_obj)
        return instruction_code, BoolType()

    def visitStringLiteral(self, ast: StringLiteral, o: dict) -> tuple[str, Type]:
        frame_obj = o['frame']
        literal_val = ast.value
        instruction_code = self.emit.emitPUSHCONST(literal_val, StringType(), frame_obj)
        return instruction_code, StringType()

    ## END basic expression ------------------------------

    ## array ------------------------------
    def visitArrayCell(self, ast: ArrayCell, o: dict) -> tuple[str, Type]:
        env_for_array_expr = o.copy()
        env_for_array_expr["isLeft"] = False

        generated_code, array_type_info = self.visit(ast.arr, env_for_array_expr)

        index_count = len(ast.idx)
        for i in range(index_count):
            index_item = ast.idx[i]
            index_code, _ = self.visit(index_item, env_for_array_expr)
            generated_code += index_code
            if i < index_count - 1:
                generated_code += self.emit.emitALOAD(array_type_info, o["frame"])

        resulting_type = None
        if len(array_type_info.dimens) == index_count:
            resulting_type = array_type_info.eleType
            if not o.get("isLeft"):
                generated_code += self.emit.emitALOAD(resulting_type, o["frame"])
            else:
                self.arrayCell = ast
                self.arrayCellType = resulting_type
        else:
            remaining_dimensions = array_type_info.dimens[index_count:]
            resulting_type = ArrayType(remaining_dimensions, array_type_info.eleType)
            if not o.get("isLeft"):
                generated_code += self.emit.emitALOAD(resulting_type, o["frame"])
            else:
                self.arrayCell = ast
                self.arrayCellType = resulting_type

        return generated_code, resulting_type

    def visitArrayLiteral(self, ast: ArrayLiteral, o: dict) -> tuple[str, Type]:
        def process_nested_list(
            data_item: Union[Literal, list["NestedList"]], context: dict
        ) -> tuple[str, Type]:
            if not isinstance(data_item, list):
                if data_item is None:
                    raise ValueError("ArrayLiteral contains a None value")
                return self.visit(data_item, context)

            current_frame = context["frame"]
            generated_code = self.emit.emitPUSHCONST(
                len(data_item), IntType(), current_frame
            )

            if (
                not data_item
            ):  # Handle empty list case if necessary, though original doesn't explicitly
                # Assuming non-empty list based on original logic focusing on dat[0]
                # This path might need adjustment if empty lists are valid and have specific type implications
                pass

            first_element = data_item[0]
            if first_element is None:
                raise ValueError("ArrayLiteral contains a None value")

            if not isinstance(first_element, list):
                _, element_type = self.visit(first_element, context)
                if isinstance(element_type, IntType):
                    generated_code += self.emit.emitNEWARRAY(
                        element_type, current_frame
                    )
                else:
                    generated_code += self.emit.emitANEWARRAY(
                        element_type, current_frame
                    )

                item_idx = 0
                while item_idx < len(data_item):
                    list_item = data_item[item_idx]
                    if list_item is None:
                        raise ValueError("ArrayLiteral contains a None value")
                    generated_code += self.emit.emitDUP(current_frame)
                    generated_code += self.emit.emitPUSHCONST(
                        item_idx, IntType(), current_frame
                    )
                    item_code, _ = self.visit(list_item, context)
                    generated_code += item_code
                    generated_code += self.emit.emitASTORE(element_type, current_frame)
                    item_idx += 1
                return generated_code, ArrayType(
                    [IntLiteral(len(data_item))], element_type
                )
            else:
                _, sub_array_type = process_nested_list(first_element, context)
                if isinstance(
                    sub_array_type, IntType
                ):  # This case seems unlikely for nested arrays based on typical usage
                    generated_code += self.emit.emitNEWARRAY(
                        sub_array_type, current_frame
                    )
                else:
                    generated_code += self.emit.emitANEWARRAY(
                        sub_array_type, current_frame
                    )

                item_idx = 0
                while item_idx < len(data_item):
                    list_item = data_item[item_idx]
                    if list_item is None:
                        raise ValueError("ArrayLiteral contains a None value")
                    generated_code += self.emit.emitDUP(current_frame)
                    generated_code += self.emit.emitPUSHCONST(
                        item_idx, IntType(), current_frame
                    )
                    item_code, _ = process_nested_list(list_item, context)
                    generated_code += item_code
                    generated_code += self.emit.emitASTORE(
                        sub_array_type, current_frame
                    )
                    item_idx += 1
                return generated_code, ArrayType(
                    [IntLiteral(len(data_item))], sub_array_type
                )

        if isinstance(ast.value, ArrayType):
            return self.visit(ast.value, o)

        return process_nested_list(ast.value, o)

    def visitConstDecl(self, ast: ConstDecl, o: dict) -> dict:
        var_decl_equivalent = VarDecl(ast.conName, ast.conType, ast.iniExpr)
        return self.visit(var_decl_equivalent, o)

    def visitArrayType(self, ast: ArrayType, o: dict) -> tuple[str, Type]:
        generated_code = ""
        dimension_codes = []

        dim_idx = 0
        while dim_idx < len(ast.dimens):
            dimension = ast.dimens[dim_idx]
            if isinstance(dimension, int):
                dimension_codes.append(self.emit.emitPUSHICONST(dimension, o["frame"]))
            else:
                dim_code_segment, _ = self.visit(dimension, o)
                dimension_codes.append(dim_code_segment)
            dim_idx += 1

        generated_code += "".join(dimension_codes)
        generated_code += self.emit.emitMULTIANEWARRAY(ast, o["frame"])
        return generated_code, ast

    def lookup(self, name_to_find, list_to_search, matching_function):
        idx = 0
        while idx < len(list_to_search):
            element = list_to_search[idx]
            if isinstance(element, list):
                found_symbol = self.lookup(name_to_find, element, matching_function)
                if found_symbol:
                    return found_symbol
            elif matching_function(element) == name_to_find:
                return element
            idx += 1
        return None

    def visitIf(self, ast: If, o: dict) -> dict:
        current_frame = o["frame"]
        exit_if_label = current_frame.getNewLabel()
        else_branch_label = current_frame.getNewLabel()

        condition_code, _ = self.visit(ast.expr, o)
        self.emit.printout(condition_code)
        self.emit.printout(self.emit.emitIFFALSE(else_branch_label, current_frame))

        self.visit(ast.thenStmt, o)
        self.emit.printout(self.emit.emitGOTO(exit_if_label, current_frame))

        self.emit.printout(self.emit.emitLABEL(else_branch_label, current_frame))
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, o)

        self.emit.printout(self.emit.emitLABEL(exit_if_label, current_frame))
        return o

    def visitForBasic(self, ast: ForBasic, o: dict) -> dict:
        current_frame = o["frame"]
        current_frame.enterLoop()

        loop_start_label = current_frame.getNewLabel()
        loop_break_label = current_frame.getBreakLabel()
        loop_continue_label = current_frame.getContinueLabel()

        self.emit.printout(self.emit.emitLABEL(loop_start_label, current_frame))

        condition_code, _ = self.visit(ast.cond, o)
        self.emit.printout(condition_code)
        self.emit.printout(self.emit.emitIFFALSE(loop_break_label, current_frame))

        self.visit(ast.loop, o)

        self.emit.printout(self.emit.emitLABEL(loop_continue_label, current_frame))
        self.emit.printout(self.emit.emitGOTO(loop_start_label, current_frame))
        self.emit.printout(self.emit.emitLABEL(loop_break_label, current_frame))

        current_frame.exitLoop()
        return o

    def visitForStep(self, ast: ForStep, o: dict) -> dict:
        current_frame = o['frame']
        current_frame.enterLoop()

        start_loop_label = current_frame.getNewLabel()
        break_loop_label = current_frame.getBreakLabel()
        continue_loop_label = current_frame.getContinueLabel()

        loop_env = o.copy()
        loop_env['env'] = [[]] + loop_env['env']

        self.visit(ast.init, loop_env)

        self.emit.printout(self.emit.emitLABEL(start_loop_label, current_frame))

        condition_code, _ = self.visit(ast.cond, loop_env)
        self.emit.printout(condition_code)
        self.emit.printout(self.emit.emitIFFALSE(break_loop_label, current_frame))

        self.visit(ast.loop, loop_env)

        self.emit.printout(self.emit.emitLABEL(continue_loop_label, current_frame))

        self.visit(ast.upda, loop_env)

        self.emit.printout(self.emit.emitGOTO(start_loop_label, current_frame))

        self.emit.printout(self.emit.emitLABEL(break_loop_label, current_frame))

        current_frame.exitLoop()
        return o

    def visitContinue(self, ast, o: dict) -> dict:
        current_frame = o['frame']
        continue_label = current_frame.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(continue_label, current_frame))
        return o

    def visitBreak(self, ast, o: dict) -> dict:
        current_frame = o['frame']
        break_label = current_frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(break_label, current_frame))
        return o

    def visitStructType(self, ast: StructType, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object"))

        for item_type_value in self.list_type.values():
            if isinstance(item_type_value, InterfaceType) and self.checkType(item_type_value, ast, [(InterfaceType, StructType)]):
                self.emit.printout(f".implements {item_type_value.name}")

        for element_item in ast.elements:
            self.emit.printout(self.emit.emitATTRIBUTE(element_item[0], element_item[1], False, False, None))

        constructor_params = [ParamDecl(name, typ) for name, typ in ast.elements]
        constructor_body_assigns = [
            Assign(FieldAccess(Id("this"), Id(name)), Id(name)) for name, _ in ast.elements
        ]
        parameterized_constructor = MethodDecl(
            None,
            None,
            FuncDecl("<init>", constructor_params, VoidType(), Block(constructor_body_assigns)),
        )
        self.visit(parameterized_constructor, o)

        default_constructor_node = MethodDecl(
            None,
            None,
            FuncDecl("<init>", [], VoidType(), Block([])),
        )
        self.visit(default_constructor_node, o)

        for method_node in ast.methods:
            self.visit(method_node, o)

        self.emit.printout(self.emit.emitEPILOG())

    def visitMethodDecl(self, ast: MethodDecl, o):
        self.function = ast.fun
        method_frame = Frame(ast.fun.name, ast.fun.retType)

        method_mtype = MType([param.parType for param in ast.fun.params], ast.fun.retType)

        declaration_index = 0
        for i, decl_item in enumerate(self.astTree.decl):
            if isinstance(decl_item, MethodDecl) and decl_item == ast:
                declaration_index = i
                break

        global_env_segment = o.get('env', [[]])[0][:declaration_index]

        method_env = o.copy()
        method_env['frame'] = method_frame
        method_env['env'] = [[]] + [global_env_segment]

        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, method_mtype, False, method_frame))
        method_frame.enterScope(True)

        self.emit.printout(self.emit.emitVAR(method_frame.getNewIndex(), "this", Id(self.struct.name), method_frame.getStartLabel(), method_frame.getEndLabel(), method_frame))

        self.emit.printout(self.emit.emitLABEL(method_frame.getStartLabel(), method_frame))

        if ast.receiver is None:
            self.emit.printout(self.emit.emitREADVAR("this", Id(self.struct.name), 0, method_frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(method_frame, "java/lang/Object/<init>", MType([], VoidType())))

        for param_node in ast.fun.params:
            self.visit(param_node, method_env)

        self.visit(ast.body, method_env)

        self.emit.printout(self.emit.emitLABEL(method_frame.getEndLabel(), method_frame))

        if isinstance(ast.fun.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), method_frame))

        self.emit.printout(self.emit.emitENDMETHOD(method_frame))
        method_frame.exitScope()
        return o

    def visitInterfaceType(self, ast: InterfaceType, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object", True))

        for method_item in ast.methods:
            method_mtype = MType([param.parType for param in method_item.params], method_item.retType)
            self.emit.printout(self.emit.emitMETHOD(method_item.name, method_mtype, True, None))
            self.emit.printout(self.emit.emitENDMETHOD(None))

        self.emit.printout(self.emit.emitEPILOG())

    def visitFieldAccess(self, ast: FieldAccess, o: dict) -> tuple[str, Type]:
        field_identifier = ast.field.name if hasattr(ast.field, "name") else ast.field

        if isinstance(ast.receiver, Id):
            receiver_symbol = self.lookup(
                ast.receiver.name, [j for i in o["env"] for j in i], lambda x: x.name
            )
            if receiver_symbol:
                if hasattr(receiver_symbol.mtype, "name"):
                    print(f"Debug: Type name: {receiver_symbol.mtype.name}")

                receiver_access_code = self.emit.emitREADVAR(
                    receiver_symbol.name, receiver_symbol.mtype, receiver_symbol.value.value, o["frame"]
                )

                resolved_struct_type = None
                if isinstance(receiver_symbol.mtype, StructType):
                    resolved_struct_type = receiver_symbol.mtype
                elif isinstance(receiver_symbol.mtype, Id):
                    resolved_struct_type = self.list_type.get(receiver_symbol.mtype.name)
                    if not resolved_struct_type:
                        for program_decl in self.astTree.decl:
                            if hasattr(program_decl, "name") and program_decl.name == receiver_symbol.mtype.name:
                                if isinstance(program_decl, StructType):
                                    resolved_struct_type = program_decl
                                    self.list_type[program_decl.name] = program_decl
                                    break

                if resolved_struct_type and isinstance(resolved_struct_type, StructType):
                    target_field = next(
                        (f_elem for f_elem in resolved_struct_type.elements if f_elem[0] == field_identifier), None
                    )
                    if target_field:
                        target_field_type = target_field[1]
                        field_access_code = self.emit.emitGETFIELD(
                            f"{resolved_struct_type.name}/{field_identifier}", target_field_type, o["frame"]
                        )
                        return receiver_access_code + field_access_code, target_field_type
                    else:
                        raise TypeError(
                            f"Field {field_identifier} not found in struct {resolved_struct_type.name}"
                        )
                else:
                    if isinstance(receiver_symbol.mtype, Id):
                        field_access_code = self.emit.emitGETFIELD(
                            f"{receiver_symbol.mtype.name}/{field_identifier}", None, o["frame"]
                        )
                        return receiver_access_code + field_access_code, None

        generated_receiver_code, receiver_actual_type = self.visit(ast.receiver, o)

        if isinstance(receiver_actual_type, Id):
            resolved_struct_type_from_id = self.list_type.get(receiver_actual_type.name)
            if resolved_struct_type_from_id and isinstance(resolved_struct_type_from_id, StructType):
                target_field_from_id = next((f_elem for f_elem in resolved_struct_type_from_id.elements if f_elem[0] == field_identifier), None)
                if target_field_from_id:
                    target_field_type_from_id = target_field_from_id[1]
                    field_access_code_from_id = self.emit.emitGETFIELD(
                        f"{resolved_struct_type_from_id.name}/{field_identifier}", target_field_type_from_id, o["frame"]
                    )
                    return generated_receiver_code + field_access_code_from_id, target_field_type_from_id

        raise TypeError(f"Receiver {ast.receiver} is not a StructType")

    def visitMethCall(self, ast: MethCall, o: dict) -> tuple[str, Type]:
        receiver_code, receiver_type = self.visit(ast.receiver, o)

        actual_struct_type = None
        if isinstance(receiver_type, StructType):
            actual_struct_type = receiver_type
        elif isinstance(receiver_type, Id):
            actual_struct_type = self.list_type.get(receiver_type.name)
            if not actual_struct_type:
                for program_decl in self.astTree.decl:
                    if isinstance(program_decl, StructType) and hasattr(program_decl, "name") and program_decl.name == receiver_type.name:
                        actual_struct_type = program_decl
                        self.list_type[program_decl.name] = program_decl
                        break

        is_statement_context = o.pop("stmt", False)

        arguments_code_segments = []
        argument_types_list = []
        for argument_node in ast.args:
            arg_code_part, arg_type_part = self.visit(argument_node, o)
            arguments_code_segments.append(arg_code_part)
            argument_types_list.append(arg_type_part)

        full_arguments_code = "".join(arguments_code_segments)
        method_identifier = ast.metName
        method_return_type = None

        if actual_struct_type:
            if isinstance(actual_struct_type, StructType):
                target_method = next((m_decl for m_decl in actual_struct_type.methods if m_decl.fun.name == method_identifier), None)
                if not target_method:
                    raise AttributeError(f"Method {method_identifier} not found in struct {actual_struct_type.name}")

                method_mtype_sig = MType([p.parType for p in target_method.fun.params], target_method.fun.retType)
                method_return_type = target_method.fun.retType
                receiver_code += full_arguments_code
                receiver_code += self.emit.emitINVOKEVIRTUAL(f"{actual_struct_type.name}/{method_identifier}", method_mtype_sig, o["frame"])
            elif isinstance(actual_struct_type, InterfaceType):
                target_method_interface = next((m_decl for m_decl in actual_struct_type.methods if m_decl.name == method_identifier), None)
                if not target_method_interface:
                    raise AttributeError(f"Method {method_identifier} not found in interface {actual_struct_type.name}")

                interface_param_types = []
                for param_item in target_method_interface.params:
                    if hasattr(param_item, 'parType'):
                        interface_param_types.append(param_item.parType)
                    else:
                        interface_param_types.append(param_item)

                interface_mtype_sig = MType(interface_param_types, target_method_interface.retType)
                method_return_type = target_method_interface.retType
                receiver_code += full_arguments_code
                receiver_code += self.emit.emitINVOKEINTERFACE(f"{actual_struct_type.name}/{method_identifier}", interface_mtype_sig, o["frame"])
        else:
            raise TypeError(f"Cannot call method on non-struct/interface type {receiver_type}")

        if is_statement_context:
            self.emit.printout(receiver_code)
            return o
        return receiver_code, method_return_type

    def visitStructLiteral(self, ast: StructLiteral, o: dict) -> tuple[str, Type]:
        generated_code = self.emit.emitNEW(ast.name, o['frame'])
        generated_code += self.emit.emitDUP(o['frame'])

        field_types_list = []
        for _, field_value_node in ast.elements:
            field_init_code, field_actual_type = self.visit(field_value_node, o)
            generated_code += field_init_code
            field_types_list.append(field_actual_type)

        constructor_mtype = MType(field_types_list, VoidType())
        generated_code += self.emit.emitINVOKESPECIAL(o['frame'], f"{ast.name}/<init>", constructor_mtype)

        return generated_code, Id(ast.name)

    def checkType(self, LSH_type: Type, RHS_type: Type, list_type_permission: List[tuple[Type, Type]] = []) -> bool:
        if isinstance(RHS_type, StructType) and RHS_type.name == "":
            return isinstance(LSH_type, (InterfaceType, StructType, Id))

        resolved_LSH_type = self.lookup(LSH_type.name, self.list_type.values(), lambda x: x.name) if isinstance(LSH_type, Id) else LSH_type
        resolved_RHS_type = self.lookup(RHS_type.name, self.list_type.values(), lambda x: x.name) if isinstance(RHS_type, Id) else RHS_type

        if (type(resolved_LSH_type), type(resolved_RHS_type)) in list_type_permission:
            if isinstance(resolved_LSH_type, InterfaceType) and isinstance(resolved_RHS_type, StructType):
                return all(
                    any(
                        sm.fun.name == im.name and
                        self.checkType(sm.fun.retType, im.retType) and
                        len(sm.fun.params) == len(im.params) and
                        all(
                            self.checkType(sm.fun.params[i].parType, im.params[i].parType)
                            for i in range(len(sm.fun.params))
                        )
                        for sm in resolved_RHS_type.methods
                    )
                    for im in resolved_LSH_type.methods
                )

            if isinstance(resolved_LSH_type, (InterfaceType, StructType)) and isinstance(resolved_RHS_type, (InterfaceType, StructType)):
                return resolved_LSH_type.name == resolved_RHS_type.name

        if isinstance(resolved_LSH_type, ArrayType) and isinstance(resolved_RHS_type, ArrayType):
            return (
                len(resolved_LSH_type.dimens) == len(resolved_RHS_type.dimens) and
                all(l.value == r.value for l, r in zip(resolved_LSH_type.dimens, resolved_RHS_type.dimens)) and
                self.checkType(resolved_LSH_type.eleType, resolved_RHS_type.eleType, list_type_permission)
            )

        if type(resolved_LSH_type) == type(resolved_RHS_type):
            return True

        return False

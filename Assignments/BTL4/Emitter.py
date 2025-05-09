

from Utils import *
# from StaticCheck import *
# from StaticError import *
import CodeGenerator as cgen # Keep this for cgen.ClassType if used, though prefer local ClassType
from MachineCode import JasminCode
from AST import *
from CodeGenError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int
        self.value = value

class CName(Val):
    def __init__(self, value,isStatic=True):
        #value: String
        self.isStatic = isStatic
        self.value = value

class ClassType:
    def __init__(self, name):
        #value: Id or String
        self.name = name

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"


class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.jvm = JasminCode()

    def getJVMType(self, inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "I"
        if typeIn is FloatType:
            return "F"
        if typeIn is BoolType:
            return "Z"
        elif typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is ArrayType:
            return "[" + self.getJVMType(inType.eleType)
        elif typeIn is MType:
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.partype))) + ")" + self.getJVMType(inType.rettype)
        elif typeIn is ClassType: # Use this class's ClassType
            return "L" + inType.name + ";"
        elif typeIn is cgen.ClassType: # Handle if cgen.ClassType is used elsewhere (legacy)
             return "L" + inType.name + ";"
        else:
            raise IllegalOperandException("Unknown type for getJVMType: " + str(typeIn) + " Value: " + str(inType) )


    def getFullType(inType): # Static method
        typeIn = type(inType)
        if typeIn is IntType:
            return "int"
        elif typeIn is StringType:
            return "java/lang/String"
        elif typeIn is VoidType:
            return "void"
        # Add other types if needed by specific Jasmin instructions not covered by getJVMType
        raise IllegalOperandException("Unsupported type for getFullType: " + str(typeIn))


    def emitPUSHICONST(self, in_, frame):
        frame.push();
        if type(in_) is int:
            i = in_
            if i >= -1 and i <=5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
            else:
                return self.jvm.emitLDC(str(i)) # For larger integers
        elif type(in_) is bool: # Handle Python bool directly
            return self.jvm.emitICONST(1) if in_ else self.jvm.emitICONST(0)
        elif type(in_) is str: # From BooleanLiteral "true"/"false" or int as string
            if in_ == "true":
                return self.jvm.emitICONST(1)
            elif in_ == "false":
                return self.jvm.emitICONST(0)
            else: # From IntLiteral as string
                return self.emitPUSHICONST(int(in_), frame) # Recurse with int after popping original frame.push
        else:
            raise IllegalOperandException("Invalid type for PUSHICONST: " + str(type(in_)))


    def emitPUSHFCONST(self, in_, frame):
        if type(in_) is str:
            f = float(in_)
        elif type(in_) is float:
            f = in_
        else:
            raise IllegalOperandException("Invalid type for PUSHFCONST: " + str(type(in_)))

        frame.push()
        if f == 0.0:
            return self.jvm.emitFCONST("0.0")
        elif f == 1.0:
            return self.jvm.emitFCONST("1.0")
        elif f == 2.0:
            return self.jvm.emitFCONST("2.0")
        else:
            return self.jvm.emitLDC(str(f))


    def emitPUSHCONST(self, in_, typ, frame):
        # in_: String (lexeme) or direct value for bool/int/float
        # typ: AST.Type

        typeIn = type(typ)
        if typeIn is IntType:
            val = int(in_) if isinstance(in_, str) else in_
            return self.emitPUSHICONST(val, frame)
        elif typeIn is BoolType:
            val = None
            if isinstance(in_, bool): val = in_
            elif isinstance(in_, str):
                if in_ == "true": val = True
                elif in_ == "false": val = False
            if val is None: raise IllegalOperandException("Invalid boolean for PUSHCONST: " + str(in_))
            return self.emitPUSHICONST(val, frame)
        elif typeIn is FloatType:
            val = float(in_) if isinstance(in_, str) else in_
            return self.emitPUSHFCONST(val, frame)
        elif typeIn is StringType:
            frame.push()
            return self.jvm.emitLDC(in_) # `in_` should be the already quoted string literal value
        else:
            raise IllegalOperandException("Unsupported type for PUSHCONST: " + str(typ))


    def emitALOAD(self, ele_type, frame):
        # ele_type: AST.Type of the element being loaded
        # Stack: arrayref, index -> value. Net effect: pop 1.
        frame.pop()

        typeIn = type(ele_type)
        if typeIn is IntType: return self.jvm.emitIALOAD()
        elif typeIn is FloatType: return self.jvm.emitFALOAD()
        elif typeIn is BoolType: return self.jvm.emitBALOAD()
        elif typeIn is StringType or \
             typeIn is ArrayType or \
             typeIn is ClassType or \
             typeIn is cgen.ClassType:
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException("Unsupported element type for ALOAD: " + str(ele_type))

    def emitASTORE(self, ele_type, frame):
        # ele_type: AST.Type of the element being stored
        # Stack: arrayref, index, value -> . Net effect: pop 3.
        frame.pop() # value
        frame.pop() # index
        frame.pop() # arrayref

        typeIn = type(ele_type)
        if typeIn is IntType: return self.jvm.emitIASTORE()
        elif typeIn is FloatType: return self.jvm.emitFASTORE()
        elif typeIn is BoolType: return self.jvm.emitBASTORE()
        elif typeIn is StringType or \
             typeIn is ArrayType or \
             typeIn is ClassType or \
             typeIn is cgen.ClassType:
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException("Unsupported element type for ASTORE: " + str(ele_type))


    def emitVAR(self, index, varName, varType, fromLabel, toLabel, frame):
        return self.jvm.emitVAR(index, varName, self.getJVMType(varType), fromLabel, toLabel)

    def emitREADVAR(self, name, inType, index, frame):
        frame.push()
        typeIn = type(inType)
        if typeIn is IntType or typeIn is BoolType: return self.jvm.emitILOAD(index)
        elif typeIn is FloatType: return self.jvm.emitFLOAD(index)
        elif typeIn is ArrayType or \
             typeIn is ClassType or \
             typeIn is cgen.ClassType or \
             typeIn is StringType: return self.jvm.emitALOAD(index)
        else: raise IllegalOperandException("Cannot read var: " + name + " of type " + str(typeIn))

    def emitWRITEVAR(self, name, inType, index, frame):
        frame.pop()
        typeIn = type(inType)
        if typeIn is IntType or typeIn is BoolType: return self.jvm.emitISTORE(index)
        elif typeIn is FloatType: return self.jvm.emitFSTORE(index)
        elif typeIn is ArrayType or \
             typeIn is ClassType or \
             typeIn is cgen.ClassType or \
             typeIn is StringType: return self.jvm.emitASTORE(index)
        else: raise IllegalOperandException("Cannot write var: " + name + " of type " + str(typeIn))

    def emitATTRIBUTE(self, lexeme, in_type, isStatic, isFinal, value_str):
        if isStatic:
            return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_type), isFinal, value_str)
        else: # Instance field
            return self.jvm.emitINSTANCEFIELD(lexeme, self.getJVMType(in_type), isFinal, value_str)

    def emitGETSTATIC(self, lexeme, in_type, frame):
        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_type))

    def emitPUTSTATIC(self, lexeme, in_type, frame):
        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_type))

    def emitGETFIELD(self, lexeme, in_type, frame):
        # Stack: obj_ref -> val ; obj_ref is consumed, val is pushed. Net 0.
        # CodeGenerator is responsible for pushing obj_ref.
        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_type))

    def emitPUTFIELD(self, lexeme, in_type, frame):
        # Stack: obj_ref, val ->
        frame.pop() # val
        frame.pop() # obj_ref
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_type))

    def emitINVOKESTATIC(self, lexeme, mtype: MType, frame):
        for _ in mtype.partype: frame.pop()
        if not type(mtype.rettype) is VoidType: frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(mtype))

    def emitINVOKESPECIAL(self, frame, lexeme=None, mtype: MType=None):
        if lexeme and mtype: # Specific constructor/super call
            for _ in mtype.partype: frame.pop() # Pop arguments
            frame.pop() # Pop objectref (this)
            # Constructor return type is VoidType, so no push.
            if not type(mtype.rettype) is VoidType: frame.push() # Should not happen for <init>
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(mtype))
        else: # Default super() in <init>
            frame.pop() # Pop objectref (this)
            return self.jvm.emitINVOKESPECIAL()

    def emitINVOKEVIRTUAL(self, lexeme, mtype: MType, frame):
        for _ in mtype.partype: frame.pop() # Pop arguments
        frame.pop() # Pop objectref
        if not type(mtype.rettype) is VoidType: frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(mtype))

    def emitINVOKEINTERFACE(self, lexeme, mtype: MType, frame):
        # Similar to invokevirtual for stack effect
        for _ in mtype.partype: frame.pop()
        frame.pop() # objectref
        if not type(mtype.rettype) is VoidType: frame.push()
        # Jasmin does not have a direct invokeinterface wrapper, usually done via invokevirtual on interface
        # or requires specific count for invokeinterface. This needs to match JasminCode.py
        # Assuming JasminCode.emitINVOKEINTERFACE exists and handles it.
        # For now, let's assume it's like invokevirtual for Emitter's purpose if JasminCode handles it.
        # If JasminCode.emitINVOKEINTERFACE takes different params, adjust here.
        # For now, let's add it to JasminCode.py based on invokevirtual structure.
        return self.jvm.emitINVOKEINTERFACE(lexeme, self.getJVMType(mtype))


    def emitNEGOP(self, in_type, frame):
        # Stack size unchanged
        if type(in_type) is IntType: return self.jvm.emitINEG()
        elif type(in_type) is FloatType: return self.jvm.emitFNEG()
        else: raise IllegalOperandException("NEGOP for non-numeric type")

    def emitNOT(self, bool_type, frame): # bool_type is BoolType()
        # value (0/1) -> result (1/0). Stack size unchanged.
        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        res = []
        # Current value is on stack. emitIFTRUE consumes it.
        res.append(self.emitIFTRUE(label1, frame))
        res.append(self.emitPUSHCONST(False, BoolType(), frame)) # Pushes 0. Consumed by GOTO or falls through.
        res.append(self.emitGOTO(label2, frame))
        res.append(self.emitLABEL(label1, frame))
        res.append(self.emitPUSHCONST(True, BoolType(), frame)) # Pushes 1.
        res.append(self.emitLABEL(label2, frame))
        return ''.join(res)

    def emitADDOP(self, op_char, num_type, frame):
        # value1, value2 -> result. Net pop 1.
        frame.pop()
        if op_char == "+":
            if type(num_type) is IntType: return self.jvm.emitIADD()
            else: return self.jvm.emitFADD()
        else: # op_char == "-"
            if type(num_type) is IntType: return self.jvm.emitISUB()
            else: return self.jvm.emitFSUB()

    def emitMULOP(self, op_char, num_type, frame):
        # value1, value2 -> result. Net pop 1.
        frame.pop()
        if op_char == "*":
            if type(num_type) is IntType: return self.jvm.emitIMUL()
            else: return self.jvm.emitFMUL()
        else: # op_char == "/"
            if type(num_type) is IntType: return self.jvm.emitIDIV()
            else: return self.jvm.emitFDIV()

    def emitMOD(self, frame):
        # value1, value2 -> result. Net pop 1.
        frame.pop()
        return self.jvm.emitIREM()

    def emitANDOP(self, frame): # For bitwise AND if used for bools 0/1
        frame.pop()
        return self.jvm.emitIAND()

    def emitOROP(self, frame): # For bitwise OR if used for bools 0/1
        frame.pop()
        return self.jvm.emitIOR()

    def emitREOP(self, op, comp_type, frame):
        # value1, value2 -> result (boolean 0/1). Net pop 1.
        # This method produces a boolean value on stack.
        res = []
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop() # value2 consumed from stack by comparison
        frame.pop() # value1 consumed from stack by comparison
        # result (boolean) will be pushed by PUSHICONST

        if type(comp_type) is IntType: # Also for BoolType comparisons
            if op == ">": res.append(self.jvm.emitIFICMPLE(labelF))
            elif op == ">=": res.append(self.jvm.emitIFICMPLT(labelF))
            elif op == "<": res.append(self.jvm.emitIFICMPGE(labelF))
            elif op == "<=": res.append(self.jvm.emitIFICMPGT(labelF))
            elif op == "!=": res.append(self.jvm.emitIFICMPEQ(labelF))
            elif op == "==": res.append(self.jvm.emitIFICMPNE(labelF))
        elif type(comp_type) is FloatType:
            res.append(self.jvm.emitFCMPL()) # Stack: ..., int_result (-1,0,1)
            # Now compare int_result with 0 and branch.
            # IFLE means "if less than or equal to 0".
            if op == ">": res.append(self.jvm.emitIFLE(labelF))     # if !(res > 0) -> F
            elif op == ">=": res.append(self.jvm.emitIFLT(labelF))  # if !(res >=0) -> F
            elif op == "<": res.append(self.jvm.emitIFGE(labelF))   # if !(res < 0) -> F
            elif op == "<=": res.append(self.jvm.emitIFGT(labelF))  # if !(res <=0) -> F
            elif op == "!=": res.append(self.jvm.emitIFEQ(labelF))  # if !(res !=0) -> F
            elif op == "==": res.append(self.jvm.emitIFNE(labelF))  # if !(res ==0) -> F

        res.append(self.emitPUSHCONST(True, BoolType(), frame)) # True path: push 1 (PUSHCONST handles frame.push)
        res.append(self.emitGOTO(labelO, frame))
        res.append(self.emitLABEL(labelF, frame))
        res.append(self.emitPUSHCONST(False, BoolType(), frame))# False path: push 0
        res.append(self.emitLABEL(labelO, frame))
        # The PUSHCONST calls already did frame.push for the boolean result.
        return "".join(res)

    def emitRELOP(self, op, comp_type, trueLabel, falseLabel, frame):
        # This method is for conditional JUMPS, does not leave a boolean on stack.
        # Consumes two operands.
        res = []
        frame.pop() # value2
        frame.pop() # value1

        if type(comp_type) is IntType:
            if op == ">": res.append(self.jvm.emitIFICMPLE(falseLabel))
            elif op == ">=": res.append(self.jvm.emitIFICMPLT(falseLabel))
            # ... (rest as in original)
            elif op == "<": res.append(self.jvm.emitIFICMPGE(falseLabel))
            elif op == "<=": res.append(self.jvm.emitIFICMPGT(falseLabel))
            elif op == "!=": res.append(self.jvm.emitIFICMPEQ(falseLabel))
            elif op == "==": res.append(self.jvm.emitIFICMPNE(falseLabel))
            res.append(self.emitGOTO(trueLabel, frame)) # Fallthrough to true if condition met
        elif type(comp_type) is FloatType:
            res.append(self.jvm.emitFCMPL()) # Stack: ..., int_result
            # Now, compare int_result with 0 and jump.
            if op == ">": res.append(self.jvm.emitIFLE(falseLabel))
            elif op == ">=": res.append(self.jvm.emitIFLT(falseLabel))
            elif op == "<": res.append(self.jvm.emitIFGE(falseLabel))
            elif op == "<=": res.append(self.jvm.emitIFGT(falseLabel))
            elif op == "!=": res.append(self.jvm.emitIFEQ(falseLabel))
            elif op == "==": res.append(self.jvm.emitIFNE(falseLabel))
            res.append(self.emitGOTO(trueLabel, frame))
        return ''.join(res)

    def emitMETHOD(self, lexeme, mtype: MType, isStatic, frame):
        return self.jvm.emitMETHOD(lexeme, self.getJVMType(mtype), isStatic)

    def emitENDMETHOD(self, frame):
        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    def emitIFTRUE(self, label, frame): # Jump if value on stack is 1 (true)
        frame.pop()
        return self.jvm.emitIFNE(label) # if_acmpne for object, if_icmpne for int, ifne for int compared to 0

    def emitIFFALSE(self, label, frame): # Jump if value on stack is 0 (false)
        frame.pop()
        return self.jvm.emitIFEQ(label)

    def emitDUP(self, frame):
        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame):
        frame.pop()
        return self.jvm.emitPOP()

    def emitI2F(self, frame):
        # Stack size unchanged
        return self.jvm.emitI2F()

    def emitRETURN(self, return_ast_type, frame):
        typeIn = type(return_ast_type)
        # Value to be returned is assumed to be on stack if not VoidType
        if typeIn is IntType or typeIn is BoolType:
            if frame.getStackSize() > 0: frame.pop()
            return self.jvm.emitIRETURN()
        elif typeIn is FloatType:
            if frame.getStackSize() > 0: frame.pop()
            return self.jvm.emitFRETURN()
        elif typeIn is StringType or \
             typeIn is ArrayType or \
             typeIn is ClassType or \
             typeIn is cgen.ClassType:
            if frame.getStackSize() > 0: frame.pop()
            return self.jvm.emitARETURN()
        elif typeIn is VoidType:
            return self.jvm.emitRETURN()
        else:
            raise IllegalOperandException("Unsupported RETURN type: " + str(return_ast_type))

    def emitLABEL(self, label, frame):
        return self.jvm.emitLABEL(label)

    def emitGOTO(self, label, frame): # label can be int or str
        return self.jvm.emitGOTO(str(label))

    def emitPROLOG(self, name, parent):
        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER("java/lang/Object" if not parent else parent))
        return ''.join(result)

    def emitLIMITSTACK(self, num): return self.jvm.emitLIMITSTACK(num)
    def emitLIMITLOCAL(self, num): return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        with open(self.filename, "w") as file:
            file.write(''.join(self.buff))

    def printout(self, in_): self.buff.append(in_)
    def clearBuff(self): self.buff.clear()

    # Array creation: CodeGenerator manages frame stack changes for dimensions
    # These Emitter methods do not change frame stack themselves.
    def emitNEWARRAY(self, ast_element_type, frame): # e.g., IntType(), FloatType()
        typeIn = type(ast_element_type)
        if typeIn is IntType: return self.jvm.emitNEWARRAY("int")
        elif typeIn is FloatType: return self.jvm.emitNEWARRAY("float")
        elif typeIn is BoolType: return self.jvm.emitNEWARRAY("boolean")
        # char, byte, short if MiniGo had them
        else: raise IllegalOperandException("NEWARRAY for non-primitive type: " + str(ast_element_type))

    def emitANEWARRAY(self, ast_element_type, frame): # e.g. StringType(), ClassType("foo"), ArrayType(...)
        return self.jvm.emitANEWARRAY(self.getJVMType(ast_element_type))

    def emitMULTIANEWARRAY(self, full_array_ast_type: ArrayType, num_dimensions: int, frame):
        return self.jvm.emitMULTIANEWARRAY(self.getJVMType(full_array_ast_type), str(num_dimensions))

    def emitNEW(self, class_name_str, frame):
        frame.push() # new instruction pushes an uninitialized objectref
        return self.jvm.emitNEW(class_name_str)

    def emitPUSHNULL(self, frame):
        frame.push()
        return self.jvm.emitPUSHNULL()

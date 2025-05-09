from Utils import *
# from StaticCheck import *
# from StaticError import *
import CodeGenerator as cgen
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

class ClassType: # Already defined in Emitter.py, ensure it's used consistently
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
            # For multi-dimensional arrays, eleType can be ArrayType itself.
            return "[" + self.getJVMType(inType.eleType)
        elif typeIn is MType:
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.partype))) + ")" + self.getJVMType(inType.rettype)
        elif typeIn is ClassType: # Use the ClassType defined in this Emitter.py or from cgen
            return "L" + inType.name + ";"
        elif typeIn is cgen.ClassType: # Handle if cgen.ClassType is used elsewhere
             return "L" + inType.name + ";"
        else: # Should not happen for valid MiniGo types
            # raise IllegalOperandException("Unknown type for getJVMType: " + str(typeIn))
            return "Ljava/lang/Object;" # Fallback, or error

    def getFullType(inType): # This seems unused in the core logic provided
        typeIn = type(inType)
        if typeIn is IntType:
            return "int"
        elif typeIn is StringType: # Original had cgen.StringType
            return "java/lang/String"
        elif typeIn is VoidType:
            return "void"

    def emitPUSHICONST(self, in_, frame):
        # in: Int or Sring or bool
        frame.push();
        if type(in_) is int:
            i = in_
            if i >= -1 and i <=5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
            else: # Larger integers might need LDC, though MiniGo spec might limit int size
                return self.jvm.emitLDC(str(i))
        elif type(in_) is bool:
            return self.emitPUSHICONST(1 if in_ else 0, frame)
        elif type(in_) is str: # From BooleanLiteral "true"/"false"
            if in_ == "true":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "false":
                return self.emitPUSHICONST(0, frame)
            else: # From IntLiteral as string
                return self.emitPUSHICONST(int(in_), frame)


    def emitPUSHFCONST(self, in_, frame):
        # in_: String or float
        # frame: Frame
        if type(in_) is str:
            f = float(in_)
        else: # type is float
            f = in_

        frame.push()
        if f == 0.0:
            return self.jvm.emitFCONST("0.0")
        elif f == 1.0:
            return self.jvm.emitFCONST("1.0")
        elif f == 2.0:
            return self.jvm.emitFCONST("2.0")
        else:
            return self.jvm.emitLDC(str(f))

    '''
    *    generate code to push a constant onto the operand stack.
    *    @param in the lexeme of the constant
    *    @param typ the type of the constant
    '''
    def emitPUSHCONST(self, in_, typ, frame):
        # in_: String (lexeme) or direct value for bool/int/float
        # typ: Type
        # frame: Frame

        if type(typ) is IntType:
            # Assuming in_ is an int or a string convertible to int
            val = int(in_) if isinstance(in_, str) else in_
            return self.emitPUSHICONST(val, frame)
        elif type(typ) is BoolType:
            # Assuming in_ is a bool or "true"/"false"
            val = None
            if isinstance(in_, bool):
                val = in_
            elif in_ == "true":
                val = True
            elif in_ == "false":
                val = False
            else:
                raise IllegalOperandException("Invalid boolean literal for PUSHCONST: " + str(in_))
            return self.emitPUSHICONST(val, frame) # emitPUSHICONST handles bool
        elif type(typ) is FloatType:
            val = float(in_) if isinstance(in_, str) else in_
            return self.emitPUSHFCONST(val, frame)
        elif type(typ) is StringType:
            frame.push()
            return self.jvm.emitLDC(in_) # in_ should be the string content with quotes for LDC
        else:
            raise IllegalOperandException(str(in_))

    ##############################################################

    def emitALOAD(self, in_ele_type, frame):
        # in_ele_type: Type of the element being loaded
        # Stack before: ..., arrayref, index
        # Stack after: ..., value
        # Net effect: pops 2, pushes 1 => frame.pop() once is correct for net change.
        frame.pop()
        if type(in_ele_type) is IntType:
            return self.jvm.emitIALOAD()
        elif type(in_ele_type) is FloatType:
            return self.jvm.emitFALOAD()
        elif type(in_ele_type) is BoolType:
            return self.jvm.emitBALOAD()
        elif type(in_ele_type) is ArrayType or \
             type(in_ele_type) is cgen.ClassType or \
             type(in_ele_type) is ClassType or \
             type(in_ele_type) is StringType:
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException("Unsupported type for ALOAD: " + str(type(in_ele_type)))

    def emitASTORE(self, in_ele_type, frame):
        # in_ele_type: Type of the element being stored
        # Stack before: ..., arrayref, index, value
        # Stack after: ...
        # Net effect: pops 3 => frame.pop() three times.
        frame.pop() # value
        frame.pop() # index
        frame.pop() # arrayref
        if type(in_ele_type) is IntType:
            return self.jvm.emitIASTORE()
        elif type(in_ele_type) is FloatType:
            return self.jvm.emitFASTORE()
        elif type(in_ele_type) is BoolType:
            return self.jvm.emitBASTORE()
        elif type(in_ele_type) is ArrayType or \
             type(in_ele_type) is cgen.ClassType or \
             type(in_ele_type) is ClassType or \
             type(in_ele_type) is StringType:
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException("Unsupported type for ASTORE: " + str(type(in_ele_type)))


    '''    generate the var directive for a local variable.
    *   @param in the index of the local variable.
    *   @param varName the name of the local variable.
    *   @param inType the type of the local variable.
    *   @param fromLabel the starting label of the scope where the variable is active.
    *   @param toLabel the ending label  of the scope where the variable is active.
    '''
    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        # in_: Int
        # varName: String
        # inType: Type
        # fromLabel: Int
        # toLabel: Int
        # frame: Frame
        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

    def emitREADVAR(self, name, inType, index, frame):
        # name: String
        # inType: Type
        # index: Int
        # frame: Frame
        # ... -> ..., value

        frame.push()
        if type(inType) is IntType or type(inType) is BoolType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is FloatType:
            return self.jvm.emitFLOAD(index)
        elif type(inType) is ArrayType or \
             type(inType) is cgen.ClassType or \
             type(inType) is ClassType or \
             type(inType) is StringType:
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''
    def emitREADVAR2(self, name, typ, frame):
        # name: String
        # typ: Type
        # frame: Frame
        # ... -> ..., value

        # frame.push()
        raise IllegalOperandException(name)

    '''
    *   generate code to pop a value on top of the operand stack and store it to a block-scoped variable.
    *   @param name the symbol entry of the variable.
    '''
    def emitWRITEVAR(self, name, inType, index, frame):
        # name: String
        # inType: Type
        # index: Int
        # frame: Frame
        # ..., value -> ...

        frame.pop()

        if type(inType) is IntType or type(inType) is BoolType:
            return self.jvm.emitISTORE(index)
        elif type(inType) is FloatType:
            return self.jvm.emitFSTORE(index)
        elif type(inType) is ArrayType or \
             type(inType) is cgen.ClassType or \
             type(inType) is ClassType or \
             type(inType) is StringType:
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''
    def emitWRITEVAR2(self, name, typ, frame):
        # name: String
        # typ: Type
        # frame: Frame
        # ..., value -> ...

        # frame.push()
        raise IllegalOperandException(name)

    ''' generate the field (static) directive for a class mutable or immutable attribute.
    *   @param lexeme the name of the attribute.
    *   @param in the type of the attribute.
    *   @param isFinal true in case of constant; false otherwise
    '''
    def emitATTRIBUTE(self, lexeme, in_, isStatic, isFinal, value): # Added value param
        # lexeme: String
        # in_: Type
        # isStatic: Boolean
        # isFinal: Boolean
        # value: String (or None) for initial value of static final
        if isStatic:
            # JasminCode.emitSTATICFIELD expects (name, jvm_type, isFinal, value_string_or_None)
            return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), isFinal, value)
        else: # Instance field
            # JasminCode.emitFIELD / emitINSTANCEFIELD
            # Assuming emitFIELD for now, though JasminCode has emitINSTANCEFIELD.
            # Let's add emitFIELD to JasminCode if not present, or use emitINSTANCEFIELD
            # It seems emitFIELD was intended for instance fields.
            # JasminCode.emitINSTANCEFIELD(self, lexeme, typ,isFinal,value)
            return self.jvm.emitINSTANCEFIELD(lexeme, self.getJVMType(in_), isFinal, value)


    def emitGETSTATIC(self, lexeme, in_, frame):
        # lexeme: String (classname/fieldname)
        # in_: Type
        # frame: Frame
        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    def emitPUTSTATIC(self, lexeme, in_, frame):
        # lexeme: String (classname/fieldname)
        # in_: Type
        # frame: Frame
        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    def emitGETFIELD(self, lexeme, in_, frame):
        # lexeme: String (classname/fieldname for instance field)
        # in_: Type
        # frame: Frame
        # Stack: objectref -> objectref, value
        # objectref is popped, value is pushed. Net effect is 0 on stack size for this.
        # However, frame.pop() for objectref, frame.push() for value is a way to model it.
        # Current Emitter does not adjust frame here. CodeGenerator pops objref, then calls this, then CG pushes value.
        # Let's keep it as no frame change in Emitter for GETFIELD.
        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme, in_, frame):
        # lexeme: String (classname/fieldname for instance field)
        # in_: Type
        # frame: Frame
        # Stack: objectref, value ->
        frame.pop() # value
        frame.pop() # objectref
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a static method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''
    def emitINVOKESTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: MType object
        # frame: Frame

        typ = in_ # in_ is MType
        list(map(lambda x: frame.pop(), typ.partype))
        if not type(typ.rettype) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))


    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        # lexeme: String
        # in_: MType
        # frame: Frame

        if not lexeme is None and not in_ is None: # Specific constructor/super call
            typ = in_ # MType
            list(map(lambda x: frame.pop(), typ.partype)) # Pop arguments
            frame.pop() # Pop objectref (this)
            if not type(typ.rettype) is VoidType: # Should be VoidType for constructor
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None: # Default super() in <init>
            frame.pop() # Pop objectref (this)
            return self.jvm.emitINVOKESPECIAL()


    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        # lexeme: String
        # in_: MType
        # frame: Frame
        typ = in_
        list(map(lambda x: frame.pop(), typ.partype)) # Pop arguments
        frame.pop() # Pop objectref
        if not type(typ.rettype) is VoidType: # Corrected: check rettype of MType
            frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))


    def emitNEGOP(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., value -> ..., result (stack size doesn't change)
        if type(in_) is IntType:
            return self.jvm.emitINEG()
        else: # FloatType
            return self.jvm.emitFNEG()

    def emitNOT(self, in_, frame): # in_ is BoolType
        # in_: Type
        # frame: Frame
        # value -> result (stack size doesn't change)
        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(label1, frame)) #Consumes value from stack
        result.append(self.emitPUSHCONST(False, BoolType(), frame)) # Pushes false (0)
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHCONST(True, BoolType(), frame)) # Pushes true (1)
        result.append(self.emitLABEL(label2, frame))
        return ''.join(result)


    def emitADDOP(self, lexeme, in_, frame):
        # lexeme: String ("+" or "-")
        # in_: Type (IntType or FloatType, type of result/operands)
        # frame: Frame
        # ..., value1, value2 -> ..., result
        frame.pop() # Consumes one operand, effectively. (pop val2, pop val1, push result)
        if lexeme == "+":
            if type(in_) is IntType:
                return self.jvm.emitIADD()
            else: # FloatType
                return self.jvm.emitFADD()
        else: # lexeme == "-"
            if type(in_) is IntType:
                return self.jvm.emitISUB()
            else: # FloatType
                return self.jvm.emitFSUB()


    def emitMULOP(self, lexeme, in_, frame):
        # lexeme: String ("*" or "/")
        # in_: Type (IntType or FloatType)
        # frame: Frame
        frame.pop()
        if lexeme == "*":
            if type(in_) is IntType:
                return self.jvm.emitIMUL()
            else: # FloatType
                return self.jvm.emitFMUL()
        else: # lexeme == "/"
            if type(in_) is IntType:
                return self.jvm.emitIDIV()
            else: # FloatType
                return self.jvm.emitFDIV()

    def emitDIV(self, frame): # Specific for int division for old code?
        # frame: Frame
        frame.pop()
        return self.jvm.emitIDIV()

    def emitMOD(self, frame):
        # frame: Frame
        frame.pop()
        return self.jvm.emitIREM() # Use JasminCode method

    def emitANDOP(self, frame): # For '&&'
        # frame: Frame
        # ..., value1, value2 -> ..., result (value1 & value2 are 0/1)
        # IAND is bitwise AND. For logical &&, short-circuiting is usually generated by CodeGenerator.
        # If CodeGenerator already pushed two booleans (0/1), then IAND is fine.
        frame.pop()
        return self.jvm.emitIAND()

    def emitOROP(self, frame): # For '||'
        # frame: Frame
        # Similar to ANDOP, IOR is bitwise.
        frame.pop()
        return self.jvm.emitIOR()

    def emitREOP(self, op, in_type, frame): # in_type is IntType or FloatType
        # op: String like ">", "==" etc.
        # frame: Frame
        # ..., value1, value2 -> ..., result (boolean 0 or 1)
        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop() # value2 popped
        frame.pop() # value1 popped
        # result (boolean) will be pushed

        if type(in_type) is IntType:
            if op == ">": result.append(self.jvm.emitIFICMPLE(labelF))
            elif op == ">=": result.append(self.jvm.emitIFICMPLT(labelF))
            elif op == "<": result.append(self.jvm.emitIFICMPGE(labelF))
            elif op == "<=": result.append(self.jvm.emitIFICMPGT(labelF))
            elif op == "!=": result.append(self.jvm.emitIFICMPEQ(labelF))
            elif op == "==": result.append(self.jvm.emitIFICMPNE(labelF))
        elif type(in_type) is FloatType:
            # Float comparisons: fcmpg or fcmpl, then ifeq, ifne, etc.
            # fcmpg: stack: v1, v2 -> result; result is 1 if v1>v2, 0 if v1=v2, -1 if v1<v2, 1 if v1 or v2 is NaN
            # fcmpl: stack: v1, v2 -> result; result is 1 if v1>v2, 0 if v1=v2, -1 if v1<v2, -1 if v1 or v2 is NaN
            # Let's use fcmpl (NaN behaves like less than)
            result.append(self.jvm.emitFCMPL()) # Stack: ..., int_result (1,0, or -1)
            # Now compare this int_result with 0.
            # op is relative to original v1, v2.
            # v1 > v2  => int_result = 1.  Compare with 0: ifne (for 1) or ifgt (for 1)
            # v1 >= v2 => int_result = 1 or 0. Compare with 0: ifge
            # v1 < v2  => int_result = -1. Compare with 0: iflt
            # v1 <= v2 => int_result = -1 or 0. Compare with 0: ifle
            # v1 == v2 => int_result = 0. Compare with 0: ifeq
            # v1 != v2 => int_result = 1 or -1. Compare with 0: ifne

            if op == ">": result.append(self.jvm.emitIFLE(labelF)) # if result <= 0, goto false (i.e. if not (res > 0))
            elif op == ">=": result.append(self.jvm.emitIFLT(labelF)) # if result < 0, goto false
            elif op == "<": result.append(self.jvm.emitIFGE(labelF))  # if result >=0, goto false
            elif op == "<=": result.append(self.jvm.emitIFGT(labelF)) # if result > 0, goto false
            elif op == "!=": result.append(self.jvm.emitIFEQ(labelF))  # if result == 0, goto false
            elif op == "==": result.append(self.jvm.emitIFNE(labelF))  # if result != 0, goto false

        result.append(self.emitPUSHICONST(1, frame)) # True path: push 1
        # frame.pop() done by PUSHICONST, but it pushes one, so net is push.
        # Here, REOP itself consumes 2, produces 1. So emitPUSHICONST's frame.push is correct for the value.
        # But the labelF path also needs to push.
        # Let's adjust: The PUSHICONST handles its own frame.push.
        # This whole REOP sequence results in one boolean on stack.
        # So after initial 2 pops, one push must occur for the boolean result.
        # This happens via emitPUSHICONST.

        result.append(self.emitGOTO(labelO, frame)) # No frame change for GOTO
        result.append(self.emitLABEL(labelF, frame))
        result.append(self.emitPUSHICONST(0, frame)) # False path: push 0
        result.append(self.emitLABEL(labelO, frame))
        frame.push() # Account for the boolean result (0 or 1) being on stack
        return "".join(result)


    def emitRELOP(self, op, in_, trueLabel, falseLabel, frame): # Used for short-circuiting in conditions
        # op: String
        # in_: Type
        # trueLabel: Int
        # falseLabel: Int
        # frame: Frame
        # ..., value1, value2 -> ... (branches, does not leave a boolean on stack)
        result = list()
        frame.pop() # value2
        frame.pop() # value1

        # This is for conditional jumps, not for producing a boolean value on stack.
        if type(in_) is IntType: # Assuming in_ refers to the type of operands
            if op == ">": result.append(self.jvm.emitIFICMPLE(falseLabel))
            elif op == ">=": result.append(self.jvm.emitIFICMPLT(falseLabel))
            elif op == "<": result.append(self.jvm.emitIFICMPGE(falseLabel))
            elif op == "<=": result.append(self.jvm.emitIFICMPGT(falseLabel))
            elif op == "!=": result.append(self.jvm.emitIFICMPEQ(falseLabel))
            elif op == "==": result.append(self.jvm.emitIFICMPNE(falseLabel))
        elif type(in_) is FloatType:
            result.append(self.jvm.emitFCMPL()) # result: 1 (gt), 0 (eq), -1 (lt)
            # Compare result with 0 and jump
            if op == ">": result.append(self.jvm.emitIFLE(falseLabel)) # if res <= 0 (not >), jump to false
            elif op == ">=": result.append(self.jvm.emitIFLT(falseLabel))# if res < 0 (not >=), jump to false
            elif op == "<": result.append(self.jvm.emitIFGE(falseLabel)) # if res >= 0 (not <), jump to false
            elif op == "<=": result.append(self.jvm.emitIFGT(falseLabel))# if res > 0 (not <=), jump to false
            elif op == "!=": result.append(self.jvm.emitIFEQ(falseLabel)) # if res == 0 (not !=), jump to false
            elif op == "==": result.append(self.jvm.emitIFNE(falseLabel))# if res != 0 (not ==), jump to false

        result.append(self.emitGOTO(trueLabel, frame)) # emitGOTO doesn't change frame stack depth
        return ''.join(result)


    def emitMETHOD(self, lexeme, in_, isStatic, frame):
        # lexeme: String
        # in_: MType
        # isStatic: Boolean
        # frame: Frame
        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

    def emitENDMETHOD(self, frame):
        # frame: Frame
        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    def getConst(self, ast): # Seems unused
        # ast: Literal
        if type(ast) is IntLiteral:
            return (str(ast.value), IntType())


    def emitIFTRUE(self, label, frame): # Jump if true (value on stack is 1)
        # label: Int
        # frame: Frame
        frame.pop() # The boolean value (0 or 1) is consumed.
        return self.jvm.emitIFNE(label) # if value != 0 (i.e., true), jump

    def emitIFFALSE(self, label, frame): # Jump if false (value on stack is 0)
        # label: Int
        # frame: Frame
        frame.pop() # The boolean value (0 or 1) is consumed.
        return self.jvm.emitIFEQ(label) # if value == 0 (i.e., false), jump


    def emitIFICMPGT(self, label, frame): # Deprecated by emitRELOP or emitREOP
        frame.pop()
        frame.pop()
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label, frame): # Deprecated by emitRELOP or emitREOP
        frame.pop()
        frame.pop()
        return self.jvm.emitIFICMPLT(label)


    def emitDUP(self, frame):
        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame):
        frame.pop()
        return self.jvm.emitPOP()


    def emitI2F(self, frame):
        # frame: Frame
        # Stack: ..., intval -> ..., floatval (stack size unchanged)
        return self.jvm.emitI2F()


    def emitRETURN(self, in_, frame):
        # in_: Type (return type of the function)
        # frame: Frame
        if type(in_) is IntType or type(in_) is BoolType:
            if frame.getStackSize() > 0: frame.pop() # Pop return value if func not void
            return self.jvm.emitIRETURN()
        elif type(in_) is FloatType:
            if frame.getStackSize() > 0: frame.pop()
            return self.jvm.emitFRETURN()
        elif type(in_) is ArrayType or \
             type(in_) is cgen.ClassType or \
             type(in_) is ClassType or \
             type(in_) is StringType: # Added ArrayType and ClassType
            if frame.getStackSize() > 0: frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is VoidType:
            # No value to pop for void return
            return self.jvm.emitRETURN()
        else:
            raise IllegalOperandException("Unsupported return type: " + str(type(in_)))


    def emitLABEL(self, label, frame):
        return self.jvm.emitLABEL(label)

    def emitGOTO(self, label, frame): # label can be int or str
        return self.jvm.emitGOTO(str(label))


    def emitPROLOG(self, name, parent):
        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER("java/lang/Object" if parent == "" or parent is None else parent)) # Corrected super
        return ''.join(result)

    def emitLIMITSTACK(self, num):
        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):
        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    def printout(self, in_):
        self.buff.append(in_)

    def clearBuff(self):
        self.buff.clear()

    # Array creation methods: CodeGenerator will manage frame stack changes
    def emitNEWARRAY(self, in_ast_eleType, frame): # in_ast_eleType is IntType, FloatType etc.
        if type(in_ast_eleType) is IntType:
            return self.jvm.emitNEWARRAY("int")
        elif type(in_ast_eleType) is FloatType:
            return self.jvm.emitNEWARRAY("float")
        elif type(in_ast_eleType) is BoolType:
            return self.jvm.emitNEWARRAY("boolean")
        else:
            raise IllegalOperandException("NEWARRAY expects primitive type, got: " + str(type(in_ast_eleType)))

    def emitANEWARRAY(self, in_ast_eleType, frame): # in_ast_eleType is ClassType, StringType, ArrayType
        # getJVMType handles ArrayType correctly (e.g. [I for int[])
        ele_jvm_type = self.getJVMType(in_ast_eleType)
        return self.jvm.emitANEWARRAY(ele_jvm_type)

    def emitMULTIANEWARRAY(self, array_ast_type, num_dimensions, frame):
        # array_ast_type is an AST.ArrayType (e.g. [[[I for int[][][]]))
        # num_dimensions is an int
        return self.jvm.emitMULTIANEWARRAY(self.getJVMType(array_ast_type), str(num_dimensions))

    def emitNEW(self, class_name_str, frame): # class_name_str e.g. "MyClass" or "pkg/MyClass"
        frame.push() # new pushes objectref
        return self.jvm.emitNEW(class_name_str)

    def emitPUSHNULL(self, frame):
        frame.push()
        return self.jvm.emitPUSHNULL()

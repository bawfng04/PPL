from Utils import *
from StaticCheck import *
from StaticError import *
import CodeGenerator as cgen
from MachineCode import JasminCode
from Frame import Frame
from CodeGenError import *


class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.jvm = JasminCode()

    def getJVMType(self, inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "I"
        elif typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is ArrayType:
            # Assuming ArrayType has eleType attribute
            return "[" + self.getJVMType(inType.eleType)
        elif typeIn is MType:
            # Assuming MType has partype and rettype attributes
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.partype))) + ")" + self.getJVMType(inType.rettype)
        elif typeIn is cgen.ClassType:
            # Assuming ClassType has name attribute
            return "L" + inType.name + ";"
        else:
            # Fallback or error handling
            raise IllegalOperandException(str(typeIn))

    def getFullType(inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "int"
        elif typeIn is StringType: # Assuming StringType is defined elsewhere or use cgen.StringType
             return "java/lang/String"
        elif typeIn is VoidType:
            return "void"
        # Add other types if necessary
        else:
            raise IllegalOperandException(str(typeIn))


    def emitPUSHICONST(self, in_, frame):
        #in: Int or Sring
        #frame: Frame

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
                 # For integers outside the SIPUSH range, use LDC
                 return self.jvm.emitLDC(str(i))
        elif type(in_) is str:
            if in_ == "true":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "false":
                return self.emitPUSHICONST(0, frame)
            else:
                # Assuming string represents an integer
                try:
                    return self.emitPUSHICONST(int(in_), frame)
                except ValueError:
                    raise IllegalOperandException(in_)


    def emitPUSHFCONST(self, in_, frame):
        #in_: String
        #frame: Frame

        f = float(in_)
        frame.push()
        rst = "{0:.1f}".format(f) # Use .1f for 0.0, 1.0, 2.0 check
        if rst == "0.0" or rst == "1.0" or rst == "2.0":
            # Jasmin uses FCONST_0, FCONST_1, FCONST_2
            return self.jvm.emitFCONST(rst)
        else:
            # Use LDC for other float constants
            return self.jvm.emitLDC(in_)


    '''
    *    generate code to push a constant onto the operand stack.
    *    @param in the lexeme of the constant
    *    @param typ the type of the constant
    '''
    def emitPUSHCONST(self, in_, typ, frame):
        #in_: String
        #typ: Type
        #frame: Frame

        if type(typ) is IntType:
            # Handles integers and booleans represented as integers
            return self.emitPUSHICONST(in_, frame)
        # Add FloatType handling if needed
        # elif type(typ) is FloatType:
        #     return self.emitPUSHFCONST(in_, frame)
        elif type(typ) is StringType:
            frame.push()
            return self.jvm.emitLDC('"' + in_ + '"') # Strings need quotes for LDC
        else:
            raise IllegalOperandException(in_)

    ##############################################################

    def emitALOAD(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., arrayref, index -> ..., value

        # ALOAD pops arrayref and index, pushes value. Net change: -1
        frame.pop() # Pop index
        frame.pop() # Pop arrayref
        frame.push() # Push value
        if type(in_) is IntType:
            return self.jvm.emitIALOAD()
        # Add FloatType handling if needed
        # elif type(in_) is FloatType:
        #     return self.jvm.emitFALOAD()
        elif type(in_) is cgen.ArrayType or type(in_) is cgen.ClassType or type(in_) is StringType:
            return self.jvm.emitAALOAD()
        # Add BooleanType handling if needed (often uses BALOAD)
        # elif type(in_) is BooleanType:
        #     return self.jvm.emitBALOAD()
        else:
            raise IllegalOperandException(str(in_))

    def emitASTORE(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., arrayref, index, value -> ...

        # ASTORE pops value, index, arrayref. Net change: -3
        frame.pop() # Pop value
        frame.pop() # Pop index
        frame.pop() # Pop arrayref
        if type(in_) is IntType:
            return self.jvm.emitIASTORE()
        # Add FloatType handling if needed
        # elif type(in_) is FloatType:
        #     return self.jvm.emitFASTORE()
        elif type(in_) is cgen.ArrayType or type(in_) is cgen.ClassType or type(in_) is StringType:
            return self.jvm.emitAASTORE()
        # Add BooleanType handling if needed (often uses BASTORE)
        # elif type(in_) is BooleanType:
        #     return self.jvm.emitBASTORE()
        else:
            raise IllegalOperandException(str(in_))

    '''    generate the var directive for a local variable.
    *   @param in the index of the local variable.
    *   @param varName the name of the local variable.
    *   @param inType the type of the local variable.
    *   @param fromLabel the starting label of the scope where the variable is active.
    *   @param toLabel the ending label  of the scope where the variable is active.
    '''
    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        #in_: Int
        #varName: String
        #inType: Type
        #fromLabel: Int
        #toLabel: Int
        #frame: Frame

        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

    def emitREADVAR(self, name, inType, index, frame):
        #name: String
        #inType: Type
        #index: Int
        #frame: Frame
        #... -> ..., value

        frame.push()
        if type(inType) is IntType:
            return self.jvm.emitILOAD(index)
        # Add FloatType handling if needed
        # elif type(inType) is FloatType:
        #     return self.jvm.emitFLOAD(index)
        elif type(inType) is cgen.ArrayType or type(inType) is cgen.ClassType or type(inType) is StringType:
            return self.jvm.emitALOAD(index)
        # Add BooleanType handling if needed (often uses ILOAD)
        # elif type(inType) is BooleanType:
        #     return self.jvm.emitILOAD(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *   (This method seems unused or incomplete in the provided context)
    '''
    def emitREADVAR2(self, name, typ, frame):
        #name: String
        #typ: Type
        #frame: Frame
        #... -> ..., value

        #frame.push() # Should adjust stack based on the specific instruction
        raise IllegalOperandException(name) # Or implement as needed

    '''
    *   generate code to pop a value on top of the operand stack and store it to a block-scoped variable.
    *   @param name the symbol entry of the variable.
    '''
    def emitWRITEVAR(self, name, inType, index, frame):
        #name: String
        #inType: Type
        #index: Int
        #frame: Frame
        #..., value -> ...

        frame.pop()

        if type(inType) is IntType:
            return self.jvm.emitISTORE(index)
        # Add FloatType handling if needed
        # elif type(inType) is FloatType:
        #     return self.jvm.emitFSTORE(index)
        elif type(inType) is cgen.ArrayType or type(inType) is cgen.ClassType or type(inType) is StringType:
            return self.jvm.emitASTORE(index)
        # Add BooleanType handling if needed (often uses ISTORE)
        # elif type(inType) is BooleanType:
        #     return self.jvm.emitISTORE(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *   (This method seems unused or incomplete in the provided context)
    '''
    def emitWRITEVAR2(self, name, typ, frame):
        #name: String
        #typ: Type
        #frame: Frame
        #..., value -> ...

        #frame.pop() # Should adjust stack based on the specific instruction
        raise IllegalOperandException(name) # Or implement as needed

    ''' generate the field (static) directive for a class mutable or immutable attribute.
    *   @param lexeme the name of the attribute.
    *   @param in the type of the attribute.
    *   @param isStatic true if the field is static; false otherwise
    *   @param isFinal true in case of constant; false otherwise
    *   @param value the initial value (for static final fields)
    '''
    def emitATTRIBUTE(self, lexeme, in_, isStatic, isFinal, value):
        #lexeme: String
        #in_: Type
        #isStatic: Boolean
        #isFinal: Boolean
        #value: String or None

        if isStatic:
            # Assuming JasminCode.emitSTATICFIELD handles the value parameter
            return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), isFinal, value)
        else:
            # Assuming JasminCode.emitINSTANCEFIELD handles the value parameter (usually None for instance fields)
            return self.jvm.emitINSTANCEFIELD(lexeme, self.getJVMType(in_), isFinal, value)


    def emitGETSTATIC(self, lexeme, in_, frame):
        #lexeme: String (e.g., "ClassName/fieldName")
        #in_: Type
        #frame: Frame

        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    def emitPUTSTATIC(self, lexeme, in_, frame):
        #lexeme: String (e.g., "ClassName/fieldName")
        #in_: Type
        #frame: Frame
        # ..., value -> ...

        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    def emitGETFIELD(self, lexeme, in_, frame):
        #lexeme: String (e.g., "ClassName/fieldName")
        #in_: Type
        #frame: Frame
        # ..., objectref -> ..., value

        # Pops objectref, pushes value. Net change: 0
        # frame.pop() # Pop objectref - Handled implicitly by GETFIELD? Check Jasmin spec. Assuming it pops.
        # frame.push() # Push value - Handled implicitly by GETFIELD? Check Jasmin spec. Assuming it pushes.
        # Let's assume GETFIELD pops objectref and pushes value, so net is 0. Frame management might not be needed here.
        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme, in_, frame):
        #lexeme: String (e.g., "ClassName/fieldName")
        #in_: Type
        #frame: Frame
        # ..., objectref, value -> ...

        frame.pop() # Pop value
        frame.pop() # Pop objectref
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a static method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''
    def emitINVOKESTATIC(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type (MType)
        #frame: Frame

        typ = in_
        # Pop arguments from stack
        list(map(lambda x: frame.pop(), typ.partype))
        # Push return value if not void
        if not type(typ.rettype) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a special method
    *   @param frame the frame
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name) or None for constructor
    *   @param in the type descriptor of the method or None for constructor
    '''
    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        #lexeme: String or None
        #in_: Type (MType) or None
        #frame: Frame

        if not lexeme is None and not in_ is None:
            # Invoking a specific special method (e.g., superclass constructor)
            typ = in_
            list(map(lambda x: frame.pop(), typ.partype)) # Pop arguments
            frame.pop() # Pop objectref ('this')
            if not type(typ.rettype) is VoidType:
                frame.push() # Push return value
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            # Invoking the default constructor of the superclass (java/lang/Object)
            frame.pop() # Pop objectref ('this')
            return self.jvm.emitINVOKESPECIAL() # Calls Object.<init>()V


    ''' generate code to invoke a virtual method
    * @param lexeme the qualified name of the method(i.e., class-name/method-name)
    * @param in the type descriptor of the method.
    '''
    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type (MType)
        #frame: Frame

        typ = in_
        # Pop arguments
        list(map(lambda x: frame.pop(), typ.partype))
        # Pop objectref
        frame.pop()
        # Push return value if not void
        if not type(typ.rettype) is VoidType: # Check rettype, not the MType itself
            frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))

    '''
    *   generate ineg, fneg.
    *   @param in the type of the operands.
    '''
    def emitNEGOP(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., value -> ..., result

        # Negation does not change stack size
        if type(in_) is IntType:
            return self.jvm.emitINEG()
        # Add FloatType handling if needed
        # elif type(in_) is FloatType:
        #     return self.jvm.emitFNEG()
        else:
            # Handle other types or raise error
            raise IllegalOperandException(str(in_))


    def emitNOT(self, in_, frame):
        #in_: Type (assuming IntType for boolean 0/1)
        #frame: Frame
        # ..., value -> ..., result (1-value)

        # This implementation uses conditional jumps, an alternative is XOR with 1
        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        # If value is 0 (false), jump to label1
        result.append(self.jvm.emitIFEQ(label1)) # ifeq jumps if value == 0
        # Value was non-zero (true), push 0 (false)
        result.append(self.emitPUSHICONST(0, frame))
        frame.pop() # Correct stack after PUSHICONST(0) which pushes 1
        frame.push() # Push the actual 0
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        # Value was 0 (false), push 1 (true)
        result.append(self.emitPUSHICONST(1, frame))
        frame.pop() # Correct stack after PUSHICONST(1) which pushes 1
        frame.push() # Push the actual 1
        result.append(self.emitLABEL(label2, frame))
        # Stack size remains unchanged overall
        return ''.join(result)

    '''
    *   generate iadd, isub, fadd or fsub.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''
    def emitADDOP(self, lexeme, in_, frame):
        #lexeme: String ('+' or '-')
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        # Pops two operands, pushes one result. Net change: -1
        frame.pop()
        if lexeme == "+":
            if type(in_) is IntType:
                return self.jvm.emitIADD()
            # Add FloatType handling if needed
            # elif type(in_) is FloatType:
            #     return self.jvm.emitFADD()
            else:
                 raise IllegalOperandException(lexeme)
        elif lexeme == "-":
            if type(in_) is IntType:
                return self.jvm.emitISUB()
            # Add FloatType handling if needed
            # elif type(in_) is FloatType:
            #     return self.jvm.emitFSUB()
            else:
                 raise IllegalOperandException(lexeme)
        else:
            raise IllegalOperandException(lexeme)


    '''
    *   generate imul, idiv, fmul or fdiv.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitMULOP(self, lexeme, in_, frame):
        #lexeme: String ('*' or '/')
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        # Pops two operands, pushes one result. Net change: -1
        frame.pop()
        if lexeme == "*":
            if type(in_) is IntType:
                return self.jvm.emitIMUL()
            # Add FloatType handling if needed
            # elif type(in_) is FloatType:
            #     return self.jvm.emitFMUL()
            else:
                 raise IllegalOperandException(lexeme)
        elif lexeme == "/":
            if type(in_) is IntType:
                return self.jvm.emitIDIV()
            # Add FloatType handling if needed
            # elif type(in_) is FloatType:
            #     return self.jvm.emitFDIV()
            else:
                 raise IllegalOperandException(lexeme)
        else:
            raise IllegalOperandException(lexeme)


    def emitDIV(self, frame):
        #frame: Frame
        # ..., value1, value2 -> ..., result (integer division)

        # Pops two operands, pushes one result. Net change: -1
        frame.pop()
        return self.jvm.emitIDIV()

    def emitMOD(self, frame):
        #frame: Frame
        # ..., value1, value2 -> ..., result (remainder)

        # Pops two operands, pushes one result. Net change: -1
        frame.pop()
        return self.jvm.emitIREM()

    '''
    *   generate iand
    '''

    def emitANDOP(self, frame):
        #frame: Frame
        # ..., value1, value2 -> ..., result (bitwise AND)

        # Pops two operands, pushes one result. Net change: -1
        frame.pop()
        return self.jvm.emitIAND()

    '''
    *   generate ior
    '''
    def emitOROP(self, frame):
        #frame: Frame
        # ..., value1, value2 -> ..., result (bitwise OR)

        # Pops two operands, pushes one result. Net change: -1
        frame.pop()
        return self.jvm.emitIOR()

    # Logical AND (&&) and OR (||) require short-circuiting, handled differently
    # than bitwise AND/OR. Typically handled in the CodeGenerator visitor.

    def emitREOP(self, op, in_, frame):
        #op: String (e.g., ">", "<=", "==")
        #in_: Type (assuming IntType for comparison)
        #frame: Frame
        #..., value1, value2 -> ..., result (0 or 1)

        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        # Pops two operands, pushes one result. Net change: -1
        frame.pop()
        frame.pop()

        # Note: JVM comparison instructions jump if condition is met.
        # We want to push 1 if true, 0 if false.
        # So, we jump to labelF (push 0) if the condition is FALSE.
        if op == ">": # value1 > value2 -> if_icmple jumps if value1 <= value2
            result.append(self.jvm.emitIFICMPLE(labelF))
        elif op == ">=": # value1 >= value2 -> if_icmplt jumps if value1 < value2
            result.append(self.jvm.emitIFICMPLT(labelF))
        elif op == "<": # value1 < value2 -> if_icmpge jumps if value1 >= value2
            result.append(self.jvm.emitIFICMPGE(labelF))
        elif op == "<=": # value1 <= value2 -> if_icmpgt jumps if value1 > value2
            result.append(self.jvm.emitIFICMPGT(labelF))
        elif op == "!=": # value1 != value2 -> if_icmpeq jumps if value1 == value2
            result.append(self.jvm.emitIFICMPEQ(labelF))
        elif op == "==": # value1 == value2 -> if_icmpne jumps if value1 != value2
            result.append(self.jvm.emitIFICMPNE(labelF))
        else:
            raise IllegalOperandException(op)

        # If condition was TRUE (didn't jump to labelF)
        result.append(self.emitPUSHICONST(1, frame)) # Push 1 (true)
        frame.pop() # Correct stack after PUSHICONST
        frame.push() # Push the actual 1
        result.append(self.emitGOTO(labelO, frame)) # Jump to end

        # If condition was FALSE (jumped here)
        result.append(self.emitLABEL(labelF, frame))
        result.append(self.emitPUSHICONST(0, frame)) # Push 0 (false)
        frame.pop() # Correct stack after PUSHICONST
        frame.push() # Push the actual 0

        # End label
        result.append(self.emitLABEL(labelO, frame))
        return ''.join(result)

    def emitRELOP(self, op, in_, trueLabel, falseLabel, frame):
        #op: String
        #in_: Type (assuming IntType for comparison)
        #trueLabel: Int
        #falseLabel: Int
        #frame: Frame
        #..., value1, value2 -> ... (jumps to trueLabel or falseLabel)

        result = list()

        # Pops two operands. Net change: -2
        frame.pop()
        frame.pop()

        # Jump to trueLabel if the condition is met
        if op == ">": # value1 > value2
            result.append(self.jvm.emitIFICMPGT(trueLabel))
        elif op == ">=": # value1 >= value2
            result.append(self.jvm.emitIFICMPGE(trueLabel))
        elif op == "<": # value1 < value2
            result.append(self.jvm.emitIFICMPLT(trueLabel))
        elif op == "<=": # value1 <= value2
            result.append(self.jvm.emitIFICMPLE(trueLabel))
        elif op == "!=": # value1 != value2
            result.append(self.jvm.emitIFICMPNE(trueLabel))
        elif op == "==": # value1 == value2
            result.append(self.jvm.emitIFICMPEQ(trueLabel))
        else:
            raise IllegalOperandException(op)

        # If condition not met, fall through or jump to falseLabel
        result.append(self.emitGOTO(falseLabel, frame)) # Explicit jump to falseLabel
        return ''.join(result)

    '''   generate the method directive for a function.
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
    '''

    def emitMETHOD(self, lexeme, in_, isStatic, frame):
        #lexeme: String
        #in_: Type (MType)
        #isStatic: Boolean
        #frame: Frame

        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

    '''   generate the end directive for a function.
    '''
    def emitENDMETHOD(self, frame):
        #frame: Frame

        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    def getConst(self, ast):
        #ast: Literal
        # This seems like a helper potentially used by CodeGenerator,
        # returning value and type.
        if type(ast) is IntLiteral:
            return (str(ast.value), IntType())
        # Add other literal types (FloatLiteral, StringLiteral, etc.)
        # elif type(ast) is FloatLiteral:
        #     return (str(ast.value), FloatType())
        # elif type(ast) is StringLiteral:
        #     return (ast.value, StringType()) # Value itself, not str()
        else:
             raise IllegalOperandException(str(type(ast)))


    '''   generate code to initialize a local array variable.<p>
    *   @param index the index of the local variable.
    *   @param in the type of the local array variable.
    '''
    # This method seems intended but not fully defined or used in provided snippets.
    # Implementation would involve NEWARRAY/ANEWARRAY and storing the reference.

    '''   generate code to initialize local array variables.
    *   @param in the list of symbol entries corresponding to local array variable.
    '''
    # Similar to the above, seems intended but not defined/used.

    '''   generate code to jump to label if the value on top of operand stack is true.<p>
    *   ifgt label (or ifne label)
    *   @param label the label where the execution continues if the value on top of stack is true.
    '''
    def emitIFTRUE(self, label, frame):
        #label: Int
        #frame: Frame
        # ..., value -> ...

        frame.pop()
        # ifne jumps if value is non-zero (true)
        return self.jvm.emitIFNE(label)

    '''
    *   generate code to jump to label if the value on top of operand stack is false.<p>
    *   ifle label (or ifeq label)
    *   @param label the label where the execution continues if the value on top of stack is false.
    '''
    def emitIFFALSE(self, label, frame):
        #label: Int
        #frame: Frame
        # ..., value -> ...

        frame.pop()
        # ifeq jumps if value is zero (false)
        return self.jvm.emitIFEQ(label)

    def emitIFICMPGT(self, label, frame):
        #label: Int
        #frame: Frame
        # ..., value1, value2 -> ...

        frame.pop()
        frame.pop()
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label, frame):
        #label: Int
        #frame: Frame
        # ..., value1, value2 -> ...

        frame.pop()
        frame.pop()
        return self.jvm.emitIFICMPLT(label)

    '''   generate code to duplicate the value on the top of the operand stack.<p>
    *   Stack:<p>
    *   Before: ...,value1<p>
    *   After:  ...,value1,value1<p>
    '''
    def emitDUP(self, frame):
        #frame: Frame

        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame):
        #frame: Frame
        # ..., value -> ...

        frame.pop()
        return self.jvm.emitPOP()

    '''   generate code to exchange an integer on top of stack to a floating-point number.
    '''
    def emitI2F(self, frame):
        #frame: Frame
        # ..., intValue -> ..., floatValue

        # Stack size remains the same
        return self.jvm.emitI2F()

    # Add F2I, etc., if needed

    ''' generate code to return.
    *   <ul>
    *   <li>ireturn if the type is IntegerType or BooleanType
    *   <li>freturn if the type is RealType
    *   <li>areturn if the type is ArrayType, ClassType, StringType
    *   <li>return if the type is void
    *   </ul>
    *   @param in the type of the returned expression.
    '''

    def emitRETURN(self, in_, frame):
        #in_: Type
        #frame: Frame

        if type(in_) is IntType: # Add BooleanType check if distinct
            frame.pop()
            return self.jvm.emitIRETURN()
        # Add FloatType handling if needed
        # elif type(in_) is FloatType:
        #     frame.pop()
        #     return self.jvm.emitFRETURN()
        elif type(in_) is VoidType:
            # No value to pop for void return
            return self.jvm.emitRETURN()
        elif type(in_) is cgen.ArrayType or type(in_) is cgen.ClassType or type(in_) is StringType:
             frame.pop()
             return self.jvm.emitARETURN()
        else:
            raise IllegalOperandException(str(in_))


    ''' generate code that represents a label
    *   @param label the label
    *   @return code Label<label>:
    '''
    def emitLABEL(self, label, frame):
        #label: Int
        #frame: Frame

        return self.jvm.emitLABEL(label)

    ''' generate code to jump to a label
    *   @param label the label
    *   @return code goto Label<label>
    '''
    def emitGOTO(self, label, frame):
        #label: Int
        #frame: Frame

        return self.jvm.emitGOTO(str(label)) # Ensure label is string for JasminCode

    ''' generate some starting directives for a class.<p>
    *   .source YourClassName.java<p>
    *   .class public YourClassName<p>
    *   .super java/lang/Object<p> or specified parent
    '''
    def emitPROLOG(self, name, parent):
        #name: String
        #parent: String

        result = list()
        # Assuming MiniGo source files might not map directly to .java, use .j or .minigo?
        # Let's stick to the example's .java convention for now.
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        # Use "java/lang/Object" as the default superclass if parent is empty or None
        result.append(self.jvm.emitSUPER("java/lang/Object" if not parent else parent))
        return ''.join(result)

    def emitLIMITSTACK(self, num):
        #num: Int

        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):
        #num: Int

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        # Writes the buffer content to the output file.
        try:
            file = open(self.filename, "w")
            file.write(''.join(self.buff))
            file.close()
        except IOError as e:
            # Handle file writing errors appropriately
            print(f"Error writing file {self.filename}: {e}")
            raise e # Re-raise the exception if needed


    ''' print out the code to screen
    *   @param in the code to be printed out
    '''
    def printout(self, in_):
        #in_: String
        # Appends the generated Jasmin code string to the buffer.
        self.buff.append(in_)

    def clearBuff(self):
        self.buff.clear()

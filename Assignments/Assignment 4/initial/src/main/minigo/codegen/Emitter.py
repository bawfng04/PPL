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

class ClassType:
    def __init__(self, name):
        #value: Id
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
            return "[" * len(inType.dimens) + self.getJVMType(inType.eleType)
        elif typeIn is MType:
            return (
                "("
                + "".join(list(map(lambda x: self.getJVMType(x), inType.partype)))
                + ")"
                + self.getJVMType(inType.rettype)
            )
        # New branch: if the type is an Id, treat it as a class type
        elif typeIn.__name__ == "Id":
            return "L" + inType.name + ";"
        elif typeIn is cgen.ClassType:
            return "L" + inType.name + ";"
        else:
            return str(typeIn)

    def getFullType(inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "int"
        elif typeIn is cgen.StringType:
            return "java/lang/String"
        elif typeIn is VoidType:
            return "void"

    def emitPUSHICONST(self, in_, frame):
        # in: Int or Sring
        # frame: Frame
        frame.push();
        if type(in_) is int:
            i = in_
            if i >= -1 and i <=5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
        elif type(in_) is str:
            if in_ == "true":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "false":
                return self.emitPUSHICONST(0, frame)
            else:
                return self.emitPUSHICONST(int(in_), frame)

    def emitPUSHFCONST(self, in_, frame):
        # in_: String
        # frame: Frame

        f = float(in_)
        frame.push()
        if f == 0.0 or f == 1.0 or f == 2.0:
            return self.jvm.emitFCONST("{0:.1f}".format(f))
        else:
            return self.jvm.emitLDC(str(f))

    '''
    *    generate code to push a constant onto the operand stack.
    *    @param in the lexeme of the constant
    *    @param typ the type of the constant
    '''
    def emitPUSHCONST(self, in_, typ, frame):
        # in_: String
        # typ: Type
        # frame: Frame

        if type(typ) is IntType or type(typ) is BoolType:
            return self.emitPUSHICONST(in_, frame)
        elif type(typ) is StringType:
            frame.push()
            return self.jvm.emitLDC(in_)
        else:
            raise IllegalOperandException(in_)

    ##############################################################

    def emitALOAD(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., arrayref, index -> ..., value

        frame.pop()
        if type(in_) is IntType:
            return self.jvm.emitIALOAD()
        elif type(in_) is FloatType:
            return self.jvm.emitFALOAD()
        elif type(in_) is BoolType:
            return self.jvm.emitBALOAD()
        elif type(in_) is StringType or type(in_) is cgen.ClassType or type(in_) is cgen.ArrayType:
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(f"Unsupported type for ALOAD: {type(in_)}")

    def emitASTORE(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., arrayref, index, value -> ...

        frame.pop()
        frame.pop()
        frame.pop()
        if type(in_) is IntType:
            return self.jvm.emitIASTORE()
        elif type(in_) is FloatType:
            return self.jvm.emitFASTORE()
        elif type(in_) is BoolType:
            return self.jvm.emitBASTORE()
        elif type(in_) is StringType or type(in_) is cgen.ClassType or type(in_) is cgen.ArrayType:
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(f"Unsupported type for ASTORE: {type(in_)}")

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
        # name: String, inType: Type, index: Int, frame: Frame
        # ... -> ..., value
        frame.push()
        if type(inType) is IntType or type(inType) is BoolType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is FloatType:
            return self.jvm.emitFLOAD(index)
        # Now also check for Id type (unresolved identifier), treat as reference type
        elif (
            type(inType) is StringType
            or type(inType) is cgen.ClassType
            or type(inType) is cgen.ArrayType
            or type(inType).__name__ == "Id"
        ):
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
        # Determine the JVM type code
        jvmType = self.getJVMType(inType)
        # Choose the store instruction based on the type
        if jvmType in ["I", "Z"]:  # integers, booleans
            return f"\tistore {index}\n"
        elif jvmType == "F":
            return f"\tfstore {index}\n"
        elif jvmType.startswith("L") or jvmType.startswith("["):  # reference types
            return f"\tastore {index}\n"
        else:
            # In case it's unhandled, we return a default astore.
            return f"\tastore {index}\n"

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
    def emitATTRIBUTE(self, lexeme, in_, isStatic, isFinal, value):
        # lexeme: String
        # in_: Type
        # isFinal: Boolean
        # value: String
        if isStatic:
            return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), isFinal, value)
        else:
            return self.jvm.emitFIELD(lexeme, self.getJVMType(in_), isFinal, value)

    def emitGETSTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    def emitPUTSTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    def emitGETFIELD(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()
        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a static method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''
    def emitINVOKESTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        if not type(typ.rettype) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a special method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''
    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        # lexeme: String
        # in_: Type
        # frame: Frame

        if not lexeme is None and not in_ is None:
            typ = in_
            list(map(lambda x: frame.pop(), typ.partype))
            frame.pop()
            if not type(typ.rettype) is VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()

    ''' generate code to invoke a virtual method
    * @param lexeme the qualified name of the method(i.e., class-name/method-name)
    * @param in the type descriptor of the method.
    '''
    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        frame.pop()
        if not type(typ) is VoidType:
            frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))

    '''
    *   generate ineg, fneg.
    *   @param in the type of the operands.
    '''
    def emitNEGOP(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., value -> ..., result

        if type(in_) is IntType:
            return self.jvm.emitINEG()
        else:
            return self.jvm.emitFNEG()

    def emitNOT(self, in_, frame):
        # in_: Type
        # frame: Frame

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(label1, frame))
        result.append(self.emitPUSHCONST("true", in_, frame))
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHCONST("false", in_, frame))
        result.append(self.emitLABEL(label2, frame))
        return ''.join(result)

    '''
    *   generate iadd, isub, fadd or fsub.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''
    def emitADDOP(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "+":
            if type(in_) is IntType:
                return self.jvm.emitIADD()
            else:
                return self.jvm.emitFADD()
        else:
            if type(in_) is IntType:
                return self.jvm.emitISUB()
            else:
                return self.jvm.emitFSUB()

    '''
    *   generate imul, idiv, fmul or fdiv.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitMULOP(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "*":
            if type(in_) is IntType:
                return self.jvm.emitIMUL()
            else:
                return self.jvm.emitFMUL()
        else:
            if type(in_) is IntType:
                return self.jvm.emitIDIV()
            else:
                return self.jvm.emitFDIV()

    def emitDIV(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIDIV()

    def emitMOD(self, frame):
        # frame: Frame

        frame.pop()
        return "\tirem\n"
        # return self.jvm.emitIREM()

    '''
    *   generate iand
    '''

    def emitANDOP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIAND()

    '''
    *   generate ior
    '''
    def emitOROP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIOR()

    def emitREOP(self, op, in_, frame):
        # op: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop()
        frame.pop()
        if type(in_) is IntType:
            if op == ">":
                result.append(self.jvm.emitIFICMPLE(labelF))
            elif op == ">=":
                result.append(self.jvm.emitIFICMPLT(labelF))
            elif op == "<":
                result.append(self.jvm.emitIFICMPGE(labelF))
            elif op == "<=":
                result.append(self.jvm.emitIFICMPGT(labelF))
            elif op == "!=":
                result.append(self.jvm.emitIFICMPEQ(labelF))
            elif op == "==":
                result.append(self.jvm.emitIFICMPNE(labelF))
        elif type(in_) is FloatType:
            if op in [">", ">=", "<", "<=", "==", "!="]:
                result.append(self.jvm.emitFCMPG())  # Emit FCMPG for FloatType comparison
            if op == ">":
                result.append(self.jvm.emitIFLE(labelF))
            elif op == ">=":
                result.append(self.jvm.emitIFLT(labelF))
            elif op == "<":
                result.append(self.jvm.emitIFGE(labelF))
            elif op == "<=":
                result.append(self.jvm.emitIFGT(labelF))
            elif op == "!=":
                result.append(self.jvm.emitIFEQ(labelF))
            elif op == "==":
                result.append(self.jvm.emitIFNE(labelF))

        # Push 1 (true) for the true case
        result.append(self.emitPUSHCONST("1", IntType(), frame))
        frame.pop()
        result.append(self.emitGOTO(labelO, frame))

        # Add the false label and push 0 (false)
        result.append(self.emitLABEL(labelF, frame))
        result.append(self.emitPUSHCONST("0", IntType(), frame))

        # Add the ending label
        result.append(self.emitLABEL(labelO, frame))
        return "".join(result)

    def emitRELOP(self, op, in_, trueLabel, falseLabel, frame):
        # op: String
        # in_: Type
        # trueLabel: Int
        # falseLabel: Int
        # frame: Frame
        # ..., value1, value2 -> ..., result

        result = list()

        frame.pop()
        frame.pop()
        if op == ">":
            result.append(self.jvm.emitIFICMPLE(falseLabel))
            result.append(self.emitGOTO(trueLabel))
        elif op == ">=":
            result.append(self.jvm.emitIFICMPLT(falseLabel))
        elif op == "<":
            result.append(self.jvm.emitIFICMPGE(falseLabel))
        elif op == "<=":
            result.append(self.jvm.emitIFICMPGT(falseLabel))
        elif op == "!=":
            result.append(self.jvm.emitIFICMPEQ(falseLabel))
        elif op == "==":
            result.append(self.jvm.emitIFICMPNE(falseLabel))
        result.append(self.jvm.emitGOTO(trueLabel))
        return ''.join(result)

    '''   generate the method directive for a function.
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
    '''

    def emitMETHOD(self, lexeme, in_, isStatic, frame):
        # lexeme: String
        # in_: Type
        # isStatic: Boolean
        # frame: Frame

        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

    '''   generate the end directive for a function.
    '''
    def emitENDMETHOD(self, frame):
        # frame: Frame

        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    def getConst(self, ast):
        # ast: Literal
        if type(ast) is IntLiteral:
            return (str(ast.value), IntType())

    '''   generate code to initialize a local array variable.<p>
    *   @param index the index of the local variable.
    *   @param in the type of the local array variable.
    '''

    '''   generate code to initialize local array variables.
    *   @param in the list of symbol entries corresponding to local array variable.
    '''

    '''   generate code to jump to label if the value on top of operand stack is true.<p>
    *   ifgt label
    *   @param label the label where the execution continues if the value on top of stack is true.
    '''
    def emitIFTRUE(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFGT(label)

    '''
    *   generate code to jump to label if the value on top of operand stack is false.<p>
    *   ifle label
    *   @param label the label where the execution continues if the value on top of stack is false.
    '''
    def emitIFFALSE(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFLE(label)

    def emitIFICMPGT(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPLT(label)

    '''   generate code to duplicate the value on the top of the operand stack.<p>
    *   Stack:<p>
    *   Before: ...,value1<p>
    *   After:  ...,value1,value1<p>
    '''
    def emitDUP(self, frame):
        # frame: Frame

        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitPOP()

    '''   generate code to exchange an integer on top of stack to a floating-point number.
    '''
    def emitI2F(self, frame):
        # frame: Frame

        return self.jvm.emitI2F()

    ''' generate code to return.
    *   <ul>
    *   <li>ireturn if the type is IntegerType or BooleanType
    *   <li>freturn if the type is RealType
    *   <li>return if the type is null
    *   </ul>
    *   @param in the type of the returned expression.
    '''

    def emitRETURN(self, in_, frame):
        # in_: Type
        # frame: Frame

        if type(in_) is IntType or type(in_) is BoolType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is FloatType:
            frame.pop()
            return self.jvm.emitFRETURN()
        elif type(in_) is StringType or type(in_) is cgen.ClassType or type(in_) is cgen.ArrayType:
            frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()
        else:
            raise IllegalOperandException(f"Unsupported type for RETURN: {type(in_)}")

    ''' generate code that represents a label
    *   @param label the label
    *   @return code Label<label>:
    '''
    def emitLABEL(self, label, frame):
        # label: Int
        # frame: Frame

        return self.jvm.emitLABEL(label)

    ''' generate code to jump to a label
    *   @param label the label
    *   @return code goto Label<label>
    '''
    def emitGOTO(self, label, frame):
        # label: Int
        # frame: Frame

        return self.jvm.emitGOTO(str(label))

    ''' generate some starting directives for a class.<p>
    *   .source MPC.CLASSNAME.java<p>
    *   .class public MPC.CLASSNAME<p>
    *   .super java/lang/Object<p>
    '''
    def emitPROLOG(self, name, parent):
        # name: String
        # parent: String

        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER("java/land/Object" if parent == "" else parent))
        return ''.join(result)

    def emitLIMITSTACK(self, num):
        # num: Int

        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):
        # num: Int

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    ''' print out the code to screen
    *   @param in the code to be printed out
    '''
    def printout(self, in_):
        # in_: String

        self.buff.append(in_)

    def clearBuff(self):
        self.buff.clear()

    def emitNEWARRAY(self, in_, frame):
        # in_: Type
        # frame: Frame

        if type(in_) is IntType:
            return self.jvm.emitNEWARRAY("int")
        elif type(in_) is FloatType:
            return self.jvm.emitNEWARRAY("float")
        elif type(in_) is BoolType:
            return self.jvm.emitNEWARRAY("boolean")
        else:
            raise IllegalOperandException(f"Unsupported type for NEWARRAY: {type(in_)}")

    def emitANEWARRAY(self, in_, frame):
        # in_: Type
        # frame: Frame
        if type(in_) is StringType or type(in_) is cgen.ClassType or type(in_) is cgen.ArrayType:
            return self.jvm.emitANEWARRAY(self.getJVMType(in_))
        else:
            raise IllegalOperandException(f"Unsupported type for ANEWARRAY: {type(in_)}")

    def emitNEW(self, lexeme, frame):
        frame.push()
        return self.jvm.emitNEW(lexeme)

    def emitPUSHNULL(self, frame):
        frame.push()
        return self.jvm.emitPUSHNULL()

    def emitMULTIANEWARRAY(self, arrayType: ArrayType, frame) -> str:
        # Get the JVM type descriptor for the array
        typeDescriptor = self.getJVMType(arrayType)
        # Get the number of dimensions
        numDimensions = len(arrayType.dimens)
        # Emit the multianewarray instruction
        return f"\tmultianewarray {typeDescriptor} {numDimensions}\n"
    # def emitObjectInit(self):
    #     frame = Frame("<init>", VoidType())
    #     self.emit.printout(
    #         self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame)
    #     )  # Bắt đầu định nghĩa phương thức <init>
    #     # sinh ra mã => .method public <init>()V
    #     frame.enterScope(True)  # Mỗi hàm có 1 frame riêng, và mỗi frame có 1 scope riêng, nên dùng enterScope để vào scope của frame này

    #     self.emit.printout(
    #         self.emit.emitVAR(
    #             frame.getNewIndex(),
    #             "this",
    #             ClassType(self.className),
    #             frame.getStartLabel(),
    #             frame.getEndLabel(),
    #             frame,
    #         )
    #     )  # Tạo biến "this" trong phương thức <init>
    #     # sinh ra mã => .var 0 is this LMiniGoClass; from Label0 to Label1

    #     self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
    #     # sinh ra mã => Label0: (nơi body method bắt đầu)

    #     self.emit.printout(
    #         self.emit.emitREADVAR("this", ClassType(self.className), 0, frame)
    #     )
    #     # sinh ra mã => aload_0 (đưa biến this vào stack)

    #     self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
    #     # sinh ra mã => invokespecial java/lang/Object/<init>()V (gọi hàm khởi tạo của class cha là Object)

    #     self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
    #     # sinh ra mã => Label1: (nơi body method kết thúc)

    #     self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
    #     # sinh ra mã => return (trả về từ hàm khởi tạo này)

    #     self.emit.printout(self.emit.emitENDMETHOD(frame))
    #     # sinh ra mã limit stack 1, limit locals 1, end method (kết thúc định nghĩa phương thức <init>)

    #     frame.exitScope()

    # def emitObjectCInit(self, ast: Program, env):
    #     frame = Frame("<clinit>", VoidType())
    #     self.emit.printout(self.emitMETHOD("<clinit>", MType([], VoidType()), True, frame))
    #     frame.enterScope(True)
    #     self.emit.printout(self.emitLABEL(frame.getStartLabel(), frame))

    #     env["frame"] = frame

    #     # Initialize global variables
    #     for decl in ast.decl:
    #         if isinstance(decl, VarDecl) and decl.varInit:
    #             rhsCode, rhsType = self.visit(decl.varInit, env)
    #             self.emit.printout(rhsCode)
    #             self.emit.printout(self.emitPUTSTATIC(f"{self.className}/{decl.varName}", decl.varType, frame))

    #     self.emit.printout(self.emitLABEL(frame.getEndLabel(), frame))
    #     self.emit.printout(self.emitRETURN(VoidType(), frame))
    #     self.emit.printout(self.emitENDMETHOD(frame))
    #     frame.exitScope()

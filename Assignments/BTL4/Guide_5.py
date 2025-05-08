from Utils import *
# from StaticCheck import *
# from StaticError import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *
from typing import List, Tuple


class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.function = None
        self.list_function = []
        self.arrayCell = None
        self.arrayCellType = None
        self.list_type = {}
        self.struct: StructType = None

    def init(self):
        mem = [
            Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)),
             Symbol("putLn", MType([], VoidType()), CName("io", True)),
            Symbol("getInt", MType([], IntType()), CName("io", True)),
            Symbol("getFloat", MType([], FloatType()), CName("io", True)),
            Symbol("getString", MType([], StringType()), CName("io", True)),
            Symbol("getBool", MType([], BoolType()), CName("io", True))
        ]
        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)
       

    def visitProgram(self, ast: Program, c):
   
        # OLDCODE
        # ... 
        # ...

        for item in self.list_type.values():
            self.struct = item
            self.emit = Emitter(self.path + "/" + item.name + ".j")
            self.visit(item, {
                'env': env['env']
            })
        return env



    def visitStructType(self, ast: StructType, o):
        self.emit.printout(self.emit.emitPROLOG("TODO", "java.lang.Object")) # khởi tạo đầu file mô tả tên
        # VD ở visitProgram: self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))


        # .implements name
        # VD sau dùng cho đoạn for bên dưới:
            #INPUT:
                # type Worker interface { 
                #     study(); 
                #     play(); 
                # }
                # type PPL4 struct {number int;}
                # func (p PPL4) study() { putInt(p.number); }
                # func (p PPL4) play()  { putInt(p.number + 5); }
            #CODE OUTPUT:
                # .source PPL4.java
                # .class public  PPL4
                # .super java.lang.Object    ---------------> khúc này trở lên là emitPROLOG
                # .implements Worker         --------------------> lệnh implement được nằm ở đây nè
                # .field public number I
                # .method public <init>(I)V
                # .......
                # .method public <init>()V
                # .......
                # .method public study()V
                # .......
                # .method public play()V
                # .......

        # ***LƯU Ý***: ..... là còn code ở đó, code VD ở trên nằm trong file PPL4.j (tên struct được khai báo ở trên), tương tự là có file Worker.j

        for item in self.list_type.values(): # Lặp qua các type đc khai báo(interface/struct)
            # Lệnh if - tìm interface mà struct này đang implement(ast là struct mà mình visit), hàm checkType sẽ check 1 struct implement đc interface
            if "TODO" and self.checkType(item, ast, [(InterfaceType, StructType)]): 
                self.emit.printout("TODO") # Sinh ra đoạn .implement ___ như ở ví dụ bên trên.

        for item in ast.elements:
            #**Lưu ý: item có type là Tuple[str,Type] -> nhờ dùng item[0], item[1]
            #Chỗ này mình tạo code cho attribute cho struct nên mã code VD sẽ là:
                # .field public name Ljava/lang/String;
                # .field public age I
            # với input:
                #  type Person struct {
                #     name string;
                #     age int;
                # }
            #từ đó mà điền tham số cho hàm emit cho phù hợp nhé, nhớ đọc hàm này trong Emiter.py
            self.emit.printout(self.emit.emitATTRIBUTE("TODO", item[1], False, False, False)) # danh sách các thuộc tính cần khởi tạo
        
        # khởi tạo Method contructor có giá trị parram (khác với constructor rỗng nha)
        #code VD cho hàm constructor cho class PPL4 ở phía trên:      
                # type PPL4 struct {number int;}

                # .method public <init>(I)V
                # .var 0 is this LPPL4; from Label0 to Label1  -------------------> param mặc định "this"
                # Label0:
                # 	aload_0
                # 	invokespecial java/lang/Object/<init>()V
                # .var 1 is number I from Label0 to Label1 --------> param đầu tiên number int;
                # Label2:    ------------------> Label2 đếm Label3 là khúc Block(..) bên dưới, bên trong là phép gán attribute
                # 	aload_0
                # 	iload_1
                # 	putfield PPL4/number I
                # Label3:
                # Label1:
                # 	return
                # .limit stack 2
                # .limit locals 2
                # .end method
        self.visit(MethodDecl(None, None, FuncDecl("<init>", [ParamDecl("TODO") for item in ast.elements], VoidType(),
                                                   
                            Block(["TODO" for item in ast.elements]))), o) 
        # Hãy xem bên trong giống như các phép gán this.fieldName = fieldName ứng với mỗi item trong ast.elements => Dùng Assign và FieldAcess


        # khởi tạo Method contructor rỗng
        # .method public <init>()V
        # .var 0 is this LPPL4; from Label0 to Label1
        # Label0:
        #     aload_0
        #     invokespecial java/lang/Object/<init>()V
        # Label2:
        # Label3:
        # Label1:
        #     return
        # .limit stack 1
        # .limit locals 1
        # .end method
        self.visit(MethodDecl(None, None, FuncDecl("TODO"), o))


        # duyệt qua method
        for item in ast.methods: self.visit(item, o)
        self.emit.printout("TODO") # kết thúc khai báo của struct

    
    def visitMethodDecl(self, ast: MethodDecl, o):
        self.function = ast.fun
        frame = Frame(ast.fun.name, ast.fun.retType)
        mtype = "TODO" # giống visitFuncDecl thôi
        
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype,False, frame))
        frame.enterScope(True) #vào trong thân method giống visitFuncDecl thôi
        # biến this
        self.emit.printout("TODO") # emitVAR cho biến this với inType là Id(...)
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # contructor thì hơi đặt biệt cần gọi đến class cha của nó .super java.lang.Object
        if ast.receiver is None:
            self.emit.printout(self.emit.emitREADVAR("this", Id("TODO"), 0, frame))  
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  

        env['env'] = [[]] + env['env']
        # cập nhật param và duyệt block
        env = "TODO"   #Này duyệt và cập nhật param giống visitFuncDecl 

        self.visit("TODO") #duyệt block thân hàm


        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.fun.retType) is VoidType:
            self.emit.printout("TODO")  # trường hợp void phải có return tránh trường hợp ko có return trong block
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    


    def visitInterfaceType(self, ast: InterfaceType, o):
        # type Course interface {study();}

        # .source Course.java
        # .class public interface Course
        # .super java.lang.Object

        # .method public abstract study()V
        # .end method

        #Giống struct type thôi nhưng đơn giản hơn
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object", True))
        for item in ast.methods:
            #TODO sinh mẫ cho các prototype, nhớ này là abstract method
            #TODO end method
            pass
        self.emit.printout(self.emit.emitEPILOG())

    def visitFieldAccess(self, ast:FieldAccess, o: dict) -> tuple[str, Type]:
        code, typ = "TODO" # Mình cần biết được code của receiver trả về, và ret type của receive
        #Sau đó dùng typ để lấy Type tương ứng trong self.list_type
        #Sau đó lấy field tương ứng ra (nhớ xài ast.field)
        return code + self.emit.emitGETFIELD("TODO"), "TODO" # -> tuple[str, Type], trong đó Type là kiểu trả về của field

    def visitMethCall(self, ast: MethCall, o: dict) -> tuple[str, Type]:
    
        # 1. Tạo mã cho receiver (đối tượng mà phương thức được gọi).
        code, typ = self.visit(ast.receiver, o)

        # 2. Lấy thông tin kiểu đầy đủ của receiver từ self.list_type.
        # 'typ' có thể chỉ là một Id (tên kiểu), cần lookup để lấy StructType hoặc InterfaceType.
        if isinstance(typ, Id):
            typ = self.list_type.get(typ.name)

        # 3. Kiểm tra xem lời gọi phương thức này có phải là một statement hay một expression
        is_stmt = o.pop("stmt", False)

        # 4. Tạo mã cho các đối số của phương thức.
        for arg in ast.args:
            arg_code, _ = "TODO"
            code += arg_code

        returnType = None
        # 5. Xử lý trường hợp receiver là một StructType (gọi phương thức thông thường).
        if isinstance(typ, StructType):
            # Tìm kiếm phương thức trong danh sách các phương thức của struct dựa trên tên.
            method = "TODO"  # có thể dùng hàm next
            
            # Tạo MType (Method Type) cho lời gọi phương thức.
            # Lấy kiểu của các tham số và kiểu trả về từ FuncDecl của phương thức.
            mtype = MType(["TODO"], method.fun.retType)
            returnType = method.fun.retType
            # Tạo mã bytecode để gọi phương thức ảo (invokevirtual).
            # invokevirtual được sử dụng cho các phương thức instance.
            code += self.emit.emitINVOKEVIRTUAL("TODO", mtype, o['frame'])
            
                
                

        # 6. Xử lý trường hợp receiver là một InterfaceType (gọi phương thức interface).
        elif isinstance(typ, InterfaceType):
            # Tìm kiếm phương thức trong danh sách các phương thức của interface dựa trên tên.
            method = "TODO" # có thể dùng hàm next
            
            # Tạo MType cho lời gọi phương thức interface.
            mtype = MType("TODO", method.retType)
            returnType = method.retType
            # Tạo mã bytecode để gọi phương thức interface (invokeinterface).
            code += self.emit.emitINVOKEINTERFACE(f"TODO", mtype, o['frame'])
        
           
        # 7. Nếu lời gọi phương thức là một statement, in mã ra mà không trả về giá trị.
        if is_stmt:
            self.emit.printout(code)
            return o

        # 8. Nếu lời gọi phương thức là một expression, trả về mã và kiểu trả về của phương thức.
        return code, returnType

    def visitStructLiteral(self, ast: StructLiteral, o: dict) -> tuple[str, Type]:
        # Gợi ý:
        # 1. Sử dụng self.emit.emitNEW để tạo một instance mới của struct (ast.name).
        # 2. Sử dụng self.emit.emitDUP để nhân đôi tham chiếu đến instance vừa tạo (cho việc gọi constructor).
        code = "TODO"
        code += self.emit.emitDUP(o['frame'])
        list_type = []
        for item in ast.elements:
            # Xử lý từng thành phần (field và giá trị) của struct literal.
            # Gợi ý:
            # 1. Gọi self.visit(item[1], o) để lấy mã và kiểu của giá trị khởi tạo (item[1]).
            # 2. Thêm mã này vào 'code'.
            # 3. Thêm kiểu của giá trị khởi tạo vào 'list_type'.
            c, t = self.visit(item[1], o)
            code += "TODO"
            list_type += "TODO"

        # Gọi constructor của struct.
        # Gợi ý:
        # 1. Tạo MType cho constructor dựa trên 'list_type' (kiểu của các tham số).
        # 2. Sử dụng self.emit.emitINVOKESPECIAL để gọi constructor của struct (ast.name/<init>).
        code += self.emit.emitINVOKESPECIAL(o['frame'], "TODO", MType("TODO") if len(ast.elements) else MType("TODO"))
        return code, Id(ast.name)

    def visitNilLiteral(self, ast: NilLiteral, o: dict) -> tuple[str, Type]:
        # Gợi ý:
        # 1. Sử dụng self.emit.emitPUSHNULL để đẩy giá trị null lên stack.
        code = "TODO"
        # Trả về mã và kiểu của 'nil'.
        # Gợi ý:
        # 1. Kiểu của 'nil' thường là một kiểu tham chiếu đặc biệt hoặc có thể được biểu diễn bằng một Id rỗng.
        return code, Id("")

        
def checkType(self, LSH_type: Type, RHS_type: Type, list_type_permission: List[Tuple[Type, Type]] = []) -> bool:
        # Kiểm tra xem hai kiểu có tương thích hay không.
        # Gợi ý:
        # 1. Xử lý trường hợp RHS_type là StructType có tên rỗng (thường là nil literal).
        if type(RHS_type) == StructType and RHS_type.name == "":
            #  nil có thể gán cho InterfaceType, StructType hoặc Id.
            return "TODO"

        # Resolve Id types thành kiểu thực tế từ self.list_type.
        LSH_type = self.lookup("TODO", self.list_type.values(), lambda x: "TODO") if isinstance(LSH_type, Id) else LSH_type
        RHS_type = self.lookup("TODO", self.list_type.values(), lambda x: "TODO") if isinstance(RHS_type, Id) else RHS_type

        #  Kiểm tra các trường hợp dựa trên danh sách các cặp kiểu cho phép.
        if (type(LSH_type), type(RHS_type)) in list_type_permission:
            # Xử lý kiểm tra tương thích giữa InterfaceType và StructType.
            if isinstance(LSH_type, InterfaceType) and isinstance(RHS_type, StructType):
                #  Kiểm tra xem StructType có implement tất cả các phương thức của InterfaceType không.
                return all(
                    any(
                        # So sánh tên, kiểu trả về và kiểu tham số của phương thức.
                        struct_methods.fun.name == inteface_method.name and
                        self.checkType(struct_methods.fun.retType, inteface_method.retType) and
                        len(struct_methods.fun.params) == len(inteface_method.params) and
                        reduce(
                            lambda x, i: x and self.checkType(struct_methods.fun.params[i].parType, inteface_method.params[i]),
                            range(len(struct_methods.fun.params)),
                            True
                        )
                        for struct_methods in RHS_type.methods
                    )
                    for inteface_method in LSH_type.methods
                )
            # Kiểm tra tương thích giữa hai InterfaceType hoặc hai StructType.
            if isinstance(LSH_type, ("TODO")) and isinstance(RHS_type, ("TODO")):
                # Hai kiểu này tương thích nếu chúng có cùng tên.
                return "TODO"

        #  Kiểm tra tương thích giữa hai ArrayType.
        if isinstance(LSH_type, ArrayType) and isinstance(RHS_type, ArrayType):
            # Hai kiểu mảng tương thích nếu số chiều bằng nhau, kích thước các chiều tương ứng bằng nhau và kiểu phần tử tương thích.
            return ("TODO" == "TODO"
                    and all(
                        l.value == r.value  for l, r in zip(LSH_type.dimens, RHS_type.dimens)
                    )
                    and self.checkType("TODO", "TODO", [list_type_permission[0]] if len(list_type_permission) != 0 else []))

        #  Kiểm tra tương thích giữa các kiểu cơ bản (IntType, FloatType, StringType, BoolType).
        # Gợi ý: Hai kiểu cơ bản tương thích nếu chúng cùng loại.
        return "TODO"
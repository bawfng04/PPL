from Utils import *
# from StaticCheck import *
# from StaticError import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *

class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        #
        self.className = "MiniGoClass" # Tên class tổng của chương trình minigo
        self.astTree = None
        self.path = None
        self.emit = None
        self.function = None
        self.list_function = []
        self.arrayCell = None # Dùng để lưu kiểu của mảng khi duyệt vào 1 ArrayCell
        self.arrayCellType = None

    def init(self):
        mem = [
            Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            # TODO: Thêm tất cả các hàm builtin trong minigo spec vào trong này, io là file trong folder _io quy định mấy hày này sẽ làm j rồi
        ]
        return mem

    def gen(self, ast, dir_):
        # Nơi được gọi để khởi tạo classCodeGen và bắt đầu sinh mã !!!
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)



    ### Vì chương trình của mình sẽ xem như nằm trong 1 class duy nhất trong java, cụ thể là MiniGoClass
    ### Nên mình sẽ định nghĩa 2 phương thức <init> và <clinit> trong class này bằng 2 phương thức emitObjectInit và emitObjectCInit
    ### Phương thức <init> sẽ được gọi khi khởi tạo 1 object của class này, và <clinit> sẽ được gọi khi class này được load vào bộ nhớ

    ### Dưới đây là mã jasmin cho 2 phương thức này(LMiniGoClass - kí hiệu L dùng để tham chiếu đến class trong java):

                    # .method public <init>()V
                    # .var 0 is this LMiniGoClass; from Label0 to Label1
                    # Label0:
                    # 	aload_0
                    # 	invokespecial java/lang/Object/<init>()V
                    # Label1:
                    # 	return
                    # .limit stack 1
                    # .limit locals 1
                    # .end method

                    # .method public static <clinit>()V
                    # Label0:
                    # Label2:
                    # 	invokestatic MiniGoClass/fint()I
                    # 	putstatic MiniGoClass/global I
                    # Label3:
                    # Label1:
                    # 	return
                    # .limit stack 2
                    # .limit locals 0
                    # .end method


    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        # sinh ra mã => .method public <init>()V
        frame.enterScope(True)  # Mỗi hàm có 1 frame riêng, và mỗi frame có 1 scope riêng, nên dùng enterScope để vào scope của frame này

        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        # sinh ra mã => .var 0 is this LMiniGoClass; from Label0 to Label1

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # sinh ra mã => Label0: (nơi body method bắt đầu)

        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
        # sinh ra mã => aload_0 (đưa biến this vào stack)

        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        # sinh ra mã => invokespecial java/lang/Object/<init>()V (gọi hàm khởi tạo của class cha là Object)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        # sinh ra mã => Label1: (nơi body method kết thúc)


        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        # sinh ra mã => return (trả về từ hàm khởi tạo này)

        self.emit.printout(self.emit.emitENDMETHOD(frame))
        # sinh ra mã limit stack 1, limit locals 1, end method (kết thúc định nghĩa phương thức <init>)

        frame.exitScope()

    def emitObjectCInit(self, ast: Program, env):


        frame = Frame("<cinit>", VoidType())
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env['frame'] = frame

        #Trừ đoạn code dưới đây thì còn lại giống emitObjectInit:
        self.visit(Block([
            #  Assign(#TODO ...) for item in ast.decl if isinstance(item, (VarDecl, ConstDecl))       => Block chứa danh sách các Assign
        ]), env)
        # Đoạn này nạp mấy biến/hằng toàn cục vào lớp MiniGoClass



        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitProgram(self, ast: Program, c):
        # Biến c ban đầu là dãy Symbol "mem" ở hàm init() ở trên, chứa các hàm builtin của minigo.

        self.list_function = c + [Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)), item.retType), CName(self.className)) for item in ast.decl if isinstance(item, FuncDecl)]
        # Đoạn này nạp mấy hàm vào list_function, biến tụi nó thành Symbol để quản lí

        env = {}
        env['env'] = [c]


        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        # sinh ra mã => .source MiniGoClass.java
        #               .class public MiniGoClass
        #               .super java.lang.Object


        # Đoạn sau sinh mã cho khai báo biến và khai báo báo hàm:
        ## 1. Khai báo biến (duyệt trước vì hàm có thể dùng biến toàn cục, cập nhật biến/hằng toàn cục vào env)
        env = reduce(lambda a, x: self.visit(x, a) if isinstance(x, VarDecl) or  isinstance(x, ConstDecl) else a, ast.decl, env)

        ## 2. Khai báo hàm (gọi hàm visitFuncDecl cho từng hàm trong danh sách hàm trong ast.decl)
        reduce(lambda a, x: self.visit(x, a) if isinstance(x, FuncDecl) else a, ast.decl, env)



        # Gọi mấy hàm đã định nghĩa ở trên
        self.emitObjectInit()
        self.emitObjectCInit(ast, env)


        self.emit.printout(self.emit.emitEPILOG())
        #Không sinh ra mã gì cả, chỉ là kết thúc chương trình thôi


        return env

    def visitFuncDecl(self, ast: FuncCall, o: dict) -> dict:

        #Lưu function đang duyệt vào biến self.function để dùng sau
        self.function = ast

        frame = Frame(ast.name, ast.retType)

        #Với hàm main thì có params và return cố định như bên dưới, này được định nghĩa trong spec:
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
            ast.body = Block([] + ast.body.member)
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)


        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, frame))
        # sinh ra mã => .method public static main([Ljava/lang/String;)V đối với hàm main

        # Tiếp theo nhảy vào body hàm:
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        env['env'] = [[]] + env['env']
        # Lưu ý: mình đang dùng field env của env để lưu reference.

        # Sinh mã VAR tùy vào hàm có phải main hay không, đồng thời cũng cập nhật biến env['env'] với các tham số của hàm:
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)

        #Gọi hàm visitBlock, truyền env đã được cập nhật scope params.
        self.visit(ast.body,env)


        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))


        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        #Nếu trả về kiểu khác void thì hàm visitBlock đã sinh mã cho return rồi.

        self.emit.printout(self.emit.emitENDMETHOD(frame))


        frame.exitScope()
        # Kết thúc thân hàm


        return o

    def visitParamDecl(self, ast: ParamDecl, o: dict) -> dict:
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(self.emit.emitVAR(index, ast.parName, ast.parType, frame.getStartLabel() ,frame.getEndLabel(), frame))
        return o

    def visitVarDecl(self, ast: VarDecl, o: dict) -> dict:


        def create_init(varType: Type, o: dict):
            if type(varType) is IntType:
                return IntLiteral(0)
            elif type(varType) is FloatType:
                return FloatLiteral(0.0)
            elif type(varType) is StringType:
                return StringLiteral("\"\"")
            elif type(varType) is BoolType:
                return BooleanLiteral("false")
            elif type(varType) is ArrayType:

                # Với mảng thì mình dùng đệ quy để sinh ra mảng giá trị cho đúng nhé.
                #  VD mảng nguyên 1 chiều thì sẽ là [0,0,0,...], mảng 2 chiều thì sẽ là [[0,0,0,...],[0,0,0,...],...]
                #  VD mảng bool 1 chiều thì sẽ là [false,false,false,...], mảng 2 chiều thì sẽ là [[false,false,false,...],[false,false,false,...],...]

                #Lưu ý ở đây mình k xử lí dimension là biểu thức hay Id, chỗ khác sẽ xử lí sau.
                pass #TODO


        varInit = ast.varInit # Giá trị khởi tạo của biến
        varType = ast.varType # Kiểu của biến

        #Nếu không có giá trị khởi tạo thì tự động gán cho nó 0, 0.0, false, "",..tùy vào kiểu biến:
        # int -> 0, float -> 0.0, bool -> false, string -> "", array -> mảng chứa các giá trị "zero" tùy thuộc vào kiểu phần tử.
        if not varInit:
            varInit = create_init(varType, o)
            if type(varType) is ArrayType:
                varInit = ArrayLiteral(varType.dimens, varType.dimens, varInit)
            ast.varInit = varInit


            ast.varInit = varInit
        env = o.copy()
        env['frame'] = Frame("<template_VT>", VoidType())

        # Như đã nói trong lưu ý ở trên thì trường hợp dimension là Id hay biểu thức sẽ đc xử lí ở visitArrayLiteral và là dòng dưới đây
        rhsCode, rhsType = self.visit(varInit, env)

        #Trường hợp khai báo với giá trị nhưng không có kiẻu thì mình sẽ tự động gán kiểu cho nó dựa vào giá trị khởi tạo.
        if not varType:
            varType = rhsType

        if 'frame' not in o: # TH global var => biến khai báo toàn cục thì mình
            o['env'][0].append(Symbol(ast.varName, varType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, varType, True, False, None))
        else:
            frame = o['frame']

            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, varType, Index(index))) # mỗi trường sẽ có 1 index riêng


            self.emit.printout(self.emit.emitVAR(index, ast.varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))
            rhsCode, rhsType = self.visit(varInit, o)
            if type(varType) is FloatType and type(rhsType) is IntType:
                pass #TODO: thêm mã chuyển đổi kiểu int -> float vào rhsCode.

            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, varType, index,  frame)) # sinh mã gán giá trị vào biến
        return o

    def visitFuncCall(self, ast: FuncCall, o: dict) -> dict:
        sym = next(filter(lambda x: x.name == ast.funName, self.list_function),None)
        if o.get('stmt'):
            o["stmt"] = False
            #TODO: dùng emittter sinh mã cho khúc lấy params trong ast.args, nhớ dùng hàm visit, visit qa từng args. Dùng list comprehension or vòng lặp: [..code..]


            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
            #Đã đặt đủ tham số vào stack rồi thì sinh mã gọi hàm thôi

            return o # trả về o luôn vì stmt luôn trả về void k cần quan tâm
        output = "".join([str(self.visit(x, o)[0]) for x in ast.args])
        output += "TODO code" ## TODO: Đã đặt đủ tham số vào stack rồi thì sinh mã gọi hàm thôi

        # Vì funcall ở chỗ này là 1 biểu thức nên mình cần trả về giá trị kèm theo kiểu trả về luôn.
        return output, sym.mtype.rettype

    def visitBlock(self, ast: Block, o: dict) -> dict:
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL('TODO: code')) #TODO: để sinh mã label cần có 2 thông tin là startLabel do frame cung cấp và frame
        # => dùng phương thức getStartLabel() của frame để lấy label này.

        for item in ast.member:
            if type(item) is FuncCall:
                env["stmt"] = True
            #Cập nhật biến cờ trước khi visit vào hàm FuncCall, lát nữa duyệt vào trong sẽ tắt biến cờ này đi.
            env = self.visit(item, env)


        self.emit.printout(self.emit.emitLABEL('TODO: code')) #TODO: để sinh mã label cần có 2 thông tin là endLabel do frame cung cấp và frame
        # => dùng phương thức getEndLabel() của frame để lấy label này.

        env['frame'].exitScope()
        return o

    def visitId(self, ast: Id, o: dict) -> dict:
        #Dòng này để xác định à Id của mình là thằng nào trong env.
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)

        #Nếu Id này nằm ở vế trái phép gán
        if o.get('isLeft'):
            if type(sym.value) is Index: #Nếu Id là 1 tên trường của 1 object
                return self.emit.emitWRITEVAR("TODO"), sym.mtype #TODO ở đây tham số inType là sym.mtype
            else:
                #Putstatic là ghi vào biến static,
                return self.emit.emitPUTSTATIC("TODO"),sym.mtype  #TODO  truyền vào tên lexeme cho đúng. VD: MiniGoClass/varName


        if type(sym.value) is Index: #Nếu Id là 1 tên trường của 1 object
            return self.emit.emitREADVAR("TODO"),sym.mtype #TODO   truyền vào tên lexeme cho đúng
        else:
            #Getstatic là đọc biến static,
            return self.emit.emitGETSTATIC("TODO"),sym.mtype #TODO  truyền vào tên lexeme cho đúng

    def visitAssign(self, ast: Assign, o: dict) -> dict:

        #Xem thử là biến này đã được khai báo chưa, trong minigo nếu phép gán mà biến chưa được khai báo thì sẽ tự động khai báo nó luôn.
        if type(ast.lhs) is Id and not next(filter(lambda x: "TODO")): # TODO: kiểm tra xem biến này đã được khai báo chưa => Duyệt trong o['env']
            return # TODO: Khúc này tạo và visit 1 VarDecl mới với kiểu của var là None.


        rhsCode, rhsType = self.visit(ast.rhs, o)

        #Trước khi duyệt vế trái (có thể chạy vào hàm visitId ở trên) thì mình bật biến cờ isLeft, duyệt xong thì tắt nó đi.
        #Biến cờ này dùng để xác định xem mình đang ở vế trái hay vế phải của phép gán, từ đó mà sinh mã cho đúng.
        o['isLeft'] = True
        lhsCode, lhsType = self.visit(ast.lhs, o)
        o['isLeft'] = False

        if type(lhsType) is FloatType and type(rhsType) is IntType:
            pass #TODO: thêm mã chuyển đổi kiểu int -> float vào lhsCode.


        # Khúc array cell này task 3

        o['frame'].push() # Tăng kích thước stack lên 1 đơn vị, vì mình sẽ dùng stack để lưu trữ giá trị của biến này.



        if type(ast.lhs) is ArrayCell:
            self.emit.printout(lhsCode)
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitASTORE("TODO")) # lưu vào mảng, truyền vào mảng và o['frame'].Gợi ý, khi visit lhs ta có visitAarrayCell và dùng self.. để lưu mảng đang xét
        # access id
        else:
            self.emit.printout(rhsCode)
            self.emit.printout(lhsCode)

        return o

    def visitReturn(self, ast: Return, o: dict) -> dict:
        if ast.expr:
            self.emit.printout(self.visit(ast.expr, o)[0])
        self.emit.printout(self.emit.emitRETURN("TODO")) # truyền vào kiểu trả về của hàm và o['frame']
        return o

    ##  END decl ------------------------------




   ##  basic expression ------------------------------
    def visitBinaryOp(self, ast: BinaryOp, o: dict) -> tuple[str, Type]:
        op = ast.op
        frame = o['frame']
        codeLeft, typeLeft = self.visit(ast.left, o)
        codeRight, typeRight = self.visit(ast.right, o)
        if op in ['+', '-'] and type(typeLeft) in [FloatType, IntType]:
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                ## TODO implement xét cả typeRight nữa
            return codeLeft + codeRight + "TODO" ## TODO implement
        if op in ['*', '/']:
            typeReturn = "TODO" ## TODO : cả trái phải đều int thì mới trả ra int con không thì trả ra float
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                ## TODO implement tương tự cho typeRight
            return codeLeft + codeRight +  "TODO"## TODO sinh mã cho mulop + trả vè kiểu trả về
        if op in ['%']:
            return codeLeft + codeRight +  "TODO"## TODO sinh mã cho mod + trả về kiểu trả về
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [FloatType, IntType]:
            return codeLeft + codeRight +  "TODO"## TODO sinh mã cho reop + trả về kiểu trả về
        if op in ['||']:
            return codeLeft + codeRight +  "TODO"## TODO sinh mã cho orop + trả về kiểu trả về
        if op in ['&&']:
            return codeLeft + codeRight + self.emit.emitANDOP(frame), BoolType()  # Lấy này làm vd làm mấy cái ở trên

        # nối string string
        if op in ['+', '-'] and type(typeLeft) in [StringType]:
            return codeLeft + codeRight + "TODO" ## TODO sinh mã cho hàm concat(nằm trong java/lang/String/concat) + trả về kiểu trả về là stringtype
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [StringType]:
            code = codeLeft + codeRight + "TODO" ## TODO sinh mã cho hàm compareTo(nằm trong java/lang/String/compareTo) + trả về kiểu trả về là inttype
            code = code +  "TODO"## TODO implement + self.emit.emitREOP(op, IntType(), frame)
            return code, BoolType()

    def visitUnaryOp(self, ast: UnaryOp, o: dict) -> tuple[str, Type]:
        if ast.op == '!':
            code, type_return = self.visit(ast.body, o)
            return code + self.emit.emitNOT(BoolType(), o['frame']), BoolType()
        ## TODO implement cho TH dấu -, dùng emitNEGOP


    def visitIntLiteral(self, ast: IntLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHICONST(ast.value, o['frame']), BoolType()

    def visitStringLiteral(self, ast: StringLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHCONST(ast.value, StringType(), o['frame']), StringType()

    ## TODO END basic expression ------------------------------

    ## TODO array ------------------------------
    def visitArrayCell(self, ast: ArrayCell, o: dict) -> tuple[str, Type]:
        newO = o.copy()
        newO['isLeft'] = False
        codeGen, arrType = "TODO" #visit thằng expr của array cell này, nên nhớ arraycell gồm phần expr phía trước và index phía sau.

        for idx, item in enumerate(ast.idx):
            codeGen += self.visit(item, newO)[0]
            if idx != len(ast.idx) - 1:
                codeGen += self.emit.emitALOAD(arrType, o['frame'])

        retType = None
        if len(arrType.dimens) == len(ast.idx):
            retType = arrType.eleType
            if not o.get('isLeft'):
                codeGen += "TODO" #TODO: thêm mã cho trường hợp này => dùng emitALOAD để lấy giá trị của phần tử trong mảng ra
            else:
                self.arrayCell = "TODO"  # TODO: Nếu nó arraycell nằm bên vế trái thì mình gán vào biến này để biết đang duyệt vào arraycell nào, dùng sau này.
        else:
            retType = ArrayType(arrType.dimens[len(ast.idx): ], arrType.eleType)
            if not o.get('isLeft'):
                codeGen += "TODO" #TODO: thêm mã cho trường hợp này => dùng emitALOAD để lấy giá trị của phần tử trong mảng ra
            else:
                self.arrayCell = "TODO" # TODO: Nếu nó arraycell nằm bên vế trái thì mình gán vào biến này để biết đang duyệt vào arraycell nào, dùng sau này.
        return #TODO trả vè mã nãy giờ tạo để thằng nào gọi thằng đó in và type -> tuple[str, Type]:

    def visitArrayLiteral(self, ast:ArrayLiteral , o: dict) -> tuple[str, Type]:

        # Phần ArrayLiteral.value là 1 nested list nên mình sẽ dùng đệ quy để duyệt nó.
        def nested2recursive(dat: Union[Literal, list['NestedList']], o: dict) -> tuple[str, Type]:
            #dat có thể là 1 Literal hoặc là 1 list chứa các Literal khác, nên mình sẽ kiểm tra xem dat có phải là list hay không.

            #Nếu là Literal thôi thì chỉ cần visit tới là xong, không cần đệ quy nữa, tham số o là 0
            if not isinstance(dat,list):
                return self.visit(dat, 0)

            #Nếu dat là 1 list thì đoạn code dưới sẽ giải quyết
            #chuẩn bị ngữ cảnh
            frame = o['frame'] # lấy frame từ o
            codeGen = self.emit.emitPUSHCONST(len(dat), IntType(), frame) #sinh mã đẩy số lượng phần tử của mảng vào stack


            #Trường hợp danh sách không lồng nhau(vì phần tử đầu tiên không phải là list)
            if not isinstance(dat[0],list):
                _, type_element_array = self.visit(dat[0], o)  # gọi hàm visit cho phần tử đầu tiên để lấy kiểu của nó
                codeGen += self.emit.TODO # cần dùng 1 trong 2 emitNEWARRAY hoặc emitANEWARRAY để tạo mảng với kiểu phần tử là type_element_array

                # Lặp qua từng phần tử trong danh sách:
                for idx, item in enumerate(dat):
                    codeGen += "TODO"  # TODO Nhân đôi tham chiếu mảng trên stack (emitDUP).
                    codeGen +="TODO"  # TODO Đẩy chỉ số của phần tử (emitPUSHCONST) lên stack.
                    codeGen += "TODO"  # TODO Gọi self.visit(item, o) để xử lý giá trị phần tử.
                    codeGen += "TODO"  # TODO Lưu giá trị vào mảng (emitASTORE).
                return codeGen , ArrayType("TODO") #TODO: Chú ý dùng đến len(dat)

            #Trường hợp danh sách lồng nhau:
            # Nếu phần tử đầu tiên của danh sách là một danh sách khác (danh sách lồng nhau), thì:
            # Gọi đệ quy nested2recursive(dat[0], o) để xử lý danh sách con.
            # Sinh mã code để tạo một mảng mới với kiểu phần tử là kiểu của danh sách con.
            _, type_element_array = nested2recursive(dat[0], o)
            codeGen += self.emit.TODO # cần dùng 1 trong 2 emitNEWARRAY hoặc emitANEWARRAY để tạo mảng với kiểu phần tử là type_element_array



            # Lặp qua từng phần tử trong danh sách:
                # Nhân đôi tham chiếu mảng trên stack (emitDUP).
                # Đẩy chỉ số của phần tử (emitPUSHCONST).
                # Gọi đệ quy nested2recursive(item, o) để xử lý danh sách con.
                # Lưu giá trị vào mảng (emitASTORE).
            for idx, item in enumerate(dat):
                codeGen += "TODO"
                codeGen += "TODO"
                codeGen +="TODO"
                codeGen += "TODO"
            return  codeGen, ArrayType("TODO") #TODO: Chú ý dùng đến len(dat)

        #Gọi hàm đệ quy trong đó tham số truyền vào là ast.value, o
        return nested2recursive(ast.value, o)

    def visitConstDecl(self, ast:ConstDecl, o: dict) -> dict:
        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)

    def visitArrayType(self, ast:ArrayType, o):
        codeGen = ""
        # TODO : Lặp qua dimens để thêm code vào codeGen, dùng visit và lưu ý rằng visit sẽ trả về cặp mã và kiểu của nó.
        # Cuối cùng đủ tham số thì dùng emitMULTIANEWARRAY để tạo mảng mới.
        codeGen += self.emit.emitMULTIANEWARRAY(ast, o['frame'])
        return codeGen, ast
    def visitIntLiteral(self, ctx, o):
        # ast: IntLiteral - Đây là nút trong cây cú pháp trừu tượng (AST)
        #                đại diện cho một hằng số nguyên. Nó có thuộc tính
        #                'value' chứa giá trị số nguyên thực tế (ví dụ: 5).
        # o: Any       - Đây là đối tượng ngữ cảnh (context) được truyền vào
        #                khi duyệt cây. Theo mô tả, nó chứa một thuộc tính
        #                'frame' là một đối tượng Frame.
        # return: (string, Type) - Hàm phải trả về một cặp gồm:
        #                         1. Chuỗi chứa mã Jasmin để đẩy hằng số lên stack.
        #                         2. Một đối tượng Type (cụ thể là IntType)
        #                            để biểu thị kiểu của hằng số vừa đẩy lên.

        # 1. Lấy đối tượng Frame từ ngữ cảnh 'o':
        frame = o.frame
        #   Đối tượng 'frame' rất quan trọng. Nó giúp theo dõi trạng thái
        #   của operand stack (ví dụ: số lượng phần tử hiện tại, kích thước tối đa)
        #   và quản lý các biến cục bộ, nhãn (labels).
        #   Ở đây, chúng ta cần 'frame' để gọi các hàm của Emitter mà có
        #   tác động lên stack (ví dụ: frame.push()).

        # 2. Lấy giá trị số nguyên từ nút AST:
        intValue = ctx.value
        #   Chúng ta cần giá trị số nguyên cụ thể (ví dụ: 5, 100, -1) để biết
        #   chính xác lệnh JVM nào cần phát sinh.

        # 3. Gọi hàm của Emitter để tạo mã Jasmin và cập nhật Frame:
        jasminCode = self.emit.emitPUSHICONST(intValue, frame)
        #   Đây là bước quan trọng nhất. Thay vì tự mình quyết định dùng
        #   iconst_1, iconst_5, bipush, sipush hay ldc, chúng ta giao nhiệm vụ
        #   này cho phương thức `emitPUSHICONST` của đối tượng Emitter (`self.emit`).
        #   - Lý do 1: `emitPUSHICONST` đã được viết sẵn để xử lý việc chọn lệnh
        #     JVM tối ưu nhất dựa trên giá trị `intValue` (xem lại code Emitter.py).
        #     Nó biết khi nào dùng iconst_<i> (cho -1 đến 5), khi nào dùng bipush
        #     (cho byte), sipush (cho short), hoặc ldc (cho các giá trị lớn hơn).
        #   - Lý do 2: Quan trọng hơn, bên trong `emitPUSHICONST`, nó cũng gọi
        #     `frame.push()`. Điều này *mô phỏng* hành động đẩy một giá trị lên
        #     operand stack, giúp cập nhật `currOpStackSize` và `maxOpStackSize`
        #     trong đối tượng `frame`. Thông tin này cực kỳ cần thiết để sau này
        #     có thể phát sinh đúng chỉ thị `.limit stack` cho phương thức.
        #   => Việc gọi `self.emit.emitPUSHICONST` vừa tạo ra mã Jasmin đúng, vừa
        #      đảm bảo đối tượng `frame` được cập nhật chính xác.

        # 4. Xác định kiểu của hằng số:
        literalType = IntType()
        #   Vì đây là visitIntLiteral, kiểu của hằng số này luôn luôn là IntType.
        #   Chúng ta tạo một đối tượng IntType để trả về cùng với mã Jasmin.
        #   Việc trả về kiểu này có thể hữu ích cho các bước kiểm tra kiểu hoặc
        #   phát sinh mã ở các nút cha trong cây AST.

        # 5. Trả về kết quả:
        return jasminCode, literalType
        #   Trả về cặp (tuple) gồm chuỗi mã Jasmin (ví dụ: "\ticonst_5\n") và
        #   đối tượng IntType theo yêu cầu của phương thức visit.


    def visitFloatLiteral(self, ctx, o):
        thisFrame = o.frame
        val = ctx.value
        jasminCode = self.emit.emitPUSHFCONST(val, thisFrame)
        literalType = FloatType()
        return jasminCode, literalType

    def visitBinExpr(self, ast, o):
        # ast: BinExpr - Nút này trong cây AST biểu diễn một biểu thức nhị phân.
        #               Nó có 3 thành phần chính:
        #               - ast.op: Toán tử (dạng chuỗi, ví dụ: "+", "-.", "*")
        #               - ast.e1: Biểu thức con bên trái (kiểu Expr)
        #               - ast.e2: Biểu thức con bên phải (kiểu Expr)
        # o: Context    - Đối tượng ngữ cảnh chứa thông tin cần thiết,
        #                 quan trọng nhất là đối tượng Frame (truy cập qua o.frame).
        # return: (string, Type) - Trả về một cặp gồm:
        #                         1. Chuỗi mã Jasmin để thực hiện biểu thức.
        #                         2. Kiểu dữ liệu (IntType hoặc FloatType) của kết quả.

        # 1. Lấy đối tượng Frame:
        frame = o.frame
        #   Chúng ta cần 'frame' để cập nhật mô phỏng trạng thái của operand stack
        #   khi các lệnh JVM được tạo ra (ví dụ: khi gọi các hàm emitADDOP,
        #   emitMULOP...).

        # 2. Duyệt (visit) toán hạng trái (e1):
        code1, type1 = self.visit(ast.e1, o)
        #   Gọi đệ quy `self.visit` cho biểu thức con bên trái (ast.e1).
        #   - Lệnh này sẽ tạo ra mã Jasmin (`code1`) cần thiết để tính toán
        #     giá trị của e1 và đẩy kết quả đó lên đỉnh operand stack.
        #   - Nó cũng trả về kiểu dữ liệu (`type1`) của kết quả e1.
        #   => Sau bước này, stack sẽ chứa kết quả của e1.

        # 3. Duyệt (visit) toán hạng phải (e2):
        code2, type2 = self.visit(ast.e2, o)
        #   Gọi đệ quy `self.visit` cho biểu thức con bên phải (ast.e2).
        #   - Lệnh này sẽ tạo ra mã Jasmin (`code2`) để tính toán giá trị của e2
        #     và đẩy kết quả đó lên đỉnh operand stack.
        #   => Sau bước này, stack sẽ chứa: [..., kết_quả_e1, kết_quả_e2]
        #      (kết quả e2 nằm trên cùng).

        # 4. Xác định mã lệnh cho phép toán và kiểu kết quả:
        op = ast.op # Lấy toán tử, ví dụ: "+", "-."
        op_code = "" # Chuỗi chứa mã Jasmin cho phép toán
        resultType = None # Kiểu dữ liệu của kết quả cuối cùng

        # Kiểm tra xem toán tử là cho số nguyên hay số thực
        if op in ['+', '-', '*', '/']:
            # Xử lý phép toán số nguyên
            resultType = IntType() # Kết quả của phép toán nguyên là nguyên
            if op == '+':
                # Gọi hàm của Emitter để tạo lệnh 'iadd'.
                # Hàm này cũng sẽ gọi frame.pop() bên trong để mô phỏng việc
                # stack giảm đi 1 (lấy 2 toán hạng, đẩy 1 kết quả).
                op_code = self.emit.emitADDOP(op, resultType, frame)
            elif op == '-':
                op_code = self.emit.emitADDOP(op, resultType, frame) # Tạo lệnh 'isub'
            elif op == '*':
                op_code = self.emit.emitMULOP(op, resultType, frame) # Tạo lệnh 'imul'
            elif op == '/':
                op_code = self.emit.emitDIV(frame) # Tạo lệnh 'idiv' (không cần toán tử)

        elif op in ['+.', '-.', '*.', '/.']:
            # Xử lý phép toán số thực
            resultType = FloatType() # Kết quả phép toán thực là thực
            # Lấy ký tự toán tử cơ bản (ví dụ: '+' từ '+.') để dùng với hàm emit
            float_op_char = op[0]
            if op in ['+.', '-.']:
                 # Gọi hàm của Emitter để tạo lệnh 'fadd' hoặc 'fsub'.
                 # Hàm này cũng gọi frame.pop().
                op_code = self.emit.emitADDOP(float_op_char, resultType, frame)
            elif op in ['*.', '/.']:
                # Gọi hàm của Emitter để tạo lệnh 'fmul' hoặc 'fdiv'.
                # Hàm này cũng gọi frame.pop().
                op_code = self.emit.emitMULOP(float_op_char, resultType, frame)
        else:
             # Nếu có toán tử khác chưa xử lý thì báo lỗi (hoặc thêm code sau)
             raise NotImplementedError(f"Binary operator {op} not yet implemented")

        # 5. Kết hợp các đoạn mã Jasmin theo đúng thứ tự thực thi:
        jasminCode = code1 + code2 + op_code
        #   - Đầu tiên là mã để tính `e1` (đẩy kết quả e1 lên stack).
        #   - Tiếp theo là mã để tính `e2` (đẩy kết quả e2 lên stack).
        #   - Cuối cùng là mã thực hiện phép toán `op` (lấy 2 giá trị trên cùng
        #     của stack, tính toán, và đẩy kết quả lại stack).

        # 6. Trả về mã Jasmin hoàn chỉnh và kiểu dữ liệu của kết quả:
        return jasminCode, resultTypea


# c2
    def visitBinExpr(self, ctx, o):

        thisFrame = o.frame
        op = ctx.op

        jcode1, type1 = self.visit(ctx.e1, o)
        jcode2, type2 = self.visit(ctx.e2, o)

        op_jcode = ""
        typ = None

        if op in ['+', '-', '*', '/']:
            typ = IntType()
            if op == '+' or op == '-' or op == '*':
                op_jcode = self.emit.emitADDOP(op, typ, thisFrame)
            elif op == '/':
                op_jcode = self.emit.emitDIV(thisFrame)
        elif op in ['+.', '-.']:
            typ = FloatType()
            if op == '+.' or op == '-.':
                op_jcode = self.emit.emitADDOP(op[0], typ, thisFrame)
            elif op == '*.' or op == '/.':
                op_jcode = self.emit.emitMULOP(op[0], typ, thisFrame)
        else:
            pass

        jasminCode = jcode1 + jcode2 + op_jcode
        return jasminCode, typ































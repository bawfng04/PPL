
# program: exp (CM exp)*;
# exp: term COMPARE term | term;
# term: (factor EXPONENT)* factor;
# factor: operand (ANDOR operand)*;
# operand: INTLIT | BOOLIT | LB exp RB;

# INTLIT: [0-9]+;
# BOOLIT: 'true' | 'false';

# ANDOR: '&';
# EXPONENT: '**';
# COMPARE: '>' | '<';
# LB: '[';
# RB: ']';
# CM: ';';
# WS: [ \t\r\n]+ -> skip;



class ASTGeneration(VoTienVisitor):
    #! program: exp+;
    def visitProgram(self, ctx:VoTienParser.ProgramContext):
        return Program([self.visit(item) for item in ctx.exp()])
        # [CHÚ THÍCH]
        # Hàm này xử lý rule 'program'. Nó gọi visit() cho từng 'exp' trong 'ctx.exp()'
        # và tạo ra một list các AST node 'Expr', sau đó bọc trong 'Program' node.

    #! exp: term COMPARE term | term;
    def visitExp(self, ctx:VoTienParser.ExpContext):
        return self.visitChildren(ctx) if ctx.getChildCount() == 1 else BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.term()[0]), self.visit(ctx.term()[1]))
        # [CHÚ THÍCH]
        # Hàm này xử lý rule 'exp'.
        # - Nếu 'exp' chỉ có 1 child (tức là rule 'term'), thì gọi visitChildren() để xử lý child đó.
        # - Nếu 'exp' có 3 child (tức là rule 'term COMPARE term'), thì tạo 'BinaryOp' node:
        #   + op: Lấy operator COMPARE (child thứ 2) bằng 'ctx.getChild(1).getText()'.
        #   + left: Gọi visit() cho 'term' thứ nhất (child đầu tiên) bằng 'self.visit(ctx.term()[0])'.
        #   + right: Gọi visit() cho 'term' thứ hai (child thứ 3) bằng 'self.visit(ctx.term()[1])'.


    #! term: (factor EXPONENT)* factor;
    def visitTerm(self, ctx: VoTienParser.TermContext):
        factors = list(map(self.visit, ctx.factor()))
        # [CHÚ THÍCH]
        # Lấy list các AST node 'factor' bằng cách gọi visit() cho từng 'factor' trong 'ctx.factor()'.

        exponents = list(map(lambda op: op.getText(), ctx.EXPONENT())) # Ô TRỐNG (1)
        # [CHÚ THÍCH - Ô TRỐNG (1)]
        # Lấy list các operator 'EXPONENT' (ví dụ '**') bằng cách:
        # 1. 'ctx.EXPONENT()': Lấy list các TerminalNode của rule 'EXPONENT'.
        # 2. 'map(lambda op: op.getText(), ...)': Áp dụng hàm lambda lên từng TerminalNode để lấy text của operator.
        # 3. 'list(...)': Chuyển kết quả map thành list.


        if len(factors) == 1:
            return factors[0]
        # [CHÚ THÍCH]
        # Nếu chỉ có 1 'factor', thì trả về 'factor' đó (base case của rule 'term').

        return reduce(lambda right, pair: BinaryOp(pair[0], pair[1], right),
                    zip(exponents, factors[:-1]), # Ô TRỐNG (2)
                    factors[-1])
        # [CHÚ THÍCH - Ô TRỐNG (2)]
        # Sử dụng hàm 'reduce' để tạo cây AST cho rule 'term' (có thể có nhiều phép toán EXPONENT).
        # - 'lambda right, pair: BinaryOp(pair[0], pair[1], right)': Hàm lambda này định nghĩa cách kết hợp các 'factor' và 'EXPONENT' thành 'BinaryOp' node.
        #   + 'right':  Giá trị tích lũy từ các lần gọi 'reduce' trước, ban đầu là 'factors[-1]' (factor cuối cùng).
        #   + 'pair': Tuple chứa (operator 'EXPONENT', 'factor' bên trái).
        #   + 'BinaryOp(pair[0], pair[1], right)': Tạo 'BinaryOp' node với:
        #     * op: operator 'EXPONENT' (lấy từ 'pair[0]').
        #     * left: 'factor' bên trái (lấy từ 'pair[1]').
        #     * right: 'right' (giá trị tích lũy từ trước).
        # - 'zip(exponents, factors[:-1])': Iterable chứa các cặp (operator 'EXPONENT', 'factor' bên trái).
        #   + 'factors[:-1]': Lấy list 'factors' trừ 'factor' cuối cùng (vì 'factor' cuối cùng là 'initializer' của reduce).
        #   + 'zip(exponents, factors[:-1])': Ghép list 'exponents' và 'factors[:-1]' thành list các tuple.
        # - 'factors[-1]': 'Initializer' cho hàm 'reduce', là 'factor' cuối cùng (vì phép toán EXPONENT có tính kết hợp trái).


    #! factor: operand (ANDOR operand)*;
    def visitFactor(self, ctx: VoTienParser.FactorContext):
        operands = list(map(self.visit, ctx.operand()))
        # [CHÚ THÍCH]
        # Tương tự 'visitTerm', lấy list các AST node 'operand'.
        operators = list(map(lambda op: op.getText(), ctx.ANDOR())) # [ĐÃ CHO TRONG ĐỀ]
        # [CHÚ THÍCH - ĐÃ CHO TRONG ĐỀ]
        # Lấy list các operator 'ANDOR' (ví dụ '&').


        if len(operands) == 1:
            return operands[0]
        # [CHÚ THÍCH]
        # Nếu chỉ có 1 'operand', trả về 'operand' đó (base case của rule 'factor').


        return reduce(lambda left, pair: BinaryOp(pair[0], left, pair[1]),
                    zip(operators, operands[1:]), # Ô TRỐNG (3)
                    operands[0])
        # [CHÚ THÍCH - Ô TRỐNG (3)]
        # Tương tự 'visitTerm', sử dụng 'reduce' để tạo cây AST cho rule 'factor' (có thể có nhiều phép toán ANDOR).
        # - 'lambda left, pair: BinaryOp(pair[0], left, pair[1])': Hàm lambda kết hợp 'operand' và 'ANDOR' thành 'BinaryOp' node.
        #   + 'left': Giá trị tích lũy, ban đầu là 'operands[0]' (operand đầu tiên).
        #   + 'pair': Tuple chứa (operator 'ANDOR', 'operand' bên phải).
        #   + 'BinaryOp(pair[0], left, pair[1])': Tạo 'BinaryOp' node với:
        #     * op: operator 'ANDOR' (lấy từ 'pair[0]').
        #     * left: 'left' (giá trị tích lũy từ trước).
        #     * right: 'operand' bên phải (lấy từ 'pair[1]').
        # - 'zip(operators, operands[1:])': Iterable chứa các cặp (operator 'ANDOR', 'operand' bên phải).
        #   + 'operands[1:]': Lấy list 'operands' trừ 'operand' đầu tiên (vì 'operand' đầu tiên là 'initializer' của reduce).
        #   + 'zip(operators, operands[1:])': Ghép list 'operators' và 'operands[1:]' thành list các tuple.
        # - 'operands[0]': 'Initializer' cho hàm 'reduce', là 'operand' đầu tiên (vì phép toán ANDOR có tính kết hợp trái).


    #! operand: INTLIT | BOOLIT | LB exp RB;
    def visitOperand(self, ctx:VoTienParser.OperandContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        # [CHÚ THÍCH]
        # Nếu 'operand' là 'INTLIT', tạo 'IntLiteral' node.
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText() == 'true') # Ô TRỐNG (4)
        # [CHÚ THÍCH - Ô TRỐNG (4)]
        # Nếu 'operand' là 'BOOLIT', tạo 'BooleanLiteral' node.
        # - 'ctx.BOOLIT().getText()': Lấy text của boolean literal ('true' hoặc 'false').
        # - 'ctx.BOOLIT().getText() == 'true'': So sánh text với 'true' để có giá trị boolean (True hoặc False).
        # - 'BooleanLiteral(...)': Tạo 'BooleanLiteral' node với giá trị boolean vừa tạo.
        elif ctx.LB():
            return self.visit(ctx.exp())
        # [CHÚ THÍCH]
        # Nếu 'operand' là 'LB exp RB' (biểu thức trong ngoặc vuông), gọi visit() cho 'exp' bên trong.
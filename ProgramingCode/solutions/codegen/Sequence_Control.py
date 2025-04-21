# 1
    def visitVarDecl(self, ctx, o):
            # ctx: VarDecl (name: str, typ: Type)
            # o: SubBody (frame: Frame or None, sym: List[Symbol])
            # return: SubBody (updated symbol list)

            varName = ctx.name
            varType = ctx.typ
            frame = o.frame
            # symList = o.sym

            if frame is None:
                # nếu frame = none -> biến global -> static
                jasminCode = self.emit.emitATTRIBUTE(varName, varType, False)
                self.emit.printout(jasminCode)
                # Create symbol with CName
                return Symbol(varName, varType, CName(self.className))
                # Return updated SubBody with new symbol prepended
                # return SubBody(None, [newSymbol] + symList)
            else:
                # Local variable/parameter declaration
                # Get new index from frame
                index = frame.getNewIndex()
                # Generate .var directive
                startLabel = frame.getStartLabel()
                endLabel = frame.getEndLabel()
                jasminCode = self.emit.emitVAR(index, varName, varType, startLabel, endLabel)
                self.emit.printout(jasminCode)
                # Create symbol with Index
                return Symbol(varName, varType, Index(index))
                # Return updated SubBody with new symbol prepended
                # return SubBody(frame, [newSymbol] + symList)


# 2
    def visitId(self, ctx, o):
        frame = o.frame
        symbols = o.sym
        isLeft = o.isLeft
        name = ctx.name

        symbol = next((s for s in symbols if s.name == name), None)

        if symbol is None:
            pass

        symbol_type = symbol.mtype
        symbol_val = symbol.value # Index (cục bộ, tham số) hoặc CName (global)

        # nếu left -> LHS (biến được gán giá trị)
        # vd, x = 5 -> x là LHS -> phải store giá trị trên đỉnh stack vào biến x (có index tương ứng)
        if isLeft:
            # Identifier is on the LHS (target of an assignment)
            if isinstance(symbol_val, Index):
                index = symbol_val.value
                jasmin_code = self.emit.emitASTORE(symbol_type, index, frame)
            elif isinstance(symbol_val, CName):
                # Global variable (static field): generate PUTSTATIC
                class_name = symbol_val.value
                jasmin_code = self.emit.emitPUTSTATIC(class_name, name, symbol_type, frame)
            else:
                 pass
        # nếu right -> RHS (biến được sử dụng trong biểu thức)
        # vd, x + 5 -> x là RHS -> phải load giá trị của biến x lên stack (có index tương ứng)
        else:
            if isinstance(symbol_val, Index):
                # Local variable or parameter: generate ALOAD
                index = symbol_val.value
                jasmin_code = self.emit.emitALOAD(symbol_type, index, frame)
            elif isinstance(symbol_val, CName):
                # Global variable (static field): generate GETSTATIC
                class_name = symbol_val.value
                jasmin_code = self.emit.emitGETSTATIC(class_name, name, symbol_type, frame)
            else:
                pass

        return jasmin_code, symbol_type

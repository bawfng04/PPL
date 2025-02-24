// Generated from d:/PPL_Initial/src/test/gui/BKOOL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BKOOLParser}.
 */
public interface BKOOLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(BKOOLParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(BKOOLParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(BKOOLParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(BKOOLParser.ExprContext ctx);
}
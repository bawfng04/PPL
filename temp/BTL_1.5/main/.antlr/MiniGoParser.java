// Generated from d:/Projects/PPL-Assignment/BTL/MiniGO_BTL2p2/main/MiniGo.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class MiniGoParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IF=1, ELSE=2, FOR=3, RETURN=4, BREAK=5, CONTINUE=6, FUNC=7, TYPE=8, VAR=9, 
		CONST=10, STRUCT=11, INTERFACE=12, STRING=13, INT=14, FLOAT=15, BOOLEAN=16, 
		RANGE=17, NIL=18, TRUE=19, FALSE=20, ADD=21, SUB=22, MUL=23, DIV=24, MOD=25, 
		EQUAL=26, NOT_EQUAL=27, LESS=28, LESS_OR_EQUAL=29, GREATER=30, GREATER_OR_EQUAL=31, 
		AND=32, OR=33, NOT=34, ASSIGN=35, ADD_ASSIGN=36, SUB_ASSIGN=37, MUL_ASSIGN=38, 
		DIV_ASSIGN=39, MOD_ASSIGN=40, DOT=41, COLON=42, LP=43, RP=44, LSB=45, 
		RSB=46, LB=47, RB=48, SEMI=49, COMMA=50, ID=51, INT_LIT=52, FLOAT_LIT=53, 
		STRING_LIT=54, LINE_COMMENT=55, BLOCK_COMMENT=56, WS=57, NEWLINE=58, UNCLOSE_STRING=59, 
		ILLEGAL_ESCAPE=60, ERROR_CHAR=61;
	public static final int
		RULE_program = 0, RULE_declared = 1, RULE_variables_declared = 2, RULE_var_decl_list = 3, 
		RULE_var_decl = 4, RULE_constants_declared = 5, RULE_const_decl_list = 6, 
		RULE_const_decl = 7, RULE_function_declared = 8, RULE_method_declared = 9, 
		RULE_receiver = 10, RULE_params_list = 11, RULE_param = 12, RULE_struct_declared = 13, 
		RULE_struct_type = 14, RULE_interface_declared = 15, RULE_interface_type = 16, 
		RULE_statement = 17, RULE_declared_statement = 18, RULE_assign_statement = 19, 
		RULE_assign_lhs = 20, RULE_if_statement = 21, RULE_for_statement = 22, 
		RULE_for_clause = 23, RULE_for_init = 24, RULE_for_update = 25, RULE_range_clause = 26, 
		RULE_assign_op = 27, RULE_break_statement = 28, RULE_continue_statement = 29, 
		RULE_return_statement = 30, RULE_call_statement = 31, RULE_block_stmt = 32, 
		RULE_expr_list = 33, RULE_expression = 34, RULE_expression1 = 35, RULE_expression2 = 36, 
		RULE_expression3 = 37, RULE_expression4 = 38, RULE_expression5 = 39, RULE_expression6 = 40, 
		RULE_operand = 41, RULE_element_access = 42, RULE_field_access = 43, RULE_call_expr = 44, 
		RULE_literal = 45, RULE_array_literal = 46, RULE_array_type = 47, RULE_type_name = 48, 
		RULE_struct_literal = 49, RULE_field_list = 50, RULE_field_init = 51;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declared", "variables_declared", "var_decl_list", "var_decl", 
			"constants_declared", "const_decl_list", "const_decl", "function_declared", 
			"method_declared", "receiver", "params_list", "param", "struct_declared", 
			"struct_type", "interface_declared", "interface_type", "statement", "declared_statement", 
			"assign_statement", "assign_lhs", "if_statement", "for_statement", "for_clause", 
			"for_init", "for_update", "range_clause", "assign_op", "break_statement", 
			"continue_statement", "return_statement", "call_statement", "block_stmt", 
			"expr_list", "expression", "expression1", "expression2", "expression3", 
			"expression4", "expression5", "expression6", "operand", "element_access", 
			"field_access", "call_expr", "literal", "array_literal", "array_type", 
			"type_name", "struct_literal", "field_list", "field_init"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'else'", "'for'", "'return'", "'break'", "'continue'", 
			"'func'", "'type'", "'var'", "'const'", "'struct'", "'interface'", "'string'", 
			"'int'", "'float'", "'boolean'", "'range'", "'nil'", "'true'", "'false'", 
			"'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", 
			"'>='", "'&&'", "'||'", "'!'", "'='", "'+='", "'-='", "'*='", "'/='", 
			"'%='", "'.'", "':'", "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", 
			"','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IF", "ELSE", "FOR", "RETURN", "BREAK", "CONTINUE", "FUNC", "TYPE", 
			"VAR", "CONST", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
			"RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
			"NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
			"AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
			"DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", "LP", "RP", "LSB", "RSB", 
			"LB", "RB", "SEMI", "COMMA", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
			"LINE_COMMENT", "BLOCK_COMMENT", "WS", "NEWLINE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
			"ERROR_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "MiniGo.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MiniGoParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(MiniGoParser.EOF, 0); }
		public List<DeclaredContext> declared() {
			return getRuleContexts(DeclaredContext.class);
		}
		public DeclaredContext declared(int i) {
			return getRuleContext(DeclaredContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1920L) != 0)) {
				{
				{
				setState(104);
				declared();
				}
				}
				setState(109);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(110);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaredContext extends ParserRuleContext {
		public Variables_declaredContext variables_declared() {
			return getRuleContext(Variables_declaredContext.class,0);
		}
		public Constants_declaredContext constants_declared() {
			return getRuleContext(Constants_declaredContext.class,0);
		}
		public Function_declaredContext function_declared() {
			return getRuleContext(Function_declaredContext.class,0);
		}
		public Method_declaredContext method_declared() {
			return getRuleContext(Method_declaredContext.class,0);
		}
		public Struct_declaredContext struct_declared() {
			return getRuleContext(Struct_declaredContext.class,0);
		}
		public Interface_declaredContext interface_declared() {
			return getRuleContext(Interface_declaredContext.class,0);
		}
		public DeclaredContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declared; }
	}

	public final DeclaredContext declared() throws RecognitionException {
		DeclaredContext _localctx = new DeclaredContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declared);
		try {
			setState(118);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(112);
				variables_declared();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(113);
				constants_declared();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(114);
				function_declared();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(115);
				method_declared();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(116);
				struct_declared();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(117);
				interface_declared();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Variables_declaredContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(MiniGoParser.VAR, 0); }
		public Var_decl_listContext var_decl_list() {
			return getRuleContext(Var_decl_listContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MiniGoParser.SEMI, 0); }
		public Variables_declaredContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variables_declared; }
	}

	public final Variables_declaredContext variables_declared() throws RecognitionException {
		Variables_declaredContext _localctx = new Variables_declaredContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_variables_declared);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(VAR);
			setState(121);
			var_decl_list();
			setState(122);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_decl_listContext extends ParserRuleContext {
		public List<Var_declContext> var_decl() {
			return getRuleContexts(Var_declContext.class);
		}
		public Var_declContext var_decl(int i) {
			return getRuleContext(Var_declContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiniGoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiniGoParser.COMMA, i);
		}
		public Var_decl_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl_list; }
	}

	public final Var_decl_listContext var_decl_list() throws RecognitionException {
		Var_decl_listContext _localctx = new Var_decl_listContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_var_decl_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			var_decl();
			setState(129);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(125);
				match(COMMA);
				setState(126);
				var_decl();
				}
				}
				setState(131);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_declContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(MiniGoParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MiniGoParser.ID, i);
		}
		public Type_nameContext type_name() {
			return getRuleContext(Type_nameContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(MiniGoParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiniGoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiniGoParser.COMMA, i);
		}
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public Var_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl; }
	}

	public final Var_declContext var_decl() throws RecognitionException {
		Var_declContext _localctx = new Var_declContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_var_decl);
		int _la;
		try {
			int _alt;
			setState(155);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(132);
				match(ID);
				setState(134);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2251799813808128L) != 0)) {
					{
					setState(133);
					type_name();
					}
				}

				setState(138);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGN) {
					{
					setState(136);
					match(ASSIGN);
					setState(137);
					expression(0);
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(140);
				match(ID);
				setState(145);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(141);
						match(COMMA);
						setState(142);
						match(ID);
						}
						} 
					}
					setState(147);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				}
				setState(149);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2251799813808128L) != 0)) {
					{
					setState(148);
					type_name();
					}
				}

				setState(153);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGN) {
					{
					setState(151);
					match(ASSIGN);
					setState(152);
					expr_list();
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Constants_declaredContext extends ParserRuleContext {
		public TerminalNode CONST() { return getToken(MiniGoParser.CONST, 0); }
		public Const_decl_listContext const_decl_list() {
			return getRuleContext(Const_decl_listContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MiniGoParser.SEMI, 0); }
		public Constants_declaredContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constants_declared; }
	}

	public final Constants_declaredContext constants_declared() throws RecognitionException {
		Constants_declaredContext _localctx = new Constants_declaredContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_constants_declared);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			match(CONST);
			setState(158);
			const_decl_list();
			setState(159);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Const_decl_listContext extends ParserRuleContext {
		public List<Const_declContext> const_decl() {
			return getRuleContexts(Const_declContext.class);
		}
		public Const_declContext const_decl(int i) {
			return getRuleContext(Const_declContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiniGoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiniGoParser.COMMA, i);
		}
		public Const_decl_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_const_decl_list; }
	}

	public final Const_decl_listContext const_decl_list() throws RecognitionException {
		Const_decl_listContext _localctx = new Const_decl_listContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_const_decl_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			const_decl();
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(162);
				match(COMMA);
				setState(163);
				const_decl();
				}
				}
				setState(168);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Const_declContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(MiniGoParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Const_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_const_decl; }
	}

	public final Const_declContext const_decl() throws RecognitionException {
		Const_declContext _localctx = new Const_declContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_const_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			match(ID);
			setState(170);
			match(ASSIGN);
			setState(171);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Function_declaredContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(MiniGoParser.FUNC, 0); }
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public TerminalNode LP() { return getToken(MiniGoParser.LP, 0); }
		public TerminalNode RP() { return getToken(MiniGoParser.RP, 0); }
		public Block_stmtContext block_stmt() {
			return getRuleContext(Block_stmtContext.class,0);
		}
		public Params_listContext params_list() {
			return getRuleContext(Params_listContext.class,0);
		}
		public Type_nameContext type_name() {
			return getRuleContext(Type_nameContext.class,0);
		}
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public Function_declaredContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_declared; }
	}

	public final Function_declaredContext function_declared() throws RecognitionException {
		Function_declaredContext _localctx = new Function_declaredContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_function_declared);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			match(FUNC);
			setState(174);
			match(ID);
			setState(175);
			match(LP);
			setState(177);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(176);
				params_list();
				}
			}

			setState(179);
			match(RP);
			setState(182);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRING:
			case INT:
			case FLOAT:
			case BOOLEAN:
			case ID:
				{
				setState(180);
				type_name();
				}
				break;
			case LSB:
				{
				setState(181);
				array_type();
				}
				break;
			case LB:
				break;
			default:
				break;
			}
			setState(184);
			block_stmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Method_declaredContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(MiniGoParser.FUNC, 0); }
		public List<TerminalNode> LP() { return getTokens(MiniGoParser.LP); }
		public TerminalNode LP(int i) {
			return getToken(MiniGoParser.LP, i);
		}
		public ReceiverContext receiver() {
			return getRuleContext(ReceiverContext.class,0);
		}
		public List<TerminalNode> RP() { return getTokens(MiniGoParser.RP); }
		public TerminalNode RP(int i) {
			return getToken(MiniGoParser.RP, i);
		}
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public Block_stmtContext block_stmt() {
			return getRuleContext(Block_stmtContext.class,0);
		}
		public Params_listContext params_list() {
			return getRuleContext(Params_listContext.class,0);
		}
		public Type_nameContext type_name() {
			return getRuleContext(Type_nameContext.class,0);
		}
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public Method_declaredContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_declared; }
	}

	public final Method_declaredContext method_declared() throws RecognitionException {
		Method_declaredContext _localctx = new Method_declaredContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_method_declared);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			match(FUNC);
			setState(187);
			match(LP);
			setState(188);
			receiver();
			setState(189);
			match(RP);
			setState(190);
			match(ID);
			setState(191);
			match(LP);
			setState(193);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(192);
				params_list();
				}
			}

			setState(195);
			match(RP);
			setState(198);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRING:
			case INT:
			case FLOAT:
			case BOOLEAN:
			case ID:
				{
				setState(196);
				type_name();
				}
				break;
			case LSB:
				{
				setState(197);
				array_type();
				}
				break;
			case LB:
				break;
			default:
				break;
			}
			setState(200);
			block_stmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReceiverContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public Type_nameContext type_name() {
			return getRuleContext(Type_nameContext.class,0);
		}
		public ReceiverContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_receiver; }
	}

	public final ReceiverContext receiver() throws RecognitionException {
		ReceiverContext _localctx = new ReceiverContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_receiver);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(ID);
			setState(203);
			type_name();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Params_listContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiniGoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiniGoParser.COMMA, i);
		}
		public Params_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params_list; }
	}

	public final Params_listContext params_list() throws RecognitionException {
		Params_listContext _localctx = new Params_listContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_params_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			param();
			setState(210);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(206);
				match(COMMA);
				setState(207);
				param();
				}
				}
				setState(212);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(MiniGoParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MiniGoParser.ID, i);
		}
		public Type_nameContext type_name() {
			return getRuleContext(Type_nameContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiniGoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiniGoParser.COMMA, i);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_param);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(ID);
			setState(218);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(214);
				match(COMMA);
				setState(215);
				match(ID);
				}
				}
				setState(220);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(221);
			type_name();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Struct_declaredContext extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(MiniGoParser.TYPE, 0); }
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public TerminalNode STRUCT() { return getToken(MiniGoParser.STRUCT, 0); }
		public TerminalNode LB() { return getToken(MiniGoParser.LB, 0); }
		public Struct_typeContext struct_type() {
			return getRuleContext(Struct_typeContext.class,0);
		}
		public TerminalNode RB() { return getToken(MiniGoParser.RB, 0); }
		public TerminalNode SEMI() { return getToken(MiniGoParser.SEMI, 0); }
		public Struct_declaredContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_struct_declared; }
	}

	public final Struct_declaredContext struct_declared() throws RecognitionException {
		Struct_declaredContext _localctx = new Struct_declaredContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_struct_declared);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			match(TYPE);
			setState(224);
			match(ID);
			setState(225);
			match(STRUCT);
			setState(226);
			match(LB);
			setState(227);
			struct_type();
			setState(228);
			match(RB);
			setState(230);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI) {
				{
				setState(229);
				match(SEMI);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Struct_typeContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(MiniGoParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MiniGoParser.ID, i);
		}
		public List<Type_nameContext> type_name() {
			return getRuleContexts(Type_nameContext.class);
		}
		public Type_nameContext type_name(int i) {
			return getRuleContext(Type_nameContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(MiniGoParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(MiniGoParser.SEMI, i);
		}
		public Struct_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_struct_type; }
	}

	public final Struct_typeContext struct_type() throws RecognitionException {
		Struct_typeContext _localctx = new Struct_typeContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_struct_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(232);
				match(ID);
				setState(233);
				type_name();
				setState(234);
				match(SEMI);
				}
				}
				setState(240);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Interface_declaredContext extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(MiniGoParser.TYPE, 0); }
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public TerminalNode INTERFACE() { return getToken(MiniGoParser.INTERFACE, 0); }
		public TerminalNode LB() { return getToken(MiniGoParser.LB, 0); }
		public Interface_typeContext interface_type() {
			return getRuleContext(Interface_typeContext.class,0);
		}
		public TerminalNode RB() { return getToken(MiniGoParser.RB, 0); }
		public TerminalNode SEMI() { return getToken(MiniGoParser.SEMI, 0); }
		public Interface_declaredContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_declared; }
	}

	public final Interface_declaredContext interface_declared() throws RecognitionException {
		Interface_declaredContext _localctx = new Interface_declaredContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_interface_declared);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			match(TYPE);
			setState(242);
			match(ID);
			setState(243);
			match(INTERFACE);
			setState(244);
			match(LB);
			setState(245);
			interface_type();
			setState(246);
			match(RB);
			setState(248);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI) {
				{
				setState(247);
				match(SEMI);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Interface_typeContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(MiniGoParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MiniGoParser.ID, i);
		}
		public List<TerminalNode> LP() { return getTokens(MiniGoParser.LP); }
		public TerminalNode LP(int i) {
			return getToken(MiniGoParser.LP, i);
		}
		public List<TerminalNode> RP() { return getTokens(MiniGoParser.RP); }
		public TerminalNode RP(int i) {
			return getToken(MiniGoParser.RP, i);
		}
		public List<TerminalNode> SEMI() { return getTokens(MiniGoParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(MiniGoParser.SEMI, i);
		}
		public List<Params_listContext> params_list() {
			return getRuleContexts(Params_listContext.class);
		}
		public Params_listContext params_list(int i) {
			return getRuleContext(Params_listContext.class,i);
		}
		public List<Type_nameContext> type_name() {
			return getRuleContexts(Type_nameContext.class);
		}
		public Type_nameContext type_name(int i) {
			return getRuleContext(Type_nameContext.class,i);
		}
		public List<Array_typeContext> array_type() {
			return getRuleContexts(Array_typeContext.class);
		}
		public Array_typeContext array_type(int i) {
			return getRuleContext(Array_typeContext.class,i);
		}
		public Interface_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_type; }
	}

	public final Interface_typeContext interface_type() throws RecognitionException {
		Interface_typeContext _localctx = new Interface_typeContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_interface_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(250);
				match(ID);
				setState(251);
				match(LP);
				setState(253);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(252);
					params_list();
					}
				}

				setState(255);
				match(RP);
				setState(258);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case STRING:
				case INT:
				case FLOAT:
				case BOOLEAN:
				case ID:
					{
					setState(256);
					type_name();
					}
					break;
				case LSB:
					{
					setState(257);
					array_type();
					}
					break;
				case SEMI:
					break;
				default:
					break;
				}
				setState(260);
				match(SEMI);
				}
				}
				setState(265);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public Declared_statementContext declared_statement() {
			return getRuleContext(Declared_statementContext.class,0);
		}
		public Assign_statementContext assign_statement() {
			return getRuleContext(Assign_statementContext.class,0);
		}
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public For_statementContext for_statement() {
			return getRuleContext(For_statementContext.class,0);
		}
		public Break_statementContext break_statement() {
			return getRuleContext(Break_statementContext.class,0);
		}
		public Continue_statementContext continue_statement() {
			return getRuleContext(Continue_statementContext.class,0);
		}
		public Return_statementContext return_statement() {
			return getRuleContext(Return_statementContext.class,0);
		}
		public Call_statementContext call_statement() {
			return getRuleContext(Call_statementContext.class,0);
		}
		public Block_stmtContext block_stmt() {
			return getRuleContext(Block_stmtContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_statement);
		try {
			setState(275);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(266);
				declared_statement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(267);
				assign_statement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(268);
				if_statement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(269);
				for_statement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(270);
				break_statement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(271);
				continue_statement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(272);
				return_statement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(273);
				call_statement();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(274);
				block_stmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Declared_statementContext extends ParserRuleContext {
		public Variables_declaredContext variables_declared() {
			return getRuleContext(Variables_declaredContext.class,0);
		}
		public Constants_declaredContext constants_declared() {
			return getRuleContext(Constants_declaredContext.class,0);
		}
		public Declared_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declared_statement; }
	}

	public final Declared_statementContext declared_statement() throws RecognitionException {
		Declared_statementContext _localctx = new Declared_statementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_declared_statement);
		try {
			setState(279);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(277);
				variables_declared();
				}
				break;
			case CONST:
				enterOuterAlt(_localctx, 2);
				{
				setState(278);
				constants_declared();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Assign_statementContext extends ParserRuleContext {
		public Assign_lhsContext assign_lhs() {
			return getRuleContext(Assign_lhsContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MiniGoParser.SEMI, 0); }
		public TerminalNode ASSIGN() { return getToken(MiniGoParser.ASSIGN, 0); }
		public TerminalNode ADD_ASSIGN() { return getToken(MiniGoParser.ADD_ASSIGN, 0); }
		public TerminalNode SUB_ASSIGN() { return getToken(MiniGoParser.SUB_ASSIGN, 0); }
		public TerminalNode MUL_ASSIGN() { return getToken(MiniGoParser.MUL_ASSIGN, 0); }
		public TerminalNode DIV_ASSIGN() { return getToken(MiniGoParser.DIV_ASSIGN, 0); }
		public TerminalNode MOD_ASSIGN() { return getToken(MiniGoParser.MOD_ASSIGN, 0); }
		public Assign_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_statement; }
	}

	public final Assign_statementContext assign_statement() throws RecognitionException {
		Assign_statementContext _localctx = new Assign_statementContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_assign_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(281);
			assign_lhs();
			setState(282);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2164663517184L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(283);
			expression(0);
			setState(284);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Assign_lhsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public Element_accessContext element_access() {
			return getRuleContext(Element_accessContext.class,0);
		}
		public Field_accessContext field_access() {
			return getRuleContext(Field_accessContext.class,0);
		}
		public Assign_lhsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_lhs; }
	}

	public final Assign_lhsContext assign_lhs() throws RecognitionException {
		Assign_lhsContext _localctx = new Assign_lhsContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_assign_lhs);
		try {
			setState(291);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(286);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(287);
				match(ID);
				setState(288);
				element_access();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(289);
				match(ID);
				setState(290);
				field_access();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class If_statementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(MiniGoParser.IF, 0); }
		public TerminalNode LP() { return getToken(MiniGoParser.LP, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RP() { return getToken(MiniGoParser.RP, 0); }
		public List<Block_stmtContext> block_stmt() {
			return getRuleContexts(Block_stmtContext.class);
		}
		public Block_stmtContext block_stmt(int i) {
			return getRuleContext(Block_stmtContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(MiniGoParser.ELSE, 0); }
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public If_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_statement; }
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_if_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(293);
			match(IF);
			setState(294);
			match(LP);
			setState(295);
			expression(0);
			setState(296);
			match(RP);
			setState(297);
			block_stmt();
			setState(303);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(298);
				match(ELSE);
				setState(301);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case IF:
					{
					setState(299);
					if_statement();
					}
					break;
				case LB:
					{
					setState(300);
					block_stmt();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_statementContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(MiniGoParser.FOR, 0); }
		public Block_stmtContext block_stmt() {
			return getRuleContext(Block_stmtContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public For_clauseContext for_clause() {
			return getRuleContext(For_clauseContext.class,0);
		}
		public Range_clauseContext range_clause() {
			return getRuleContext(Range_clauseContext.class,0);
		}
		public For_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_statement; }
	}

	public final For_statementContext for_statement() throws RecognitionException {
		For_statementContext _localctx = new For_statementContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_for_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(305);
			match(FOR);
			setState(309);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				{
				setState(306);
				expression(0);
				}
				break;
			case 2:
				{
				setState(307);
				for_clause();
				}
				break;
			case 3:
				{
				setState(308);
				range_clause();
				}
				break;
			}
			setState(311);
			block_stmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_clauseContext extends ParserRuleContext {
		public List<TerminalNode> SEMI() { return getTokens(MiniGoParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(MiniGoParser.SEMI, i);
		}
		public For_initContext for_init() {
			return getRuleContext(For_initContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public For_updateContext for_update() {
			return getRuleContext(For_updateContext.class,0);
		}
		public For_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_clause; }
	}

	public final For_clauseContext for_clause() throws RecognitionException {
		For_clauseContext _localctx = new For_clauseContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_for_clause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(314);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR || _la==ID) {
				{
				setState(313);
				for_init();
				}
			}

			setState(316);
			match(SEMI);
			setState(318);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 33820994856288256L) != 0)) {
				{
				setState(317);
				expression(0);
				}
			}

			setState(320);
			match(SEMI);
			setState(322);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(321);
				for_update();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_initContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(MiniGoParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode VAR() { return getToken(MiniGoParser.VAR, 0); }
		public Type_nameContext type_name() {
			return getRuleContext(Type_nameContext.class,0);
		}
		public For_initContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_init; }
	}

	public final For_initContext for_init() throws RecognitionException {
		For_initContext _localctx = new For_initContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_for_init);
		int _la;
		try {
			setState(334);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(324);
				match(ID);
				setState(325);
				match(ASSIGN);
				setState(326);
				expression(0);
				}
				break;
			case VAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(327);
				match(VAR);
				setState(328);
				match(ID);
				setState(330);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2251799813808128L) != 0)) {
					{
					setState(329);
					type_name();
					}
				}

				setState(332);
				match(ASSIGN);
				setState(333);
				expression(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_updateContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public Assign_opContext assign_op() {
			return getRuleContext(Assign_opContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public For_updateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_update; }
	}

	public final For_updateContext for_update() throws RecognitionException {
		For_updateContext _localctx = new For_updateContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_for_update);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(336);
			match(ID);
			setState(337);
			assign_op();
			setState(338);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Range_clauseContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(MiniGoParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MiniGoParser.ID, i);
		}
		public TerminalNode COMMA() { return getToken(MiniGoParser.COMMA, 0); }
		public TerminalNode RANGE() { return getToken(MiniGoParser.RANGE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Range_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_range_clause; }
	}

	public final Range_clauseContext range_clause() throws RecognitionException {
		Range_clauseContext _localctx = new Range_clauseContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_range_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(340);
			match(ID);
			setState(341);
			match(COMMA);
			setState(342);
			match(ID);
			setState(343);
			match(RANGE);
			setState(344);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Assign_opContext extends ParserRuleContext {
		public TerminalNode ASSIGN() { return getToken(MiniGoParser.ASSIGN, 0); }
		public TerminalNode ADD_ASSIGN() { return getToken(MiniGoParser.ADD_ASSIGN, 0); }
		public TerminalNode SUB_ASSIGN() { return getToken(MiniGoParser.SUB_ASSIGN, 0); }
		public TerminalNode MUL_ASSIGN() { return getToken(MiniGoParser.MUL_ASSIGN, 0); }
		public TerminalNode DIV_ASSIGN() { return getToken(MiniGoParser.DIV_ASSIGN, 0); }
		public TerminalNode MOD_ASSIGN() { return getToken(MiniGoParser.MOD_ASSIGN, 0); }
		public Assign_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_op; }
	}

	public final Assign_opContext assign_op() throws RecognitionException {
		Assign_opContext _localctx = new Assign_opContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_assign_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(346);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2164663517184L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Break_statementContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(MiniGoParser.BREAK, 0); }
		public TerminalNode SEMI() { return getToken(MiniGoParser.SEMI, 0); }
		public Break_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_statement; }
	}

	public final Break_statementContext break_statement() throws RecognitionException {
		Break_statementContext _localctx = new Break_statementContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_break_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(348);
			match(BREAK);
			setState(349);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Continue_statementContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(MiniGoParser.CONTINUE, 0); }
		public TerminalNode SEMI() { return getToken(MiniGoParser.SEMI, 0); }
		public Continue_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_statement; }
	}

	public final Continue_statementContext continue_statement() throws RecognitionException {
		Continue_statementContext _localctx = new Continue_statementContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_continue_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(351);
			match(CONTINUE);
			setState(352);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Return_statementContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(MiniGoParser.RETURN, 0); }
		public TerminalNode SEMI() { return getToken(MiniGoParser.SEMI, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Return_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_statement; }
	}

	public final Return_statementContext return_statement() throws RecognitionException {
		Return_statementContext _localctx = new Return_statementContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_return_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(354);
			match(RETURN);
			setState(356);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 33820994856288256L) != 0)) {
				{
				setState(355);
				expression(0);
				}
			}

			setState(358);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Call_statementContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(MiniGoParser.LP, 0); }
		public TerminalNode RP() { return getToken(MiniGoParser.RP, 0); }
		public TerminalNode SEMI() { return getToken(MiniGoParser.SEMI, 0); }
		public List<TerminalNode> ID() { return getTokens(MiniGoParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(MiniGoParser.ID, i);
		}
		public TerminalNode DOT() { return getToken(MiniGoParser.DOT, 0); }
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public Call_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_statement; }
	}

	public final Call_statementContext call_statement() throws RecognitionException {
		Call_statementContext _localctx = new Call_statementContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_call_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(364);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				{
				setState(360);
				match(ID);
				}
				break;
			case 2:
				{
				setState(361);
				match(ID);
				setState(362);
				match(DOT);
				setState(363);
				match(ID);
				}
				break;
			}
			setState(366);
			match(LP);
			setState(368);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 33820994856288256L) != 0)) {
				{
				setState(367);
				expr_list();
				}
			}

			setState(370);
			match(RP);
			setState(371);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Block_stmtContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(MiniGoParser.LB, 0); }
		public TerminalNode RB() { return getToken(MiniGoParser.RB, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public Block_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_stmt; }
	}

	public final Block_stmtContext block_stmt() throws RecognitionException {
		Block_stmtContext _localctx = new Block_stmtContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_block_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(373);
			match(LB);
			setState(377);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2392537302042234L) != 0)) {
				{
				{
				setState(374);
				statement();
				}
				}
				setState(379);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(380);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_listContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiniGoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiniGoParser.COMMA, i);
		}
		public Expr_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_list; }
	}

	public final Expr_listContext expr_list() throws RecognitionException {
		Expr_listContext _localctx = new Expr_listContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_expr_list);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(382);
			expression(0);
			setState(387);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(383);
					match(COMMA);
					setState(384);
					expression(0);
					}
					} 
				}
				setState(389);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public Expression1Context expression1() {
			return getRuleContext(Expression1Context.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode OR() { return getToken(MiniGoParser.OR, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 68;
		enterRecursionRule(_localctx, 68, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(391);
			expression1(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(398);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,38,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpressionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression);
					setState(393);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(394);
					match(OR);
					setState(395);
					expression1(0);
					}
					} 
				}
				setState(400);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,38,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expression1Context extends ParserRuleContext {
		public Expression2Context expression2() {
			return getRuleContext(Expression2Context.class,0);
		}
		public Expression1Context expression1() {
			return getRuleContext(Expression1Context.class,0);
		}
		public TerminalNode AND() { return getToken(MiniGoParser.AND, 0); }
		public Expression1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression1; }
	}

	public final Expression1Context expression1() throws RecognitionException {
		return expression1(0);
	}

	private Expression1Context expression1(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expression1Context _localctx = new Expression1Context(_ctx, _parentState);
		Expression1Context _prevctx = _localctx;
		int _startState = 70;
		enterRecursionRule(_localctx, 70, RULE_expression1, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(402);
			expression2(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(409);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,39,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression1Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression1);
					setState(404);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(405);
					match(AND);
					setState(406);
					expression2(0);
					}
					} 
				}
				setState(411);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,39,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expression2Context extends ParserRuleContext {
		public Expression3Context expression3() {
			return getRuleContext(Expression3Context.class,0);
		}
		public Expression2Context expression2() {
			return getRuleContext(Expression2Context.class,0);
		}
		public TerminalNode EQUAL() { return getToken(MiniGoParser.EQUAL, 0); }
		public TerminalNode NOT_EQUAL() { return getToken(MiniGoParser.NOT_EQUAL, 0); }
		public TerminalNode LESS() { return getToken(MiniGoParser.LESS, 0); }
		public TerminalNode LESS_OR_EQUAL() { return getToken(MiniGoParser.LESS_OR_EQUAL, 0); }
		public TerminalNode GREATER() { return getToken(MiniGoParser.GREATER, 0); }
		public TerminalNode GREATER_OR_EQUAL() { return getToken(MiniGoParser.GREATER_OR_EQUAL, 0); }
		public Expression2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression2; }
	}

	public final Expression2Context expression2() throws RecognitionException {
		return expression2(0);
	}

	private Expression2Context expression2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expression2Context _localctx = new Expression2Context(_ctx, _parentState);
		Expression2Context _prevctx = _localctx;
		int _startState = 72;
		enterRecursionRule(_localctx, 72, RULE_expression2, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(413);
			expression3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(420);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression2Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression2);
					setState(415);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(416);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4227858432L) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(417);
					expression3(0);
					}
					} 
				}
				setState(422);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expression3Context extends ParserRuleContext {
		public Expression4Context expression4() {
			return getRuleContext(Expression4Context.class,0);
		}
		public Expression3Context expression3() {
			return getRuleContext(Expression3Context.class,0);
		}
		public TerminalNode ADD() { return getToken(MiniGoParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(MiniGoParser.SUB, 0); }
		public Expression3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression3; }
	}

	public final Expression3Context expression3() throws RecognitionException {
		return expression3(0);
	}

	private Expression3Context expression3(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expression3Context _localctx = new Expression3Context(_ctx, _parentState);
		Expression3Context _prevctx = _localctx;
		int _startState = 74;
		enterRecursionRule(_localctx, 74, RULE_expression3, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(424);
			expression4(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(431);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,41,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression3Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression3);
					setState(426);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(427);
					_la = _input.LA(1);
					if ( !(_la==ADD || _la==SUB) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(428);
					expression4(0);
					}
					} 
				}
				setState(433);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,41,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expression4Context extends ParserRuleContext {
		public Expression5Context expression5() {
			return getRuleContext(Expression5Context.class,0);
		}
		public Expression4Context expression4() {
			return getRuleContext(Expression4Context.class,0);
		}
		public TerminalNode MUL() { return getToken(MiniGoParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(MiniGoParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(MiniGoParser.MOD, 0); }
		public Expression4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression4; }
	}

	public final Expression4Context expression4() throws RecognitionException {
		return expression4(0);
	}

	private Expression4Context expression4(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expression4Context _localctx = new Expression4Context(_ctx, _parentState);
		Expression4Context _prevctx = _localctx;
		int _startState = 76;
		enterRecursionRule(_localctx, 76, RULE_expression4, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(435);
			expression5();
			}
			_ctx.stop = _input.LT(-1);
			setState(442);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,42,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression4Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression4);
					setState(437);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(438);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 58720256L) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(439);
					expression5();
					}
					} 
				}
				setState(444);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,42,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expression5Context extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(MiniGoParser.NOT, 0); }
		public Expression5Context expression5() {
			return getRuleContext(Expression5Context.class,0);
		}
		public TerminalNode SUB() { return getToken(MiniGoParser.SUB, 0); }
		public Expression6Context expression6() {
			return getRuleContext(Expression6Context.class,0);
		}
		public Expression5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression5; }
	}

	public final Expression5Context expression5() throws RecognitionException {
		Expression5Context _localctx = new Expression5Context(_ctx, getState());
		enterRule(_localctx, 78, RULE_expression5);
		try {
			setState(450);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(445);
				match(NOT);
				setState(446);
				expression5();
				}
				break;
			case SUB:
				enterOuterAlt(_localctx, 2);
				{
				setState(447);
				match(SUB);
				setState(448);
				expression5();
				}
				break;
			case NIL:
			case TRUE:
			case FALSE:
			case LP:
			case LSB:
			case ID:
			case INT_LIT:
			case FLOAT_LIT:
			case STRING_LIT:
				enterOuterAlt(_localctx, 3);
				{
				setState(449);
				expression6();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expression6Context extends ParserRuleContext {
		public OperandContext operand() {
			return getRuleContext(OperandContext.class,0);
		}
		public List<Element_accessContext> element_access() {
			return getRuleContexts(Element_accessContext.class);
		}
		public Element_accessContext element_access(int i) {
			return getRuleContext(Element_accessContext.class,i);
		}
		public List<Field_accessContext> field_access() {
			return getRuleContexts(Field_accessContext.class);
		}
		public Field_accessContext field_access(int i) {
			return getRuleContext(Field_accessContext.class,i);
		}
		public List<Call_exprContext> call_expr() {
			return getRuleContexts(Call_exprContext.class);
		}
		public Call_exprContext call_expr(int i) {
			return getRuleContext(Call_exprContext.class,i);
		}
		public Expression6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression6; }
	}

	public final Expression6Context expression6() throws RecognitionException {
		Expression6Context _localctx = new Expression6Context(_ctx, getState());
		enterRule(_localctx, 80, RULE_expression6);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(452);
			operand();
			setState(458);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,45,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(456);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case LSB:
						{
						setState(453);
						element_access();
						}
						break;
					case DOT:
						{
						setState(454);
						field_access();
						}
						break;
					case LP:
						{
						setState(455);
						call_expr();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(460);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,45,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperandContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public TerminalNode LP() { return getToken(MiniGoParser.LP, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RP() { return getToken(MiniGoParser.RP, 0); }
		public OperandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operand; }
	}

	public final OperandContext operand() throws RecognitionException {
		OperandContext _localctx = new OperandContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_operand);
		try {
			setState(467);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(461);
				literal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(462);
				match(ID);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(463);
				match(LP);
				setState(464);
				expression(0);
				setState(465);
				match(RP);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Element_accessContext extends ParserRuleContext {
		public TerminalNode LSB() { return getToken(MiniGoParser.LSB, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RSB() { return getToken(MiniGoParser.RSB, 0); }
		public Element_accessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element_access; }
	}

	public final Element_accessContext element_access() throws RecognitionException {
		Element_accessContext _localctx = new Element_accessContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_element_access);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(469);
			match(LSB);
			setState(470);
			expression(0);
			setState(471);
			match(RSB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Field_accessContext extends ParserRuleContext {
		public TerminalNode DOT() { return getToken(MiniGoParser.DOT, 0); }
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public Field_accessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_access; }
	}

	public final Field_accessContext field_access() throws RecognitionException {
		Field_accessContext _localctx = new Field_accessContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_field_access);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(473);
			match(DOT);
			setState(474);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Call_exprContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(MiniGoParser.LP, 0); }
		public TerminalNode RP() { return getToken(MiniGoParser.RP, 0); }
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public Call_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_expr; }
	}

	public final Call_exprContext call_expr() throws RecognitionException {
		Call_exprContext _localctx = new Call_exprContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_call_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(476);
			match(LP);
			setState(478);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 33820994856288256L) != 0)) {
				{
				setState(477);
				expr_list();
				}
			}

			setState(480);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INT_LIT() { return getToken(MiniGoParser.INT_LIT, 0); }
		public TerminalNode FLOAT_LIT() { return getToken(MiniGoParser.FLOAT_LIT, 0); }
		public TerminalNode STRING_LIT() { return getToken(MiniGoParser.STRING_LIT, 0); }
		public Array_literalContext array_literal() {
			return getRuleContext(Array_literalContext.class,0);
		}
		public Struct_literalContext struct_literal() {
			return getRuleContext(Struct_literalContext.class,0);
		}
		public TerminalNode TRUE() { return getToken(MiniGoParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(MiniGoParser.FALSE, 0); }
		public TerminalNode NIL() { return getToken(MiniGoParser.NIL, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_literal);
		try {
			setState(490);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_LIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(482);
				match(INT_LIT);
				}
				break;
			case FLOAT_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(483);
				match(FLOAT_LIT);
				}
				break;
			case STRING_LIT:
				enterOuterAlt(_localctx, 3);
				{
				setState(484);
				match(STRING_LIT);
				}
				break;
			case LSB:
				enterOuterAlt(_localctx, 4);
				{
				setState(485);
				array_literal();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 5);
				{
				setState(486);
				struct_literal();
				}
				break;
			case TRUE:
				enterOuterAlt(_localctx, 6);
				{
				setState(487);
				match(TRUE);
				}
				break;
			case FALSE:
				enterOuterAlt(_localctx, 7);
				{
				setState(488);
				match(FALSE);
				}
				break;
			case NIL:
				enterOuterAlt(_localctx, 8);
				{
				setState(489);
				match(NIL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Array_literalContext extends ParserRuleContext {
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public TerminalNode LB() { return getToken(MiniGoParser.LB, 0); }
		public TerminalNode RB() { return getToken(MiniGoParser.RB, 0); }
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public Array_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_literal; }
	}

	public final Array_literalContext array_literal() throws RecognitionException {
		Array_literalContext _localctx = new Array_literalContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_array_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(492);
			array_type();
			setState(493);
			match(LB);
			setState(495);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 33820994856288256L) != 0)) {
				{
				setState(494);
				expr_list();
				}
			}

			setState(497);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Array_typeContext extends ParserRuleContext {
		public List<TerminalNode> LSB() { return getTokens(MiniGoParser.LSB); }
		public TerminalNode LSB(int i) {
			return getToken(MiniGoParser.LSB, i);
		}
		public List<TerminalNode> INT_LIT() { return getTokens(MiniGoParser.INT_LIT); }
		public TerminalNode INT_LIT(int i) {
			return getToken(MiniGoParser.INT_LIT, i);
		}
		public List<TerminalNode> RSB() { return getTokens(MiniGoParser.RSB); }
		public TerminalNode RSB(int i) {
			return getToken(MiniGoParser.RSB, i);
		}
		public Type_nameContext type_name() {
			return getRuleContext(Type_nameContext.class,0);
		}
		public Array_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_type; }
	}

	public final Array_typeContext array_type() throws RecognitionException {
		Array_typeContext _localctx = new Array_typeContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_array_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(499);
			match(LSB);
			setState(500);
			match(INT_LIT);
			setState(501);
			match(RSB);
			setState(507);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LSB) {
				{
				{
				setState(502);
				match(LSB);
				setState(503);
				match(INT_LIT);
				setState(504);
				match(RSB);
				}
				}
				setState(509);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(510);
			type_name();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Type_nameContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(MiniGoParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(MiniGoParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(MiniGoParser.STRING, 0); }
		public TerminalNode BOOLEAN() { return getToken(MiniGoParser.BOOLEAN, 0); }
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public Type_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_name; }
	}

	public final Type_nameContext type_name() throws RecognitionException {
		Type_nameContext _localctx = new Type_nameContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_type_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(512);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2251799813808128L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Struct_literalContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public TerminalNode LB() { return getToken(MiniGoParser.LB, 0); }
		public TerminalNode RB() { return getToken(MiniGoParser.RB, 0); }
		public Field_listContext field_list() {
			return getRuleContext(Field_listContext.class,0);
		}
		public Struct_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_struct_literal; }
	}

	public final Struct_literalContext struct_literal() throws RecognitionException {
		Struct_literalContext _localctx = new Struct_literalContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_struct_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(514);
			match(ID);
			setState(515);
			match(LB);
			setState(517);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(516);
				field_list();
				}
			}

			setState(519);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Field_listContext extends ParserRuleContext {
		public List<Field_initContext> field_init() {
			return getRuleContexts(Field_initContext.class);
		}
		public Field_initContext field_init(int i) {
			return getRuleContext(Field_initContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiniGoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiniGoParser.COMMA, i);
		}
		public Field_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_list; }
	}

	public final Field_listContext field_list() throws RecognitionException {
		Field_listContext _localctx = new Field_listContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_field_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(521);
			field_init();
			setState(526);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(522);
				match(COMMA);
				setState(523);
				field_init();
				}
				}
				setState(528);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Field_initContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MiniGoParser.ID, 0); }
		public TerminalNode COLON() { return getToken(MiniGoParser.COLON, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Field_initContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_init; }
	}

	public final Field_initContext field_init() throws RecognitionException {
		Field_initContext _localctx = new Field_initContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_field_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(529);
			match(ID);
			setState(530);
			match(COLON);
			setState(531);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 34:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		case 35:
			return expression1_sempred((Expression1Context)_localctx, predIndex);
		case 36:
			return expression2_sempred((Expression2Context)_localctx, predIndex);
		case 37:
			return expression3_sempred((Expression3Context)_localctx, predIndex);
		case 38:
			return expression4_sempred((Expression4Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expression1_sempred(Expression1Context _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expression2_sempred(Expression2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expression3_sempred(Expression3Context _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expression4_sempred(Expression4Context _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001=\u0216\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007,\u0002"+
		"-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u00070\u00021\u00071\u0002"+
		"2\u00072\u00023\u00073\u0001\u0000\u0005\u0000j\b\u0000\n\u0000\f\u0000"+
		"m\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001w\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0005\u0003\u0080\b\u0003\n\u0003\f\u0003\u0083\t\u0003\u0001\u0004\u0001"+
		"\u0004\u0003\u0004\u0087\b\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u008b"+
		"\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004\u0090\b\u0004"+
		"\n\u0004\f\u0004\u0093\t\u0004\u0001\u0004\u0003\u0004\u0096\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0003\u0004\u009a\b\u0004\u0003\u0004\u009c\b\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0005\u0006\u00a5\b\u0006\n\u0006\f\u0006\u00a8\t\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0003\b\u00b2\b\b\u0001\b\u0001\b\u0001\b\u0003\b\u00b7\b\b\u0001\b"+
		"\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003"+
		"\t\u00c2\b\t\u0001\t\u0001\t\u0001\t\u0003\t\u00c7\b\t\u0001\t\u0001\t"+
		"\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b"+
		"\u00d1\b\u000b\n\u000b\f\u000b\u00d4\t\u000b\u0001\f\u0001\f\u0001\f\u0005"+
		"\f\u00d9\b\f\n\f\f\f\u00dc\t\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r"+
		"\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00e7\b\r\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0005\u000e\u00ed\b\u000e\n\u000e\f\u000e\u00f0"+
		"\t\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0003\u000f\u00f9\b\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0003\u0010\u00fe\b\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0003"+
		"\u0010\u0103\b\u0010\u0001\u0010\u0005\u0010\u0106\b\u0010\n\u0010\f\u0010"+
		"\u0109\t\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u0114\b\u0011"+
		"\u0001\u0012\u0001\u0012\u0003\u0012\u0118\b\u0012\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0003\u0014\u0124\b\u0014\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0003\u0015\u012e\b\u0015\u0003\u0015\u0130\b\u0015\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0003\u0016\u0136\b\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0017\u0003\u0017\u013b\b\u0017\u0001\u0017\u0001\u0017\u0003"+
		"\u0017\u013f\b\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u0143\b\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0003\u0018\u014b\b\u0018\u0001\u0018\u0001\u0018\u0003\u0018\u014f\b"+
		"\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001"+
		"\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001"+
		"\u001d\u0001\u001e\u0001\u001e\u0003\u001e\u0165\b\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0003\u001f\u016d"+
		"\b\u001f\u0001\u001f\u0001\u001f\u0003\u001f\u0171\b\u001f\u0001\u001f"+
		"\u0001\u001f\u0001\u001f\u0001 \u0001 \u0005 \u0178\b \n \f \u017b\t "+
		"\u0001 \u0001 \u0001!\u0001!\u0001!\u0005!\u0182\b!\n!\f!\u0185\t!\u0001"+
		"\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0005\"\u018d\b\"\n\"\f\"\u0190"+
		"\t\"\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0005#\u0198\b#\n#\f#\u019b"+
		"\t#\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0005$\u01a3\b$\n$\f$\u01a6"+
		"\t$\u0001%\u0001%\u0001%\u0001%\u0001%\u0001%\u0005%\u01ae\b%\n%\f%\u01b1"+
		"\t%\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0005&\u01b9\b&\n&\f&\u01bc"+
		"\t&\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'\u0003\'\u01c3\b\'\u0001(\u0001"+
		"(\u0001(\u0001(\u0005(\u01c9\b(\n(\f(\u01cc\t(\u0001)\u0001)\u0001)\u0001"+
		")\u0001)\u0001)\u0003)\u01d4\b)\u0001*\u0001*\u0001*\u0001*\u0001+\u0001"+
		"+\u0001+\u0001,\u0001,\u0003,\u01df\b,\u0001,\u0001,\u0001-\u0001-\u0001"+
		"-\u0001-\u0001-\u0001-\u0001-\u0001-\u0003-\u01eb\b-\u0001.\u0001.\u0001"+
		".\u0003.\u01f0\b.\u0001.\u0001.\u0001/\u0001/\u0001/\u0001/\u0001/\u0001"+
		"/\u0005/\u01fa\b/\n/\f/\u01fd\t/\u0001/\u0001/\u00010\u00010\u00011\u0001"+
		"1\u00011\u00031\u0206\b1\u00011\u00011\u00012\u00012\u00012\u00052\u020d"+
		"\b2\n2\f2\u0210\t2\u00013\u00013\u00013\u00013\u00013\u0000\u0005DFHJ"+
		"L4\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a"+
		"\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPRTVXZ\\^`bdf\u0000\u0005\u0001\u0000"+
		"#(\u0001\u0000\u001a\u001f\u0001\u0000\u0015\u0016\u0001\u0000\u0017\u0019"+
		"\u0002\u0000\r\u001033\u022f\u0000k\u0001\u0000\u0000\u0000\u0002v\u0001"+
		"\u0000\u0000\u0000\u0004x\u0001\u0000\u0000\u0000\u0006|\u0001\u0000\u0000"+
		"\u0000\b\u009b\u0001\u0000\u0000\u0000\n\u009d\u0001\u0000\u0000\u0000"+
		"\f\u00a1\u0001\u0000\u0000\u0000\u000e\u00a9\u0001\u0000\u0000\u0000\u0010"+
		"\u00ad\u0001\u0000\u0000\u0000\u0012\u00ba\u0001\u0000\u0000\u0000\u0014"+
		"\u00ca\u0001\u0000\u0000\u0000\u0016\u00cd\u0001\u0000\u0000\u0000\u0018"+
		"\u00d5\u0001\u0000\u0000\u0000\u001a\u00df\u0001\u0000\u0000\u0000\u001c"+
		"\u00ee\u0001\u0000\u0000\u0000\u001e\u00f1\u0001\u0000\u0000\u0000 \u0107"+
		"\u0001\u0000\u0000\u0000\"\u0113\u0001\u0000\u0000\u0000$\u0117\u0001"+
		"\u0000\u0000\u0000&\u0119\u0001\u0000\u0000\u0000(\u0123\u0001\u0000\u0000"+
		"\u0000*\u0125\u0001\u0000\u0000\u0000,\u0131\u0001\u0000\u0000\u0000."+
		"\u013a\u0001\u0000\u0000\u00000\u014e\u0001\u0000\u0000\u00002\u0150\u0001"+
		"\u0000\u0000\u00004\u0154\u0001\u0000\u0000\u00006\u015a\u0001\u0000\u0000"+
		"\u00008\u015c\u0001\u0000\u0000\u0000:\u015f\u0001\u0000\u0000\u0000<"+
		"\u0162\u0001\u0000\u0000\u0000>\u016c\u0001\u0000\u0000\u0000@\u0175\u0001"+
		"\u0000\u0000\u0000B\u017e\u0001\u0000\u0000\u0000D\u0186\u0001\u0000\u0000"+
		"\u0000F\u0191\u0001\u0000\u0000\u0000H\u019c\u0001\u0000\u0000\u0000J"+
		"\u01a7\u0001\u0000\u0000\u0000L\u01b2\u0001\u0000\u0000\u0000N\u01c2\u0001"+
		"\u0000\u0000\u0000P\u01c4\u0001\u0000\u0000\u0000R\u01d3\u0001\u0000\u0000"+
		"\u0000T\u01d5\u0001\u0000\u0000\u0000V\u01d9\u0001\u0000\u0000\u0000X"+
		"\u01dc\u0001\u0000\u0000\u0000Z\u01ea\u0001\u0000\u0000\u0000\\\u01ec"+
		"\u0001\u0000\u0000\u0000^\u01f3\u0001\u0000\u0000\u0000`\u0200\u0001\u0000"+
		"\u0000\u0000b\u0202\u0001\u0000\u0000\u0000d\u0209\u0001\u0000\u0000\u0000"+
		"f\u0211\u0001\u0000\u0000\u0000hj\u0003\u0002\u0001\u0000ih\u0001\u0000"+
		"\u0000\u0000jm\u0001\u0000\u0000\u0000ki\u0001\u0000\u0000\u0000kl\u0001"+
		"\u0000\u0000\u0000ln\u0001\u0000\u0000\u0000mk\u0001\u0000\u0000\u0000"+
		"no\u0005\u0000\u0000\u0001o\u0001\u0001\u0000\u0000\u0000pw\u0003\u0004"+
		"\u0002\u0000qw\u0003\n\u0005\u0000rw\u0003\u0010\b\u0000sw\u0003\u0012"+
		"\t\u0000tw\u0003\u001a\r\u0000uw\u0003\u001e\u000f\u0000vp\u0001\u0000"+
		"\u0000\u0000vq\u0001\u0000\u0000\u0000vr\u0001\u0000\u0000\u0000vs\u0001"+
		"\u0000\u0000\u0000vt\u0001\u0000\u0000\u0000vu\u0001\u0000\u0000\u0000"+
		"w\u0003\u0001\u0000\u0000\u0000xy\u0005\t\u0000\u0000yz\u0003\u0006\u0003"+
		"\u0000z{\u00051\u0000\u0000{\u0005\u0001\u0000\u0000\u0000|\u0081\u0003"+
		"\b\u0004\u0000}~\u00052\u0000\u0000~\u0080\u0003\b\u0004\u0000\u007f}"+
		"\u0001\u0000\u0000\u0000\u0080\u0083\u0001\u0000\u0000\u0000\u0081\u007f"+
		"\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000\u0000\u0000\u0082\u0007"+
		"\u0001\u0000\u0000\u0000\u0083\u0081\u0001\u0000\u0000\u0000\u0084\u0086"+
		"\u00053\u0000\u0000\u0085\u0087\u0003`0\u0000\u0086\u0085\u0001\u0000"+
		"\u0000\u0000\u0086\u0087\u0001\u0000\u0000\u0000\u0087\u008a\u0001\u0000"+
		"\u0000\u0000\u0088\u0089\u0005#\u0000\u0000\u0089\u008b\u0003D\"\u0000"+
		"\u008a\u0088\u0001\u0000\u0000\u0000\u008a\u008b\u0001\u0000\u0000\u0000"+
		"\u008b\u009c\u0001\u0000\u0000\u0000\u008c\u0091\u00053\u0000\u0000\u008d"+
		"\u008e\u00052\u0000\u0000\u008e\u0090\u00053\u0000\u0000\u008f\u008d\u0001"+
		"\u0000\u0000\u0000\u0090\u0093\u0001\u0000\u0000\u0000\u0091\u008f\u0001"+
		"\u0000\u0000\u0000\u0091\u0092\u0001\u0000\u0000\u0000\u0092\u0095\u0001"+
		"\u0000\u0000\u0000\u0093\u0091\u0001\u0000\u0000\u0000\u0094\u0096\u0003"+
		"`0\u0000\u0095\u0094\u0001\u0000\u0000\u0000\u0095\u0096\u0001\u0000\u0000"+
		"\u0000\u0096\u0099\u0001\u0000\u0000\u0000\u0097\u0098\u0005#\u0000\u0000"+
		"\u0098\u009a\u0003B!\u0000\u0099\u0097\u0001\u0000\u0000\u0000\u0099\u009a"+
		"\u0001\u0000\u0000\u0000\u009a\u009c\u0001\u0000\u0000\u0000\u009b\u0084"+
		"\u0001\u0000\u0000\u0000\u009b\u008c\u0001\u0000\u0000\u0000\u009c\t\u0001"+
		"\u0000\u0000\u0000\u009d\u009e\u0005\n\u0000\u0000\u009e\u009f\u0003\f"+
		"\u0006\u0000\u009f\u00a0\u00051\u0000\u0000\u00a0\u000b\u0001\u0000\u0000"+
		"\u0000\u00a1\u00a6\u0003\u000e\u0007\u0000\u00a2\u00a3\u00052\u0000\u0000"+
		"\u00a3\u00a5\u0003\u000e\u0007\u0000\u00a4\u00a2\u0001\u0000\u0000\u0000"+
		"\u00a5\u00a8\u0001\u0000\u0000\u0000\u00a6\u00a4\u0001\u0000\u0000\u0000"+
		"\u00a6\u00a7\u0001\u0000\u0000\u0000\u00a7\r\u0001\u0000\u0000\u0000\u00a8"+
		"\u00a6\u0001\u0000\u0000\u0000\u00a9\u00aa\u00053\u0000\u0000\u00aa\u00ab"+
		"\u0005#\u0000\u0000\u00ab\u00ac\u0003D\"\u0000\u00ac\u000f\u0001\u0000"+
		"\u0000\u0000\u00ad\u00ae\u0005\u0007\u0000\u0000\u00ae\u00af\u00053\u0000"+
		"\u0000\u00af\u00b1\u0005+\u0000\u0000\u00b0\u00b2\u0003\u0016\u000b\u0000"+
		"\u00b1\u00b0\u0001\u0000\u0000\u0000\u00b1\u00b2\u0001\u0000\u0000\u0000"+
		"\u00b2\u00b3\u0001\u0000\u0000\u0000\u00b3\u00b6\u0005,\u0000\u0000\u00b4"+
		"\u00b7\u0003`0\u0000\u00b5\u00b7\u0003^/\u0000\u00b6\u00b4\u0001\u0000"+
		"\u0000\u0000\u00b6\u00b5\u0001\u0000\u0000\u0000\u00b6\u00b7\u0001\u0000"+
		"\u0000\u0000\u00b7\u00b8\u0001\u0000\u0000\u0000\u00b8\u00b9\u0003@ \u0000"+
		"\u00b9\u0011\u0001\u0000\u0000\u0000\u00ba\u00bb\u0005\u0007\u0000\u0000"+
		"\u00bb\u00bc\u0005+\u0000\u0000\u00bc\u00bd\u0003\u0014\n\u0000\u00bd"+
		"\u00be\u0005,\u0000\u0000\u00be\u00bf\u00053\u0000\u0000\u00bf\u00c1\u0005"+
		"+\u0000\u0000\u00c0\u00c2\u0003\u0016\u000b\u0000\u00c1\u00c0\u0001\u0000"+
		"\u0000\u0000\u00c1\u00c2\u0001\u0000\u0000\u0000\u00c2\u00c3\u0001\u0000"+
		"\u0000\u0000\u00c3\u00c6\u0005,\u0000\u0000\u00c4\u00c7\u0003`0\u0000"+
		"\u00c5\u00c7\u0003^/\u0000\u00c6\u00c4\u0001\u0000\u0000\u0000\u00c6\u00c5"+
		"\u0001\u0000\u0000\u0000\u00c6\u00c7\u0001\u0000\u0000\u0000\u00c7\u00c8"+
		"\u0001\u0000\u0000\u0000\u00c8\u00c9\u0003@ \u0000\u00c9\u0013\u0001\u0000"+
		"\u0000\u0000\u00ca\u00cb\u00053\u0000\u0000\u00cb\u00cc\u0003`0\u0000"+
		"\u00cc\u0015\u0001\u0000\u0000\u0000\u00cd\u00d2\u0003\u0018\f\u0000\u00ce"+
		"\u00cf\u00052\u0000\u0000\u00cf\u00d1\u0003\u0018\f\u0000\u00d0\u00ce"+
		"\u0001\u0000\u0000\u0000\u00d1\u00d4\u0001\u0000\u0000\u0000\u00d2\u00d0"+
		"\u0001\u0000\u0000\u0000\u00d2\u00d3\u0001\u0000\u0000\u0000\u00d3\u0017"+
		"\u0001\u0000\u0000\u0000\u00d4\u00d2\u0001\u0000\u0000\u0000\u00d5\u00da"+
		"\u00053\u0000\u0000\u00d6\u00d7\u00052\u0000\u0000\u00d7\u00d9\u00053"+
		"\u0000\u0000\u00d8\u00d6\u0001\u0000\u0000\u0000\u00d9\u00dc\u0001\u0000"+
		"\u0000\u0000\u00da\u00d8\u0001\u0000\u0000\u0000\u00da\u00db\u0001\u0000"+
		"\u0000\u0000\u00db\u00dd\u0001\u0000\u0000\u0000\u00dc\u00da\u0001\u0000"+
		"\u0000\u0000\u00dd\u00de\u0003`0\u0000\u00de\u0019\u0001\u0000\u0000\u0000"+
		"\u00df\u00e0\u0005\b\u0000\u0000\u00e0\u00e1\u00053\u0000\u0000\u00e1"+
		"\u00e2\u0005\u000b\u0000\u0000\u00e2\u00e3\u0005/\u0000\u0000\u00e3\u00e4"+
		"\u0003\u001c\u000e\u0000\u00e4\u00e6\u00050\u0000\u0000\u00e5\u00e7\u0005"+
		"1\u0000\u0000\u00e6\u00e5\u0001\u0000\u0000\u0000\u00e6\u00e7\u0001\u0000"+
		"\u0000\u0000\u00e7\u001b\u0001\u0000\u0000\u0000\u00e8\u00e9\u00053\u0000"+
		"\u0000\u00e9\u00ea\u0003`0\u0000\u00ea\u00eb\u00051\u0000\u0000\u00eb"+
		"\u00ed\u0001\u0000\u0000\u0000\u00ec\u00e8\u0001\u0000\u0000\u0000\u00ed"+
		"\u00f0\u0001\u0000\u0000\u0000\u00ee\u00ec\u0001\u0000\u0000\u0000\u00ee"+
		"\u00ef\u0001\u0000\u0000\u0000\u00ef\u001d\u0001\u0000\u0000\u0000\u00f0"+
		"\u00ee\u0001\u0000\u0000\u0000\u00f1\u00f2\u0005\b\u0000\u0000\u00f2\u00f3"+
		"\u00053\u0000\u0000\u00f3\u00f4\u0005\f\u0000\u0000\u00f4\u00f5\u0005"+
		"/\u0000\u0000\u00f5\u00f6\u0003 \u0010\u0000\u00f6\u00f8\u00050\u0000"+
		"\u0000\u00f7\u00f9\u00051\u0000\u0000\u00f8\u00f7\u0001\u0000\u0000\u0000"+
		"\u00f8\u00f9\u0001\u0000\u0000\u0000\u00f9\u001f\u0001\u0000\u0000\u0000"+
		"\u00fa\u00fb\u00053\u0000\u0000\u00fb\u00fd\u0005+\u0000\u0000\u00fc\u00fe"+
		"\u0003\u0016\u000b\u0000\u00fd\u00fc\u0001\u0000\u0000\u0000\u00fd\u00fe"+
		"\u0001\u0000\u0000\u0000\u00fe\u00ff\u0001\u0000\u0000\u0000\u00ff\u0102"+
		"\u0005,\u0000\u0000\u0100\u0103\u0003`0\u0000\u0101\u0103\u0003^/\u0000"+
		"\u0102\u0100\u0001\u0000\u0000\u0000\u0102\u0101\u0001\u0000\u0000\u0000"+
		"\u0102\u0103\u0001\u0000\u0000\u0000\u0103\u0104\u0001\u0000\u0000\u0000"+
		"\u0104\u0106\u00051\u0000\u0000\u0105\u00fa\u0001\u0000\u0000\u0000\u0106"+
		"\u0109\u0001\u0000\u0000\u0000\u0107\u0105\u0001\u0000\u0000\u0000\u0107"+
		"\u0108\u0001\u0000\u0000\u0000\u0108!\u0001\u0000\u0000\u0000\u0109\u0107"+
		"\u0001\u0000\u0000\u0000\u010a\u0114\u0003$\u0012\u0000\u010b\u0114\u0003"+
		"&\u0013\u0000\u010c\u0114\u0003*\u0015\u0000\u010d\u0114\u0003,\u0016"+
		"\u0000\u010e\u0114\u00038\u001c\u0000\u010f\u0114\u0003:\u001d\u0000\u0110"+
		"\u0114\u0003<\u001e\u0000\u0111\u0114\u0003>\u001f\u0000\u0112\u0114\u0003"+
		"@ \u0000\u0113\u010a\u0001\u0000\u0000\u0000\u0113\u010b\u0001\u0000\u0000"+
		"\u0000\u0113\u010c\u0001\u0000\u0000\u0000\u0113\u010d\u0001\u0000\u0000"+
		"\u0000\u0113\u010e\u0001\u0000\u0000\u0000\u0113\u010f\u0001\u0000\u0000"+
		"\u0000\u0113\u0110\u0001\u0000\u0000\u0000\u0113\u0111\u0001\u0000\u0000"+
		"\u0000\u0113\u0112\u0001\u0000\u0000\u0000\u0114#\u0001\u0000\u0000\u0000"+
		"\u0115\u0118\u0003\u0004\u0002\u0000\u0116\u0118\u0003\n\u0005\u0000\u0117"+
		"\u0115\u0001\u0000\u0000\u0000\u0117\u0116\u0001\u0000\u0000\u0000\u0118"+
		"%\u0001\u0000\u0000\u0000\u0119\u011a\u0003(\u0014\u0000\u011a\u011b\u0007"+
		"\u0000\u0000\u0000\u011b\u011c\u0003D\"\u0000\u011c\u011d\u00051\u0000"+
		"\u0000\u011d\'\u0001\u0000\u0000\u0000\u011e\u0124\u00053\u0000\u0000"+
		"\u011f\u0120\u00053\u0000\u0000\u0120\u0124\u0003T*\u0000\u0121\u0122"+
		"\u00053\u0000\u0000\u0122\u0124\u0003V+\u0000\u0123\u011e\u0001\u0000"+
		"\u0000\u0000\u0123\u011f\u0001\u0000\u0000\u0000\u0123\u0121\u0001\u0000"+
		"\u0000\u0000\u0124)\u0001\u0000\u0000\u0000\u0125\u0126\u0005\u0001\u0000"+
		"\u0000\u0126\u0127\u0005+\u0000\u0000\u0127\u0128\u0003D\"\u0000\u0128"+
		"\u0129\u0005,\u0000\u0000\u0129\u012f\u0003@ \u0000\u012a\u012d\u0005"+
		"\u0002\u0000\u0000\u012b\u012e\u0003*\u0015\u0000\u012c\u012e\u0003@ "+
		"\u0000\u012d\u012b\u0001\u0000\u0000\u0000\u012d\u012c\u0001\u0000\u0000"+
		"\u0000\u012e\u0130\u0001\u0000\u0000\u0000\u012f\u012a\u0001\u0000\u0000"+
		"\u0000\u012f\u0130\u0001\u0000\u0000\u0000\u0130+\u0001\u0000\u0000\u0000"+
		"\u0131\u0135\u0005\u0003\u0000\u0000\u0132\u0136\u0003D\"\u0000\u0133"+
		"\u0136\u0003.\u0017\u0000\u0134\u0136\u00034\u001a\u0000\u0135\u0132\u0001"+
		"\u0000\u0000\u0000\u0135\u0133\u0001\u0000\u0000\u0000\u0135\u0134\u0001"+
		"\u0000\u0000\u0000\u0136\u0137\u0001\u0000\u0000\u0000\u0137\u0138\u0003"+
		"@ \u0000\u0138-\u0001\u0000\u0000\u0000\u0139\u013b\u00030\u0018\u0000"+
		"\u013a\u0139\u0001\u0000\u0000\u0000\u013a\u013b\u0001\u0000\u0000\u0000"+
		"\u013b\u013c\u0001\u0000\u0000\u0000\u013c\u013e\u00051\u0000\u0000\u013d"+
		"\u013f\u0003D\"\u0000\u013e\u013d\u0001\u0000\u0000\u0000\u013e\u013f"+
		"\u0001\u0000\u0000\u0000\u013f\u0140\u0001\u0000\u0000\u0000\u0140\u0142"+
		"\u00051\u0000\u0000\u0141\u0143\u00032\u0019\u0000\u0142\u0141\u0001\u0000"+
		"\u0000\u0000\u0142\u0143\u0001\u0000\u0000\u0000\u0143/\u0001\u0000\u0000"+
		"\u0000\u0144\u0145\u00053\u0000\u0000\u0145\u0146\u0005#\u0000\u0000\u0146"+
		"\u014f\u0003D\"\u0000\u0147\u0148\u0005\t\u0000\u0000\u0148\u014a\u0005"+
		"3\u0000\u0000\u0149\u014b\u0003`0\u0000\u014a\u0149\u0001\u0000\u0000"+
		"\u0000\u014a\u014b\u0001\u0000\u0000\u0000\u014b\u014c\u0001\u0000\u0000"+
		"\u0000\u014c\u014d\u0005#\u0000\u0000\u014d\u014f\u0003D\"\u0000\u014e"+
		"\u0144\u0001\u0000\u0000\u0000\u014e\u0147\u0001\u0000\u0000\u0000\u014f"+
		"1\u0001\u0000\u0000\u0000\u0150\u0151\u00053\u0000\u0000\u0151\u0152\u0003"+
		"6\u001b\u0000\u0152\u0153\u0003D\"\u0000\u01533\u0001\u0000\u0000\u0000"+
		"\u0154\u0155\u00053\u0000\u0000\u0155\u0156\u00052\u0000\u0000\u0156\u0157"+
		"\u00053\u0000\u0000\u0157\u0158\u0005\u0011\u0000\u0000\u0158\u0159\u0003"+
		"D\"\u0000\u01595\u0001\u0000\u0000\u0000\u015a\u015b\u0007\u0000\u0000"+
		"\u0000\u015b7\u0001\u0000\u0000\u0000\u015c\u015d\u0005\u0005\u0000\u0000"+
		"\u015d\u015e\u00051\u0000\u0000\u015e9\u0001\u0000\u0000\u0000\u015f\u0160"+
		"\u0005\u0006\u0000\u0000\u0160\u0161\u00051\u0000\u0000\u0161;\u0001\u0000"+
		"\u0000\u0000\u0162\u0164\u0005\u0004\u0000\u0000\u0163\u0165\u0003D\""+
		"\u0000\u0164\u0163\u0001\u0000\u0000\u0000\u0164\u0165\u0001\u0000\u0000"+
		"\u0000\u0165\u0166\u0001\u0000\u0000\u0000\u0166\u0167\u00051\u0000\u0000"+
		"\u0167=\u0001\u0000\u0000\u0000\u0168\u016d\u00053\u0000\u0000\u0169\u016a"+
		"\u00053\u0000\u0000\u016a\u016b\u0005)\u0000\u0000\u016b\u016d\u00053"+
		"\u0000\u0000\u016c\u0168\u0001\u0000\u0000\u0000\u016c\u0169\u0001\u0000"+
		"\u0000\u0000\u016d\u016e\u0001\u0000\u0000\u0000\u016e\u0170\u0005+\u0000"+
		"\u0000\u016f\u0171\u0003B!\u0000\u0170\u016f\u0001\u0000\u0000\u0000\u0170"+
		"\u0171\u0001\u0000\u0000\u0000\u0171\u0172\u0001\u0000\u0000\u0000\u0172"+
		"\u0173\u0005,\u0000\u0000\u0173\u0174\u00051\u0000\u0000\u0174?\u0001"+
		"\u0000\u0000\u0000\u0175\u0179\u0005/\u0000\u0000\u0176\u0178\u0003\""+
		"\u0011\u0000\u0177\u0176\u0001\u0000\u0000\u0000\u0178\u017b\u0001\u0000"+
		"\u0000\u0000\u0179\u0177\u0001\u0000\u0000\u0000\u0179\u017a\u0001\u0000"+
		"\u0000\u0000\u017a\u017c\u0001\u0000\u0000\u0000\u017b\u0179\u0001\u0000"+
		"\u0000\u0000\u017c\u017d\u00050\u0000\u0000\u017dA\u0001\u0000\u0000\u0000"+
		"\u017e\u0183\u0003D\"\u0000\u017f\u0180\u00052\u0000\u0000\u0180\u0182"+
		"\u0003D\"\u0000\u0181\u017f\u0001\u0000\u0000\u0000\u0182\u0185\u0001"+
		"\u0000\u0000\u0000\u0183\u0181\u0001\u0000\u0000\u0000\u0183\u0184\u0001"+
		"\u0000\u0000\u0000\u0184C\u0001\u0000\u0000\u0000\u0185\u0183\u0001\u0000"+
		"\u0000\u0000\u0186\u0187\u0006\"\uffff\uffff\u0000\u0187\u0188\u0003F"+
		"#\u0000\u0188\u018e\u0001\u0000\u0000\u0000\u0189\u018a\n\u0002\u0000"+
		"\u0000\u018a\u018b\u0005!\u0000\u0000\u018b\u018d\u0003F#\u0000\u018c"+
		"\u0189\u0001\u0000\u0000\u0000\u018d\u0190\u0001\u0000\u0000\u0000\u018e"+
		"\u018c\u0001\u0000\u0000\u0000\u018e\u018f\u0001\u0000\u0000\u0000\u018f"+
		"E\u0001\u0000\u0000\u0000\u0190\u018e\u0001\u0000\u0000\u0000\u0191\u0192"+
		"\u0006#\uffff\uffff\u0000\u0192\u0193\u0003H$\u0000\u0193\u0199\u0001"+
		"\u0000\u0000\u0000\u0194\u0195\n\u0002\u0000\u0000\u0195\u0196\u0005 "+
		"\u0000\u0000\u0196\u0198\u0003H$\u0000\u0197\u0194\u0001\u0000\u0000\u0000"+
		"\u0198\u019b\u0001\u0000\u0000\u0000\u0199\u0197\u0001\u0000\u0000\u0000"+
		"\u0199\u019a\u0001\u0000\u0000\u0000\u019aG\u0001\u0000\u0000\u0000\u019b"+
		"\u0199\u0001\u0000\u0000\u0000\u019c\u019d\u0006$\uffff\uffff\u0000\u019d"+
		"\u019e\u0003J%\u0000\u019e\u01a4\u0001\u0000\u0000\u0000\u019f\u01a0\n"+
		"\u0002\u0000\u0000\u01a0\u01a1\u0007\u0001\u0000\u0000\u01a1\u01a3\u0003"+
		"J%\u0000\u01a2\u019f\u0001\u0000\u0000\u0000\u01a3\u01a6\u0001\u0000\u0000"+
		"\u0000\u01a4\u01a2\u0001\u0000\u0000\u0000\u01a4\u01a5\u0001\u0000\u0000"+
		"\u0000\u01a5I\u0001\u0000\u0000\u0000\u01a6\u01a4\u0001\u0000\u0000\u0000"+
		"\u01a7\u01a8\u0006%\uffff\uffff\u0000\u01a8\u01a9\u0003L&\u0000\u01a9"+
		"\u01af\u0001\u0000\u0000\u0000\u01aa\u01ab\n\u0002\u0000\u0000\u01ab\u01ac"+
		"\u0007\u0002\u0000\u0000\u01ac\u01ae\u0003L&\u0000\u01ad\u01aa\u0001\u0000"+
		"\u0000\u0000\u01ae\u01b1\u0001\u0000\u0000\u0000\u01af\u01ad\u0001\u0000"+
		"\u0000\u0000\u01af\u01b0\u0001\u0000\u0000\u0000\u01b0K\u0001\u0000\u0000"+
		"\u0000\u01b1\u01af\u0001\u0000\u0000\u0000\u01b2\u01b3\u0006&\uffff\uffff"+
		"\u0000\u01b3\u01b4\u0003N\'\u0000\u01b4\u01ba\u0001\u0000\u0000\u0000"+
		"\u01b5\u01b6\n\u0002\u0000\u0000\u01b6\u01b7\u0007\u0003\u0000\u0000\u01b7"+
		"\u01b9\u0003N\'\u0000\u01b8\u01b5\u0001\u0000\u0000\u0000\u01b9\u01bc"+
		"\u0001\u0000\u0000\u0000\u01ba\u01b8\u0001\u0000\u0000\u0000\u01ba\u01bb"+
		"\u0001\u0000\u0000\u0000\u01bbM\u0001\u0000\u0000\u0000\u01bc\u01ba\u0001"+
		"\u0000\u0000\u0000\u01bd\u01be\u0005\"\u0000\u0000\u01be\u01c3\u0003N"+
		"\'\u0000\u01bf\u01c0\u0005\u0016\u0000\u0000\u01c0\u01c3\u0003N\'\u0000"+
		"\u01c1\u01c3\u0003P(\u0000\u01c2\u01bd\u0001\u0000\u0000\u0000\u01c2\u01bf"+
		"\u0001\u0000\u0000\u0000\u01c2\u01c1\u0001\u0000\u0000\u0000\u01c3O\u0001"+
		"\u0000\u0000\u0000\u01c4\u01ca\u0003R)\u0000\u01c5\u01c9\u0003T*\u0000"+
		"\u01c6\u01c9\u0003V+\u0000\u01c7\u01c9\u0003X,\u0000\u01c8\u01c5\u0001"+
		"\u0000\u0000\u0000\u01c8\u01c6\u0001\u0000\u0000\u0000\u01c8\u01c7\u0001"+
		"\u0000\u0000\u0000\u01c9\u01cc\u0001\u0000\u0000\u0000\u01ca\u01c8\u0001"+
		"\u0000\u0000\u0000\u01ca\u01cb\u0001\u0000\u0000\u0000\u01cbQ\u0001\u0000"+
		"\u0000\u0000\u01cc\u01ca\u0001\u0000\u0000\u0000\u01cd\u01d4\u0003Z-\u0000"+
		"\u01ce\u01d4\u00053\u0000\u0000\u01cf\u01d0\u0005+\u0000\u0000\u01d0\u01d1"+
		"\u0003D\"\u0000\u01d1\u01d2\u0005,\u0000\u0000\u01d2\u01d4\u0001\u0000"+
		"\u0000\u0000\u01d3\u01cd\u0001\u0000\u0000\u0000\u01d3\u01ce\u0001\u0000"+
		"\u0000\u0000\u01d3\u01cf\u0001\u0000\u0000\u0000\u01d4S\u0001\u0000\u0000"+
		"\u0000\u01d5\u01d6\u0005-\u0000\u0000\u01d6\u01d7\u0003D\"\u0000\u01d7"+
		"\u01d8\u0005.\u0000\u0000\u01d8U\u0001\u0000\u0000\u0000\u01d9\u01da\u0005"+
		")\u0000\u0000\u01da\u01db\u00053\u0000\u0000\u01dbW\u0001\u0000\u0000"+
		"\u0000\u01dc\u01de\u0005+\u0000\u0000\u01dd\u01df\u0003B!\u0000\u01de"+
		"\u01dd\u0001\u0000\u0000\u0000\u01de\u01df\u0001\u0000\u0000\u0000\u01df"+
		"\u01e0\u0001\u0000\u0000\u0000\u01e0\u01e1\u0005,\u0000\u0000\u01e1Y\u0001"+
		"\u0000\u0000\u0000\u01e2\u01eb\u00054\u0000\u0000\u01e3\u01eb\u00055\u0000"+
		"\u0000\u01e4\u01eb\u00056\u0000\u0000\u01e5\u01eb\u0003\\.\u0000\u01e6"+
		"\u01eb\u0003b1\u0000\u01e7\u01eb\u0005\u0013\u0000\u0000\u01e8\u01eb\u0005"+
		"\u0014\u0000\u0000\u01e9\u01eb\u0005\u0012\u0000\u0000\u01ea\u01e2\u0001"+
		"\u0000\u0000\u0000\u01ea\u01e3\u0001\u0000\u0000\u0000\u01ea\u01e4\u0001"+
		"\u0000\u0000\u0000\u01ea\u01e5\u0001\u0000\u0000\u0000\u01ea\u01e6\u0001"+
		"\u0000\u0000\u0000\u01ea\u01e7\u0001\u0000\u0000\u0000\u01ea\u01e8\u0001"+
		"\u0000\u0000\u0000\u01ea\u01e9\u0001\u0000\u0000\u0000\u01eb[\u0001\u0000"+
		"\u0000\u0000\u01ec\u01ed\u0003^/\u0000\u01ed\u01ef\u0005/\u0000\u0000"+
		"\u01ee\u01f0\u0003B!\u0000\u01ef\u01ee\u0001\u0000\u0000\u0000\u01ef\u01f0"+
		"\u0001\u0000\u0000\u0000\u01f0\u01f1\u0001\u0000\u0000\u0000\u01f1\u01f2"+
		"\u00050\u0000\u0000\u01f2]\u0001\u0000\u0000\u0000\u01f3\u01f4\u0005-"+
		"\u0000\u0000\u01f4\u01f5\u00054\u0000\u0000\u01f5\u01fb\u0005.\u0000\u0000"+
		"\u01f6\u01f7\u0005-\u0000\u0000\u01f7\u01f8\u00054\u0000\u0000\u01f8\u01fa"+
		"\u0005.\u0000\u0000\u01f9\u01f6\u0001\u0000\u0000\u0000\u01fa\u01fd\u0001"+
		"\u0000\u0000\u0000\u01fb\u01f9\u0001\u0000\u0000\u0000\u01fb\u01fc\u0001"+
		"\u0000\u0000\u0000\u01fc\u01fe\u0001\u0000\u0000\u0000\u01fd\u01fb\u0001"+
		"\u0000\u0000\u0000\u01fe\u01ff\u0003`0\u0000\u01ff_\u0001\u0000\u0000"+
		"\u0000\u0200\u0201\u0007\u0004\u0000\u0000\u0201a\u0001\u0000\u0000\u0000"+
		"\u0202\u0203\u00053\u0000\u0000\u0203\u0205\u0005/\u0000\u0000\u0204\u0206"+
		"\u0003d2\u0000\u0205\u0204\u0001\u0000\u0000\u0000\u0205\u0206\u0001\u0000"+
		"\u0000\u0000\u0206\u0207\u0001\u0000\u0000\u0000\u0207\u0208\u00050\u0000"+
		"\u0000\u0208c\u0001\u0000\u0000\u0000\u0209\u020e\u0003f3\u0000\u020a"+
		"\u020b\u00052\u0000\u0000\u020b\u020d\u0003f3\u0000\u020c\u020a\u0001"+
		"\u0000\u0000\u0000\u020d\u0210\u0001\u0000\u0000\u0000\u020e\u020c\u0001"+
		"\u0000\u0000\u0000\u020e\u020f\u0001\u0000\u0000\u0000\u020fe\u0001\u0000"+
		"\u0000\u0000\u0210\u020e\u0001\u0000\u0000\u0000\u0211\u0212\u00053\u0000"+
		"\u0000\u0212\u0213\u0005*\u0000\u0000\u0213\u0214\u0003D\"\u0000\u0214"+
		"g\u0001\u0000\u0000\u00005kv\u0081\u0086\u008a\u0091\u0095\u0099\u009b"+
		"\u00a6\u00b1\u00b6\u00c1\u00c6\u00d2\u00da\u00e6\u00ee\u00f8\u00fd\u0102"+
		"\u0107\u0113\u0117\u0123\u012d\u012f\u0135\u013a\u013e\u0142\u014a\u014e"+
		"\u0164\u016c\u0170\u0179\u0183\u018e\u0199\u01a4\u01af\u01ba\u01c2\u01c8"+
		"\u01ca\u01d3\u01de\u01ea\u01ef\u01fb\u0205\u020e";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
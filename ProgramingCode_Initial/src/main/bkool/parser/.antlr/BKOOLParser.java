// Generated from d:/PPL_Initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class BKOOLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ARRAY=1, VARNAME=2, PAIRNAME=3, INTLIT=4, FLOATLIT=5, STRINGLIT=6, DSTAR=7, 
		DOT=8, MUL=9, DIV=10, MOD=11, ADD=12, SUB=13, DQUES=14, EQ=15, ARROW=16, 
		LP=17, RP=18, COMMA=19, SEMI=20, WS=21;
	public static final int
		RULE_program = 0, RULE_vardecl = 1, RULE_expr = 2, RULE_atom_expr = 3, 
		RULE_array_expr = 4, RULE_pair = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "vardecl", "expr", "atom_expr", "array_expr", "pair"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'array'", null, null, null, null, null, "'**'", "'.'", "'*'", 
			"'/'", "'%'", "'+'", "'-'", "'??'", "'='", "'=>'", "'('", "')'", "','", 
			"';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ARRAY", "VARNAME", "PAIRNAME", "INTLIT", "FLOATLIT", "STRINGLIT", 
			"DSTAR", "DOT", "MUL", "DIV", "MOD", "ADD", "SUB", "DQUES", "EQ", "ARROW", 
			"LP", "RP", "COMMA", "SEMI", "WS"
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
	public String getGrammarFileName() { return "BKOOL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BKOOLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(BKOOLParser.EOF, 0); }
		public List<VardeclContext> vardecl() {
			return getRuleContexts(VardeclContext.class);
		}
		public VardeclContext vardecl(int i) {
			return getRuleContext(VardeclContext.class,i);
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
			setState(13); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(12);
				vardecl();
				}
				}
				setState(15); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==VARNAME );
			setState(17);
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
	public static class VardeclContext extends ParserRuleContext {
		public TerminalNode VARNAME() { return getToken(BKOOLParser.VARNAME, 0); }
		public TerminalNode EQ() { return getToken(BKOOLParser.EQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public VardeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardecl; }
	}

	public final VardeclContext vardecl() throws RecognitionException {
		VardeclContext _localctx = new VardeclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_vardecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			match(VARNAME);
			setState(20);
			match(EQ);
			setState(21);
			expr(0);
			setState(22);
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
	public static class ExprContext extends ParserRuleContext {
		public Atom_exprContext atom_expr() {
			return getRuleContext(Atom_exprContext.class,0);
		}
		public TerminalNode LP() { return getToken(BKOOLParser.LP, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode RP() { return getToken(BKOOLParser.RP, 0); }
		public TerminalNode DSTAR() { return getToken(BKOOLParser.DSTAR, 0); }
		public TerminalNode DOT() { return getToken(BKOOLParser.DOT, 0); }
		public TerminalNode MUL() { return getToken(BKOOLParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(BKOOLParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(BKOOLParser.MOD, 0); }
		public TerminalNode ADD() { return getToken(BKOOLParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(BKOOLParser.SUB, 0); }
		public TerminalNode DQUES() { return getToken(BKOOLParser.DQUES, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ARRAY:
			case VARNAME:
			case INTLIT:
			case FLOATLIT:
			case STRINGLIT:
				{
				setState(25);
				atom_expr();
				}
				break;
			case LP:
				{
				setState(26);
				match(LP);
				setState(27);
				expr(0);
				setState(28);
				match(RP);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(49);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(47);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(32);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(33);
						match(DSTAR);
						setState(34);
						expr(7);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(35);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(36);
						match(DOT);
						setState(37);
						expr(6);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(38);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(39);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3584L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(40);
						expr(5);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(41);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(42);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(43);
						expr(4);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(44);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(45);
						match(DQUES);
						setState(46);
						expr(3);
						}
						break;
					}
					} 
				}
				setState(51);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
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
	public static class Atom_exprContext extends ParserRuleContext {
		public TerminalNode VARNAME() { return getToken(BKOOLParser.VARNAME, 0); }
		public TerminalNode INTLIT() { return getToken(BKOOLParser.INTLIT, 0); }
		public TerminalNode FLOATLIT() { return getToken(BKOOLParser.FLOATLIT, 0); }
		public TerminalNode STRINGLIT() { return getToken(BKOOLParser.STRINGLIT, 0); }
		public Array_exprContext array_expr() {
			return getRuleContext(Array_exprContext.class,0);
		}
		public Atom_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom_expr; }
	}

	public final Atom_exprContext atom_expr() throws RecognitionException {
		Atom_exprContext _localctx = new Atom_exprContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_atom_expr);
		try {
			setState(57);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VARNAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(52);
				match(VARNAME);
				}
				break;
			case INTLIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(53);
				match(INTLIT);
				}
				break;
			case FLOATLIT:
				enterOuterAlt(_localctx, 3);
				{
				setState(54);
				match(FLOATLIT);
				}
				break;
			case STRINGLIT:
				enterOuterAlt(_localctx, 4);
				{
				setState(55);
				match(STRINGLIT);
				}
				break;
			case ARRAY:
				enterOuterAlt(_localctx, 5);
				{
				setState(56);
				array_expr();
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
	public static class Array_exprContext extends ParserRuleContext {
		public TerminalNode ARRAY() { return getToken(BKOOLParser.ARRAY, 0); }
		public TerminalNode LP() { return getToken(BKOOLParser.LP, 0); }
		public TerminalNode RP() { return getToken(BKOOLParser.RP, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKOOLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKOOLParser.COMMA, i);
		}
		public List<PairContext> pair() {
			return getRuleContexts(PairContext.class);
		}
		public PairContext pair(int i) {
			return getRuleContext(PairContext.class,i);
		}
		public Array_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_expr; }
	}

	public final Array_exprContext array_expr() throws RecognitionException {
		Array_exprContext _localctx = new Array_exprContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_array_expr);
		int _la;
		try {
			setState(85);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(59);
				match(ARRAY);
				setState(60);
				match(LP);
				setState(69);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 131190L) != 0)) {
					{
					setState(61);
					expr(0);
					setState(66);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(62);
						match(COMMA);
						setState(63);
						expr(0);
						}
						}
						setState(68);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(71);
				match(RP);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(72);
				match(ARRAY);
				setState(73);
				match(LP);
				setState(82);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==PAIRNAME) {
					{
					setState(74);
					pair();
					setState(79);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(75);
						match(COMMA);
						setState(76);
						pair();
						}
						}
						setState(81);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(84);
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
	public static class PairContext extends ParserRuleContext {
		public TerminalNode PAIRNAME() { return getToken(BKOOLParser.PAIRNAME, 0); }
		public TerminalNode ARROW() { return getToken(BKOOLParser.ARROW, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public PairContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pair; }
	}

	public final PairContext pair() throws RecognitionException {
		PairContext _localctx = new PairContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_pair);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(PAIRNAME);
			setState(88);
			match(ARROW);
			setState(89);
			expr(0);
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
		case 2:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		case 2:
			return precpred(_ctx, 4);
		case 3:
			return precpred(_ctx, 3);
		case 4:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0015\\\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0001\u0000\u0004\u0000\u000e\b\u0000\u000b\u0000\f"+
		"\u0000\u000f\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0003\u0002\u001f\b\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0005\u00020\b\u0002\n\u0002\f\u00023\t\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003:\b\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004"+
		"A\b\u0004\n\u0004\f\u0004D\t\u0004\u0003\u0004F\b\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004N\b"+
		"\u0004\n\u0004\f\u0004Q\t\u0004\u0003\u0004S\b\u0004\u0001\u0004\u0003"+
		"\u0004V\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0000\u0001\u0004\u0006\u0000\u0002\u0004\u0006\b\n\u0000\u0002"+
		"\u0001\u0000\t\u000b\u0001\u0000\f\re\u0000\r\u0001\u0000\u0000\u0000"+
		"\u0002\u0013\u0001\u0000\u0000\u0000\u0004\u001e\u0001\u0000\u0000\u0000"+
		"\u00069\u0001\u0000\u0000\u0000\bU\u0001\u0000\u0000\u0000\nW\u0001\u0000"+
		"\u0000\u0000\f\u000e\u0003\u0002\u0001\u0000\r\f\u0001\u0000\u0000\u0000"+
		"\u000e\u000f\u0001\u0000\u0000\u0000\u000f\r\u0001\u0000\u0000\u0000\u000f"+
		"\u0010\u0001\u0000\u0000\u0000\u0010\u0011\u0001\u0000\u0000\u0000\u0011"+
		"\u0012\u0005\u0000\u0000\u0001\u0012\u0001\u0001\u0000\u0000\u0000\u0013"+
		"\u0014\u0005\u0002\u0000\u0000\u0014\u0015\u0005\u000f\u0000\u0000\u0015"+
		"\u0016\u0003\u0004\u0002\u0000\u0016\u0017\u0005\u0014\u0000\u0000\u0017"+
		"\u0003\u0001\u0000\u0000\u0000\u0018\u0019\u0006\u0002\uffff\uffff\u0000"+
		"\u0019\u001f\u0003\u0006\u0003\u0000\u001a\u001b\u0005\u0011\u0000\u0000"+
		"\u001b\u001c\u0003\u0004\u0002\u0000\u001c\u001d\u0005\u0012\u0000\u0000"+
		"\u001d\u001f\u0001\u0000\u0000\u0000\u001e\u0018\u0001\u0000\u0000\u0000"+
		"\u001e\u001a\u0001\u0000\u0000\u0000\u001f1\u0001\u0000\u0000\u0000 !"+
		"\n\u0006\u0000\u0000!\"\u0005\u0007\u0000\u0000\"0\u0003\u0004\u0002\u0007"+
		"#$\n\u0005\u0000\u0000$%\u0005\b\u0000\u0000%0\u0003\u0004\u0002\u0006"+
		"&\'\n\u0004\u0000\u0000\'(\u0007\u0000\u0000\u0000(0\u0003\u0004\u0002"+
		"\u0005)*\n\u0003\u0000\u0000*+\u0007\u0001\u0000\u0000+0\u0003\u0004\u0002"+
		"\u0004,-\n\u0002\u0000\u0000-.\u0005\u000e\u0000\u0000.0\u0003\u0004\u0002"+
		"\u0003/ \u0001\u0000\u0000\u0000/#\u0001\u0000\u0000\u0000/&\u0001\u0000"+
		"\u0000\u0000/)\u0001\u0000\u0000\u0000/,\u0001\u0000\u0000\u000003\u0001"+
		"\u0000\u0000\u00001/\u0001\u0000\u0000\u000012\u0001\u0000\u0000\u0000"+
		"2\u0005\u0001\u0000\u0000\u000031\u0001\u0000\u0000\u00004:\u0005\u0002"+
		"\u0000\u00005:\u0005\u0004\u0000\u00006:\u0005\u0005\u0000\u00007:\u0005"+
		"\u0006\u0000\u00008:\u0003\b\u0004\u000094\u0001\u0000\u0000\u000095\u0001"+
		"\u0000\u0000\u000096\u0001\u0000\u0000\u000097\u0001\u0000\u0000\u0000"+
		"98\u0001\u0000\u0000\u0000:\u0007\u0001\u0000\u0000\u0000;<\u0005\u0001"+
		"\u0000\u0000<E\u0005\u0011\u0000\u0000=B\u0003\u0004\u0002\u0000>?\u0005"+
		"\u0013\u0000\u0000?A\u0003\u0004\u0002\u0000@>\u0001\u0000\u0000\u0000"+
		"AD\u0001\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000"+
		"\u0000CF\u0001\u0000\u0000\u0000DB\u0001\u0000\u0000\u0000E=\u0001\u0000"+
		"\u0000\u0000EF\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000GV\u0005"+
		"\u0012\u0000\u0000HI\u0005\u0001\u0000\u0000IR\u0005\u0011\u0000\u0000"+
		"JO\u0003\n\u0005\u0000KL\u0005\u0013\u0000\u0000LN\u0003\n\u0005\u0000"+
		"MK\u0001\u0000\u0000\u0000NQ\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000"+
		"\u0000OP\u0001\u0000\u0000\u0000PS\u0001\u0000\u0000\u0000QO\u0001\u0000"+
		"\u0000\u0000RJ\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000ST\u0001"+
		"\u0000\u0000\u0000TV\u0005\u0012\u0000\u0000U;\u0001\u0000\u0000\u0000"+
		"UH\u0001\u0000\u0000\u0000V\t\u0001\u0000\u0000\u0000WX\u0005\u0003\u0000"+
		"\u0000XY\u0005\u0010\u0000\u0000YZ\u0003\u0004\u0002\u0000Z\u000b\u0001"+
		"\u0000\u0000\u0000\n\u000f\u001e/19BEORU";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
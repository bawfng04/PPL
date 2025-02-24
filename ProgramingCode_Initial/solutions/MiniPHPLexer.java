// Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MiniPHPLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ARRAY=1, VARNAME=2, PAIRNAME=3, INTLIT=4, FLOATLIT=5, STRINGLIT=6, DSTAR=7,
		DOT=8, MUL=9, DIV=10, MOD=11, ADD=12, SUB=13, DQUES=14, EQ=15, ARROW=16,
		LP=17, RP=18, COMMA=19, SEMI=20, WS=21;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"ARRAY", "VARNAME", "PAIRNAME", "INTLIT", "FLOATLIT", "STRINGLIT", "DSTAR",
			"DOT", "MUL", "DIV", "MOD", "ADD", "SUB", "DQUES", "EQ", "ARROW", "LP",
			"RP", "COMMA", "SEMI", "WS"
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


	public MiniPHPLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "BKOOL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27\u0080\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\3\3\3\7\3\66\n\3\f\3\16\39\13\3\3\4\3\4\7\4=\n\4\f\4\16\4@\13\4\3\5"+
		"\6\5C\n\5\r\5\16\5D\3\6\6\6H\n\6\r\6\16\6I\3\6\3\6\6\6N\n\6\r\6\16\6O"+
		"\3\7\3\7\7\7T\n\7\f\7\16\7W\13\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3"+
		"\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21"+
		"\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\6\26{\n\26\r\26\16"+
		"\26|\3\26\3\26\3U\2\27\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27"+
		"\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27\3\2\6\5\2C\\aac|\6"+
		"\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2\u0086\2\3\3\2\2\2\2\5\3\2\2"+
		"\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21"+
		"\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2"+
		"\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3"+
		"\2\2\2\2)\3\2\2\2\2+\3\2\2\2\3-\3\2\2\2\5\63\3\2\2\2\7:\3\2\2\2\tB\3\2"+
		"\2\2\13G\3\2\2\2\rQ\3\2\2\2\17Z\3\2\2\2\21]\3\2\2\2\23_\3\2\2\2\25a\3"+
		"\2\2\2\27c\3\2\2\2\31e\3\2\2\2\33g\3\2\2\2\35i\3\2\2\2\37l\3\2\2\2!n\3"+
		"\2\2\2#q\3\2\2\2%s\3\2\2\2\'u\3\2\2\2)w\3\2\2\2+z\3\2\2\2-.\7c\2\2./\7"+
		"t\2\2/\60\7t\2\2\60\61\7c\2\2\61\62\7{\2\2\62\4\3\2\2\2\63\67\t\2\2\2"+
		"\64\66\t\3\2\2\65\64\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\6"+
		"\3\2\2\29\67\3\2\2\2:>\t\2\2\2;=\t\3\2\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2"+
		">?\3\2\2\2?\b\3\2\2\2@>\3\2\2\2AC\t\4\2\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2"+
		"\2DE\3\2\2\2E\n\3\2\2\2FH\t\4\2\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2"+
		"\2\2JK\3\2\2\2KM\7\60\2\2LN\t\4\2\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3"+
		"\2\2\2P\f\3\2\2\2QU\7$\2\2RT\13\2\2\2SR\3\2\2\2TW\3\2\2\2UV\3\2\2\2US"+
		"\3\2\2\2VX\3\2\2\2WU\3\2\2\2XY\7$\2\2Y\16\3\2\2\2Z[\7,\2\2[\\\7,\2\2\\"+
		"\20\3\2\2\2]^\7\60\2\2^\22\3\2\2\2_`\7,\2\2`\24\3\2\2\2ab\7\61\2\2b\26"+
		"\3\2\2\2cd\7\'\2\2d\30\3\2\2\2ef\7-\2\2f\32\3\2\2\2gh\7/\2\2h\34\3\2\2"+
		"\2ij\7A\2\2jk\7A\2\2k\36\3\2\2\2lm\7?\2\2m \3\2\2\2no\7?\2\2op\7@\2\2"+
		"p\"\3\2\2\2qr\7*\2\2r$\3\2\2\2st\7+\2\2t&\3\2\2\2uv\7.\2\2v(\3\2\2\2w"+
		"x\7=\2\2x*\3\2\2\2y{\t\5\2\2zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2\2\2}"+
		"~\3\2\2\2~\177\b\26\2\2\177,\3\2\2\2\n\2\67>DIOU|\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
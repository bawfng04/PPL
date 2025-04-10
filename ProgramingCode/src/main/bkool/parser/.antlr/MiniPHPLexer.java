// Generated from d:/PPL_Initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class MiniPHPLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

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
		"\u0004\u0000\u0015~\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0005\u00014\b\u0001\n\u0001\f\u00017\t\u0001\u0001"+
		"\u0002\u0001\u0002\u0005\u0002;\b\u0002\n\u0002\f\u0002>\t\u0002\u0001"+
		"\u0003\u0004\u0003A\b\u0003\u000b\u0003\f\u0003B\u0001\u0004\u0004\u0004"+
		"F\b\u0004\u000b\u0004\f\u0004G\u0001\u0004\u0001\u0004\u0004\u0004L\b"+
		"\u0004\u000b\u0004\f\u0004M\u0001\u0005\u0001\u0005\u0005\u0005R\b\u0005"+
		"\n\u0005\f\u0005U\t\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0014\u0004\u0014y\b\u0014\u000b\u0014\f\u0014z\u0001"+
		"\u0014\u0001\u0014\u0001S\u0000\u0015\u0001\u0001\u0003\u0002\u0005\u0003"+
		"\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015"+
		"\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012"+
		"%\u0013\'\u0014)\u0015\u0001\u0000\u0004\u0003\u0000AZ__az\u0004\u0000"+
		"09AZ__az\u0001\u000009\u0003\u0000\t\n\r\r  \u0084\u0000\u0001\u0001\u0000"+
		"\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000"+
		"\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000"+
		"\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000"+
		"\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000"+
		"\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000"+
		"\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000"+
		"\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000"+
		"\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000"+
		"#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001"+
		"\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0001+\u0001\u0000\u0000"+
		"\u0000\u00031\u0001\u0000\u0000\u0000\u00058\u0001\u0000\u0000\u0000\u0007"+
		"@\u0001\u0000\u0000\u0000\tE\u0001\u0000\u0000\u0000\u000bO\u0001\u0000"+
		"\u0000\u0000\rX\u0001\u0000\u0000\u0000\u000f[\u0001\u0000\u0000\u0000"+
		"\u0011]\u0001\u0000\u0000\u0000\u0013_\u0001\u0000\u0000\u0000\u0015a"+
		"\u0001\u0000\u0000\u0000\u0017c\u0001\u0000\u0000\u0000\u0019e\u0001\u0000"+
		"\u0000\u0000\u001bg\u0001\u0000\u0000\u0000\u001dj\u0001\u0000\u0000\u0000"+
		"\u001fl\u0001\u0000\u0000\u0000!o\u0001\u0000\u0000\u0000#q\u0001\u0000"+
		"\u0000\u0000%s\u0001\u0000\u0000\u0000\'u\u0001\u0000\u0000\u0000)x\u0001"+
		"\u0000\u0000\u0000+,\u0005a\u0000\u0000,-\u0005r\u0000\u0000-.\u0005r"+
		"\u0000\u0000./\u0005a\u0000\u0000/0\u0005y\u0000\u00000\u0002\u0001\u0000"+
		"\u0000\u000015\u0007\u0000\u0000\u000024\u0007\u0001\u0000\u000032\u0001"+
		"\u0000\u0000\u000047\u0001\u0000\u0000\u000053\u0001\u0000\u0000\u0000"+
		"56\u0001\u0000\u0000\u00006\u0004\u0001\u0000\u0000\u000075\u0001\u0000"+
		"\u0000\u00008<\u0007\u0000\u0000\u00009;\u0007\u0001\u0000\u0000:9\u0001"+
		"\u0000\u0000\u0000;>\u0001\u0000\u0000\u0000<:\u0001\u0000\u0000\u0000"+
		"<=\u0001\u0000\u0000\u0000=\u0006\u0001\u0000\u0000\u0000><\u0001\u0000"+
		"\u0000\u0000?A\u0007\u0002\u0000\u0000@?\u0001\u0000\u0000\u0000AB\u0001"+
		"\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000"+
		"C\b\u0001\u0000\u0000\u0000DF\u0007\u0002\u0000\u0000ED\u0001\u0000\u0000"+
		"\u0000FG\u0001\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000GH\u0001\u0000"+
		"\u0000\u0000HI\u0001\u0000\u0000\u0000IK\u0005.\u0000\u0000JL\u0007\u0002"+
		"\u0000\u0000KJ\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000MK\u0001"+
		"\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000N\n\u0001\u0000\u0000\u0000"+
		"OS\u0005\"\u0000\u0000PR\t\u0000\u0000\u0000QP\u0001\u0000\u0000\u0000"+
		"RU\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000"+
		"\u0000TV\u0001\u0000\u0000\u0000US\u0001\u0000\u0000\u0000VW\u0005\"\u0000"+
		"\u0000W\f\u0001\u0000\u0000\u0000XY\u0005*\u0000\u0000YZ\u0005*\u0000"+
		"\u0000Z\u000e\u0001\u0000\u0000\u0000[\\\u0005.\u0000\u0000\\\u0010\u0001"+
		"\u0000\u0000\u0000]^\u0005*\u0000\u0000^\u0012\u0001\u0000\u0000\u0000"+
		"_`\u0005/\u0000\u0000`\u0014\u0001\u0000\u0000\u0000ab\u0005%\u0000\u0000"+
		"b\u0016\u0001\u0000\u0000\u0000cd\u0005+\u0000\u0000d\u0018\u0001\u0000"+
		"\u0000\u0000ef\u0005-\u0000\u0000f\u001a\u0001\u0000\u0000\u0000gh\u0005"+
		"?\u0000\u0000hi\u0005?\u0000\u0000i\u001c\u0001\u0000\u0000\u0000jk\u0005"+
		"=\u0000\u0000k\u001e\u0001\u0000\u0000\u0000lm\u0005=\u0000\u0000mn\u0005"+
		">\u0000\u0000n \u0001\u0000\u0000\u0000op\u0005(\u0000\u0000p\"\u0001"+
		"\u0000\u0000\u0000qr\u0005)\u0000\u0000r$\u0001\u0000\u0000\u0000st\u0005"+
		",\u0000\u0000t&\u0001\u0000\u0000\u0000uv\u0005;\u0000\u0000v(\u0001\u0000"+
		"\u0000\u0000wy\u0007\u0003\u0000\u0000xw\u0001\u0000\u0000\u0000yz\u0001"+
		"\u0000\u0000\u0000zx\u0001\u0000\u0000\u0000z{\u0001\u0000\u0000\u0000"+
		"{|\u0001\u0000\u0000\u0000|}\u0006\u0014\u0000\u0000}*\u0001\u0000\u0000"+
		"\u0000\b\u00005<BGMSz\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
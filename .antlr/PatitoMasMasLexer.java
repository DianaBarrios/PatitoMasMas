// Generated from /Users/alberto/Documents/PatitoMasMas/Código/PatitoMasMas.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PatitoMasMasLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, Programa=23, Principal=24, 
		Var=25, Function=26, Regresa=27, Lee=28, Escribe=29, Si=30, Entonces=31, 
		Sino=32, Mientras=33, Haz=34, Desde=35, Hasta=36, Hacer=37, Int=38, Float=39, 
		Char=40, Void=41, ID=42, CTE_INT=43, CTE_FLOAT=44, CTE_CHAR=45, CTE_STRING=46, 
		DIGIT=47, Whitespace=48, Newline=49;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
		"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
		"T__17", "T__18", "T__19", "T__20", "T__21", "Programa", "Principal", 
		"Var", "Function", "Regresa", "Lee", "Escribe", "Si", "Entonces", "Sino", 
		"Mientras", "Haz", "Desde", "Hasta", "Hacer", "Int", "Float", "Char", 
		"Void", "ID", "CTE_INT", "CTE_FLOAT", "CTE_CHAR", "CTE_STRING", "DIGIT", 
		"Whitespace", "Newline"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "';'", "','", "'['", "']'", "'('", "')'", "'{'", "'}'", "'='", "'&'", 
		"'||'", "'>'", "'<'", "'=='", "'!='", "'+'", "'-'", "'*'", "'/'", "'$'", 
		"'?'", "'\u00A1'", "'programa'", "'principal()'", "'var'", "'funcion'", 
		"'regresa'", "'lee'", "'escribe'", "'si'", "'entonces'", "'sino'", "'mientras'", 
		"'haz'", "'desde'", "'hasta'", "'hacer'", "'int'", "'float'", "'char'", 
		"'void'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, "Programa", 
		"Principal", "Var", "Function", "Regresa", "Lee", "Escribe", "Si", "Entonces", 
		"Sino", "Mientras", "Haz", "Desde", "Hasta", "Hacer", "Int", "Float", 
		"Char", "Void", "ID", "CTE_INT", "CTE_FLOAT", "CTE_CHAR", "CTE_STRING", 
		"DIGIT", "Whitespace", "Newline"
	};
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


	public PatitoMasMasLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "PatitoMasMas.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63\u013c\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\3\3"+
		"\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3"+
		"\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3"+
		"\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3"+
		"\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3"+
		"\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3"+
		"\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3"+
		"\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3"+
		" \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3"+
		"#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3"+
		"\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\7+\u0110"+
		"\n+\f+\16+\u0113\13+\3,\6,\u0116\n,\r,\16,\u0117\3-\3-\3-\3-\3.\3.\3."+
		"\3.\3/\3/\7/\u0124\n/\f/\16/\u0127\13/\3/\3/\3\60\3\60\3\61\6\61\u012e"+
		"\n\61\r\61\16\61\u012f\3\61\3\61\3\62\3\62\5\62\u0136\n\62\3\62\5\62\u0139"+
		"\n\62\3\62\3\62\2\2\63\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27"+
		"\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33"+
		"\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63"+
		"\3\2\7\3\2c|\5\2\62;C\\c|\4\2C\\c|\3\2$$\4\2\13\13\"\"\2\u0141\2\3\3\2"+
		"\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17"+
		"\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2"+
		"\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3"+
		"\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3"+
		"\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2"+
		"=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3"+
		"\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2"+
		"\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2"+
		"c\3\2\2\2\3e\3\2\2\2\5g\3\2\2\2\7i\3\2\2\2\tk\3\2\2\2\13m\3\2\2\2\ro\3"+
		"\2\2\2\17q\3\2\2\2\21s\3\2\2\2\23u\3\2\2\2\25w\3\2\2\2\27y\3\2\2\2\31"+
		"|\3\2\2\2\33~\3\2\2\2\35\u0080\3\2\2\2\37\u0083\3\2\2\2!\u0086\3\2\2\2"+
		"#\u0088\3\2\2\2%\u008a\3\2\2\2\'\u008c\3\2\2\2)\u008e\3\2\2\2+\u0090\3"+
		"\2\2\2-\u0092\3\2\2\2/\u0094\3\2\2\2\61\u009d\3\2\2\2\63\u00a9\3\2\2\2"+
		"\65\u00ad\3\2\2\2\67\u00b5\3\2\2\29\u00bd\3\2\2\2;\u00c1\3\2\2\2=\u00c9"+
		"\3\2\2\2?\u00cc\3\2\2\2A\u00d5\3\2\2\2C\u00da\3\2\2\2E\u00e3\3\2\2\2G"+
		"\u00e7\3\2\2\2I\u00ed\3\2\2\2K\u00f3\3\2\2\2M\u00f9\3\2\2\2O\u00fd\3\2"+
		"\2\2Q\u0103\3\2\2\2S\u0108\3\2\2\2U\u010d\3\2\2\2W\u0115\3\2\2\2Y\u0119"+
		"\3\2\2\2[\u011d\3\2\2\2]\u0121\3\2\2\2_\u012a\3\2\2\2a\u012d\3\2\2\2c"+
		"\u0138\3\2\2\2ef\7=\2\2f\4\3\2\2\2gh\7.\2\2h\6\3\2\2\2ij\7]\2\2j\b\3\2"+
		"\2\2kl\7_\2\2l\n\3\2\2\2mn\7*\2\2n\f\3\2\2\2op\7+\2\2p\16\3\2\2\2qr\7"+
		"}\2\2r\20\3\2\2\2st\7\177\2\2t\22\3\2\2\2uv\7?\2\2v\24\3\2\2\2wx\7(\2"+
		"\2x\26\3\2\2\2yz\7~\2\2z{\7~\2\2{\30\3\2\2\2|}\7@\2\2}\32\3\2\2\2~\177"+
		"\7>\2\2\177\34\3\2\2\2\u0080\u0081\7?\2\2\u0081\u0082\7?\2\2\u0082\36"+
		"\3\2\2\2\u0083\u0084\7#\2\2\u0084\u0085\7?\2\2\u0085 \3\2\2\2\u0086\u0087"+
		"\7-\2\2\u0087\"\3\2\2\2\u0088\u0089\7/\2\2\u0089$\3\2\2\2\u008a\u008b"+
		"\7,\2\2\u008b&\3\2\2\2\u008c\u008d\7\61\2\2\u008d(\3\2\2\2\u008e\u008f"+
		"\7&\2\2\u008f*\3\2\2\2\u0090\u0091\7A\2\2\u0091,\3\2\2\2\u0092\u0093\7"+
		"\u00a3\2\2\u0093.\3\2\2\2\u0094\u0095\7r\2\2\u0095\u0096\7t\2\2\u0096"+
		"\u0097\7q\2\2\u0097\u0098\7i\2\2\u0098\u0099\7t\2\2\u0099\u009a\7c\2\2"+
		"\u009a\u009b\7o\2\2\u009b\u009c\7c\2\2\u009c\60\3\2\2\2\u009d\u009e\7"+
		"r\2\2\u009e\u009f\7t\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1\7p\2\2\u00a1\u00a2"+
		"\7e\2\2\u00a2\u00a3\7k\2\2\u00a3\u00a4\7r\2\2\u00a4\u00a5\7c\2\2\u00a5"+
		"\u00a6\7n\2\2\u00a6\u00a7\7*\2\2\u00a7\u00a8\7+\2\2\u00a8\62\3\2\2\2\u00a9"+
		"\u00aa\7x\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7t\2\2\u00ac\64\3\2\2\2\u00ad"+
		"\u00ae\7h\2\2\u00ae\u00af\7w\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7e\2\2"+
		"\u00b1\u00b2\7k\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4\7p\2\2\u00b4\66\3\2"+
		"\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7i\2\2\u00b8\u00b9"+
		"\7t\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc\7c\2\2\u00bc"+
		"8\3\2\2\2\u00bd\u00be\7n\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7g\2\2\u00c0"+
		":\3\2\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\7u\2\2\u00c3\u00c4\7e\2\2\u00c4"+
		"\u00c5\7t\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7d\2\2\u00c7\u00c8\7g\2\2"+
		"\u00c8<\3\2\2\2\u00c9\u00ca\7u\2\2\u00ca\u00cb\7k\2\2\u00cb>\3\2\2\2\u00cc"+
		"\u00cd\7g\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0\7q\2\2"+
		"\u00d0\u00d1\7p\2\2\u00d1\u00d2\7e\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4"+
		"\7u\2\2\u00d4@\3\2\2\2\u00d5\u00d6\7u\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8"+
		"\7p\2\2\u00d8\u00d9\7q\2\2\u00d9B\3\2\2\2\u00da\u00db\7o\2\2\u00db\u00dc"+
		"\7k\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7v\2\2\u00df"+
		"\u00e0\7t\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7u\2\2\u00e2D\3\2\2\2\u00e3"+
		"\u00e4\7j\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7|\2\2\u00e6F\3\2\2\2\u00e7"+
		"\u00e8\7f\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea\7u\2\2\u00ea\u00eb\7f\2\2"+
		"\u00eb\u00ec\7g\2\2\u00ecH\3\2\2\2\u00ed\u00ee\7j\2\2\u00ee\u00ef\7c\2"+
		"\2\u00ef\u00f0\7u\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7c\2\2\u00f2J\3\2"+
		"\2\2\u00f3\u00f4\7j\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7e\2\2\u00f6\u00f7"+
		"\7g\2\2\u00f7\u00f8\7t\2\2\u00f8L\3\2\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb"+
		"\7p\2\2\u00fb\u00fc\7v\2\2\u00fcN\3\2\2\2\u00fd\u00fe\7h\2\2\u00fe\u00ff"+
		"\7n\2\2\u00ff\u0100\7q\2\2\u0100\u0101\7c\2\2\u0101\u0102\7v\2\2\u0102"+
		"P\3\2\2\2\u0103\u0104\7e\2\2\u0104\u0105\7j\2\2\u0105\u0106\7c\2\2\u0106"+
		"\u0107\7t\2\2\u0107R\3\2\2\2\u0108\u0109\7x\2\2\u0109\u010a\7q\2\2\u010a"+
		"\u010b\7k\2\2\u010b\u010c\7f\2\2\u010cT\3\2\2\2\u010d\u0111\t\2\2\2\u010e"+
		"\u0110\t\3\2\2\u010f\u010e\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f\3\2"+
		"\2\2\u0111\u0112\3\2\2\2\u0112V\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0116"+
		"\5_\60\2\u0115\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0115\3\2\2\2\u0117"+
		"\u0118\3\2\2\2\u0118X\3\2\2\2\u0119\u011a\5W,\2\u011a\u011b\7\60\2\2\u011b"+
		"\u011c\5W,\2\u011cZ\3\2\2\2\u011d\u011e\7)\2\2\u011e\u011f\t\4\2\2\u011f"+
		"\u0120\7)\2\2\u0120\\\3\2\2\2\u0121\u0125\7$\2\2\u0122\u0124\n\5\2\2\u0123"+
		"\u0122\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2"+
		"\2\2\u0126\u0128\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0129\7$\2\2\u0129"+
		"^\3\2\2\2\u012a\u012b\4\62;\2\u012b`\3\2\2\2\u012c\u012e\t\6\2\2\u012d"+
		"\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130\3\2"+
		"\2\2\u0130\u0131\3\2\2\2\u0131\u0132\b\61\2\2\u0132b\3\2\2\2\u0133\u0135"+
		"\7\17\2\2\u0134\u0136\7\f\2\2\u0135\u0134\3\2\2\2\u0135\u0136\3\2\2\2"+
		"\u0136\u0139\3\2\2\2\u0137\u0139\7\f\2\2\u0138\u0133\3\2\2\2\u0138\u0137"+
		"\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013b\b\62\2\2\u013bd\3\2\2\2\t\2\u0111"+
		"\u0117\u0125\u012f\u0135\u0138\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
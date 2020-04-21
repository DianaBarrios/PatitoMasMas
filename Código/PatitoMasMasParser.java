// Generated from PatitoMasMas.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PatitoMasMasParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

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
	public static final int
		RULE_start = 0, RULE_programa = 1, RULE_principal = 2, RULE_dec_variables = 3, 
		RULE_dec_var = 4, RULE_lista_ids = 5, RULE_ids = 6, RULE_dimension = 7, 
		RULE_dec_functions = 8, RULE_funcion = 9, RULE_tipo_ret = 10, RULE_params = 11, 
		RULE_bloque_est = 12, RULE_estatuto = 13, RULE_asignacion = 14, RULE_var = 15, 
		RULE_dim = 16, RULE_retorno = 17, RULE_lectura = 18, RULE_lista_vars = 19, 
		RULE_escritura = 20, RULE_escrituras = 21, RULE_string = 22, RULE_decision = 23, 
		RULE_repeticion = 24, RULE_condicional = 25, RULE_no_condicional = 26, 
		RULE_llamada = 27, RULE_params_llamada = 28, RULE_llamada_est = 29, RULE_expresion = 30, 
		RULE_op_log = 31, RULE_op_comp = 32, RULE_exp = 33, RULE_op_arit = 34, 
		RULE_term = 35, RULE_op_prod = 36, RULE_factor = 37, RULE_var_cte = 38, 
		RULE_op_esp = 39, RULE_tipo = 40;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "programa", "principal", "dec_variables", "dec_var", "lista_ids", 
			"ids", "dimension", "dec_functions", "funcion", "tipo_ret", "params", 
			"bloque_est", "estatuto", "asignacion", "var", "dim", "retorno", "lectura", 
			"lista_vars", "escritura", "escrituras", "string", "decision", "repeticion", 
			"condicional", "no_condicional", "llamada", "params_llamada", "llamada_est", 
			"expresion", "op_log", "op_comp", "exp", "op_arit", "term", "op_prod", 
			"factor", "var_cte", "op_esp", "tipo"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "','", "'['", "']'", "'('", "')'", "'{'", "'}'", "'='", 
			"'&'", "'||'", "'>'", "'<'", "'=='", "'!='", "'+'", "'-'", "'*'", "'/'", 
			"'$'", "'?'", "'\u00A1'", "'programa'", "'principal()'", "'var'", "'funcion'", 
			"'regresa'", "'lee'", "'escribe'", "'si'", "'entonces'", "'sino'", "'mientras'", 
			"'haz'", "'desde'", "'hasta'", "'hacer'", "'int'", "'float'", "'char'", 
			"'void'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, "Programa", 
			"Principal", "Var", "Function", "Regresa", "Lee", "Escribe", "Si", "Entonces", 
			"Sino", "Mientras", "Haz", "Desde", "Hasta", "Hacer", "Int", "Float", 
			"Char", "Void", "ID", "CTE_INT", "CTE_FLOAT", "CTE_CHAR", "CTE_STRING", 
			"DIGIT", "Whitespace", "Newline"
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
	public String getGrammarFileName() { return "PatitoMasMas.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PatitoMasMasParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(PatitoMasMasParser.EOF, 0); }
		public ProgramaContext programa() {
			return getRuleContext(ProgramaContext.class,0);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterStart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitStart(this);
		}
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Programa) {
				{
				setState(82);
				programa();
				}
			}

			setState(85);
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

	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode Programa() { return getToken(PatitoMasMasParser.Programa, 0); }
		public TerminalNode ID() { return getToken(PatitoMasMasParser.ID, 0); }
		public PrincipalContext principal() {
			return getRuleContext(PrincipalContext.class,0);
		}
		public Dec_variablesContext dec_variables() {
			return getRuleContext(Dec_variablesContext.class,0);
		}
		public Dec_functionsContext dec_functions() {
			return getRuleContext(Dec_functionsContext.class,0);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterPrograma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitPrograma(this);
		}
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(Programa);
			setState(88);
			match(ID);
			setState(89);
			match(T__0);
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Var) {
				{
				setState(90);
				dec_variables();
				}
			}

			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Function) {
				{
				setState(93);
				dec_functions();
				}
			}

			setState(96);
			principal();
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

	public static class PrincipalContext extends ParserRuleContext {
		public TerminalNode Principal() { return getToken(PatitoMasMasParser.Principal, 0); }
		public Bloque_estContext bloque_est() {
			return getRuleContext(Bloque_estContext.class,0);
		}
		public PrincipalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_principal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterPrincipal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitPrincipal(this);
		}
	}

	public final PrincipalContext principal() throws RecognitionException {
		PrincipalContext _localctx = new PrincipalContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_principal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			match(Principal);
			setState(99);
			bloque_est();
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

	public static class Dec_variablesContext extends ParserRuleContext {
		public TerminalNode Var() { return getToken(PatitoMasMasParser.Var, 0); }
		public List<Dec_varContext> dec_var() {
			return getRuleContexts(Dec_varContext.class);
		}
		public Dec_varContext dec_var(int i) {
			return getRuleContext(Dec_varContext.class,i);
		}
		public Dec_variablesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dec_variables; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterDec_variables(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitDec_variables(this);
		}
	}

	public final Dec_variablesContext dec_variables() throws RecognitionException {
		Dec_variablesContext _localctx = new Dec_variablesContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_dec_variables);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			match(Var);
			setState(103); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(102);
				dec_var();
				}
				}
				setState(105); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==Int || _la==Float );
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

	public static class Dec_varContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public List<Lista_idsContext> lista_ids() {
			return getRuleContexts(Lista_idsContext.class);
		}
		public Lista_idsContext lista_ids(int i) {
			return getRuleContext(Lista_idsContext.class,i);
		}
		public Dec_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dec_var; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterDec_var(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitDec_var(this);
		}
	}

	public final Dec_varContext dec_var() throws RecognitionException {
		Dec_varContext _localctx = new Dec_varContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_dec_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			tipo();
			setState(109); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(108);
				lista_ids();
				}
				}
				setState(111); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			setState(113);
			match(T__0);
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

	public static class Lista_idsContext extends ParserRuleContext {
		public IdsContext ids() {
			return getRuleContext(IdsContext.class,0);
		}
		public Lista_idsContext lista_ids() {
			return getRuleContext(Lista_idsContext.class,0);
		}
		public Lista_idsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_ids; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterLista_ids(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitLista_ids(this);
		}
	}

	public final Lista_idsContext lista_ids() throws RecognitionException {
		Lista_idsContext _localctx = new Lista_idsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_lista_ids);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			ids();
			setState(118);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(116);
				match(T__1);
				setState(117);
				lista_ids();
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

	public static class IdsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PatitoMasMasParser.ID, 0); }
		public List<DimensionContext> dimension() {
			return getRuleContexts(DimensionContext.class);
		}
		public DimensionContext dimension(int i) {
			return getRuleContext(DimensionContext.class,i);
		}
		public IdsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ids; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterIds(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitIds(this);
		}
	}

	public final IdsContext ids() throws RecognitionException {
		IdsContext _localctx = new IdsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_ids);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(ID);
			setState(122);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(121);
				dimension();
				}
				break;
			}
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2) {
				{
				setState(124);
				dimension();
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

	public static class DimensionContext extends ParserRuleContext {
		public TerminalNode CTE_INT() { return getToken(PatitoMasMasParser.CTE_INT, 0); }
		public DimensionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dimension; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterDimension(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitDimension(this);
		}
	}

	public final DimensionContext dimension() throws RecognitionException {
		DimensionContext _localctx = new DimensionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_dimension);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(T__2);
			setState(128);
			match(CTE_INT);
			setState(129);
			match(T__3);
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

	public static class Dec_functionsContext extends ParserRuleContext {
		public List<FuncionContext> funcion() {
			return getRuleContexts(FuncionContext.class);
		}
		public FuncionContext funcion(int i) {
			return getRuleContext(FuncionContext.class,i);
		}
		public Dec_functionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dec_functions; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterDec_functions(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitDec_functions(this);
		}
	}

	public final Dec_functionsContext dec_functions() throws RecognitionException {
		Dec_functionsContext _localctx = new Dec_functionsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_dec_functions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(131);
				funcion();
				}
				}
				setState(134); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==Function );
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

	public static class FuncionContext extends ParserRuleContext {
		public TerminalNode Function() { return getToken(PatitoMasMasParser.Function, 0); }
		public Tipo_retContext tipo_ret() {
			return getRuleContext(Tipo_retContext.class,0);
		}
		public TerminalNode ID() { return getToken(PatitoMasMasParser.ID, 0); }
		public Bloque_estContext bloque_est() {
			return getRuleContext(Bloque_estContext.class,0);
		}
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public Dec_variablesContext dec_variables() {
			return getRuleContext(Dec_variablesContext.class,0);
		}
		public FuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterFuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitFuncion(this);
		}
	}

	public final FuncionContext funcion() throws RecognitionException {
		FuncionContext _localctx = new FuncionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_funcion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			match(Function);
			setState(137);
			tipo_ret();
			setState(138);
			match(ID);
			setState(139);
			match(T__4);
			setState(141);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Int || _la==Float) {
				{
				setState(140);
				params();
				}
			}

			setState(143);
			match(T__5);
			setState(144);
			match(T__0);
			setState(146);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Var) {
				{
				setState(145);
				dec_variables();
				}
			}

			setState(148);
			bloque_est();
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

	public static class Tipo_retContext extends ParserRuleContext {
		public TerminalNode Void() { return getToken(PatitoMasMasParser.Void, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public Tipo_retContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo_ret; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterTipo_ret(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitTipo_ret(this);
		}
	}

	public final Tipo_retContext tipo_ret() throws RecognitionException {
		Tipo_retContext _localctx = new Tipo_retContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_tipo_ret);
		try {
			setState(152);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Void:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				match(Void);
				}
				break;
			case Int:
			case Float:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				tipo();
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

	public static class ParamsContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(PatitoMasMasParser.ID, 0); }
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterParams(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitParams(this);
		}
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			tipo();
			setState(155);
			match(ID);
			setState(158);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(156);
				match(T__1);
				setState(157);
				params();
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

	public static class Bloque_estContext extends ParserRuleContext {
		public List<EstatutoContext> estatuto() {
			return getRuleContexts(EstatutoContext.class);
		}
		public EstatutoContext estatuto(int i) {
			return getRuleContext(EstatutoContext.class,i);
		}
		public Bloque_estContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque_est; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterBloque_est(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitBloque_est(this);
		}
	}

	public final Bloque_estContext bloque_est() throws RecognitionException {
		Bloque_estContext _localctx = new Bloque_estContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_bloque_est);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			match(T__6);
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Regresa) | (1L << Lee) | (1L << Escribe) | (1L << Si) | (1L << Mientras) | (1L << Desde) | (1L << ID))) != 0)) {
				{
				{
				setState(161);
				estatuto();
				}
				}
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(167);
			match(T__7);
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

	public static class EstatutoContext extends ParserRuleContext {
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public RetornoContext retorno() {
			return getRuleContext(RetornoContext.class,0);
		}
		public LecturaContext lectura() {
			return getRuleContext(LecturaContext.class,0);
		}
		public DecisionContext decision() {
			return getRuleContext(DecisionContext.class,0);
		}
		public RepeticionContext repeticion() {
			return getRuleContext(RepeticionContext.class,0);
		}
		public Llamada_estContext llamada_est() {
			return getRuleContext(Llamada_estContext.class,0);
		}
		public EscrituraContext escritura() {
			return getRuleContext(EscrituraContext.class,0);
		}
		public EstatutoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_estatuto; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterEstatuto(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitEstatuto(this);
		}
	}

	public final EstatutoContext estatuto() throws RecognitionException {
		EstatutoContext _localctx = new EstatutoContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_estatuto);
		try {
			setState(176);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(169);
				asignacion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(170);
				retorno();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(171);
				lectura();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(172);
				decision();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(173);
				repeticion();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(174);
				llamada_est();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(175);
				escritura();
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

	public static class AsignacionContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterAsignacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitAsignacion(this);
		}
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			var();
			setState(179);
			match(T__8);
			setState(180);
			expresion(0);
			setState(181);
			match(T__0);
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

	public static class VarContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PatitoMasMasParser.ID, 0); }
		public List<DimContext> dim() {
			return getRuleContexts(DimContext.class);
		}
		public DimContext dim(int i) {
			return getRuleContext(DimContext.class,i);
		}
		public VarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterVar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitVar(this);
		}
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(183);
			match(ID);
			setState(185);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(184);
				dim();
				}
				break;
			}
			setState(188);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				setState(187);
				dim();
				}
				break;
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

	public static class DimContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public DimContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dim; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterDim(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitDim(this);
		}
	}

	public final DimContext dim() throws RecognitionException {
		DimContext _localctx = new DimContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_dim);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			match(T__2);
			setState(191);
			expresion(0);
			setState(192);
			match(T__3);
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

	public static class RetornoContext extends ParserRuleContext {
		public TerminalNode Regresa() { return getToken(PatitoMasMasParser.Regresa, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public RetornoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_retorno; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterRetorno(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitRetorno(this);
		}
	}

	public final RetornoContext retorno() throws RecognitionException {
		RetornoContext _localctx = new RetornoContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_retorno);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			match(Regresa);
			setState(195);
			match(T__4);
			setState(196);
			expresion(0);
			setState(197);
			match(T__5);
			setState(198);
			match(T__0);
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

	public static class LecturaContext extends ParserRuleContext {
		public TerminalNode Lee() { return getToken(PatitoMasMasParser.Lee, 0); }
		public Lista_varsContext lista_vars() {
			return getRuleContext(Lista_varsContext.class,0);
		}
		public LecturaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lectura; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterLectura(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitLectura(this);
		}
	}

	public final LecturaContext lectura() throws RecognitionException {
		LecturaContext _localctx = new LecturaContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_lectura);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			match(Lee);
			setState(201);
			match(T__4);
			setState(202);
			lista_vars();
			setState(203);
			match(T__5);
			setState(204);
			match(T__0);
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

	public static class Lista_varsContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public Lista_varsContext lista_vars() {
			return getRuleContext(Lista_varsContext.class,0);
		}
		public Lista_varsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_vars; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterLista_vars(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitLista_vars(this);
		}
	}

	public final Lista_varsContext lista_vars() throws RecognitionException {
		Lista_varsContext _localctx = new Lista_varsContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_lista_vars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			var();
			setState(209);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(207);
				match(T__1);
				setState(208);
				lista_vars();
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

	public static class EscrituraContext extends ParserRuleContext {
		public TerminalNode Escribe() { return getToken(PatitoMasMasParser.Escribe, 0); }
		public EscriturasContext escrituras() {
			return getRuleContext(EscriturasContext.class,0);
		}
		public EscrituraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_escritura; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterEscritura(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitEscritura(this);
		}
	}

	public final EscrituraContext escritura() throws RecognitionException {
		EscrituraContext _localctx = new EscrituraContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_escritura);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			match(Escribe);
			setState(212);
			match(T__4);
			setState(213);
			escrituras();
			setState(214);
			match(T__5);
			setState(215);
			match(T__0);
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

	public static class EscriturasContext extends ParserRuleContext {
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public EscriturasContext escrituras() {
			return getRuleContext(EscriturasContext.class,0);
		}
		public EscriturasContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_escrituras; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterEscrituras(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitEscrituras(this);
		}
	}

	public final EscriturasContext escrituras() throws RecognitionException {
		EscriturasContext _localctx = new EscriturasContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_escrituras);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CTE_STRING:
				{
				setState(217);
				string();
				}
				break;
			case T__4:
			case T__15:
			case T__16:
			case ID:
			case CTE_INT:
			case CTE_FLOAT:
				{
				setState(218);
				expresion(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(223);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(221);
				match(T__1);
				setState(222);
				escrituras();
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

	public static class StringContext extends ParserRuleContext {
		public TerminalNode CTE_STRING() { return getToken(PatitoMasMasParser.CTE_STRING, 0); }
		public StringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitString(this);
		}
	}

	public final StringContext string() throws RecognitionException {
		StringContext _localctx = new StringContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_string);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			match(CTE_STRING);
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

	public static class DecisionContext extends ParserRuleContext {
		public TerminalNode Si() { return getToken(PatitoMasMasParser.Si, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode Entonces() { return getToken(PatitoMasMasParser.Entonces, 0); }
		public List<Bloque_estContext> bloque_est() {
			return getRuleContexts(Bloque_estContext.class);
		}
		public Bloque_estContext bloque_est(int i) {
			return getRuleContext(Bloque_estContext.class,i);
		}
		public TerminalNode Sino() { return getToken(PatitoMasMasParser.Sino, 0); }
		public DecisionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decision; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterDecision(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitDecision(this);
		}
	}

	public final DecisionContext decision() throws RecognitionException {
		DecisionContext _localctx = new DecisionContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_decision);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(227);
			match(Si);
			setState(228);
			match(T__4);
			setState(229);
			expresion(0);
			setState(230);
			match(T__5);
			setState(231);
			match(Entonces);
			setState(232);
			bloque_est();
			setState(235);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Sino) {
				{
				setState(233);
				match(Sino);
				setState(234);
				bloque_est();
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

	public static class RepeticionContext extends ParserRuleContext {
		public CondicionalContext condicional() {
			return getRuleContext(CondicionalContext.class,0);
		}
		public No_condicionalContext no_condicional() {
			return getRuleContext(No_condicionalContext.class,0);
		}
		public RepeticionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repeticion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterRepeticion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitRepeticion(this);
		}
	}

	public final RepeticionContext repeticion() throws RecognitionException {
		RepeticionContext _localctx = new RepeticionContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_repeticion);
		try {
			setState(239);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Mientras:
				enterOuterAlt(_localctx, 1);
				{
				setState(237);
				condicional();
				}
				break;
			case Desde:
				enterOuterAlt(_localctx, 2);
				{
				setState(238);
				no_condicional();
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

	public static class CondicionalContext extends ParserRuleContext {
		public TerminalNode Mientras() { return getToken(PatitoMasMasParser.Mientras, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode Haz() { return getToken(PatitoMasMasParser.Haz, 0); }
		public Bloque_estContext bloque_est() {
			return getRuleContext(Bloque_estContext.class,0);
		}
		public CondicionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicional; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterCondicional(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitCondicional(this);
		}
	}

	public final CondicionalContext condicional() throws RecognitionException {
		CondicionalContext _localctx = new CondicionalContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_condicional);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			match(Mientras);
			setState(242);
			expresion(0);
			setState(243);
			match(Haz);
			setState(244);
			bloque_est();
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

	public static class No_condicionalContext extends ParserRuleContext {
		public TerminalNode Desde() { return getToken(PatitoMasMasParser.Desde, 0); }
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode Hasta() { return getToken(PatitoMasMasParser.Hasta, 0); }
		public TerminalNode Hacer() { return getToken(PatitoMasMasParser.Hacer, 0); }
		public Bloque_estContext bloque_est() {
			return getRuleContext(Bloque_estContext.class,0);
		}
		public No_condicionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_no_condicional; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterNo_condicional(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitNo_condicional(this);
		}
	}

	public final No_condicionalContext no_condicional() throws RecognitionException {
		No_condicionalContext _localctx = new No_condicionalContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_no_condicional);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(246);
			match(Desde);
			setState(247);
			var();
			setState(248);
			match(T__8);
			setState(249);
			expresion(0);
			setState(250);
			match(Hasta);
			setState(251);
			expresion(0);
			setState(252);
			match(Hacer);
			setState(253);
			bloque_est();
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

	public static class LlamadaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PatitoMasMasParser.ID, 0); }
		public Params_llamadaContext params_llamada() {
			return getRuleContext(Params_llamadaContext.class,0);
		}
		public LlamadaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_llamada; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterLlamada(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitLlamada(this);
		}
	}

	public final LlamadaContext llamada() throws RecognitionException {
		LlamadaContext _localctx = new LlamadaContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_llamada);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(255);
			match(ID);
			setState(256);
			match(T__4);
			setState(258);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__4) | (1L << T__15) | (1L << T__16) | (1L << ID) | (1L << CTE_INT) | (1L << CTE_FLOAT))) != 0)) {
				{
				setState(257);
				params_llamada();
				}
			}

			setState(260);
			match(T__5);
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

	public static class Params_llamadaContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public Params_llamadaContext params_llamada() {
			return getRuleContext(Params_llamadaContext.class,0);
		}
		public Params_llamadaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params_llamada; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterParams_llamada(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitParams_llamada(this);
		}
	}

	public final Params_llamadaContext params_llamada() throws RecognitionException {
		Params_llamadaContext _localctx = new Params_llamadaContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_params_llamada);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(262);
			expresion(0);
			setState(265);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(263);
				match(T__1);
				setState(264);
				params_llamada();
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

	public static class Llamada_estContext extends ParserRuleContext {
		public LlamadaContext llamada() {
			return getRuleContext(LlamadaContext.class,0);
		}
		public Llamada_estContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_llamada_est; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterLlamada_est(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitLlamada_est(this);
		}
	}

	public final Llamada_estContext llamada_est() throws RecognitionException {
		Llamada_estContext _localctx = new Llamada_estContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_llamada_est);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			llamada();
			setState(268);
			match(T__0);
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

	public static class ExpresionContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public Op_compContext op_comp() {
			return getRuleContext(Op_compContext.class,0);
		}
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public Op_logContext op_log() {
			return getRuleContext(Op_logContext.class,0);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterExpresion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitExpresion(this);
		}
	}

	public final ExpresionContext expresion() throws RecognitionException {
		return expresion(0);
	}

	private ExpresionContext expresion(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpresionContext _localctx = new ExpresionContext(_ctx, _parentState);
		ExpresionContext _prevctx = _localctx;
		int _startState = 60;
		enterRecursionRule(_localctx, 60, RULE_expresion, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(276);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				{
				setState(271);
				exp();
				}
				break;
			case 2:
				{
				setState(272);
				exp();
				setState(273);
				op_comp();
				setState(274);
				exp();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(284);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpresionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expresion);
					setState(278);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(279);
					op_log();
					setState(280);
					expresion(3);
					}
					} 
				}
				setState(286);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
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

	public static class Op_logContext extends ParserRuleContext {
		public Op_logContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op_log; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterOp_log(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitOp_log(this);
		}
	}

	public final Op_logContext op_log() throws RecognitionException {
		Op_logContext _localctx = new Op_logContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_op_log);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(287);
			_la = _input.LA(1);
			if ( !(_la==T__9 || _la==T__10) ) {
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

	public static class Op_compContext extends ParserRuleContext {
		public Op_compContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op_comp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterOp_comp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitOp_comp(this);
		}
	}

	public final Op_compContext op_comp() throws RecognitionException {
		Op_compContext _localctx = new Op_compContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_op_comp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(289);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14))) != 0)) ) {
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

	public static class ExpContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Op_aritContext op_arit() {
			return getRuleContext(Op_aritContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitExp(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_exp);
		try {
			setState(296);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(291);
				term();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(292);
				term();
				setState(293);
				op_arit();
				setState(294);
				exp();
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

	public static class Op_aritContext extends ParserRuleContext {
		public Op_aritContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op_arit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterOp_arit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitOp_arit(this);
		}
	}

	public final Op_aritContext op_arit() throws RecognitionException {
		Op_aritContext _localctx = new Op_aritContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_op_arit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(298);
			_la = _input.LA(1);
			if ( !(_la==T__15 || _la==T__16) ) {
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

	public static class TermContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Op_prodContext op_prod() {
			return getRuleContext(Op_prodContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitTerm(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_term);
		try {
			setState(305);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(300);
				factor();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(301);
				factor();
				setState(302);
				op_prod();
				setState(303);
				term();
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

	public static class Op_prodContext extends ParserRuleContext {
		public Op_prodContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op_prod; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterOp_prod(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitOp_prod(this);
		}
	}

	public final Op_prodContext op_prod() throws RecognitionException {
		Op_prodContext _localctx = new Op_prodContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_op_prod);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(307);
			_la = _input.LA(1);
			if ( !(_la==T__17 || _la==T__18) ) {
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

	public static class FactorContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public Op_espContext op_esp() {
			return getRuleContext(Op_espContext.class,0);
		}
		public Var_cteContext var_cte() {
			return getRuleContext(Var_cteContext.class,0);
		}
		public Op_aritContext op_arit() {
			return getRuleContext(Op_aritContext.class,0);
		}
		public LlamadaContext llamada() {
			return getRuleContext(LlamadaContext.class,0);
		}
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitFactor(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_factor);
		int _la;
		try {
			setState(322);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(309);
				var();
				setState(311);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
				case 1:
					{
					setState(310);
					op_esp();
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(314);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__15 || _la==T__16) {
					{
					setState(313);
					op_arit();
					}
				}

				setState(316);
				var_cte();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(317);
				llamada();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(318);
				match(T__4);
				setState(319);
				expresion(0);
				setState(320);
				match(T__5);
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

	public static class Var_cteContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public TerminalNode CTE_INT() { return getToken(PatitoMasMasParser.CTE_INT, 0); }
		public TerminalNode CTE_FLOAT() { return getToken(PatitoMasMasParser.CTE_FLOAT, 0); }
		public Var_cteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_cte; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterVar_cte(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitVar_cte(this);
		}
	}

	public final Var_cteContext var_cte() throws RecognitionException {
		Var_cteContext _localctx = new Var_cteContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_var_cte);
		try {
			setState(327);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(324);
				var();
				}
				break;
			case CTE_INT:
				enterOuterAlt(_localctx, 2);
				{
				setState(325);
				match(CTE_INT);
				}
				break;
			case CTE_FLOAT:
				enterOuterAlt(_localctx, 3);
				{
				setState(326);
				match(CTE_FLOAT);
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

	public static class Op_espContext extends ParserRuleContext {
		public Op_espContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op_esp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterOp_esp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitOp_esp(this);
		}
	}

	public final Op_espContext op_esp() throws RecognitionException {
		Op_espContext _localctx = new Op_espContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_op_esp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(329);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__19) | (1L << T__20) | (1L << T__21))) != 0)) ) {
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

	public static class TipoContext extends ParserRuleContext {
		public TerminalNode Int() { return getToken(PatitoMasMasParser.Int, 0); }
		public TerminalNode Float() { return getToken(PatitoMasMasParser.Float, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterTipo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitTipo(this);
		}
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(331);
			_la = _input.LA(1);
			if ( !(_la==Int || _la==Float) ) {
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 30:
			return expresion_sempred((ExpresionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expresion_sempred(ExpresionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63\u0150\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\5\2"+
		"V\n\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3^\n\3\3\3\5\3a\n\3\3\3\3\3\3\4\3\4\3"+
		"\4\3\5\3\5\6\5j\n\5\r\5\16\5k\3\6\3\6\6\6p\n\6\r\6\16\6q\3\6\3\6\3\7\3"+
		"\7\3\7\5\7y\n\7\3\b\3\b\5\b}\n\b\3\b\5\b\u0080\n\b\3\t\3\t\3\t\3\t\3\n"+
		"\6\n\u0087\n\n\r\n\16\n\u0088\3\13\3\13\3\13\3\13\3\13\5\13\u0090\n\13"+
		"\3\13\3\13\3\13\5\13\u0095\n\13\3\13\3\13\3\f\3\f\5\f\u009b\n\f\3\r\3"+
		"\r\3\r\3\r\5\r\u00a1\n\r\3\16\3\16\7\16\u00a5\n\16\f\16\16\16\u00a8\13"+
		"\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00b3\n\17\3\20"+
		"\3\20\3\20\3\20\3\20\3\21\3\21\5\21\u00bc\n\21\3\21\5\21\u00bf\n\21\3"+
		"\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3"+
		"\24\3\24\3\25\3\25\3\25\5\25\u00d4\n\25\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\27\3\27\5\27\u00de\n\27\3\27\3\27\5\27\u00e2\n\27\3\30\3\30\3\31\3"+
		"\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00ee\n\31\3\32\3\32\5\32\u00f2"+
		"\n\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34"+
		"\3\34\3\35\3\35\3\35\5\35\u0105\n\35\3\35\3\35\3\36\3\36\3\36\5\36\u010c"+
		"\n\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \5 \u0117\n \3 \3 \3 \3 \7 \u011d"+
		"\n \f \16 \u0120\13 \3!\3!\3\"\3\"\3#\3#\3#\3#\3#\5#\u012b\n#\3$\3$\3"+
		"%\3%\3%\3%\3%\5%\u0134\n%\3&\3&\3\'\3\'\5\'\u013a\n\'\3\'\5\'\u013d\n"+
		"\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0145\n\'\3(\3(\3(\5(\u014a\n(\3)\3)\3"+
		"*\3*\3*\2\3>+\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64"+
		"\668:<>@BDFHJLNPR\2\b\3\2\f\r\3\2\16\21\3\2\22\23\3\2\24\25\3\2\26\30"+
		"\3\2()\2\u014e\2U\3\2\2\2\4Y\3\2\2\2\6d\3\2\2\2\bg\3\2\2\2\nm\3\2\2\2"+
		"\fu\3\2\2\2\16z\3\2\2\2\20\u0081\3\2\2\2\22\u0086\3\2\2\2\24\u008a\3\2"+
		"\2\2\26\u009a\3\2\2\2\30\u009c\3\2\2\2\32\u00a2\3\2\2\2\34\u00b2\3\2\2"+
		"\2\36\u00b4\3\2\2\2 \u00b9\3\2\2\2\"\u00c0\3\2\2\2$\u00c4\3\2\2\2&\u00ca"+
		"\3\2\2\2(\u00d0\3\2\2\2*\u00d5\3\2\2\2,\u00dd\3\2\2\2.\u00e3\3\2\2\2\60"+
		"\u00e5\3\2\2\2\62\u00f1\3\2\2\2\64\u00f3\3\2\2\2\66\u00f8\3\2\2\28\u0101"+
		"\3\2\2\2:\u0108\3\2\2\2<\u010d\3\2\2\2>\u0116\3\2\2\2@\u0121\3\2\2\2B"+
		"\u0123\3\2\2\2D\u012a\3\2\2\2F\u012c\3\2\2\2H\u0133\3\2\2\2J\u0135\3\2"+
		"\2\2L\u0144\3\2\2\2N\u0149\3\2\2\2P\u014b\3\2\2\2R\u014d\3\2\2\2TV\5\4"+
		"\3\2UT\3\2\2\2UV\3\2\2\2VW\3\2\2\2WX\7\2\2\3X\3\3\2\2\2YZ\7\31\2\2Z[\7"+
		",\2\2[]\7\3\2\2\\^\5\b\5\2]\\\3\2\2\2]^\3\2\2\2^`\3\2\2\2_a\5\22\n\2`"+
		"_\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\5\6\4\2c\5\3\2\2\2de\7\32\2\2ef\5\32\16"+
		"\2f\7\3\2\2\2gi\7\33\2\2hj\5\n\6\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2"+
		"\2\2l\t\3\2\2\2mo\5R*\2np\5\f\7\2on\3\2\2\2pq\3\2\2\2qo\3\2\2\2qr\3\2"+
		"\2\2rs\3\2\2\2st\7\3\2\2t\13\3\2\2\2ux\5\16\b\2vw\7\4\2\2wy\5\f\7\2xv"+
		"\3\2\2\2xy\3\2\2\2y\r\3\2\2\2z|\7,\2\2{}\5\20\t\2|{\3\2\2\2|}\3\2\2\2"+
		"}\177\3\2\2\2~\u0080\5\20\t\2\177~\3\2\2\2\177\u0080\3\2\2\2\u0080\17"+
		"\3\2\2\2\u0081\u0082\7\5\2\2\u0082\u0083\7-\2\2\u0083\u0084\7\6\2\2\u0084"+
		"\21\3\2\2\2\u0085\u0087\5\24\13\2\u0086\u0085\3\2\2\2\u0087\u0088\3\2"+
		"\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\23\3\2\2\2\u008a\u008b"+
		"\7\34\2\2\u008b\u008c\5\26\f\2\u008c\u008d\7,\2\2\u008d\u008f\7\7\2\2"+
		"\u008e\u0090\5\30\r\2\u008f\u008e\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091"+
		"\3\2\2\2\u0091\u0092\7\b\2\2\u0092\u0094\7\3\2\2\u0093\u0095\5\b\5\2\u0094"+
		"\u0093\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\5\32"+
		"\16\2\u0097\25\3\2\2\2\u0098\u009b\7+\2\2\u0099\u009b\5R*\2\u009a\u0098"+
		"\3\2\2\2\u009a\u0099\3\2\2\2\u009b\27\3\2\2\2\u009c\u009d\5R*\2\u009d"+
		"\u00a0\7,\2\2\u009e\u009f\7\4\2\2\u009f\u00a1\5\30\r\2\u00a0\u009e\3\2"+
		"\2\2\u00a0\u00a1\3\2\2\2\u00a1\31\3\2\2\2\u00a2\u00a6\7\t\2\2\u00a3\u00a5"+
		"\5\34\17\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2"+
		"\u00a6\u00a7\3\2\2\2\u00a7\u00a9\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00aa"+
		"\7\n\2\2\u00aa\33\3\2\2\2\u00ab\u00b3\5\36\20\2\u00ac\u00b3\5$\23\2\u00ad"+
		"\u00b3\5&\24\2\u00ae\u00b3\5\60\31\2\u00af\u00b3\5\62\32\2\u00b0\u00b3"+
		"\5<\37\2\u00b1\u00b3\5*\26\2\u00b2\u00ab\3\2\2\2\u00b2\u00ac\3\2\2\2\u00b2"+
		"\u00ad\3\2\2\2\u00b2\u00ae\3\2\2\2\u00b2\u00af\3\2\2\2\u00b2\u00b0\3\2"+
		"\2\2\u00b2\u00b1\3\2\2\2\u00b3\35\3\2\2\2\u00b4\u00b5\5 \21\2\u00b5\u00b6"+
		"\7\13\2\2\u00b6\u00b7\5> \2\u00b7\u00b8\7\3\2\2\u00b8\37\3\2\2\2\u00b9"+
		"\u00bb\7,\2\2\u00ba\u00bc\5\"\22\2\u00bb\u00ba\3\2\2\2\u00bb\u00bc\3\2"+
		"\2\2\u00bc\u00be\3\2\2\2\u00bd\u00bf\5\"\22\2\u00be\u00bd\3\2\2\2\u00be"+
		"\u00bf\3\2\2\2\u00bf!\3\2\2\2\u00c0\u00c1\7\5\2\2\u00c1\u00c2\5> \2\u00c2"+
		"\u00c3\7\6\2\2\u00c3#\3\2\2\2\u00c4\u00c5\7\35\2\2\u00c5\u00c6\7\7\2\2"+
		"\u00c6\u00c7\5> \2\u00c7\u00c8\7\b\2\2\u00c8\u00c9\7\3\2\2\u00c9%\3\2"+
		"\2\2\u00ca\u00cb\7\36\2\2\u00cb\u00cc\7\7\2\2\u00cc\u00cd\5(\25\2\u00cd"+
		"\u00ce\7\b\2\2\u00ce\u00cf\7\3\2\2\u00cf\'\3\2\2\2\u00d0\u00d3\5 \21\2"+
		"\u00d1\u00d2\7\4\2\2\u00d2\u00d4\5(\25\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4"+
		"\3\2\2\2\u00d4)\3\2\2\2\u00d5\u00d6\7\37\2\2\u00d6\u00d7\7\7\2\2\u00d7"+
		"\u00d8\5,\27\2\u00d8\u00d9\7\b\2\2\u00d9\u00da\7\3\2\2\u00da+\3\2\2\2"+
		"\u00db\u00de\5.\30\2\u00dc\u00de\5> \2\u00dd\u00db\3\2\2\2\u00dd\u00dc"+
		"\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00e0\7\4\2\2\u00e0\u00e2\5,\27\2\u00e1"+
		"\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2-\3\2\2\2\u00e3\u00e4\7\60\2\2"+
		"\u00e4/\3\2\2\2\u00e5\u00e6\7 \2\2\u00e6\u00e7\7\7\2\2\u00e7\u00e8\5>"+
		" \2\u00e8\u00e9\7\b\2\2\u00e9\u00ea\7!\2\2\u00ea\u00ed\5\32\16\2\u00eb"+
		"\u00ec\7\"\2\2\u00ec\u00ee\5\32\16\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3"+
		"\2\2\2\u00ee\61\3\2\2\2\u00ef\u00f2\5\64\33\2\u00f0\u00f2\5\66\34\2\u00f1"+
		"\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2\63\3\2\2\2\u00f3\u00f4\7#\2\2"+
		"\u00f4\u00f5\5> \2\u00f5\u00f6\7$\2\2\u00f6\u00f7\5\32\16\2\u00f7\65\3"+
		"\2\2\2\u00f8\u00f9\7%\2\2\u00f9\u00fa\5 \21\2\u00fa\u00fb\7\13\2\2\u00fb"+
		"\u00fc\5> \2\u00fc\u00fd\7&\2\2\u00fd\u00fe\5> \2\u00fe\u00ff\7\'\2\2"+
		"\u00ff\u0100\5\32\16\2\u0100\67\3\2\2\2\u0101\u0102\7,\2\2\u0102\u0104"+
		"\7\7\2\2\u0103\u0105\5:\36\2\u0104\u0103\3\2\2\2\u0104\u0105\3\2\2\2\u0105"+
		"\u0106\3\2\2\2\u0106\u0107\7\b\2\2\u01079\3\2\2\2\u0108\u010b\5> \2\u0109"+
		"\u010a\7\4\2\2\u010a\u010c\5:\36\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2"+
		"\2\2\u010c;\3\2\2\2\u010d\u010e\58\35\2\u010e\u010f\7\3\2\2\u010f=\3\2"+
		"\2\2\u0110\u0111\b \1\2\u0111\u0117\5D#\2\u0112\u0113\5D#\2\u0113\u0114"+
		"\5B\"\2\u0114\u0115\5D#\2\u0115\u0117\3\2\2\2\u0116\u0110\3\2\2\2\u0116"+
		"\u0112\3\2\2\2\u0117\u011e\3\2\2\2\u0118\u0119\f\4\2\2\u0119\u011a\5@"+
		"!\2\u011a\u011b\5> \5\u011b\u011d\3\2\2\2\u011c\u0118\3\2\2\2\u011d\u0120"+
		"\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f?\3\2\2\2\u0120"+
		"\u011e\3\2\2\2\u0121\u0122\t\2\2\2\u0122A\3\2\2\2\u0123\u0124\t\3\2\2"+
		"\u0124C\3\2\2\2\u0125\u012b\5H%\2\u0126\u0127\5H%\2\u0127\u0128\5F$\2"+
		"\u0128\u0129\5D#\2\u0129\u012b\3\2\2\2\u012a\u0125\3\2\2\2\u012a\u0126"+
		"\3\2\2\2\u012bE\3\2\2\2\u012c\u012d\t\4\2\2\u012dG\3\2\2\2\u012e\u0134"+
		"\5L\'\2\u012f\u0130\5L\'\2\u0130\u0131\5J&\2\u0131\u0132\5H%\2\u0132\u0134"+
		"\3\2\2\2\u0133\u012e\3\2\2\2\u0133\u012f\3\2\2\2\u0134I\3\2\2\2\u0135"+
		"\u0136\t\5\2\2\u0136K\3\2\2\2\u0137\u0139\5 \21\2\u0138\u013a\5P)\2\u0139"+
		"\u0138\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u0145\3\2\2\2\u013b\u013d\5F"+
		"$\2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\3\2\2\2\u013e"+
		"\u0145\5N(\2\u013f\u0145\58\35\2\u0140\u0141\7\7\2\2\u0141\u0142\5> \2"+
		"\u0142\u0143\7\b\2\2\u0143\u0145\3\2\2\2\u0144\u0137\3\2\2\2\u0144\u013c"+
		"\3\2\2\2\u0144\u013f\3\2\2\2\u0144\u0140\3\2\2\2\u0145M\3\2\2\2\u0146"+
		"\u014a\5 \21\2\u0147\u014a\7-\2\2\u0148\u014a\7.\2\2\u0149\u0146\3\2\2"+
		"\2\u0149\u0147\3\2\2\2\u0149\u0148\3\2\2\2\u014aO\3\2\2\2\u014b\u014c"+
		"\t\6\2\2\u014cQ\3\2\2\2\u014d\u014e\t\7\2\2\u014eS\3\2\2\2\"U]`kqx|\177"+
		"\u0088\u008f\u0094\u009a\u00a0\u00a6\u00b2\u00bb\u00be\u00d3\u00dd\u00e1"+
		"\u00ed\u00f1\u0104\u010b\u0116\u011e\u012a\u0133\u0139\u013c\u0144\u0149";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
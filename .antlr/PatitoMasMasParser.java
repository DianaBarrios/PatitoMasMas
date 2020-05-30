// Generated from /Users/alberto/Documents/PatitoMasMas/PatitoMasMas.g4 by ANTLR 4.7.1
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
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, Programa=20, Principal=21, Var=22, Function=23, Regresa=24, 
		Lee=25, Escribe=26, Si=27, Entonces=28, Sino=29, Mientras=30, Haz=31, 
		Desde=32, Hasta=33, Hacer=34, Int=35, Float=36, Char=37, Void=38, ESP=39, 
		ID=40, CTE_INT=41, CTE_FLOAT=42, CTE_CHAR=43, CTE_STRING=44, DIGIT=45, 
		Whitespace=46, Newline=47;
	public static final int
		RULE_start = 0, RULE_programa = 1, RULE_principal = 2, RULE_dec_variables = 3, 
		RULE_dec_var = 4, RULE_lista_ids = 5, RULE_ids = 6, RULE_dimension = 7, 
		RULE_dec_functions = 8, RULE_funcion = 9, RULE_tipo_ret = 10, RULE_params = 11, 
		RULE_bloque_est = 12, RULE_estatuto = 13, RULE_asignacion_est = 14, RULE_asignacion = 15, 
		RULE_var = 16, RULE_dim = 17, RULE_retorno = 18, RULE_lectura = 19, RULE_lista_vars = 20, 
		RULE_escritura = 21, RULE_escrituras = 22, RULE_string = 23, RULE_decision = 24, 
		RULE_repeticion = 25, RULE_condicional = 26, RULE_no_condicional = 27, 
		RULE_llamada = 28, RULE_params_llamada = 29, RULE_llamada_est = 30, RULE_expresion = 31, 
		RULE_op_log = 32, RULE_op_comp = 33, RULE_exp = 34, RULE_op_arit = 35, 
		RULE_term = 36, RULE_op_prod = 37, RULE_factor = 38, RULE_exp_par = 39, 
		RULE_par_empieza = 40, RULE_par_termina = 41, RULE_var_cte = 42, RULE_op_esp = 43, 
		RULE_tipo = 44;
	public static final String[] ruleNames = {
		"start", "programa", "principal", "dec_variables", "dec_var", "lista_ids", 
		"ids", "dimension", "dec_functions", "funcion", "tipo_ret", "params", 
		"bloque_est", "estatuto", "asignacion_est", "asignacion", "var", "dim", 
		"retorno", "lectura", "lista_vars", "escritura", "escrituras", "string", 
		"decision", "repeticion", "condicional", "no_condicional", "llamada", 
		"params_llamada", "llamada_est", "expresion", "op_log", "op_comp", "exp", 
		"op_arit", "term", "op_prod", "factor", "exp_par", "par_empieza", "par_termina", 
		"var_cte", "op_esp", "tipo"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "';'", "','", "'['", "']'", "'('", "')'", "'{'", "'}'", "'='", "'&'", 
		"'||'", "'>'", "'<'", "'=='", "'!='", "'+'", "'-'", "'*'", "'/'", "'programa'", 
		"'principal()'", "'var'", "'funcion'", "'regresa'", "'lee'", "'escribe'", 
		"'si'", "'entonces'", "'sino'", "'mientras'", "'haz'", "'desde'", "'hasta'", 
		"'hacer'", "'int'", "'float'", "'char'", "'void'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, "Programa", "Principal", 
		"Var", "Function", "Regresa", "Lee", "Escribe", "Si", "Entonces", "Sino", 
		"Mientras", "Haz", "Desde", "Hasta", "Hacer", "Int", "Float", "Char", 
		"Void", "ESP", "ID", "CTE_INT", "CTE_FLOAT", "CTE_CHAR", "CTE_STRING", 
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
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Programa) {
				{
				setState(90);
				programa();
				}
			}

			setState(93);
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
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(Programa);
			setState(96);
			match(ID);
			setState(97);
			match(T__0);
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Var) {
				{
				setState(98);
				dec_variables();
				}
			}

			setState(102);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Function) {
				{
				setState(101);
				dec_functions();
				}
			}

			setState(104);
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
	}

	public final PrincipalContext principal() throws RecognitionException {
		PrincipalContext _localctx = new PrincipalContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_principal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(Principal);
			setState(107);
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
	}

	public final Dec_variablesContext dec_variables() throws RecognitionException {
		Dec_variablesContext _localctx = new Dec_variablesContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_dec_variables);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			match(Var);
			setState(111); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(110);
				dec_var();
				}
				}
				setState(113); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Int) | (1L << Float) | (1L << Char))) != 0) );
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
	}

	public final Dec_varContext dec_var() throws RecognitionException {
		Dec_varContext _localctx = new Dec_varContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_dec_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			tipo();
			setState(117); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(116);
				lista_ids();
				}
				}
				setState(119); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			setState(121);
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
	}

	public final Lista_idsContext lista_ids() throws RecognitionException {
		Lista_idsContext _localctx = new Lista_idsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_lista_ids);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			ids();
			setState(126);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(124);
				match(T__1);
				setState(125);
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
	}

	public final IdsContext ids() throws RecognitionException {
		IdsContext _localctx = new IdsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_ids);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(ID);
			setState(130);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(129);
				dimension();
				}
				break;
			}
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2) {
				{
				setState(132);
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
	}

	public final DimensionContext dimension() throws RecognitionException {
		DimensionContext _localctx = new DimensionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_dimension);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			match(T__2);
			setState(136);
			match(CTE_INT);
			setState(137);
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
	}

	public final Dec_functionsContext dec_functions() throws RecognitionException {
		Dec_functionsContext _localctx = new Dec_functionsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_dec_functions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(139);
				funcion();
				}
				}
				setState(142); 
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
	}

	public final FuncionContext funcion() throws RecognitionException {
		FuncionContext _localctx = new FuncionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_funcion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			match(Function);
			setState(145);
			tipo_ret();
			setState(146);
			match(ID);
			setState(147);
			match(T__4);
			setState(149);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Int) | (1L << Float) | (1L << Char))) != 0)) {
				{
				setState(148);
				params();
				}
			}

			setState(151);
			match(T__5);
			setState(152);
			match(T__0);
			setState(154);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Var) {
				{
				setState(153);
				dec_variables();
				}
			}

			setState(156);
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
	}

	public final Tipo_retContext tipo_ret() throws RecognitionException {
		Tipo_retContext _localctx = new Tipo_retContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_tipo_ret);
		try {
			setState(160);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Void:
				enterOuterAlt(_localctx, 1);
				{
				setState(158);
				match(Void);
				}
				break;
			case Int:
			case Float:
			case Char:
				enterOuterAlt(_localctx, 2);
				{
				setState(159);
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
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			tipo();
			setState(163);
			match(ID);
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(164);
				match(T__1);
				setState(165);
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
	}

	public final Bloque_estContext bloque_est() throws RecognitionException {
		Bloque_estContext _localctx = new Bloque_estContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_bloque_est);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			match(T__6);
			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Regresa) | (1L << Lee) | (1L << Escribe) | (1L << Si) | (1L << Mientras) | (1L << Desde) | (1L << ID))) != 0)) {
				{
				{
				setState(169);
				estatuto();
				}
				}
				setState(174);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(175);
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
		public Asignacion_estContext asignacion_est() {
			return getRuleContext(Asignacion_estContext.class,0);
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
	}

	public final EstatutoContext estatuto() throws RecognitionException {
		EstatutoContext _localctx = new EstatutoContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_estatuto);
		try {
			setState(184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(177);
				asignacion_est();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(178);
				retorno();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(179);
				lectura();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(180);
				decision();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(181);
				repeticion();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(182);
				llamada_est();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(183);
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

	public static class Asignacion_estContext extends ParserRuleContext {
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public Asignacion_estContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion_est; }
	}

	public final Asignacion_estContext asignacion_est() throws RecognitionException {
		Asignacion_estContext _localctx = new Asignacion_estContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_asignacion_est);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			asignacion();
			setState(187);
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

	public static class AsignacionContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public List<VarContext> var() {
			return getRuleContexts(VarContext.class);
		}
		public VarContext var(int i) {
			return getRuleContext(VarContext.class,i);
		}
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_asignacion);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(192); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(189);
					var();
					setState(190);
					match(T__8);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(194); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(196);
			expresion(0);
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
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			match(ID);
			setState(200);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				setState(199);
				dim();
				}
				break;
			}
			setState(203);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				setState(202);
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
	}

	public final DimContext dim() throws RecognitionException {
		DimContext _localctx = new DimContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_dim);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			match(T__2);
			setState(206);
			expresion(0);
			setState(207);
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
	}

	public final RetornoContext retorno() throws RecognitionException {
		RetornoContext _localctx = new RetornoContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_retorno);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			match(Regresa);
			setState(210);
			match(T__4);
			setState(211);
			expresion(0);
			setState(212);
			match(T__5);
			setState(213);
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
	}

	public final LecturaContext lectura() throws RecognitionException {
		LecturaContext _localctx = new LecturaContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_lectura);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(215);
			match(Lee);
			setState(216);
			match(T__4);
			setState(217);
			lista_vars();
			setState(218);
			match(T__5);
			setState(219);
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
	}

	public final Lista_varsContext lista_vars() throws RecognitionException {
		Lista_varsContext _localctx = new Lista_varsContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_lista_vars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			var();
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(222);
				match(T__1);
				setState(223);
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
	}

	public final EscrituraContext escritura() throws RecognitionException {
		EscrituraContext _localctx = new EscrituraContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_escritura);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			match(Escribe);
			setState(227);
			match(T__4);
			setState(228);
			escrituras();
			setState(229);
			match(T__5);
			setState(230);
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
	}

	public final EscriturasContext escrituras() throws RecognitionException {
		EscriturasContext _localctx = new EscriturasContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_escrituras);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CTE_STRING:
				{
				setState(232);
				string();
				}
				break;
			case T__4:
			case T__15:
			case T__16:
			case ID:
			case CTE_INT:
			case CTE_FLOAT:
			case CTE_CHAR:
				{
				setState(233);
				expresion(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(238);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(236);
				match(T__1);
				setState(237);
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
	}

	public final StringContext string() throws RecognitionException {
		StringContext _localctx = new StringContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_string);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(240);
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
	}

	public final DecisionContext decision() throws RecognitionException {
		DecisionContext _localctx = new DecisionContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_decision);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			match(Si);
			setState(243);
			match(T__4);
			setState(244);
			expresion(0);
			setState(245);
			match(T__5);
			setState(246);
			match(Entonces);
			setState(247);
			bloque_est();
			setState(250);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Sino) {
				{
				setState(248);
				match(Sino);
				setState(249);
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
	}

	public final RepeticionContext repeticion() throws RecognitionException {
		RepeticionContext _localctx = new RepeticionContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_repeticion);
		try {
			setState(254);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Mientras:
				enterOuterAlt(_localctx, 1);
				{
				setState(252);
				condicional();
				}
				break;
			case Desde:
				enterOuterAlt(_localctx, 2);
				{
				setState(253);
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
	}

	public final CondicionalContext condicional() throws RecognitionException {
		CondicionalContext _localctx = new CondicionalContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_condicional);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(256);
			match(Mientras);
			setState(257);
			expresion(0);
			setState(258);
			match(Haz);
			setState(259);
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
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public TerminalNode Hasta() { return getToken(PatitoMasMasParser.Hasta, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode Hacer() { return getToken(PatitoMasMasParser.Hacer, 0); }
		public Bloque_estContext bloque_est() {
			return getRuleContext(Bloque_estContext.class,0);
		}
		public No_condicionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_no_condicional; }
	}

	public final No_condicionalContext no_condicional() throws RecognitionException {
		No_condicionalContext _localctx = new No_condicionalContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_no_condicional);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(261);
			match(Desde);
			setState(262);
			asignacion();
			setState(263);
			match(Hasta);
			setState(264);
			expresion(0);
			setState(265);
			match(Hacer);
			setState(266);
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
	}

	public final LlamadaContext llamada() throws RecognitionException {
		LlamadaContext _localctx = new LlamadaContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_llamada);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			match(ID);
			setState(269);
			match(T__4);
			setState(271);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__4) | (1L << T__15) | (1L << T__16) | (1L << ID) | (1L << CTE_INT) | (1L << CTE_FLOAT) | (1L << CTE_CHAR))) != 0)) {
				{
				setState(270);
				params_llamada();
				}
			}

			setState(273);
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
	}

	public final Params_llamadaContext params_llamada() throws RecognitionException {
		Params_llamadaContext _localctx = new Params_llamadaContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_params_llamada);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(275);
			expresion(0);
			setState(278);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(276);
				match(T__1);
				setState(277);
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
	}

	public final Llamada_estContext llamada_est() throws RecognitionException {
		Llamada_estContext _localctx = new Llamada_estContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_llamada_est);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(280);
			llamada();
			setState(281);
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
	}

	public final ExpresionContext expresion() throws RecognitionException {
		return expresion(0);
	}

	private ExpresionContext expresion(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpresionContext _localctx = new ExpresionContext(_ctx, _parentState);
		ExpresionContext _prevctx = _localctx;
		int _startState = 62;
		enterRecursionRule(_localctx, 62, RULE_expresion, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(289);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				{
				setState(284);
				exp();
				}
				break;
			case 2:
				{
				setState(285);
				exp();
				setState(286);
				op_comp();
				setState(287);
				exp();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(297);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpresionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expresion);
					setState(291);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(292);
					op_log();
					setState(293);
					expresion(3);
					}
					} 
				}
				setState(299);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
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
	}

	public final Op_logContext op_log() throws RecognitionException {
		Op_logContext _localctx = new Op_logContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_op_log);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(300);
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
	}

	public final Op_compContext op_comp() throws RecognitionException {
		Op_compContext _localctx = new Op_compContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_op_comp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(302);
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
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_exp);
		try {
			setState(309);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(304);
				term();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(305);
				term();
				setState(306);
				op_arit();
				setState(307);
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
	}

	public final Op_aritContext op_arit() throws RecognitionException {
		Op_aritContext _localctx = new Op_aritContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_op_arit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(311);
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
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_term);
		try {
			setState(318);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(313);
				factor();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(314);
				factor();
				setState(315);
				op_prod();
				setState(316);
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
	}

	public final Op_prodContext op_prod() throws RecognitionException {
		Op_prodContext _localctx = new Op_prodContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_op_prod);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(320);
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
		public Exp_parContext exp_par() {
			return getRuleContext(Exp_parContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_factor);
		int _la;
		try {
			setState(332);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(322);
				var();
				setState(324);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
				case 1:
					{
					setState(323);
					op_esp();
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(327);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__15 || _la==T__16) {
					{
					setState(326);
					op_arit();
					}
				}

				setState(329);
				var_cte();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(330);
				llamada();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(331);
				exp_par();
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

	public static class Exp_parContext extends ParserRuleContext {
		public Par_empiezaContext par_empieza() {
			return getRuleContext(Par_empiezaContext.class,0);
		}
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public Par_terminaContext par_termina() {
			return getRuleContext(Par_terminaContext.class,0);
		}
		public Exp_parContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_par; }
	}

	public final Exp_parContext exp_par() throws RecognitionException {
		Exp_parContext _localctx = new Exp_parContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_exp_par);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(334);
			par_empieza();
			setState(335);
			expresion(0);
			setState(336);
			par_termina();
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

	public static class Par_empiezaContext extends ParserRuleContext {
		public Par_empiezaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_par_empieza; }
	}

	public final Par_empiezaContext par_empieza() throws RecognitionException {
		Par_empiezaContext _localctx = new Par_empiezaContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_par_empieza);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(338);
			match(T__4);
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

	public static class Par_terminaContext extends ParserRuleContext {
		public Par_terminaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_par_termina; }
	}

	public final Par_terminaContext par_termina() throws RecognitionException {
		Par_terminaContext _localctx = new Par_terminaContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_par_termina);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(340);
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

	public static class Var_cteContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public TerminalNode CTE_INT() { return getToken(PatitoMasMasParser.CTE_INT, 0); }
		public TerminalNode CTE_FLOAT() { return getToken(PatitoMasMasParser.CTE_FLOAT, 0); }
		public TerminalNode CTE_CHAR() { return getToken(PatitoMasMasParser.CTE_CHAR, 0); }
		public Var_cteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_cte; }
	}

	public final Var_cteContext var_cte() throws RecognitionException {
		Var_cteContext _localctx = new Var_cteContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_var_cte);
		try {
			setState(346);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(342);
				var();
				}
				break;
			case CTE_INT:
				enterOuterAlt(_localctx, 2);
				{
				setState(343);
				match(CTE_INT);
				}
				break;
			case CTE_FLOAT:
				enterOuterAlt(_localctx, 3);
				{
				setState(344);
				match(CTE_FLOAT);
				}
				break;
			case CTE_CHAR:
				enterOuterAlt(_localctx, 4);
				{
				setState(345);
				match(CTE_CHAR);
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
		public TerminalNode ESP() { return getToken(PatitoMasMasParser.ESP, 0); }
		public Op_espContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op_esp; }
	}

	public final Op_espContext op_esp() throws RecognitionException {
		Op_espContext _localctx = new Op_espContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_op_esp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(348);
			match(ESP);
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
		public TerminalNode Char() { return getToken(PatitoMasMasParser.Char, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(350);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Int) | (1L << Float) | (1L << Char))) != 0)) ) {
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
		case 31:
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61\u0163\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\3\2\5\2^\n\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3f\n\3\3\3\5\3"+
		"i\n\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\6\5r\n\5\r\5\16\5s\3\6\3\6\6\6x\n\6"+
		"\r\6\16\6y\3\6\3\6\3\7\3\7\3\7\5\7\u0081\n\7\3\b\3\b\5\b\u0085\n\b\3\b"+
		"\5\b\u0088\n\b\3\t\3\t\3\t\3\t\3\n\6\n\u008f\n\n\r\n\16\n\u0090\3\13\3"+
		"\13\3\13\3\13\3\13\5\13\u0098\n\13\3\13\3\13\3\13\5\13\u009d\n\13\3\13"+
		"\3\13\3\f\3\f\5\f\u00a3\n\f\3\r\3\r\3\r\3\r\5\r\u00a9\n\r\3\16\3\16\7"+
		"\16\u00ad\n\16\f\16\16\16\u00b0\13\16\3\16\3\16\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\5\17\u00bb\n\17\3\20\3\20\3\20\3\21\3\21\3\21\6\21\u00c3"+
		"\n\21\r\21\16\21\u00c4\3\21\3\21\3\22\3\22\5\22\u00cb\n\22\3\22\5\22\u00ce"+
		"\n\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\3\26\3\26\3\26\5\26\u00e3\n\26\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\30\3\30\5\30\u00ed\n\30\3\30\3\30\5\30\u00f1\n\30\3\31\3\31\3"+
		"\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u00fd\n\32\3\33\3\33\5\33"+
		"\u0101\n\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35"+
		"\3\36\3\36\3\36\5\36\u0112\n\36\3\36\3\36\3\37\3\37\3\37\5\37\u0119\n"+
		"\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\5!\u0124\n!\3!\3!\3!\3!\7!\u012a\n!\f!"+
		"\16!\u012d\13!\3\"\3\"\3#\3#\3$\3$\3$\3$\3$\5$\u0138\n$\3%\3%\3&\3&\3"+
		"&\3&\3&\5&\u0141\n&\3\'\3\'\3(\3(\5(\u0147\n(\3(\5(\u014a\n(\3(\3(\3("+
		"\5(\u014f\n(\3)\3)\3)\3)\3*\3*\3+\3+\3,\3,\3,\3,\5,\u015d\n,\3-\3-\3."+
		"\3.\3.\2\3@/\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64"+
		"\668:<>@BDFHJLNPRTVXZ\2\7\3\2\f\r\3\2\16\21\3\2\22\23\3\2\24\25\3\2%\'"+
		"\2\u015f\2]\3\2\2\2\4a\3\2\2\2\6l\3\2\2\2\bo\3\2\2\2\nu\3\2\2\2\f}\3\2"+
		"\2\2\16\u0082\3\2\2\2\20\u0089\3\2\2\2\22\u008e\3\2\2\2\24\u0092\3\2\2"+
		"\2\26\u00a2\3\2\2\2\30\u00a4\3\2\2\2\32\u00aa\3\2\2\2\34\u00ba\3\2\2\2"+
		"\36\u00bc\3\2\2\2 \u00c2\3\2\2\2\"\u00c8\3\2\2\2$\u00cf\3\2\2\2&\u00d3"+
		"\3\2\2\2(\u00d9\3\2\2\2*\u00df\3\2\2\2,\u00e4\3\2\2\2.\u00ec\3\2\2\2\60"+
		"\u00f2\3\2\2\2\62\u00f4\3\2\2\2\64\u0100\3\2\2\2\66\u0102\3\2\2\28\u0107"+
		"\3\2\2\2:\u010e\3\2\2\2<\u0115\3\2\2\2>\u011a\3\2\2\2@\u0123\3\2\2\2B"+
		"\u012e\3\2\2\2D\u0130\3\2\2\2F\u0137\3\2\2\2H\u0139\3\2\2\2J\u0140\3\2"+
		"\2\2L\u0142\3\2\2\2N\u014e\3\2\2\2P\u0150\3\2\2\2R\u0154\3\2\2\2T\u0156"+
		"\3\2\2\2V\u015c\3\2\2\2X\u015e\3\2\2\2Z\u0160\3\2\2\2\\^\5\4\3\2]\\\3"+
		"\2\2\2]^\3\2\2\2^_\3\2\2\2_`\7\2\2\3`\3\3\2\2\2ab\7\26\2\2bc\7*\2\2ce"+
		"\7\3\2\2df\5\b\5\2ed\3\2\2\2ef\3\2\2\2fh\3\2\2\2gi\5\22\n\2hg\3\2\2\2"+
		"hi\3\2\2\2ij\3\2\2\2jk\5\6\4\2k\5\3\2\2\2lm\7\27\2\2mn\5\32\16\2n\7\3"+
		"\2\2\2oq\7\30\2\2pr\5\n\6\2qp\3\2\2\2rs\3\2\2\2sq\3\2\2\2st\3\2\2\2t\t"+
		"\3\2\2\2uw\5Z.\2vx\5\f\7\2wv\3\2\2\2xy\3\2\2\2yw\3\2\2\2yz\3\2\2\2z{\3"+
		"\2\2\2{|\7\3\2\2|\13\3\2\2\2}\u0080\5\16\b\2~\177\7\4\2\2\177\u0081\5"+
		"\f\7\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\r\3\2\2\2\u0082\u0084"+
		"\7*\2\2\u0083\u0085\5\20\t\2\u0084\u0083\3\2\2\2\u0084\u0085\3\2\2\2\u0085"+
		"\u0087\3\2\2\2\u0086\u0088\5\20\t\2\u0087\u0086\3\2\2\2\u0087\u0088\3"+
		"\2\2\2\u0088\17\3\2\2\2\u0089\u008a\7\5\2\2\u008a\u008b\7+\2\2\u008b\u008c"+
		"\7\6\2\2\u008c\21\3\2\2\2\u008d\u008f\5\24\13\2\u008e\u008d\3\2\2\2\u008f"+
		"\u0090\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\23\3\2\2"+
		"\2\u0092\u0093\7\31\2\2\u0093\u0094\5\26\f\2\u0094\u0095\7*\2\2\u0095"+
		"\u0097\7\7\2\2\u0096\u0098\5\30\r\2\u0097\u0096\3\2\2\2\u0097\u0098\3"+
		"\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\7\b\2\2\u009a\u009c\7\3\2\2\u009b"+
		"\u009d\5\b\5\2\u009c\u009b\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\3\2"+
		"\2\2\u009e\u009f\5\32\16\2\u009f\25\3\2\2\2\u00a0\u00a3\7(\2\2\u00a1\u00a3"+
		"\5Z.\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\27\3\2\2\2\u00a4"+
		"\u00a5\5Z.\2\u00a5\u00a8\7*\2\2\u00a6\u00a7\7\4\2\2\u00a7\u00a9\5\30\r"+
		"\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\31\3\2\2\2\u00aa\u00ae"+
		"\7\t\2\2\u00ab\u00ad\5\34\17\2\u00ac\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2"+
		"\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00ae"+
		"\3\2\2\2\u00b1\u00b2\7\n\2\2\u00b2\33\3\2\2\2\u00b3\u00bb\5\36\20\2\u00b4"+
		"\u00bb\5&\24\2\u00b5\u00bb\5(\25\2\u00b6\u00bb\5\62\32\2\u00b7\u00bb\5"+
		"\64\33\2\u00b8\u00bb\5> \2\u00b9\u00bb\5,\27\2\u00ba\u00b3\3\2\2\2\u00ba"+
		"\u00b4\3\2\2\2\u00ba\u00b5\3\2\2\2\u00ba\u00b6\3\2\2\2\u00ba\u00b7\3\2"+
		"\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\35\3\2\2\2\u00bc\u00bd"+
		"\5 \21\2\u00bd\u00be\7\3\2\2\u00be\37\3\2\2\2\u00bf\u00c0\5\"\22\2\u00c0"+
		"\u00c1\7\13\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00bf\3\2\2\2\u00c3\u00c4\3"+
		"\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6"+
		"\u00c7\5@!\2\u00c7!\3\2\2\2\u00c8\u00ca\7*\2\2\u00c9\u00cb\5$\23\2\u00ca"+
		"\u00c9\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00ce\5$"+
		"\23\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce#\3\2\2\2\u00cf\u00d0"+
		"\7\5\2\2\u00d0\u00d1\5@!\2\u00d1\u00d2\7\6\2\2\u00d2%\3\2\2\2\u00d3\u00d4"+
		"\7\32\2\2\u00d4\u00d5\7\7\2\2\u00d5\u00d6\5@!\2\u00d6\u00d7\7\b\2\2\u00d7"+
		"\u00d8\7\3\2\2\u00d8\'\3\2\2\2\u00d9\u00da\7\33\2\2\u00da\u00db\7\7\2"+
		"\2\u00db\u00dc\5*\26\2\u00dc\u00dd\7\b\2\2\u00dd\u00de\7\3\2\2\u00de)"+
		"\3\2\2\2\u00df\u00e2\5\"\22\2\u00e0\u00e1\7\4\2\2\u00e1\u00e3\5*\26\2"+
		"\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3+\3\2\2\2\u00e4\u00e5\7"+
		"\34\2\2\u00e5\u00e6\7\7\2\2\u00e6\u00e7\5.\30\2\u00e7\u00e8\7\b\2\2\u00e8"+
		"\u00e9\7\3\2\2\u00e9-\3\2\2\2\u00ea\u00ed\5\60\31\2\u00eb\u00ed\5@!\2"+
		"\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ef"+
		"\7\4\2\2\u00ef\u00f1\5.\30\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1"+
		"/\3\2\2\2\u00f2\u00f3\7.\2\2\u00f3\61\3\2\2\2\u00f4\u00f5\7\35\2\2\u00f5"+
		"\u00f6\7\7\2\2\u00f6\u00f7\5@!\2\u00f7\u00f8\7\b\2\2\u00f8\u00f9\7\36"+
		"\2\2\u00f9\u00fc\5\32\16\2\u00fa\u00fb\7\37\2\2\u00fb\u00fd\5\32\16\2"+
		"\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\63\3\2\2\2\u00fe\u0101"+
		"\5\66\34\2\u00ff\u0101\58\35\2\u0100\u00fe\3\2\2\2\u0100\u00ff\3\2\2\2"+
		"\u0101\65\3\2\2\2\u0102\u0103\7 \2\2\u0103\u0104\5@!\2\u0104\u0105\7!"+
		"\2\2\u0105\u0106\5\32\16\2\u0106\67\3\2\2\2\u0107\u0108\7\"\2\2\u0108"+
		"\u0109\5 \21\2\u0109\u010a\7#\2\2\u010a\u010b\5@!\2\u010b\u010c\7$\2\2"+
		"\u010c\u010d\5\32\16\2\u010d9\3\2\2\2\u010e\u010f\7*\2\2\u010f\u0111\7"+
		"\7\2\2\u0110\u0112\5<\37\2\u0111\u0110\3\2\2\2\u0111\u0112\3\2\2\2\u0112"+
		"\u0113\3\2\2\2\u0113\u0114\7\b\2\2\u0114;\3\2\2\2\u0115\u0118\5@!\2\u0116"+
		"\u0117\7\4\2\2\u0117\u0119\5<\37\2\u0118\u0116\3\2\2\2\u0118\u0119\3\2"+
		"\2\2\u0119=\3\2\2\2\u011a\u011b\5:\36\2\u011b\u011c\7\3\2\2\u011c?\3\2"+
		"\2\2\u011d\u011e\b!\1\2\u011e\u0124\5F$\2\u011f\u0120\5F$\2\u0120\u0121"+
		"\5D#\2\u0121\u0122\5F$\2\u0122\u0124\3\2\2\2\u0123\u011d\3\2\2\2\u0123"+
		"\u011f\3\2\2\2\u0124\u012b\3\2\2\2\u0125\u0126\f\4\2\2\u0126\u0127\5B"+
		"\"\2\u0127\u0128\5@!\5\u0128\u012a\3\2\2\2\u0129\u0125\3\2\2\2\u012a\u012d"+
		"\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012cA\3\2\2\2\u012d"+
		"\u012b\3\2\2\2\u012e\u012f\t\2\2\2\u012fC\3\2\2\2\u0130\u0131\t\3\2\2"+
		"\u0131E\3\2\2\2\u0132\u0138\5J&\2\u0133\u0134\5J&\2\u0134\u0135\5H%\2"+
		"\u0135\u0136\5F$\2\u0136\u0138\3\2\2\2\u0137\u0132\3\2\2\2\u0137\u0133"+
		"\3\2\2\2\u0138G\3\2\2\2\u0139\u013a\t\4\2\2\u013aI\3\2\2\2\u013b\u0141"+
		"\5N(\2\u013c\u013d\5N(\2\u013d\u013e\5L\'\2\u013e\u013f\5J&\2\u013f\u0141"+
		"\3\2\2\2\u0140\u013b\3\2\2\2\u0140\u013c\3\2\2\2\u0141K\3\2\2\2\u0142"+
		"\u0143\t\5\2\2\u0143M\3\2\2\2\u0144\u0146\5\"\22\2\u0145\u0147\5X-\2\u0146"+
		"\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u014f\3\2\2\2\u0148\u014a\5H"+
		"%\2\u0149\u0148\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b\3\2\2\2\u014b"+
		"\u014f\5V,\2\u014c\u014f\5:\36\2\u014d\u014f\5P)\2\u014e\u0144\3\2\2\2"+
		"\u014e\u0149\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014fO\3"+
		"\2\2\2\u0150\u0151\5R*\2\u0151\u0152\5@!\2\u0152\u0153\5T+\2\u0153Q\3"+
		"\2\2\2\u0154\u0155\7\7\2\2\u0155S\3\2\2\2\u0156\u0157\7\b\2\2\u0157U\3"+
		"\2\2\2\u0158\u015d\5\"\22\2\u0159\u015d\7+\2\2\u015a\u015d\7,\2\2\u015b"+
		"\u015d\7-\2\2\u015c\u0158\3\2\2\2\u015c\u0159\3\2\2\2\u015c\u015a\3\2"+
		"\2\2\u015c\u015b\3\2\2\2\u015dW\3\2\2\2\u015e\u015f\7)\2\2\u015fY\3\2"+
		"\2\2\u0160\u0161\t\6\2\2\u0161[\3\2\2\2#]ehsy\u0080\u0084\u0087\u0090"+
		"\u0097\u009c\u00a2\u00a8\u00ae\u00ba\u00c4\u00ca\u00cd\u00e2\u00ec\u00f0"+
		"\u00fc\u0100\u0111\u0118\u0123\u012b\u0137\u0140\u0146\u0149\u014e\u015c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
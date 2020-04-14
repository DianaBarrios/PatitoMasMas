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
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, Programa=24, 
		Principal=25, Var=26, Function=27, Regresa=28, Lee=29, Escribe=30, Si=31, 
		Entonces=32, Sino=33, Mientras=34, Haz=35, Desde=36, Hasta=37, Hacer=38, 
		Nombre=39, Int=40, Float=41, Char=42, Void=43, DIGIT=44, ID=45, CTE_INT=46, 
		CTE_FLOAT=47, CTE_CHAR=48, CTE_STRING=49, Whitespace=50, Newline=51;
	public static final int
		RULE_start = 0, RULE_programa = 1, RULE_principal = 2, RULE_variables = 3, 
		RULE_var = 4, RULE_ids = 5, RULE_id_cte = 6, RULE_functions = 7, RULE_tipo_ret = 8, 
		RULE_params = 9, RULE_bloque_est = 10, RULE_estatutos = 11, RULE_estatuto = 12, 
		RULE_asignacion = 13, RULE_id_expressions = 14, RULE_id_exp = 15, RULE_retorno = 16, 
		RULE_lectura = 17, RULE_escritura = 18, RULE_escrituras = 19, RULE_decision = 20, 
		RULE_repeticion = 21, RULE_condicional = 22, RULE_no_condicional = 23, 
		RULE_llamada = 24, RULE_llamada_est = 25, RULE_op_esp = 26, RULE_expresion = 27, 
		RULE_exp_a = 28, RULE_exp_b = 29, RULE_exp_c = 30, RULE_exp_d = 31, RULE_exp_e = 32, 
		RULE_tipo = 33, RULE_var_cte = 34;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "programa", "principal", "variables", "var", "ids", "id_cte", 
			"functions", "tipo_ret", "params", "bloque_est", "estatutos", "estatuto", 
			"asignacion", "id_expressions", "id_exp", "retorno", "lectura", "escritura", 
			"escrituras", "decision", "repeticion", "condicional", "no_condicional", 
			"llamada", "llamada_est", "op_esp", "expresion", "exp_a", "exp_b", "exp_c", 
			"exp_d", "exp_e", "tipo", "var_cte"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "':'", "','", "'['", "']'", "'('", "')'", "'{'", "'}'", 
			"'='", "'$'", "'?'", "'\u00A1'", "'||'", "'&'", "'>'", "'<'", "'=='", 
			"'!='", "'+'", "'-'", "'*'", "'/'", "'programa'", "'principal()'", "'var'", 
			"'function'", "'regresa'", "'lee'", "'escribe'", "'si'", "'entonces'", 
			"'sino'", "'mientras'", "'haz'", "'desde'", "'hasta'", "'hacer'", "'nombre'", 
			"'int'", "'float'", "'char'", "'void'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"Programa", "Principal", "Var", "Function", "Regresa", "Lee", "Escribe", 
			"Si", "Entonces", "Sino", "Mientras", "Haz", "Desde", "Hasta", "Hacer", 
			"Nombre", "Int", "Float", "Char", "Void", "DIGIT", "ID", "CTE_INT", "CTE_FLOAT", 
			"CTE_CHAR", "CTE_STRING", "Whitespace", "Newline"
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
			setState(71);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Programa) {
				{
				setState(70);
				programa();
				}
			}

			setState(73);
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
		public VariablesContext variables() {
			return getRuleContext(VariablesContext.class,0);
		}
		public PrincipalContext principal() {
			return getRuleContext(PrincipalContext.class,0);
		}
		public List<FunctionsContext> functions() {
			return getRuleContexts(FunctionsContext.class);
		}
		public FunctionsContext functions(int i) {
			return getRuleContext(FunctionsContext.class,i);
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
			setState(75);
			match(Programa);
			setState(76);
			match(ID);
			setState(77);
			match(T__0);
			setState(78);
			variables();
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Function) {
				{
				{
				setState(79);
				functions();
				}
				}
				setState(84);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(85);
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
			setState(87);
			match(Principal);
			setState(88);
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

	public static class VariablesContext extends ParserRuleContext {
		public TerminalNode Var() { return getToken(PatitoMasMasParser.Var, 0); }
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public VariablesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variables; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterVariables(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitVariables(this);
		}
	}

	public final VariablesContext variables() throws RecognitionException {
		VariablesContext _localctx = new VariablesContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_variables);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(Var);
			setState(91);
			var();
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
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public IdsContext ids() {
			return getRuleContext(IdsContext.class,0);
		}
		public List<VarContext> var() {
			return getRuleContexts(VarContext.class);
		}
		public VarContext var(int i) {
			return getRuleContext(VarContext.class,i);
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
		enterRule(_localctx, 8, RULE_var);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			tipo();
			setState(94);
			match(T__1);
			setState(95);
			ids();
			setState(96);
			match(T__0);
			setState(100);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(97);
					var();
					}
					} 
				}
				setState(102);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
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
		public Id_cteContext id_cte() {
			return getRuleContext(Id_cteContext.class,0);
		}
		public List<IdsContext> ids() {
			return getRuleContexts(IdsContext.class);
		}
		public IdsContext ids(int i) {
			return getRuleContext(IdsContext.class,i);
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
		enterRule(_localctx, 10, RULE_ids);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			id_cte();
			setState(108);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(104);
					match(T__2);
					setState(105);
					ids();
					}
					} 
				}
				setState(110);
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
			exitRule();
		}
		return _localctx;
	}

	public static class Id_cteContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PatitoMasMasParser.ID, 0); }
		public List<TerminalNode> CTE_INT() { return getTokens(PatitoMasMasParser.CTE_INT); }
		public TerminalNode CTE_INT(int i) {
			return getToken(PatitoMasMasParser.CTE_INT, i);
		}
		public Id_cteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_cte; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterId_cte(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitId_cte(this);
		}
	}

	public final Id_cteContext id_cte() throws RecognitionException {
		Id_cteContext _localctx = new Id_cteContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_id_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(ID);
			setState(115);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(112);
				match(T__3);
				setState(113);
				match(CTE_INT);
				setState(114);
				match(T__4);
				}
				break;
			}
			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(117);
				match(T__3);
				setState(118);
				match(CTE_INT);
				setState(119);
				match(T__4);
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

	public static class FunctionsContext extends ParserRuleContext {
		public TerminalNode Function() { return getToken(PatitoMasMasParser.Function, 0); }
		public Tipo_retContext tipo_ret() {
			return getRuleContext(Tipo_retContext.class,0);
		}
		public TerminalNode ID() { return getToken(PatitoMasMasParser.ID, 0); }
		public VariablesContext variables() {
			return getRuleContext(VariablesContext.class,0);
		}
		public Bloque_estContext bloque_est() {
			return getRuleContext(Bloque_estContext.class,0);
		}
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public FunctionsContext functions() {
			return getRuleContext(FunctionsContext.class,0);
		}
		public FunctionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functions; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterFunctions(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitFunctions(this);
		}
	}

	public final FunctionsContext functions() throws RecognitionException {
		FunctionsContext _localctx = new FunctionsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_functions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			match(Function);
			setState(123);
			tipo_ret();
			setState(124);
			match(ID);
			setState(125);
			match(T__5);
			setState(127);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Int) | (1L << Float) | (1L << CTE_CHAR))) != 0)) {
				{
				setState(126);
				params();
				}
			}

			setState(129);
			match(T__6);
			setState(130);
			match(T__0);
			setState(131);
			variables();
			setState(132);
			bloque_est();
			setState(134);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(133);
				functions();
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
		enterRule(_localctx, 16, RULE_tipo_ret);
		try {
			setState(138);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Void:
				enterOuterAlt(_localctx, 1);
				{
				setState(136);
				match(Void);
				}
				break;
			case Int:
			case Float:
			case CTE_CHAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(137);
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
		enterRule(_localctx, 18, RULE_params);
		try {
			setState(148);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(140);
				tipo();
				setState(141);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(143);
				tipo();
				setState(144);
				match(ID);
				setState(145);
				match(T__2);
				setState(146);
				params();
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

	public static class Bloque_estContext extends ParserRuleContext {
		public EstatutosContext estatutos() {
			return getRuleContext(EstatutosContext.class,0);
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
		enterRule(_localctx, 20, RULE_bloque_est);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(T__7);
			setState(151);
			estatutos();
			setState(152);
			match(T__8);
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

	public static class EstatutosContext extends ParserRuleContext {
		public List<EstatutoContext> estatuto() {
			return getRuleContexts(EstatutoContext.class);
		}
		public EstatutoContext estatuto(int i) {
			return getRuleContext(EstatutoContext.class,i);
		}
		public EstatutosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_estatutos; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterEstatutos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitEstatutos(this);
		}
	}

	public final EstatutosContext estatutos() throws RecognitionException {
		EstatutosContext _localctx = new EstatutosContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_estatutos);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Regresa) | (1L << Lee) | (1L << Escribe) | (1L << Si) | (1L << Mientras) | (1L << Desde) | (1L << Nombre) | (1L << ID))) != 0)) {
				{
				{
				setState(154);
				estatuto();
				}
				}
				setState(159);
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
		enterRule(_localctx, 24, RULE_estatuto);
		try {
			setState(167);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(160);
				asignacion();
				}
				break;
			case Regresa:
				enterOuterAlt(_localctx, 2);
				{
				setState(161);
				retorno();
				}
				break;
			case Lee:
				enterOuterAlt(_localctx, 3);
				{
				setState(162);
				lectura();
				}
				break;
			case Si:
				enterOuterAlt(_localctx, 4);
				{
				setState(163);
				decision();
				}
				break;
			case Mientras:
			case Desde:
				enterOuterAlt(_localctx, 5);
				{
				setState(164);
				repeticion();
				}
				break;
			case Nombre:
				enterOuterAlt(_localctx, 6);
				{
				setState(165);
				llamada_est();
				}
				break;
			case Escribe:
				enterOuterAlt(_localctx, 7);
				{
				setState(166);
				escritura();
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

	public static class AsignacionContext extends ParserRuleContext {
		public Id_expContext id_exp() {
			return getRuleContext(Id_expContext.class,0);
		}
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public Op_espContext op_esp() {
			return getRuleContext(Op_espContext.class,0);
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
		enterRule(_localctx, 26, RULE_asignacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			id_exp();
			setState(170);
			match(T__9);
			setState(171);
			expresion();
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__10) | (1L << T__11) | (1L << T__12))) != 0)) {
				{
				setState(172);
				op_esp();
				}
			}

			setState(175);
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

	public static class Id_expressionsContext extends ParserRuleContext {
		public List<Id_expContext> id_exp() {
			return getRuleContexts(Id_expContext.class);
		}
		public Id_expContext id_exp(int i) {
			return getRuleContext(Id_expContext.class,i);
		}
		public Id_expressionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_expressions; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterId_expressions(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitId_expressions(this);
		}
	}

	public final Id_expressionsContext id_expressions() throws RecognitionException {
		Id_expressionsContext _localctx = new Id_expressionsContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_id_expressions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(177);
				id_exp();
				}
				}
				setState(182);
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

	public static class Id_expContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PatitoMasMasParser.ID, 0); }
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public Id_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterId_exp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitId_exp(this);
		}
	}

	public final Id_expContext id_exp() throws RecognitionException {
		Id_expContext _localctx = new Id_expContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_id_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(183);
			match(ID);
			setState(188);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(184);
				match(T__3);
				setState(185);
				expresion();
				setState(186);
				match(T__4);
				}
				break;
			}
			setState(194);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(190);
				match(T__3);
				setState(191);
				expresion();
				setState(192);
				match(T__4);
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
		enterRule(_localctx, 32, RULE_retorno);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			match(Regresa);
			setState(197);
			match(T__5);
			setState(198);
			expresion();
			setState(199);
			match(T__6);
			setState(200);
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
		public Id_expressionsContext id_expressions() {
			return getRuleContext(Id_expressionsContext.class,0);
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
		enterRule(_localctx, 34, RULE_lectura);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(Lee);
			setState(203);
			match(T__5);
			setState(204);
			id_expressions();
			setState(205);
			match(T__6);
			setState(206);
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
		enterRule(_localctx, 36, RULE_escritura);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			match(Escribe);
			setState(209);
			match(T__5);
			setState(210);
			escrituras();
			setState(211);
			match(T__6);
			setState(212);
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
		public TerminalNode CTE_STRING() { return getToken(PatitoMasMasParser.CTE_STRING, 0); }
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
		enterRule(_localctx, 38, RULE_escrituras);
		try {
			setState(223);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(214);
				match(CTE_STRING);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(215);
				expresion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(216);
				match(CTE_STRING);
				setState(217);
				match(T__2);
				setState(218);
				escrituras();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(219);
				expresion();
				setState(220);
				match(T__2);
				setState(221);
				escrituras();
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
		enterRule(_localctx, 40, RULE_decision);
		try {
			setState(241);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(225);
				match(Si);
				setState(226);
				match(T__5);
				setState(227);
				expresion();
				setState(228);
				match(T__6);
				setState(229);
				match(Entonces);
				setState(230);
				bloque_est();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(232);
				match(Si);
				setState(233);
				match(T__5);
				setState(234);
				expresion();
				setState(235);
				match(T__6);
				setState(236);
				match(Entonces);
				setState(237);
				bloque_est();
				setState(238);
				match(Sino);
				setState(239);
				bloque_est();
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
		enterRule(_localctx, 42, RULE_repeticion);
		try {
			setState(245);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Mientras:
				enterOuterAlt(_localctx, 1);
				{
				setState(243);
				condicional();
				}
				break;
			case Desde:
				enterOuterAlt(_localctx, 2);
				{
				setState(244);
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
		enterRule(_localctx, 44, RULE_condicional);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			match(Mientras);
			setState(248);
			expresion();
			setState(249);
			match(Haz);
			setState(250);
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
		public Id_expContext id_exp() {
			return getRuleContext(Id_expContext.class,0);
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
		enterRule(_localctx, 46, RULE_no_condicional);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			match(Desde);
			setState(253);
			id_exp();
			setState(254);
			match(T__9);
			setState(255);
			expresion();
			setState(256);
			match(Hasta);
			setState(257);
			expresion();
			setState(258);
			match(Hacer);
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

	public static class LlamadaContext extends ParserRuleContext {
		public TerminalNode Nombre() { return getToken(PatitoMasMasParser.Nombre, 0); }
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
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
		enterRule(_localctx, 48, RULE_llamada);
		try {
			setState(271);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(261);
				match(Nombre);
				setState(262);
				match(T__5);
				setState(263);
				match(T__6);
				setState(264);
				match(T__0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(265);
				match(Nombre);
				setState(266);
				match(T__5);
				setState(267);
				params();
				setState(268);
				match(T__6);
				setState(269);
				match(T__0);
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
		enterRule(_localctx, 50, RULE_llamada_est);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(273);
			llamada();
			setState(274);
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
		enterRule(_localctx, 52, RULE_op_esp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(276);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__10) | (1L << T__11) | (1L << T__12))) != 0)) ) {
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

	public static class ExpresionContext extends ParserRuleContext {
		public Exp_aContext exp_a() {
			return getRuleContext(Exp_aContext.class,0);
		}
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
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
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_expresion);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(278);
			exp_a();
			setState(280);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__13) {
				{
				setState(279);
				match(T__13);
				}
			}

			setState(285);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(282);
					expresion();
					}
					} 
				}
				setState(287);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
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

	public static class Exp_aContext extends ParserRuleContext {
		public Exp_bContext exp_b() {
			return getRuleContext(Exp_bContext.class,0);
		}
		public List<Exp_aContext> exp_a() {
			return getRuleContexts(Exp_aContext.class);
		}
		public Exp_aContext exp_a(int i) {
			return getRuleContext(Exp_aContext.class,i);
		}
		public Exp_aContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_a; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterExp_a(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitExp_a(this);
		}
	}

	public final Exp_aContext exp_a() throws RecognitionException {
		Exp_aContext _localctx = new Exp_aContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_exp_a);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			exp_b();
			setState(290);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14) {
				{
				setState(289);
				match(T__14);
				}
			}

			setState(295);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(292);
					exp_a();
					}
					} 
				}
				setState(297);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
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

	public static class Exp_bContext extends ParserRuleContext {
		public List<Exp_cContext> exp_c() {
			return getRuleContexts(Exp_cContext.class);
		}
		public Exp_cContext exp_c(int i) {
			return getRuleContext(Exp_cContext.class,i);
		}
		public Exp_bContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_b; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterExp_b(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitExp_b(this);
		}
	}

	public final Exp_bContext exp_b() throws RecognitionException {
		Exp_bContext _localctx = new Exp_bContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_exp_b);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(298);
			exp_c();
			setState(303);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__15) {
				{
				setState(299);
				match(T__15);
				setState(300);
				match(T__16);
				setState(301);
				match(T__17);
				setState(302);
				match(T__18);
				}
			}

			setState(306);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				{
				setState(305);
				exp_c();
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

	public static class Exp_cContext extends ParserRuleContext {
		public Exp_dContext exp_d() {
			return getRuleContext(Exp_dContext.class,0);
		}
		public Exp_cContext exp_c() {
			return getRuleContext(Exp_cContext.class,0);
		}
		public Exp_cContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_c; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterExp_c(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitExp_c(this);
		}
	}

	public final Exp_cContext exp_c() throws RecognitionException {
		Exp_cContext _localctx = new Exp_cContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_exp_c);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
			exp_d();
			setState(311);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__19) {
				{
				setState(309);
				match(T__19);
				setState(310);
				match(T__20);
				}
			}

			setState(314);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				{
				setState(313);
				exp_c();
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

	public static class Exp_dContext extends ParserRuleContext {
		public Exp_eContext exp_e() {
			return getRuleContext(Exp_eContext.class,0);
		}
		public Exp_dContext exp_d() {
			return getRuleContext(Exp_dContext.class,0);
		}
		public Exp_dContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_d; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterExp_d(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitExp_d(this);
		}
	}

	public final Exp_dContext exp_d() throws RecognitionException {
		Exp_dContext _localctx = new Exp_dContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_exp_d);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(316);
			exp_e();
			setState(319);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__21) {
				{
				setState(317);
				match(T__21);
				setState(318);
				match(T__22);
				}
			}

			setState(322);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				{
				setState(321);
				exp_d();
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

	public static class Exp_eContext extends ParserRuleContext {
		public Id_expContext id_exp() {
			return getRuleContext(Id_expContext.class,0);
		}
		public Var_cteContext var_cte() {
			return getRuleContext(Var_cteContext.class,0);
		}
		public LlamadaContext llamada() {
			return getRuleContext(LlamadaContext.class,0);
		}
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public Exp_eContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_e; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).enterExp_e(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PatitoMasMasListener ) ((PatitoMasMasListener)listener).exitExp_e(this);
		}
	}

	public final Exp_eContext exp_e() throws RecognitionException {
		Exp_eContext _localctx = new Exp_eContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_exp_e);
		try {
			setState(331);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(324);
				id_exp();
				}
				break;
			case CTE_INT:
			case CTE_FLOAT:
			case CTE_CHAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(325);
				var_cte();
				}
				break;
			case Nombre:
				enterOuterAlt(_localctx, 3);
				{
				setState(326);
				llamada();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 4);
				{
				setState(327);
				match(T__5);
				setState(328);
				expresion();
				setState(329);
				match(T__6);
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

	public static class TipoContext extends ParserRuleContext {
		public TerminalNode Int() { return getToken(PatitoMasMasParser.Int, 0); }
		public TerminalNode Float() { return getToken(PatitoMasMasParser.Float, 0); }
		public TerminalNode CTE_CHAR() { return getToken(PatitoMasMasParser.CTE_CHAR, 0); }
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
		enterRule(_localctx, 66, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(333);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Int) | (1L << Float) | (1L << CTE_CHAR))) != 0)) ) {
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

	public static class Var_cteContext extends ParserRuleContext {
		public TerminalNode CTE_INT() { return getToken(PatitoMasMasParser.CTE_INT, 0); }
		public TerminalNode CTE_FLOAT() { return getToken(PatitoMasMasParser.CTE_FLOAT, 0); }
		public TerminalNode CTE_CHAR() { return getToken(PatitoMasMasParser.CTE_CHAR, 0); }
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
		enterRule(_localctx, 68, RULE_var_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(335);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CTE_INT) | (1L << CTE_FLOAT) | (1L << CTE_CHAR))) != 0)) ) {
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65\u0154\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\3\2\5\2J\n\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3S"+
		"\n\3\f\3\16\3V\13\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3"+
		"\6\7\6e\n\6\f\6\16\6h\13\6\3\7\3\7\3\7\7\7m\n\7\f\7\16\7p\13\7\3\b\3\b"+
		"\3\b\3\b\5\bv\n\b\3\b\3\b\3\b\5\b{\n\b\3\t\3\t\3\t\3\t\3\t\5\t\u0082\n"+
		"\t\3\t\3\t\3\t\3\t\3\t\5\t\u0089\n\t\3\n\3\n\5\n\u008d\n\n\3\13\3\13\3"+
		"\13\3\13\3\13\3\13\3\13\3\13\5\13\u0097\n\13\3\f\3\f\3\f\3\f\3\r\7\r\u009e"+
		"\n\r\f\r\16\r\u00a1\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00aa"+
		"\n\16\3\17\3\17\3\17\3\17\5\17\u00b0\n\17\3\17\3\17\3\20\7\20\u00b5\n"+
		"\20\f\20\16\20\u00b8\13\20\3\21\3\21\3\21\3\21\3\21\5\21\u00bf\n\21\3"+
		"\21\3\21\3\21\3\21\5\21\u00c5\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23"+
		"\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00e2\n\25\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00f4\n\26"+
		"\3\27\3\27\5\27\u00f8\n\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32"+
		"\3\32\5\32\u0112\n\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\5\35\u011b\n"+
		"\35\3\35\7\35\u011e\n\35\f\35\16\35\u0121\13\35\3\36\3\36\5\36\u0125\n"+
		"\36\3\36\7\36\u0128\n\36\f\36\16\36\u012b\13\36\3\37\3\37\3\37\3\37\3"+
		"\37\5\37\u0132\n\37\3\37\5\37\u0135\n\37\3 \3 \3 \5 \u013a\n \3 \5 \u013d"+
		"\n \3!\3!\3!\5!\u0142\n!\3!\5!\u0145\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5"+
		"\"\u014e\n\"\3#\3#\3$\3$\3$\2\2%\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36"+
		" \"$&(*,.\60\62\64\668:<>@BDF\2\5\3\2\r\17\4\2*+\62\62\3\2\60\62\2\u0158"+
		"\2I\3\2\2\2\4M\3\2\2\2\6Y\3\2\2\2\b\\\3\2\2\2\n_\3\2\2\2\fi\3\2\2\2\16"+
		"q\3\2\2\2\20|\3\2\2\2\22\u008c\3\2\2\2\24\u0096\3\2\2\2\26\u0098\3\2\2"+
		"\2\30\u009f\3\2\2\2\32\u00a9\3\2\2\2\34\u00ab\3\2\2\2\36\u00b6\3\2\2\2"+
		" \u00b9\3\2\2\2\"\u00c6\3\2\2\2$\u00cc\3\2\2\2&\u00d2\3\2\2\2(\u00e1\3"+
		"\2\2\2*\u00f3\3\2\2\2,\u00f7\3\2\2\2.\u00f9\3\2\2\2\60\u00fe\3\2\2\2\62"+
		"\u0111\3\2\2\2\64\u0113\3\2\2\2\66\u0116\3\2\2\28\u0118\3\2\2\2:\u0122"+
		"\3\2\2\2<\u012c\3\2\2\2>\u0136\3\2\2\2@\u013e\3\2\2\2B\u014d\3\2\2\2D"+
		"\u014f\3\2\2\2F\u0151\3\2\2\2HJ\5\4\3\2IH\3\2\2\2IJ\3\2\2\2JK\3\2\2\2"+
		"KL\7\2\2\3L\3\3\2\2\2MN\7\32\2\2NO\7/\2\2OP\7\3\2\2PT\5\b\5\2QS\5\20\t"+
		"\2RQ\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2VT\3\2\2\2WX\5\6\4"+
		"\2X\5\3\2\2\2YZ\7\33\2\2Z[\5\26\f\2[\7\3\2\2\2\\]\7\34\2\2]^\5\n\6\2^"+
		"\t\3\2\2\2_`\5D#\2`a\7\4\2\2ab\5\f\7\2bf\7\3\2\2ce\5\n\6\2dc\3\2\2\2e"+
		"h\3\2\2\2fd\3\2\2\2fg\3\2\2\2g\13\3\2\2\2hf\3\2\2\2in\5\16\b\2jk\7\5\2"+
		"\2km\5\f\7\2lj\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2\2o\r\3\2\2\2pn\3\2"+
		"\2\2qu\7/\2\2rs\7\6\2\2st\7\60\2\2tv\7\7\2\2ur\3\2\2\2uv\3\2\2\2vz\3\2"+
		"\2\2wx\7\6\2\2xy\7\60\2\2y{\7\7\2\2zw\3\2\2\2z{\3\2\2\2{\17\3\2\2\2|}"+
		"\7\35\2\2}~\5\22\n\2~\177\7/\2\2\177\u0081\7\b\2\2\u0080\u0082\5\24\13"+
		"\2\u0081\u0080\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084"+
		"\7\t\2\2\u0084\u0085\7\3\2\2\u0085\u0086\5\b\5\2\u0086\u0088\5\26\f\2"+
		"\u0087\u0089\5\20\t\2\u0088\u0087\3\2\2\2\u0088\u0089\3\2\2\2\u0089\21"+
		"\3\2\2\2\u008a\u008d\7-\2\2\u008b\u008d\5D#\2\u008c\u008a\3\2\2\2\u008c"+
		"\u008b\3\2\2\2\u008d\23\3\2\2\2\u008e\u008f\5D#\2\u008f\u0090\7/\2\2\u0090"+
		"\u0097\3\2\2\2\u0091\u0092\5D#\2\u0092\u0093\7/\2\2\u0093\u0094\7\5\2"+
		"\2\u0094\u0095\5\24\13\2\u0095\u0097\3\2\2\2\u0096\u008e\3\2\2\2\u0096"+
		"\u0091\3\2\2\2\u0097\25\3\2\2\2\u0098\u0099\7\n\2\2\u0099\u009a\5\30\r"+
		"\2\u009a\u009b\7\13\2\2\u009b\27\3\2\2\2\u009c\u009e\5\32\16\2\u009d\u009c"+
		"\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0"+
		"\31\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00aa\5\34\17\2\u00a3\u00aa\5\""+
		"\22\2\u00a4\u00aa\5$\23\2\u00a5\u00aa\5*\26\2\u00a6\u00aa\5,\27\2\u00a7"+
		"\u00aa\5\64\33\2\u00a8\u00aa\5&\24\2\u00a9\u00a2\3\2\2\2\u00a9\u00a3\3"+
		"\2\2\2\u00a9\u00a4\3\2\2\2\u00a9\u00a5\3\2\2\2\u00a9\u00a6\3\2\2\2\u00a9"+
		"\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\33\3\2\2\2\u00ab\u00ac\5 \21"+
		"\2\u00ac\u00ad\7\f\2\2\u00ad\u00af\58\35\2\u00ae\u00b0\5\66\34\2\u00af"+
		"\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\7\3"+
		"\2\2\u00b2\35\3\2\2\2\u00b3\u00b5\5 \21\2\u00b4\u00b3\3\2\2\2\u00b5\u00b8"+
		"\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\37\3\2\2\2\u00b8"+
		"\u00b6\3\2\2\2\u00b9\u00be\7/\2\2\u00ba\u00bb\7\6\2\2\u00bb\u00bc\58\35"+
		"\2\u00bc\u00bd\7\7\2\2\u00bd\u00bf\3\2\2\2\u00be\u00ba\3\2\2\2\u00be\u00bf"+
		"\3\2\2\2\u00bf\u00c4\3\2\2\2\u00c0\u00c1\7\6\2\2\u00c1\u00c2\58\35\2\u00c2"+
		"\u00c3\7\7\2\2\u00c3\u00c5\3\2\2\2\u00c4\u00c0\3\2\2\2\u00c4\u00c5\3\2"+
		"\2\2\u00c5!\3\2\2\2\u00c6\u00c7\7\36\2\2\u00c7\u00c8\7\b\2\2\u00c8\u00c9"+
		"\58\35\2\u00c9\u00ca\7\t\2\2\u00ca\u00cb\7\3\2\2\u00cb#\3\2\2\2\u00cc"+
		"\u00cd\7\37\2\2\u00cd\u00ce\7\b\2\2\u00ce\u00cf\5\36\20\2\u00cf\u00d0"+
		"\7\t\2\2\u00d0\u00d1\7\3\2\2\u00d1%\3\2\2\2\u00d2\u00d3\7 \2\2\u00d3\u00d4"+
		"\7\b\2\2\u00d4\u00d5\5(\25\2\u00d5\u00d6\7\t\2\2\u00d6\u00d7\7\3\2\2\u00d7"+
		"\'\3\2\2\2\u00d8\u00e2\7\63\2\2\u00d9\u00e2\58\35\2\u00da\u00db\7\63\2"+
		"\2\u00db\u00dc\7\5\2\2\u00dc\u00e2\5(\25\2\u00dd\u00de\58\35\2\u00de\u00df"+
		"\7\5\2\2\u00df\u00e0\5(\25\2\u00e0\u00e2\3\2\2\2\u00e1\u00d8\3\2\2\2\u00e1"+
		"\u00d9\3\2\2\2\u00e1\u00da\3\2\2\2\u00e1\u00dd\3\2\2\2\u00e2)\3\2\2\2"+
		"\u00e3\u00e4\7!\2\2\u00e4\u00e5\7\b\2\2\u00e5\u00e6\58\35\2\u00e6\u00e7"+
		"\7\t\2\2\u00e7\u00e8\7\"\2\2\u00e8\u00e9\5\26\f\2\u00e9\u00f4\3\2\2\2"+
		"\u00ea\u00eb\7!\2\2\u00eb\u00ec\7\b\2\2\u00ec\u00ed\58\35\2\u00ed\u00ee"+
		"\7\t\2\2\u00ee\u00ef\7\"\2\2\u00ef\u00f0\5\26\f\2\u00f0\u00f1\7#\2\2\u00f1"+
		"\u00f2\5\26\f\2\u00f2\u00f4\3\2\2\2\u00f3\u00e3\3\2\2\2\u00f3\u00ea\3"+
		"\2\2\2\u00f4+\3\2\2\2\u00f5\u00f8\5.\30\2\u00f6\u00f8\5\60\31\2\u00f7"+
		"\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8-\3\2\2\2\u00f9\u00fa\7$\2\2\u00fa"+
		"\u00fb\58\35\2\u00fb\u00fc\7%\2\2\u00fc\u00fd\5\26\f\2\u00fd/\3\2\2\2"+
		"\u00fe\u00ff\7&\2\2\u00ff\u0100\5 \21\2\u0100\u0101\7\f\2\2\u0101\u0102"+
		"\58\35\2\u0102\u0103\7\'\2\2\u0103\u0104\58\35\2\u0104\u0105\7(\2\2\u0105"+
		"\u0106\5\26\f\2\u0106\61\3\2\2\2\u0107\u0108\7)\2\2\u0108\u0109\7\b\2"+
		"\2\u0109\u010a\7\t\2\2\u010a\u0112\7\3\2\2\u010b\u010c\7)\2\2\u010c\u010d"+
		"\7\b\2\2\u010d\u010e\5\24\13\2\u010e\u010f\7\t\2\2\u010f\u0110\7\3\2\2"+
		"\u0110\u0112\3\2\2\2\u0111\u0107\3\2\2\2\u0111\u010b\3\2\2\2\u0112\63"+
		"\3\2\2\2\u0113\u0114\5\62\32\2\u0114\u0115\7\3\2\2\u0115\65\3\2\2\2\u0116"+
		"\u0117\t\2\2\2\u0117\67\3\2\2\2\u0118\u011a\5:\36\2\u0119\u011b\7\20\2"+
		"\2\u011a\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011f\3\2\2\2\u011c\u011e"+
		"\58\35\2\u011d\u011c\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3\2\2\2\u011f"+
		"\u0120\3\2\2\2\u01209\3\2\2\2\u0121\u011f\3\2\2\2\u0122\u0124\5<\37\2"+
		"\u0123\u0125\7\21\2\2\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0129"+
		"\3\2\2\2\u0126\u0128\5:\36\2\u0127\u0126\3\2\2\2\u0128\u012b\3\2\2\2\u0129"+
		"\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a;\3\2\2\2\u012b\u0129\3\2\2\2"+
		"\u012c\u0131\5> \2\u012d\u012e\7\22\2\2\u012e\u012f\7\23\2\2\u012f\u0130"+
		"\7\24\2\2\u0130\u0132\7\25\2\2\u0131\u012d\3\2\2\2\u0131\u0132\3\2\2\2"+
		"\u0132\u0134\3\2\2\2\u0133\u0135\5> \2\u0134\u0133\3\2\2\2\u0134\u0135"+
		"\3\2\2\2\u0135=\3\2\2\2\u0136\u0139\5@!\2\u0137\u0138\7\26\2\2\u0138\u013a"+
		"\7\27\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c\3\2\2\2"+
		"\u013b\u013d\5> \2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d?\3\2"+
		"\2\2\u013e\u0141\5B\"\2\u013f\u0140\7\30\2\2\u0140\u0142\7\31\2\2\u0141"+
		"\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0144\3\2\2\2\u0143\u0145\5@"+
		"!\2\u0144\u0143\3\2\2\2\u0144\u0145\3\2\2\2\u0145A\3\2\2\2\u0146\u014e"+
		"\5 \21\2\u0147\u014e\5F$\2\u0148\u014e\5\62\32\2\u0149\u014a\7\b\2\2\u014a"+
		"\u014b\58\35\2\u014b\u014c\7\t\2\2\u014c\u014e\3\2\2\2\u014d\u0146\3\2"+
		"\2\2\u014d\u0147\3\2\2\2\u014d\u0148\3\2\2\2\u014d\u0149\3\2\2\2\u014e"+
		"C\3\2\2\2\u014f\u0150\t\3\2\2\u0150E\3\2\2\2\u0151\u0152\t\4\2\2\u0152"+
		"G\3\2\2\2!ITfnuz\u0081\u0088\u008c\u0096\u009f\u00a9\u00af\u00b6\u00be"+
		"\u00c4\u00e1\u00f3\u00f7\u0111\u011a\u011f\u0124\u0129\u0131\u0134\u0139"+
		"\u013c\u0141\u0144\u014d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
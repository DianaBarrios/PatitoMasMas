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
		RULE_start = 0, RULE_programa = 1, RULE_principal = 2, RULE_variables = 3, 
		RULE_var = 4, RULE_ids = 5, RULE_id_cte = 6, RULE_functions = 7, RULE_tipo_ret = 8, 
		RULE_params = 9, RULE_bloque_est = 10, RULE_estatutos = 11, RULE_estatuto = 12, 
		RULE_asignacion = 13, RULE_id_expressions = 14, RULE_id_exp = 15, RULE_retorno = 16, 
		RULE_lectura = 17, RULE_escritura = 18, RULE_escrituras = 19, RULE_decision = 20, 
		RULE_repeticion = 21, RULE_condicional = 22, RULE_no_condicional = 23, 
		RULE_llamada = 24, RULE_params_llamada = 25, RULE_llamada_est = 26, RULE_op_esp = 27, 
		RULE_expresion = 28, RULE_exp_a = 29, RULE_exp_b = 30, RULE_exp_c = 31, 
		RULE_exp_d = 32, RULE_exp_e = 33, RULE_tipo = 34, RULE_var_cte = 35;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "programa", "principal", "variables", "var", "ids", "id_cte", 
			"functions", "tipo_ret", "params", "bloque_est", "estatutos", "estatuto", 
			"asignacion", "id_expressions", "id_exp", "retorno", "lectura", "escritura", 
			"escrituras", "decision", "repeticion", "condicional", "no_condicional", 
			"llamada", "params_llamada", "llamada_est", "op_esp", "expresion", "exp_a", 
			"exp_b", "exp_c", "exp_d", "exp_e", "tipo", "var_cte"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "','", "'['", "']'", "'('", "')'", "'{'", "'}'", "'='", 
			"'$'", "'?'", "'\u00A1'", "'||'", "'&'", "'>'", "'<'", "'=='", "'!='", 
			"'+'", "'-'", "'*'", "'/'", "'programa'", "'principal()'", "'var'", "'funcion'", 
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
			setState(73);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Programa) {
				{
				setState(72);
				programa();
				}
			}

			setState(75);
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
			setState(77);
			match(Programa);
			setState(78);
			match(ID);
			setState(79);
			match(T__0);
			setState(80);
			variables();
			setState(84);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Function) {
				{
				{
				setState(81);
				functions();
				}
				}
				setState(86);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(87);
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
			setState(89);
			match(Principal);
			setState(90);
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
			setState(92);
			match(Var);
			setState(93);
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
			setState(95);
			tipo();
			setState(96);
			ids();
			setState(97);
			match(T__0);
			setState(101);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(98);
					var();
					}
					} 
				}
				setState(103);
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
			setState(104);
			id_cte();
			setState(109);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(105);
					match(T__1);
					setState(106);
					ids();
					}
					} 
				}
				setState(111);
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
			setState(112);
			match(ID);
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2) {
				{
				setState(113);
				match(T__2);
				setState(114);
				match(CTE_INT);
				setState(115);
				match(T__3);
				setState(119);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__2) {
					{
					setState(116);
					match(T__2);
					setState(117);
					match(CTE_INT);
					setState(118);
					match(T__3);
					}
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
			setState(123);
			match(Function);
			setState(124);
			tipo_ret();
			setState(125);
			match(ID);
			setState(126);
			match(T__4);
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Int) | (1L << Float) | (1L << Char))) != 0)) {
				{
				setState(127);
				params();
				}
			}

			setState(130);
			match(T__5);
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
			case Char:
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
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			tipo();
			setState(141);
			match(ID);
			setState(144);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(142);
				match(T__1);
				setState(143);
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
			setState(146);
			match(T__6);
			setState(147);
			estatutos();
			setState(148);
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
			setState(153);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Regresa) | (1L << Lee) | (1L << Escribe) | (1L << Si) | (1L << Mientras) | (1L << Desde) | (1L << ID))) != 0)) {
				{
				{
				setState(150);
				estatuto();
				}
				}
				setState(155);
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
			setState(163);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(156);
				asignacion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(157);
				retorno();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(158);
				lectura();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(159);
				decision();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(160);
				repeticion();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(161);
				llamada_est();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(162);
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
			setState(165);
			id_exp();
			setState(166);
			match(T__8);
			setState(167);
			expresion();
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__9) | (1L << T__10) | (1L << T__11))) != 0)) {
				{
				setState(168);
				op_esp();
				}
			}

			setState(171);
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
			setState(176);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(173);
				id_exp();
				}
				}
				setState(178);
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
			setState(179);
			match(ID);
			setState(184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(180);
				match(T__2);
				setState(181);
				expresion();
				setState(182);
				match(T__3);
				}
				break;
			}
			setState(190);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2) {
				{
				setState(186);
				match(T__2);
				setState(187);
				expresion();
				setState(188);
				match(T__3);
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
			setState(192);
			match(Regresa);
			setState(193);
			match(T__4);
			setState(194);
			expresion();
			setState(195);
			match(T__5);
			setState(196);
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
			setState(198);
			match(Lee);
			setState(199);
			match(T__4);
			setState(200);
			id_expressions();
			setState(201);
			match(T__5);
			setState(202);
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
			setState(204);
			match(Escribe);
			setState(205);
			match(T__4);
			setState(206);
			escrituras();
			setState(207);
			match(T__5);
			setState(208);
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
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CTE_STRING:
				{
				setState(210);
				match(CTE_STRING);
				}
				break;
			case T__4:
			case ID:
			case CTE_INT:
			case CTE_FLOAT:
			case CTE_CHAR:
				{
				setState(211);
				expresion();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(216);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(214);
				match(T__1);
				setState(215);
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
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			match(Si);
			setState(219);
			match(T__4);
			setState(220);
			expresion();
			setState(221);
			match(T__5);
			setState(222);
			match(Entonces);
			setState(223);
			bloque_est();
			setState(226);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Sino) {
				{
				setState(224);
				match(Sino);
				setState(225);
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
		enterRule(_localctx, 42, RULE_repeticion);
		try {
			setState(230);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Mientras:
				enterOuterAlt(_localctx, 1);
				{
				setState(228);
				condicional();
				}
				break;
			case Desde:
				enterOuterAlt(_localctx, 2);
				{
				setState(229);
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
			setState(232);
			match(Mientras);
			setState(233);
			expresion();
			setState(234);
			match(Haz);
			setState(235);
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
			setState(237);
			match(Desde);
			setState(238);
			id_exp();
			setState(239);
			match(T__8);
			setState(240);
			expresion();
			setState(241);
			match(Hasta);
			setState(242);
			expresion();
			setState(243);
			match(Hacer);
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
		enterRule(_localctx, 48, RULE_llamada);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(246);
			match(ID);
			setState(247);
			match(T__4);
			setState(249);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(248);
				params_llamada();
				}
			}

			setState(251);
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
		public TerminalNode ID() { return getToken(PatitoMasMasParser.ID, 0); }
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
		enterRule(_localctx, 50, RULE_params_llamada);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
			match(ID);
			setState(256);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(254);
				match(T__1);
				setState(255);
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
		enterRule(_localctx, 52, RULE_llamada_est);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			llamada();
			setState(259);
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
		enterRule(_localctx, 54, RULE_op_esp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(261);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__9) | (1L << T__10) | (1L << T__11))) != 0)) ) {
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
		enterRule(_localctx, 56, RULE_expresion);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			exp_a();
			setState(265);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(264);
				match(T__12);
				}
			}

			setState(270);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(267);
					expresion();
					}
					} 
				}
				setState(272);
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
		enterRule(_localctx, 58, RULE_exp_a);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(273);
			exp_b();
			setState(275);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__13) {
				{
				setState(274);
				match(T__13);
				}
			}

			setState(280);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(277);
					exp_a();
					}
					} 
				}
				setState(282);
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
		enterRule(_localctx, 60, RULE_exp_b);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			exp_c();
			setState(288);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14) {
				{
				setState(284);
				match(T__14);
				setState(285);
				match(T__15);
				setState(286);
				match(T__16);
				setState(287);
				match(T__17);
				}
			}

			setState(291);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				{
				setState(290);
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
		enterRule(_localctx, 62, RULE_exp_c);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(293);
			exp_d();
			setState(296);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__18) {
				{
				setState(294);
				match(T__18);
				setState(295);
				match(T__19);
				}
			}

			setState(299);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				{
				setState(298);
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
		enterRule(_localctx, 64, RULE_exp_d);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(301);
			exp_e();
			setState(304);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(302);
				match(T__20);
				setState(303);
				match(T__21);
				}
			}

			setState(307);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				{
				setState(306);
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
		enterRule(_localctx, 66, RULE_exp_e);
		try {
			setState(316);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(309);
				id_exp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(310);
				var_cte();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(311);
				llamada();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(312);
				match(T__4);
				setState(313);
				expresion();
				setState(314);
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

	public static class TipoContext extends ParserRuleContext {
		public TerminalNode Int() { return getToken(PatitoMasMasParser.Int, 0); }
		public TerminalNode Float() { return getToken(PatitoMasMasParser.Float, 0); }
		public TerminalNode Char() { return getToken(PatitoMasMasParser.Char, 0); }
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
		enterRule(_localctx, 68, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(318);
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
		enterRule(_localctx, 70, RULE_var_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(320);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63\u0145\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\5\2L\n\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3"+
		"\7\3U\n\3\f\3\16\3X\13\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3"+
		"\6\7\6f\n\6\f\6\16\6i\13\6\3\7\3\7\3\7\7\7n\n\7\f\7\16\7q\13\7\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\5\bz\n\b\5\b|\n\b\3\t\3\t\3\t\3\t\3\t\5\t\u0083\n"+
		"\t\3\t\3\t\3\t\3\t\5\t\u0089\n\t\3\n\3\n\5\n\u008d\n\n\3\13\3\13\3\13"+
		"\3\13\5\13\u0093\n\13\3\f\3\f\3\f\3\f\3\r\7\r\u009a\n\r\f\r\16\r\u009d"+
		"\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00a6\n\16\3\17\3\17\3\17"+
		"\3\17\5\17\u00ac\n\17\3\17\3\17\3\20\7\20\u00b1\n\20\f\20\16\20\u00b4"+
		"\13\20\3\21\3\21\3\21\3\21\3\21\5\21\u00bb\n\21\3\21\3\21\3\21\3\21\5"+
		"\21\u00c1\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\5\25\u00d7\n\25\3\25\3\25"+
		"\5\25\u00db\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00e5\n"+
		"\26\3\27\3\27\5\27\u00e9\n\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\5\32\u00fc\n\32\3\32\3\32"+
		"\3\33\3\33\3\33\5\33\u0103\n\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\5\36"+
		"\u010c\n\36\3\36\7\36\u010f\n\36\f\36\16\36\u0112\13\36\3\37\3\37\5\37"+
		"\u0116\n\37\3\37\7\37\u0119\n\37\f\37\16\37\u011c\13\37\3 \3 \3 \3 \3"+
		" \5 \u0123\n \3 \5 \u0126\n \3!\3!\3!\5!\u012b\n!\3!\5!\u012e\n!\3\"\3"+
		"\"\3\"\5\"\u0133\n\"\3\"\5\"\u0136\n\"\3#\3#\3#\3#\3#\3#\3#\5#\u013f\n"+
		"#\3$\3$\3%\3%\3%\2\2&\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,."+
		"\60\62\64\668:<>@BDFH\2\5\3\2\f\16\3\2(*\3\2-/\2\u0148\2K\3\2\2\2\4O\3"+
		"\2\2\2\6[\3\2\2\2\b^\3\2\2\2\na\3\2\2\2\fj\3\2\2\2\16r\3\2\2\2\20}\3\2"+
		"\2\2\22\u008c\3\2\2\2\24\u008e\3\2\2\2\26\u0094\3\2\2\2\30\u009b\3\2\2"+
		"\2\32\u00a5\3\2\2\2\34\u00a7\3\2\2\2\36\u00b2\3\2\2\2 \u00b5\3\2\2\2\""+
		"\u00c2\3\2\2\2$\u00c8\3\2\2\2&\u00ce\3\2\2\2(\u00d6\3\2\2\2*\u00dc\3\2"+
		"\2\2,\u00e8\3\2\2\2.\u00ea\3\2\2\2\60\u00ef\3\2\2\2\62\u00f8\3\2\2\2\64"+
		"\u00ff\3\2\2\2\66\u0104\3\2\2\28\u0107\3\2\2\2:\u0109\3\2\2\2<\u0113\3"+
		"\2\2\2>\u011d\3\2\2\2@\u0127\3\2\2\2B\u012f\3\2\2\2D\u013e\3\2\2\2F\u0140"+
		"\3\2\2\2H\u0142\3\2\2\2JL\5\4\3\2KJ\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\7\2"+
		"\2\3N\3\3\2\2\2OP\7\31\2\2PQ\7,\2\2QR\7\3\2\2RV\5\b\5\2SU\5\20\t\2TS\3"+
		"\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2WY\3\2\2\2XV\3\2\2\2YZ\5\6\4\2Z\5"+
		"\3\2\2\2[\\\7\32\2\2\\]\5\26\f\2]\7\3\2\2\2^_\7\33\2\2_`\5\n\6\2`\t\3"+
		"\2\2\2ab\5F$\2bc\5\f\7\2cg\7\3\2\2df\5\n\6\2ed\3\2\2\2fi\3\2\2\2ge\3\2"+
		"\2\2gh\3\2\2\2h\13\3\2\2\2ig\3\2\2\2jo\5\16\b\2kl\7\4\2\2ln\5\f\7\2mk"+
		"\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3\2\2\2p\r\3\2\2\2qo\3\2\2\2r{\7,\2\2s"+
		"t\7\5\2\2tu\7-\2\2uy\7\6\2\2vw\7\5\2\2wx\7-\2\2xz\7\6\2\2yv\3\2\2\2yz"+
		"\3\2\2\2z|\3\2\2\2{s\3\2\2\2{|\3\2\2\2|\17\3\2\2\2}~\7\34\2\2~\177\5\22"+
		"\n\2\177\u0080\7,\2\2\u0080\u0082\7\7\2\2\u0081\u0083\5\24\13\2\u0082"+
		"\u0081\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085\7\b"+
		"\2\2\u0085\u0086\5\b\5\2\u0086\u0088\5\26\f\2\u0087\u0089\5\20\t\2\u0088"+
		"\u0087\3\2\2\2\u0088\u0089\3\2\2\2\u0089\21\3\2\2\2\u008a\u008d\7+\2\2"+
		"\u008b\u008d\5F$\2\u008c\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d\23\3"+
		"\2\2\2\u008e\u008f\5F$\2\u008f\u0092\7,\2\2\u0090\u0091\7\4\2\2\u0091"+
		"\u0093\5\24\13\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\25\3\2"+
		"\2\2\u0094\u0095\7\t\2\2\u0095\u0096\5\30\r\2\u0096\u0097\7\n\2\2\u0097"+
		"\27\3\2\2\2\u0098\u009a\5\32\16\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2"+
		"\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\31\3\2\2\2\u009d\u009b"+
		"\3\2\2\2\u009e\u00a6\5\34\17\2\u009f\u00a6\5\"\22\2\u00a0\u00a6\5$\23"+
		"\2\u00a1\u00a6\5*\26\2\u00a2\u00a6\5,\27\2\u00a3\u00a6\5\66\34\2\u00a4"+
		"\u00a6\5&\24\2\u00a5\u009e\3\2\2\2\u00a5\u009f\3\2\2\2\u00a5\u00a0\3\2"+
		"\2\2\u00a5\u00a1\3\2\2\2\u00a5\u00a2\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5"+
		"\u00a4\3\2\2\2\u00a6\33\3\2\2\2\u00a7\u00a8\5 \21\2\u00a8\u00a9\7\13\2"+
		"\2\u00a9\u00ab\5:\36\2\u00aa\u00ac\58\35\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac"+
		"\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\7\3\2\2\u00ae\35\3\2\2\2\u00af"+
		"\u00b1\5 \21\2\u00b0\u00af\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2"+
		"\2\2\u00b2\u00b3\3\2\2\2\u00b3\37\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00ba"+
		"\7,\2\2\u00b6\u00b7\7\5\2\2\u00b7\u00b8\5:\36\2\u00b8\u00b9\7\6\2\2\u00b9"+
		"\u00bb\3\2\2\2\u00ba\u00b6\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00c0\3\2"+
		"\2\2\u00bc\u00bd\7\5\2\2\u00bd\u00be\5:\36\2\u00be\u00bf\7\6\2\2\u00bf"+
		"\u00c1\3\2\2\2\u00c0\u00bc\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1!\3\2\2\2"+
		"\u00c2\u00c3\7\35\2\2\u00c3\u00c4\7\7\2\2\u00c4\u00c5\5:\36\2\u00c5\u00c6"+
		"\7\b\2\2\u00c6\u00c7\7\3\2\2\u00c7#\3\2\2\2\u00c8\u00c9\7\36\2\2\u00c9"+
		"\u00ca\7\7\2\2\u00ca\u00cb\5\36\20\2\u00cb\u00cc\7\b\2\2\u00cc\u00cd\7"+
		"\3\2\2\u00cd%\3\2\2\2\u00ce\u00cf\7\37\2\2\u00cf\u00d0\7\7\2\2\u00d0\u00d1"+
		"\5(\25\2\u00d1\u00d2\7\b\2\2\u00d2\u00d3\7\3\2\2\u00d3\'\3\2\2\2\u00d4"+
		"\u00d7\7\60\2\2\u00d5\u00d7\5:\36\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3"+
		"\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d9\7\4\2\2\u00d9\u00db\5(\25\2\u00da"+
		"\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db)\3\2\2\2\u00dc\u00dd\7 \2\2\u00dd"+
		"\u00de\7\7\2\2\u00de\u00df\5:\36\2\u00df\u00e0\7\b\2\2\u00e0\u00e1\7!"+
		"\2\2\u00e1\u00e4\5\26\f\2\u00e2\u00e3\7\"\2\2\u00e3\u00e5\5\26\f\2\u00e4"+
		"\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5+\3\2\2\2\u00e6\u00e9\5.\30\2"+
		"\u00e7\u00e9\5\60\31\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9-"+
		"\3\2\2\2\u00ea\u00eb\7#\2\2\u00eb\u00ec\5:\36\2\u00ec\u00ed\7$\2\2\u00ed"+
		"\u00ee\5\26\f\2\u00ee/\3\2\2\2\u00ef\u00f0\7%\2\2\u00f0\u00f1\5 \21\2"+
		"\u00f1\u00f2\7\13\2\2\u00f2\u00f3\5:\36\2\u00f3\u00f4\7&\2\2\u00f4\u00f5"+
		"\5:\36\2\u00f5\u00f6\7\'\2\2\u00f6\u00f7\5\26\f\2\u00f7\61\3\2\2\2\u00f8"+
		"\u00f9\7,\2\2\u00f9\u00fb\7\7\2\2\u00fa\u00fc\5\64\33\2\u00fb\u00fa\3"+
		"\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\7\b\2\2\u00fe"+
		"\63\3\2\2\2\u00ff\u0102\7,\2\2\u0100\u0101\7\4\2\2\u0101\u0103\5\64\33"+
		"\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\65\3\2\2\2\u0104\u0105"+
		"\5\62\32\2\u0105\u0106\7\3\2\2\u0106\67\3\2\2\2\u0107\u0108\t\2\2\2\u0108"+
		"9\3\2\2\2\u0109\u010b\5<\37\2\u010a\u010c\7\17\2\2\u010b\u010a\3\2\2\2"+
		"\u010b\u010c\3\2\2\2\u010c\u0110\3\2\2\2\u010d\u010f\5:\36\2\u010e\u010d"+
		"\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111"+
		";\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0115\5> \2\u0114\u0116\7\20\2\2\u0115"+
		"\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u011a\3\2\2\2\u0117\u0119\5<"+
		"\37\2\u0118\u0117\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a"+
		"\u011b\3\2\2\2\u011b=\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u0122\5@!\2\u011e"+
		"\u011f\7\21\2\2\u011f\u0120\7\22\2\2\u0120\u0121\7\23\2\2\u0121\u0123"+
		"\7\24\2\2\u0122\u011e\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0125\3\2\2\2"+
		"\u0124\u0126\5@!\2\u0125\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126?\3\2"+
		"\2\2\u0127\u012a\5B\"\2\u0128\u0129\7\25\2\2\u0129\u012b\7\26\2\2\u012a"+
		"\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012d\3\2\2\2\u012c\u012e\5@"+
		"!\2\u012d\u012c\3\2\2\2\u012d\u012e\3\2\2\2\u012eA\3\2\2\2\u012f\u0132"+
		"\5D#\2\u0130\u0131\7\27\2\2\u0131\u0133\7\30\2\2\u0132\u0130\3\2\2\2\u0132"+
		"\u0133\3\2\2\2\u0133\u0135\3\2\2\2\u0134\u0136\5B\"\2\u0135\u0134\3\2"+
		"\2\2\u0135\u0136\3\2\2\2\u0136C\3\2\2\2\u0137\u013f\5 \21\2\u0138\u013f"+
		"\5H%\2\u0139\u013f\5\62\32\2\u013a\u013b\7\7\2\2\u013b\u013c\5:\36\2\u013c"+
		"\u013d\7\b\2\2\u013d\u013f\3\2\2\2\u013e\u0137\3\2\2\2\u013e\u0138\3\2"+
		"\2\2\u013e\u0139\3\2\2\2\u013e\u013a\3\2\2\2\u013fE\3\2\2\2\u0140\u0141"+
		"\t\3\2\2\u0141G\3\2\2\2\u0142\u0143\t\4\2\2\u0143I\3\2\2\2#KVgoy{\u0082"+
		"\u0088\u008c\u0092\u009b\u00a5\u00ab\u00b2\u00ba\u00c0\u00d6\u00da\u00e4"+
		"\u00e8\u00fb\u0102\u010b\u0110\u0115\u011a\u0122\u0125\u012a\u012d\u0132"+
		"\u0135\u013e";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
// Generated from PatitoMasMas.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PatitoMasMasParser}.
 */
public interface PatitoMasMasListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(PatitoMasMasParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(PatitoMasMasParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(PatitoMasMasParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(PatitoMasMasParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#principal}.
	 * @param ctx the parse tree
	 */
	void enterPrincipal(PatitoMasMasParser.PrincipalContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#principal}.
	 * @param ctx the parse tree
	 */
	void exitPrincipal(PatitoMasMasParser.PrincipalContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#variables}.
	 * @param ctx the parse tree
	 */
	void enterVariables(PatitoMasMasParser.VariablesContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#variables}.
	 * @param ctx the parse tree
	 */
	void exitVariables(PatitoMasMasParser.VariablesContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#var}.
	 * @param ctx the parse tree
	 */
	void enterVar(PatitoMasMasParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#var}.
	 * @param ctx the parse tree
	 */
	void exitVar(PatitoMasMasParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#ids}.
	 * @param ctx the parse tree
	 */
	void enterIds(PatitoMasMasParser.IdsContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#ids}.
	 * @param ctx the parse tree
	 */
	void exitIds(PatitoMasMasParser.IdsContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#id_cte}.
	 * @param ctx the parse tree
	 */
	void enterId_cte(PatitoMasMasParser.Id_cteContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#id_cte}.
	 * @param ctx the parse tree
	 */
	void exitId_cte(PatitoMasMasParser.Id_cteContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#functions}.
	 * @param ctx the parse tree
	 */
	void enterFunctions(PatitoMasMasParser.FunctionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#functions}.
	 * @param ctx the parse tree
	 */
	void exitFunctions(PatitoMasMasParser.FunctionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#tipo_ret}.
	 * @param ctx the parse tree
	 */
	void enterTipo_ret(PatitoMasMasParser.Tipo_retContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#tipo_ret}.
	 * @param ctx the parse tree
	 */
	void exitTipo_ret(PatitoMasMasParser.Tipo_retContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#params}.
	 * @param ctx the parse tree
	 */
	void enterParams(PatitoMasMasParser.ParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#params}.
	 * @param ctx the parse tree
	 */
	void exitParams(PatitoMasMasParser.ParamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#bloque_est}.
	 * @param ctx the parse tree
	 */
	void enterBloque_est(PatitoMasMasParser.Bloque_estContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#bloque_est}.
	 * @param ctx the parse tree
	 */
	void exitBloque_est(PatitoMasMasParser.Bloque_estContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#estatutos}.
	 * @param ctx the parse tree
	 */
	void enterEstatutos(PatitoMasMasParser.EstatutosContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#estatutos}.
	 * @param ctx the parse tree
	 */
	void exitEstatutos(PatitoMasMasParser.EstatutosContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#estatuto}.
	 * @param ctx the parse tree
	 */
	void enterEstatuto(PatitoMasMasParser.EstatutoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#estatuto}.
	 * @param ctx the parse tree
	 */
	void exitEstatuto(PatitoMasMasParser.EstatutoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(PatitoMasMasParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(PatitoMasMasParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#id_expressions}.
	 * @param ctx the parse tree
	 */
	void enterId_expressions(PatitoMasMasParser.Id_expressionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#id_expressions}.
	 * @param ctx the parse tree
	 */
	void exitId_expressions(PatitoMasMasParser.Id_expressionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#id_exp}.
	 * @param ctx the parse tree
	 */
	void enterId_exp(PatitoMasMasParser.Id_expContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#id_exp}.
	 * @param ctx the parse tree
	 */
	void exitId_exp(PatitoMasMasParser.Id_expContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#retorno}.
	 * @param ctx the parse tree
	 */
	void enterRetorno(PatitoMasMasParser.RetornoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#retorno}.
	 * @param ctx the parse tree
	 */
	void exitRetorno(PatitoMasMasParser.RetornoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#lectura}.
	 * @param ctx the parse tree
	 */
	void enterLectura(PatitoMasMasParser.LecturaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#lectura}.
	 * @param ctx the parse tree
	 */
	void exitLectura(PatitoMasMasParser.LecturaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#escritura}.
	 * @param ctx the parse tree
	 */
	void enterEscritura(PatitoMasMasParser.EscrituraContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#escritura}.
	 * @param ctx the parse tree
	 */
	void exitEscritura(PatitoMasMasParser.EscrituraContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#escrituras}.
	 * @param ctx the parse tree
	 */
	void enterEscrituras(PatitoMasMasParser.EscriturasContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#escrituras}.
	 * @param ctx the parse tree
	 */
	void exitEscrituras(PatitoMasMasParser.EscriturasContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#decision}.
	 * @param ctx the parse tree
	 */
	void enterDecision(PatitoMasMasParser.DecisionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#decision}.
	 * @param ctx the parse tree
	 */
	void exitDecision(PatitoMasMasParser.DecisionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#repeticion}.
	 * @param ctx the parse tree
	 */
	void enterRepeticion(PatitoMasMasParser.RepeticionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#repeticion}.
	 * @param ctx the parse tree
	 */
	void exitRepeticion(PatitoMasMasParser.RepeticionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#condicional}.
	 * @param ctx the parse tree
	 */
	void enterCondicional(PatitoMasMasParser.CondicionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#condicional}.
	 * @param ctx the parse tree
	 */
	void exitCondicional(PatitoMasMasParser.CondicionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#no_condicional}.
	 * @param ctx the parse tree
	 */
	void enterNo_condicional(PatitoMasMasParser.No_condicionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#no_condicional}.
	 * @param ctx the parse tree
	 */
	void exitNo_condicional(PatitoMasMasParser.No_condicionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#llamada}.
	 * @param ctx the parse tree
	 */
	void enterLlamada(PatitoMasMasParser.LlamadaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#llamada}.
	 * @param ctx the parse tree
	 */
	void exitLlamada(PatitoMasMasParser.LlamadaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#params_llamada}.
	 * @param ctx the parse tree
	 */
	void enterParams_llamada(PatitoMasMasParser.Params_llamadaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#params_llamada}.
	 * @param ctx the parse tree
	 */
	void exitParams_llamada(PatitoMasMasParser.Params_llamadaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#llamada_est}.
	 * @param ctx the parse tree
	 */
	void enterLlamada_est(PatitoMasMasParser.Llamada_estContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#llamada_est}.
	 * @param ctx the parse tree
	 */
	void exitLlamada_est(PatitoMasMasParser.Llamada_estContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#op_esp}.
	 * @param ctx the parse tree
	 */
	void enterOp_esp(PatitoMasMasParser.Op_espContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#op_esp}.
	 * @param ctx the parse tree
	 */
	void exitOp_esp(PatitoMasMasParser.Op_espContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExpresion(PatitoMasMasParser.ExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExpresion(PatitoMasMasParser.ExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#exp_a}.
	 * @param ctx the parse tree
	 */
	void enterExp_a(PatitoMasMasParser.Exp_aContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#exp_a}.
	 * @param ctx the parse tree
	 */
	void exitExp_a(PatitoMasMasParser.Exp_aContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#exp_b}.
	 * @param ctx the parse tree
	 */
	void enterExp_b(PatitoMasMasParser.Exp_bContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#exp_b}.
	 * @param ctx the parse tree
	 */
	void exitExp_b(PatitoMasMasParser.Exp_bContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#exp_c}.
	 * @param ctx the parse tree
	 */
	void enterExp_c(PatitoMasMasParser.Exp_cContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#exp_c}.
	 * @param ctx the parse tree
	 */
	void exitExp_c(PatitoMasMasParser.Exp_cContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#exp_d}.
	 * @param ctx the parse tree
	 */
	void enterExp_d(PatitoMasMasParser.Exp_dContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#exp_d}.
	 * @param ctx the parse tree
	 */
	void exitExp_d(PatitoMasMasParser.Exp_dContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#exp_e}.
	 * @param ctx the parse tree
	 */
	void enterExp_e(PatitoMasMasParser.Exp_eContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#exp_e}.
	 * @param ctx the parse tree
	 */
	void exitExp_e(PatitoMasMasParser.Exp_eContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(PatitoMasMasParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(PatitoMasMasParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoMasMasParser#var_cte}.
	 * @param ctx the parse tree
	 */
	void enterVar_cte(PatitoMasMasParser.Var_cteContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoMasMasParser#var_cte}.
	 * @param ctx the parse tree
	 */
	void exitVar_cte(PatitoMasMasParser.Var_cteContext ctx);
}
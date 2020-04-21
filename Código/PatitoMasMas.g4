// Define a grammar called PatitoMasMas
grammar PatitoMasMas;

/*
    Expressions
*/
start
    : programa? EOF
    ;

programa
    : Programa ID ';' dec_variables? dec_functions? principal
    ;

principal
    : Principal bloque_est
    ;

dec_variables
    : Var dec_var+
    ;

dec_var
    : tipo lista_ids+ ';'
    ;

lista_ids
    : ids (','  lista_ids)?
    ;

ids
    : ID dimension? dimension?
    ;

dimension
    : '[' CTE_INT ']'
    ;

dec_functions
	: funcion+
	;

funcion
    : Function tipo_ret ID '(' params? ')' ';' dec_variables? bloque_est
    ;

tipo_ret
    : Void
    | tipo
    ;

params
    : tipo ID (',' params)?
    ;

bloque_est
    : '{' estatuto* '}'
    ;

estatuto
    : asignacion
    | retorno
    | lectura
    | decision
    | repeticion
    | llamada_est
    | escritura
    ;

asignacion
    : var '=' expresion  ';'
    ;

var
    : ID dim? dim?
    ;

dim
    : '[' expresion ']'
    ;

retorno
    : Regresa '(' expresion ')' ';'
    ;

lectura
    : Lee '(' lista_vars ')' ';'
    ;

lista_vars
    : var (',' lista_vars)?
    ;

escritura
    : Escribe '(' escrituras ')' ';'
    ;

escrituras
    : (string | expresion) (',' escrituras)?
    ;

string
    : CTE_STRING
    ;

decision
    : Si '(' expresion ')' Entonces bloque_est (Sino bloque_est)?
    ;

repeticion
    : condicional
    | no_condicional
    ;

condicional
    : Mientras expresion Haz bloque_est
    ;

no_condicional
    : Desde var '=' expresion Hasta expresion Hacer bloque_est
    ;

llamada
    : ID '(' params_llamada? ')'
    ;

params_llamada
    : expresion (',' params_llamada)?
    ;

llamada_est
    : llamada ';'
    ;

expresion
    : exp
    | expresion op_log expresion
    | exp op_comp exp
    ;

op_log
    : '&'
    | '||'
    ;

op_comp
    : '>'
    | '<'
    | '=='
    | '!='
    ;

exp
    : term
    | term op_arit exp
    ;

op_arit
    : '+'
    | '-'
    ;

term
    : factor
    | factor op_prod term
    ;

op_prod
    : '*'
    | '/'
    ;

factor
    : var op_esp?
    | (op_arit)? var_cte
    | llamada
    | par_empieza expresion par_termina
    ;

par_empieza
	: '('
	;

par_termina
	: ')'
	;

var_cte
    : var
    | CTE_INT
    | CTE_FLOAT
    ;

op_esp
    : '$'
    | '?'
    | '¡'
    ;

tipo
    : Int
    | Float
    ;

/*
    Keywords and Tokens
*/

Programa
    : 'programa'
    ;

Principal
    : 'principal()'
    ;

Var
    : 'var'
    ;

Function
    : 'funcion'
    ;

Regresa
    : 'regresa'
    ;

Lee
    : 'lee'
    ;

Escribe
    : 'escribe'
    ;

Si
    : 'si'
    ;

Entonces
    : 'entonces'
    ;

Sino
    : 'sino'
    ;

Mientras
    : 'mientras'
    ;

Haz
    : 'haz'
    ;

Desde
    : 'desde'
    ;

Hasta
    : 'hasta'
    ;

Hacer
    : 'hacer'
    ;


Int
    : 'int'
    ;

Float
    : 'float'
    ;

Char
    : 'char'
    ;

Void
    : 'void'
    ;

ID
    : [a-z] [0-9a-zA-Z]*
    ;

CTE_INT
    : DIGIT +
    ;

CTE_FLOAT
    : CTE_INT '.' CTE_INT
    ;

CTE_CHAR
    : '\'' [a-zA-Z] '\''
    ;

CTE_STRING
    : '"' ~["]* '"'
    ;

DIGIT
    : ('0' .. '9')
    ;

Whitespace
   : [ \t]+ -> skip
   ;

Newline
   : ('\r' '\n'? | '\n') -> skip
   ;

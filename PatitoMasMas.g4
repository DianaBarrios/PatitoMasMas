// Define a grammar called PatitoMasMas
grammar PatitoMasMas;

/*
    Expressions
*/
start
    : programa? EOF
    ;

programa
    : Programa ID ';' variables functions* principal

    ;

principal
    : Principal bloque_est
    ;

variables
    : Var var;

var
    : tipo ':' ids ';' var*
    ;

ids
    : id_cte (','  ids)*
    ;

id_cte
    : ID ('[' CTE_INT ']')? ('[' CTE_INT ']')?
    ;

functions
    : Function tipo_ret ID '(' params? ')' ';' variables bloque_est functions?
    ;

tipo_ret
    : Void
    | tipo
    ;

params
    : tipo ID
    | tipo ID ',' params
    ;

bloque_est
    : '{' estatutos '}'
    ;

estatutos
    : estatuto*
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
    : id_exp '=' expresion op_esp?  ';'
    ;

id_expressions
    : id_exp*
    ;

id_exp
    : ID ('[' expresion ']')? ('[' expresion ']')?
    ;

retorno
    : Regresa '(' expresion ')' ';'
    ;

lectura
    : Lee '(' id_expressions ')' ';'
    ;

escritura
    : Escribe '(' escrituras ')' ';'
    ;

escrituras
    : CTE_STRING
    | expresion
    | CTE_STRING ',' escrituras
    | expresion  ',' escrituras
    ;

decision
    : Si '(' expresion ')' Entonces bloque_est
    | Si '(' expresion ')' Entonces bloque_est Sino bloque_est
    ;

repeticion
    : condicional
    | no_condicional
    ;

condicional
    : Mientras expresion Haz bloque_est
    ;

no_condicional
    : Desde id_exp '=' expresion Hasta expresion Hacer bloque_est
    ;

llamada
    : Nombre '(' ')' ';'
    | Nombre '(' params ')' ';'
    ;

llamada_est
    : llamada ';'
    ;

op_esp
    : '$'
    | '?'
    | '¡'
    ;

expresion
    : exp_a ('||')? expresion*
    ;

exp_a
    : exp_b ('&')? exp_a*
    ;

exp_b
    : exp_c ('>' '<' '==' '!=')? exp_c?
    ;

exp_c
    : exp_d ('+' '-')? exp_c?
    ;

exp_d
    : exp_e ('*' '/')? exp_d?
    ;

exp_e
    : id_exp
    | var_cte
    | llamada
    | '(' expresion ')'
    ;

tipo
    : Int
    | Float
    | CTE_CHAR
    ;

var_cte
    : CTE_INT
    | CTE_FLOAT
    | CTE_CHAR
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
    : 'function'
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

Nombre
    : 'nombre'
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

DIGIT
    : [0-9]
    ;


ID
    : [a-z] [0-9a-zA-Z]*
    ;

CTE_INT
    : [0-9]+
    ;

CTE_FLOAT
    : CTE_INT '.' CTE_INT
    ;

CTE_CHAR
    : [a-zA-Z]
    ;

CTE_STRING
    : '\'' CTE_CHAR+ '\''
    ;

Whitespace
   : [ \t]+ -> skip
   ;

Newline
   : ('\r' '\n'? | '\n') -> skip
   ;

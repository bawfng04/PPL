literal: literal_prim | array_literal | struct_literal;
literal_prim: INT_LIT | FLOAT_LIT | STRING_LIT | NIL | TRUE | FALSE;
struct_literal: ID LBRACE list_elements? RBRACE;
list_elements: element COMMA list_elements | element;
element: ID COLON expression;


program: (declared SEMICOLON)+ EOF;
declared:
	variables
	| constants
	| function
	| method
	| struct_type_declared
	| interface_type_declared;
function: FUNC ID LPAREN list_param? RPAREN type_minigo? LBRACE list_statement? RBRACE;
method:
	FUNC LPAREN ID ID RPAREN ID LPAREN list_param? RPAREN type_minigo? LBRACE list_statement? RBRACE;

struct_type_declared: TYPE ID STRUCT LBRACE list_fields RBRACE;
list_fields: fields SEMICOLON list_fields | fields SEMICOLON;
fields: ID type_minigo;

interface_type_declared: TYPE ID INTERFACE LBRACE list_meth_interface RBRACE;
list_meth_interface: meth_interface SEMICOLON list_meth_interface | meth_interface SEMICOLON;
meth_interface: ID LPAREN list_param? RPAREN type_minigo?;

list_param: param list_param | param;
param: list_ID type_minigo COMMA param | list_ID type_minigo;
list_ID: ID COMMA list_ID | ID;

list_statement: statement list_statement | statement;
statement: (
		declared_statement
		| assign_statement
		| if_statement
		| for_statement
		| break_statement
		| continue_statement
		| call_statement
		| return_statement
	) SEMICOLON;
declared_statement: variables | constants;
variables:
	VAR ID type_minigo
	| VAR ID (ASSIGN expression)
	| VAR ID type_minigo (ASSIGN expression);
constants: CONST ID ASSIGN expression;

assign_statement: (lhs) (
		SEMICOLON_ASSIGN
		| ADD_ASSIGN
		| SUB_ASSIGN
		| MUL_ASSIGN
		| DIV_ASSIGN
		| MOD_ASSIGN
	) expression;
lhs: lhs LBRACK expression RBRACK | lhs DOT ID | ID;

if_statement:
	IF LPAREN expression RPAREN LBRACE list_statement? RBRACE list_else_if? else_statement?;
list_else_if: else_if list_else_if | else_if;
else_statement: ELSE LBRACE list_statement? RBRACE;
else_if: ELSE IF LPAREN expression RPAREN LBRACE list_statement? RBRACE;

for_statement: basic_for | for_loop | for_array;
basic_for: FOR expression LBRACE list_statement? RBRACE;
for_loop:
	FOR (assign_for | variables_for) SEMICOLON expression SEMICOLON assign_for LBRACE list_statement RBRACE;
for_array: FOR ID COMMA ID SEMICOLON_ASSIGN RANGE expression LBRACE list_statement? RBRACE;
variables_for: VAR ID type_minigo? (ASSIGN expression);
assign_for: (ID) (
		SEMICOLON_ASSIGN
		| ADD_ASSIGN
		| SUB_ASSIGN
		| MUL_ASSIGN
		| DIV_ASSIGN
		| MOD_ASSIGN
	) expression;

break_statement: BREAK;
continue_statement: CONTINUE;
call_statement: (lhs DOT)? ID LPAREN list_expression? RPAREN;
return_statement: RETURN expression?;
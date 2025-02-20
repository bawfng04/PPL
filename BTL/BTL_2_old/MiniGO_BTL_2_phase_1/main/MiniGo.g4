grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    else:
        return super().emit();
}

options{
	language = Python3;
}

// program: list_expression;

//========================================================== PARSER ==========================================================

// program: (NEWLINE | declared)* EOF; Original: program: NEWLINE* declared (NEWLINE* declared)* NEWLINE* EOF;

// program: newlines declared more_declared newlines EOF;

program: list_expression;

newlines: | NEWLINE newlines;

more_declared: | newlines declared more_declared;

declared:
	(
		variables_declared
		| constants_declared
		| function_declared
		| method_declared
		| struct_declared
		| interface_declared
	) NEWLINE*;

// Original: list_statement: (statement NEWLINE*)* | statement;
list_statement: statement | statement newlines list_statement;

statement:
	declared_statement
	| assign_statement
	| if_statement
	| for_statement
	| break_statement
	| continue_statement
	| call_statement
	| return_statement;

// Variable and constant declarations

//khai báo biến - var + tên biến + type (optional) + giá trị (optional) + ";"
variables_declared: VAR var_decl_list SEMI;

// Original: var_decl_list: var_decl (COMMA var_decl)*;
var_decl_list: var_decl | var_decl COMMA var_decl_list;

var_decl: ID type_name? (ASSIGN expression)? | ID (COMMA ID)* type_name? (ASSIGN expr_list)?;

//khai báo hằng - const + tên hằng + giá trị + ";"

constants_declared: CONST const_decl_list (SEMI | NEWLINE);

// Original: const_decl_list: const_decl (COMMA const_decl)*;
const_decl_list: const_decl | const_decl COMMA const_decl_list;

const_decl: ID ASSIGN expression;

// khai báo hàm - func + tên hàm + (danh sách tham số - type) + (type trả về) + block_stmt
function_declared:
	FUNC ID LP params_list? RP (LP type_name (COMMA type_name)* RP | type_name)? NEWLINE? block_stmt;

//method
receiver: ID (ID | STRUCT | INTERFACE);

// method_declared: FUNC LP receiver RP ID LP params_list? RP (type_name)? block_stmt;
method_declared:
	FUNC LP receiver RP ID LP method_params? RP (LP type_name (COMMA type_name)* RP | type_name)? block_stmt;

// Original: method_params: method_param (COMMA method_param)*;
method_params: method_param | method_param COMMA method_params;

method_param: ID type_name;

// Block statement Original: params_list: param (COMMA param)*;
params_list: param | param COMMA params_list;

param: (ID | ID COMMA ID (COMMA ID)*) type_name;

// Struct declaration

//ex: type Point struct {x, y int}
struct_declared: TYPE ID STRUCT LB NEWLINE* struct_type NEWLINE* RB (SEMI | NEWLINE);

// struct_type: (ID type_name SEMI? NEWLINE*)*;

//struct_type: (ID (COMMA ID)* type_name SEMI? NEWLINE*)*;

//c Cal a int; -> wrong, c Calculator -> right;

// struct_type: ((ID (COMMA ID)* type_name SEMI? NEWLINE) | (ID (COMMA ID)* type_name SEMI NEWLINE?))*;

// Original: struct_type: (ID (COMMA ID)* type_name (SEMI | SEMI? NEWLINE))*;
struct_type: | struct_field struct_type;
struct_field: ID more_ids type_name struct_end;
more_ids: | COMMA ID more_ids;
struct_end: SEMI | SEMI? NEWLINE;

// Interface declaration

interface_declared: TYPE ID INTERFACE LB NEWLINE* interface_type RB SEMI?;

// Update interface_type rule Original: interface_type: (ID LP params_list? RP (type_name)? SEMI? NEWLINE*)*;
interface_type: | interface_method interface_type;
interface_method: ID LP optional_params RP optional_type optional_semi newlines;
optional_params: | params_list;
optional_type: | type_name;
optional_semi: | SEMI;

// Statements
declared_statement: variables_declared | constants_declared;

assign_statement: assign_lhs assign_op expression SEMI?;

assign_op: ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN | SHORT_ASSIGN;

assign_lhs: ID (field_access | element_access)*;

if_statement:
	IF LP expression RP NEWLINE? block_stmt NEWLINE? (ELSE if_statement | ELSE block_stmt)?;

for_statement:
	FOR (
		(ID | UNDERSCORE) COMMA (ID | UNDERSCORE) SHORT_ASSIGN RANGE expression block_stmt	// Range form
		| for_init SEMI expression SEMI for_update block_stmt								// Three-part form
		| expression block_stmt																// Basic form
	);

for_init:
	ID SHORT_ASSIGN expression				// Short declaration
	| ID assign_op expression				// Assignment
	| VAR ID type_name? ASSIGN expression;	// Variable declaration

//assign_lhs: ID (field_access | element_access)*;
for_update: assign_lhs assign_op expression;

break_statement: BREAK (SEMI | NEWLINE);

continue_statement: CONTINUE (SEMI | NEWLINE);

// Prevents return return expr (Test 34 passes) Allows return expr; and return; and return (Test 35 passes) Maintains proper statement separation with
// semicolons /newlines Forces proper statement termination return_statement: RETURN ((expression? SEMI) | (expression? NEWLINE) | expression | SEMI);
return_statement: RETURN (expression? SEMI | expression? NEWLINE);

call_statement: (ID | assign_lhs) LP list_expression? RP SEMI?;

block_stmt: NEWLINE? LB NEWLINE? (statement | NEWLINE)* NEWLINE? RB;

// Original: expr_list: expression (COMMA expression)*;
expr_list: expression | expression COMMA expr_list;

expression: expression OR expression1 | expression1;

expression1: expression1 AND expression2 | expression2;

expression2: expression2 (EQUAL | NOT_EQUAL) expression3 | expression3;

expression3:
	expression3 (LESS | LESS_OR_EQUAL | GREATER | GREATER_OR_EQUAL) expression4
	| expression4;
expression4: expression4 (ADD | SUB) expression5 | expression5;

expression5: expression5 (MUL | DIV | MOD) expression6 | expression6;

expression6: NOT expression6 | SUB expression6 | expression7;

//-1.c -> failed, a.b -> passed
expression7: operand (element_access | field_access | call_expr)*;

// Operands

operand: literal | ID | LP expression RP;

// Element access, field access, function calls

element_access: LSB expression RSB;

field_access: DOT ID;

call_expr: LP list_expression? RP;

// Literals

literal: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | array_literal | struct_literal;

// Array literal with type

// ex: [2][3]int{{1,2,3},{4,5,6}};
array_literal: array_type LB list_expression RB;

// ex: [2][3]int;
array_type: LSB INT_LIT RSB (LSB INT_LIT RSB)* type_name;

type_name: INT | FLOAT | STRING | BOOLEAN | ID | array_type;

// Struct literal

struct_literal: ID LB (field_list)? RB;

// Original: field_list: field_init (COMMA field_init)*;
field_list: field_init | field_init COMMA field_list;

field_init: ID COLON expression;

// List of expressions

// Original: list_expression: expression (COMMA expression)*;
list_expression: expression | expression COMMA list_expression;

//========================================================== LEXER ==========================================================

IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';
// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
LESS_OR_EQUAL: '<=';
GREATER: '>';
GREATER_OR_EQUAL: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
DOT: '.';
COLON: ':';
SHORT_ASSIGN: ':=';
UNDERSCORE: '_';
// Separators
LP: '(';
RP: ')';
LB: '{';
RB: '}';
LSB: '[';
RSB: ']';
COMMA: ',';
SEMI: ';';

// Identifiers

ID: [a-zA-Z_][a-zA-Z_0-9]*;

// Literals

fragment DECIMAL: '0' | [1-9][0-9]*;

fragment HEX: ('0x' | '0X') [0-9a-fA-F]+;

fragment OCTAL: ('0o' | '0O') [0-7]+;

fragment BINARY: ('0b' | '0B') [0-1]+;

fragment FLOAT_DECIMAL: '0' | [1-9][0-9]*;

fragment DECIMAL_PART: '.' [0-9]*;

fragment EXPONENT: [eE] [+-]? ('0' | [1-9][0-9]*);

INT_LIT:
	DECIMAL
	| HEX { self.text = str(int(self.text,16)) }
	| OCTAL { self.text = str(int(self.text,8)) }
	| BINARY { self.text = str(int(self.text,2)) };

FLOAT_LIT: FLOAT_DECIMAL DECIMAL_PART EXPONENT?;

// | FLOAT_DECIMAL EXPONENT | DECIMAL_PART [0-9]+ EXPONENT? | FLOAT_DECIMAL DECIMAL_PART;

fragment ESC_CHAR: 'r' | 'n' | 't' | '"' | '\\';

fragment STR_CHAR: ~[\r\n"\\] | '\\' ESC_CHAR;

STRING_LIT: '"' STR_CHAR* '"' { self.text = self.text[1:-1] };

// Newline + comments

// WS: [ \t\r\f]+ -> skip; //Lexer pass hết, Parser sẽ fail 14, 15, 16, 28, 29

// WS: [ \t\r\f\n]+ -> skip; //Lexer sẽ fail 14, 31, 32, Parser pass hết

WS: [ \t\r\f]+ -> skip;

// NEWLINE: '\n' | '\r' '\n' { self.text = "\n" };
NEWLINE: 'r'? '\n';

//nếu skip n -> fail lexer 14, 31, 32 nếu '\r'? '\n' {self.text = "\n"} -> fail parser 14, 15, 16, 28, 29

BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;

UNCLOSE_STRING: // Error handling
	'"' STR_CHAR* ([\r\n] | EOF) {
        if self.text[-1] in ['\r','\n']: #nếu kết thúc bằng dấu xuống dòng thì cắt dấu xuống dòng
            self.text = self.text[1:-1]
        else: #nếu kết thúc bằng EOF thì lấy từ đầu chuỗi đến hết
            self.text = self.text[1:]
        raise UncloseString(self.text)
    };

ILLEGAL_ESCAPE:
	'"' (STR_CHAR* '\\' ~[rnt"\\] STR_CHAR*) '"'? {
        illegal_str = str(self.text)
        i = illegal_str.find('\\')
        while i != -1 and illegal_str[i+1] in 'rnt"\\':
            i = illegal_str.find('\\', i+2)
        raise IllegalEscape(illegal_str[1:i+2])
    };

ERROR_CHAR: . {raise ErrorToken(self.text)};
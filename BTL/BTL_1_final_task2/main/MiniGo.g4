grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preType = None

def emit(self):
    tk = self.type
    self.preType = tk;
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

//========================================================== PARSER ==========================================================

// program: (NEWLINE | declared)* EOF; Original: program: NEWLINE* declared (NEWLINE* declared)* NEWLINE* EOF;

program: newlines declared more_declared newlines EOF;

// program: list_expression;

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
variables_declared: VAR var_decl_list (SEMI | NEWLINE);

// Original: var_decl_list: var_decl (COMMA var_decl)*;
var_decl_list: var_decl | var_decl COMMA var_decl_list;

// var_decl: ID type_name? (ASSIGN expression)? | ID (COMMA ID)* type_name? (ASSIGN expr_list)?;

var_decl:
	ID type_name (ASSIGN expression)?
	| ID (COMMA ID)* type_name (ASSIGN expr_list)?
	| ID (ASSIGN expression)
	| ID (COMMA ID)* (ASSIGN expr_list);

//khai báo hằng - const + tên hằng + giá trị + ";"

constants_declared: CONST const_decl_list (SEMI | NEWLINE);

// Original: const_decl_list: const_decl (COMMA const_decl)*;
const_decl_list: const_decl | const_decl COMMA const_decl_list;

const_decl: ID ASSIGN expression;

// khai báo hàm - func + tên hàm + (danh sách tham số - type) + (type trả về) + block_stmt ví dụ: func add(a int, b int) int { return a + b; }
not_null_block_statement: LB NEWLINE? statement (statement | NEWLINE)* NEWLINE? RB;

function_declared:
	FUNC ID LP params_list? RP (LP type_name (COMMA type_name)* RP | type_name)? NEWLINE? not_null_block_statement SEMI?;

//method
receiver: ID (ID | STRUCT | INTERFACE);

// method_declared: FUNC LP receiver RP ID LP params_list? RP (type_name)? block_stmt;
method_declared:
	FUNC LP receiver RP ID LP params_list? RP (type_name)? NEWLINE? block_stmt (SEMI | NEWLINE);

// Original: method_params: method_param (COMMA method_param)*;
method_params: method_param | method_param COMMA method_params;

method_param: ID type_name;

// Block statement Original: params_list: param (COMMA param)*;
params_list: ID type_name | ID (COMMA ID)* type_name | param (COMMA param)*;

param: (ID | ID COMMA ID (COMMA ID)*) type_name;

// Struct declaration

//ex: type Point struct {x, y int}
struct_declared: TYPE ID STRUCT LB NEWLINE* struct_type_list NEWLINE* RB (SEMI | NEWLINE);

struct_type_list: (struct_field NEWLINE*)+;

struct_field: ID more_ids type_name struct_end | method_declared;

more_ids: | COMMA ID more_ids;

struct_end: SEMI | SEMI? NEWLINE;

// struct_type: (ID type_name SEMI? NEWLINE*)*;

//struct_type: (ID (COMMA ID)* type_name SEMI? NEWLINE*)*;

//c Cal a int; -> wrong, c Calculator -> right;

// struct_type: ((ID (COMMA ID)* type_name SEMI? NEWLINE) | (ID (COMMA ID)* type_name SEMI NEWLINE?))*;

// Original: struct_type: (ID (COMMA ID)* type_name (SEMI | SEMI? NEWLINE))*;
struct_type: | struct_field struct_type;
// struct_field: ID more_ids type_name struct_end; more_ids: | COMMA ID more_ids; struct_end: SEMI | SEMI? NEWLINE;

// Interface declaration

interface_declared:
	TYPE ID INTERFACE LB NEWLINE* interface_type_list NEWLINE* RB (SEMI | NEWLINE);

interface_type_list: interface_method+;

// Update interface_type rule Original: interface_type: (ID LP params_list? RP (type_name)? SEMI? NEWLINE*)*;
interface_type: | interface_method interface_type;
interface_method:
	ID LP params_list? RP (type_name)? (SEMI | NEWLINE)
	| ID LP params_list? RP (type_name)? (SEMI | NEWLINE);
optional_params: | params_list;
optional_type: | type_name;
optional_semi: | SEMI;

// Statements
declared_statement: variables_declared | constants_declared;

assign_statement: assign_lhs assign_op expression SEMI?;

assign_op: ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN | SHORT_ASSIGN;

assign_lhs: ID (field_access | element_access)*;

if_statement:
	IF LP expression RP not_null_block_statement (
		ELSE if_statement
		| ELSE not_null_block_statement
	)?;

// FOR STATEMENT

for_statement:
	FOR (
		(ID | UNDERSCORE) COMMA (ID | UNDERSCORE) SHORT_ASSIGN RANGE expression not_null_block_statement	// Range form
		| for_init (SEMI | NEWLINE) expression (SEMI | NEWLINE) for_update not_null_block_statement			// Three-part form
		| expression not_null_block_statement
		// Basic form
	);

// for_statement: FOR ( (ID | UNDERSCORE) COMMA (ID | UNDERSCORE) SHORT_ASSIGN RANGE expression block_stmt | for_init (SEMI | NEWLINE) expression
// (SEMI | NEWLINE) for_update block_stmt | expression block_stmt );

// for_init: ID SHORT_ASSIGN expression // Short declaration | ID assign_op expression // Assignment | VAR ID type_name? ASSIGN expression; //
// Variable declaration

//for init cho btl2
for_init:
	assign_lhs SHORT_ASSIGN expression		// Short declaration
	| assign_lhs assign_op expression		// Assignment
	| VAR ID type_name? ASSIGN expression;	// Variable declaration

//assign_lhs: ID (field_access | element_access)*;
for_update: ID assign_op expression;

break_statement: BREAK (SEMI | NEWLINE);

continue_statement: CONTINUE (SEMI | NEWLINE);

// Prevents return return expr (Test 34 passes) Allows return expr; and return; and return (Test 35 passes) Maintains proper statement separation with
// semicolons /newlines Forces proper statement termination return_statement: RETURN ((expression? SEMI) | (expression? NEWLINE) | expression | SEMI);
return_statement: RETURN (expression? SEMI | expression? NEWLINE);

call_statement: (ID | assign_lhs) LP list_expression? RP SEMI?;

// block_stmt: NEWLINE? LB NEWLINE statement (statement | NEWLINE)* NEWLINE? RB;

block_stmt: LB NEWLINE? (statement | NEWLINE)* NEWLINE? RB;
//not_null_block_statement: not null

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

literal:
	INT_LIT
	| FLOAT_LIT
	| STRING_LIT
	| TRUE
	| FALSE
	| NIL
	| typed_array_literal
	| untyped_array_literal
	| struct_literal;

// Array literal with type

// ex: [2][3]int{{1,2,3},{4,5,6}};

typed_array_literal: array_type LB literal_list RB;
untyped_array_literal: LB literal_list RB;

array_literal: array_type LB literal_list RB | LB literal_list RB;

literal_list: literal_item (COMMA literal_item)*;

literal_item:
	untyped_array_literal
	| struct_literal
	| INT_LIT
	| FLOAT_LIT
	| STRING_LIT
	| TRUE
	| FALSE
	| NIL
	| ID;

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

//========================================================== LEXER ========================================================== Keywords Keywords
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

// Literals fragment DECIMAL: '0' | [1-9][0-9]*;
fragment DECIMAL: '0' | [1-9][0-9]*;
fragment HEX: ('0x' | '0X') [0-9a-fA-F]+;
fragment OCTAL: ('0o' | '0O') [0-7]+;
fragment BINARY: ('0b' | '0B') [0-1]+;

// fragment FLOAT_DECIMAL: '0' | [1-9][0-9]*;
fragment FLOAT_DECIMAL: [0-9]+;
fragment EXPONENT: [eE] [+-]? FLOAT_DECIMAL;
FLOAT_LIT: FLOAT_DECIMAL '.' [0-9]* EXPONENT?;

INT_LIT: DECIMAL | HEX | OCTAL | BINARY;

fragment ESC_CHAR: 'r' | 'n' | 't' | '"' | '\\';
fragment STR_CHAR: ~[\r\n"\\] | '\\' ESC_CHAR;
STRING_LIT: '"' STR_CHAR* '"' { self.text = self.text[1:-1] };

// Newline + comments

NEWLINE:
	'\r'? '\n' {
        if self.preType in [self.ID, self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT,
                           self.TRUE, self.FALSE, self.NIL,
                           self.RETURN, self.CONTINUE, self.BREAK,
                           self.RP, self.RB, self.RSB
						   ]:
            self.text = ';'
        else:
            self.skip()
    };

// TAB: '\t';

WS: [ \t\f\r]+ -> skip;

// Comments
BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// WS: [ \t\r\n\f]+ -> skip;

// NEWLINE: '\r'? '\n' -> skip;

// LINE_COMMENT: '//' ~[\r\n]* -> skip;

// BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;

// Error handling
UNCLOSE_STRING:
	'"' STR_CHAR* ([\r\n] | EOF) {
        if self.text[-1] in ['\r','\n']: #nếu kết thúc bằng dấu xuống dòng thì cắt dấu xuống dòng
            self.text = '\"' + self.text[1:-1]
        else: #nếu kết thúc bằng EOF thì lấy từ đầu chuỗi đến hết
            self.text = '\"' + self.text[1:]
        raise UncloseString(self.text)
    };

ILLEGAL_ESCAPE:
	'"' (STR_CHAR* '\\' ~[rnt"\\] STR_CHAR*) {
        illegal_str = self.text[1:] # Remove leading quote
        result = '"' + illegal_str # Reconstruct with leading quote
        raise IllegalEscape(result)
    };

ERROR_CHAR: . {raise ErrorToken(self.text)};
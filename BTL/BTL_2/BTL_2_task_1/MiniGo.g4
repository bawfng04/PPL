// 2210298 - Nguyễn Đinh Bằng

grammar MiniGo;

@lexer::header {
from lexererr import *
}
//16 02 2025 - 18 04 - remove some rule
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

program: (CONST ID ASSIGN expression SEMI) EOF;

/*
 newlines: | NEWLINE newlines; more_declared: | newlines declared more_declared; declared: (variables_declared | constants_declared |
 function_declared | method_declared | struct_declared | interface_declared) newlines; list_statement: statement | statement newlines list_statement;
 statement: declared_statement | assign_statement | if_statement | for_statement | break_statement | continue_statement | call_statement |
 return_statement; variables_declared: VAR var_decl (SEMI | NEWLINE); var_decl: ID type_name (ASSIGN expression)? | ID type_name_ids type_name (ASSIGN
 expr_list)? | ID (ASSIGN expression) | ID comma_ids (ASSIGN expr_list); type_name_ids: | COMMA ID type_name_ids; comma_ids: | COMMA ID comma_ids;
 constants_declared: CONST const_decl_list (SEMI | NEWLINE); const_decl_list: const_decl | const_decl COMMA const_decl_list; const_decl: ID ASSIGN
 expression; function_declared: FUNC ID LP params_list? RP return_type? NEWLINE? block_stmt (SEMI | NEWLINE); return_type: LP type_name more_types RP
 | type_name; more_types: | COMMA type_name more_types; receiver: ID (ID | STRUCT | INTERFACE); method_declared: FUNC LP receiver RP ID LP
 params_list? RP (type_name)? NEWLINE? block_stmt (SEMI | NEWLINE); params_list: ID type_name | ID comma_ids type_name | param | param COMMA
 params_list; param: ID type_name | ID comma_param_ids type_name; comma_param_ids: COMMA ID | COMMA ID comma_param_ids; struct_declared: TYPE ID
 STRUCT LB opt_newlines struct_type_list opt_newlines RB (SEMI | NEWLINE); struct_type_list: struct_field opt_newlines more_struct_fields;
 more_struct_fields: | struct_field opt_newlines more_struct_fields; opt_newlines: | NEWLINE opt_newlines; struct_field: ID more_ids type_name (SEMI |
 NEWLINE); more_ids: | COMMA ID more_ids; interface_declared: TYPE ID INTERFACE LB opt_newlines interface_type_list opt_newlines RB (SEMI | NEWLINE);
 interface_type_list: interface_method more_interface_methods; more_interface_methods: | interface_method more_interface_methods; interface_method: ID
 LP params_list? RP (type_name)? (SEMI | NEWLINE); declared_statement: variables_declared | constants_declared; assign_statement: assign_lhs assign_op
 expression (SEMI | NEWLINE); assign_op: ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN | SHORT_ASSIGN; assign_lhs: ID
 more_access; more_access: | (field_access | element_access) more_access; if_statement: IF LP expression RP block_stmt ( ELSE if_statement | ELSE
 block_stmt)?; for_statement: FOR ((ID | UNDERSCORE) COMMA (ID | UNDERSCORE) SHORT_ASSIGN RANGE expression block_stmt | for_init (SEMI | NEWLINE)
 expression (SEMI | NEWLINE) for_update block_stmt | expression block_stmt); for_init: ID SHORT_ASSIGN expression | ID assign_op expression | VAR ID
 type_name? ASSIGN expression; for_update: ID assign_op expression; break_statement: BREAK (SEMI | NEWLINE); continue_statement: CONTINUE (SEMI |
 NEWLINE); return_statement: RETURN (expression? SEMI | expression? NEWLINE); call_statement: (ID | assign_lhs) LP list_expression? RP (SEMI |
 NEWLINE); block_stmt: LB NEWLINE? block_content NEWLINE? RB SEMI?; block_content: | statement block_content | NEWLINE block_content; expr_list:
 expression | expression COMMA expr_list;
 */

expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 (EQUAL | NOT_EQUAL) expression3 | expression3;
expression3:
	expression3 (LESS | LESS_OR_EQUAL | GREATER | GREATER_OR_EQUAL) expression4
	| expression4;
expression4: expression4 (ADD | SUB) expression5 | expression5;
expression5: expression5 (MUL | DIV | MOD) expression6 | expression6;
expression6: NOT expression6 | SUB expression6 | expression7;
expression7: operand more_access_expr;
more_access_expr: | (element_access | field_access | call_expr) more_access_expr;
operand: literal | ID | LP expression RP;
element_access: LSB expression RSB;
field_access: DOT ID;
call_expr: LP list_expression? RP;
literal:
	INT_LIT
	| FLOAT_LIT
	| STRING_LIT
	| TRUE
	| FALSE
	| NIL
	| typed_array_literal
	| struct_literal;
typed_array_literal: array_type LB literal_list RB;
untyped_array_literal: LB literal_list RB;
literal_list: literal_item | literal_item COMMA literal_list;
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
array_type: LSB (INT_LIT | ID) RSB more_dimensions type_name;
more_dimensions: | LSB (INT_LIT | ID) RSB more_dimensions;
type_name: INT | FLOAT | STRING | BOOLEAN | ID | array_type;
struct_literal: ID LB optional_field_list RB;
optional_field_list: | field_list;
field_list: field_init | field_init COMMA field_list;
field_init: ID COLON expression;
list_expression: expression | expression COMMA list_expression;

//========================================================== LEXER ========================================================== Keywords Keywords

// Keywords
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

fragment FLOAT_DECIMAL: [0-9]+;
fragment EXPONENT: [eE] [+-]? FLOAT_DECIMAL;

FLOAT_LIT: FLOAT_DECIMAL '.' [0-9]* EXPONENT?;

INT_LIT: DECIMAL | HEX | OCTAL | BINARY;

fragment ESC_CHAR: 'r' | 'n' | 't' | '"' | '\\';

//string char: any character except \r, \n, ", and \;
fragment STR_CHAR: ~[\r\n"\\] | '\\' ESC_CHAR;

STRING_LIT: '"' STR_CHAR* '"';

// ============== Whitespace and comments

// newline: '\r'? '\n'; if the previous token is an ID, INT_LIT, FLOAT_LIT, STRING_LIT, TRUE, FALSE, NIL, RETURN, CONTINUE, BREAK, RP, RB, RSB, then return a SEMI token;
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

//whitespace: blankspace (' '), tab ('\t'), formfeed ('\f'), carriage return ('\r');
WS: [ \t\f\r]+ -> skip;

// ================== Comments
BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;

// ================== Error tokens
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
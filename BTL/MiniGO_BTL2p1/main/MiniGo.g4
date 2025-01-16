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
// ! ---------------- PASER DEADLINE PASS 13 TEST CASE 23:59 16/1 ----------------------- */
program: ((CONST ID ASSIGN expression) | NEWLINE)+ EOF;
//TODO Literal 6.6 pdf literal: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | array_literal | struct_literal; TODO 5.2 Expressions 6 pdf
// Expressions by precedence
expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 (EQUAL | NOT_EQUAL) expression3 | expression3;
expression3:
	expression3 (LESS | LESS_OR_EQUAL | GREATER | GREATER_OR_EQUAL) expression4
	| expression4;
expression4: expression4 (ADD | SUB) expression5 | expression5;
expression5: expression5 (MUL | DIV | MOD) expression6 | expression6;
expression6: NOT expression6 | SUB expression6 | expression7; // Unary operators
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
array_literal: array_type LB list_expression? RB;
array_type: LSB INT_LIT RSB (LSB INT_LIT RSB)* type_name;
type_name: INT | FLOAT | STRING | BOOLEAN | ID;

// Struct literal
struct_literal: ID LB (field_list)? RB;
field_list: field_init (COMMA field_init)*;
field_init: ID COLON expression;

// List of expressions
list_expression: expression (COMMA expression)*;

//thêm vào cho btl2
NEWLINE: '\r'? '\n' -> skip;
COLON: ':';

//! ---------------- PARSER ----------------------- */ ! ---------------- LEXER DEADLINE PASS 13 TEST CASE 23:59 16/1 ----------------------- */ TODO
// LEXER Keywords
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
fragment DIGIT: [0-9];
fragment OCTAL_DIGIT: [0-7];
fragment OCTAL: ('0o' | '0O') [0-7]+;
fragment HEX_DIGIT: [0-9a-fA-F];
fragment HEX: ('0x' | '0X') [0-9a-fA-F]+;
fragment DECIMAL: '0' | [1-9][0-9]*;
fragment DECIMAL_PART: '.' [0-9]*;
fragment BINARY_DIGIT: [01];
fragment BINARY: ('0b' | '0B') [0-1]+;
fragment EXPONENT: [eE][+-]? [0-9]+;
INT_LIT:
	DECIMAL
	| HEX {self.text = str(int(self.text,16))}
	| OCTAL {self.text = str(int(self.text,8))}
	| BINARY {self.text = str(int(self.text,2))};
FLOAT_LIT: [0-9]+ DECIMAL_PART EXPONENT? | DECIMAL_PART EXPONENT? | [0-9]+ EXPONENT;
fragment ESC_CHAR: 'b' | 'r' | 'n' | 't' | '\'' | '\\' | '"';
fragment STR_CHAR: ~[\r\n"\\] | '\\' ESC_CHAR;
STRING_LIT: '"' STR_CHAR* '"' { self.text = self.text[1:-1] };
// STRING_LIT: '"' (~[\n\\"] | '\\' [bfrnt'\\] | '\'"')* '"' {self.text = self.text[1:-1]}; Comments
WS: [ \t\r\n\f]+ -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;
// Error handling
UNCLOSE_STRING:
	'"' STR_CHAR* ([\r\n] | EOF) {
        if self.text[-1] in ['\r','\n']: #nếu kết thúc bằng dấu xuống dòng thì cắt dấu xuống dòng
            self.text = self.text[1:-1]
        else: #nếu kết thúc bằng EOF thì lấy từ đầu chuỗi đến hết
            self.text = self.text[1:]
        raise UncloseString(self.text)
    };
ILLEGAL_ESCAPE:
	'"' (STR_CHAR* '\\' ~[brnt'"\\] STR_CHAR*) {  #nếu có kí tự escape không hợp lệ (không phải \b, \r, \n, \t, \', \", \\)
    illegal_str = str(self.text)
    i = illegal_str.find('\\') #tìm vị trí xuất hiện đầu tiên của kí tự escape
    while i != -1 and illegal_str[i+1] in 'brnt\'"\\': #hợp lệ thì tìm tiếp
        i = illegal_str.find('\\', i+2)
    raise IllegalEscape(illegal_str[1:i+2])
};
ERROR_CHAR: . {raise ErrorToken(self.text)};
//! ---------------- LEXER ----------------------- */
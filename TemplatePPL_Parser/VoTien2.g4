grammar VoTien;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

//! -------------------------- Lexical structure ----------------------- //
// TODO KeyWord
fragment CHAR: [a-zA-Z];
KEYWORD: CHAR+;
INT: 'int';
PRINT: 'print';

// TODO Operators
ADD: '+';
SUB: '-';
MUL: '*';
POW: '**';
HASH: '#';
EQUAL: '=';
LT: '<';
GT: '>';
ASSIGNI: '<-';

// TODO Separators
LB: '{';
RB: '}';
LSB: '[';
RSB: ']';
LP: '(';
RP: ')';
CM: ',';
CL: ':';
COMCOMMA: ';';

// TODO Identifiers
ID: [a-zA-Z_@][a-zA-Z0-9_]*;

//Number Literals: số thực
NUMBER_LIT: DIGITS OPT_FRAC OPT_EXP;
fragment DIGIT: [0-9];
fragment DIGITS: DIGIT+;
fragment OPT_FRAC: ('.' DIGIT*)?;
fragment OPT_EXP: ([Ee] [+-]? DIGITS)?;

//String Literals
STRING_LIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1] };

fragment STR_CHAR: ~[\n\\"] | ESC_SEQ;
//mean [\n, \\, "], ký tự ko được chấp nhận hoặc \ được kết hợp trong mô tả ESC_SEQ

fragment ESC_SEQ: '\\' [bfrnt'\\] | '\\"';
//mean \b \f \r \n \t \' \\ and \"
fragment ESC_ILLEGAL: '\\' ~[bfrnt'\\];

// TODO Literal
INT_LIT: [0-9]+;

// TODO SKIP
COMMENTS: '//' ~[\n]* -> skip;
BLOCK_COMMENTS: '/*' (.)*? '*/' ~[\n]* -> skip;
WS: [ \t\r\f\b\n]+ -> skip; // skip spaces, tabs, ...

// TODO ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' STR_CHAR* ('\r\n' | '\n' | EOF) {
	if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
		raise UncloseString(self.text[1:-2])
	elif (self.text[-1] == '\n'):
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL {
	raise IllegalEscape(self.text[1:])
};

//!  -------------------------- end Lexical structure ------------------- //

// //! --------------------------  parser structure ----------------------- //

// declared
program: statement+ EOF;

//  Statements
statement: (declaration_statement | call_statement);
declaration_statement: INT ID ASSIGNI expression COMCOMMA;
call_statement: PRINT LP expression RP COMCOMMA;

// Expression
expression: expression1 ADD expression | expression1;
expression1: ID | INT_LIT;

// //! -------------------------- end  parser structure ----------------------- //
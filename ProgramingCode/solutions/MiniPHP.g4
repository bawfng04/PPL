grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// Parser Rules
program: vardecl* EOF;

vardecl: VARNAME EQ expr SEMI;

expr:
	expr DSTAR expr					# powerExpr
	| expr DOT expr					# concatExpr
	| expr (MUL | DIV | MOD) expr	# mulDivModExpr
	| expr (ADD | SUB) expr			# addSubExpr
	| expr DQUES expr				# nullCoalesceExpr
	| LP expr RP					# parenExpr
	| array							# arrayExpr
	| VARNAME						# varExpr
	| INTLIT						# intLitExpr
	| FLOATLIT						# floatLitExpr
	| STRINGLIT						# stringLitExpr;

array:
	ARRAY LP (expr (COMMA expr)*)? RP	# indexedArray
	| ARRAY LP (pair (COMMA pair)*)? RP	# associativeArray;

pair: VARNAME ARROW expr;

// Lexer Rules
ARRAY: 'array';
DSTAR: '**';
DOT: '.';
MUL: '*';
DIV: '/';
MOD: '%';
ADD: '+';
SUB: '-';
DQUES: '??';
LP: '(';
RP: ')';
EQ: '=';
SEMI: ';';
COMMA: ',';
ARROW: '=>';

VARNAME: [a-zA-Z_][a-zA-Z0-9_]*;
INTLIT: [0-9]+;
FLOATLIT: [0-9]+ '.' [0-9]* | '.' [0-9]+;
STRINGLIT: '\'' (~['] | '\'\'')* '\'' {self.text = self.text[1:-1]};

WS: [ \t\r\n]+ -> skip;
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
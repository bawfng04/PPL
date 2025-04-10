 # 1 grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
program: (expr NEWLINE)* EOF;

ID: [a-z][a-z0-9]*;

expr: expr ('*' | '/') expr | expr ('+' | '-') expr | '(' expr ')';
NEWLINE: [\r\n]+;

STRINGLIT: '\'' (~['] | '\'\'')* '\'' {self.text = self.text[1:-1]};

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;

# 2 grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
program: (expr NEWLINE)* EOF;

REAL: ([0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)?) | ([0-9]+ [eE] [+-]? [0-9]+);

expr: expr ('*' | '/') expr | expr ('+' | '-') expr | '(' expr ')';
NEWLINE: [\r\n]+;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;

# 3 grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: (expr NEWLINE)* EOF;
expr: expr ('*' | '/') expr | expr ('+' | '-') expr | '(' expr ')';
NEWLINE: [\r\n]+;

REAL: ([0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)?) | ([0-9]+ [eE] [+-]? [0-9]+);

STRING: '\'' ( ~('\'' | '\r' | '\n') | '\'\'')* '\'';

WS: [ \t\r\n]+ -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
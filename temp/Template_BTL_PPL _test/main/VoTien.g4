grammar VoTien;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

//! -------------------------- Lexical structure ----------------------- // TODO KeyWord and
// Operators and Separators
INT: 'int';
ADD: '+';
ASSIGNI: '=';
PRINT: 'print';
LP: '(';
RP: ')';
COMCOMMA: ';';

// TODO Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// TODO Literal
INT_LIT: [0-9]+;

// TODO SKIP
COMMENTS: '##' ~[\n]* -> skip; // Comments
WS: [ \t\r\f\b\n]+ -> skip; // skip spaces, tabs

// TODO ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};

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
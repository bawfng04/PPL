grammar VoTien;

@lexer::header {
from lexererr import *
}

options {
    language = Python3;
}

//! -------------------------- Lexical structure ----------------------- Keyword and Operators and Separators
INT: 'int';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
EXP: '**';
ASSIGNI: '=';
LP: '(';
RP: ')';
CM: ',';
SEM: ';';

// Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Literal
INT_LIT: [0-9]+;

// SKIP
COMMENTS: '##' ~[\n]* -> skip; // Comments
WS: [ \t\r\f\b\n]+ -> skip; // skip spaces, tabs

// ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};

//!  -------------------------- end Lexical structure ------------------- //

//! --------------------------  parser structure ----------------------- //
program: stm+ EOF;

stm: declaration | assignment;

declaration: INT var_decl_list SEM;

assignment: var_list ASSIGNI expr_list SEM;

var_decl_list: var_list (ASSIGNI expr_list)?;

var_list: ID (CM ID)*;

expr_list: expression (CM expression)*;

expression: term ((ADD | SUB) term)*;

term: factor ((MUL | DIV) factor)*;

/* Only allow a single exponent operator in factor */
factor: primary (EXP primary)?;

primary: INT_LIT | ID | LP expression RP;

//! -------------------------- end  parser structure ----------------------- //
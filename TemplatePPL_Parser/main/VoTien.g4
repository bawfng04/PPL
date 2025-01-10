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

// //! --------------------------  parser structure ----------------------- //

// declared

program: stm+ EOF;

stm: declarationStm | assignmentStm;

declarationStm: INT var_decl_list SEM;

var_decl_list: single_decl | multiple_decl;

single_decl: ID (ASSIGNI expression)?;

multiple_decl: ID CM ID (CM ID)* (ASSIGNI expr_list)?;

assignmentStm: single_assign | multiple_assign;

single_assign: ID ASSIGNI expression SEM;

multiple_assign: ID CM ID (CM ID)* ASSIGNI expr_list SEM;

expr_list: expression (CM expression)*;

expression: term ((ADD | SUB) term)*;

term: factor ((MUL | DIV) factor)*;

factor: primary (EXP primary)?;

primary: ID | INT_LIT | LP expression RP;

// //! -------------------------- end  parser structure ----------------------- //
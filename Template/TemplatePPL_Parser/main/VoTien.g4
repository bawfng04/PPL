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
COMMENTS: '##' ~[\n]* -> skip;	// Comments
WS: [ \t\r\f\b\n]+ -> skip;		// skip spaces, tabs

// ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};

//!  -------------------------- end Lexical structure ------------------- //

// //! --------------------------  parser structure ----------------------- //

// declared

program: stm+ EOF;

stm: declarationStm | assignmentStm; //một câu lệnh có thể là khai báo hoặc gán

declarationStm: INT var_decl_list SEM;

var_decl_list: single_decl | multiple_decl;

single_decl: ID (ASSIGNI expression)?; //a; 	a = 10;

multiple_decl: ID CM ID (CM ID)* (ASSIGNI expr_list)?; //	 a, b, c; 	a, b, c = 1, 2, 3;

assignmentStm:
	single_assign
	| multiple_assign; //một câu gán có thể là gán một biến hoặc nhiều biến

single_assign: ID ASSIGNI expression SEM; //a = 10;

multiple_assign: ID CM ID (CM ID)* ASSIGNI expr_list SEM; // a, b, c = 10, 20, 30;

expr_list: expression (CM expression)*;

expression: term ((ADD | SUB) term)*;

term: factor ((MUL | DIV) factor)*;

factor: primary (EXP primary)?;

primary: ID | INT_LIT | LP expression RP; //x;		10;		(x+5);

// //! -------------------------- end  parser structure ----------------------- //
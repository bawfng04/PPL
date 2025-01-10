grammar VoTien;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

//! -------------------------- Lexical structure ----------------------- // TODO KeyWord and



// Keywords
T: 'T';
F: 'F';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
FOR: 'for';
BOOL: 'bool';
NUMBER: 'number';
RETURN: 'return';
STRING: 'string';
FUNC: 'func';
ENDFUNC: 'endfunc';
CALL: 'call';

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
EQUAL: '=';
LT: '<';
GT: '>';
POW: '**';
HASH: '#';
ASSIGN: '<-';

// Separators
LSB: '[';
RSB: ']';
LP: '(';
RP: ')';
LB: '{';
RB: '}';
SC: ';';
COLON: ':';
CM: ',';

// Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;
IDG: '@'[a-zA-Z0-9_]+;

// Literal
INTEGER: [0-9]+;
FLOAT: [0-9]+ ('.' [0-9]*)? ([eE] [+-]? [0-9]+)?
    | [0-9]+ '.' [0-9]* ;


//STRING
STRING_LIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1] };

// SKIP
WS: [ \t\r\n]+ -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;


// ERROR

fragment STR_CHAR: ~[\n\\"] | ESC_SEQ;
fragment ESC_ILLEGAL: '\\' ~[bfrnt'\\];
fragment ESC_SEQ: '\\' [bfrnt'\\] | '\\"';

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
program: (ID | ERROR_STRING*) EOF;





// //! -------------------------- end  parser structure ----------------------- //
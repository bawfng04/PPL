grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    else:
        return super().emit();
}

options{
	language = Python3;
}

program: 'votien'+ EOF;

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
fragment HEX_DIGIT: [0-9a-fA-F];
fragment DECIMAL: '0' | [1-9][0-9]*;
fragment OCTAL: '0' [0-7]+;
fragment HEX: ('0x' | '0X') [0-9a-fA-F]+;
fragment EXPONENT: [eE][+-]? [0-9]+;
fragment DECIMAL_PART: '.' [0-9]*;

INT_LIT:
	DECIMAL
	| HEX {self.text = str(int(self.text,16))}
	| OCTAL {self.text = str(int(self.text,8))};

FLOAT_LIT: [0-9]+ DECIMAL_PART EXPONENT? | DECIMAL_PART EXPONENT? | [0-9]+ EXPONENT;

fragment ESC_CHAR: 'b' | 'r' | 'n' | 't' | '\'' | '\\' | '"'; // Remove 'f'
fragment STR_CHAR: ~[\r\n"\\] | '\\' ESC_CHAR;

STRING_LIT:
	'"' STR_CHAR* '"' {
    self.text = self.text[1:-1]
};

// Comments
WS: [ \t\r\n\f]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;

// Error handling
UNCLOSE_STRING:
	'"' STR_CHAR* ([\r\n] | EOF) {
    if self.text[-1] in ['\r','\n']:
        self.text = self.text[1:-1]
    else:
        self.text = self.text[1:]
    raise UncloseString(self.text)
};

ILLEGAL_ESCAPE:
	'"' (STR_CHAR* '\\' ~[brnt'"\\] STR_CHAR*) {
    illegal_str = str(self.text)
    i = illegal_str.find('\\')
    while i != -1 and illegal_str[i+1] in 'brnt\'"\\':
        i = illegal_str.find('\\', i+2)
    raise IllegalEscape(illegal_str[1:i+2])
};

ERROR_CHAR: . {raise ErrorToken(self.text)};
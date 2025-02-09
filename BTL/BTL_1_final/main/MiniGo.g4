grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preType = None

def emit(self):
    tk = self.type
    self.preType = tk;
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
COLON: ':';
SHORT_ASSIGN: ':=';
UNDERSCORE: '_';

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

// Literals fragment DECIMAL: '0' | [1-9][0-9]*;
fragment DECIMAL: '0' | [1-9][0-9]*;
fragment HEX: ('0x' | '0X') [0-9a-fA-F]+;
fragment OCTAL: ('0o' | '0O') [0-7]+;
fragment BINARY: ('0b' | '0B') [0-1]+;

// fragment FLOAT_DECIMAL: '0' | [1-9][0-9]*;
fragment FLOAT_DECIMAL: [0-9]+;
fragment DECIMAL_PART: '.' [0-9]*;
fragment EXPONENT: [eE] [+-]? FLOAT_DECIMAL;

INT_LIT:
	DECIMAL
	| HEX
	// { self.text = str(int(self.text,16)) }
	| OCTAL
	// { self.text = str(int(self.text,8)) }
	| BINARY;
// { self.text = str(int(self.text,2)) };

FLOAT_LIT:
	FLOAT_DECIMAL DECIMAL_PART EXPONENT?
	| FLOAT_DECIMAL EXPONENT
	| DECIMAL_PART [0-9]+ EXPONENT?
	| FLOAT_DECIMAL DECIMAL_PART;

fragment ESC_CHAR: 'r' | 'n' | 't' | '"' | '\\';
fragment STR_CHAR: ~[\r\n"\\] | '\\' ESC_CHAR;
STRING_LIT: '"' STR_CHAR* '"' { self.text = self.text[1:-1] };

// Newline + comments

// In the lexer rules section, modify the NEWLINE rule:

NEWLINE:
	'\r'? '\n' {
        if self.preType in [self.ID, self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT,
                           self.TRUE, self.FALSE, self.NIL,
                           self.RETURN, self.CONTINUE, self.BREAK,
                           self.RP, self.RB, self.RSB]:
            self.text = ';'
        else:
            self.skip()
    };

// Move the whitespace rule after NEWLINE to ensure newlines are processed first
WS: [ \t\f\r]+ -> skip;

// Comment rules should also be after NEWLINE
BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// WS: [ \t\r\n\f]+ -> skip;

// NEWLINE: '\r'? '\n' -> skip;

// LINE_COMMENT: '//' ~[\r\n]* -> skip;

// BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;

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
	'"' (STR_CHAR* '\\' ~[rnt"\\] STR_CHAR*) '"'? {
        illegal_str = str(self.text)
        i = illegal_str.find('\\')
        while i != -1 and illegal_str[i+1] in 'rnt"\\':
            i = illegal_str.find('\\', i+2)
        raise IllegalEscape(illegal_str[1:i+2])
    };

ERROR_CHAR: . {raise ErrorToken(self.text)};
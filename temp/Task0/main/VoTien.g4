grammar VoTien;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

//! -------------------------- Lexical structure ----------------------- // TODO KeyWord and


// TODO Identifiers
ID: (.)((.)(.))*;

// TODO ERROR
ERROR_STRING: (.)* {raise ErrorToken(self.text)};

//!  -------------------------- end Lexical structure ------------------- //

// //! --------------------------  parser structure ----------------------- //

// declared
program: (ID | ERROR_STRING*) EOF;


// //! -------------------------- end  parser structure ----------------------- //

class ErrorToken(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
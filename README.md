# Principles of Programming Languages - MiniGo Compiler Project

## Overview
This repository contains assignments, resources, and code for the Principles of Programming Languages (PPL) course, focused on building a compiler for MiniGo, a simplified version of the Go programming language.

## About MiniGo
MiniGo is a teaching language designed for students to practice building a compiler within a limited timeframe. It retains core concepts of Go such as basic data types, structs, and interfaces, but removes more complex features like goroutines and channels. The simplified structure allows students to focus on fundamental concepts of programming language implementation.

## Project Structure
The project is divided into 4 main assignments:

1. **Lexer & Recognizer:** Implementing lexical analysis and parsing.
2. **AST Generation:** Constructing an Abstract Syntax Tree from the parse tree.
3. **Static Checker:** Performing static semantic analysis on the AST.
4. **Code Generation** Generating target code from the semantically checked AST.

## Repository Structure
```
.
├── Assignments/           # Assignment specifications and starter code
│   ├── Assignment 1/              # Assignment 1 (Lexer and Parser)
│   ├── Assignment 2/              # Assignment 2 (AST Generation)
│   └── Assignment 3/              # Assignment 3 (Type Checking and Code Generation)
│   └── Assignment 4/              # Assignment 4 (Code Generation)
│   └── votien/                    # Votien's courses
├── Lectures/              # Course lecture materials
├── Exams/                 # Midterm and final exam materials
└── ProgramingCode/        # Programing code template and solutions
```

## Development Environment Setup
1. Install Python 3.12 from https://www.python.org/
2. Download ANTLR 4.9.2 (antlr-4.9.2-complete.jar) from https://www.antlr.org/download.html
3. Set an environment variable ANTLR_JAR pointing to the jar file
4. Install the Python ANTLR runtime:
   ```
   pip install antlr4-python3-runtime==4.9.2
   ```

## Assignment Details

### Assignment 1: Lexer & Recognizer (30%)

* **Goal:** To define the lexical rules (tokens) and grammar rules for the MiniGo language and implement a lexer and parser using ANTLR.
* **Tasks:**
  * Define tokens and handle lexical errors (ErrorToken, UnclosedString, IllegalEscapeInString) in `MiniGo.g4`.
  * Define the context-free grammar for MiniGo in `MiniGo.g4`.
  * Create test cases (`LexerSuite.py`, `ParserSuite.py`) to validate the lexer and parser.
* **Key Files:**
  * `src/main/minigo/parser/MiniGo.g4`: ANTLR grammar file containing lexer and parser rules.
  * `src/test/LexerSuite.py`: Test cases for the lexer.
  * `src/test/ParserSuite.py`: Test cases for the parser.

### Assignment 2: AST Generation (30%)

* **Goal:** To automatically generate an Abstract Syntax Tree (AST) from the parse tree produced by the ANTLR parser (from Assignment 1).
* **Tasks:**
  * Implement the `ASTGeneration` visitor (in `ASTGenerator.py`) to traverse the parse tree.
  * Construct AST nodes using the predefined classes in `AST.py`.
  * Ensure the generated AST accurately represents the structure of the MiniGo source code.
  * Create test cases (`ASTGenSuite.py`) to verify the AST structure for various MiniGo programs.
* **Key Files:**
  * `src/main/minigo/astgen/ASTGenerator.py`: Python code using the Visitor pattern to build the AST.
  * `src/main/minigo/utils/AST.py`: Predefined classes representing the nodes of the AST (Not modified).
  * `src/main/minigo/utils/Visitor.py`: Base Visitor class (Used in assignment 2 & 3).
  * `src/test/ASTGenSuite.py`: Test cases for AST generation.
  * `src/main/minigo/parser/MiniGo.g4`: (updated from assignment 1).

### Assignment 3: Static Checker (30%) ☠️

* **Goal:** To implement a static semantic checker that analyzes the AST (from Assignment 2) for semantic errors according to MiniGo's rules.
* **Tasks:**
  * Implement the `StaticChecker` visitor (in `StaticCheck.py`) to traverse the AST.
  * Perform checks for:
    * Redeclarations (variables, constants, functions, types, parameters, fields, methods, prototypes within the same scope).
    * Undeclared identifiers (variables, functions, types, fields, methods).
    * Type mismatches in expressions, assignments, function calls, return statements, loop conditions, etc.
    * Function/method call argument compatibility.
    * Field access validity.
    * Array indexing validity.
  * Raise specific exceptions defined in `StaticError.py` upon detecting errors.
  * Create test cases (`CheckSuite.py`) covering various semantic rules and error conditions.
* **Key Files:**
  * `src/main/minigo/checker/StaticCheck.py`: Python code implementing the static semantic checks using the Visitor pattern.
  * `src/main/minigo/checker/StaticError.py`: Definitions for semantic error exceptions.
  * `src/test/CheckSuite.py`: Test cases for the static checker.
  * `src/main/minigo/utils/AST.py`: AST definitions (Input for the checker).

### Assignment 4: Code Generation (10%)

* **Goal:** To generate target code (e.g., Jasmin bytecode for the Java Virtual Machine) from the semantically checked AST (from Assignment 3).
* **Tasks:**
  * Implement the `CodeGenerator` visitor (in `CodeGenerator.py`) to traverse the AST.
  * Generate appropriate target code instructions for MiniGo constructs (declarations, expressions, statements, function calls, etc.).
  * Manage memory allocation, stack frames, and control flow in the target code.
  * Create test cases (`CodeGenSuite.py`) to verify the correctness of the generated code for various MiniGo programs.
* **Key Files:**
  * `src/main/minigo/codegen/CodeGenerator.py`: Python code implementing the code generation logic using the Visitor pattern.
  * `src/main/minigo/utils/AST.py`: AST definitions (Input for the code generator).
  * `src/main/minigo/utils/Visitor.py`: Base Visitor class.
  * `src/test/CodeGenSuite.py`: Test cases for code generation.
  * `src/main/minigo/utils/MachineCode.py`: Helper classes/functions for generating target code instructions.

## Running the Code
The template files include a run.py script with various commands:

```
python run.py gen     # Generate ANTLR parser
python run.py test    # Run test suites
python run.py clear   # Clear generated files
```

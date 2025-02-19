# Workspace Overview

This repository contains multiple directories and files for working with MiniGo (a simplified Go-like language) and related ANTLR-based components. It includes sample assignments, ANTLR grammar definitions, test scripts, Docker configurations, and various template references for building, testing, and running MiniGo code.

## Main Directories

- **BTL/**: Contains assignment phases with MiniGo grammar and other code, such as:
  - **BTL/BTL1/**: Contains phases 1, 2, and 3 of MiniGo assignments.
    - **MiniGo.g4**: The ANTLR grammar for the MiniGo language.
  - **BTL/BTL2/**: Contains phase 1 of MiniGo assignments.
- **Lecture/**: Lecture-related references (if any).
- **Template/**: Template projects for Lexer and Parser, such as TemplatePPL_Lexer and TemplatePPL_Parser.
- **temp/**: Tasks and sample scripts. Includes Dockerfiles, test environments, and Python scripts, for example `run.py`.

## Environment Setup

1. Install Java (JDK).
2. Install Python 3.12 or above.
3. Set an environment variable named `ANTLR_JAR` pointing to your `antlr-4.9.2-complete.jar` file.
4. (Optional) Use Docker by referring to Dockerfile or Dockerfile.

## How to Build / Run

Several `run.py` files exist in different directories (for example, `run.py` or `temp/Task0/run.py`) with similar usage patterns:

```sh
python3 run.py gen                             # Generate required files
python3 run.py test LexerSuite [test_case]     # Run LexerSuite tests
python3 run.py test ParserSuite [test_case]    # Run ParserSuite tests
python3 run.py test ASTGenSuite [test_case]    # Run ASTGenSuite tests
python3 run.py test CheckerSuite [test_case]   # Run CheckerSuite tests
python3 run.py test CodeGenSuite [test_case]   # Run CodeGenSuite tests
```

If a specific [test_case] is provided (e.g., test_1), only that test runs; otherwise, all tests in the suite are executed.

## Docker Usage

Dockerfiles are provided in temp/Task0/Docker-Ubuntu and temp/Task0/temp. For example:

```sh
# Build the Docker image
docker build -t my-ubuntu-app .

# Run the container
docker run my-ubuntu-app
```

Refer to the comments in each Dockerfile for additional instructions (like installing dependencies or sending emails).

## Additional Notes

- Various assignment instructions are found in text files like assignment1.txt.
- The ANTLR grammar for the MiniGo language (e.g., MiniGo.g4) defines tokens and structures for parsing and lexing MiniGo code.
- Tests are organized by suites (LexerSuite, ParserSuite, ASTGenSuite, CheckerSuite, CodeGenSuite).
- For questions about contributing or building, see the run.py scripts or the comments within each directory.

## Ex

Giả sử chúng ta có một chương trình MiniGo đơn giản như sau:

```
    var x = 10;
    func main() {
        var y = 20;
    }
```

Cây phân tích cú pháp (parse tree) cho chương trình này sẽ trông như sau:

```
    program
    ├── newlines
    ├── declared (variables_declared)
    │   └── var_decl (x, 10)
    ├── more_declared
    │   └── declared (function_declared)
    │       └── func_decl (main, [], Block)
    │           └── block_stmt
    │               └── block_content
    │                   └── statement (variables_declared)
    │                       └── var_decl (y, 20)
    ├── newlines
    └── EOF
```

Hàm visitProgram sẽ chuyển đổi cây phân tích cú pháp này thành cây cú pháp trừu tượng (AST) như sau:

```
Program
  ├── VarDecl (x, IntType, 10)
  └── FuncDecl (main, [], VoidType, Block
        └── VarDecl (y, IntType, 20)
      )
```

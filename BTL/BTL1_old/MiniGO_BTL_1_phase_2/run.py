"""
 * Initial code for Assignment 1, 2
 * file : run.py
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025

 * install extension ANTLR4 grammar syntax support, Better Comments
 * run code
    Usage:
    python3 run.py gen                            # Generate required files
    python3 run.py test LexerSuite [test_case]    # Run LexerSuite tests (test_case is optional)
    python3 run.py test ParserSuite [test_case]   # Run ParserSuite tests (test_case is optional)
    python3 run.py test ASTGenSuite [test_case]   # Run ASTGenSuite tests (test_case is optional)

    Notes:
    - Replace [test_case] with the specific test you want to run, e.g., test_1.
    - If [test_case] is not provided, all tests in the suite will be executed.
"""

import sys
import os
import subprocess
import unittest
import shutil
from antlr4 import *
from colorama import Fore, Style, init

for path in ['./test/', './test/Lexer/', './test/Parser/', './test/ASTGen/',  './test/Check/', './test/CodeGen/',  './main/']:
    sys.path.append(path)

# load_dotenv()
ANTLR_JAR = os.getenv('ANTLR_JAR', "antlr-4.9.2-complete.jar")
TARGET_DIR = 'target/main'
GENERATE_DIR = 'main/parser'
ARGV = ""

def main(argv):

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        # java -jar ../libs/antlr/antlr-4.9.2-complete.jar -o target -no-listener -visitor main/MT22.g4
        subprocess.run(["java", "-jar", ANTLR_JAR, "-o", "target",
                       "-no-listener", "-visitor", "main/MiniGo.g4"])
    elif argv[0] == 'clear':
        folders = ["ASTGen/input", "ASTGen/output",
                  "Check/input", "Check/output",
                  "CodeGen/input", "CodeGen/output",
                  "Lexer/input", "Lexer/output",
                  "Parser/input", "Parser/output"]

        folder_pycache = ["main", "target/main", "target", "test", 'test/Lexer/', 'test/Parser/', 'test/ASTGen/',  'test/Check/', 'test/CodeGen/']
        for folder in folder_pycache:
            folder_path = folder + "/__pycache__"
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
        if os.path.exists("target/main"):
            shutil.rmtree("target/main")

        for folder in folders:
            folder_path = "test/" + folder

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            else:
                files = os.listdir(folder_path)
                for file in files:
                    file_path = os.path.join(folder_path, file)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print(f'Failed to delete {file_path}. Reason: {e}')

        print("Clear full file input/ouput in test")
    elif argv[0] == 'test':
        if not os.path.isdir(TARGET_DIR):
            subprocess.run(["java", "-jar", ANTLR_JAR, "-o", "target",
                       "-no-listener", "-visitor", "main/MiniGo.g4"])
        if not (TARGET_DIR) in sys.path:
            sys.path.append(TARGET_DIR)
            sys.path.append("target")
        if len(argv) < 2:
            printUsage()
        if len(argv) == 2:
            if argv[1] == 'LexerSuite':
                from LexerSuite import LexerSuite
                getAndTest(argv[1], LexerSuite)
            elif argv[1] == 'ParserSuite':
                from ParserSuite import ParserSuite
                getAndTest(argv[1], ParserSuite)
            elif argv[1] == 'ASTGenSuite':
                from ASTGenSuite import ASTGenSuite
                getAndTest(argv[1], ASTGenSuite)
            else:
                printUsage()
        else:
            if argv[1] == 'LexerSuite':
                from LexerSuite import LexerSuite
                getAndTestFucntion(argv[1] + " - " + argv[2], LexerSuite, argv[2])
            elif argv[1] == 'ParserSuite':
                from ParserSuite import ParserSuite
                getAndTestFucntion(argv[1] + " - " + argv[2], ParserSuite, argv[2])
            elif argv[1] == 'ASTGenSuite':
                from ASTGenSuite import ASTGenSuite
                getAndTestFucntion(argv[1] + " - " + argv[2], ASTGenSuite, argv[2])
            else:
                printUsage()
    else:
        printUsage()


def getAndTest(argv, cls):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(cls)
    test(argv, suite)

def getAndTestFucntion(argv, cls, nameFunction):
    suite = unittest.TestSuite()
    suite.addTest(cls(nameFunction))
    test(argv, suite)

def generate_repeating_sequence(size):
    base_sequence = "1234567890"
    repeated_sequence = (base_sequence * ((size // len(base_sequence)) + 1))[:size]
    return repeated_sequence

def printMiniGo(argv, stream, result):
    print("----------------------------------------------------------------------")
    print(f'{Fore.RED}{argv} - Assignment- PPL - HK242 - VO TIEN{Style.RESET_ALL} ')
    print(f'{Fore.GREEN}Vo Tien{Style.RESET_ALL} : {Fore.BLUE}https://www.facebook.com/Shiba.Vo.Tien{Style.RESET_ALL}')
    print(f'Tests run: {Fore.MAGENTA}{result.testsRun}{Style.RESET_ALL}')

    stream.seek(0)
    expect = stream.readline()
    print(generate_repeating_sequence(len(expect) - 1))

    styled_expect = ''.join(
        f"{Fore.RED}{c}{Style.RESET_ALL}" if c == 'E' else
        f"{Fore.YELLOW}{c}{Style.RESET_ALL}" if c == 'F' else
        f"{Fore.GREEN}{c}{Style.RESET_ALL}" if c == '.' else c
        for c in expect
    )
    print(styled_expect, end='')

    listErrors = []
    listFailures = []
    for i in range(1, len(expect)):
        if expect[i - 1] == 'E': listErrors.append(i)
        elif expect[i - 1] == 'F': listFailures.append(i)

    errors_str = ", ".join(map(str, listErrors))
    failures_str = ", ".join(map(str, listFailures))

    if len(listFailures) + len(listErrors):
        Pass = 100.0 * (1 - (len(listFailures) + len(listErrors)) / (len(expect) - 1))
        print(f"\n{Fore.GREEN}Pass     : {Pass:.2f} %{Style.RESET_ALL}")
        print(f"{Fore.RED}Errors   : {errors_str}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Failures : {failures_str}{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}Pass full 10.{Style.RESET_ALL}")
    print("----------------------------------------------------------------------")

def test(argv, suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())
    printMiniGo(argv, stream, result)


def printUsage():
    print("Usage:")
    print("  python3 run.py gen                            # Generate required files")
    print("  python3 run.py test LexerSuite [test_case]    # Run LexerSuite tests (test_case is optional)")
    print("  python3 run.py test ParserSuite [test_case]   # Run ParserSuite tests (test_case is optional)")
    print("  python3 run.py test ASTGenSuite [test_case]   # Run ASTGenSuite tests (test_case is optional)")
    print()
    print("Notes:")
    print("  - Replace [test_case] with the specific test you want to run, e.g., test_1.")
    print("  - If [test_case] is not provided, all tests in the suite will be executed.")


if __name__ == "__main__":
    main(sys.argv[1:])
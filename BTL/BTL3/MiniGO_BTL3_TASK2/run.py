"""
 * Initial code for Assignment 3
 * file : run.py
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
 
 * install extension ANTLR4 grammar syntax support, Better Comments
 * run code
    Usage:
    python3 run.py test CheckSuite [test_case]   # Run CheckSuite tests (test_case is optional)

    Notes:
    - Replace [test_case] with the specific test you want to run, e.g., test_1.
    - If [test_case] is not provided, all tests in the suite will be executed.
"""

import sys
import unittest
from antlr4 import *
from colorama import Fore, Style, init

def main(argv):
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'test' and argv[1] == 'CheckSuite':
        if len(argv) == 2:
            from CheckSuite import CheckSuite
            getAndTest(argv[1], CheckSuite)
        else:
            from CheckSuite import CheckSuite
            getAndTestFucntion(argv[1] + " - " + argv[2], CheckSuite, argv[2])
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
    print("  python3 run.py test CheckSuite [test_case]   # Run CheckSuite tests (test_case is optional)")
    print()
    print("Notes:")
    print("  - Replace [test_case] with the specific test you want to run, e.g., test_1.")
    print("  - If [test_case] is not provided, all tests in the suite will be executed.")


if __name__ == "__main__":
    main(sys.argv[1:])
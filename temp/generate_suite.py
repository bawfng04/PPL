import re
import os

def generate_checksuite(input_txt_file, output_py_file):
    """
    Generates CheckSuite.py from testcase.txt format.

    Args:
        input_txt_file (str): Path to the input testcase.txt file.
        output_py_file (str): Path to the output CheckSuite.py file.
    """

    try:
        with open(input_txt_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_txt_file}'")
        return
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    # Split content into test case blocks using "Test Case:" as a delimiter
    # Keep the delimiter by using a capturing group in re.split
    test_blocks = re.split(r'(Test Case: test_\d+\n)', content)

    generated_methods = []

    # Start from index 1 because split will likely have an empty string at the beginning
    # Iterate in steps of 2 (delimiter, block content)
    for i in range(1, len(test_blocks), 2):
        test_name_line = test_blocks[i].strip()
        block_content = test_blocks[i+1]

        # Extract test name
        match_name = re.match(r'Test Case: (test_\d+)', test_name_line)
        if not match_name:
            print(f"Warning: Could not parse test name from '{test_name_line}'")
            continue
        test_name = match_name.group(1)

        # Extract AST Input line
        ast_input_line = None
        match_ast = re.search(r'^\s*Program\(.*\)\s*$', block_content, re.MULTILINE)
        if match_ast:
            ast_input_line = match_ast.group(0).strip()
        else:
            print(f"Warning: Could not find AST 'Program(...)' line for {test_name}")
            continue # Skip if AST is missing

        # Extract Expected Output
        expected_output = "VOTIEN" # Default if not found
        match_expect = re.search(r'# Expected Output:\n(.*?)\n', block_content, re.DOTALL)
        if match_expect:
            expected_output = match_expect.group(1).strip()
            # Handle potential quotes already present in the expected output
            if (expected_output.startswith('"') and expected_output.endswith('"')) or \
               (expected_output.startswith("'") and expected_output.endswith("'")):
                # It's likely already quoted, keep as is but might need adjustment
                # For simplicity, we'll re-quote it safely later
                pass # Keep the content for now
            # Escape backslashes and double quotes for Python string literal
            expected_output = expected_output.replace('\\', '\\\\').replace('"', '\\"')


        # Generate the Python method code
        # Using f-string with triple quotes for the AST part helps with quoting
        method_code = f"""
    def {test_name}(self):
        input = {ast_input_line}
        expect = "{expected_output}" # Ensure output is double-quoted
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
"""
        generated_methods.append(method_code)

    # Assemble the final CheckSuite.py content
    output_content = f"""import unittest
from TestUtils import TestChecker
from AST import * # Import all AST node types
import inspect

class CheckSuite(unittest.TestCase):
{''.join(generated_methods)}

# Optional: Add if __name__ == '__main__' block if needed
# if __name__ == '__main__':
#     unittest.main()
"""

    try:
        with open(output_py_file, 'w', encoding='utf-8') as outfile:
            outfile.write(output_content)
        print(f"Successfully generated '{output_py_file}' with {len(generated_methods)} test cases.")
    except Exception as e:
        print(f"Error writing output file: {e}")

# --- Main execution ---
if __name__ == "__main__":
    input_file = "testcase.txt"  # Make sure this file exists
    output_file = "CheckSuite.py"
    generate_checksuite(input_file, output_file)
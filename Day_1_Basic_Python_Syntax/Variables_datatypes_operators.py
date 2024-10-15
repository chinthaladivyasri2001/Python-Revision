"""
Day 1: Variables, Data Types, and Operators

This module covers the basics of variables, data types, and operators in Python.
Understanding these fundamentals is essential for writing effective and efficient Python code.
"""

# Variables and Data Types
integer_var = 10          # An integer variable
float_var = 3.14          # A floating-point variable
string_var = "Hello, Python!"  # A string variable
bool_var = True           # A boolean variable

# Printing Variables using f-strings for formatted output
print(f"Integer: {integer_var}")   # Output: Integer: 10
print(f"Float: {float_var}")       # Output: Float: 3.14
print(f"String: {string_var}")     # Output: String: Hello, Python!
print(f"Boolean: {bool_var}")      # Output: Boolean: True

# Displaying the data types of each variable using the type() function
print(f"Type of integer_var: {type(integer_var)}")  # Output: <class 'int'>
print(f"Type of float_var: {type(float_var)}")      # Output: <class 'float'>
print(f"Type of string_var: {type(string_var)}")    # Output: <class 'str'>
print(f"Type of bool_var: {type(bool_var)}")        # Output: <class 'bool'>

# Operators
# Arithmetic Operators: Perform mathematical operations
a = 15
b = 4
print(f"a + b = {a + b}")   # Addition: 15 + 4 = 19
print(f"a - b = {a - b}")   # Subtraction: 15 - 4 = 11
print(f"a * b = {a * b}")   # Multiplication: 15 * 4 = 60
print(f"a / b = {a / b}")   # Division: 15 / 4 = 3.75
print(f"a // b = {a // b}") # Floor Division: 15 // 4 = 3
print(f"a % b = {a % b}")   # Modulus: 15 % 4 = 3
print(f"a ** b = {a ** b}") # Exponentiation: 15 ** 4 = 50625

# Comparison Operators: Compare two values and return a boolean result
print(f"a == b: {a == b}")  # Equal to: False
print(f"a != b: {a != b}")  # Not equal to: True
print(f"a > b: {a > b}")    # Greater than: True
print(f"a < b: {a < b}")    # Less than: False
print(f"a >= b: {a >= b}")  # Greater than or equal to: True
print(f"a <= b: {a <= b}")  # Less than or equal to: False

# Logical Operators: Combine conditional statements
c = True
d = False
print(f"c and d: {c and d}")  # Logical AND: False
print(f"c or d: {c or d}")    # Logical OR: True
print(f"not c: {not c}")      # Logical NOT: False

# Assignment Operators: Assign values to variables
e = 5
e += 3  # Equivalent to e = e + 3
print(f"e after += 3: {e}")  # Output: e after += 3: 8

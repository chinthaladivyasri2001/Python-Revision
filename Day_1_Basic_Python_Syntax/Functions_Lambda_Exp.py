"""
Day 1: Functions and Lambda Expressions

This module covers defining and using functions, as well as lambda expressions in Python.
Functions promote code reusability and modularity, while lambda expressions provide
a concise way to create small, anonymous functions.
"""

# Defining a Simple Function
def greet(name):
    """
    Greets the person with the provided name.

    Args:
        name (str): The name of the person.

    Returns:
        str: Greeting message.
    """
    return f"Hello, {name}!"

# Using the Function
message = greet("Alice")
print(message)  # Output: Hello, Alice!

# Function with Multiple Parameters
def add(a, b):
    """
    Adds two numbers and returns the result.

    Args:
        a (int/float): The first number.
        b (int/float): The second number.

    Returns:
        int/float: The sum of a and b.
    """
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8

# Function with Default Parameters
def power(base, exponent=2):
    """
    Raises a base number to a specified exponent.

    Args:
        base (int/float): The base number.
        exponent (int/float, optional): The exponent. Defaults to 2.

    Returns:
        int/float: The result of base raised to the exponent.
    """
    return base ** exponent

print(power(4))      # Output: 16
print(power(4, 3))   # Output: 64

# Lambda Expressions
multiply = lambda x, y: x * y  # Defines an anonymous function that multiplies two numbers
print(multiply(3, 4))           # Output: 12

# Using Lambda with Higher-order Functions
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))  # Applies the lambda function to each element in numbers
print(squares)  # Output: [1, 4, 9, 16]

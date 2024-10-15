"""
Day 1: List Comprehensions

This module explores list comprehensions in Python for creating and manipulating lists efficiently.
List comprehensions provide a concise syntax for generating lists based on existing iterables.
"""

# Basic List Comprehension
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List Comprehension with Condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

# Nested List Comprehensions
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flattening a Matrix using Nested List Comprehension
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List Comprehension with Function
def uppercase(word):
    """
    Converts a word to uppercase.

    Args:
        word (str): The word to convert.

    Returns:
        str: The uppercase version of the word.
    """
    return word.upper()

words = ['hello', 'world', 'python']
upper_words = [uppercase(word) for word in words]
print(upper_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# Conditional Expressions in List Comprehensions
status = ['even' if x % 2 == 0 else 'odd' for x in range(10)]
print(status)  # Output: ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

# ============================
# List Comprehensions Examples
# ============================

# 1. Basic List Comprehension: Squares of numbers from 0 to 4
squares = [x**2 for x in range(5)]
print("Squares:", squares)  # Output: [0, 1, 4, 9, 16]

# 2. List Comprehension with a Condition: Even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print("Even Numbers:", evens)  # Output: [0, 2, 4, 6, 8]

# 3. List Comprehension with a Function
def square(x):
    return x * x

squares_func = [square(x) for x in range(5)]
print("Squares using function:", squares_func)  # Output: [0, 1, 4, 9, 16]

# 4. Nested List Comprehension: Creating a 3x3 Matrix
matrix = [[j for j in range(3)] for i in range(3)]
print("Matrix:", matrix)


# 5. List Comprehension with Multiple Conditions: Even Pairs
pairs = [(x, y) for x in range(5) for y in range(5) if x % 2 == 0 and y % 2 == 0]
print("Even Pairs:", pairs)


# =================================
# Dictionary Comprehensions Examples
# =================================

# 1. Basic Dictionary Comprehension: Mapping numbers to their squares
squares_dict = {x: x**2 for x in range(5)}
print("Squares Dictionary:", squares_dict)


# 2. Dictionary Comprehension with a Condition: Even numbers and their squares
evens_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print("Evens Dictionary:", evens_dict)

# 3. Swapping Keys and Values in a Dictionary
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {value: key for key, value in original.items()}
print("Swapped Dictionary:", swapped)


# 4. Dictionary Comprehension with Functions: Mapping words to their lengths
words = ['apple', 'banana', 'cherry']
lengths = {word: len(word) for word in words}
print("Word Lengths:", lengths)


# 5. Nested Dictionary Comprehension: Creating a Multiplication Table
multiplication_table = {x: {y: x * y for y in range(1, 4)} for x in range(1, 4)}
print("Multiplication Table:", multiplication_table)
# }

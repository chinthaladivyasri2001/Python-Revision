"""
Day 1: Loops

This module covers loops in Python: for and while loops.
Loops are used to execute a block of code repeatedly under certain conditions.
"""

# For Loop: Iterating over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"I like {fruit}")  # Outputs each fruit in the list

# For Loop: Using range()
for i in range(5):
    print(f"Number: {i}")        # Outputs numbers from 0 to 4

# While Loop: Basic example
count = 0
while count < 5:
    print(f"Count: {count}")      # Outputs count from 0 to 4
    count += 1                     # Increment count by 1

# While Loop: Using break and continue
n = 0
while True:
    n += 1
    if n == 3:
        continue                  # Skip the print statement when n is 3
    if n > 5:
        break                     # Exit the loop when n is greater than 5
    print(f"n is {n}")             # Outputs n values except when n is 3

# Nested Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")    # Outputs combinations of i and j from 1 to 3

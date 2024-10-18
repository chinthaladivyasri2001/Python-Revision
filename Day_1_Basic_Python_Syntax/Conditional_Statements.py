"""
Day 1: Conditional Statements

This module explores conditional statements in Python: if, else, and elif.
Conditional statements allow the program to make decisions based on certain conditions.
"""

# Example 1: Simple if statement
age = 17
if age >= 18:
    print("You are eligible to vote.")  # This will not be printed since age is 17

# Example 2: if-else statement
temperature = 20
if temperature > 25:
    print("It's a hot day.")          # This will not be printed since temperature is 20
else:
    print("It's a pleasant day.")     # Output: It's a pleasant day.

# Example 3: if-elif-else statement
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'                         # This block will execute since score is 85
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
print(f"Your grade is: {grade}")        # Output: Your grade is: B

# Example 4: Nested if statements
num = 3
if num > 0:
    if num % 2 == 0:
        print(f"{num} is a positive even number.")  # This will not be printed since num is 3
    else:
        print(f"{num} is a positive odd number.")   # Output: 3 is a positive odd number.
else:
    print(f"{num} is not a positive number.")

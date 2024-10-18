# numpy_element_aggregate_operations.py

"""
Element-wise and Aggregate Operations in NumPy
-----------------------------------------------
This script covers:
1. Introduction to Element-wise Operations
2. Common Element-wise Operations
3. Introduction to Aggregate Operations
4. Common Aggregate Functions
5. Practice Exercises with Explanations

Prerequisites:
- Ensure that NumPy is installed in your Python environment.
  You can install it using pip:
      pip install numpy
"""

import numpy as np

# ---------------------------------------------
# 1. Introduction to Element-wise Operations
# ---------------------------------------------
print("=== 1. Introduction to Element-wise Operations ===\n")

# Element-wise operations in NumPy allow you to perform arithmetic and other operations on arrays element by element.
# This means that operations are applied individually to each element of the arrays, making computations straightforward and efficient.

# Example of element-wise addition
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
result_add = array_a + array_b
print("Element-wise Addition:")
print(f"A: {array_a}")
print(f"B: {array_b}")
print(f"A + B: {result_add}\n")


print("=== 5. Practice Exercises ===\n")

# Exercise 1: Element-wise Operations
print("Exercise 1: Element-wise Operations\n")
"""
Tasks:
1. Create two 1D arrays: A with values [5, 10, 15] and B with values [1, 2, 3].
2. Perform element-wise addition, subtraction, multiplication, and division.
3. Calculate the square root of array A.
"""
print("Solution:")
A_ex1 = np.array([5, 10, 15])
B_ex1 = np.array([1, 2, 3])

# Element-wise operations
add_result = A_ex1 + B_ex1
sub_result = A_ex1 - B_ex1
mul_result = A_ex1 * B_ex1
div_result = A_ex1 / B_ex1
sqrt_result = np.sqrt(A_ex1)

print(f"A: {A_ex1}")
print(f"B: {B_ex1}")
print(f"A + B: {add_result}")
print(f"A - B: {sub_result}")
print(f"A * B: {mul_result}")
print(f"A / B: {div_result}")
print(f"Square root of A: {sqrt_result}\n")

# Exercise 2: Aggregate Functions
print("Exercise 2: Aggregate Functions\n")
"""
Tasks:
1. Create a 2D array C with shape (3, 4) containing values from 1 to 12.
2. Calculate the total sum, mean, minimum, and maximum of the array.
3. Calculate the sum along each axis.
"""
print("Solution:")
C_ex2 = np.arange(1, 13).reshape(3, 4)  # Creates a 3x4 array

total_sum_ex2 = np.sum(C_ex2)
mean_ex2 = np.mean(C_ex2)
min_ex2 = np.min(C_ex2)
max_ex2 = np.max(C_ex2)
sum_axis0_ex2 = np.sum(C_ex2, axis=0)
sum_axis1_ex2 = np.sum(C_ex2, axis=1)

print(f"Array C:\n{C_ex2}")
print(f"Total Sum: {total_sum_ex2}")
print(f"Mean: {mean_ex2}")
print(f"Minimum: {min_ex2}")
print(f"Maximum: {max_ex2}")
print(f"Sum along axis 0: {sum_axis0_ex2}")
print(f"Sum along axis 1: {sum_axis1_ex2}\n")

# Exercise 3: Applying Multiple Aggregate Functions
print("Exercise 3: Applying Multiple Aggregate Functions\n")
"""
Tasks:
1. Create a 1D array D with values [10, 20, 30, 40, 50].
2. Find the mean and standard deviation of the array.
"""
print("Solution:")
D_ex3 = np.array([10, 20, 30, 40, 50])
mean_ex3 = np.mean(D_ex3)
std_dev_ex3 = np.std(D_ex3)

print(f"Array D: {D_ex3}")
print(f"Mean of D: {mean_ex3}")
print(f"Standard Deviation of D: {std_dev_ex3}\n")

# ---------------------------------------------
# 6. Conclusion
# ---------------------------------------------
print("=== 6. Conclusion ===\n")
print("""
Element-wise and aggregate operations in NumPy provide powerful tools for data analysis and manipulation. 
Understanding these operations is fundamental for effective numerical computing and data science tasks.

**Key Takeaways:**
- Element-wise operations allow you to apply arithmetic and functions to each element of arrays.
- Aggregate functions condense array data into summary statistics, making it easier to analyze data.
- Common aggregate functions include sum, mean, min, max, and standard deviation.


""")
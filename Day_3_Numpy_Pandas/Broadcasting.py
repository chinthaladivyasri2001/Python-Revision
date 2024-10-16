# numpy_broadcasting.py

"""
NumPy Broadcasting
------------------
This script provides an in-depth exploration of broadcasting in NumPy, including:
1. Introduction to Broadcasting
2. Broadcasting Rules
3. Practical Broadcasting Examples
   - Adding Scalars to Arrays
   - Adding Arrays of Different Shapes
   - Multiplying Arrays with Different Shapes
   - Broadcasting in Higher Dimensions
4. Common Broadcasting Pitfalls
5. Practice Exercises with Explanations

Prerequisites:
- Ensure that NumPy is installed in your Python environment.
  You can install it using pip:
      pip install numpy
"""

import numpy as np

# ---------------------------------------------
# 1. Introduction to Broadcasting
# ---------------------------------------------
print("=== 1. Introduction to Broadcasting ===\n")

# Broadcasting is a powerful mechanism that allows NumPy to work with arrays of different shapes during arithmetic operations.
# It eliminates the need for explicit replication of data, enabling efficient and concise code.

# **Key Advantages of Broadcasting:**
# - **Memory Efficiency:** Avoids unnecessary data duplication.
# - **Performance:** Leverages optimized C routines within NumPy for fast computations.
# - **Flexibility:** Simplifies code by handling operations between arrays of different shapes seamlessly.

# ---------------------------------------------
# 2. Broadcasting Rules
# ---------------------------------------------
print("=== 2. Broadcasting Rules ===\n")

# NumPy follows specific rules to determine how arrays with different shapes are broadcasted.
# Understanding these rules is crucial to avoid unexpected behaviors.

# **Broadcasting Rules:**
# 1. **Align the arrays' shapes from the trailing (last) dimensions.**
#    - If the arrays do not have the same number of dimensions, prepend the shape of the smaller array with 1s until both shapes have the same length.
# 2. **Two dimensions are compatible for broadcasting if:**
#    - They are equal, or
#    - One of them is 1.
# 3. **The resulting array shape is the maximum size along each dimension.**

# **Example Scenarios:**

# Let's consider two arrays:
# - Array A with shape (4, 3, 2)
# - Array B with shape (3, 1)
# To make their shapes compatible:
# - Prepend 1s to the shape of B: (1, 3, 1)
# - Now, compare each dimension from the last:
#   - 2 and 1 → Compatible (1 can be broadcasted to 2)
#   - 3 and 3 → Compatible
#   - 4 and 1 → Compatible (1 can be broadcasted to 4)
# - The resulting shape after broadcasting: (4, 3, 2)

# ---------------------------------------------
# 3. Practical Broadcasting Examples
# ---------------------------------------------
print("=== 3. Practical Broadcasting Examples ===\n")

# 3.1. Adding Scalars to Arrays
print("3.1. Adding Scalars to Arrays\n")

# Adding a scalar to a NumPy array broadcasts the scalar across the array.
array_scalar_add = np.array([1, 2, 3, 4])
scalar = 10
result_add_scalar = array_scalar_add + scalar
print("Original Array:", array_scalar_add)
print("Scalar:", scalar)
print("Array + Scalar:", result_add_scalar)
print()

# 3.2. Adding Arrays of Different Shapes
print("3.2. Adding Arrays of Different Shapes\n")

# Consider two arrays of shapes (3, 1) and (1, 4)
array_a = np.array([[1], [2], [3]])  # Shape: (3, 1)
array_b = np.array([[10, 20, 30, 40]])  # Shape: (1, 4)

# Broadcasting allows us to add these arrays to get a (3, 4) array
result_add_diff_shapes = array_a + array_b
print("Array A (3x1):")
print(array_a)
print("\nArray B (1x4):")
print(array_b)
print("\nA + B (Broadcasted to 3x4):")
print(result_add_diff_shapes)
print()

# 3.3. Multiplying Arrays with Different Shapes
print("3.3. Multiplying Arrays with Different Shapes\n")

# Multiplying a (3, 1) array with a (1, 4) array
result_mul_diff_shapes = array_a * array_b
print("A (3x1):")
print(array_a)
print("\nB (1x4):")
print(array_b)
print("\nA * B (Broadcasted to 3x4):")
print(result_mul_diff_shapes)
print()

# 3.4. Broadcasting in Higher Dimensions
print("3.4. Broadcasting in Higher Dimensions\n")

# Consider a 3D array and a 1D array
array_3d = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10, 11, 12]]
])  # Shape: (2, 2, 3)

array_1d = np.array([100, 200, 300])  # Shape: (3,)

# Broadcasting the 1D array to add to the 3D array
result_broadcast_3d = array_3d + array_1d
print("3D Array:")
print(array_3d)
print("\n1D Array:")
print(array_1d)
print("\n3D Array + 1D Array (Broadcasted):")
print(result_broadcast_3d)
print()

# ---------------------------------------------
# 4. Common Broadcasting Pitfalls
# ---------------------------------------------
print("=== 4. Common Broadcasting Pitfalls ===\n")

# 4.1. Incompatible Shapes
print("4.1. Incompatible Shapes\n")

# Attempting to broadcast arrays with incompatible shapes will result in an error
array_x = np.array([1, 2, 3])
array_y = np.array([[1, 2], [3, 4]])

print("Array X Shape:", array_x.shape)
print("Array Y Shape:", array_y.shape)
try:
    result_incompatible = array_x + array_y
except ValueError as e:
    print("Error:", e)
print()

# 4.2. Unintended Broadcasting
print("4.2. Unintended Broadcasting\n")

# Be cautious when the trailing dimensions are compatible, but the leading ones are not intended
array_p = np.array([[1, 2, 3]])
array_q = np.array([[4], [5], [6]])

# This will broadcast to (3, 3), but it might not be the intended operation
result_unintended = array_p + array_q
print("Array P (1x3):")
print(array_p)
print("\nArray Q (3x1):")
print(array_q)
print("\nP + Q (Broadcasted to 3x3):")
print(result_unintended)
print()

# ---------------------------------------------
# 5. Practice Exercises
# ---------------------------------------------
print("=== 5. Practice Exercises ===\n")

# Exercise 1: Broadcasting with Scalars
print("Exercise 1: Broadcasting with Scalars\n")
"""
Tasks:
1. Create a 1D array with elements [10, 20, 30].
2. Subtract a scalar value of 5 from each element using broadcasting.
3. Multiply each element by 2 using broadcasting.
"""
print("Solution:")
array_ex1 = np.array([10, 20, 30])
print("Original Array:", array_ex1)

# Subtract scalar
result_sub_ex1 = array_ex1 - 5
print("Array - 5:", result_sub_ex1)

# Multiply by scalar
result_mul_ex1 = array_ex1 * 2
print("Array * 2:", result_mul_ex1)
print()

# Exercise 2: Broadcasting with Arrays of Different Shapes
print("Exercise 2: Broadcasting with Arrays of Different Shapes\n")
"""
Tasks:
1. Create a 2D array A with shape (4, 1) containing values [[1], [2], [3], [4]].
2. Create a 1D array B with shape (3,) containing values [10, 20, 30].
3. Attempt to add A and B. Explain the outcome.
4. Modify B to have shape (1, 3) and add it to A.
"""
print("Solution:")
# Step 1
A_ex2 = np.array([[1], [2], [3], [4]])
print("Array A (4x1):")
print(A_ex2)

# Step 2
B_ex2 = np.array([10, 20, 30])
print("\nArray B (3,):")
print(B_ex2)

# Step 3: Attempt to add A and B
print("\nAttempting to add A and B:")
try:
    result_add_ex2 = A_ex2 + B_ex2
    print("A + B:")
    print(result_add_ex2)
except ValueError as e:
    print("Error:", e)

# Step 4: Modify B to shape (1, 3) and add
B_ex2_reshaped = B_ex2.reshape((1, 3))
print("\nReshaped Array B (1x3):")
print(B_ex2_reshaped)

print("\nAdding A and reshaped B:")
# Note: Now, A has shape (4,1) and B has shape (1,3), which are compatible
result_add_ex2_reshaped = A_ex2 + B_ex2_reshaped
print("A + B (Broadcasted to 4x3):")
print(result_add_ex2_reshaped)
print()

# Exercise 3: Broadcasting in Higher Dimensions
print("Exercise 3: Broadcasting in Higher Dimensions\n")
"""
Tasks:
1. Create a 3D array C with shape (2, 1, 3) containing values [[[1, 2, 3]], [[4, 5, 6]]].
2. Create a 2D array D with shape (1, 3) containing values [[10, 20, 30]].
3. Add arrays C and D using broadcasting.
"""
print("Solution:")
# Step 1
C_ex3 = np.array([
    [[1, 2, 3]],
    [[4, 5, 6]]
])  # Shape: (2, 1, 3)
print("Array C (2x1x3):")
print(C_ex3)

# Step 2
D_ex3 = np.array([[10, 20, 30]])  # Shape: (1, 3)
print("\nArray D (1x3):")
print(D_ex3)

# Step 3: Add C and D using broadcasting
print("\nAdding C and D:")
# Broadcasting:
# C has shape (2,1,3)
# D has shape (1,3) -> treated as (1,1,3)
# Resulting shape: (2,1,3)
result_add_ex3 = C_ex3 + D_ex3
print("C + D (Broadcasted to 2x1x3):")
print(result_add_ex3)
print()

# Exercise 4: Element-Wise Multiplication with Broadcasting
print("Exercise 4: Element-Wise Multiplication with Broadcasting\n")
"""
Tasks:
1. Create a 2D array E with shape (3, 1) containing values [[1], [2], [3]].
2. Create a 1D array F with shape (3,) containing values [4, 5, 6].
3. Perform element-wise multiplication between E and F using broadcasting.
"""
print("Solution:")
# Step 1
E_ex4 = np.array([[1], [2], [3]])  # Shape: (3,1)
print("Array E (3x1):")
print(E_ex4)

# Step 2
F_ex4 = np.array([4, 5, 6])  # Shape: (3,)
print("\nArray F (3,):")
print(F_ex4)

# Step 3: Element-wise multiplication using broadcasting
result_mul_ex4 = E_ex4 * F_ex4
print("\nE * F (Broadcasted to 3x3):")
print(result_mul_ex4)
print()

# ---------------------------------------------
# 6. Conclusion
# ---------------------------------------------
print("=== 6. Conclusion ===\n")
print("""
Broadcasting in NumPy is a versatile and efficient feature that simplifies arithmetic operations between arrays of different shapes. 
By understanding and applying the broadcasting rules, you can write concise and optimized code without the need for explicit loops or data duplication.

**Key Takeaways:**
- **Broadcasting Rules:** Align shapes from the trailing dimensions and ensure compatibility (dimensions are equal or one of them is 1).
- **Scalar Operations:** Scalars are automatically broadcasted to match the shape of arrays.
- **Higher-Dimensional Broadcasting:** Broadcasting works seamlessly with arrays of more than two dimensions.
- **Avoid Pitfalls:** Ensure that arrays are compatible for broadcasting to prevent unexpected results or errors.

**Best Practices:**
- **Understand Array Shapes:** Always be mindful of the shapes of your arrays when performing operations.
- **Use `.reshape()` When Necessary:** Adjust the shape of arrays to make them compatible for broadcasting.
- **Leverage Broadcasting for Efficiency:** Utilize broadcasting to write more efficient and readable code.

**Next Steps:**
- Explore more advanced NumPy features such as vectorized operations, universal functions, and linear algebra routines.
- Integrate broadcasting techniques into data processing pipelines for enhanced performance.
- Practice by solving real-world problems that involve multi-dimensional data manipulations.


""")

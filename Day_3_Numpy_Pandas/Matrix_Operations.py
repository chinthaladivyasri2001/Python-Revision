# numpy_matrix_operations.py

"""
NumPy Matrix Operations
-----------------------
This script provides a comprehensive overview of matrix operations using NumPy, including:
1. Matrix Creation
2. Basic Matrix Operations (Addition, Subtraction, Multiplication)
3. Matrix Transpose
4. Matrix Inversion
5. Determinant Calculation
6. Solving Linear Equations
7. Practice Exercises with Explanations

Prerequisites:
- Ensure that NumPy is installed in your Python environment.
  You can install it using pip:
      pip install numpy
"""

import numpy as np

# ---------------------------------------------
# 1. Introduction to Matrix Operations
# ---------------------------------------------
print("=== 1. Introduction to Matrix Operations ===\n")

# Matrices are two-dimensional arrays that represent mathematical matrices.
# NumPy provides powerful tools for creating and manipulating matrices efficiently.

# ---------------------------------------------
# 2. Matrix Creation
# ---------------------------------------------
print("=== 2. Matrix Creation ===\n")

# 2.1. Creating Matrices from Python Lists
print("2.1. Creating Matrices from Python Lists\n")

# Creating a 2x3 matrix
matrix_2x3 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("2x3 Matrix:")
print(matrix_2x3)
print("Shape:", matrix_2x3.shape)
print()

# Creating a 3x3 identity matrix
identity_matrix = np.identity(3)
print("3x3 Identity Matrix:")
print(identity_matrix)
print("Shape:", identity_matrix.shape)
print()

# Creating a 3x3 diagonal matrix
diagonal_matrix = np.diag([10, 20, 30])
print("3x3 Diagonal Matrix:")
print(diagonal_matrix)
print("Shape:", diagonal_matrix.shape)
print()

# 2.2. Using NumPy Built-in Functions to Create Matrices
print("2.2. Creating Matrices Using NumPy Built-in Functions\n")

# Creating a matrix of zeros
zeros_matrix = np.zeros((2, 2))
print("2x2 Zeros Matrix:")
print(zeros_matrix)
print()

# Creating a matrix of ones
ones_matrix = np.ones((3, 3))
print("3x3 Ones Matrix:")
print(ones_matrix)
print()

# Creating a matrix with a range of values
range_matrix = np.arange(1, 10).reshape((3, 3))
print("3x3 Range Matrix (1 to 9):")
print(range_matrix)
print()

# Creating a matrix with random values
random_matrix = np.random.random((2, 3))
print("2x3 Random Matrix:")
print(random_matrix)
print()

# ---------------------------------------------
# 3. Basic Matrix Operations
# ---------------------------------------------
print("=== 3. Basic Matrix Operations ===\n")

# 3.1. Matrix Addition
print("3.1. Matrix Addition\n")
A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print()

# Adding matrices A and B
C = A + B
print("A + B:")
print(C)
print()

# 3.2. Matrix Subtraction
print("3.2. Matrix Subtraction\n")

# Subtracting matrix B from A
D = A - B
print("A - B:")
print(D)
print()

# 3.3. Element-Wise Matrix Multiplication
print("3.3. Element-Wise Matrix Multiplication\n")

# Element-wise multiplication of A and B
E = A * B
print("A * B (Element-Wise):")
print(E)
print()

# 3.4. Matrix Multiplication (Dot Product)
print("3.4. Matrix Multiplication (Dot Product)\n")

# Matrix multiplication using np.dot()
F = np.dot(A, B)
print("A · B (Dot Product):")
print(F)
print()

# Alternatively, using the @ operator (Python 3.5+)
G = A @ B
print("A @ B (Dot Product using @ operator):")
print(G)
print()

# ---------------------------------------------
# 4. Matrix Transpose
# ---------------------------------------------
print("=== 4. Matrix Transpose ===\n")

# Transposing matrix A
A_transpose = A.T
print("Transposed Matrix A:")
print(A_transpose)
print("Shape:", A_transpose.shape)
print()

# ---------------------------------------------
# 5. Matrix Inversion
# ---------------------------------------------
print("=== 5. Matrix Inversion ===\n")

# Creating a square matrix
H = np.array([
    [4, 7],
    [2, 6]
])
print("Matrix H:")
print(H)
print()

# Calculating the inverse of H
H_inv = np.linalg.inv(H)
print("Inverse of Matrix H:")
print(H_inv)
print()

# Verifying the inverse by multiplying H and H_inv
identity = np.dot(H, H_inv)
print("H · H_inv (Should be Identity Matrix):")
print(identity)
print()

# ---------------------------------------------
# 6. Determinant Calculation
# ---------------------------------------------
print("=== 6. Determinant Calculation ===\n")

# Calculating the determinant of matrix H
det_H = np.linalg.det(H)
print("Determinant of Matrix H:", det_H)
print()

# ---------------------------------------------
# 7. Solving Linear Equations
# ---------------------------------------------
print("=== 7. Solving Linear Equations ===\n")

# Solving the system:
# 2x + 3y = 8
# 5x + y = 14

# Coefficient matrix
coeff_matrix = np.array([
    [2, 3],
    [5, 1]
])

# Right-hand side vector
rhs = np.array([8, 14])

# Solving for [x, y]
solution = np.linalg.solve(coeff_matrix, rhs)
print("Solution to the system:")
print(f"x = {solution[0]}, y = {solution[1]}")
print()

# ---------------------------------------------
# 8. Practice Exercises
# ---------------------------------------------
print("=== 8. Practice Exercises ===\n")

# Exercise 1: Matrix Operations
print("Exercise 1: Matrix Operations\n")

"""
Tasks:
1. Create two 3x3 matrices.
2. Perform matrix addition and subtraction.
3. Perform both element-wise and matrix multiplication.
4. Calculate the inverse and determinant of one matrix.
5. Verify the inverse by multiplying it with the original matrix.
"""

# 1. Creating two 3x3 matrices
print("1. Creating two 3x3 matrices:")
Matrix1 = np.array([
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
])
Matrix2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])
print("Matrix1:")
print(Matrix1)
print("\nMatrix2:")
print(Matrix2)
print()

# 2. Matrix Addition and Subtraction
print("2. Matrix Addition and Subtraction:")
Addition = Matrix1 + Matrix2
Subtraction = Matrix1 - Matrix2
print("Matrix1 + Matrix2:")
print(Addition)
print("\nMatrix1 - Matrix2:")
print(Subtraction)
print()

# 3. Element-Wise and Matrix Multiplication
print("3. Element-Wise and Matrix Multiplication:")
Element_Wise_Mul = Matrix1 * Matrix2
Dot_Product = np.dot(Matrix1, Matrix2)
print("Element-Wise Multiplication (Matrix1 * Matrix2):")
print(Element_Wise_Mul)
print("\nMatrix Multiplication (Matrix1 · Matrix2):")
print(Dot_Product)
print()

# 4. Inverse and Determinant
print("4. Inverse and Determinant of Matrix1:\n")
# For inversion, the matrix must be square and have a non-zero determinant
det_Matrix1 = np.linalg.det(Matrix1)
print("Determinant of Matrix1:", det_Matrix1)
if det_Matrix1 != 0:
    Inverse_Matrix1 = np.linalg.inv(Matrix1)
    print("\nInverse of Matrix1:")
    print(Inverse_Matrix1)
else:
    print("\nMatrix1 is singular and does not have an inverse.")
print()

# 5. Verifying the Inverse
print("5. Verifying the Inverse by multiplying Matrix1 with its Inverse:\n")
if det_Matrix1 != 0:
    Verification = np.dot(Matrix1, Inverse_Matrix1)
    print("Matrix1 · Inverse of Matrix1:")
    print(Verification)
    print("\nShould be close to the Identity Matrix:")
    Identity_Matrix = np.identity(3)
    print(Identity_Matrix)
else:
    print("Cannot verify inverse as Matrix1 is singular.")
print()

# Exercise 2: Solving Linear Equations
print("Exercise 2: Solving Linear Equations\n")

"""
Tasks:
1. Define a system of linear equations.
2. Represent the system in matrix form.
3. Solve the system using NumPy.
"""

# 1. Defining the system of equations:
# 3x + 2y - z = 1
# 2x - 2y + 4z = -2
# -x + 0.5y - z = 0

print("1. Defining the system of equations:")
print("""
3x + 2y - z = 1
2x - 2y + 4z = -2
-x + 0.5y - z = 0
""")
print()

# 2. Representing the system in matrix form (Ax = b)
A = np.array([
    [3, 2, -1],
    [2, -2, 4],
    [-1, 0.5, -1]
])
b = np.array([1, -2, 0])
print("Coefficient Matrix A:")
print(A)
print("\nRight-Hand Side Vector b:")
print(b)
print()

# ---------------------------------------------
print("=== 9. Conclusion ===\n")
print("""
Matrix operations are fundamental in various fields such as engineering, physics, computer science, and data analysis. 
NumPy provides efficient and intuitive tools to perform these operations, enabling complex computations with ease.

Key Takeaways:
- **Matrix Creation:** Use `np.array()`, `np.identity()`, `np.diag()`, and other built-in functions to create matrices.
- **Basic Operations:** Perform addition, subtraction, and both element-wise and matrix multiplication effortlessly.
- **Advanced Operations:** Calculate the inverse and determinant of matrices, which are crucial for solving linear systems and understanding matrix properties.
- **Solving Linear Equations:** Utilize `np.linalg.solve()` to find solutions to systems of linear equations efficiently.

By mastering these matrix operations, you can tackle a wide range of computational problems effectively using Python and NumPy.


""")

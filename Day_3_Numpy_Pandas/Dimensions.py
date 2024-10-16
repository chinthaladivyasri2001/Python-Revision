import numpy as np

# Creating NumPy Arrays
#Example 1: Creating Arrays from Lists


# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)
print("Shape:", array_1d.shape)
print()

# Creating a 2D array
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("2D Array:")
print(array_2d)
print("Shape:", array_2d.shape)
print()

# Creating a 3D array
array_3d = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])
print("3D Array:")
print(array_3d)
print("Shape:", array_3d.shape)

## Array operations

# 5. Array Operations
# ---------------------------------------------
print("=== 5. Array Operations ===\n")

# 5.1. Element-Wise Arithmetic Operations
print("5.1. Element-Wise Arithmetic Operations\n")
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Addition
add = a + b
print("Addition:", add)

# Subtraction
sub = a - b
print("Subtraction:", sub)

# Multiplication
mul = a * b
print("Multiplication:", mul)

# Division
div = a / b
print("Division:", div)
print()

# 5.2. Universal Functions (ufuncs)
print("5.2. Universal Functions (ufuncs)\n")
arr_ufunc = np.array([1, 4, 9, 16, 25])

# Square root
sqrt = np.sqrt(arr_ufunc)
print("Square Roots:", sqrt)

# Exponential
exp = np.exp(arr_ufunc)
print("Exponential:", exp)

# Sine
angles = np.array([0, np.pi/2, np.pi])
sine = np.sin(angles)
print("Sine:", sine)
print()

# 5.3. Broadcasting
print("5.3. Broadcasting\n")

# 5.3.1. Broadcasting with Scalars
print("5.3.1. Broadcasting with Scalars\n")
a_broadcast = np.array([1, 2, 3])
result_add = a_broadcast + 10
print("Array + Scalar:", result_add)

result_mul = a_broadcast * 5
print("Array * Scalar:", result_mul)
print()

# 5.3.2. Broadcasting with Arrays of Different Shapes
print("5.3.2. Broadcasting with Arrays of Different Shapes\n")
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([10, 20, 30])

# Broadcasting addition
C = A + B
print("A + B (Broadcasted):")
print(C)
print()

# 1D array as a column vector
D = np.array([100, 200]).reshape(2, 1)

# Broadcasting multiplication
E = A * D
print("A * D (Broadcasted):")
print(E)
print()

# 5.4. Reshaping and Transposing Arrays
print("5.4. Reshaping and Transposing Arrays\n")

# Reshaping Arrays
array_reshape = np.arange(1, 13)  # [1, 2, ..., 12]
print("Original Array:", array_reshape)

reshaped_3x4 = array_reshape.reshape((3, 4))
print("Reshaped Array (3x4):")
print(reshaped_3x4)
print()

reshaped_2x2x3 = array_reshape.reshape((2, 2, 3))
print("Reshaped Array (2x2x3):")
print(reshaped_2x2x3)
print()

# Transposing Arrays
A_transpose = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Original Array A:")
print(A_transpose)
print()

A_T = A_transpose.T
print("Transposed Array A_T:")
print(A_T)
print()

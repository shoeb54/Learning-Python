# ============================================================
# NUMPY MASTER SCRIPT
# ============================================================

import numpy as np


# ============================================================
# 1️⃣ CREATING ARRAYS
# ============================================================

# 1D array (vector)
a = np.array([1, 2, 3, 4])
print("1D Array:", a)

# 2D array (matrix)
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print("2D Array:\n", b)

# Zeros, Ones, Identity
zeros = np.zeros((2, 3))
ones = np.ones((2, 2))
identity = np.eye(3)

print("Zeros:\n", zeros)
print("Identity:\n", identity)

# Range-based arrays
c = np.arange(0, 10, 2)     # start, stop, step
d = np.linspace(0, 1, 5)    # evenly spaced values
print("Arange:", c)
print("Linspace:", d)

print("Shape:", b.shape)
print("Dimensions:", b.ndim)
print("Data type:", b.dtype)


# ============================================================
# 2️⃣ INDEXING & SLICING
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice 1:4:", arr[1:4])

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Element (row1,col2):", matrix[0, 1])
print("First row:", matrix[0])
print("Second column:", matrix[:, 1])
print("Submatrix:\n", matrix[0:2, 1:3])


# ============================================================
# 3️⃣ BROADCASTING
# ============================================================

# Broadcasting = automatic shape alignment
x = np.array([1, 2, 3])
print("x + 5:", x + 5)   # scalar broadcast

M = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Matrix + vector:\n", M + x)
# x automatically expands across rows


# ============================================================
# 4️⃣ VECTORIZED OPERATIONS
# ============================================================

# No loops required!
nums = np.array([1, 2, 3, 4])

print("Squared:", nums ** 2)
print("Sqrt:", np.sqrt(nums))
print("Exponential:", np.exp(nums))
print("Log:", np.log(nums))

# Aggregations
print("Sum:", np.sum(nums))
print("Mean:", np.mean(nums))
print("Std Dev:", np.std(nums))
print("Max:", np.max(nums))


# ============================================================
# 5️⃣ MATRIX OPERATIONS
# ============================================================

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Element-wise multiplication
print("Element-wise multiply:\n", A * B)

# Matrix multiplication
print("Matrix multiply:\n", A @ B)
print("Using dot():\n", np.dot(A, B))

# Transpose
print("Transpose:\n", A.T)


# ============================================================
# 6️⃣ LINEAR ALGEBRA BASICS
# ============================================================

# Determinant
print("Determinant:", np.linalg.det(A))

# Inverse
print("Inverse:\n", np.linalg.inv(A))

# Eigenvalues & Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Solving linear equations Ax = b
b_vec = np.array([5, 6])
solution = np.linalg.solve(A, b_vec)
print("Solution of Ax=b:", solution)


# ============================================================
# END
# ============================================================
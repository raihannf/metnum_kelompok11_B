import numpy as np

def lu_decomposition(A, b):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        for k in range(i, n):
            sum_val = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_val

        for k in range(i, n):
            if i == k:
                L[i][i] = 1
            else:
                sum_val = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - sum_val) / U[i][i]

    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

    return L, U, y, x

# Contoh penggunaan
A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
b = np.array([1, 0, 1])
L, U, y, x = lu_decomposition(A, b)

print("Matriks L:")
print(L)
print("Matriks U:")
print(U)
print("Nilai y:")
print(y)
print("Nilai x:")
print(x)

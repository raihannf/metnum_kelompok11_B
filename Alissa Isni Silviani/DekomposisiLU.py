import numpy as np  # Mengimpor library NumPy

# Fungsi dekomposisi LU
n = len(A)
L = np.zeros((n, n))  # Matriks segitiga bawah
U = np.zeros((n, n))  # Matriks segitiga atas

    for i in range(n):
        L[i, i] = 1  # diagonal L menjadi 1
        for j in range(i, n):
            U[i, j] = A[i, j]
            for k in range(i):
                U[i, j] -= L[i, k] * U[k, j]  # penghitungan elemen U
        for j in range(i + 1, n):
            L[j, i] = A[j, i]
            for k in range(i):
                L[j, i] -= L[j, k] * U[k, i]
            L[j, i] /= U[i, i]  # penghitungan elemen L

    return L, U

# Fungsi penyelesaian SPL dengan dekomposisi LU
def hitungLU(L, U, b):
    n = len(b)
    y = np.zeros(n)
    x = np.zeros(n)

    # Substitusi untuk menyelesaikan Ly = b
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]

    # Substitusi untuk menyelesaikan Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]

    return x, y

# Menginput ordo matriks A
n = int(input("Masukkan Ordo Matriks A: "))
A = np.zeros((n, n))
b = np.zeros(n)

# menginput elemen pada matriks A dan vektor b
print("Masukkan elemen matriks A:")
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"A[{i+1},{j+1}]: "))

print("Masukkan elemen vektor b:")
for i in range(n):
    b[i] = float(input(f"b[{i+1}]: "))

# Melakukan dekomposisi LU menggunakan fungsi dekomposisiLU dengan memasukkan matriks A
L, U = dekomposisiLU(A)

# Mencetak matriks segitiga bawah L
print("\nMatriks Segitiga Bawah L:")
for i in range(n):
    for j in range(n):
        print(L[i, j], end="\t")
    print()

# Mencetak matriks segitiga atas U
print("\nMatriks Segitiga Atas U:")
for i in range(n):
    for j in range(n):
        print(U[i, j], end="\t")
    print()

# Menyelesaikan SPL dengan matriks L, matriks U, dan vektor b menggunakan fungsi hitungLU
x, y = hitungLU(L, U, b)

# Mencetak nilai y
print("\nNilai y:")
print(y)

# Mencetak solusi nilai x
print("Solusi x:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.2f}")

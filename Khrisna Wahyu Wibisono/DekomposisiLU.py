# Nama: Khrisna Wahyu Wibisono
# NIM: 2204340

import numpy as np  #Library Numpy digunakan untuk membantu perhitungan

def dekomposisiLU(A):  #Mendefinisikan fungsi untuk melakukan dekomposisi LU
    n = len(A)
    L = np.zeros((n, n))  #Inisialisasi matriks segitiga bawah (lower)
    U = np.zeros((n, n))  #Inisialisasi matriks segitiga atas (upper)

    for i in range(n):
        L[i, i] = 1  #Membuat diagonal L menjadi 1
        for j in range(i, n):
            U[i, j] = A[i, j]
            for k in range(i):
                U[i, j] -= L[i, k] * U[k, j]  #Menghitung elemen U
        for j in range(i + 1, n):
            L[j, i] = A[j, i]
            for k in range(i):
                L[j, i] -= L[j, k] * U[k, i]
            L[j, i] /= U[i, i]  #Menghitung elemen L

    return L, U


#Mendefinisikan fungsi untuk menyelesaikan SPL menggunakan dekomposisi LU
def hitungLU(L, U, b):
    n = len(b)
    y = np.zeros(n)
    x = np.zeros(n)

    # substitusi untuk menyelesaikan Ly = b
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]

    # substitusi untuk menyelesaikan Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]

    return x, y


#Input untuk mengatur ordo matriks A
n = int(input("Masukkan Ordo Matriks A: "))
A = np.zeros((n, n))
b = np.zeros(n)

#Input untuk memasukkan elemen pada matriks A dan vektor b
print("Masukkan elemen matriks A:")
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"A[{i+1},{j+1}]: "))

print("Masukkan elemen vektor b:")
for i in range(n):
    b[i] = float(input(f"b[{i+1}]: "))

#Melakukan dekomposisi LU menggunakan fungsi dekomposisiLU dengan memasukkan matriks A
L, U = dekomposisiLU(A)

#Mencetak matriks segitiga bawah L
print("Matriks L:")
for i in range(n):
    for j in range(n):
        print(L[i, j], end="\t")
    print()

#MMencetak matriks segitiga atas U
print("Matriks U:")
for i in range(n):
    for j in range(n):
        print(U[i, j], end="\t")
    print()

#Menyelesaikan SPL menggunakan fungsi hitungLU dengan memasukkan matriks L, matriks U, dan vektor b
x, y = hitungLU(L, U, b)

#Mencetak nilai y
print("Nilai y:")
print(y)

#Mencetak solusi x
print("Solusi x:")
print(x)
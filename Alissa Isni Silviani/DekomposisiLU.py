import numpy as np  # Mengimpor library NumPy untuk operasi matriks

def dekomposisi_LU(matrix_input):
    n = len(matrix_input)  # Menghitung ukuran matriks input
    matrix_L = np.zeros((n, n))  # Membuat matriks nol dengan ukuran n x n untuk matriks L
    matrix_U = np.zeros((n, n))  # Membuat matriks nol dengan ukuran n x n untuk matriks U

    for baris in range(n): # Iterasi melalui baris matriks untuk dekomposisi LU
        # Proses dekomposisi matriks input menjadi matriks U (Segitiga Atas)
        for kolom in range(baris, n):
            total = 0
            for indeks in range(baris):
                total += matrix_L[baris][indeks] * matrix_U[indeks][kolom]
            matrix_U[baris][kolom] = matrix_input[baris][kolom] - total

        # Proses dekomposisi matriks input menjadi matriks L (Segitiga Bawah)
        for kolom in range(baris, n):
            if baris == kolom:
                matrix_L[baris][baris] = 1  # Elemen diagonal utama matriks L selalu 1
            else:
                total = 0
                for indeks in range(baris):
                    total += matrix_L[kolom][indeks] * matrix_U[indeks][baris]
                matrix_L[kolom][baris] = (matrix_input[kolom][baris] - total) / matrix_U[baris][baris]

    return matrix_L, matrix_U  # Mengembalikan matriks L dan U setelah dekomposisi

# User menginput matriks
ukuran_matriks = int(input("Masukkan ukuran matriks (n): "))  # Meminta pengguna untuk memasukkan ukuran matriks
matrix_input = np.zeros((ukuran_matriks, ukuran_matriks))  # Membuat matriks nol dengan ukuran yang telah diinputkan

print("Masukkan elemen matriks input:")  # Memberikan instruksi kepada pengguna untuk memasukkan elemen matriks input
for baris in range(ukuran_matriks):
    for indeks in range(ukuran_matriks):
        matrix_input[baris][indeks] = float(input(f"A[{baris+1}][{indeks+1}]: "))  # User menginput elemen matriks

# Lakukan dekomposisi LU
matrix_L, matrix_U = dekomposisi_LU(matrix_input)  # Memanggil fungsi dekomposisi_LU untuk mendapatkan matriks L dan U

# Tampilkan matriks L dan U
print("\nMatriks Segitiga Bawah L:")  # Mencetak matriks L (Segitiga Bawah)
print(matrix_L)
print("\nMatriks Segitiga Atas U:")  # Mencetak matriks U (Segitiga Atas)
print(matrix_U)

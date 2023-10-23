import numpy as np  # Mengimpor library NumPy untuk operasi matriks

# Definisi Matriks A dan Vektor B
A = []  # Inisialisasi matriks A sebagai daftar kosong
B = []  # Inisialisasi vektor B sebagai daftar kosong

n = int(input("Masukkan ukuran Matriks: "))  # Meminta user menginput uk matriks

# Meminta pengguna untuk memasukkan nilai-nilai koefisien matriks A
for i in range(n):
    baris = []  # Inisialisasi baris matriks A sebagai daftar kosong
    for j in range(n):
        a = float(input(f"Masukkan Nilai Koefisien A[{i+1},{j+1}]: "))  # Meminta pengguna untuk memasukkan nilai koefisien
        baris.append(a)  # Menambahkan nilai ke baris matriks A
    A.append(baris)  # Menambahkan baris ke matriks A

# Meminta pengguna untuk memasukkan nilai-nilai vektor B
for i in range(n):
    h = float(input(f"Masukkan Hasil B[{i+1}]: "))  # Meminta pengguna untuk memasukkan nilai hasil
    B.append(h)  # Menambahkan nilai ke vektor B

Matrix = np.array(A, float)  # Membuat matriks A sebagai array NumPy dengan tipe data float
Hasil = np.array(B, float)  # Membuat vektor B sebagai array NumPy dengan tipe data float

print("Matriks A:")
print(Matrix)  # Mencetak matriks A ke layar

print("Vektor B:")
print(Hasil)  # Mencetak vektor B ke layar

# Eliminasi Gauss Maju
for k in range(0, n-1):
    for i in range(k+1, n):
        if Matrix[i, k] != 0:
            lam = Matrix[i, k] / Matrix[k, k]
            Matrix[i, k:n] = Matrix[i, k:n] - (Matrix[k, k:n] * lam)
            Hasil[i] = Hasil[i] - (Hasil[k] * lam)

print("Matriks A setelah Eliminasi Gauss Maju:")
print(Matrix)  # Mencetak matriks A setelah eliminasi Gauss Maju

print("Vektor B setelah Eliminasi Gauss Maju:")
print(Hasil)  # Mencetak vektor B setelah eliminasi Gauss Maju

# Substitusi Mundur (Backward Substitution)
x = np.zeros(n, float)  # Inisialisasi vektor solusi x
for m in range(n-1, -1, -1):
    x[m] = (Hasil[m] - np.dot(Matrix[m, m+1:n], x[m+1:n])) / Matrix[m, m]
    print(f'Nilai X[{m+1}] = {x[m]}')  # Mencetak solusi x ke layar

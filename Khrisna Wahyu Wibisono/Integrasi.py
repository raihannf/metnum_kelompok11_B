# Nama: Khrisna Wahyu Wibisono
# NIM: 2204340

import numpy as np  # Mengimport library numpy
import math  # Mengimport library math untuk penggunaan bilangan euler ('e')

e = math.e  # Digunakan jika user menginput e sebagai bilangan euler pada fungsi


def inputFungsi():  # Mendefinisikan fungsi yang diinputkan oleh user
    fungsi = input("Masukkan f(x): ")
    return lambda x: eval(fungsi)


def inputBatas():  # Mendefinisikan batas bawah dan batas atas integral yang diinputkan oleh user
    a = float(input("Masukkan batas bawah integral: "))
    b = float(input("Masukkan batas atas integral: "))
    return a, b


def inputPartisi():  # Mendefinisikan jumlah partisi yang diinputkan oleh user
    n = int(input("Masukkan jumlah partisi: "))
    return n


f = inputFungsi()
a, b = inputBatas()
n = inputPartisi()


# Mendefinisikan fungsi untuk metode trapesium
def trapesium(f, a, b, n):
    # Mendapatkan interval
    h = (b - a) / n
    x = np.arange(a, b + h, h)
    # Menjumlahkan interval
    trap = f(x[0]) + f(x[n])
    for i in range(1, n):
        trap += 2 * f(x[i])
    trap = (h / 2.0) * trap
    return trap


# Mendefinisikan fungsi untuk metode simpson 1/3
def simpson(f, a, b, n):
    # Jumlah partisi harus genap untuk metode simpson 1/3
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    x = np.arange(a, b + h, h)
    # Menjumlahkan interval
    simp = f(x[0]) + f(x[n])
    for i in range(1, n):
        if i % 2 == 0:
            w = 2
        else:
            w = 4
        simp += w * f(x[i])
    simp = (h / 3.0) * simp
    return simp


def titikTengah(f, a, b, n):
    # Mendapatkan interval
    h = (b - a) / n
    tengah = 0
    for i in range(n):
        x_tengah = a + (i + 0.5) * h
        tengah += f(x_tengah)
    tengah *= h
    return tengah


# Memanggil fungsi integrasi
trap = trapesium(f, a, b, n)
simp = simpson(f, a, b, n)
tengah = titikTengah(f, a, b, n)


# Menampilkan hasil integrasi
print("Hasil integrasi menggunakan metode trapesium: ", trap)
print("Hasil integrasi menggunakan metode Simpson 1/3: ", simp)
print("Hasil integrasi menggunakan metode titik tengah: ", tengah)

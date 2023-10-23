# Nama: Khrisna Wahyu Wibisono
# NIM: 2204340

import numpy as np  #Library Numpy digunakan untuk membantu perhitungan
import math  #Library math digunakan untuk mendefine bilangan euler ('e')

e = math.e 

def inputFungsi():  #Mendefinisikan Fungsi untuk memasukkan ekspresi fungsi yang akan dicari akarnya
    fungsi = input("Masukkan f(x): ")
    return lambda x: eval(fungsi)

def inputInterval():  #Mendefinisikan Fungsi untuk memasukkan interval (a, b) yang akan digunakan
    a = float(input("Masukkan batas kiri interval: "))
    b = float(input("Masukkan batas kanan interval: "))
    return a, b

def inputEpsilon():  #Mendefinisikan Fungsi untuk memasukkan nilai toleransi (epsilon)
    return float(input("Masukkan nilai toleransi (epsilon): "))

def inputIterasiMaks():  # Fungsi untuk memasukkan jumlah maksimum iterasi
    iterasiMaks = int(input("Masukkan jumlah maksimum iterasi: "))
    return iterasiMaks

def my_bisection(a, b, eps, f, iterasiMaks):  #Implementasi metode bisection
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Tidak ada akar pada interval a dan b")  # Munculkan pesan jika tanda fungsi pada kedua ujung interval sama

    iterasi = 0  #Mengatur jumlah iterasi dimulai dari nol

    # Proses pencarian akar
    while np.abs(a - b) > eps:  #Terus lakukan iterasi selama selisih interval masih lebih besar dari toleransi (epsilon)
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterasi += 1

    return (a + b) / 2

f = inputFungsi()
a, b = inputInterval()
eps = inputEpsilon()
iterasiMaks = inputIterasiMaks()

#Menggunakan fungsi my_bisection dengan memasukkan interval (a, b) dan epsilon untuk mencari akar
akarHampiran = my_bisection(a, b, eps, f, iterasiMaks)

print("Akar hampiran dari f:", akarHampiran)  #Menampilkan Output hasil pencarian akar
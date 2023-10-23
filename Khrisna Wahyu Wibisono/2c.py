# Nama: Khrisna Wahyu Wibisono
# NIM: 2204340

import numpy as np #Library Numpy digunakan untuk membantu perhitungan
import math #Library math digunakan untuk mendefine bilangan euler ('e')
import matplotlib.pyplot as plt #Import library matplotlib untuk visualisasi grafik

e = math.e 

def inputFungsi(): #Mendefinisikan Fungsi untuk memasukkan ekspresi fungsi yang akan dicari akarnya
    fungsi = input("Masukkan f(x): ")
    return lambda x: eval(fungsi)

def inputInterval(): #Mendefinisikan Fungsi untuk memasukkan interval (a, b) yang akan digunakan
    a = float(input("Masukkan batas kiri interval: "))
    b = float(input("Masukkan batas kanan interval: "))
    return a, b

def inputEpsilon(): #Mendefinisikan Fungsi untuk memasukkan nilai toleransi (epsilon)
    return float(input("Masukkan ketelitian (epsilon): "))

def inputIterasiMaks(): #Mendefinisikan Fungsi untuk memasukkan jumlah maksimum iterasi
    iterasiMaks = int(input("Masukkan iterasi maksimal (n-iterasi): "))
    return iterasiMaks

def my_bisection(a, b, eps, f, iterasiMaks): #Implementasi metode bisection
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Tidak ada akar pada interval a dan b") #Munculkan pesan jika tanda fungsi pada kedua ujung interval sama

    iterasi = 0 #Mengatur jumlah iterasi dimulai dari nol


    #Proses pencarian akar
    while np.abs(a-b) > eps: #Terus lakukan iterasi selama selisih interval masih lebih besar dari toleransi (epsilon)
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

print("Akar Hampiran dari f:", akarHampiran) #Menampilkan hasil pencarian akar

#Mendefinisikan visualisasi grafik akar dari fungsi
def grafikAkar(f, a, b, akar):
    x = np.linspace(a, b, 1000) #Membuat array x yang berisi 1000 titik antara a dan b
    y = f(x) #Menghitung nilai fungsi f(x) pada setiap titik x

    plt.plot(x, y, label="f(x)") #Membuat plot garis f(x)
    plt.axhline(0, color="red", linestyle="--", linewidth=0.8, label="Akar") #Menambahkan garis horizontal untuk menandai akar
    plt.scatter(akar, 0, color="red", marker="o") #Menambahkan marker merah untuk menandai akar
    plt.annotate(f"Akar Hampiran: {akarHampiran:.10f}", (akarHampiran, f(akarHampiran)), color="red") #Menambahkan teks yang menunjukkan nilai akar hampiran
    plt.xlabel("x") 
    plt.ylabel("f(x)")
    plt.legend()
    plt.title("Grafik Akar dari f(x)") #Menambahkan judul grafik
    plt.grid(True)
    plt.show()

grafikAkar(f, a, b, akarHampiran)
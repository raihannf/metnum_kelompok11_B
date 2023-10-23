# Nama: Khrisna Wahyu Wibisono
# NIM: 2204340
# f(x) = x^3 - 2x + 1

import numpy as np #Library Numpy digunakan untuk membantu perhitungan

def f(x):
    return x**3 - 2*x + 1 #Menisialisasi fungsi yang digunakan

def my_bisection(a, b, eps, iterasiMaks):
    #Memeriksa tanda fungsi pada titik awal interval (a, b).
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b') # Akan melempar pesan kesalahan jika f(a) dan f(b) memiliki tanda yang sama

    iterasi = 0 #mendefiniskan iterasi, dan dimulai dari nol

    #Proses melakukan pencarian akar
    while np.abs(a - b) > eps and iterasi < iterasiMaks: # Terus melakukan iterasi selama selisih b dan a lebih besar dari ketelitian (epsilon).
        c = (a + b) / 2
        if f(c) == 0: #Jika fungsi mencapai nol tepat di titik tengah, akar ditemukan.
            return c
        elif f(a) * f(c) < 0: #Jika tanda fungsi pada a dan c berbeda, akar ada di interval (a, c).
            b = c
        else: #Jika tanda fungsi pada c dan b berbeda, akar ada di interval (c, b).
            a = c
        iterasi += 1

    return (a + b) / 2

#Menentukan iterasi maksimal (n-iterasi)
iterasiMaks = 100

#Mencari akar menggunakan fungsi my_bisection dengan memberikan interval (a, b) dan nilai epsilon
akarHampiran = my_bisection(0, 1, 1e-6, iterasiMaks)

print("Akar Hampiran dari f:", akarHampiran) # Menampilkan hasil pencarian akar
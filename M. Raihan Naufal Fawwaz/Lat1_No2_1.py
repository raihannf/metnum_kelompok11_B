import numpy as np #memanggil library numpy

def f(x):
    return x**3-2*x+1 #mendefinisikan fungsi dari soal 1 a

def my_bisection(a, b, eps, iterasiMaks):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b') #akan memunculkan pesan jika f(a) dan f(b) sama sama positif atau negatif

    iterasi = 0 #mengatur iterasi untuk dimulai dari nol

    #memproses pencarian akar
    while np.abs(a - b) > eps and iterasi < iterasiMaks: #terus lakukan iterasi jika |a-b| masih lebih besar dari ketelitian (epsilon) dan iterasi belum melebihi iterasi maksimal
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterasi += 1

    return (a + b)/2

#menentukan iterasi maksimal (n-iterasi)
iterasiMaks = 100

#mencari akar menggunakan fungsi my_bisection dengan memasukkan interval (a, b) dan epsilon
akarHampiran = my_bisection(0, 1, 1e-6, iterasiMaks)

print("Akar Hampiran dari f:", akarHampiran) #hasil pencarian akar
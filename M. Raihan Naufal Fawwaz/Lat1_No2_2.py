import numpy as np #memanggil library numpy
import math #memanggil library math supaya program dapat mengenal bilangan euler ('e')

e = math.e #digunakan jika user menginput e sebagai bilangan euler pada fungsi

def inputFungsi(): #mendefinisikan fungsi yang diinputkan user
    fungsi = input("Masukkan f(x): ")
    return lambda x: eval(fungsi)

def inputInterval(): #mendefinisikan interval (a, b) yang diinputkan user
    a = float(input("Masukkan batas kiri interval: "))
    b = float(input("Masukkan batas kanan interval: "))
    return a, b

def inputEpsilon(): #mendefinisikan nilai ketelitian (epsilon) yang diinputkan user
    return float(input("Masukkan ketelitian (epsilon): "))

def inputIterasiMaks(): #mendefinisikan nilai iterasi maksimal (n-iterasi)
    iterasiMaks = int(input("Masukkan iterasi maksimal (n-iterasi): "))
    return iterasiMaks

def my_bisection(a, b, eps, f, iterasiMaks):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Tidak ada akar pada interval a dan b") #akan memunculkan pesan jika f(a) dan f(b) sama sama positif atau negatif

    iterasi = 0 #mengatur iterasi untuk dimulai dari nol

    #memproses pencarian akar
    while np.abs(a-b) > eps: #terus lakukan iterasi jika |a-b| masih lebih besar dari ketelitian (epsilon)
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

#mencari akar menggunakan fungsi my_bisection dengan memasukkan interval (a, b) dan epsilon
akarHampiran = my_bisection(a, b, eps, f, iterasiMaks)

print("Akar Hampiran dari f:", akarHampiran) #hasil pencarian akar

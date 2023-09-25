import numpy as np #memanggil library numpy
import math #memanggil library math supaya program dapat mengenal bilangan euler ('e')
import matplotlib.pyplot as plt #memanggil library matplotlib untuk memvisualisasikan akar dalam bentuk grafik

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

#mendefinisikan bentuk grafik akar dari fungsi
def grafikAkar(f, a, b, akar):
    x = np.linspace(a, b, 1000)
    y = f(x)

    plt.plot(x, y, label="f(x)")
    plt.axhline(0, color="red", linestyle="--", linewidth=0.8, label="Akar")
    plt.scatter(akar, 0, color="red", marker="o")
    plt.annotate(f"Akar Hampiran: {akarHampiran:.10f}", (akarHampiran, f(akarHampiran)), color="red")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.title("Grafik Akar dari f(x)")
    plt.grid(True)
    plt.show()

grafikAkar(f, a, b, akarHampiran)
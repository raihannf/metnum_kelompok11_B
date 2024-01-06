# Nama: Khrisna Wahyu Wibisono
# NIM: 2204340

import math # library math digunakan untuk mengenal bilangan euler ('e')

def f(x):
    # Mendefinisikan fungsi f(x)
    return math.exp(x) - 5 * (x**2)

def g(x):
    # Mendefinisikan fungsi g(x)
    return math.exp(x) - 10 * x

# Menginisialsisasi nilai akar
akar = 0 

# Pencarian akar
def newtonRaphson(a, eps, f, g, N):
    # Cek apakah fungsi g(a) tidak sama dengan 0
    if g(a) != 0:
        i = 1
        while i <= N:
            # Iterasi hingga N
            c = a - (f(a) / g(a))
            if abs(c - a) < eps or abs(f(c)) < eps:
                akar = c
                # Hasil akar dari pencarian iterasi ke-i
                print("Akar ke-", i, "=", akar)
                break
            else:
                akar = c
                # Hasil akar dari pencarian iterasi ke-i
                print("Akar ke-", i, "=", akar)
            a = c
            i = i + 1
    else:
        print("g(x) = 0")


# Mencari akar menggunakan fungsi NewtonRaphson

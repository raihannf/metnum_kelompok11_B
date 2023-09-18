import numpy as np  # Memanggil library numpy

def f(x):
    return x**3 - 2*x + 1

def my_bisection(a, b, eps):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')

    iterasi = 0
    while True:  # Terus berjalan hingga kondisi berhenti terpenuhi
        x = (a + b) / 2  # Titik tengah interval
        if np.abs(f(x)) < eps:  # Kondisi berhenti jika toleransi terpenuhi
            return x

        # Memilih interval baru berdasarkan tanda f(x)
        if np.sign(f(a)) == np.sign(f(x)):
            a = x
        else:
            b = x

        iterasi += 1

# Mencari akar dalam interval [0, 1] dengan toleransi 1e-5
akarHampiran = my_bisection(0, 1, 1e-5)

print("Akar Hampiran dari f:", akarHampiran)

import numpy as np  # Memanggil library numpy

def f(x):
    return np.exp(x) - x  # Menggunakan fungsi baru f(x) = e^x - x

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

# Mencari akar dalam interval [0, 1] dengan toleransi yang dapat diatur
toleransi = 1e-6  #nilai toleransi sesuai dengan keinginan Anda
hasilAkhir = my_bisection(0, 1, toleransi)

print("Akar hampirannya yaitu:", hasilAkhir)
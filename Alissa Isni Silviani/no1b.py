import numpy as np # Menggunakan numpy sebagai library matematika
import math #memanggil library math supaya program dapat mengenal bilangan euler ('e')

e = math.e

def f(x): 
    return e**x-x # Mendefinisikan fungsi dari soal nomor 1 bagian (b)

def my_bisection(a, b, eps):
  # Memproses pencarian akar menggunakan metode bisection
  
  while np.abs(a-b) > eps: # Terus melakukan iterasi selama selisih b dan a lebih besar dari ketelitian (epsilon)
    c = (a + b)/2 # Titik tengah interval
    if f(c) == 0: # Jika fungsi mencapai nol tepat di titik tengah, akar ditemukan.
      return c
    elif f(a) * f(c) < 0: # Jika tanda fungsi pada a dan c berbeda, akar ada di interval (a, c).
      return my_bisection(a, c, eps)
    else:
      return my_bisection(c, b, eps)
    
  return (a + b)/2

# Mencari akar menggunakan fungsi my_bisection dengan memberikan interval (a, b) dan nilai epsilon
akarHampiran = my_bisection(-1, 1, 1e-6)

print("Akar Hampiran dari f:", akarHampiran) # Menampilkan hasil pencarian akar

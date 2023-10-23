# Nama: Khrisna Wahyu Wibisono
# NIM: 2204340
# Buatlah sebuah fungsi penyelesaian yang tepat baik dengan menggunakan metode Bagi Dua ketika
# b. f(x) = e^x - x
# Buatlah modifikasi fungsi ketika kriteria program berhenti adalah sudah mencapai pada iterasi ke-n

import numpy as np #Library Numpy digunakan untuk membantu perhitungan
import math #Library math digunakan untuk mendefine bilangan euler ('e')

e = math.e

def f(x): 
    return e**x-x #Mendefinisikan fungsi dari soal nomor 1 bagian (b)

def my_bisection(a, b, eps):
  #Proses melakukan pencarian akar menggunakan metode bisection
  
  while np.abs(a-b) > eps: # Terus melakukan iterasi selama selisih b dan a lebih besar dari ketelitian (epsilon)
    c = (a + b)/2 #Titik tengah interval
    if f(c) == 0: #Jika fungsi mencapai nol tepat di titik tengah, akar ditemukan.
      return c
    elif f(a) * f(c) < 0: #Jika tanda fungsi pada a dan c berbeda, akar ada di interval (a, c).
      return my_bisection(a, c, eps)
    else:
      return my_bisection(c, b, eps)
    
  return (a + b)/2

#Mencari akar menggunakan fungsi my_bisection dengan memberikan interval (a, b) dan nilai epsilon
akarHampiran = my_bisection(-1, 1, 1e-6)

print("Akar Hampiran dari f:", akarHampiran) #Menampilkan Output hasil pencarian akar

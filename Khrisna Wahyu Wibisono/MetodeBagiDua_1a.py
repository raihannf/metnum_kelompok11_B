# Nama: Khrisna Wahyu Wibisono
# NIM: 2204340
# Buatlah sebuah fungsi penyelesaian yang tepat baik dengan menggunakan metode Bagi Dua ketika
# a. f(x) = x^3 - 2x + 1


import numpy as np  #Library Numpy digunakan untuk membantu perhitungan

def f(x):
    return x**3-2*x+1  #Menisialisasi fungsi yang digunakan

def my_bisection(a, b, eps):
  #Memeriksa tanda fungsi pada titik awal interval (a, b).
  if np.sign(f(a)) == np.sign(f(b)):
    raise Exception('Tidak ada akar pada interval a dan b')  #jika f(a) dan f(b) memiliki tanda yang sama, Raise Pesan
  
  #Proses melakukan pencarian akar
  while np.abs(b-a) > eps:  #Dengan menggunakan perulangan while,melakukan iterasi selama selisih b dan a lebih besar dari ketelitian (epsilon)
    c = (a + b)/2
    if f(c) == 0: 
      return c
    elif f(a) * f(c) < 0:
      return my_bisection(a, c, eps)
    else:
      return my_bisection(c, b, eps)
  return (a + b)/2
    
#Mencari akar menggunakan fungsi my_bisection dengan memberikan interval (a, b) dan nilai epsilon
akarHampiran = my_bisection(0, 1, 1e-6)

print("Akar Hampiran dari f:", akarHampiran)  #Menampilkan Output hasil pencarian akar

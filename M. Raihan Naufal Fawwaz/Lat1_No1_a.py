import numpy as np #memanggil library numpy

def f(x):
    return x**3-2*x+1 #mendefinisikan fungsi dari soal 1 a

def my_bisection(a, b, eps):
  if np.sign(f(a)) == np.sign(f(b)):
    raise Exception('Tidak ada akar pada interval a dan b') #akan memunculkan pesan jika f(a) dan f(b) sama sama positif atau negatif
  
  #memproses pencarian akar
  while np.abs(b-a) > eps: #terus lakukan iterasi jika |f(c)| masih lebih besar dari ketelitian (epsilon)
    c = (a + b)/2
    if f(c) == 0: 
      return c
    elif f(a) * f(c) < 0:
      return my_bisection(a, c, eps)
    else:
      return my_bisection(c, b, eps)
  return (a + b)/2
    
#mencari akar menggunakan fungsi my_bisection dengan memasukkan interval (a, b) dan epsilon
akarHampiran = my_bisection(0, 1, 1e-6)

print("Akar Hampiran dari f:", akarHampiran) #hasil pencarian akar
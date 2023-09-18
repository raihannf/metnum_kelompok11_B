import numpy as np #memanggil library numpy
import math #memanggil library math supaya program dapat mengenal bilangan euler ('e')

e = math.e

def f(x): 
    return e**x-x #mendefinisikan fungsi dari soal 1 b

def my_bisection(a, b, eps):
  
  #memproses pencarian akar
  while np.abs(a-b) > eps: #terus lakukan iterasi jika |a-b| masih lebih besar dari ketelitian (epsilon)
    c = (a + b)/2
    if f(c) == 0: 
      return c
    elif f(a) * f(c) < 0:
      return my_bisection(a, c, eps)
    else:
      return my_bisection(c, b, eps)
    
  return (a + b)/2

#mencari akar menggunakan fungsi my_bisection dengan memasukkan interval (a, b) dan epsilon
akarHampiran = my_bisection(-1, 1, 1e-6)

print("Akar Hampiran dari f:", akarHampiran) #hasil pencarian akar
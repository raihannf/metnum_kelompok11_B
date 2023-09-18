import math

def f(x):
    #Soal nomor 1b
    return math.exp(x) - x

def bisection_iterasi(N):
    x = 0  #nilai x dari awal
    Iterasi = 0  #Menginisialisasi Iterasi
    #looping mencari iterasi
    while Iterasi < N:
        x_New = x - f(x) / (math.exp(x) - x) 
        if abs(x_New - x) < 1e-6:  
            break
        x = x_New
        Iterasi += 1
    return x

n = 3
root = bisection_iterasi(N)
print(f"Akar hampirannya adalah: {root}")
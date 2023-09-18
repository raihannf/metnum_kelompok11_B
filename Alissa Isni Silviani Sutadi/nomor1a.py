def f(x):
    #Soal nomor 1a
    return x**3 - 2*x + 1

def bisection_iterasi(N):
    x = 0 #nilai x dari awal
    Iterasi = 0 #Menginisialisasi Iterasi
    #looping mencari iterasi
    while Iterasi < N: 
        #mencari akar
        x_New = x - f(x) / (3*x**2 - 2)
        if abs(x_New - x) < 1e-6: 
            break
        x = x_New
        Iterasi += 1
    return x

N = 3 
root = bisection_iterasi(N)
print(f"Akar hampirannya adalah: {root}")
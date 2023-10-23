# mendefinisikan fungsi untuk menghitung hasil f siku -> f[xn, xn-1, ..., x1, x0]
def fsiku(x, fx):
    if len(fx) == 2:
        hasil = (fx[1] - fx[0]) / (x[1] - x[0])
    else:
        hasil = (
            fsiku(x[1 : len(x)], fx[1 : len(fx)])
            - fsiku(x[0 : len(x) - 1], fx[0 : len(fx) - 1])
        ) / (x[len(fx) - 1] - x[0])
    return hasil


# mendefinisikan fungsi untuk melakukan interpolasi Newton
def interpolasiNewton(a, fa, estimasi_x):
    x = [fa[0]]
    fx = fa[0]
    for i in range(len(a) - 1):
        xi = fsiku(a[0 : i + 2], fa[0 : i + 2])
        x.append(xi)
        multiElemen = xi
        for j in range(i + 1):
            multiElemen = multiElemen * (estimasi_x - a[j])
        fx = fx + multiElemen
    return [x, fx]


# input untuk memasukkan data
n = int(input("Masukkan jumlah titik data: "))
a = []
fa = []

for i in range(n):
    ai = float(input(f"Masukkan x[{i}]: "))
    fai = float(input(f"Masukkan f(x)[{i}]: "))
    a.append(ai)
    fa.append(fai)

estimasi_x = float(input("Masukkan nilai x untuk estimasi: "))

# menyelesaikan interpolasi Newton menggunakan fungsi interpolasiNewton dengan memasukkan a, fa, dan nilai estimasi x
hasil = interpolasiNewton(a, fa, estimasi_x)

# mencetak hasil estimasi
print("Hasil estimasi pada x = ", estimasi_x, " adalah ", hasil[1])

# mendefinisikan fungsi untuk menghitung hasil f siku -> f[xn, xn-1, ..., x1, x0]
def fsiku(x, fx):
    # Menghitung hasil f siku menggunakan formula Newton
    hasil = (
        fx[-1] - fx[0]
    ) / (x[-1] - x[0])
    return hasil


# mendefinisikan fungsi untuk melakukan interpolasi Newton
def interpolasiNewton(a, fa, estimasi_x):
    # Inisialisasi nilai x dan f(x)
    x = [fa[0]]
    fx = fa[0]

    # Menghitung nilai x dan f(x) secara iteratif
    for i in range(len(a) - 1, -1, -1):
        # Menghitung nilai x[i]
        xi = fsiku(a[i : len(a)], fa[i : len(a)])
        x.append(xi)

        # Menghitung nilai f(x[i])
        multiElemen = xi
        for j in range(i + 1):
            multiElemen *= (estimasi_x - a[j])
        fx += multiElemen

    return [x, fx]


# input untuk memasukkan data
n = int(input("Masukkan jumlah titik data: "))
a = []
fa = []

for i in range(n):
    # Menginput nilai x dan f(x)
    ai = float(input(f"Masukkan x[{i}]: "))
    fai = float(input(f"Masukkan f(x)[{i}]: "))

    # Menyimpan nilai x dan f(x) ke dalam list
    a.append(ai)
    fa.append(fai)

# memasukkan input nilai yang ingin diestimasi
estimasi_x = float(input("Masukkan nilai x untuk estimasi: "))

# menghitung nilai estimasi menggunakan fungsi interpolasiNewton
estimasiNilai = interpolasiNewton(a, fa, estimasi_x)

# mencetak hasil estimasi menggunakan interpolasi Newton
print("Hasil estimasi pada x =", estimasi_x, "adalah", estimasiNilai[1])

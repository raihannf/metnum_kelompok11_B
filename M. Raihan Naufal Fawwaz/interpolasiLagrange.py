# mendefinisikan fungsi untuk untuk menghitung basis polinomial Lagrange (L0(x), L1(x), ...)
def basisPoliLagrange(x, estimasi_x, k):
    n = len(x)
    hasil = 1.0

    for i in range(n):
        if i != k:
            hasil = hasil * ((estimasi_x - x[i]) / (x[k] - x[i]))

    return hasil


# mendefinisikan fungsi untuk untuk melakukan interpolasi Lagrange
def interpolasiLagrange(x, fx, estimasi_x):
    n = len(x)
    hasil = 0.0

    for k in range(n):
        basis = basisPoliLagrange(x, estimasi_x, k)
        hasil = hasil + (fx[k] * basis)

    return hasil


# input untuk memasukkan data
n = int(input("Masukkan jumlah titik data: "))
x = []
fx = []

for i in range(n):
    xi = float(input(f"Masukkan x[{i}]: "))
    fxi = float(input(f"Masukkan f(x)[{i}]: "))
    x.append(xi)
    fx.append(fxi)

# memasukkan input nilai yang ingin diestimasi
estimasi_x = float(input("Masukkan nilai x untuk estimasi: "))

# menghitung nilai estimasi menggunakan fungsi interpolasiLagrange dengan memasukkan x, fx, dan nilai estimasi x
estimasiNilai = interpolasiLagrange(x, fx, estimasi_x)

# mencetak bentuk umum polinomial Lagrange
print("Bentuk umum polinomial Lagrange:")
for k in range(len(x)):
    basis = basisPoliLagrange(x, estimasi_x, k)
    print(f"L{k}(x) = {basis}")

# mencetak hasil estimasi menggunakan interpolasi Lagrange
print("Hasil estimasi pada x =", estimasi_x, "adalah", estimasiNilai)

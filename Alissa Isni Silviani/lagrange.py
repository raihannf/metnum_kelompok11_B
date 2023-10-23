def lagrange_interpolation(x, y, x_interp):
    n = len(x)
    result = 0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (x_interp - x[j]) / (x[i] - x[j])
        result += term

    return result

# Input data dari pengguna
n = int(input("Masukkan jumlah pasangan data (n): "))
x_data = []
y_data = []

for i in range(n):
    x = float(input(f"Masukkan x[{i + 1}]: "))
    y = float(input(f"Masukkan y[{i + 1}]: "))
    x_data.append(x)
    y_data.append(y)

x_interp = float(input("Masukkan nilai x yang ingin diinterpolasi: "))

# Menghitung interpolasi Lagrange
final_result = lagrange_interpolation(x_data, y_data, x_interp)

# Mencetak bentuk umum polinomial Lagrange
print("Bentuk umum polinomial Lagrange:")
results = []
for k in range(len(x_data)):
    basis = f"L{k}(x) = "
    result = 1.0
    for i in range(len(x_data)):
        if i != k:
            basis += f"(x - {x_data[i]:.1f}) / ({x_data[k] - x_data[i]:.1f})"
            result *= (x_interp - x_data[i]) / (x_data[k] - x_data[i])
            if i != len(x_data) - 1:
                basis += " * "
    results.append(result)
    print(f"{basis} = {result:.3f}")

# Mencetak hasil
print(f"Hasil interpolasi pada x = {x_interp} adalah {final_result:.3f}")
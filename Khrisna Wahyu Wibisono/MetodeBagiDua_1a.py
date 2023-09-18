# Nama: Khrisna Wahyu Wibisono
# NIM: 2204340
# Buatlah sebuah fungsi penyelesaian yang tepat baik dengan menggunakan metode Bagi Dua ketika
# a. f(x) = x^3 - 2x + 1
# Buatlah modifikasi fungsi ketika kriteria program berhenti adalah sudah mencapai pada iterasi ke-n

def f(x): #Menisialisasi fungsi yang digunakan
    return x**3 - 2*x + 1 #fungsi f(x) = x^3 - 2x + 1

def BagiDua_Iterasi_N(N):
    x = 0  # Nilai awal dari x
    Iterasi = 0  #Inisialisasi hitungan iterasi

    #Melakukan Perulangan untuk mencari Iterasi k-N
    while Iterasi < N: 
        x_new = x - f(x) / (3*x**2 - 2)  # Metode untuk mencari akar
        if abs(x_new - x) < 1e-6:  # Kondisi dimana program akan berhenti jika perbedaan sangat kecil
            break
        x = x_new
        Iterasi += 1

    return x

N = 3  # Ganti dengan nilai n yang Anda inginkan
root = BagiDua_Iterasi_N(N)
print(f"Akar setelah iterasi ke {N} adalah: {root}")
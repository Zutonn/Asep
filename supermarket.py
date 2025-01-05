import sys

# Data stok barang disimpan di luar fungsi agar tetap konsisten
items = {
    1: ("Downy", 23000, 50),  # (Nama Barang, Harga, Stok)
    2: ("Baygon", 41100, 50),
    3: ("Mamy Poko", 59000, 50),
    4: ("Ovaltine", 23000, 50),
    5: ("Beras", 70000, 50)
}

def tampilkan_daftar_barang():
    print(" No | Nama Barang | Harga | Stok")
    print("-------------------------------")
    for key, value in items.items():
        print(f" {key}  | {value[0]:<12} | {value[1]} | {value[2]}")
    print("-------------------------------")

def daftar_barang():
    global items  # Menggunakan variabel items yang sudah didefinisikan di luar fungsi
    while True:
        tampilkan_daftar_barang()
        
        try:
            kode = int(input("Masukkan angka barang  : "))
            if kode in items:
                if items[kode][2] == 0:  # Cek jika stok habis
                    print(f"Stok {items[kode][0]} habis!")
                    continue
                
                jumlah = int(input("Masukkan jumlah barang : "))
                if jumlah > items[kode][2]:
                    print("Stok tidak mencukupi!")
                    continue
                
                total_price = items[kode][1] * jumlah
                items[kode] = (items[kode][0], items[kode][1], items[kode][2] - jumlah)  # Kurangi stok
                print(f"Stok {items[kode][0]} tersisa: {items[kode][2]}")
                
                if items[kode][2] == 0:  # Cek jika stok habis setelah pembelian
                    print(f"Stok {items[kode][0]} habis!")
                
                return total_price  # Kembalikan total harga untuk transaksi ini
            else:
                print("Barang tidak ditemukan!")
                continue
        except ValueError:
            print("Input tidak valid! Silakan masukkan angka.")
            continue

def akhir(total_transaksi):
    subtotal = sum(total_transaksi)
    print("\n-------------------------------")
    print("SubTotal         : ", subtotal)
    
    # Diskon
    diskon = 0
    if subtotal > 500000:
        diskon = subtotal * 8 / 100
    elif subtotal > 300000:
        diskon = subtotal * 5 / 100
    elif subtotal > 200000:
        diskon = subtotal * 3 / 100
    elif subtotal > 100000:
        diskon = subtotal * 1 / 100
    
    print("Potongan Harga   : ", diskon)
    totalakhir = subtotal - diskon
    print("Total            : ", totalakhir)
    print("-------------------------------")
    
    while True:
        try:
            bayar = int(input("Bayar            :  "))
            if bayar < totalakhir:
                print("Jumlah bayar tidak cukup!")
                continue
            kembalian = bayar - totalakhir
            print("Kembalian        : ", kembalian)
            break
        except ValueError:
            print("Input tidak valid! Silakan masukkan angka.")
    
    print("-------------------------------")
    print("          Terima Kasih         ")
    print("-------------------------------")

# Loop utama untuk kembali ke menu awal
def main():
    while True:
        total_transaksi = []  # Reset total transaksi untuk transaksi baru
        while True:
            total_harga = daftar_barang()
            total_transaksi.append(total_harga)
            
            tanya = input("Ingin tambah barang? [y/t] : ")
            if tanya.lower() != 'y':
                break
        
        akhir(total_transaksi)
        
        ulangi = input("Apakah Anda ingin melakukan transaksi baru? [y/t] : ")
        if ulangi.lower() != 'y':
            print("Program selesai. Terima kasih!")
            break

# Memanggil fungsi utama untuk memulai program
main()
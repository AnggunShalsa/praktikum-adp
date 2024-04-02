# Daftar barang beserta harga per pcs
daftar_barang = {
    'A': {'nama': 'Buku', 'harga': 50000},
    'B': {'nama': 'Pensil', 'harga': 2000},
    'C': {'nama': 'Pensil Warna', 'harga': 10000},
    'D': {'nama': 'Penghapus', 'harga': 5000}
}

# Fungsi untuk menghitung total harga belanjaan
def hitung_total_belanja(daftar_belanja):
    total = 0
    for barang, jumlah in daftar_belanja.items():
        total += daftar_barang[barang]['harga'] * jumlah
    return total

# Input jenis barang dan jumlah barang yang dibeli
daftar_belanja = {}
while True:
    kode_barang = input("Masukkan kode barang (A/B/C/D) atau ketik 'selesai' untuk selesai belanja: ").upper()
    if kode_barang == 'SELESAI':
        break
    elif kode_barang not in daftar_barang:
        print("Kode barang tidak valid. Silakan masukkan kembali.")
        continue
    jumlah_barang = int(input(f"Masukkan jumlah {daftar_barang[kode_barang]['nama']}: "))
    if jumlah_barang <= 0:
        print("Jumlah barang harus lebih dari 0. Silakan masukkan kembali.")
        continue
    if kode_barang in daftar_belanja:
        daftar_belanja[kode_barang] += jumlah_barang
    else:
        daftar_belanja[kode_barang] = jumlah_barang

# Berikan promo atau diskon potongan harga untuk barang tertentu
for barang, jumlah in daftar_belanja.items():
    if barang == 'A' and jumlah > 3:
        diskon = 0.25 * daftar_barang[barang]['harga'] * (jumlah // 3)
        print(f"Diskon untuk {daftar_barang[barang]['nama']}: Rp{diskon}")
        total_diskon = diskon if 'total_diskon' not in locals() else total_diskon + diskon

# Hitung total harga belanjaan
total_belanja = hitung_total_belanja(daftar_belanja)

# Berikan promo atau diskon potongan harga untuk total belanja
if total_belanja > 200000:
    diskon_total = 0.1 * total_belanja
    print(f"Diskon total: Rp{diskon_total}")
    total_diskon = diskon_total if 'total_diskon' not in locals() else total_diskon + diskon_total

# Hitung total harga setelah diskon
total_setelah_diskon = total_belanja - total_diskon if 'total_diskon' in locals() else total_belanja

# Output
print("======= STRUK BELANJA =======")
for barang, jumlah in daftar_belanja.items():
    print(f"{daftar_barang[barang]['nama']} ({jumlah} pcs) : Rp{daftar_barang[barang]['harga']*jumlah}")
print("==============================")
print(f"Total Belanja: Rp{total_belanja}")
if 'total_diskon' in locals():
    print(f"Total Diskon: Rp{total_diskon}")
print(f"Total yang harus dibayar: Rp{total_setelah_diskon}")
print("==============================")

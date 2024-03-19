#include <iostream>
#include <string>
#include <map>

using namespace std;

// Map untuk menyimpan harga paket makanan
map<char, int> harga_paket = {
    {'A', 25000},
    {'B', 30000},
    {'C', 45000}
};

// Fungsi untuk menghitung biaya ongkir berdasarkan jarak
int hitung_ongkir(float jarak) {
    if (jarak < 0) {
        cout << "Jarak tidak boleh negatif." << endl;
        return -1; // Mengembalikan nilai negatif untuk menandakan kesalahan
    } else if (jarak <= 5) {
        return 5000;
    } else if (jarak <= 10) {
        return 10000;
    } else {
        return 15000;
    }
}

int main() {
    char paket_pilihan;
    float jarak;

    // Menampilkan daftar paket makanan beserta harganya
    cout << "Daftar Paket Makanan:" << endl;
    for (auto const& pair : harga_paket) {
        cout << "Paket " << pair.first << ": Rp " << pair.second << endl;
    }

    // Meminta input paket yang akan dipesan
    cout << "Masukkan pilihan paket (A/B/C): ";
    cin >> paket_pilihan;

    // Memeriksa apakah paket yang dimasukkan oleh pelanggan valid
    if (harga_paket.find(paket_pilihan) == harga_paket.end()) {
        cout << "Pilihan paket tidak valid. Silakan pilih antara paket A, B, atau C." << endl;
        return 1; // Keluar dari program jika input tidak valid
    }

    // Meminta input jarak rumah pelanggan
    cout << "Masukkan jarak rumah Anda dari restoran (dalam km): ";
    cin >> jarak;

    // Menghitung biaya ongkir
    int ongkir = hitung_ongkir(jarak);
    if (ongkir == -1) {
        return 1; // Keluar dari program jika jarak negatif
    }

    // Menghitung total biaya berdasarkan paket yang dipilih dan jarak
    int total_biaya = harga_paket[paket_pilihan] + ongkir;
    cout << "Total biaya yang perlu dibayar: Rp " << total_biaya << endl;

    return 0;
}

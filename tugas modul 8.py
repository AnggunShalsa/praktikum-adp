import json
import os

# Nama file untuk menyimpan data film
FILE_NAME = 'data_film.txt'

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

def display_menu():
    print("\nMenu:")
    print("1. Menambah data film")
    print("2. Menghapus data film")
    print("3. Mengedit data film")
    print("4. Menampilkan data film")
    print("5. Keluar")

def add_film(data):
    title = input("Masukkan judul film: ")
    if title in data:
        print("Film sudah ada dalam database.")
        return
    writer = input("Masukkan nama penulis skenario: ")
    director = input("Masukkan nama sutradara: ")
    release_year = input("Masukkan tahun rilis: ")
    data[title] = {
        'penulis': writer,
        'sutradara': director,
        'tahun_rilis': release_year
    }
    save_data(data)
    print("Data film berhasil ditambahkan.")

def delete_film(data):
    title = input("Masukkan judul film yang ingin dihapus: ")
    if title in data:
        del data[title]
        save_data(data)
        print("Data film berhasil dihapus.")
    else:
        print("Film tidak ditemukan.")

def edit_film(data):
    title = input("Masukkan judul film yang ingin diedit: ")
    if title in data:
        writer = input("Masukkan nama penulis skenario baru: ")
        director = input("Masukkan nama sutradara baru: ")
        release_year = input("Masukkan tahun rilis baru: ")
        data[title] = {
            'penulis': writer,
            'sutradara': director,
            'tahun_rilis': release_year
        }
        save_data(data)
        print("Data film berhasil diperbarui.")
    else:
        print("Film tidak ditemukan.")

def display_films(data):
    if data:
        for title, info in data.items():
            print(f"Judul: {title}")
            print(f"Penulis Skenario: {info['penulis']}")
            print(f"Sutradara: {info['sutradara']}")
            print(f"Tahun Rilis: {info['tahun_rilis']}\n")
    else:
        print("Tidak ada data film.")

def main():
    data = load_data()
    while True:
        display_menu()
        choice = input("Pilih opsi (1-5): ")
        if choice == '1':
            add_film(data)
        elif choice == '2':
            delete_film(data)
        elif choice == '3':
            edit_film(data)
        elif choice == '4':
            display_films(data)
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
from prettytable import PrettyTable
import pwinput
import os
data_pelanggaran = []
data_user = {"Mahasiswa": {"password": "123", "role": "user"}}
data_admin = {"admin": {"password": "321", "role": "admin"}}

def lihat_data():
    tabel = PrettyTable()
    tabel.field_names = ["No", "NIM", "Nama", "Pelanggaran", "Poin"]

    if not data_pelanggaran:
        print("Bruh Tambah dulu datanya, baru bisa liat.")
        return

    # Membaca data berbasis Tuple menggunakan enumerate
    for nomor, info in enumerate(data_pelanggaran, start=1):
        nim, nama, pelanggaran, poin = info
        tabel.add_row([nomor, nim, nama, pelanggaran, poin])
    
    print(tabel)

print(" SISTEM PELANGGARAN MAHASISWA ")
user_input = input("Masukkan username: ").strip()
pass_input = pwinput.pwinput("Masukkan password: ")

# Verifikasi login
if user_input in data_admin and data_admin[user_input]["password"] == pass_input:
    print("Login berhasil sebagai admin.")
elif user_input in data_user and data_user[user_input]["password"] == pass_input:
    print("Login berhasil sebagai user.")
else:
    print("Username atau password salah.")
    exit()

role = data_admin[user_input]["role"] if user_input in data_admin else data_user[user_input]["role"]

if role == "admin":
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nMenu Sistem Pelanggaran Mahasiswa (Admin)")
        print("1. Tambah data pelanggaran")
        print("2. Lihat data pelanggaran")
        print("3. Edit data pelanggaran")
        print("4. Hapus data pelanggaran")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ").strip()
    
        # OPSI 1: TAMBAH DATA
        if pilihan == "1":
            print("\nTambah Data Pelanggaran")
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()
            pelanggaran = input("Masukkan Jenis Pelanggaran: ").strip()
            poin = input("Masukkan Poin Pelanggaran: ").strip()

            if not nim.isdigit():
                print("NIM/Poin harus angka ganteng/cantik :). Data pelanggaran tidak ditambahkan.")
                input("Pencet itu enter buat lanjut...")
            elif not poin.isdigit():
                print("NIM/Poin harus angka ganteng/cantik :). Data pelanggaran tidak ditambahkan.")
                input("Pencet itu enter buat lanjut...")
            else:
                data_pelanggaran.append((nim, nama, pelanggaran, int(poin)))
                print("Data pelanggaran sudah ditambahkan!")
                input("if you want to continue, press enter...")

        # OPSI 2: LIHAT DATA
        elif pilihan == "2":
            lihat_data()
            input("Tekan enter untuk melanjutkan...")

        # OPSI 3: EDIT DATA
        elif pilihan == "3":
            print("\nEdit Data Pelanggaran")
            if not data_pelanggaran:
                print("Belum Ada Data Pelanggaran")
                input("Tekan enter untuk melanjutkan...")
            else:
                lihat_data()
                input_index = input("Masukkan nomor data yang ingin diedit: ").strip()
                
                if input_index.isdigit():
                    index = int(input_index) - 1
                    if 0 <= index < len(data_pelanggaran):
                        nim = input("Masukkan NIM baru: ").strip()
                        nama = input("Masukkan Nama baru: ").strip()
                        pelanggaran = input("Masukkan Jenis Pelanggaran baru: ").strip()
                        poin = input("Masukkan Poin Pelanggaran baru: ").strip()

                        if not poin.isdigit():
                            print("Poin harus berupa angka. Data pelanggaran tidak diubah.")
                        else:
                            data_pelanggaran[index] = (nim, nama, pelanggaran, int(poin))
                            print("Data pelanggaran berhasil diubah.")
                    else:
                        print("Nomor data tidak valid.")
                else:
                    print("Nomor data harus berupa angka!")
                input("Tekan enter untuk melanjutkan...")

        # OPSI 4: HAPUS DATA 
        elif pilihan == "4":
            print("\nHapus Data Pelanggaran")
            if not data_pelanggaran:
                print("Belum Ada Data Pelanggaran")
                input("Tekan enter untuk melanjutkan...")
            else:
                lihat_data()
                input_index = input("Masukkan nomor data yang ingin dihapus: ").strip()
                
                if input_index.isdigit():
                    index = int(input_index) - 1
                    if 0 <= index < len(data_pelanggaran):
                        del data_pelanggaran[index]
                        print("Data pelanggaran berhasil dihapus.")
                    else:
                        print("Nomor data tidak valid.")
                else:
                    print("Nomor data harus berupa angka!")
                input("Tekan enter untuk melanjutkan...")

        # OPSI 5: KELUAR 
        elif pilihan == "5":
            print("Anda Keluar dari Program.")
            break
            
        else:
            print("Pilihan bukan menu yang tersedia. Silakan pilih menu yang tersedia.")
            input("Tekan enter untuk melanjutkan...")

else:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nMenu Sistem Pelanggaran Mahasiswa (User)")
        print("1. Lihat data Pelanggaran")
        print("2. Keluar")

        pilihan = input("Pilih menu (1/2): ").strip()

        # OPSI 1:
        if pilihan == "1":
            lihat_data()
            input("Tekan enter untuk melanjutkan...")

        # OPSI 2:
        elif pilihan == "2":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih 1 atau 2.")
            input("Tekan enter untuk melanjutkan...")
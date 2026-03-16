print(f"""
==================================
    KALKULATOR OPERATOR PYTHON
==================================
========== DAFTAR MENU ===========
[1] OPERATOR ARITMATIKA
[2] OPERATOR PERBANDINGAN
[3] OPERATOR PENUGASAN
[4] LOGIKA BOOLEAN
[0] KELUAR
==================================:""")
# funsi aritmatika
def aritmatika (pilihan, angka1, angka2):
    if pilihan == "1":
        total = angka1 + angka2
        return f"Penjumlahan {angka1} + {angka2} = {total}"
    elif pilihan == "2":
        total = angka1 - angka2
        return f"Pengurangan {angka1} - {angka2} = {total}"
    elif pilihan == "3":
        total = angka1 * angka2
        return f"Perkalian {angka1} * {angka2} = {total}"
    elif pilihan == "4":
        total = angka1 / angka2
        return f"Pembagian {angka1} / {angka2} = {total}"
    elif pilihan == "5":
        total = angka1 % angka2
        return f"Modulo {angka1} % {angka2} = {total}"
    return "rawr error"
# fungsi perbandingan
def perbandingan (pilihan, angka1, angka2):
    hasil = "SALAH"
    if pilihan == "1":
        if angka1 == angka2:
            hasil = "BENAR"
        return f"Hasil Perbandingan apakah {angka1} SAMA DENGAN {angka2} adalah {hasil}"
    elif pilihan == "2":
        if angka1 > angka2:
            hasil = "BENAR"
        return f"Hasil Perbandingan apakah {angka1} LEBIH BESAR {angka2} adalah {hasil}"
    elif pilihan == "3":
        if angka1 < angka2:
            hasil = "BENAR"
        return f"Hasil Perbandingan apakah {angka1} LEBIH KECIL {angka2} adalah {hasil}"
    elif pilihan == "4":
        if angka1 >= angka2:
            hasil = "BENAR"
        return f"Hasil Perbandingan apakah {angka1} LEBIH BESAR ATAU SAMA DENGAN {angka2} adalah {hasil}"
    elif pilihan == "5":
        if angka1 <= angka2:
            hasil = "BENAR"
        return f"Hasil Perbandingan apakah {angka1} LEBIH KECIL ATAU SAMA DENGAN {angka2} adalah {hasil}"
    elif pilihan == "6":
        if angka1 != angka2:
            hasil = "BENAR"
        return f"Hasil Perbandingan apakah {angka1} TIDAK SAMA DENGAN {angka2} adalah {hasil}"
    return "rawr error"
# fungsi penugasan
def penugasan (pilihan, angka, penugasan):
    hasil = angka
    if pilihan == "1":
        hasil += penugasan
        return hasil
    elif pilihan == "2":
        hasil -= penugasan
        return hasil
    elif pilihan == "3":
        hasil *= penugasan
        return hasil
    elif pilihan == "4":
        hasil /= penugasan
        return hasil
    elif pilihan == "5":
        hasil %= penugasan
        return hasil
    return "rawr"
# fungsi boolean
def boolean (pilihan, nama, password):
    # data
    akun = {
            "nama": "wendy",
            "password": "123",
            "darurat": {
                "nama": "wendy",
                "password": "000"
            },
            "akun_banned": {
                "nama": "asep",
            }
        }
    # pengecekan data
    if pilihan == "1":
        if nama == akun["nama"] and password == akun["password"]:
            akun = "Berhasil Masuk"
            return akun
        else:
            akun = "Gagal Masuk"
            return akun
    elif pilihan == "2":
        if nama == akun["nama"] and password == akun["password"]:
            akun = "Berhasil Masuk"
            return akun
        elif nama == akun["darurat"]["nama"] or password == akun["darurat"]["password"]:
            akun = "Brhasil Masuk dengan Mode DARURAT"
            return akun
        else:
            akun = "Gagal Masuk"
            return akun
    elif pilihan == "3":
        if nama != akun["akun_banned"]["nama"]:       
            if nama == akun["nama"] and password == akun["password"]:
                akun = "Berhasil Masuk dengan akun utama"
                return akun
            elif nama == akun["darurat"]["nama"] or password == akun["darurat"]["password"]:
                akun = "Brhasil Masuk dengan Mode DARURAT"
                return akun
            else:
                akun = "GAGAL MASUK"
                return akun
        akun = f"Akun {akun['akun_banned']["nama"]} Terblokir karena melakukan pelanggaran"
        return akun
    else:
        return "Maaf, Menu Tidak tersedia."
# ulangi -> untuk mengulang pilihan menu secara otomatis  
ulangi = True
while ulangi:
    
    pilih_menu = input("Pilih menu: ")
    # validasi input user
    if pilih_menu != "0" and pilih_menu != "1" and pilih_menu != "2" and pilih_menu != "3" and pilih_menu != "4":
        print("Maaf, Menu tidak tersedia! Pilih y untuk melanjutkan atau n untuk keluar!")
        ulangi = False
        # validasi ke 2 untuk mengecek apakah user ingin mencoba lagi atau tidak
        coba_lagi = input("mau coba lagi? (y/n): ")
        # validasi bila input user selain dari y/n maka sistem otomatis keluar 
        if coba_lagi != "y" and coba_lagi != "n":
            print("kesalahan input, sistem otomatis keluar")
            break
        elif coba_lagi == "y":
            ulangi = True
        elif coba_lagi == "n":
            print("Terima kasih sudah berkunjung")
            break
        # akhir validasi coba lagi
    # sistem otomatis keluar bila user mengetik 0 
    elif pilih_menu == "0":
        print("Terima kasih sudah berkunjung")
        break
    # user memilih menu 1
    elif pilih_menu == "1":
        print(f"""=== OPERATOR ARITMATIKA ===
    [1] PENJUMLAHAN (+)
    [2] PENGURANGAN (-)
    [3] PERKALIAN (*)
    [4] PEMBAGIAN (/)
    [5] SISA BAGI (%)""")
        
        operator_aritmatika = input("Pilih Operator : ")
        # validasi apakah menu operator aritmatika yang dipilih user apakah tersedia atau tidak
        if operator_aritmatika in ["1", "2", "3", "4", "5"]:
            angka1 = float(input("Masukan angka 1: "))
            angka2 = float(input("Masukan angka 2: "))
            hasil = aritmatika(operator_aritmatika, angka1, angka2)
            print(f"Hasil {hasil}")
        else:
        # output menu operator aritmatika yang dipilih user tidak tersedia
            print("Maaf, Operator tidak tersedia. hanya (+, -, *, /, %)")
    # user memilih menu 2 
    elif pilih_menu == "2":
        print(f"""=== OPERATOR PERBANDINGAN ===
[1] SAMA DENGAN (==)
[2] LEBIH BESAR (>)
[3] LEBIH KECIL (<)
[4] LEBIH BESAR ATAU SAMA DENGAN (>=)
[5] LEBIH KECIL ATAU SAMA DENGAN (<=)
[6] TIDAK SAMA DENGAN (!=)""")
        operator_perbandingan = input("Pilih Operator : ")
        if operator_perbandingan in ["1", "2", "3", "4", "5", "6"]:
        # validasi apakah menu operator perbandingan yang dipilih user apakah tersedia atau tidak
            angka1 = int(input("Masukan angka 1: "))
            angka2 = int(input("Masukan angka 2: "))
            hasil = perbandingan(operator_perbandingan, angka1, angka2)
            print(hasil)
        else:
        # output menu operator perbandingan yang dipilih user tidak tersedia
            print("Maaf, Operator tidak tersedia. hanya (==, >, <, >=, <=, !=)")
    # user memilih menu 3
    elif pilih_menu == "3":
        print(f"""=== OPERATOR PENUGASAN ===
[1] PENGISIAN DAN PENAMBAHAN (+=)
[2] PENGISIAN DAN PENGURANGAN (-=)
[3] PENGISIAN DAN PERKALIAN (*=)
[4] PENGISIAN DAN PEMBAGIAN (/=)
[5] PENGISIAN DAN MODULO (%=)""")
        menu_operator = {"1" : "tambah", "2": "kurang", "3": "kali", "4": "bagi", "5": "modulo"}
        operator_penugasan = input("Pilih Operator penugasan: ")
        # {ulang = true} untuk menjalankan looping while bila user ingin menambahkan inputan baru
        ulang2 = True
        # validasi apakah menu operator penugasan yang dipilih user apakah tersedia atau tidak
        if operator_penugasan in ["1", "2", "3", "4", "5", "6"]:
            # value variabel {aksi} yang akan di tambahkan ke value variabel {angka_penugasan}
            if operator_penugasan == "1":
                aksi = menu_operator["1"]
            elif operator_penugasan == "2":
                aksi = menu_operator["2"]
            elif operator_penugasan == "3":
                aksi = menu_operator["3"]
            elif operator_penugasan == "4":
                aksi = menu_operator["4"]
            elif operator_penugasan == "5":
                aksi = menu_operator["5"]
            angka_usr = int(input("Masukan Angka awal: "))
            # {ulang2} untuk mengecek apakah user ingin menambahkan inputan baru atau tidak
            while ulang2:
                # variabel aksi akan di tambahkan di sini
                angka_penugasan = float(input(f"Mau {aksi} berapa?: "))
                hasil = penugasan(operator_penugasan, angka_usr, angka_penugasan)
                print(hasil)
                angka_usr = hasil
                # validasi apakah user mau mencoba memasukan angka baru atau tidak
                tambah_lagi = input("Mau nyoba lagi? (y/n): ")
                if tambah_lagi == "y":
                    # validasi looping akan kembali di jalankan bila user mengetik y
                    ulang2 = True
                elif tambah_lagi == "n":
                    # validasi looping akan berhenti di jalankan bila user mengetik n
                    ulang2 = False
                    break
                else:
                    # output bila user melakukan kesalahan input selain dari y/n
                    print("kesalahan input, sistem kembali ke menu utama!")
                    break
        else:
        # v apakah menu operator penugasan yang dipilih user apakah tersedia atau tidak
            print("Maaf, Operator tidak tersedia. hanya (+=, -=, *=. /=, %=)")
    # user memilih menu 3
    elif pilih_menu == "4":
        print(f"""=== LOGIKA BOOLEAN ===
[1] DAN (AND)
[2] ATAU (OR)
[3] NEGASI (NOT)""")
        operator_boolean = input("Pilih Operator boolean: ")
        # validasi apakah menu operator bool yang dipilih user apakah tersedia atau tidak
        if operator_boolean in ["1", "2", "3"]:
            user_name = input("Masukan nama: ")
            user_password = input("Masukan password: ")
            user_akun = boolean(operator_boolean, user_name, user_password)
            print(user_akun)
        else:
        # output menu operator bool yang dipilih user tidak tersedia
            print("Maaf, Operator tidak tersedia. hanya (AND, OR, NOT)")
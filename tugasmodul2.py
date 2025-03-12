
DAFTAR = "DAFTAR JUDUL FILM DAN HARGA TIKET"

F_1 = (" Kode film: 1 \n    Judul Film: Antara Dia dan Kalkulus\n    Harga tiket: RP 47.000")
F_2 = (" Kode film: 2 \n    Judul Film: Aksara Wanita Muslimah \n    Harga Tiket: RP 55.000")
F_3 = (" Kode film: 3 \n    Judul Film: Di Balik Suara Samudra \n    Harga Tiket: RP 30.000")
F_4 = (" Kode film: 4 \n    Judul Film: Jika Hujan Tak Datang  \n    Harga Tiket: RP 35.000")
F_5 = (" Kode film: 5 \n    Judul Film: Sepatu Penukar Jiwa    \n    Harga Tiket: RP 60.000")

K1 = "Antara Dia dan Kalkulus"
K2 = "Aksara Wanita Muslimah"  
K3 = "Di Balik Suara Samudra"
K4 = "Jika Hujan Tak Datang"
K5 = "Sepatu Penukar Jiwa "

#TAMPILAN 1
LIST = (f"(1){F_1}\n(2){F_2}\n(3){F_3}\n(4){F_4}\n(5){F_5}")
print(DAFTAR)
print(LIST)
print("\n")

#TAMPILAN 2
Nama_pelanggan = str(input("Silahkan masukkan nama pelanggan:   "))
kode_film = int(input("Silahkan masukkan kode film:            "))
jumlah_tiket= int(input("Jumlah pembelian tiket:                "))
print(" ")

if kode_film == 1 :
    print(f'Judul film           = ',K1) 
    harga = 47000
    Judul = K1
elif kode_film == 2 :
    print(f'Judul film           = ',K2)
    harga = 55000
    Judul = K2
elif kode_film == 3 :
    print(f'Judul film           = ',K3)
    harga = 30000
    Judul = K3
elif kode_film == 4 :
    print(f'Judul film           = ',K4)
    harga = 35000
    Judul = K4
elif kode_film == 5 :
    print(f'Judul film           = ',K5)
    harga = 60000
    Judul = K5
else :
    print("kode film tidak valid")


total_harga = harga*jumlah_tiket
print("Harga satuan tiket   = RP ", harga)
print("Total Harga Tiket    = RP ", total_harga,)


if 100000<total_harga<250000 :
    print("(Selamat, anda mendapatkan diskon sebesar 15%)")
    diskon = 0.15*total_harga
    print(f'Potongan harga       = RP ', diskon)
elif total_harga> 250000 :
    print("(Selamat, anda mendapat diskon sebesar 35%)")
    diskon = 0.15*total_harga
    print(f'Potongan harga       = RP ', diskon)
else :
    diskon = 0
    print(f'Potongan harga       = RP 0')
setelah_diskon = total_harga - diskon
Harga_akhir = setelah_diskon
if Harga_akhir == setelah_diskon :
    print(f'Total Harga          = RP {Harga_akhir}(setelah potongan harga)')
else :
    print(f'Total Harga= ', Harga_akhir = total_harga)
print("\n")


#TAMPILAN 3
S = ("STRUK PEMESANAN")

print(S)
print(f'Nama            :',Nama_pelanggan)
print(f'Judul Film      :',Judul)
print(f'Jumlah Tiket    :', jumlah_tiket)
print(f'Harga Satuan    : RP ',harga)
print(f'Potongan Harga  : RP ', diskon)
print(f'Total Harga     : RP ', Harga_akhir)




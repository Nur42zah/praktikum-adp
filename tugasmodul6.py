print("-----"*20)
print("PROGRAM ARRAY 2D MENCARI INDEKS PRESTASI (IP) MAHASISWA")
print("-----"*20)

#list indeks prestasi
Huruf =['A','A-','B+','B','B-','C+','C','D','E']
Nilai =[4.00,3.75,3.50,3.00,2.75,2.50,2.00,1.00,0.00]

#PROGRAM UTAMA
jmlh_mahasiswa = int(input(f'Input banyaknya mahasiswa =   '))
matkul = int(input(f'Input banyaknya mata kuliah yang diambil = '))
print( )    
Data_mahasiswa = []
for i in range (jmlh_mahasiswa):
    print()
    print(f'Mahasiswa ke-{i+1}')
    nama = str(input('Nama mahasiswa : '))
    nilai = []
    total_nilai = 0
    for j in range(matkul):
        b = input(f'Nilai matkul {j+1} = ').upper()
        nilai.append(b)
        total_nilai+= Nilai[Huruf.index(b)]
    IP = total_nilai / matkul
    Data_mahasiswa.append([nama,nilai,IP])
    print(Data_mahasiswa)
print( ) 
k = len(Data_mahasiswa)
for i in range(k):
    for j in range(i+1,k):
        if Data_mahasiswa[i][2] < Data_mahasiswa[j][2]:
            r = Data_mahasiswa[i]
            Data_mahasiswa[i] = Data_mahasiswa[j]
            Data_mahasiswa[j] = r

#PEMBUATAN TABEL
print('---'*18)    
print('       TABEL NILAI INDEKS PRESTASI (IP) MAHASISWA   ')
print('---'*18)
print(f'{'Nama':<10}{'Nilai':>15}{'IP':>20}')
print('---'*18)
for p in Data_mahasiswa:
    nama = p[0]
    n_str = ','.join(p[1])
    ip = p[2]
    print(f'{nama:<10}{n_str:<15}{ip:<20}')
print('---'*18)
print("_______________________PROGRAM SELESAI___________________")
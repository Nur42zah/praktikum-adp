PROGRAM = 'PROGRAM MEMBUAT POLA X DAN O'
print('==========================================')
print(PROGRAM)
print('==========================================')
print("Silahkan input jumlah baris dan kolom yang Anda inginkan")
B = int(input("Masukkan jumlah baris = "))
K = int(input("Masukkan jumlah kolom = "))
i = 1
j = 1
print()
for i in range(1,B+1) :
    for j in range(1,K+1):
        if (i + j) % 2 == 0:
            print( 'X', end="   ")
        else :
            print( 'O', end="   ")
    print()
print()
print("Pola yang Anda inginkan telah selesai!")
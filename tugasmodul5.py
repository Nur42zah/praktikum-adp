#fungsi f(x), g(x), dan h(x)

print("OUTPUT 1 :")
print("\tf(x) = 4x**3 + 7x – 5,  x≥0")
print("\t     = 3x**2 + 5x + 1,  x<0")
print("\tg(x) = (f(x))**2 – f(x)")
print("\th(x) = f(x) * g(x)")
print()

#PROGRAM UTAMA
x = []
f = []
g = []
h = []
n = int(input("Input banyak data n : "))
for i in range (n):
    print("Input x ke",i+1,":",end=" ")
    b = int(input(''))
    x.append(b)

    if b >= 0:
        f_x= 4*(b**3) + 7*b - 5
    elif b < 0:
        f_x= 3*(b**2) + 5*b + 1
    else:
        f_x = None

    g_x = (f_x)**2 - f_x
    h_x = f_x * g_x

    f.append(f_x)
    g.append(g_x)
    h.append(h_x)
print()
print("OUTPUT 2 : ")
print('----'* 18)
print('|No  |\tx\t|\tf(x)\t|\tg(x)\t|\th(x)\t\t|')
print('----'* 18)
for i in range (n):
    print(f'|{i+1}   |\t{x[i]}\t|\t{f[i]}\t|\t{g[i]}\t|\t{h[i]:<8}\t|')
print()

while True:
    ulang_x= input("Input nilai x lagi (Y/N)? ").upper()
    if ulang_x != 'Y':
        print("PROGRAM SELESAI!")
        break
    else:
        x_baru = []
        f_baru = []
        g_baru = []
        h_baru = []
        n_baru = int(input("Masukkan nilai n baru: "))
        for i in range(n_baru):
            print("Input x ke",i + 1,":",end=" ")
            y = int(input(''))
            x_baru.append(y)

            if y >= 0:
                 f_y= 4*(y**3) + 7*y - 5
            elif y < 0:
                 f_y= 3*(y**2) + 5*y + 1
            else:
                 print(" ")
            g_y = (f_y)**2 - f_y
            h_y = f_y * g_y

            f_baru.append(f_y)
            g_baru.append(g_y)
            h_baru.append(h_y)

        x.extend(x_baru)  # Menggabungkan list x
        f.extend(f_baru)  # Menggabungkan list f
        g.extend(g_baru)  # Menggabungkan list g
        h.extend(h_baru)  # Menggabungkan list h
    print()
    print("OUTPUT 2 : ")
    print('----' * 18)
    print('|No  |\tx\t|\tf(x)\t|\tg(x)\t|\th(x)\t\t|')
    print('----' * 18)
    for i in range(len(x)):
        print(f'|{i+1}   |\t{x[i]}\t|\t{f[i]}\t|\t{g[i]}\t|\t{h[i]:<8}\t|')
    print()
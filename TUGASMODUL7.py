print("==="*20)
print('   PROGRAM MENGHITUNG KECEPATAN YANG DITEMPUH DALAM GLBB  ')
print("==="*20)
print()
n =int(input("Masukkan banyak data= "))
def vt_dan_s(v0,a,t):
    vt = v0 + a*t
    s = v0*t+0.5*a*t**2
    return vt,s

def input_data(n):
    data =[ ]
    for i in range(n):
        print(f"n ke-{i+1}:")
        v0 = float(input("kecepatan awal:  "))
        a = float(input("percepatan:    "))
        t = float(input("waktu:   ",))
        kec_akhir,jarak = vt_dan_s(v0,a,t)
        data.append((v0,a,t,kec_akhir,jarak))
    return data
data = input_data(n)
print()
print('-------'*12)
print("                               TABEL HASIL PERHITUNGAN                            ")
def print_data(data):
    print('-------'*12)
    print("|n| Kecepatan awal | Percepatan | Waktu  | Kecepatan akhir  | Jarak   |")
    print('-------'*12)

    i=1
    for kec_awal,percepatan,waktu,kec_akhir,jarak in data:
        print(f"|{i:<1}|{kec_awal:<16.0f}|{percepatan:<11.0f} |{waktu:<8.0f}|{kec_akhir:<18.0f}|{jarak:<9.0f}|")
        i+=1
        print('-------'*12)
print_data(data)
print("PROGRAM SELESAI!")
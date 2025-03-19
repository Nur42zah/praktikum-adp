#PROGRAM MENGHITUNG PERKEMBANGAN MODAL SETIAP TAHUN HINGGA MENCAPAI TARGET INVESTASI

M = float(input("Masukkan modal awal investasi   =    "))
r = float(input("Masukkan suku bunga tahunan (%) =    "))
T = float(input("Masukkan target investasi       =    "))
print ()
i = 0
M = M
while M < T :
      i+=1
      M += M*(r/100)
      print(f"Tahun ke-{i} = Rp {M}")
      
      
print()   
print(f"Target tercapai dalam {i} tahun!")
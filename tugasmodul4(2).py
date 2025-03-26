#PROGRAM VALIDASI PASSWORD
print('========================================')
print("PROGRAM VALIDASI PASSWORD")
print('========================================')
print()
PWD         = str(input("Masukkan password : "))
H_Kecil     = False
H_Kapital   = False
Angka       = False
Kar_Khusus  = False
C_Kh        = " :!@#$%^&*90-_=+[]{}|;:’\”,.<>?`~' "
print()

while True :
    PWD == PWD
   
    for karakter in PWD :
        if "a" <= karakter <= "z" :
            H_Kecil = True
        elif "A" <= karakter <= "Z" :
            H_Kapital = True
        elif "0" <= karakter <= "9" :
            Angka = True
        elif karakter in C_Kh :
            Kar_Khusus = True
        

    if len(PWD) < 8 : 
        print("(Panjang password minimal 8 karakter)")
        print("Silahkan coba lagi!")
        break

    elif H_Kecil == False:
        print("(Password harus memiliki setidaknya 1 huruf kecil)")
        print("Silahkan coba lagi!")
        break
        
    elif H_Kapital == False :
        print("(Password harus memiliki setidaknya 1 huruf kapital)")
        print("Silahkan coba lagi!")
        break
            
    elif Angka == False:
        print("(Password harus memiliki setidaknya 1 angka)")
        print("Silahkan coba lagi!")
        break
                 
    elif Kar_Khusus == False:
        print("(Password harus memiliki setidaknya 1 karakter khusus:!@#$%^&*90-_=+[]{}|;:’\”,.<>?`~))")
        print("Silahkan coba lagi!")
        break
                    
    else :
        print("Password Valid!")
        break

  


   

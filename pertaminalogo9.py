import os
import time
from termcolor import colored,cprint

os.system('cls')
print(colored("3...","yellow"))
time.sleep(3)
os.system('cls')
print(colored("2...","yellow"))
time.sleep(2)
os.system('cls')
print(colored("1...","yellow"))
time.sleep(2)
os.system('cls')
cprint("\t\t\t\t\t\t\t  =======SELAMAT DATANG DI PROGRAM PEMBUATAN LOGO PERTAMINA=======  ","blue","on_white")
time.sleep(2)
print()

def logo_pertamina():
    

    print(colored("                           ██████████████████", "red"))
    print(colored("                             ██████████████████", "red"))
    print(colored("                               ██████████████████", "red"))
    print(colored("                                 ██████████████████", "red"))
    print(colored("                                   ██████████████████", "red"))
    print()

    print(colored("              ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "   " + colored("  ███████  ██████  ██████   ██████   █████   ███     ███  ██  ███   ██   █████   ", "black","on_white"))
    print(colored("            ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "     " + colored("  ██   ██  ██      ██   ██    ██    ██   ██  ████   ████  ██  ████  ██  ██   ██  ", "black","on_white"))
    print(colored("          ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "       " + colored("  ███████  █████   ██████     ██    ███████  ██ ██ ██ ██  ██  ██ ██ ██  ███████  ", "black","on_white"))
    print(colored("        ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "         " + colored("  ██       ██      ██ ██      ██    ██   ██  ██  ███  ██  ██  ██  ████  ██   ██  ", "black","on_white"))
    print(colored("      ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "           " + colored("  ██       ██████  ██  ███    ██    ██   ██  ██       ██  ██  ██   ███  ██   ██  ", "black","on_white"))
    print(colored("    ██████████████████", "blue"))
    print(colored("  ██████████████████", "blue"))
    print(colored("██████████████████", "blue"))
    
logo_pertamina()

print()
time.sleep(2)
cprint("\t\t\t\t\t\t\t\t\t =======PROGRAM TELAH SELESAI=======","green","on_white")
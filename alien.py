import random
import time
import os
from colorama import Fore, Style, init
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def illuminati_utama():
    clear_screen()
    print(Fore.CYAN + Style.BRIGHT + "========================")
    print(Fore.CYAN + Style.BRIGHT + "Selamat Datang di Aplikasi Pendeteksi Alien")
    print(Fore.CYAN + "Pilih Detektor yang akan digunakan:")
    print(Fore.CYAN + Style.BRIGHT + "========================")

    print(Fore.YELLOW + "1. Detektor Alien")
    print(Fore.MAGENTA + "2. Detektor Setan")

    pilihan_alat = input(Fore.CYAN + Style.BRIGHT + "\nMasukkan Pilihan (1 atau 2): ")

    if pilihan_alat == "1":
        area_51()
    elif pilihan_alat == "2":
        illuminati_kegelapan()
    else:
        print("Tidak ada pilihan yang valid. Coba lagi")
        illuminati_utama()

def area_51():
    print(Fore.GREEN + "Detektor Alien diaktifkan!")

def illuminati_kegelapan():
    print(Fore.RED + "Detektor Setan diaktifkan!")

# Start the application
illuminati_utama()
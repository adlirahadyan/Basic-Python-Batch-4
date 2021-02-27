#Aplikasi Kontak
import function

#List Of Dictionary
daftar_kontak = []
daftar_kontak.append({
    "nama" : "Mbappe",
    "email" : "kylian.mbappe@gmail.com",
    "telepon" : "0852453674580"
})

#Menu Program
while True :
    print("# Menu")
    print("1. Daftar Kontak")
    print("0. Keluar")

    menu = input("Pilih menu : ")

    if menu == "0" :
        break
    elif menu == "1" :
        function.display_kontak(daftar_kontak)
 
print("Program selesai")

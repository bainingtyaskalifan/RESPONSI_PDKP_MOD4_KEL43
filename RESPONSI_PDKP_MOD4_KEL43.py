print("Program Modul 4")

abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

kunci = 17
kunci = int(kunci)
def enskripsi(abjad):
    str = input("Kalimat yang akan dienkripsikan: ")
    str = str.lower()
    hasil = ''

    for i in str:
        if i in abjad:
            n = abjad.index(i)
            enkrip = (n + kunci) % 26 
            ubah = abjad[enkrip]
            hasil = hasil + ubah
        else:
            hasil = hasil + ''

    print(f"hasil : {hasil}")

def deskripsi(abjad):
    str = input("Kalimat yang akan dideskripsikan : ")
    str = str.lower()
    hasil = ''

    for i in str:
        if i in abjad:
            n = abjad.index(i)
            Deskripsi = (n - kunci) % 26
            ubah = abjad[Deskripsi]
            hasil = hasil + ubah
        else:
            hasil = hasil + ''

    print(f"hasil : {hasil}")

pilihan = 'y'

while (pilihan == 'y'):
    print("Pilihan Menu : ")
    print("1. Data Enkripsi")
    print("2. Data Deskripsi")
    print("3. Keluar")

    menu = input("Pilih menu : ")
    print("------------------------------------")

    if menu == '1':
        print("Data Enkripsi")
        fungsiEnkripsi = enskripsi(abjad)
        fungsiEnkripsi
    elif menu == '2':
        print("Data Deskripsi")
        deskripsi(abjad)
    elif menu == '3':
        print("Anda Keluar.")
        break
    else:
        print("Tidak ditemukan!!")

    print("------------------------------------")

class ucapan:
    def terimaKasih():
        print("Terima kasih")
p1 = ucapan
p1.terimaKasih()

from Segitiga import Segitiga
from PersegiPanjang import PersegiPanjang
from Persegi import Persegi
from Lingkaran import Lingkaran

class MainProject :

 def __init__(self):
    print("Rumus Bangun Datar")
    print("1. Segitiga")
    print("2. Persegi Panjang")
    print("3. Persegi")
    print("4. Persegi Panjang")
    pil = int(input("Masukkan Pilihan : "))
    print()

    if (pil == 1) :
        alas = int(input("Input Alas : "))
        tinggi = int(input("Input Tinggi : "))
        sisi = int(input("Input Sisi :"))
        segitiga = Segitiga()
        segitiga.isiField(alas , tinggi , sisi)
        print()
        print("Alas : " , segitiga.tampilAlas() , " cm")
        print("Tinggi : " , segitiga.tampilTinggi() , " cm")
        print("Sisi : " , segitiga.tampilSisi() , " cm")
        print()
        print("Luas : " , segitiga.luasSegitiga() , " cm")
        print("Keliling : " , segitiga.kelilingSegitiga() , " cm")
    elif (pil == 2) :
        panjang = int(input("Input Panjang : "))
        lebar = int(input("Input Lebar : "))
        print()
        persegiPanjang = PersegiPanjang()
        persegiPanjang.isiField(panjang , lebar)
        print("Panjang : " , persegiPanjang.tampilPanjang() , " cm")
        print("Lebar : " , persegiPanjang.tampilLebar() , " cm")
        print()
        print("Luas : " , persegiPanjang.luasPersegi() , " cm")
        print("Keliling : " , persegiPanjang.kelilingPersegi() , " cm")
    elif (pil == 3) :
        sisi = int(input("Input Sisi : "))
        print()
        persegi = Persegi()
        persegi.isiField(sisi)
        print("Sisi : " , persegi.tampilSisi() , " cm")
        print()
        print("Luas : " , persegi.luasPersegi() , " cm")
        print("Keliling : " , persegi.kelilingPersegi() , " cm")
    elif (pil == 4) :
        jari2 = int(input("Input Jari - Jari : "))
        print()
        lingkaran = Lingkaran()
        lingkaran.isiField(jari2)
        print("Jari - Jari : " , lingkaran.tampilJari2() , " cm")
        print()
        print("Luas : " , lingkaran.luasLingkaran() , " cm")
        print("Keliling : " , lingkaran.kelilingLingkaran() , " cm")

while (True) :
    main = MainProject()
    print()
    ulang = input("Mengulang Lagi(y/t) : ")
    print()
    if (ulang == 't') :
        print("Terima Kasih")
        break






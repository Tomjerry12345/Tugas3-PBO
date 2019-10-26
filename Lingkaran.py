class Lingkaran :
    def isiField(self , jari2):
        self.__jari2 = jari2
    def tampilJari2(self):
        return self.__jari2
    def luasLingkaran(self):
        luas = 3.14 * (self.__jari2 * self.__jari2)
        return luas
    def kelilingLingkaran(self):
        keliling = 2 * 3.14 * self.__jari2
        return keliling
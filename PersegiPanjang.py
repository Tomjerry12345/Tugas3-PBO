class PersegiPanjang :

    def isiField(self , panjang , lebar):
        self.__panjang = panjang
        self.__lebar = lebar
    def tampilPanjang(self):
        return self.__panjang
    def tampilLebar(self):
        return self.__lebar
    def luasPersegi(self):
        luas = self.__panjang * self.__lebar
        return luas
    def kelilingPersegi(self):
        keliling = 2 * (self.__panjang + self.__lebar)
        return keliling

class Persegi :
    def isiField(self , sisi):
        self.__sisi = sisi
    def tampilSisi(self):
        return self.__sisi
    def luasPersegi(self):
        luas = self.__sisi * self.__sisi
        return luas
    def kelilingPersegi(self):
        keliling = 4 * self.__sisi
        return keliling
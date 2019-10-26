class Segitiga :

    def isiField(self , alas , tinggi , sisi) :
        self.__alas = alas;
        self.__tinggi = tinggi;
        self.__sisi = sisi


    def tampilAlas(self):
        return self.__alas

    def tampilTinggi(self):
        return self.__tinggi

    def tampilSisi(self):
        return self.__sisi

    def luasSegitiga(self):
        luas = 0.5 * self.__alas * self.__tinggi
        return luas

    def kelilingSegitiga(self):
        keliling = self.__sisi + self.__sisi + self.__sisi
        return keliling



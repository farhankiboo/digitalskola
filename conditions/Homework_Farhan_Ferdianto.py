from ast import If
from codecs import namereplace_errors
from os import uname_result


# 1. Buat class Hewan yang memiliki class attributes nama_latin dan instance attributes nama dan umur:   
# a. Di class Hewan, memiliki instance method bangun, & class method change_nama_latin

# b. Buat child class Kucing yang memiliki value class attributes yang berbeda dengan parent class, menggunakan class method change_nama_latin
# c. Di child class, override method bangun
# d. Di child class, buat method lari yang memiliki parameter kecepatan. Jika value dari parameter kecepatan lebih dari 10, maka print cepat sekali selain itu print lambat

# Parent class
class Hewan:

# class attribute
    nama_latin = str(input('Masukan nama latin hewan: '))

# Initializer / Instance attributes
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

# instance method
    def bangun(self):
        pass #return f"{self.nama} berumur {self.umur} tahun"

#class method
@classmethod
def change_nama_latin(self):
    self.nama_latin = self.nama
    return

# Child class (inherits from Hewan class)
class Kucing(Hewan):
    def lari(a):
        if (a > 10):
            return 'cepat sekali'
        else:
            return 'lambat'

kucing = Kucing("kucing", 10)
# print("Nama Hewan ini: "+kucing.nama_latin)
b = int(input("Masukan Kecepatan: "))
print("Kecepatan Hewan ini, " + Kucing.lari(a = b))
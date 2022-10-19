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
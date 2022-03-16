print ('Rizki Januar I. / 20051397046')
print ('-----------------------')
class hasil :
    def hitung (angka):
        print (' ')
        print ('Panjang Bangun : ', angka.bil1)
        print ('Lebar Bangun : ', angka.bil2)
        print (' ')
        print ('Luas Bangun Persegi Adalah :', angka.bil1*angka.bil2)
class nilai(hasil) :
    def __init__(self):
        self.bil1 = int(input('Masukan Panjang : '))
        self.bil2 = int(input('Masukan Lebar : '))

coba = ('y')
while coba == ('y') or coba == ('Y') :
    print ('|===========================|')
    print ('|Mencari Luas Pesegi|')
    print ('|===========================|')
    objek = nilai()
    objek.hitung()

    print(' ')
    coba = input('Mau Menghitung Lagi : ')
    if coba == ('y') or coba == ('Y') :
        print (' ')
        continue
    elif coba == ('n') or coba == ('N') :
        print ('Terima Kasih')
        break
    else :
        print ('Pilihan yang Anda Masukan Salah')
        break

usia = int(input('Masukkan Usia Anda : '))
if usia > 0 and usia <= 12 :
    print('Kategori Usia : Anak-anak')
elif usia >= 13 and usia <= 17 :
    print('Kategori Usia : Remaja')
elif usia >= 18 and usia <= 59 :
    print('Kategori Usia : Dewasa')
elif usia >= 60 :
    print('Kategori Usia : Lansia')
else :
    print('usia tidak valid')


# a. Luas persegi panjang
def luas_persegi_panjang(panjang,lebar) :
    hasil = panjang * lebar
    return hasil

print('==========MENGHITUNG LUAS PERSEGI PANJANG============')
panjang = float(input('masukkan panjang persegi panjang : '))
lebar = float(input('masukkan lebar persegi panjang : '))
print(f'luas persegi panjang : {luas_persegi_panjang(panjang,lebar)}')

# b. Volume persegi panjang
def vol_pp(luas,tinggi) :
    hasil = luas * tinggi
    return hasil

print('==========MENGHITUNG VOLUME PERSEGI PANJANG==========')
luas = float(input('masukkan luas persegi panjang : '))
tinggi = float(input('masukkan tinggi persegi panjang : '))
print(f'volume persegi panjang : {vol_pp(luas,tinggi)}')

# c. Luas lingkaran
def luas_lingk(jari_jari) :
    pi = 3.14
    hasil = pi * (jari_jari ** 2)
    return hasil

print('==========MENGHITUNG LUAS LINGKARAN==================')
jari_jari = float(input('masukkan jari-jari lingkaran : '))
print(f'luas lingkaran : {luas_lingk(jari_jari)}')

# d. Volume bola
def vol_bola(jari_jari) :
    pi = 3.14
    hasil = (4/3) * pi * (jari_jari ** 3)
    return hasil

print('=========MENGHITUNG VOLUME BOLA======================')
jari_jari = float(input('masukkan jari-jari bola : '))
print(f'volume bola : {vol_bola(jari_jari)}')






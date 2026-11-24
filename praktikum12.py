# program 12.1
def hello_world() :
    print('hello world')
    print('kepada fauzan zein')
    print('dan juga kpd faza biri biri')
hello_world()


# program 12.2
def hello_world(nama) :
    print(f'selamat datang di dunia , {nama}')
hello_world('ucup')

def tambah(angka_1,angka_2) :
    hasil = angka_1 + angka_2
    print(f'{angka_1} + {angka_2} = {hasil}')
tambah(1,8)

def say_hi(list_peserta) :
    data_peserta = list_peserta.copy()
    for peserta in data_peserta :
        print(f'selamat datang {peserta}')

kumpulan_mahasiswa = ['budi','tono','joko']
say_hi(kumpulan_mahasiswa)

# program 12.3
def kuadrat(input_angka) :
    output_kuadrat = input_angka ** 2
    return output_kuadrat

y = kuadrat(5)
print(y)
print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

def fungsi_tambah(angka_1,angka_2) :
    return angka_1 + angka_2
a = fungsi_tambah(10,8)
print(a)

def operasi_matematika(angka_1,angka_2) :
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    return tambah,kurang,kali,bagi
k,l,m,n = operasi_matematika(9,5)
print(f'hasil tambah = {k}')
print(f'hasil kurang = {l}')
print(f'hasil kali = {m}')
print(f'hasil bagi = {n}')

# program 12.4 default argumen fungsi

# contoh 1
def say_hello(nama = 'ojul') :
    print(f'hello {nama}')

say_hello('ucup')
say_hello()

# contoh 2
def sapa_dia(nama, pesan = 'apa kabar ?') :
    print(f'hai {nama} ,{pesan}')

sapa_dia('nanda','selamat pagi')
sapa_dia('budi')

# contoh 3
def hitung_pangkat(angka,pangkat) :
    hasil = angka**pangkat
    return hasil
print(hitung_pangkat(2,4))
hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

# contoh 4
def faktorial(input_1 = 1,input_2 = 2,input_3 = 3,input_4 = 4) :
    hasil = input_1 * input_2 * input_3 * input_4
    return hasil

print(faktorial())
print(faktorial(input_3 = 10))











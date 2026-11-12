# No. 1
# a. Buatlah sebuah Tuple bernama mahasiswa yang berisi 3 data diri Anda: ("Nama", "NIM", "Prodi"). 
mahasiswa = ('Nugroho Prasetyo Widodo','2605060036','Teknologi Informasi')

# b. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya. 
print('NIM : ', mahasiswa[1])
print('PRODI : ', mahasiswa[2])

# c. Coba jalankan kode mahasiswa[2] = "Teknologi Informasi". Amati pesan error yang muncul, lalu jelaskan mengapa hal tersebut terjadi
# print(mahasiswa[2] = 'Teknologi Informasi'
# kode tersebut error karena tuple bersifat immutable, yaitu setelah tuple dibuat kita tidak dapat mengubah,menambah,atau menghapus elemen di dalamnya

# d. Buatlah sebuah Set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5. Cetak nilai_angka ke layar dan jelaskan apa yang terjadi pada angka 10 dan 4 yang ditulis dua kali! 
nilai_angka = {10,4,3,2,4,10,7,5}
print(nilai_angka)
# ketika dicetak, nilai 4 dan 10 hanya akan muncul 1 kali karena karateristik dari sets adalah menyimpan elemen unik(tidak ada duplikasi),dan otomatis mengapus nilai yang kembar


# No.2
# a. membuat dictionary data mahasiswa
data_mahaiswa = {
    'nim' : '240101',
    'nama' : 'Budi Santoso',
    'prodi' : 'Teknologi Informasi'
}
# b. mengubah prodi dan menambahkan key baru
data_mahaiswa['prodi'] = 'Sastra Mesin'
data_mahaiswa['angkatan'] = 2026
 # c. menghapus nim dan menampilkan ke layar
del data_mahaiswa['nim']
print(f'Data Mahasiswa : ', data_mahaiswa)                                                       

# No.3 
# a.membuat dictionary keranjang
keranjang = {
    'apel' : 5000,
    'pisang' : 3000,
    'jeruk' : 7000,
    'anggur' : 15000
}

# b. menampilkan dengan perulangan
for barang, harga in keranjang.items() :
    print(f'Harga {barang} : Rp {harga}')

# c. menampilkan total belanja 
total_belanja = 0
for harga in keranjang.values(): 
    total_belanja = total_belanja + harga
print(f'total belanja = Rp {total_belanja}')








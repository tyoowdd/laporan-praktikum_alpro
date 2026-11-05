# latihan tugas

kendaraan = ['motor','mobil','sepeda','bus']
print(f'data kendaraan awal = {kendaraan}')

# No.1
# a. menambah truk pada akhir list
kendaraan.append('truk')
print(f'data kendaraan setelah ditambah = {kendaraan}')
# b. menyisipkan becak pada index-1
kendaraan.insert(1,'becak')
print(f'data kendaraan setelah di sisipkan = {kendaraan}')
# c. Hapus data yang berada paling belakang dari list tersebut
kendaraan.pop()
print(f'data kendaraan setelah dihapus = {kendaraan}')
# d. Ubah elemen 'sepeda' menjadi 'skuter'
kendaraan[kendaraan.index('sepeda')] = 'skuter'
print(f'data kendaraan setelah di ubah = {kendaraan}')
# e. Tampilkan informasi jumlah total data di dalam list tersebut
panjang_data = len(kendaraan)
print(f'list data kendaraan akhir = {kendaraan}')
print(f'jumlah total data kendaraan = {panjang_data}')

# No.2
angka = [75, 80, 90, 75, 85, 100, 65]
print(f'data angka = {angka}')

# a. Cari tahu di indeks ke berapa skor 100 berada
index_100 = angka.index(100)
print(f'index skor 100 berada pada index ke-{index_100}')
# b. Hitung ada berapa banyak siswa yang mendapatkan skor 75
jumlah_75 = angka.count(75) 
print(f'jumlah siswa yang mendapatlan skor 75 = {jumlah_75}')
# c. mengurutkan list angka dari terkecil ke terbesar
angka.sort()
print(f'list angka dari yang terkecil ke yang terbesar = {angka}')
# d. mengurutkan list angka dari terbesar ke terkecil
angka.reverse()
print(f'list angka dari yang terbesar ke terkecil = {angka}')

# No.3
menu_utama = ["Nasi Goreng", "Mie Ayam"]
print(f'menu utama = {menu_utama}')
menu_tambahan = ["Kerupuk", "Es Teh"]
print(f'menu tambahan = {menu_tambahan}')
# menggabungkan menu_tambahan ke menu_utama menggunakan fungsi extend 
menu_utama.extend(menu_tambahan)
# menampiilkan hasil gabungan
print(f'menu gabungan = {menu_utama}')

# No.4
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]] 
print
# a. menampilkan harga pensil dengan memanggil indeks dan kolom
harga_pensil = data_barang[1][1]
print(f'harga pensil = {harga_pensil}')

# b. perulangan nama & harga barang 
for barang in data_barang :
    print(f'nama barang : {barang[0]}')
    print(f'harga : {barang[1]}')
 


# Latihan Praktikum
# operasi aritmatika
a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi kurang -
hasil = a-b
print(a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a*b
print(a,'*',b,'=',hasil)

# operasi pembagian /
hasil = a/b
print(a,'/',b,'=',hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi modulus %
hasil = a % b
print (a,'%',b,'=',hasil)

# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

# 3.2

print('\nPROGRAM KONVERSI TEMPERATURE\n')
celcius = float(input('masukkan suhu dalam celcius : '))
print("suhu adalah",celcius, "Celcius")

# reamur

reamur = (4/5) * celcius
print("suhu dalam reamur adalah", reamur , "Reamur")

# fahrenheit

farenheit = ( (9/5) * celcius ) + 32
print("suhu dalam farenheit adalah", farenheit , "Farenheit")

# kelvin

kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin , "Kelvin")

# 3.3 komparasi

a = 4
b = 2
# lebih besar dari >
print("=============== lebih besar dari (>)")
hasil = a > 3
print(a,'>',b,'=',hasil)
hasil = b > 3
print(b,'>',a,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# kurang dari <
print("=============== kurang dari (<)")
hasil = a < 3
print(a,'<',b,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan >=
print("=============== lebih dari sama dengan (>=)")
hasil = a >= 3
print(a,'>=',b,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan <=
print("=============== kurang dari sama dengan (<=)")
hasil = a <= 3
print(a,'<=',b,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil =  b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan (==)
print("=============== sama dengan(==)")
hasil = a==4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)


# tidak sama dengan (!=)
print("=============== tidak sama dengan(!=)")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# ‘is’ sebagai komparasi obj identity (bukan literal) 

x = 5
y = 5

hasil = x is y
print('x is y =',hasil)

# is not
x = 5
y = 6
hasil = x is not y
print('x is not y =',hasil)
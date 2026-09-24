# soal no. 1
ganjil = ""
genap = ""

for i in range(1, 51):
    if i % 2 == 0:
        genap += str(i) + " "
    else:
        ganjil += str(i) + " "

print(" Bilangan Ganjil (1 - 50) ")
print(ganjil)

print(" Bilangan Genap (1 - 50) ")
print(genap)

# soal no. 2
prima = ""

for angka in range(2, 101):
    is_prima = True
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            is_prima = False
            break
    if is_prima:
        prima += str(angka) + " "

print(" Bilangan Prima (1 - 100) ")
print(prima)
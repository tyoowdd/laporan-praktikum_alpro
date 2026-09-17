# operasi logika atau bolean
# not, or, and, xor

print('===NOT===')
a = True
b = not a
print('data a =',a)
print('------------ NOT')
print('data b =',b)

# or,jika salah satu true,maka hasilnya akan true
print('===OR===')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

# AND (harus benar semuanya)
print('===AND===')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

# XOR (akan true jika salah satu true,sisanya false)
print('===XOR===')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False 
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
                                                                    # program 4.2                                                                   
# logika dan komparasi
# membuat gabungan area rentang dari angka
# ++++++3------10++++++
inputUser = float(input('masukkan angka yang bernilai\n kurang dari 3  \n atau \n lebih besar dari 10\n : '))
#+++++3-----
isKurangDari = (inputUser < 3)
print('kurang dari 3 =', isKurangDari)
#------10++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print('lebih dari 10 =',isLebihDari)
isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukkan : ', isCorrect)
print('========================================')
#-------3+++++++10-------
# kasus irisan
inputUser = float(input('masukkan angka yang bernilai\n Lebih dari 3 \n dan \n kurang dari 10\n: ' ))
# ----3++++
# lebih dari 3
isLebihDari = inputUser > 3
print('Lebih dari 3 = ', isLebihDari)
# +++++10-----
# kurang dari 10
isKurangDari = inputUser < 10
print ('Kurang dari 10 = ', isKurangDari)
isCorrect = isKurangDari and isLebihDari
print('angka yang anda masukkan : ', isCorrect)


                                                                # program 4.3

# if dan else statement
# 1. if nya 
# # 2. kondisinya 
# # 3. aksinya 
nama = input('Siapa nama anda? ') 
# 1. program if inline 
if nama == 'tio' : print('Kamu Ganteng abieeezz!!!!')
print('akhir dari program')

# 2. Program if indentation 
if nama == 'tio' : 
     print('kamu ganteng abiiez!')    
     print('kamu juga keren banget') 
print('akhir dari program')
# 3. Else statement
if nama == 'tio' :
    print('hai tio, si keren!')
else:   
     print('ah kamu bukan tio, kamu gak keren')
print('akhir dari program') 

                                                            # program 4.4
# ELIF = else if statement 
nama = input('siapa nama anda? ') 

# if kondisi: 
#   aksi true 
# elif kondisi: 
#   aksi true 
# elif kondisi: 
#   aksi true 
# else: 
#   aksi 
if nama == 'tio' :  #kondisi 1 
    print('hai ganteng abiiz!!!') #aksi true 1
elif nama == 'nugroho': #kondisi 2 
     print('hai si kece bangeets!!!') #aksi true 2 
elif nama == 'widodo': #kondisi 3 
    print('hai humoris!!!') #aksi true 3
else: 
    print('au ah gak kenal!!!') #aksi false
print('akhir dari program') 
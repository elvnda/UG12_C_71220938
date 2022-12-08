x = input("Masukan angka :")
y = input("Masukan angka yang hilang :")
hitung = 0
for i in x:
    if i == y:
        hitung += 1
print("angka",y,"muncul sebanyak",hitung,"kali")
Klub_A = input("Masukkan Nama Klub 1 :")
Klub_B = input("Masukkan Nama Klub 2 :")
print(f"Klub A : {Klub_A}")
print(f"Klub B : {Klub_B}")
hasil = {}
i=0
while i>=0:
    match = input(f"Pertandingan {i+1} : ").split()
    if int(match[0]) >= 0 and int(match[1]) >= 0:
        if match[0] > match[1]:
            hasil.update({f"Hasil {i+1}" : f"{Klub_A} Menang"})
        elif match[0] == match[1]:
            hasil.update({f"Hasil {i+1}" : "Seri"})
        elif match[0] < match[1]:
            hasil.update({f"Hasil {i+1}" : f"{Klub_B} Menang"}) 
    else:
        break
    i += 1

for key, val in hasil.items():
    print(key,":", val)

print("Pertandingan selesai")

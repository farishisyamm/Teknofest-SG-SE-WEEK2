arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum   
    bMin = round(min(arrBerat),2)
    bMax = round(max(arrBerat),2)

def rerata(arrBerat):
    total = sum(arrBerat)
    # Definisikan Proses Mencari Rerata Dari Total Berat
    berat_rerata= total / n
    # Return Hasil Rerata
    return round(berat_rerata,2)
    
print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    dataBerat = float(input())
    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(dataBerat)

# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)
# Print Data Minimum, Maximum, dan Rerata Berat
print(f"Berat Balita Minimum = {bMin}kg,\nBerat Balita Maksimum = {bMax}kg,\nRerata Berat Balita = {rerata(arrBerat)}kg")

 
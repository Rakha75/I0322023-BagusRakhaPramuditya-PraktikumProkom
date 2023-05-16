import json
from tabulate import tabulate

# Load Data
with open('history.city.list.json', encoding='utf-8') as f:
    data = json.load(f)

# List kota Prancis
kota_kota = []
for kota in data:
    if kota['city']['country'] == 'FR':
        kota_kota.append([kota['city']['name'], kota['city']['coord']
                          ['lon'], kota['city']['coord']['lat'], kota['city']['country']])

# Tabel nama kota Prancis beserta Longitude dan Latitude
print("Kota-kota Prancis yang ada dilist adalah sebagai berikut.")
print()
print(tabulate(kota_kota, headers=[
      'City', 'Longitude', 'Latitude', 'Country'], tablefmt='orgtbl'))

# Menghitung jumlah kota
totalkota = len(kota_kota)

# Print jumlah kota
print("Jumlah kota-kota di Prancis dalam file tersebut:", totalkota)

# Membuat dalam bentuk text file
with open('Bagus Rakha Pramuditya.txt', 'w') as f:
    f.write(tabulate(kota_kota, headers=[
            'City', 'Longitude', 'Latitude', 'Country'], tablefmt='orgtbl'))

kota_prancis = [element[0].lower() for element in kota_kota]

# Nomor 6
pencarian = input("Apakah anda ingin melakukan pencarian nama kota? (yes/no)")
if pencarian.lower() in ["yes"]:
    pencarian = True
else:
    pencarian = False

# Yes
while pencarian:
    find = input("Masukkan nama kota yang ada di Prancis")
    if find.lower() in kota_prancis:
        index = kota_prancis.index(find.lower())
        print(tabulate([kota_kota[index]], headers=[
              'City', 'Longitude', 'Latitude', 'Country'], tablefmt='orgtbl'))
    else:
        print("Kota yang anda masukkan tidak ditemukan")
    print("="*50)
    # Mencari nama kota lagi
    pencarian = input("Cari nama kota lagi? (yes/no)")
    if pencarian.lower() in ["yes"]:
        pencarian = True
    else:
        pencarian = False
print("="*50)

# Nomor 7
huruf_depan = [element[0][0] for element in kota_kota]
set = sorted(list(set(huruf_depan)))

for letter in set:
    hitung = huruf_depan.count(letter)
    print("Ada", hitung, "kota yang berawalan huruf", letter)

nama = input("masukkan nama: ")
nim =input("masukkan nim:")

fisika= int(input("masukkan nilai fisika: "))
biologi = int(input("masukkan nilai biologi: "))
matematika = int(input("masukkan nilai matematika: "))

ip = (fisika + biologi+ matematika)/ 3
if ip == 80 >=100:
    print("A")
elif ip == 70 >= 79.9:
    print("B")
elif ip == 60>=69.9:
    print("C")
elif ip == 50>=59.9:
    print("D")
elif ip == 0>=49.9:
    print("E")
else:
    print("tidak")

print ("mahasiswa dengan nama",nama,"dan nim",nim,"mendapatkan IP", ip)


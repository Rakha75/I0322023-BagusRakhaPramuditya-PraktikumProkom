nama = input("masukkan nama: ")
nim =input("masukkan nim:")

fisika= int(input("masukkan nilai fisika: "))
biologi = int(input("masukkan nilai biologi: "))
matematika = int(input("masukkan nilai matematika: "))

ip = (fisika + biologi+ matematika)/ 3

dict = {'A':{80>=100}, 
                     'B':{70>=79.9},
                     'C':{60>=69.9},
                     'D':{50>=59.9},
                     'E':{0>=49.9}}

print ("mahasiswa dengan nama",nama,"dan nim",nim,"mendapatkan IP", ip,dict)


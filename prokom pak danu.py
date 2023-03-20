def luas_segitiga(alas,tinggi):
    luas = (alas* tinggi)/2
    print('')
    print("Luas segitiga adalah = %f" %luas)

def Luas_persegi(alas,tinggi):
    LuasPersegi = alas* tinggi
    print("Luas Persegi adalah = %f" %LuasPersegi)

def Keliling_persegi(alas,tinggi):
    Kelilingpersegi = (alas*2)+(tinggi*2)
    print("Keliling Persegi adalah = %f" %Kelilingpersegi)
    
def luas_kubus(sisi):
    luaskubus = sisi*sisi
    return luaskubus

def volume_kubus (sisi):
    volume = luas_kubus(sisi)* sisi
    return volume
print("volume Kubus = %f" %volume_kubus(sisi= 4))

alas = int(input("inputkan nilai alas: "))
tinggi = int(input("inputkan nilai tiggi: "))
sisi = int(input("inputkan nilai sisi: "))
luas_segitiga(alas, tinggi)
Luas_persegi(alas,tinggi)
Keliling_persegi(alas,tinggi)
volume_kubus(sisi)
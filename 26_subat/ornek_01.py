sinav1 = int(input("1. Sınav notunu gir"))
sinav2 = int(input("2. Sınav notunu gir"))
performans = int(input("Performans notunu gir"))
ortalama = (sinav1 + sinav2 + performans) / 3
print(ortalama)
if ortalama >= 50 :
    print("Başarılı")
else:
    print("Başarısız")
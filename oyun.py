from random import random
sans = int(input("Kaç kere denemek istersiniz ? "))
ilk_sans = sans
oyun_sayisi = 0
ikili = 0
while 0 < sans:
    for k in range(sans):
        a = int(random()*10)
        b = int(random()*10)
        c = int(random()*10)
        oyun_sayisi += 1
        print(k+1,". denemede gelen sayılar :",a,b,c)
        if a == b == c:
            print("Tebrikler Kazandınız", ilk_sans*100)
            sans = 0
            break
        else:
            if a == b or a == c or b == c:
                ikili += 1
    if sans != 0:
        print("Bu turdaki tutturulan ikili sayısı : ", ikili)
        sans = ikili
        ikili = 0
if ikili == 0:
    print("Kaybettiniz :(")
print("Toplam Oyun Sayısı", oyun_sayisi)

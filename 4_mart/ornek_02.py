# saat girişi yap
# eğer saat <=1 ise
#    5 tl ödeme
# değilde eğer saat >1 ve saat <=5 ise
#    saat * 4 tl ödeme
# değilse
#    saat * 3 tl ödeme

saat = int(input("Kaç saat"))
if saat <= 1 :
    print("5 tl ödeme")
elif saat >1 and saat <=5 :
    print(saat * 4 ,"tl ödeme")
else:
    print(saat * 3 ,"tl ödeme")
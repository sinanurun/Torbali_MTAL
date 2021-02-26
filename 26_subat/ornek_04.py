ilk_urun = float(input("ilk ürün fiyatı"))
ikinci_urun = float(input("ikinci ürün fiyatı"))

toplam = ilk_urun + ikinci_urun

if toplam <= 200:
    print("ödemeniz gereken tutar",toplam)
else:
    tutar = toplam * 0,75
    print("indirilimli hali",tutar)
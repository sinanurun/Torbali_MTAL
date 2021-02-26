bagaj = int(input("Bagaj ağırlığını giriniz"))
if bagaj <= 20 :
    print (" Bagaj ücreti ödemenize gerek yok")
else:
    fazla = bagaj - 20
    tutar = fazla * 10
    print("ödemeniz gerken tutar",tutar)
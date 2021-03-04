# kenar uzunluklarını al k1, k2, k3
# eğer k1 eşit k2 ve k2 eşit k3 ise
#    eş kenar
# eğer k1 eşit k2 or k2 eşit k3 or k1 eşit k3 ise
#    ikiz kenar
# değilse
#    çeşitkenar

kenar1 = int(input("Kenar 1 giriniz : "))
kenar2 = int(input("Kenar 2 giriniz : "))
kenar3 = int(input("Kenar 3 giriniz : "))
if kenar1 == kenar2 and kenar3 == kenar2 :
    print("eşit kenar üçgen")
elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
    print("ikiz kenar üçgen")
else:
    print("çeşit kenar üçgen")


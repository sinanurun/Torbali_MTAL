# hava girişi yap
# eğer hava <5 ise:
#  soğuk de
# değilde eğer hava >6 ve hava <15 ise:
#   ılık de
# değilde eğer hava<15 ise
#   sıcak
#

hava = int(input("Hava kaç derece"))
if hava <= 5 :
    print("Soğuk")
elif hava >= 6 and hava <=14 :
    print("ılık")
elif hava >= 15 :
    print("sıcak")
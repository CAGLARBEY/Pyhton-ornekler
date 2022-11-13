import time

from parca import *
print("İlk modül denememize hoşgeldiniz... ")
print("""-----------------------------------
        Kare ile ilgili hesaplamaları yapmak için 1 tuşuna 
        Dikdörtgen ile ilgili hesapları yapmak için 2 tuşuna 
        üçgen ile hesapları yapmak için 3 tuşuna 
        Çıkmak için 4 tuşuna basınız...
        ------------------------------------
""")
tercih=int(input("Bir seçim yapınız ? "))


if tercih==1:
    kare()
    print("------------------------------")

elif tercih==2:
    dikdörtgen()
    print("--------------------------------")

elif tercih==3:
    ikizkenar()
    print("---------------------------------")

elif tercih==4:
    print("Çıkış yapılıyor")
    time.sleep(1)
    print("Çıkış yapıldı.")

else:
    print("Hatalı bir seçim yaptınız...")

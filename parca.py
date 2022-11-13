def kare():
    kenar = int(input("Bir kenar uzunluğunu giriniz : "))
    print(f"""Karenin kenarının uzunluğu : {kenar}
               Karenin çevresi:{kenar * 4}
               Karenin alanı: {kenar * kenar}
               Karenin hacmi: {kenar * kenar * kenar}

""")


def dikdörtgen():
    kenar, kenar1 = int(input("Kısa olan kenarı  giriniz : ")), int(input("Uzun olan kenarı giriniz: "))
    yükseklik = int(input("Yükseklik giriniz :"))
    print(f"""Dikdörtgenin kenar uzunlukları : {kenar, kenar1}
                   Dikdörtgenin çevresi:{(kenar + kenar1) * 2}
                   Dikdörtgenin alanı: {kenar * kenar1}
                   Dikdörtgenin hacmi: {kenar * kenar1 * yükseklik} """)


def ikizkenar():
    ikizkenar = int(input("İkiz olan kenarın değerini giriniz : "))
    farklıkenar = int(input("Taba olan kenarı giriniz : "))

    print(f"""Üçgenin  kenar uzunlukları : {ikizkenar, farklıkenar}
                      Üçgenin çevresi:{(ikizkenar * 2) + farklıkenar}
                     """)

print("deneme")
def belirli_kosul_sayilari(baslangic,bitis,kosul):
    for sayi in range(baslangic,bitis):
        if kosul(sayi):
            print(sayi)
def cift_sayi(sayi):
    return sayi % 2 == 0
belirli_kosul_sayilari(1,10,cift_sayi)

print("deneme")
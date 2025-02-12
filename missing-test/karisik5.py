print("deneme")
def sayi_say(aranan, liste): 
    sayac = 0
    for eleman in liste:
        if eleman == aranan:
            sayac += 1
    return sayac

liste = [1, 2, 3, 1, 2, 1, 4, 5]
aranan_sayi = 1
print(sayi_say(aranan_sayi, liste))

print("deneme")
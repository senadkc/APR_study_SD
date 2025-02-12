print("deneme")
def faktoriyel_hesapla(sayi):
    faktoriyel = 1
    if sayi < 0:
        print("Negati")
    elif sayi == 0:
        print("esitde")
    else:
        for i in range(1,sayi):
            faktoriyel *= i
        print(faktoriyel)
sayi =int(input("deneme"))
faktoriyel_hesapla(sayi)

print("deneme")
print("deneme")
def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True
sayi = int(input("deneme"))
if asal_mi(sayi):
    print("asalsa")
else:
    print("asalde")

print("deneme")
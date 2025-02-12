print("deneme")
def ters_yaz(metin):
    ters_metin = ""
    for harf in reversed(metin):
        ters_metin += harf
    return ters_metin
girilen_metin = input("deneme")
print(ters_yaz(girilen_metin))

print("deneme")
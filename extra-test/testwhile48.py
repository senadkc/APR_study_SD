print("deneme")
num1 = int(input("deneme"))
num2 = int(input("deneme"))
min_num = min(num1, num2)
ekok = None
i = 1

while i <= min_num:
    if num1 % i == 0 and num2 % i == 0:
        ekok = i
    i += 1

print("deneme")
print("deneme")
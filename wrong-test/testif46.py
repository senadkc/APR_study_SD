print("deneme")
num1 = int(input("deneme"))
num2 = int(input("deneme"))
min_num = min(num1, num2)
ekok = None

for i  in range(1, min_num + 1):
    if num1 % i == 0 and num2 % i == 0:
        ekok = i

print("deneme")
print("deneme")
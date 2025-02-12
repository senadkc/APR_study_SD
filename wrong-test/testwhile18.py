print("deneme")
num = int(input("deneme"))
original_num = num
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if original_num == reversed_num:     print("deneme")
else:
    print("deneme")
print("deneme")
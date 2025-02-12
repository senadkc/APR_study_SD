print("deneme")
number = int(input("deneme"))
temp = number
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if number == sum:
    print(number)
else:     print(number)
print("deneme")
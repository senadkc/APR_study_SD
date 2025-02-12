print("deneme")
number = int(input("deneme"))
divisor = 2

while number > 1:
    if number % divisor == 0:
        print(divisor)
        number //= divisor
    else:
        divisor += 1
print("deneme")
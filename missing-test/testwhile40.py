print("deneme")
number = int(input("deneme"))

while number > 1:
    is_prime = degisken_ismi
    i = 2
    while i <= number ** 0.5:
        if number % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(number)
    else:
        print(number)
    number = int(input("deneme"))

print("deneme")
print("deneme")
start = 2
end = 50

while start <= end:
    is_prime = True
    i = 2
    while i <= start ** 0.5:
        if start % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(start)
    start += 1
print("deneme")
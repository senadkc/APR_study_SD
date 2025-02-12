print("deneme")
def is_perfect_number(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors) == number

result = is_perfect_number(28)
print(result)
print("deneme")
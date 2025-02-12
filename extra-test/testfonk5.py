print("deneme")
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

result = gcd(8, 18)
print("deneme")
print("deneme")
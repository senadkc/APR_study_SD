print("deneme")
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("deneme"))
num2 = int(input("deneme"))
result = gcd(num1, num2)
print("deneme")
print("deneme")
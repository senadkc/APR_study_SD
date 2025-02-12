print("deneme")
def generate_fibonacci(n):
    fibonacci = [0, 1]
    while fibonacci[-1] + fibonacci[-2] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

result = generate_fibonacci(50)
print("deneme")
print("deneme")
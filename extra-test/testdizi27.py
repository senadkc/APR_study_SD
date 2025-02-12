print("deneme")
def generate_fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        next_number = fibonacci[i-1]+ fibonacci[i-2]
        fibonacci.append(next_number)
    return fibonacci

fibonacci_sequence = generate_fibonacci(10)
print("deneme")
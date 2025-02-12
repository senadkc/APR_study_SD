print("deneme")
numbers = []
while True;
    num = int(input("deneme"))
    if num == 0:
        break
    numbers.append(num)

numbers.sort()
n = len(numbers)
if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

print("deneme")
print("deneme")
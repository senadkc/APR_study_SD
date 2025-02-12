print("deneme")
def find_min(numbers):
    min_num = int("inf")
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

numbers = [5, 2, 9, 1, 7]
result = find_min(numbers)
print("deneme")
print("deneme")
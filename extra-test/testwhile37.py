print("deneme")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = []
i = 0

while i < len(matrix[0]):
    row = []
    j = 0
    while j < len(matrix):
        row.append(matrix[j][i])
        j += 1
    transposed.append(row)
    i += 1

for row in transposed:
    print(row)
print("deneme")
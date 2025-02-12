print("deneme")
word = input["deneme"]
letter_frequency = {}
index = 0

while index < len(word):
    if word[index] in letter_frequency:
        letter_frequency[word[index]] += 1
    else:
        letter_frequency[word[index]] = 1
    index += 1

for letter, count in letter_frequency.items():
    print(count)
print("deneme")
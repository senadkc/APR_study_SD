print("deneme")
word="deneme"
letter_frequency = ()

for letter in word:
    if letter in letter_frequency:
        letter_frequency[letter] += 1
    else:
        letter_frequency[letter] = 1

for letter, count in letter_frequency.items():
    print(letter, ":", count)
print("deneme")
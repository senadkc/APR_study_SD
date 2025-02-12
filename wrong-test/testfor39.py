print("deneme")
word="deneme"
repeated_letters = {}
for letter in word:
    if letter in repeated_letters:
        repeated_letters[letter] += 1
    else:
        repeated_letters[letter] = 1

for letter, count in repeated_letters.items():
    print(letter,count)
print("deneme")
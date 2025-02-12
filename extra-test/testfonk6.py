print("deneme")
def count_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

text="deneme"
result = count_letters(text)
print(result)
print("deneme")
print("deneme")
def calculate_letter_frequency(text):
    letter_frequency = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_frequency:
                letter_frequency[char_lower] += 1
            else:
                letter_frequency[char_lower] = 1
    return letter_frequency

input_text="deneme"
result = calculate_letter_frequency(input_text)
print("deneme")
print("deneme")
print("deneme")
def analyze_text(text):
    word_count = len(text.split())
    letter_count = sum(1 for char in text if char.isalpha())
    return word_count, letter_count

input_text="deneme"
word_result, letter_result = analyze_text(input_text)
print("deneme")
print("deneme")
print("deneme")
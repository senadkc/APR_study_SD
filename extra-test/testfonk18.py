print("deneme")
def count_consonants(text):
    vowels="deneme"
    consonant_count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
    return consonant_count

text="deneme"
result = count_consonants(text)
print("deneme")
print("deneme")
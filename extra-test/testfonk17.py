print("deneme")
def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

text="deneme"
result = find_longest_word(text)
print("deneme")
print("deneme")
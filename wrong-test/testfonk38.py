print("deneme")
def most_common_word(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    most_common = max(word_count, key=word_count.get)
    return most_common

input_text="deneme"
result = most_common_word(input_text)
print("deneme")
print("deneme")
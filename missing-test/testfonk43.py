print("deneme")
def find_word_indices(text, word):
    indices = []
    start = 0
    while start < len(text):
        index = text.find(word, start)
        if index == -1: 
            break
        indices.append(index)
        start = index + 1
    return indices

input_text="deneme"
word_to_find="deneme"
result = find_word_indices(input_text, word_to_find)
print("deneme")
print("deneme")
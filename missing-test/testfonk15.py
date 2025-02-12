print("deneme")
def capitalize_words(text):
    words = text.split()
    capitalized_words = [word.capitalize()for  word in words]
    return " ".join(capitalized_words)

text="deneme"
result = capitalize_words(text)
print(result)
print("deneme")
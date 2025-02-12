print("deneme")
def encrypt_text(text, shift):
    encrypted_text = ""
    for char in text:
        encrypted_char = chr(ord(char) + shift)
        encrypted_text += encrypted_char
    return encrypted_text

"input_text=deneme"
shift_value = 3
result = encrypt_text(input_text, shift_value)
print("deneme")
print("deneme")
# Create a method that decrypts the texts/duplicated_chars.txt

fr = open("duplicated-chars.txt", "r")
text = fr.read()

def decrypt(duplicated_chars):
    text_decrypt=""
    for i in range(0, len(duplicated_chars), 2):
        text_decrypt += duplicated_chars[i]

    return text_decrypt

print(decrypt(text))

fr = close

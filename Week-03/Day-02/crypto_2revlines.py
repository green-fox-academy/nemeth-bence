# Create a method that decrypts texts/reversed_zen_lines.txt
fr = open("reversed-lines.txt")
line = fr.readlines()

def decrypt(reverse):
    text=""
    for betu in range(0, len(line)):
        text += line[betu][::-1]
    return text

print(decrypt(line))

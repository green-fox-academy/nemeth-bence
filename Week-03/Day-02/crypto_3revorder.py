fr = open("reversed-order.txt")
line = fr.readlines()

def decrypt(reverse):
    text=""
    for betu in range(1, len(line) +1):
        text += line[-betu]

    return text

print(decrypt(line))

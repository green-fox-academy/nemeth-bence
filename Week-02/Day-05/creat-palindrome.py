# Create a function named create palindrome following your current language's style guide. It should take a string, create a palindrome from it and then return it.

def create_palindrome(text):
    text = text + text[::-1]
    return text

print(create_palindrome("Pali drón "))

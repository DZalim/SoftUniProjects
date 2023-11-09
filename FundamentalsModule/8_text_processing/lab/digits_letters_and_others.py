text = input()

digits = ""
letters = ""
characters = ""

for char in text:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char
    else:
        characters += char

print(digits)
print(letters)
print(characters)

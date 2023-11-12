import re

text = input()
word = input()

pattern = fr"\b{word}\b"

result = re.findall(pattern, text, re.IGNORECASE)

print(len(result))

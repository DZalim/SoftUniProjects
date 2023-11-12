import re

text = input()

pattern = r"\d+"

while text:
    result = re.findall(pattern, text)
    if result:
        print(" ".join(result), end=" ")
    text = input()

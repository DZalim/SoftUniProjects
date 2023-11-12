import re

text = input()

pattern = r"w{3}\.[A-Za-z0-9\-]+\.[a-z]+[\.?[a-z]*]*"

while text:
    result = re.findall(pattern, text)
    if result:
        print(*result)
    text = input()

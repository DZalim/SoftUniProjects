import re

text = input()

pattern = r"\s(([A-Za-z0-9]+[A-Za-z0-9\.\-\_]*)(@)([A-Za-z]+\-*[A-Za-z]*\.[A-Za-z\-]+(\.[[A-Za-z\-]+)*))"

result = re.finditer(pattern, text)

for match in result:
    if match:
        print(match.group(1))

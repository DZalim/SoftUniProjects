import re

input_rows = int(input())

pattern = r"\|(?P<Boss>[A-Z]{4,})\|:#(?P<Title>[A-Za-z]+\s[A-Za-z]+)#"

for row in range(input_rows):
    text_to_check = input()
    result = re.finditer(pattern, text_to_check)
    matches = []
    for match in result:
        matches.append(match.group('Boss'))
        matches.append(match.group('Title'))
    if matches:
        print(f"{matches[0]}, The {matches[1]}")
        print(f">> Strength: {len(matches[0])}")
        print(f">> Armor: {len(matches[1])}")
    else:
        print("Access denied!")

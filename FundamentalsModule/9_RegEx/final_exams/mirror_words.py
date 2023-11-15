import re

some_text = input()

pattern = r"([@#])(?P<first_word>[A-Za-z]{3,})\1{2}(?P<second_word>[A-Za-z]{3,})\1"

result = re.finditer(pattern, some_text)

found_pairs = 0
mirror_words = []
for match in result:
    words = match.groups()
    found_pairs += 1
    if match.group(2) == match.group(3)[::-1]:
        mirror_words.append(match.group(2))

if found_pairs > 0:
    print(f"{found_pairs} word pairs found!")
else:
    print(f"No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    for word in mirror_words:
        if word == mirror_words[-1]:
            print(f"{word} <=> {word[::-1]}")
        else:
            print(f"{word} <=> {word[::-1]}", end=", ")
else:
    print("No mirror words!")

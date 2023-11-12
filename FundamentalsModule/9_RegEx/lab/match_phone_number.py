import re

sequence_of_phone_numbers = input()

#pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"
#result = re.findall(pattern, sequence_of_phone_numbers)
#print(*result, sep=", ")

pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"
result = re.finditer(pattern, sequence_of_phone_numbers)
matches = []

for match in result:
    matches.append(match.group())

print(*matches, sep=", ")

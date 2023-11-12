import re
sequence_of_string = input()

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

result = re.findall(pattern, sequence_of_string)

print(*result, sep=" ")

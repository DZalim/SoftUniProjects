import re

sequence_of_dates = input()

pattern = r"\b(?P<Day>\d{2})([-.\/])(?P<Month>[A-Z][a-z)]{2})\2(?P<Year>\d{4})\b"

results = re.finditer(pattern, sequence_of_dates)

for match in results:
    match = match.groupdict()
    print(f"Day: {match['Day']}, Month: {match['Month']}, Year: {match['Year']}")

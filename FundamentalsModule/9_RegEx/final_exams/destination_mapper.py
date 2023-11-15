import re

some_text = input()

pattern = r"([=\/])([A-Z][A-Za-z]{2,})\1"

result = re.finditer(pattern, some_text)

destinations = []
travel_points = 0

for match in result:
    dest = match.group(2)
    travel_points += len(dest)
    destinations.append(dest)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")

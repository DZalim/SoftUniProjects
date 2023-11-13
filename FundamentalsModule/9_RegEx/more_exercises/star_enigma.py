import re

input_row = int(input())

pattern_to_count = r"[star]"
star_pattern = r"@(?P<Planet>[A-Za-z]+)[^@\-!:>]*:(?P<Population>[0-9]+)[^@\-!:>]*!(?P<Type>[A,D])![^@\-!:>]*->(?P<Soldiers>[0-9]+)"

attacked_planets = []
destroyed_planets = []

for row in range(input_row):
    text = input()
    result_pattern_to_count = re.findall(pattern_to_count, text, re.IGNORECASE)
    count = len(result_pattern_to_count)
    new_text = ""
    for character in text:
        new_text += chr(ord(character) - count)
    result_star_pattern = re.finditer(star_pattern, new_text)
    if result_star_pattern:
        for match in result_star_pattern:
            star_pattern_dict = match.groupdict()
            if star_pattern_dict["Type"] == "A":
                attacked_planets.append(star_pattern_dict["Planet"])
            elif star_pattern_dict["Type"] == "D":
                destroyed_planets.append(star_pattern_dict["Planet"])

print(f"Attacked planets: {len(attacked_planets)}")
attacked_planets.sort()
for planet in attacked_planets:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
destroyed_planets.sort()
for planet in destroyed_planets:
    print(f"-> {planet}")

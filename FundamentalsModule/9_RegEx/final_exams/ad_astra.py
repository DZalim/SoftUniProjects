import re

text_string = input()

pattern = r"(\||#)(?P<item_name>[A-Za-z\s]+)\1(?P<expiration_date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>[0-9]{1,5})\1"

result = re.finditer(pattern, text_string)

total_calories = 0
all_matches= []

for match in result:
    items_dict = match.groupdict()
    total_calories += float(items_dict["calories"])
    all_matches.append(items_dict)

days = int(total_calories // 2000)

print(f"You have food to last you for: {days} days!")
for matches in all_matches:
    print(f"Item: {matches['item_name']}, Best before: {matches['expiration_date']}, Nutrition: {matches['calories']}")

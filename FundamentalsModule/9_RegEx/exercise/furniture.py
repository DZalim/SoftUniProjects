import re

command = input()

pattern = r">>(?P<Furniture>[A-Za-z]+)<<(?P<Price>[0-9]+\.*[0-9]*)!(?P<Quantity>[0-9]+)"

total_sum = 0
print("Bought furniture:")
while command != "Purchase":
    result = re.finditer(pattern, command)
    if result:
        for match in result:
            furniture = match.groupdict()
            total_sum += float(furniture["Price"])*int(furniture["Quantity"])
            print(furniture["Furniture"])
    command = input()

print(f"Total money spend: {total_sum:.2f}")

import re

pattern =r"%(?P<Customer>[A-Z][a-z]+)%[^\|\$\%\.0-9]*<(?P<Product>\w+)>[^\|\$\%\.0-9]*\|(?P<Quantity>\d+)\|[^\|$\%\.0-9]*(?P<Price>[0-9]+\.?[0-9]*)\$"
total_income = 0

command = input()
while command != "end of shift":
    pattern_result = re.finditer(pattern, command)
    if pattern_result:
        for match in pattern_result:
            pattern_dict = match.groupdict()
            income = int(pattern_dict["Quantity"]) * float(pattern_dict["Price"])
            total_income += income
            print(f"{pattern_dict['Customer']}: {pattern_dict['Product']} - {income:.2f}")
    command = input()

print(f"Total income: {total_income:.2f}")

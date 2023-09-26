months = int(input())

total_electricity = 0
total_water = 0
total_internet = 0
total_other = 0

for bills in range(months):
    electricity = float(input())
    total_electricity +=electricity
    water = 20
    total_water += water
    internet = 15
    total_internet += internet
    other = (electricity + water + internet) * 1.2
    total_other += other

total_bills = total_other + total_water + total_electricity + total_internet
average_bills = total_bills / months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {average_bills:.2f} lv")

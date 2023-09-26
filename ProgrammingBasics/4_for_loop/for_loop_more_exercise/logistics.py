number_of_cargo = int(input())

tons_for_van = 0
tons_for_truck = 0
tons_for_train = 0
total_ton = 0
total_price = 0
price_per_ton = 0

for cargo in range(number_of_cargo):
    tons_of_cargo = float(input())
    if tons_of_cargo <= 3:
        tons_for_van += tons_of_cargo
        price_per_ton = 200
    elif 4 <= tons_of_cargo <= 11:
        tons_for_truck += tons_of_cargo
        price_per_ton = 175
    elif tons_of_cargo >= 12:
        tons_for_train += tons_of_cargo
        price_per_ton = 120
    total_price += price_per_ton * tons_of_cargo
    total_ton += tons_of_cargo

average_price = total_price / total_ton
percent_for_van = tons_for_van / total_ton * 100
percent_for_truck = tons_for_truck / total_ton * 100
percent_for_train = tons_for_train / total_ton * 100

print(f"{average_price:.2f}")
print(f"{percent_for_van:.2f}%")
print(f"{percent_for_truck:.2f}%")
print(f"{percent_for_train:.2f}%")

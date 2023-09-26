drink = input()
sugar = input()
number_of_drinks = int(input())

price_per_drink = 0

if drink == "Espresso":
    if sugar == "Without":
        price_per_drink = 0.90
        price_per_drink *= 0.65
    elif sugar == "Normal":
        price_per_drink = 1
    elif sugar == "Extra":
        price_per_drink = 1.20
    if number_of_drinks >= 5:
        price_per_drink *= 0.75
elif drink == "Cappuccino":
    if sugar == "Without":
        price_per_drink = 1
        price_per_drink *= 0.65
    elif sugar == "Normal":
        price_per_drink = 1.20
    elif sugar == "Extra":
        price_per_drink = 1.60
elif drink == "Tea":
    if sugar == "Without":
        price_per_drink = 0.50
        price_per_drink *= 0.65
    elif sugar == "Normal":
        price_per_drink = 0.60
    elif sugar == "Extra":
        price_per_drink = 0.70

total_price = number_of_drinks * price_per_drink

if total_price > 15:
    total_price *= 0.80

print(f"You bought {number_of_drinks} cups of {drink} for {total_price:.2f} lv.")

needed_profit = float(input())

counter = 0
total_price = 0

cocktail = input()
while cocktail != "Party!":
    count_of_cocktails = int(input())
    counter += 1
    price_per_cocktail = len(cocktail) * count_of_cocktails
    if price_per_cocktail % 2 != 0:
        price_per_cocktail *= 0.75
    total_price += price_per_cocktail
    if total_price >= needed_profit:
        break
    cocktail = input()


if total_price >= needed_profit:
    print("Target acquired.")
else:
    diff = abs(needed_profit - total_price)
    print(f"We need {diff:.2f} leva more.")
print(f"Club income - {total_price:.2f} leva.")

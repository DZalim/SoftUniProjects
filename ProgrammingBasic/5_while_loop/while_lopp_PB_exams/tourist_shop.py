budget = float(input())

number_of_products = 0
total_price = 0

name_of_product = input()
while name_of_product != "Stop":
    price_of_product = float(input())
    number_of_products += 1
    if number_of_products % 3 == 0:
        price_of_product *= 0.5
    total_price += price_of_product
    if budget < total_price:
        break
    name_of_product = input()

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"You bought {number_of_products} products for {total_price:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {diff:.2f} leva!")
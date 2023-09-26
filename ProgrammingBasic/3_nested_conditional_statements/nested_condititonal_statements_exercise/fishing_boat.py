budget = int(input())
season = input()
number_of_fishman = int(input())

price = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if number_of_fishman <= 6:
    price *= 0.90
elif number_of_fishman > 12:
    price *= 0.75
else:
    price *= 0.85

if number_of_fishman % 2 == 0 and season != "Autumn":
    price *= 0.95

diff = abs(budget - price)

if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
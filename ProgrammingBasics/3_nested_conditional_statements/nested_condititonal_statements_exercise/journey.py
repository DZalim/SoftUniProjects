budget = float(input())
season = input()

price = 0
destination = ""
type_of_rest = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = 0.3 * budget
        type_of_rest = "Camp"
    elif season == "winter":
        price = 0.7 * budget
        type_of_rest = "Hotel"
elif budget > 1000:
    destination = "Europe"
    price = 0.90 * budget
    type_of_rest = "Hotel"
else:
    destination = "Balkans"
    if season == "summer":
        price = 0.4 * budget
        type_of_rest = "Camp"
    elif season == "winter":
        price = 0.8 * budget
        type_of_rest = "Hotel"

diff = abs(budget - price)

print(f"Somewhere in {destination}")
print(f"{type_of_rest} - {price:.2f}")
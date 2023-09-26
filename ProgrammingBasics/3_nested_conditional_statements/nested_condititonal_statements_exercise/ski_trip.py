days = int(input())
type_of_room = input()
grade = input()

price_per_night = 0

overnight_stays = days - 1

if type_of_room == "room for one person":
    price_per_night = 18
elif type_of_room == "apartment":
    price_per_night = 25
    if days < 10:
        price_per_night *= 0.70
    elif days > 15:
        price_per_night *= 0.50
    else:
        price_per_night *= 0.65
elif type_of_room == "president apartment":
    price_per_night = 35
    if days < 10:
        price_per_night *= 0.90
    elif days > 15:
        price_per_night *= 0.80
    else:
        price_per_night *= 0.85

if grade == "positive":
    price_per_night *= 1.25
elif grade == "negative":
    price_per_night *= 0.90

price = price_per_night * overnight_stays

print(f"{price:.2f}")

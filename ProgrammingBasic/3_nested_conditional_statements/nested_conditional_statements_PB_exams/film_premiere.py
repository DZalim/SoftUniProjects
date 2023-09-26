projection = input()
packet = input()
number_of_ticket = int(input())

price_per_ticket = 0

if projection == "John Wick":
    if packet == "Drink":
        price_per_ticket = 12
    elif packet == "Popcorn":
        price_per_ticket = 15
    elif packet == "Menu":
        price_per_ticket = 19
elif projection == "Star Wars":
    if packet == "Drink":
        price_per_ticket = 18
    elif packet == "Popcorn":
        price_per_ticket = 25
    elif packet == "Menu":
        price_per_ticket = 30
    if number_of_ticket >= 4:
        price_per_ticket *= 0.70
elif projection == "Jumanji":
    if packet == "Drink":
        price_per_ticket = 9
    elif packet == "Popcorn":
        price_per_ticket = 11
    elif packet == "Menu":
        price_per_ticket = 14
    if number_of_ticket == 2:
        price_per_ticket *= 0.85

price = price_per_ticket * number_of_ticket

print(f"Your bill is {price:.2f} leva.")





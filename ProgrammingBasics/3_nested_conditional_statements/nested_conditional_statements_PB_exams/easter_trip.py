destination = input()
days = input()
number_of_overnight_stays = int(input())

price_per_overnight = 0

if destination == "France":
    if days == "21-23":
        price_per_overnight = 30
    elif days == "24-27":
        price_per_overnight = 35
    elif days == "28-31":
        price_per_overnight = 40
elif destination == "Italy":
    if days == "21-23":
        price_per_overnight = 28
    elif days == "24-27":
        price_per_overnight = 32
    elif days == "28-31":
        price_per_overnight = 39
elif destination == "Germany":
    if days == "21-23":
        price_per_overnight = 32
    elif days == "24-27":
        price_per_overnight = 37
    elif days == "28-31":
        price_per_overnight = 43

total_price = number_of_overnight_stays * price_per_overnight

print(f"Easter trip to {destination} : {total_price:.2f} leva.")
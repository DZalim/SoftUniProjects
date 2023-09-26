stage_of_the_championship = input()
type_of_ticket = input()
number_of_ticket = int(input())
pictures = input()

price_per_picture = 0
price_per_ticket = 0

if stage_of_the_championship == "Quarter final":
    if type_of_ticket == "Standard":
        price_per_ticket = 55.50
    elif type_of_ticket == "Premium":
        price_per_ticket = 105.20
    elif type_of_ticket == "VIP":
        price_per_ticket = 118.90
elif stage_of_the_championship == "Semi final":
    if type_of_ticket == "Standard":
        price_per_ticket = 75.88
    elif type_of_ticket == "Premium":
        price_per_ticket = 125.22
    elif type_of_ticket == "VIP":
        price_per_ticket = 300.40
elif stage_of_the_championship == "Final":
    if type_of_ticket == "Standard":
        price_per_ticket = 110.10
    elif type_of_ticket == "Premium":
        price_per_ticket = 160.66
    elif type_of_ticket == "VIP":
        price_per_ticket = 400

total_price = number_of_ticket * price_per_ticket

if pictures == "Y":
    price_per_picture = 40 * number_of_ticket

if total_price > 4000:
    total_price *= 0.75
elif 2500 < total_price <= 4000:
    total_price = total_price * 0.9 + price_per_picture
else:
    total_price = total_price + price_per_picture

print(f"{total_price: .2f}")

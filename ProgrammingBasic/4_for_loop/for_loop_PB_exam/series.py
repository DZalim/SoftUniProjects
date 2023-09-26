budget = float(input())
number_of_serials = int(input())

total_price = 0

for serial in range (number_of_serials):
    name_of_serial = input()
    price = float(input())
    if name_of_serial == "Thrones":
        total_price += price * 0.50
    elif name_of_serial == "Lucifer":
        total_price += price * 0.60
    elif name_of_serial == "Protector":
        total_price += price * 0.70
    elif name_of_serial == "TotalDrama":
        total_price += price * 0.80
    elif name_of_serial == "Area":
        total_price += price * 0.90
    else:
        total_price += price

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")
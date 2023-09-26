number_of_days = int(input())
number_of_hours_per_day = int(input())

total_pay = 0

for day in range (1, number_of_days +1):
    price_per_day = 0
    for hour in range (1, number_of_hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            price = 1.25
        else:
            price = 1
        price_per_day += price
    total_pay += price_per_day
    print(f"Day: {day} - {price_per_day:.2f} leva")

print(f"Total: {total_pay:.2f} leva")


budget_for_travel = float(input())
needed_litres_of_fuel = float(input())
day_of_week = input()

price_for_litres_of_fuel = 2.10
tour_guide = 100
discount_for_saturday = 0.10
discount_for_sunday = 0.20

price_for_fuel = needed_litres_of_fuel * price_for_litres_of_fuel
needed_sum = price_for_fuel + tour_guide

if day_of_week == "Saturday":
    needed_sum *= 0.90
elif day_of_week == "Sunday":
    needed_sum *= 0.80

diff = abs(needed_sum - budget_for_travel)

if budget_for_travel>= needed_sum:
    print(f"Safari time! Money left: {diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")



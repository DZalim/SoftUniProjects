budget_for_movie = float(input())
number_of_statist = int(input())
price_for_one_dress = float(input())

price_for_decor = budget_for_movie * 0.10
if number_of_statist > 150:
    price_for_one_dress *= 0.90

total_sum = number_of_statist * price_for_one_dress + price_for_decor
diff = abs(budget_for_movie - total_sum)

if total_sum > budget_for_movie:
    print(f"Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
budget_for_movie = float(input())
number_of_statists = int(input())
price_for_dress_for_one_statist = float(input())

decor = budget_for_movie * 0.10

if number_of_statists > 150:
    price_for_dress_for_one_statist *= 0.9

needed_money = number_of_statists * price_for_dress_for_one_statist + decor
diff = abs(needed_money - budget_for_movie)

if needed_money > budget_for_movie:
    print(f"Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print(f"Action!" )
    print(f"Wingard starts filming with {diff:.2f} leva left.")
budget = float(input())
number_of_over_nihgts = int(input())
price_for_over_nights = float(input())
percent_for_additional_expenses = int(input())

if number_of_over_nihgts > 7:
    price_for_over_nights *= 0.95

needed_money = number_of_over_nihgts * price_for_over_nights + (budget * (percent_for_additional_expenses/100))
diff = abs(budget - needed_money)

if budget >= needed_money:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
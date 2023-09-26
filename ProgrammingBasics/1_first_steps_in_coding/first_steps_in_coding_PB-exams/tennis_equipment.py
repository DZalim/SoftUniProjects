import math

price_for_tennis_racket = float(input())
number_of_tennis_racket = int(input())
number_of_pair_of_sneakers = int(input())

price_for_pair_of_sneakers = price_for_tennis_racket * (1/6)
expenses = price_for_pair_of_sneakers * number_of_pair_of_sneakers + price_for_tennis_racket * number_of_tennis_racket
total_expenses = expenses + expenses * 0.20

expenses_for_him = math.floor(total_expenses * (1/8))
expenses_for_others = math.ceil(total_expenses * (7/8))

print(f"Price to be paid by Djokovic {expenses_for_him}")
print(f"Price to be paid by sponsors {expenses_for_others}")


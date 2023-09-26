annual_training_fee = int(input())

price_for_sneakers = annual_training_fee * 0.60
price_for_outfit = price_for_sneakers * 0.80
price_for_ball = price_for_outfit * 0.25
price_for_accessories = price_for_ball * 0.20

total_expenses = annual_training_fee + price_for_accessories + price_for_ball + price_for_outfit + price_for_sneakers

print(f"{total_expenses:.2f}")
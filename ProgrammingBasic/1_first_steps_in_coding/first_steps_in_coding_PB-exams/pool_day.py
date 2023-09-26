import math

number_of_people = int(input())
entrance_fee = float(input())
price_for_one_lounger = float(input())
price_for_one_umbrella = float(input())

entrance_fee_for_all_people = number_of_people * entrance_fee
people_for_umbrella = math.ceil(number_of_people / 2)
price_for_umbrella = people_for_umbrella * price_for_one_umbrella
people_for_lounger = math.ceil(number_of_people * 0.75)
price_for_lounger = people_for_lounger * price_for_one_lounger

total = entrance_fee_for_all_people + price_for_lounger + price_for_umbrella

print(f"{total:.2f}", "lv.")

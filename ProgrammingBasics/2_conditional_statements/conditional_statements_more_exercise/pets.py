import math

number_of_days = int(input())
left_food_in_kg = int(input())
food_for_dog_per_day_in_kg = float(input())
food_for_cat_per_day_in_kg = float(input())
food_for_turtle_per_day_in_gr = float(input())

food_for_turtle_per_day_in_kg = food_for_turtle_per_day_in_gr / 1000

total_needed_food = number_of_days * food_for_dog_per_day_in_kg \
                    + number_of_days * food_for_cat_per_day_in_kg \
                    + number_of_days * food_for_turtle_per_day_in_kg

diff = abs(left_food_in_kg - total_needed_food)

if left_food_in_kg > total_needed_food:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")

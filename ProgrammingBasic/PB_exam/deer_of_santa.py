import math

number_of_days_off = int(input())
left_food_in_kg = int(input())
food_ing_kg_per_day_for_first_deer = float(input())
food_ing_kg_per_day_for_second_deer = float(input())
food_ing_kg_per_day_for_third_deer = float(input())

needed_food_for_first_deer = number_of_days_off * food_ing_kg_per_day_for_first_deer
needed_food_for_second_deer = number_of_days_off * food_ing_kg_per_day_for_second_deer
needed_food_for_third_deer = number_of_days_off * food_ing_kg_per_day_for_third_deer
total_needed_food =  needed_food_for_third_deer + needed_food_for_second_deer + needed_food_for_first_deer

diff = abs(left_food_in_kg - total_needed_food)

if left_food_in_kg >= total_needed_food:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")

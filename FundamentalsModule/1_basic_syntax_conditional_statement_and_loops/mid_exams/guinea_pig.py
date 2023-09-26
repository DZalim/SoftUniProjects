quantity_food_in_kilograms = float(input())
quantity_hay_in_kilograms = float(input())
quantity_cover_in_kilograms = float(input())
guinea_weight_in_kilograms = float(input())

for day in range (1, 31):
    needed_quantity_food_per_day = 0.300
    quantity_food_in_kilograms -= needed_quantity_food_per_day
    if day % 2 == 0:
        needed_quantity_hay_per_day = quantity_food_in_kilograms * 0.05
        quantity_hay_in_kilograms -= needed_quantity_hay_per_day
    if day % 3 == 0:
        needed_quantity_cover_per_day = 1/3 * guinea_weight_in_kilograms
        quantity_cover_in_kilograms -= needed_quantity_cover_per_day

if quantity_food_in_kilograms <= 0 or quantity_hay_in_kilograms <= 0 or quantity_cover_in_kilograms <= 0:
    print(f"Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food_in_kilograms:.2f}, Hay: {quantity_hay_in_kilograms:.2f}, Cover: {quantity_cover_in_kilograms:.2f}.")


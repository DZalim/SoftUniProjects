number_of_days = int(input())
quantity_of_food = float(input())

total_dog = 0
total_cat = 0
biscuits = 0
total_food = 0

for day in range (1, number_of_days + 1):
    quantity_dog = float(input())
    quantity_cat = float(input())
    total_dog += quantity_dog
    total_cat += quantity_cat
    total_food += quantity_cat + quantity_dog
    if day % 3 == 0:
        biscuits += round(0.10 * (quantity_cat + quantity_dog))

percent_food = total_food / quantity_of_food * 100
percent_dog = total_dog / total_food * 100
percent_cat = total_cat / total_food * 100

print(f"Total eaten biscuits: {biscuits}gr.")
print(f"{percent_food:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")


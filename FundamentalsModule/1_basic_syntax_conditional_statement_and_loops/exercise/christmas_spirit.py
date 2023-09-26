quantity_of_decorations = int(input())
left_days = int(input())

total_cost = 0
total_spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

for day in range (1, left_days+1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        total_cost += quantity_of_decorations * ornament_set_price
        total_spirit += 5
    if day % 3 == 0:
        total_cost += quantity_of_decorations * (tree_skirt_price + tree_garland_price)
        total_spirit += 3 + 10
    if day % 5 == 0:
        total_cost += quantity_of_decorations * tree_lights_price
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price

if left_days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")



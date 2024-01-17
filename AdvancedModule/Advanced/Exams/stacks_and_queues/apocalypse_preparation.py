from collections import deque

textiles = deque(int(textile) for textile in input().split())  # queue
medicaments = deque(int(medicament) for medicament in input().split())  # stack

healing_items = {}

while textiles and medicaments:
    first_textile = textiles.popleft()
    last_medicament = medicaments.pop()

    sum_of_items = first_textile + last_medicament

    if sum_of_items == 30:
        healing_items['Patch'] = healing_items.get('Patch', 0) + 1
    elif sum_of_items == 40:
        healing_items['Bandage'] = healing_items.get('Bandage', 0) + 1
    elif sum_of_items == 100:
        healing_items['MedKit'] = healing_items.get('MedKit', 0) + 1
    elif sum_of_items > 100:
        healing_items['MedKit'] = healing_items.get('MedKit', 0) + 1
        difference = sum_of_items - 100
        if medicaments:
            medicaments[-1] += difference
    else:
        medicament_value = last_medicament + 10
        medicaments.append(medicament_value)

if not textiles and medicaments:
    print("Textiles are empty.")
elif not medicaments and textiles:
    print("Medicaments are empty.")
elif not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

sorted_dict_by_key = dict(sorted(healing_items.items()))
sorted_healing_items = sorted(sorted_dict_by_key, key=sorted_dict_by_key.get, reverse=True)

for key_item in sorted_healing_items:
    print(f"{key_item} - {healing_items[key_item]}")

if medicaments:
    medicaments.reverse()
    print('Medicaments left:', end=" ")
    print(*medicaments, sep=", ")
if textiles:
    print('Textiles left:', end=" ")
    print(*textiles, sep=", ")

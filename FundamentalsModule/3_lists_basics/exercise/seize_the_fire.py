strings_in_list = input().split("#")
amount_of_water = int(input())

effort = 0
total_fire = 0

print("Cells:")

for fire_cell in strings_in_list:
    current_cell = fire_cell.split()
    if (current_cell[0] == "High" and 81 <= int(current_cell[2]) <= 125) or\
    (current_cell[0] == "Medium" and 51 <= int(current_cell[2]) <= 80) or\
    (current_cell[0] == "Low" and 1 <= int(current_cell[2]) <= 50):
        if amount_of_water - total_fire >= int(current_cell[2]):
            print(f" - {int(current_cell[2])}")
            effort += 0.25 * int(current_cell[2])
            total_fire += int(current_cell[2])

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
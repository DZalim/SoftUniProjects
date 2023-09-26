number_of_bottles = int(input())

quantity_of_preparation = number_of_bottles * 750
needed_quantity_for_plates = 0
needed_quantity_for_pots = 0
total_plates = 0
total_pots = 0
counter = 0

command = input()
while command != "End":
    number_of_dishes = int(command)
    counter += 1
    if counter % 3 != 0:
        total_plates += number_of_dishes
        needed_quantity_for_plates += number_of_dishes * 5
    else:
        total_pots += number_of_dishes
        needed_quantity_for_pots += number_of_dishes * 15
    total_needed_quantity = needed_quantity_for_pots + needed_quantity_for_plates
    if quantity_of_preparation < total_needed_quantity:
        break
    command = input()

diff = abs(total_needed_quantity - quantity_of_preparation)
if quantity_of_preparation < total_needed_quantity:
    print(f"Not enough detergent, {diff} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{total_plates} dishes and {total_pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")


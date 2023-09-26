baggage_capacity = float(input())

number_of_suitcase = 0

command = input()
while command != "End":
    suitcase_volume = float(command)
    if baggage_capacity >= suitcase_volume:
        number_of_suitcase += 1
        if number_of_suitcase % 3 == 0:
            suitcase_volume *= 1.1
        baggage_capacity -= suitcase_volume
    else:
        break
    command = input()

if command == "End" or baggage_capacity == 0:
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {number_of_suitcase} suitcases loaded.")
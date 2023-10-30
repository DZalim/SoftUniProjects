list_of_treasure_chest = input().split("|")
command = input()

stealed_items = []

while "Yohoho!" not in command:
    current_command = command.split()
    initial_loot = current_command[0]
    if initial_loot == "Loot":
        for item in current_command:
            if item == "Loot":
                continue
            if item not in list_of_treasure_chest:
                list_of_treasure_chest.insert(0, item)
    elif initial_loot == "Drop":
        if int(current_command[1]) < len(list_of_treasure_chest):
            list_of_treasure_chest.append(list_of_treasure_chest[int(current_command[1])])
            for item in list_of_treasure_chest:
                if item == list_of_treasure_chest[int(current_command[1])]:
                    list_of_treasure_chest.remove(item)
                    break
    elif initial_loot == "Steal":
        if int(current_command[1]) < len(list_of_treasure_chest):
            for steal in range (int(current_command[1])):
                stealed_items.append(list_of_treasure_chest[-1])
                list_of_treasure_chest.remove(list_of_treasure_chest[-1])
            stealed_items.reverse()
            print(", ".join(stealed_items))
        else:
            stealed_items = list_of_treasure_chest
            print(", ".join(stealed_items))
            list_of_treasure_chest = []
    command = input()

if len(list_of_treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    sum_of_all_items = 0
    for item in list_of_treasure_chest:
        sum_of_all_items += len(item)
    sum_of_all_items = sum_of_all_items / len(list_of_treasure_chest)
    print(f"Average treasure gain: {sum_of_all_items:.2f} pirate credits.")

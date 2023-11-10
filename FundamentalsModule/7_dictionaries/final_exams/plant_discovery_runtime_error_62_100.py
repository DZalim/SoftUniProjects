number_of_lines = int(input())

my_dict_with_plant_and_rarity = {}

for line in range(number_of_lines):
    current_plant, current_rarity = input().split("<->")
    my_dict_with_plant_and_rarity[current_plant] = [int(current_rarity)]

command = input()
while command != "Exhibition":
    split_command = command.split(": ")
    second_split = split_command[1].split(" - ")
    action = split_command[0]
    plant = second_split[0]
    if action == "Rate":
        rating = int(second_split[1])
        if plant in my_dict_with_plant_and_rarity.keys() and len(my_dict_with_plant_and_rarity[plant]) == 1:
            my_dict_with_plant_and_rarity[plant].append([])
        my_dict_with_plant_and_rarity[plant][1].append(rating)
    elif action == "Update":
        new_rarity = int(second_split[1])
        if plant in my_dict_with_plant_and_rarity.keys():
            my_dict_with_plant_and_rarity[plant][0] = new_rarity
    elif action == "Reset":
        if plant in my_dict_with_plant_and_rarity.keys():
            if len(my_dict_with_plant_and_rarity[plant]) > 1:
                my_dict_with_plant_and_rarity[plant][1].clear()
    if plant not in my_dict_with_plant_and_rarity.keys():
        print("error")
    command = input()

print(f"Plants for the exhibition:")

for plant_name, plant_values in my_dict_with_plant_and_rarity.items():
    if len(plant_values[1]) > 0:
        average_rating = sum(plant_values[1])/len(plant_values[1])
    else:
        average_rating = 0
    print(f"- {plant_name}; Rarity: {plant_values[0]}; Rating: {average_rating:.2f}")

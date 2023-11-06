first_command = input()

my_dict_with_towns = {}

while first_command != "Sail":
    current_city, current_population, current_gold = first_command.split("||")
    current_population = int(current_population)
    current_gold = int(current_gold)
    if current_city not in my_dict_with_towns.keys():
        my_dict_with_towns[current_city] = [0, 0]
    my_dict_with_towns[current_city][0] += current_population
    my_dict_with_towns[current_city][1] += current_gold
    first_command = input()

second_command = input()
while second_command != "End":
    split_command = second_command.split("=>")
    action = split_command[0]
    if action == "Plunder":
        city, population, gold = split_command[1], int(split_command[2]), int(split_command[3])
        if city in my_dict_with_towns.keys():
            my_dict_with_towns[city][0] -= population
            my_dict_with_towns[city][1] -= gold
            print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
        if my_dict_with_towns[city][0] <= 0 or my_dict_with_towns[city][1] <= 0:
            del my_dict_with_towns[city]
            print(f"{city} has been wiped off the map!")
    elif action == "Prosper":
        city, gold = split_command[1], int(split_command[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            my_dict_with_towns[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {my_dict_with_towns[city][1]} gold.")
    second_command = input()


if len(my_dict_with_towns) > 0:
    print(f"Ahoy, Captain! There are {len(my_dict_with_towns)} wealthy settlements to go to:")
    for town, town_values in my_dict_with_towns.items():
        print(f"{town} -> Population: {town_values[0]} citizens, Gold: {town_values[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

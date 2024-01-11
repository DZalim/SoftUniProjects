animals_information = input().split(": ")

my_dict_with_animals = {}
my_dict_with_areas = {}
animals_area = {}

while animals_information[0] != "EndDay":
    action = animals_information[0]
    split_second_part = animals_information[1].split("-")
    name_of_animal = split_second_part[0]
    food_in_gr = int(split_second_part[1])
    if action == "Add":
        current_area = split_second_part[2]
        if current_area not in my_dict_with_areas.keys():
            my_dict_with_areas[current_area] = 1
        elif current_area in my_dict_with_areas.keys():
            if name_of_animal not in my_dict_with_animals.keys():
                my_dict_with_areas[current_area] += 1
        if name_of_animal not in my_dict_with_animals.keys():
            my_dict_with_animals[name_of_animal] = 0
        my_dict_with_animals[name_of_animal] += food_in_gr
        if name_of_animal not in animals_area.keys():
            animals_area[name_of_animal] = current_area
    elif action == "Feed":
        if name_of_animal in my_dict_with_animals.keys():
            my_dict_with_animals[name_of_animal] -= food_in_gr
            if my_dict_with_animals[name_of_animal] <= 0:
                my_dict_with_animals.pop(name_of_animal)
                print(f"{name_of_animal} was successfully fed")
                if name_of_animal in animals_area.keys():
                    area_for_decrease = animals_area[name_of_animal]
                    my_dict_with_areas[area_for_decrease] -= 1
                    if my_dict_with_areas[area_for_decrease] == 0:
                        my_dict_with_areas.pop(area_for_decrease)
    animals_information = input().split(": ")

print("Animals:")
for key, value in my_dict_with_animals.items():
    print(f" {key} -> {value}g")

print("Areas with hungry animals:")
for key, value in my_dict_with_areas.items():
    print(f" {key}: {value}")

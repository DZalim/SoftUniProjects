import re

list_of_participants = input().split(", ")

name_pattern = r"[A-Za-z]"
digit_pattern = r"[0-9]"

total_distance_for_racer = {}

command = input()
while command != "end of race":
    name_pattern_result = re.findall(name_pattern, command)
    digit_patter_result = re.findall(digit_pattern, command)
    if "".join(name_pattern_result) in list_of_participants:
        name_key = "".join(name_pattern_result)
        distance = 0
        for number in digit_patter_result:
            distance += int(number)
        if name_key not in total_distance_for_racer.keys():
            total_distance_for_racer[name_key] = 0
        total_distance_for_racer[name_key] += distance
    command = input()

sorted_dictionary = sorted(total_distance_for_racer.items(), key=lambda x: x[1], reverse=True)
total_distance_for_racer.clear()
for key, value in sorted_dictionary:
    total_distance_for_racer[key] = value

iterate = 1
for key, value in total_distance_for_racer.items():
    if iterate == 1:
        print(f"1st place: {key}")
    elif iterate == 2:
        print(f"2nd place: {key}")
    elif iterate == 3:
        print(f"3rd place: {key}")
    if iterate == 3:
        break
    iterate += 1

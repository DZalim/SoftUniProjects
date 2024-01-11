import re

name_of_demon = input().split(", ")

health_pattern = r"[^\d\+\-\*\/\.]"
number_pattern = r"\-?[0-9][1-9]*\.?[0-9]*"
divide_and_multiplication_pattern = r"[\*\/]"

dict_of_demon = {}

for demon in name_of_demon:
    if demon not in dict_of_demon.keys():
        dict_of_demon[demon] = {"health": 0, "damage": 0.00}

    result_health_pattern = re.findall(health_pattern, demon)
    if result_health_pattern:
        health = 0
        for char in result_health_pattern:
            health += ord(char)
        dict_of_demon[demon]["health"] = health

    result_number_pattern = re.findall(number_pattern, demon)
    if result_number_pattern:
        damage = 0
        for number in result_number_pattern:
            damage += float(number)
        dict_of_demon[demon]["damage"] = damage

    result_divide_and_multiplication = re.findall(divide_and_multiplication_pattern, demon)
    if result_divide_and_multiplication:
        for symbol in result_divide_and_multiplication:
            if symbol == "*":
                dict_of_demon[demon]["damage"] = dict_of_demon[demon]["damage"] * 2
            elif symbol == "/":
                dict_of_demon[demon]["damage"] = dict_of_demon[demon]["damage"] / 2

dict_of_demon_sorted = dict(sorted(dict_of_demon.items()))

for key, value in dict_of_demon_sorted.items():
    print(f"{key} - {dict_of_demon_sorted[key]['health']} health, {dict_of_demon_sorted[key]['damage']:.2f} damage")

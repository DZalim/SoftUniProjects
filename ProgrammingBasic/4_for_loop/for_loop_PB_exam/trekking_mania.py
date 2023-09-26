number_of_groups = int(input())

musala_climbers = 0
monblan_climbers = 0
kilimandzharo_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0

for group in range (number_of_groups):
    number_of_climbers = int(input())
    if number_of_climbers <= 5:
        musala_climbers += number_of_climbers
    elif 6 <= number_of_climbers <= 12:
        monblan_climbers += number_of_climbers
    elif 13 <= number_of_climbers <= 25:
        kilimandzharo_climbers += number_of_climbers
    elif 26 <= number_of_climbers <= 40:
        k2_climbers += number_of_climbers
    elif number_of_climbers > 40:
        everest_climbers += number_of_climbers
    total_climbers += number_of_climbers

percent_musala_climbers = musala_climbers / total_climbers * 100
percent_monblan_climbers = monblan_climbers / total_climbers * 100
percent_kilimandzharo_climbers = kilimandzharo_climbers / total_climbers * 100
percent_k2_climbers = k2_climbers / total_climbers * 100
percent_everest_climbers = everest_climbers / total_climbers * 100

print(f"{percent_musala_climbers:.2f}%")
print(f"{percent_monblan_climbers:.2f}%")
print(f"{percent_kilimandzharo_climbers:.2f}%")
print(f"{percent_k2_climbers:.2f}%")
print(f"{percent_everest_climbers:.2f}%")
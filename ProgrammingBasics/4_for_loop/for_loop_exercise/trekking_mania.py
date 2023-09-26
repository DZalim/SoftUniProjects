number_of_groups = int(input())

musala_climbers = 0
monblan_climbers = 0
kilimandzharo_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0

for climbers in range (number_of_groups):
    number_of_climbers = int(input())
    total_climbers +=number_of_climbers
    if number_of_climbers <= 5:
        musala_climbers += number_of_climbers
    elif 5 < number_of_climbers <= 12:
        monblan_climbers += number_of_climbers
    elif 12 < number_of_climbers <= 25:
        kilimandzharo_climbers += number_of_climbers
    elif 25 < number_of_climbers <= 40:
        k2_climbers += number_of_climbers
    elif number_of_climbers > 40:
        everest_climbers += number_of_climbers

musala_percent = musala_climbers / total_climbers * 100
monblan_percent = monblan_climbers / total_climbers * 100
kilimandzharo_percent = kilimandzharo_climbers / total_climbers * 100
k2_percent = k2_climbers / total_climbers * 100
everest_percent = everest_climbers / total_climbers * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandzharo_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")



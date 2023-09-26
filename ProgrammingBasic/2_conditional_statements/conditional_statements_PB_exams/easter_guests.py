import math

number_of_guests = int(input())
budget = float(input())

price_for_one_easter_bread = 4
price_for_one_egg = 0.45

total_easter_bread = math.ceil(number_of_guests / 3)
total_for_easter_bread = total_easter_bread * price_for_one_easter_bread
total_egg = number_of_guests * 2
total_for_egg = total_egg * price_for_one_egg
total_sum = total_for_egg + total_for_easter_bread

diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Lyubo bought {total_easter_bread} Easter bread and {total_egg} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")

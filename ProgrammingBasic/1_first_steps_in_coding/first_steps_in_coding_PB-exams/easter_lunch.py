number_of_easter_bread = int(input())
number_of_egg_shells = int(input())
kg_of_cookies = int(input())

price_for_easter_bread = 3.20
price_for_egg_shells = 4.35
price_for_kg_of_cookies = 5.40
paint_for_egg = 0.15

expenses = number_of_easter_bread * price_for_easter_bread + number_of_egg_shells * price_for_egg_shells + \
           kg_of_cookies * price_for_kg_of_cookies + (number_of_egg_shells * 12 *paint_for_egg)

print(f"{expenses:.2f}")

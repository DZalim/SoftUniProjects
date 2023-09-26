number_of_chicken_menu = int(input())
number_of_fish_menu = int(input())
number_of_veg_menu = int(input())

chicken_menu = 10.35
fish_menu = 12.40
veg_menu = 8.15
delivery = 2.50

chicken = number_of_chicken_menu * chicken_menu
fish = number_of_fish_menu * fish_menu
veg = number_of_veg_menu * veg_menu

total_without_desert = chicken + fish + veg
dessert = total_without_desert * 0.2
total = total_without_desert + dessert + delivery

print(total)


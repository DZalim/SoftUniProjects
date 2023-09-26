lenght = int(input())
width = int(input())
height = int(input())
percent_non_free_volume = float(input())

fish_tank_volume_in_centimeters = lenght * width * height
fish_tank_volume_in_liters = fish_tank_volume_in_centimeters / 1000 # *0.001
percentage = percent_non_free_volume / 100 # *0.01
needed_liters = fish_tank_volume_in_liters * (1 - percentage)

print(needed_liters)

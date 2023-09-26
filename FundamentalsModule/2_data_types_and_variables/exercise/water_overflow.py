numbers_of_pour = int(input())
tank_capacity = 255
filled_water = 0

for water in range (numbers_of_pour):
    litres_of_water = int(input())
    if litres_of_water > tank_capacity:
        print("Insufficient capacity!")
        continue
    filled_water += litres_of_water
    tank_capacity -= litres_of_water

print(filled_water)


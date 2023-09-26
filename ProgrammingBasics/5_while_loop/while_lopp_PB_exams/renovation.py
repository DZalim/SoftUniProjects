from math import ceil

room_height = int(input())
room_width = int(input())
percent_windows = int(input())

walls_for_painting = ceil((room_height * room_width * 4) - ((room_width * room_height * 4) * (percent_windows / 100)))
painted_walls = 0

command = input()
while command != "Tired!":
    litres_paint = int(command)
    painted_walls += litres_paint
    if painted_walls >= walls_for_painting:
        break
    command = input()

diff = abs(walls_for_painting - painted_walls)
if painted_walls == walls_for_painting:
    print("All walls are painted! Great job, Pesho!")
elif painted_walls > walls_for_painting:
    print(f"All walls are painted and you have {diff} l paint left!")
else:
    print(f"{diff} quadratic m left.")
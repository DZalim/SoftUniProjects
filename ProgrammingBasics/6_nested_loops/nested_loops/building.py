number_of_floors = int(input())
number_of_rooms = int(input())

for floor in reversed(range(1, number_of_floors + 1)):
    for room in range (number_of_rooms):
        room_type = "A" if floor % 2 == 1 else "O"
        if floor == number_of_floors:
            room_type = "L"
        print(f"{room_type}{floor}{room}", end=" ")
    print()


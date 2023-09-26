name_of_player = input()

points = 301
successful_shots = 0
unsuccessful_shots = 0

command = input()
while command != "Retire":
    current_points = int(input())
    if command == "Single":
        current_points *= 1
    elif command == "Double":
        current_points *= 2
    elif command == "Triple":
        current_points *= 3
    if points >= current_points:
        successful_shots += 1
        points -= current_points
    else:
        unsuccessful_shots += 1
    if points == 0:
        break
    command = input()

if command == "Retire":
    print(f"{name_of_player} retired after {unsuccessful_shots} unsuccessful shots.")
else:
    print(f"{name_of_player} won the leg with {successful_shots} shots.")
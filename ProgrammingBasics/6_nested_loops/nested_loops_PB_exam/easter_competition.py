number_of_easter_bread = int(input())

max_points = 0
best_baker = ""

for easter_bread in range(number_of_easter_bread):
    name_of_baker = input()
    command = input()
    points = 0
    while command != "Stop":
        grade = int(command)
        points += grade
        command = input()
    print(f"{name_of_baker} has {points} points.")
    if points > max_points:
        max_points = points
        best_baker = name_of_baker
        print(f"{name_of_baker} is the new number 1!")

print(f"{best_baker} won competition with {max_points} points!")

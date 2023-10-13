number_of_wagons = int(input())
peoples_in_wagons = [0] * number_of_wagons

command = input()
while command != "End":
    splitted_command = command.split()
    action = splitted_command[0]
    if action == "add":
        number_of_people = int(splitted_command[1])
        peoples_in_wagons[-1] += number_of_people
    elif action == "insert":
        index_of_wagon = int(splitted_command[1])
        number_of_people = int(splitted_command[2])
        peoples_in_wagons[index_of_wagon] += number_of_people
    elif action == "leave":
        index_of_wagon = int(splitted_command[1])
        number_of_people = int(splitted_command[2])
        peoples_in_wagons[index_of_wagon] -= number_of_people
    command = input()

print(peoples_in_wagons)

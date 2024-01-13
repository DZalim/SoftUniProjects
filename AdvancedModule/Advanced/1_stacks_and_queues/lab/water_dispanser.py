from collections import deque

quantity_of_water = int(input())

people_wants_water = deque()

command = input()
while command != "Start":
    people_wants_water.append(command)
    command = input()

command = input().split()
while command[0] != "End":
    if len(command) == 1:
        wanted_water = int(command[0])
        current_people = people_wants_water.popleft()
        if quantity_of_water >= wanted_water:
            quantity_of_water -= wanted_water
            print(f"{current_people} got water")
        else:
            print(f"{current_people} must wait")
    else:
        litres_to_refill = int(command[1])
        quantity_of_water += litres_to_refill
    command = input().split()

print(f"{quantity_of_water} liters left")

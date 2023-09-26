hall_capacity = int(input())

number_of_peoples = 0
income = 0
cinema_full = False

command = input()
while command != "Movie time!":
    entered_people = int(command)
    number_of_peoples += entered_people
    if number_of_peoples > hall_capacity:
        cinema_full = True
        break
    else:
        income += entered_people * 5
        if entered_people % 3 == 0:
            income -= 5
    command = input()

diff = abs(hall_capacity - number_of_peoples)

if cinema_full:
    print("The cinema is full.")
else:
    print(f"There are {diff} seats left in the cinema.")
print(f"Cinema income - {income} lv.")
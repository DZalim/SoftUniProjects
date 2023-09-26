command = input()

cup_of_coffee = 0

while command != "END":
    if command.lower() == "coding" or command.lower() == "cat" or command.lower() == "dog" or command.lower() == "movie":
        if command.islower():
            cup_of_coffee += 1
        else:
            cup_of_coffee += 2
    command = input()

if cup_of_coffee > 5:
    print("You need extra sleep")
else:
    print(cup_of_coffee)

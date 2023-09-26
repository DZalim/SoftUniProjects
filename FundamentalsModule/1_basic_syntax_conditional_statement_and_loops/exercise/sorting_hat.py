command = input()

word_is_found = False

while command != "Welcome!":
    if command == "Voldemort":
        word_is_found = True
        print("You must not speak of that name!")
        break
    else:
        if len(command) < 5:
            print(f"{command} goes to Gryffindor.")
        elif len(command) == 5:
            print(f"{command} goes to Slytherin.")
        elif len(command) == 6:
            print(f"{command} goes to Ravenclaw.")
        else:
            print(f"{command} goes to Hufflepuff.")
    command = input()
if not word_is_found:
    print("Welcome to Hogwarts.")
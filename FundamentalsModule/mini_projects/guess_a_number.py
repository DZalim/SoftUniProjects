import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number 1-100: ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    else:
        player_number = int(player_input)

    if player_number == computer_number:
        print("You guess it!")
        break
    elif player_number < computer_number:
        print("Too Low!")
    else:
        print("Too High!")

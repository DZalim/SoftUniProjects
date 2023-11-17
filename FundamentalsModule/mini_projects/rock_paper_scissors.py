import random

from colorama import Fore

computer_points = 0
player_points = 0

name_input = input("What's your name? ")

while True:
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"

    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Try again...")

    computer_random_number = random.randint(1, 3)

    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print(Fore.BLUE + f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or\
            (player_move == scissors and computer_move == paper):
        player_points += 1
        print(Fore.GREEN + "You win!")
    elif computer_move == player_move:
        print(Fore.YELLOW + "Draw!")
    else:
        computer_points += 1
        print(Fore.RED + "You lose!")

    print(Fore.RESET + f"The results is: Computer - {computer_points}, {name_input} - {player_points}.")

    play_again_input = input("Type [yes] to play again or [no) to quit: ")
    if play_again_input == "no":
        print("Thank you for playing.")
        break
    elif play_again_input == "yes":
        continue
    else:
        raise SystemExit("Invalid input. Try again...")

if computer_points > player_points:
    print(f"The winner is Computer with {computer_points} points.")
elif player_points > computer_points:
    print(f"The winner is {name_input} with {player_points} points.")
else:
    print("The game ended in a draw.")

number_of_eggs_for_first_player = int(input())
number_of_eggs_for_second_player = int(input())

winner = input()
while winner != "End":
    if winner == "one":
        number_of_eggs_for_second_player -= 1
    elif winner == "two":
        number_of_eggs_for_first_player -= 1
    if number_of_eggs_for_first_player == 0 or number_of_eggs_for_second_player == 0:
        break
    winner = input()

if number_of_eggs_for_first_player == 0:
    print(f"Player one is out of eggs. Player two has {number_of_eggs_for_second_player} eggs left.")
elif number_of_eggs_for_second_player == 0:
    print(f"Player two is out of eggs. Player one has {number_of_eggs_for_first_player} eggs left.")
else:
    print(f"Player one has {number_of_eggs_for_first_player} eggs left.")
    print(f"Player two has {number_of_eggs_for_second_player} eggs left.")
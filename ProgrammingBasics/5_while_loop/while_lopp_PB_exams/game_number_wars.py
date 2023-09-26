name_of_first_player = input()
name_of_second_player = input()

points_of_first_player = 0
points_of_second_player = 0
is_number_wars = False

command = input()
while command != "End of game":
    first_player_card = int(command)
    second_player_card = int(input())
    if first_player_card > second_player_card:
        points_of_first_player += first_player_card - second_player_card
    elif second_player_card > first_player_card:
        points_of_second_player += second_player_card - first_player_card
    else:
        is_number_wars = True
        first_card = int(input())
        second_card = int(input())
        if first_card > second_card:
            winner = name_of_first_player
            winner_points = points_of_first_player
        elif second_card > first_card:
            winner = name_of_second_player
            winner_points = points_of_second_player
        break
    command = input()

if is_number_wars:
    print("Number wars!")
    print(f"{winner} is winner with {winner_points} points")
else:
    print(f"{name_of_first_player} has {points_of_first_player} points")
    print(f"{name_of_second_player} has {points_of_second_player} points")



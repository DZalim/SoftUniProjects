rows, cols = 6, 6

players = [player for player in input().split(', ')]

matrix = [input().split() for row in range(rows)]

player_rest = {
    0: False,
    1: False,
}


def check_position(player_one, player_two, position, rotate):
    if player_rest[rotate]:
        player_rest[rotate] = False
    else:
        if matrix[position[0]][position[1]] == 'T':
            print(f"{player_one} is out of the game! The winner is {player_two}.")
            exit()
        elif matrix[position[0]][position[1]] == 'E':
            print(f"{player_one} found the Exit and wins the game!")
            exit()
        elif matrix[position[0]][position[1]] == 'W':
            player_rest[rotate] = True
            print(f"{player_one} hits a wall and needs to rest.")


index = 0

while True:
    player_position_command = input()
    position_to_move = [int(player_position_command[1]), int(player_position_command[-2])]

    current_player = players[0] if index == 0 else players[-1]
    other_player = players[-1] if index == 0 else players[0]
    check_position(current_player, other_player, position_to_move, index)

    if index == 0:
        index = 1
    else:
        index = 0

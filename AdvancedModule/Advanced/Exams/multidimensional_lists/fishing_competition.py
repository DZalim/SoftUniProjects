rows = int(input())

matrix = []

current_position = []

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'right': [0, 1],
    'left': [0, -1],
}

fish_caught = 0

for row in range(rows):
    col = [el for el in input()]
    matrix.append(col)
    if 'S' in matrix[row]:
        col_position = matrix[row].index('S')
        current_position = [row, col_position]
        matrix[row][col_position] = '-'

command = input()
while command != "collect the nets":
    position_to_move = [current_position[0] + directions[command][0], current_position[1] + directions[command][1]]
    if 0 <= position_to_move[0] < rows and 0 <= position_to_move[1] < rows:
        current_position = position_to_move
    else:
        if position_to_move[0] < 0 or position_to_move[0] >= rows:
            if position_to_move[0] < 0:
                current_position[0] = rows - 1
            elif position_to_move[0] >= rows:
                current_position[0] = 0
        if position_to_move[1] < 0 or position_to_move[1] >= rows:
            if position_to_move[1] < 0:
                current_position[1] = rows - 1
            elif position_to_move[1] >= rows:
                current_position[1] = 0

    position = matrix[current_position[0]][current_position[1]]

    if position.isdigit():
        fish_caught += int(position)
        matrix[current_position[0]][current_position[1]] = '-'
    elif position == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{current_position[0]},{current_position[1]}]")
        break

    command = input()

else:
    matrix[current_position[0]][current_position[1]] = 'S'
    if fish_caught >= 20:
        print("Success! You managed to reach the quota!")
        print(f"Amount of fish caught: {fish_caught} tons.")
    else:
        difference = 20 - fish_caught
        print(f"You didn't catch enough fish and didn't reach the quota! You need {difference} tons of fish more.")
        if fish_caught > 0:
            print(f"Amount of fish caught: {fish_caught} tons.")
    [print(*row, sep="") for row in matrix]

rows = int(input())
commands = input().split(', ')
matrix = []

squirrel_position = []

for row in range(rows):
    current_col = [el for el in input()]
    matrix.append(current_col)
    if 's' in current_col:
        col_position = matrix[row].index('s')
        squirrel_position = [row, col_position]
        matrix[squirrel_position[0]][squirrel_position[1]] = '*'

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

collected_hazelnuts = 0

for command in commands:
    position_to_move = [squirrel_position[0] + directions[command][0], squirrel_position[1] + directions[command][1]]
    if 0 <= position_to_move[0] < rows and 0 <= position_to_move[1] < rows:
        position = matrix[position_to_move[0]][position_to_move[1]]
        if position == 't':
            print("Unfortunately, the squirrel stepped on a trap...")
            break
        elif position == 'h':
            collected_hazelnuts += 1
            matrix[position_to_move[0]][position_to_move[1]] = '*'
            if collected_hazelnuts >= 3:
                print("Good job! You have collected all hazelnuts!")
                break
        squirrel_position = position_to_move
    else:
        print("The squirrel is out of the field.")
        break
else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_hazelnuts}")

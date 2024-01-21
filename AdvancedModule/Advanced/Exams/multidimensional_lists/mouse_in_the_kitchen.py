rows, cols = [int(el) for el in input().split(',')]

matrix = []
mouse_position = []

for row in range(rows):
    current_col = [el for el in input()]
    matrix.append(current_col)
    if 'M' in current_col:
        col_position = matrix[row].index('M')
        mouse_position = [row, col_position]
        matrix[row][col_position] = '*'

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

command = input()

while command != "danger":
    position_to_move = [mouse_position[0] + directions[command][0], mouse_position[1] + directions[command][1]]
    if 0 <= position_to_move[0] < rows and 0 <= position_to_move[1] < cols:
        position = matrix[position_to_move[0]][position_to_move[1]]
        if 'C' in position:
            matrix[position_to_move[0]][position_to_move[1]] = '*'
            for row in matrix:
                if 'C' in row:
                    break
            else:
                matrix[position_to_move[0]][position_to_move[1]] = 'M'
                print("Happy mouse! All the cheese is eaten, good night!")
                break
        elif "@" in position:
            command = input()
            continue
        elif "T" in position:
            print("Mouse is trapped!")
            matrix[position_to_move[0]][position_to_move[1]] = 'M'
            break

        mouse_position = [position_to_move[0], position_to_move[1]]
    else:
        matrix[mouse_position[0]][mouse_position[1]] = 'M'
        print("No more cheese for tonight!")
        break

    command = input()
else:
    matrix[mouse_position[0]][mouse_position[1]] = 'M'
    print("Mouse will come back later!")

[print(*row, sep="") for row in matrix]

rows, cols = [int(el) for el in input().split()]

matrix = []

start_position = []

for row in range(rows):
    col = [el for el in input()]
    matrix.append(col)
    if 'B' in col:
        col_position = matrix[row].index('B')
        start_position = [row, col_position]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

current_position = start_position.copy()

while True:
    command = input()
    position_to_move = [current_position[0] + directions[command][0], current_position[1] + directions[command][1]]
    if 0 <= position_to_move[0] < rows and 0 <= position_to_move[1] < cols:
        position = matrix[position_to_move[0]][position_to_move[1]]
        if position == "*":
            continue
        elif position == "-":
            matrix[position_to_move[0]][position_to_move[1]] = '.'
        elif position == "P":
            matrix[position_to_move[0]][position_to_move[1]] = 'R'
            print("Pizza is collected. 10 minutes for delivery.")
        elif position == "A":
            matrix[position_to_move[0]][position_to_move[1]] = 'P'
            print("Pizza is delivered on time! Next order...")
            break

        current_position = position_to_move.copy()

    else:
        matrix[start_position[0]][start_position[1]] = ' '
        print("The delivery is late. Order is canceled.")
        break

[print(*row, sep='') for row in matrix]

initial_string = input()
matrix_row = int(input())

matrix = []
player_pos = []

for row in range(matrix_row):
    cur_col = [el for el in input()]
    matrix.append(cur_col)
    if 'P' in cur_col:
        col_pos = cur_col.index('P')
        player_pos = [row, col_pos]
        matrix[row][col_pos] = '-'

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

commands_count = int(input())

for command in range(commands_count):
    command = input()
    row_to_move = player_pos[0] + directions[command][0]
    col_to_move = player_pos[1] + directions[command][1]

    if 0 <= row_to_move < matrix_row and 0 <= col_to_move < matrix_row:
        position = matrix[row_to_move][col_to_move]
        if position.isalpha():
            initial_string += position
            matrix[row_to_move][col_to_move] = '-'
        player_pos = [row_to_move, col_to_move]

    else:
        if initial_string:
            initial_string = initial_string[:len(initial_string) - 1]

matrix[player_pos[0]][player_pos[1]] = 'P'

print(initial_string)
[print(*row, sep='') for row in matrix]

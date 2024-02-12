ROWS, COLS = 8, 8

matrix = []
queens_positions = []

for row in range(ROWS):
    current_col = input().split()
    matrix.append(current_col)
    for el_index in range(len(current_col)):
        if current_col[el_index] == 'Q':
            queens_positions.append([row, el_index])

danger_queens = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'up-left': (-1, -1),
    'up-right': (-1, 1),
    'down-left': (1, -1),
    'down-right': (1, 1),
}

for queen in queens_positions:
    current_row, current_col = queen
    for direction in directions.values():
        direction_row, direction_col = direction

        next_row, next_col = current_row + direction_row, current_col + direction_col

        while 0 <= next_row < ROWS and 0 <= next_col < COLS:
            if matrix[next_row][next_col] == 'Q':
                break
            if matrix[next_row][next_col] == 'K':
                danger_queens.append([current_row, current_col])
                break
            next_row, next_col = next_row + direction_row, next_col + direction_col


if danger_queens:
    [print(queen, sep='\n') for queen in danger_queens]
else:
    print("The king is safe!")

size_of_matrix = int(input()) #square
number_of_bombs = int(input())

matrix = [[0]*size_of_matrix for row in range(size_of_matrix)]

DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'up-left': (-1, -1),
    'up-right': (-1, 1),
    'down-left': (1, -1),
    'down-right': (1, 1),
}

for bomb in range(number_of_bombs):
    current_bomb = input()
    row, col = current_bomb.split(', ')
    bomb_row, bomb_col = int(row[1:]), int(col[:-1])
    matrix[bomb_row][bomb_col] = '*'

    for direction in DIRECTIONS.values():
        direction_row, direction_col = direction
        next_row, next_col = bomb_row + direction_row, bomb_col + direction_col

        if 0 <= next_row < size_of_matrix and 0 <= next_col < size_of_matrix:
            position = matrix[next_row][next_col]

            if isinstance(position, int):
                matrix[next_row][next_col] += 1

for row in matrix:
    print(*row, sep=' ')
print()


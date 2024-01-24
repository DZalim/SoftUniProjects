rows = int(input())

matrix = []
my_coordinates = []

for row in range(rows):
    cur_col = [int(el) if el.isdigit() else el for el in input().split()]
    matrix.append(cur_col)
    if 'P' in cur_col:
        col_pos = cur_col.index('P')
        my_coordinates = [[row, col_pos]]
        matrix[row][col_pos] = 0

collected_coins = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

while True:
    command = input()

    row_to_move = my_coordinates[-1][0] + directions[command][0]
    col_to_move = my_coordinates[-1][1] + directions[command][1]

    if command == 'up' or command == 'down':
        if not (0 <= row_to_move < rows):
            row_to_move = rows - 1 if row_to_move < 0 else 0
    else:
        if not (0 <= col_to_move < rows):
            col_to_move = rows - 1 if col_to_move < 0 else 0

    position = matrix[row_to_move][col_to_move]
    matrix[row_to_move][col_to_move] = 0
    my_coordinates.append([row_to_move, col_to_move])

    if position == 'X':
        collected_coins //= 2
        print(f"Game over! You've collected {collected_coins} coins.")
        break

    collected_coins += position

    if collected_coins >= 100:
        print(f"You won! You've collected {collected_coins} coins.")
        break

print("Your path:")
[print(row) for row in my_coordinates]

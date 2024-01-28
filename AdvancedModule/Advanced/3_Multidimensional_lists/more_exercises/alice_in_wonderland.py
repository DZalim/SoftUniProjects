rows = int(input())

matrix = []
alice_start_position = []

for row in range(rows):
    cur_col = input().split()
    matrix.append(cur_col)
    if 'A' in cur_col:
        col_pos = matrix[row].index('A')
        alice_start_position = [row, col_pos]
        matrix[row][col_pos] = '*'

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

collected_tea = 0

while True:
    command = input()

    next_row_move = alice_start_position[0] + directions[command][0]
    next_col_move = alice_start_position[1] + directions[command][1]

    if not (0 <= next_row_move < rows and 0 <= next_col_move < rows):
        print("Alice didn't make it to the tea party.")
        break

    current_position = matrix[next_row_move][next_col_move]
    matrix[next_row_move][next_col_move] = '*'
    alice_start_position = [next_row_move, next_col_move]

    if current_position == 'R':
        print("Alice didn't make it to the tea party.")
        break
    elif current_position.isdigit():
        collected_tea += int(current_position)

        if collected_tea >= 10:
            print("She did it! She went to the party.")
            break

[print(*row, sep=' ') for row in matrix]

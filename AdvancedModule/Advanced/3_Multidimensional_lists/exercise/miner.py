rows = int(input())
commands = input().split()

matrix = []
miner_position = []
total_coals = 0
collected_coals = 0

for row in range(rows):
    current_col = input().split()
    matrix.append(current_col)
    if 's' in current_col:
        col_pos = matrix[row].index('s')
        miner_position = [row, col_pos]
        matrix[row][col_pos] = '*'
    total_coals += matrix[row].count('c')

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],

}

for command in commands:
    row_to_move = miner_position[0] + directions[command][0]
    col_to_move = miner_position[1] + directions[command][1]

    if 0 <= row_to_move < rows and 0 <= col_to_move < rows:
        position_to_move = matrix[row_to_move][col_to_move]

        if position_to_move == 'e':
            print(f"Game over! ({row_to_move}, {col_to_move})")
            break
        elif position_to_move == 'c':
            collected_coals += 1

            if collected_coals == total_coals:
                print(f"You collected all coal! ({row_to_move}, {col_to_move})")
                break

        miner_position = [row_to_move, col_to_move]
        matrix[row_to_move][col_to_move] = '*'
else:
    print(f"{total_coals - collected_coals} pieces of coal left. ({row_to_move}, {col_to_move})")

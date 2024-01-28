rows, cols = 5, 5

matrix = []
player_position = []
total_targets = 0

for row in range(rows):
    cur_col = input().split()
    matrix.append(cur_col)
    if 'A' in cur_col:
        col_pos = matrix[row].index('A')
        matrix[row][col_pos] = '.'
        player_position = [row, col_pos]
    total_targets += matrix[row].count('x')

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

shoot_targets = []

for command in range(int(input())):
    current_command = input().split()
    command = current_command[0]
    position = current_command[1]

    if command == 'move':
        steps = int(current_command[2])
        row_to_move = player_position[0] + directions[position][0] * steps
        col_to_move = player_position[1] + directions[position][1] * steps

        if 0 <= row_to_move < rows and 0 <= col_to_move < cols:
            current_pos = matrix[row_to_move][col_to_move]
            if current_pos == '.':
                player_position = [row_to_move, col_to_move]

    elif command == 'shoot':

        current_position_to_shoot = player_position.copy()

        while True:

            row_to_shoot = current_position_to_shoot[0] + directions[position][0]
            col_to_shoot = current_position_to_shoot[1] + directions[position][1]

            if not (0 <= row_to_shoot < rows and 0 <= col_to_shoot < cols):
                break

            current_pos = matrix[row_to_shoot][col_to_shoot]

            if current_pos == 'x':
                shoot_targets.append([row_to_shoot, col_to_shoot])
                matrix[row_to_shoot][col_to_shoot] = '.'
                break

            current_position_to_shoot = [row_to_shoot, col_to_shoot]

    if len(shoot_targets) == total_targets:
        print(f"Training completed! All {total_targets} targets hit.")
        break
else:
    print(f"Training not completed! {total_targets - len(shoot_targets)} targets left.")

[print(row) for row in shoot_targets]

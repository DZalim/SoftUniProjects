def check_coordinates(direction, position):
    row = position[0] + directions[direction][0]
    col = position[1] + directions[direction][1]

    if not (0 <= row < rows and 0 <= col < cols):
        if not (0 <= row < rows):
            row = 0 if row >= rows else rows - 1
        elif not (0 <= col < cols):
            col = 0 if col >= cols else cols - 1

    return row, col


rows, cols = 6, 6

matrix = []

explorer_position = []

for row in range(rows):
    current_row = input().split()
    matrix.append(current_row)
    if 'E' in current_row:
        col = matrix[row].index('E')
        explorer_position = [row, col]

commands = input().split(', ')

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

collected_deposits = {
    'W': [0, 'Water'],
    'C': [0, 'Concrete'],
    'M': [0, 'Metal'],
}

for command in commands:

    row_to_move, col_to_move = check_coordinates(command, explorer_position)

    explorer_position = [row_to_move, col_to_move]
    position = matrix[row_to_move][col_to_move]
    matrix[row_to_move][col_to_move] = '-'

    if position in collected_deposits:
        collected_deposits[position][0] += 1
        print(f'{collected_deposits[position][1]} deposit found at ({row_to_move}, {col_to_move})')
    elif position == 'R':
        print(f"Rover got broken at ({row_to_move}, {col_to_move})")
        break

for deposit_value in collected_deposits.values():
    if deposit_value[0] < 1:
        print("Area not suitable to start the colony.")
        break
else:
    print("Area suitable to start the colony.")

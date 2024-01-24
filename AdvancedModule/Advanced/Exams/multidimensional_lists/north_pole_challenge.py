rows, cols = [int(x) for x in input().split(', ')]

matrix = []
santa_pos = []
total_items = 0


def check_collected_items(items):
    collected = 0
    for value in collected_items.values():
        collected += value[1]
    if collected == total_items:
        return True
    return False


def check_coordinates(direction):
    row = santa_pos[0] + directions[direction][0]
    col = santa_pos[1] + directions[direction][1]

    if direction == 'up' or direction == 'down':
        if not (0 <= row < rows):
            row = rows - 1 if row < 0 else 0
    elif direction == 'left' or direction == 'right':
        if not (0 <= col < cols):
            col = cols - 1 if col < 0 else 0
    return row, col


for row in range(rows):
    cur_col = input().split()
    matrix.append(cur_col)
    if 'Y' in cur_col:
        col_pos = matrix[row].index('Y')
        santa_pos = [row, col_pos]
        matrix[row][col_pos] = 'x'
    total_items += cur_col.count('D') + cur_col.count('G') + cur_col.count('C')

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

collected_items = {
    'D': ['Christmas decorations', 0],
    'G': ['Gifts', 0],
    'C': ['Cookies', 0],
}

command_info = input().split('-')
while command_info[0] != 'End':
    command, steps = command_info[0], int(command_info[1])

    move = 0
    while steps != move:

        current_row_step, current_col_step = check_coordinates(command)

        current_position = matrix[current_row_step][current_col_step]

        if current_position.isalpha() and current_position != 'x':
            collected_items[current_position][1] += 1

        matrix[current_row_step][current_col_step] = 'x'
        santa_pos = [current_row_step, current_col_step]

        collected_item = check_collected_items(collected_items)
        if collected_item:
            break

        move += 1

    if collected_item:
        break

    command_info = input().split('-')

matrix[santa_pos[0]][santa_pos[1]] = 'Y'

if collected_item:
    print("Merry Christmas!")

print("You've collected:")
for values in collected_items.values():
    print(f"- {values[1]} {values[0]}")

[print(*row) for row in matrix]

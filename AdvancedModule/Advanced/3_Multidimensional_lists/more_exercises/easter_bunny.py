rows = int(input())

matrix = []
bunny_pos = []

for row in range(rows):
    cur_col = input().split()
    matrix.append(cur_col)
    if "B" in cur_col:
        col_pos = matrix[row].index('B')
        bunny_pos = [row, col_pos]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

direction_with_max_sum = ''
all_positions = []
max_sum_of_collecting_eggs = float('-inf')

for direction, row_col in directions.items():
    row, col = bunny_pos[0] + row_col[0], bunny_pos[1] + row_col[1]
    all_steps = []
    collected_eggs = 0

    while 0 <= row < rows and 0 <= col < rows:

        current_pos = matrix[row][col]
        if current_pos == 'X':
            break
        collected_eggs += int(current_pos)
        all_steps.append([row, col])

        row += row_col[0]
        col += row_col[1]

    if collected_eggs >= max_sum_of_collecting_eggs:
        max_sum_of_collecting_eggs = collected_eggs
        all_positions = all_steps
        direction_with_max_sum = direction

print(direction_with_max_sum)
[print(step, sep='\n') for step in all_positions]
print(max_sum_of_collecting_eggs)

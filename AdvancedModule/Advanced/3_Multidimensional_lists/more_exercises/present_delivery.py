presents = int(input())
rows = int(input())

matrix = []
santa_pos = []
nice_kids = 0

for row in range(rows):
    cur_col = input().split()
    matrix.append(cur_col)
    if 'S' in cur_col:
        col = matrix[row].index('S')
        santa_pos = [row, col]
        matrix[row][col] = '-'
    nice_kids += cur_col.count('V')

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

total_gifts_given_for_nice_kids = 0

command = input()
while command != "Christmas morning":

    row_to_move = santa_pos[0] + directions[command][0]
    col_to_move = santa_pos[1] + directions[command][1]

    position = matrix[row_to_move][col_to_move]
    matrix[row_to_move][col_to_move] = '-'
    santa_pos = [row_to_move, col_to_move]

    if position == 'V':
        total_gifts_given_for_nice_kids += 1
        presents -= 1
    elif position == 'C':
        for direction, row_col in directions.items():
            new_row = santa_pos[0] + row_col[0]
            new_col = santa_pos[1] + row_col[1]

            pos = matrix[new_row][new_col]
            matrix[new_row][new_col] = '-'

            if pos == 'V':
                total_gifts_given_for_nice_kids += 1
                presents -= 1
            elif pos == 'X':
                presents -= 1

    if presents <= 0 or nice_kids == total_gifts_given_for_nice_kids:
        break

    command = input()

matrix[santa_pos[0]][santa_pos[1]] = 'S'

if presents <= 0 and total_gifts_given_for_nice_kids < nice_kids:
    print("Santa ran out of presents!")
[print(*row, sep=' ') for row in matrix]

if total_gifts_given_for_nice_kids == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - total_gifts_given_for_nice_kids} nice kid/s.")

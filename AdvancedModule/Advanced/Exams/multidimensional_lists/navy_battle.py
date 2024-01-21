rows = int(input())  # square matrix

matrix = []
submarine_position= []

for row in range(rows):
    current_col = [el for el in input()]
    matrix.append(current_col)
    if 'S' in current_col:
        col_position = matrix[row].index('S')
        submarine_position = [row, col_position]
        matrix[submarine_position[0]][submarine_position[1]] = '-'

damage = 0
reached_cruiser = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

while True:
    command = input()
    position_to_move = [submarine_position[0] + directions[command][0], submarine_position[1] + directions[command][1]]
    submarine_position = position_to_move
    if 0 <= position_to_move[0] <= rows and 0 <= position_to_move[1] <= rows:
        position = matrix[position_to_move[0]][position_to_move[1]]
        if position == '*':
            damage += 1
            if damage == 3:
                print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_position[0]}, {submarine_position[1]}]!")
                break
        elif position == 'C':
            reached_cruiser += 1
            if reached_cruiser == 3:
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                break
        matrix[position_to_move[0]][position_to_move[1]] = '-'

matrix[submarine_position[0]][submarine_position[1]] = 'S'

[print(*row, sep='') for row in matrix]

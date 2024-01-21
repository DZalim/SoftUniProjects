rows, cols = [int(x) for x in input().split()]

matrix = []
current_position = []

for row in range(rows):
    current_col = input().split()
    matrix.append(current_col)
    if 'B' in current_col:
        col_position = matrix[row].index('B')
        current_position = [row, col_position]
        matrix[current_position[0]][current_position[1]] = '-'

moves = 0
touched_opponents = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

command = input()
while command != "Finish":
    position_to_move = [current_position[0] + directions[command][0], current_position[1] + directions[command][1]]
    if 0 <= position_to_move[0] < rows and 0 <= position_to_move[1] < cols:
        position = matrix[position_to_move[0]][position_to_move[1]]
        if position == 'P':
            current_position = position_to_move
            matrix[position_to_move[0]][position_to_move[1]] = '-'
            touched_opponents += 1
            moves += 1
            if touched_opponents == 3:
                break
        elif position == '-':
            current_position = position_to_move
            moves += 1
    command = input()

print('Game over!')
print(f'Touched opponents: {touched_opponents} Moves made: {moves}')

size_of_matrix = int(input()) #square

matrix = []
snake_position = []
burrow_positions = []

for row in range(size_of_matrix):
    current_row = list(input())
    matrix.append(current_row)
    for el in range(len(current_row)):
        if current_row[el] == 'S':
            snake_position = [row, el]
            matrix[row][el] = '.'
        elif current_row[el] == 'B':
            burrow_positions.append([row, el])


DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

total_food = 0

while total_food < 10:
    command = input()
    next_row, next_col = snake_position[0] + DIRECTIONS[command][0], snake_position[1] + DIRECTIONS[command][1]

    if not (0 <= next_row < size_of_matrix and 0 <= next_col < size_of_matrix):
        print("Game over!")
        break

    snake_position = [next_row, next_col]
    symbol = matrix[next_row][next_col]
    matrix[next_row][next_col] = '.'

    if symbol == '*':
        total_food += 1
    elif symbol == 'B':
        for burrow in burrow_positions:
            if [next_row, next_col] != burrow:
                snake_position = [burrow[0], burrow[1]]
                matrix[burrow[0]][burrow[1]] = '.'
else:
    matrix[snake_position[0]][snake_position[1]] = 'S'
    print("You won! You fed the snake.")

print(f"Food eaten: {total_food}")
[print(*row, sep='') for row in matrix]

size_of_matrix = int(input()) #square

matrix = []
jetfighter_position = []

for row in range(size_of_matrix):
    current_row = list(input())
    matrix.append(current_row)
    if 'J' in current_row:
        col = current_row.index('J')
        jetfighter_position = [row, col]
        matrix[row][col] = '-'


DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


INITIAL_ARMOR_VALUE = 300
TOTAL_ENEMIES = 4

while True:
    command = input()
    next_row, next_col = jetfighter_position[0] + DIRECTIONS[command][0], jetfighter_position[1] + DIRECTIONS[command][1]
    symbol = matrix[next_row][next_col]
    matrix[next_row][next_col] = '-'
    jetfighter_position = [next_row, next_col]


    if symbol == 'R':
        INITIAL_ARMOR_VALUE = 300

    elif symbol == 'E':
        TOTAL_ENEMIES -= 1

        if TOTAL_ENEMIES == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            INITIAL_ARMOR_VALUE -= 100

            if INITIAL_ARMOR_VALUE == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!")
                break

matrix[next_row][next_col] = 'J'
[print(*row, sep='') for row in matrix]

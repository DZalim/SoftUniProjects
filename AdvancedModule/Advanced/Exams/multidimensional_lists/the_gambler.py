rows = int(input())

total_amount = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

benefits = {
    'W': 100,
    'P': -200,
    'J': 100000,
    '-': 0,
}

matrix = []
current_position = []
for row in range(rows):
    current_row = [el for el in input()]
    matrix.append(current_row)
    if "G" in current_row:
        col_position = current_row.index('G')
        current_position = [row, col_position]
        total_amount = 100
        matrix[row][col_position] = '-'

command = input()
while command != 'end':
    position_to_move = [current_position[0] + directions[command][0], current_position[1] + directions[command][1]]
    if 0 <= position_to_move[0] < rows and 0 <= position_to_move[1] < rows:
        current_position = position_to_move
        benefit = matrix[current_position[0]][current_position[1]]
        total_amount += benefits[benefit]
        matrix[current_position[0]][current_position[1]] = '-'

        if total_amount <= 0:
            print("Game over! You lost everything!")
            break
        elif benefit == 'J':
            matrix[current_position[0]][current_position[1]] = 'G'
            print("You win the Jackpot!")
            print(f"End of the game. Total amount: {total_amount}$")
            [print(*row, sep='') for row in matrix]
            break

    else:
        print("Game over! You lost everything!")
        break
    command = input()
else:
    matrix[current_position[0]][current_position[1]] = 'G'
    print(f"End of the game. Total amount: {total_amount}$")
    [print(*row, sep='') for row in matrix]

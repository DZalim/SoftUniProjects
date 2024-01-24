rows, cols = 8, 8

matrix = []

players = ['w', 'b']

players_move = {
    'w': [[-1, 1], [-1, -1], [-1, 0]],
    'b': [[1, -1], [1, 1], [1, 0]]
}

players_information = {
    'w': ['White', []],
    'b': ['Black', []]
}

for row in range(rows):
    cur_col = input().split()
    matrix.append(cur_col)
    if 'w' in cur_col:
        col_pos = matrix[row].index('w')
        players_information['w'][1] = [row, col_pos]
    elif 'b' in cur_col:
        col_pos = matrix[row].index('b')
        players_information['b'][1] = [row, col_pos]

auxiliary_matrix = []

for row in range(rows, 0, -1):
    current_col = []
    for col in range(97, 97 + cols):
        character = chr(col) + str(row)
        current_col.append(character)
    auxiliary_matrix.append(current_col)

counter = 0

while True:
    index = counter % 2
    player = players[index]

    current_position = players_information[player][1]

    for move in players_move[player]:

        new_row, new_col = current_position[0] + move[0], current_position[1] + move[1]

        if not (0 <= new_row < rows):
            pos = auxiliary_matrix[current_position[0]][current_position[1]]
            print(f"Game over! {players_information[player][0]} pawn is promoted to a queen at {pos}.")
            exit()

        if 0 <= new_col < cols:
            position = matrix[new_row][new_col]

            if position.isalpha():
                print(
                    f"Game over! {players_information[player][0]} win, capture on {auxiliary_matrix[new_row][new_col]}.")
                exit()

    matrix[current_position[0]][current_position[1]] = '-'
    matrix[new_row][new_col] = player
    players_information[player][1] = [new_row, new_col]

    counter += 1

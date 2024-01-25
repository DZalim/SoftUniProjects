rows = int(input())

matrix = [list(input()) for row in range(rows)]
knight_positions = []
total_attacks = 0


for row in range(rows):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 'K':
            knight_positions.append([row, col])

directions = [
    [-2, -1],
    [-1, -2],
    [-2, 1],
    [-1, 2],
    [2, -1],
    [1, -2],
    [2, 1],
    [1, 2]
]

while True:
    max_attacks = 0
    knight_with_max_attacks = []

    for knight in knight_positions:
        knight_attacks = 0
        for direction in directions:
            row = knight[0] + direction[0]
            col = knight[1] + direction[1]

            if 0 <= row < rows and 0 <= col < rows:
                position = matrix[row][col]
                if position == 'K':
                    knight_attacks += 1

        if knight_attacks > max_attacks:
            max_attacks = knight_attacks
            knight_with_max_attacks = [knight[0], knight[1]]


    if knight_with_max_attacks:
        total_attacks += 1
        matrix[knight_with_max_attacks[0]][knight_with_max_attacks[1]] = 0
        for removed_knight in knight_positions:
            if removed_knight == knight_with_max_attacks:
                knight_positions.remove(removed_knight)
    else:
        break


print(total_attacks)

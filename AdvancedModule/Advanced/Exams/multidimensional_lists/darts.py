rows, cols = 7, 7

players = input().split(', ')

player_hit_and_points = {
    players[0]: [501, 0],
    players[1]: [501, 0],
}

matrix = [[int(el) if el.isdigit() else el for el in input().split()] for row in range(rows)]

counter = 0
while True:
    command = input().split(', ')
    row = int(command[0][1:])
    col = int(command[1][:len(command[1]) - 1])

    index = counter % 2
    player = players[index]
    player_hit_and_points[player][1] += 1

    if 0 <= row < rows and 0 <= col <= cols:
        current_hit = matrix[row][col]
        if isinstance(current_hit, int):
            player_hit_and_points[player][0] -= current_hit
        elif current_hit == "D":
            total_points = (matrix[row][0] + matrix[row][cols - 1] + matrix[0][col] + matrix[rows - 1][col]) * 2
            player_hit_and_points[player][0] -= total_points
        elif current_hit == "T":
            total_points = (matrix[row][0] + matrix[row][cols - 1] + matrix[0][col] + matrix[rows - 1][col]) * 3
            player_hit_and_points[player][0] -= total_points
        else:
            print(f"{player} won the game with {player_hit_and_points[player][1]} throws!")
            break

    if player_hit_and_points[player][0] <= 0:
        print(f"{player} won the game with {player_hit_and_points[player][1]} throws!")
        break

    counter += 1

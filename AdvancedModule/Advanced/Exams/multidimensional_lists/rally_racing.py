rows = int(input())  # square matrix
racing_number = input()

car_position = [0, 0]
matrix = [input().split() for row in range(rows)]

distance = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

command = input()
while command != "End":
    position_to_move = [car_position[0] + directions[command][0], car_position[1] + directions[command][1]]
    car_position = position_to_move
    position = matrix[car_position[0]][car_position[1]]
    if position == '.':
        distance += 10
    elif position == 'F':
        distance += 10
        print(f"Racing car {racing_number} finished the stage!")
        break
    else:
        distance += 30
        for row in range(car_position[0], rows):
            if 'T' in matrix[row]:
                col_position = matrix[row].index('T')
                matrix[row][col_position] = '.'
                car_position = [row, col_position]
    command = input()
else:
    print(f"Racing car {racing_number} DNF.")

matrix[car_position[0]][car_position[1]] = 'C'
print(f"Distance covered {distance} km.")
[print(*row, sep='') for row in matrix]

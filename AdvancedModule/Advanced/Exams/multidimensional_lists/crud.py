rows, cols = 6, 6
matrix = [input().split() for row in range(rows)]
position_info = input()
current_position = [int(position_info[1]), int(position_info[-2])]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'right': [0, 1],
    'left': [0, -1]
}

command_data = input().split(', ')
while 'Stop' not in command_data:
    command, direction = command_data[0], command_data[1]
    command_position = [current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]]
    current_position = command_position
    if command == 'Create':
        to_create = command_data[2]
        if matrix[command_position[0]][command_position[1]] == '.':
            matrix[command_position[0]][command_position[1]] = to_create
    elif command == 'Update':
        to_update = command_data[2]
        if matrix[command_position[0]][command_position[1]] != '.':
            matrix[command_position[0]][command_position[1]] = to_update
    elif command == 'Delete':
        matrix[command_position[0]][command_position[1]] = '.'
    elif command == 'Read':
        if matrix[command_position[0]][command_position[1]] != '.':
            print(matrix[command_position[0]][command_position[1]])
    command_data = input().split(', ')

[print(*row) for row in matrix]

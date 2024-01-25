rows = int(input())
matrix = [[int(el) for el in input().split()] for row in range(rows)]

command_info = input().split()
while command_info[0] != "END":
    command = command_info[0]
    row = int(command_info[1])
    col = int(command_info[2])
    value = int(command_info[3])

    if 0 <= row < rows and 0 <= col < rows:
        if command == 'Add':
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

    command_info = input().split()

[print(*row) for row in matrix]

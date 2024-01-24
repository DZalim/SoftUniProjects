rows, cols = [int(el) for el in input().split()]

matrix = [input().split() for row in range(rows)]

command_info = input().split()

while command_info[0] != 'END':

    if len(command_info) == 5:
        command = command_info[0]
        row_one = int(command_info[1])
        col_one = int(command_info[2])
        row_two = int(command_info[3])
        col_two = int(command_info[4])

        if command == 'swap' and 0 <= row_one <= rows and 0 <= col_one < cols and 0 <= row_two < rows and 0 <= col_two < cols:
            matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
            for row in matrix:
                print(' '.join(row))
        else:
            print('Invalid input!')

    else:
        print('Invalid input!')

    command_info = input().split()

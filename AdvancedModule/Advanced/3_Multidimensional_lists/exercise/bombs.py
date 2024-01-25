rows = int(input())
matrix = [[int(el) for el in input().split()] for row in range(rows)]

explode_coordinates = [[int(el) for el in row.split(',')] for row in input().split()]

for coordinate in explode_coordinates:
    number_row = coordinate[0]
    number_col = coordinate[1]
    number_to_explode = matrix[number_row][number_col]

    if number_to_explode <= 0:
        continue

    for row in range(number_row - 1, number_row + 2):
        for col in range(number_col - 1, number_col + 2):
            if 0 <= row < rows and 0 <= col < rows:
                if matrix[row][col] > 0:
                    matrix[row][col] -= number_to_explode

alive_cells = 0
sum_of_alive_cells = 0

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] > 0:
            alive_cells += 1
            sum_of_alive_cells += matrix[row][col]

print(f'Alive cells: {alive_cells}')
print(f'Sum: {sum_of_alive_cells}')

[print(*row, sep=' ') for row in matrix]

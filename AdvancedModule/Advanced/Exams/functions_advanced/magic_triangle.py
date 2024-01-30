def get_magic_triangle(count):
    matrix = [[1], [1, 1]]

    for row in range(2, count):
        matrix.append([])
        for col in range(0, row + 1):
            if col == 0 or col == row:
                matrix[row].append(1)
            else:
                first_number = matrix[row - 1][col - 1]
                second_number = matrix[row - 1][col]
                matrix[row].append(first_number + second_number)

    return matrix


print(get_magic_triangle(5))

rows, cols = [int(x) for x in input().split()]

matrix = [[int(item) for item in input().split()] for row in range(rows)]

max_sum = float('-inf')
submatrix = []

for row in range(rows - 2):
    for col in range(cols - 2):

        first_row = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2]
        second_row = matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2]
        third_row = matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

        sum_rows = first_row + second_row + third_row

        if sum_rows > max_sum:
            max_sum = sum_rows
            submatrix = [
                [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
            ]

print(f"Sum = {max_sum}")
print(*submatrix[0])
print(*submatrix[1])
print(*submatrix[2])

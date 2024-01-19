rows, cols = [int(x) for x in input().split(', ')]

matrix = [[int(item) for item in input().split(', ')] for row in range(rows)]

max_number = float('-inf')
find_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        first_number = matrix[row][col]
        next_number = matrix[row][col + 1]
        under_number = matrix[row + 1][col]
        diagonal_number = matrix[row + 1][col + 1]

        sum_of_elements = first_number + next_number + under_number + diagonal_number

        if sum_of_elements > max_number:
            max_number = sum_of_elements
            find_matrix = [[first_number, next_number], [under_number, diagonal_number]]

print(*find_matrix[0])
print(*find_matrix[1])
print(max_number)

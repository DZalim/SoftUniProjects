rows, cols = [int(x) for x in input().split(', ')]

matrix = [[int(item) for item in input().split()] for row in range(rows)]

for col in range(cols):
    sum_of_columns = 0
    for row in range(rows):
        sum_of_columns += matrix[row][col]
    print(sum_of_columns)

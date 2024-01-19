matrix = [[int(item) for item in input().split()] for row in range(int(input()))]

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if row == col:
            primary_diagonal_sum += matrix[row][col]
        if (row + col) == len(matrix) - 1:
            secondary_diagonal_sum += matrix[row][col]

difference = primary_diagonal_sum - secondary_diagonal_sum

print(abs(difference))

matrix = [[int(item) for item in input().split(', ')] for row in range(int(input()))]

primary_diagonal = []
primary_diagonal_sum = 0

secondary_diagonal = []
secondary_diagonal_sum = 0


for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if row == col:
            primary_diagonal.append(matrix[row][col])
            primary_diagonal_sum += matrix[row][col]
        if (row + col) == len(matrix) - 1:
            secondary_diagonal.append(matrix[row][col])
            secondary_diagonal_sum += matrix[row][col]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {primary_diagonal_sum}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {secondary_diagonal_sum}")

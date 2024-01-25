matrix = [row.split() for row in input().split("|")]

for row in range(len(matrix) - 1, -1, -1):
    for col in range(len(matrix[row])):
        print(matrix[row][col], sep=' ', end=' ')

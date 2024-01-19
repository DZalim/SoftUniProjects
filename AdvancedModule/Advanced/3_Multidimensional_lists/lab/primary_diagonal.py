matrix = [[int(item) for item in input().split()] for row in range(int(input()))]

diagonal_sum = 0

for row in range(len(matrix)):
    diagonal_sum += matrix[row][row]

print(diagonal_sum)

rows, cols = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for row in range(rows)]

total_sum = [sum(row) for row in matrix]

print(sum(total_sum))
print(matrix)

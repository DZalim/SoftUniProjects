rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for row in range(rows)]

flattening_matrix = [item for row in matrix for item in row]

print(flattening_matrix)

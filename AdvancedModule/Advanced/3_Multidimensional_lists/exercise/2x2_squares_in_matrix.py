rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for row in range(rows)]

matches = 0

for row in range(rows - 1):
    for col in range(cols - 1):

        letter = matrix[row][col]
        next_letter = matrix[row][col + 1]
        under_letter = matrix[row + 1][col]
        diagonal_letter = matrix[row + 1][col + 1]

        if letter == next_letter == under_letter == diagonal_letter:
            matches += 1

print(matches)

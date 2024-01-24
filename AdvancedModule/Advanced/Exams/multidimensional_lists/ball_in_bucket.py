rows, cols = 6, 6

matrix = [[int(el) if el.isdigit() else el for el in input().split()] for row in range(rows)]

total_sum = 0

for hit_coordinate in range(3):
    coordinate = input().split(', ')
    coordinate_to_hit = [int(coordinate[0][1:]), int(coordinate[1][0:len(coordinate[1]) - 1])]

    row, col = coordinate_to_hit[0], coordinate_to_hit[1]

    if 0 <= row < rows and 0 <= col <= cols:
        position = matrix[row][col]

        if position == 'B':
            matrix[row][col] = 0
            column_sum = 0
            for sum_row in range(rows):
                column_sum += matrix[sum_row][col]
            total_sum += column_sum

if total_sum < 100:
    print(f"Sorry! You need {100 - total_sum} points more to win a prize.")
elif 100 <= total_sum < 200:
    print(f"Good job! You scored {total_sum} points, and you've won Football.")
elif 200 <= total_sum < 300:
    print(f"Good job! You scored {total_sum} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {total_sum} points, and you've won Lego Construction Set.")

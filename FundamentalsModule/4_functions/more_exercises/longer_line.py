import math


def first_pair_line(point_x1, point_y1, point_x2, point_y2):
    first_line = abs(point_x1) + abs(point_y1)
    second_line = abs(point_x2) + abs(point_y2)
    if first_line > second_line:
        return f"({math.floor(point_x2)}, {math.floor(point_y2)})({math.floor(point_x1)}, {math.floor(point_y1)})"
    return f"({math.floor(point_x1)}, {math.floor(point_y1)})({math.floor(point_x2)}, {math.floor(point_y2)})"


def second_pair_line(point_x3, point_y3, point_x4, point_y4):
    first_line = abs(point_x3) + abs(point_y3)
    second_line = abs(point_x4) + abs(point_y4)
    if first_line > second_line:
        return f"({math.floor(point_x4)}, {math.floor(point_y4)})({math.floor(point_x3)}, {math.floor(point_y3)})"
    return f"({math.floor(point_x3)}, {math.floor(point_y3)})({math.floor(point_x4)}, {math.floor(point_y4)})"


def find_the_longer_line(point_x1, point_y1, point_x2, point_y2, point_x3, point_y3, point_x4, point_y4):
    first_sum_of_all_points = abs(point_x1) + abs(point_y1) + abs(point_x2) + abs(point_y2)
    second_sum_of_all_points = abs(point_x3) + abs(point_y3) + abs(point_x4) + abs(point_y4)
    if first_sum_of_all_points > second_sum_of_all_points:
        return first_pair_line(x1, y1, x2, y2)
    return second_pair_line(x3, y3, x4, y4)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

returned_result = find_the_longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
print(returned_result)

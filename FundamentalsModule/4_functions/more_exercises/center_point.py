import math


def find_the_center_point(point_x1, point_y1, point_x2, point_y2):
    point_line_1 = abs(point_x1) + abs(point_y1)
    point_line_2 = abs(point_x2) + abs(point_y2)
    if point_line_1 > point_line_2:
        return f"({math.floor(point_x2)}, {math.floor(point_y2)})"
    return f"({math.floor(point_x1)}, {math.floor(point_y1)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

returned_result = find_the_center_point(x1, y1, x2, y2)
print(returned_result)
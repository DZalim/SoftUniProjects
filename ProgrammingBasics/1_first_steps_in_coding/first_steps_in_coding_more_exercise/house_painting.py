x = float(input())
y = float(input())
h = float(input())

green_paint = 3.4
red_paint = 4.3
door_width = 1.2
door_height = 2
window_widht_and_height = 1.5

front_and_back_wall_without_door = x * x - door_width * door_height + x * x
side_walls = 2 * (x * y) - 2 * (window_widht_and_height * window_widht_and_height)
walls = front_and_back_wall_without_door + side_walls

roof_rectangle = 2 * (x * y)
roof_triangle = 2 * ((x * h)/2)
roof = roof_triangle + roof_rectangle

paint_for_walls = walls / green_paint
paint_for_roof = roof / red_paint

print (f"{paint_for_walls:.2f}")
print (f"{paint_for_roof:.2f}")


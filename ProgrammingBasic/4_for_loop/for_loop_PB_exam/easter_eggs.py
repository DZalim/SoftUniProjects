number_of_painted_eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0
max_eggs = 0
max_paint = ""

for eggs in range (number_of_painted_eggs):
    color_of_egg = input()
    if color_of_egg == "red":
        red += 1
    elif color_of_egg == "orange":
        orange += 1
    elif color_of_egg == "blue":
        blue += 1
    elif color_of_egg == "green":
        green += 1

if red > orange and red > blue and red > green:
    max_paint = "red"
    max_eggs = red
elif orange > red and orange > blue and orange > green:
    max_paint = "orange"
    max_eggs = orange
elif blue > red and blue > orange and blue > green:
    max_paint = "blue"
    max_eggs = blue
elif green > red and green > orange and green > blue:
    max_paint = "green"
    max_eggs = green

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {max_paint}")

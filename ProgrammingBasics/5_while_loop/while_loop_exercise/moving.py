width = int(input())
length = int(input())
height = int(input())

volume = width * length * height
boxes = 0

command = input()
while command != "Done":
    boxes += int(command)
    if volume < boxes:
        break
    command = input()

diff = abs(volume - boxes)
if volume < boxes:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")


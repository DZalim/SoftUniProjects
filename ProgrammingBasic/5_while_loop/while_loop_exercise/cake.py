width = int(input())
length = int(input())

pieces = width * length
taken_pieces = 0

command = input()
while command != "STOP":
    taken_pieces += int(command)
    if taken_pieces > pieces:
        break
    command = input()

diff = abs(pieces - taken_pieces)

if taken_pieces > pieces:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")


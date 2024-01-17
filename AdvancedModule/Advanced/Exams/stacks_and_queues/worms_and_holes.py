from collections import deque

worms = deque(int(worm) for worm in input().split())  # stack
holes = deque(int(hole) for hole in input().split())  # queue

start_worms_length = len(worms)
start_holes_length = len(holes)

matches = 0

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_worm <= 0:
        holes.appendleft(current_hole)
        continue

    if current_worm > current_hole or current_worm < current_hole:
        reduced_worm = current_worm - 3
        worms.append(reduced_worm)
    else:
        matches += 1

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and start_worms_length == matches:
    print("Every worm found a suitable hole!")
elif not worms and start_worms_length > matches:
    print("Worms left: none")
elif worms:
    print(f"Worms left:", end=' ')
    print(*worms, sep=', ')

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left:", end=' ')
    print(*holes, sep=', ')

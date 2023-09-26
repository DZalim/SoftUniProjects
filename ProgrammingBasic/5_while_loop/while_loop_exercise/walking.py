walked_steps = 0

while walked_steps <= 10000:
    command = input()
    if command == "Going home":
        steps = int(input())
        walked_steps += steps
        break
    steps = int(command)
    walked_steps += steps

diff = abs(10000-walked_steps)
if walked_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")


from collections import deque

children = deque(input().split())
n_toss = int(input()) - 1

while len(children) > 1:
    children.rotate(-n_toss)
    remove_kid = children.popleft()
    print(f"Removed {remove_kid}")

print(f"Last is {children.popleft()}")

from collections import deque

queue = deque()

while True:
    command = input()
    if command == "Paid":
        while queue:
            print(queue.popleft())
    elif command == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(command)

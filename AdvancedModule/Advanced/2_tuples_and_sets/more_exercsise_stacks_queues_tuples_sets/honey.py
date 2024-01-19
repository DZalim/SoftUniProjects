from collections import deque

working_bees = deque(int(x) for x in input().split())  # queue
nectar = [int(x) for x in input().split()]  # stack
symbols = deque(input().split())

total_honey_made = 0

while working_bees and nectar:
    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()

    if last_nectar >= first_bee:
        symbol = symbols.popleft()
        if last_nectar == 0 and symbol == '/':
            continue
        total_honey_made += abs(eval(f'{first_bee}{symbol}{last_nectar}'))
    else:
        working_bees.appendleft(first_bee)

print(f"Total honey made: {total_honey_made}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")

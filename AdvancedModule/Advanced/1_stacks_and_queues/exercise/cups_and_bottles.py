from collections import deque

cups = deque([int(cup) for cup in input().split()])  # queue
bottles = deque([int(bottle) for bottle in input().split()])  # stack

wasted_litres = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_cup > current_bottle:
        cups.appendleft(current_cup - current_bottle)
    else:
        wasted_litres += current_bottle - current_cup

bottles.reverse()

if not cups:
    print(f'Bottles:', *bottles)
if not bottles:
    print(f'Cups:', *cups)

print(f"Wasted litters of water: {wasted_litres}")

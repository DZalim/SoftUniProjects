from collections import deque

chocolates = [int(x) for x in input().split(', ')]  # stack
cups_of_milk = deque(int(x) for x in input().split(', '))  # queue

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    last_chocolate = chocolates.pop()
    first_cup = cups_of_milk.popleft()

    if last_chocolate <= 0 or first_cup <= 0:
        if last_chocolate > 0 and first_cup <= 0:
            chocolates.append(last_chocolate)
        if last_chocolate <= 0 and first_cup > 0:
            cups_of_milk.appendleft(first_cup)
        continue

    if last_chocolate != first_cup:
        cups_of_milk.append(first_cup)
        chocolates.append(last_chocolate - 5)
    else:
        milkshakes += 1

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")

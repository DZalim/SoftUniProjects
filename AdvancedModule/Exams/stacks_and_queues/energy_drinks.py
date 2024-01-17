from collections import deque

milligrams_of_caffeine = deque(int(caffeine) for caffeine in input().split(', '))  # stack
energy_drinks = deque(int(drink) for drink in input().split(', '))  # queue

initial_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    daily_caffeine = milligrams_of_caffeine.pop()
    daily_energy = energy_drinks.popleft()

    result = daily_energy * daily_caffeine

    if result + initial_caffeine <= 300:
        initial_caffeine += result

    else:
        energy_drinks.append(daily_energy)
        initial_caffeine -= 30
        if initial_caffeine < 0:
            initial_caffeine = 0

if energy_drinks:
    print('Drinks left:', end=' ')
    print(*energy_drinks, sep=', ')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {initial_caffeine} mg caffeine.")

from collections import deque

firework_effects = deque(int(x) for x in input().split(', ')) #queue
explosive_power = [int(x) for x in input().split(', ')] #stack

created_fireworks = {'Palm Fireworks': 0,
                     'Willow Fireworks': 0,
                     'Crossette Fireworks': 0}

while firework_effects and explosive_power:
    first_firework = firework_effects.popleft()
    last_explosive = explosive_power.pop()

    if first_firework <= 0 or last_explosive <= 0:
        if first_firework <= 0:
            explosive_power.append(last_explosive)
        if last_explosive <= 0:
            firework_effects.appendleft(first_firework)
        continue

    result = first_firework + last_explosive

    if result % 3 == 0 and result % 5 != 0:
        created_fireworks['Palm Fireworks'] += 1
    elif result % 5 == 0 and result % 3 != 0:
        created_fireworks['Willow Fireworks'] += 1
    elif result % 5 == 0 and result % 3 == 0:
        created_fireworks['Crossette Fireworks'] += 1
    else:
        firework_effects.append(first_firework-1)
        explosive_power.append(last_explosive)

    if created_fireworks['Palm Fireworks'] >= 3 and created_fireworks['Willow Fireworks'] >= 3 \
        and created_fireworks['Crossette Fireworks'] >= 3:
        break

if  created_fireworks['Palm Fireworks'] >= 3 and created_fireworks['Willow Fireworks'] >= 3 \
        and created_fireworks['Crossette Fireworks'] >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

for key, value in created_fireworks.items():
    print(f"{key}: {value}")

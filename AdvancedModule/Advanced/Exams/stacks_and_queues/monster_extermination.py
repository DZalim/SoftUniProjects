from collections import deque

armor_of_the_monsters = deque(int(monster) for monster in input().split(','))  # queue
soldiers_stricking_impact = deque(int(impact) for impact in input().split(','))  # stack

monsters_len = len(armor_of_the_monsters)

killed_monsters = 0

while armor_of_the_monsters and soldiers_stricking_impact:
    first_armor_value = armor_of_the_monsters.popleft()
    last_strike_strenght_value = soldiers_stricking_impact.pop()

    if last_strike_strenght_value >= first_armor_value:
        strike_value_to_add = last_strike_strenght_value - first_armor_value
        if soldiers_stricking_impact:
            soldiers_stricking_impact[-1] += strike_value_to_add
        else:
            if strike_value_to_add > 0:
                soldiers_stricking_impact.append(strike_value_to_add)
        killed_monsters += 1
    else:
        monster_value_to_add = first_armor_value - last_strike_strenght_value
        armor_of_the_monsters.append(monster_value_to_add)

    if killed_monsters == monsters_len:
        print("All monsters have been killed!")
    if not soldiers_stricking_impact:
        print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")

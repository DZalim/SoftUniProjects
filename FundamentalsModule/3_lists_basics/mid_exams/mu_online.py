dungeons_rooms = input().split("|")

initial_health = 100
initial_bitcoin = 0
total_rooms = 0
is_died = False

for room in dungeons_rooms:
    command = room.split()
    name_of_command = command[0]
    health_or_bitcoin = int(command[1])
    total_rooms += 1
    if name_of_command == "potion":
        if initial_health + health_or_bitcoin > 100:
            health_or_bitcoin = 100 - initial_health
        initial_health += health_or_bitcoin
        print(f"You healed for {health_or_bitcoin} hp.")
        print(f"Current health: {initial_health} hp.")
    elif name_of_command == "chest":
        initial_bitcoin += health_or_bitcoin
        print(f"You found {health_or_bitcoin} bitcoins.")
    else:
        if initial_health > health_or_bitcoin:
            initial_health -= health_or_bitcoin
            print(f"You slayed {name_of_command}.")
        else:
            print(f"You died! Killed by {name_of_command}.")
            print(f"Best room: {total_rooms}")
            is_died = True
            break

if not is_died:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoin}")
    print(f"Health: {initial_health}")

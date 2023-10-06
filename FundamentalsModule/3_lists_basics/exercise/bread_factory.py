working_day_events = input().split("|")

starting_coins = 100
starting_energy = 100

bread_factory_is_open = True

for event in working_day_events:
    current_event = event.split("-")
    name_of_event = current_event[0]
    coins_or_energy = int(current_event[1])
    if name_of_event == "rest":
        if starting_energy + coins_or_energy >= 100:
            coins_or_energy = 100 - starting_energy
        starting_energy += coins_or_energy
        print(f"You gained {coins_or_energy} energy.")
        print(f"Current energy: {starting_energy}.")
    elif name_of_event == "order":
        if starting_energy >= 30:
            starting_coins += coins_or_energy
            starting_energy -= 30
            print(f"You earned {coins_or_energy} coins.")
        else:
            starting_energy += 50
            print("You had to rest!")
    else:
        if starting_coins >= coins_or_energy:
            print(f"You bought {name_of_event}.")
            starting_coins -= coins_or_energy
        else:
            print(f"Closed! Cannot afford {name_of_event}.")
            bread_factory_is_open = False
            break

if bread_factory_is_open:
    print("Day completed!")
    print(f"Coins: {starting_coins}")
    print(f"Energy: {starting_energy}")

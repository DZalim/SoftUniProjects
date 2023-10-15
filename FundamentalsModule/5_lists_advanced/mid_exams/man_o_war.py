status_of_pirate_ship = [int(ship) for ship in input().split(">")]
status_warship = [int(warship) for warship in input().split(">")]
max_health_capacity = int(input())

won_enemy = False
lose = False

command = input()
while command != "Retire":
    split_command = command.split()
    action = split_command[0]
    if action == "Fire":
        index = int(split_command[1])
        damage = int(split_command[2])
        if 0 <= index < len(status_warship):
            status_warship[index] -= damage
            if status_warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                won_enemy = True
                break
    elif action == "Defend":
        start_index = int(split_command[1])
        end_index = int(split_command[2])
        damage = int(split_command[3])
        if 0 <= start_index < end_index < len(status_of_pirate_ship):
            for attack in range(start_index, end_index + 1):
                status_of_pirate_ship[attack] -= damage
                if status_of_pirate_ship[attack] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    lose = True
                    break
    elif action == "Repair":
        index = int(split_command[1])
        health = int(split_command[2])
        if 0 <= index < len(status_of_pirate_ship):
            if status_of_pirate_ship[index] + health > max_health_capacity:
                health = max_health_capacity - status_of_pirate_ship[index]
            status_of_pirate_ship[index] += health
    elif action == "Status":
        sections_to_repair = len([section for section in status_of_pirate_ship if section/max_health_capacity < 0.20])
        print(f"{sections_to_repair} sections need repair.")

    command = input()

if not won_enemy and not lose:
    print(f"Pirate ship status: {sum(status_of_pirate_ship)}")
    print(f"Warship status: {sum(status_warship)}")

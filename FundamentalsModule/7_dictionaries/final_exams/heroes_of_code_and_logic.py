number_of_heroes = int(input())

my_dict_with_heroes = {}

for hero in range(number_of_heroes):
    name_of_hero, hit_points, mana_points = input().split()
    my_dict_with_heroes[name_of_hero] = [0, 0]
    if my_dict_with_heroes[name_of_hero][0] > 100:
        hit_points = 100 - my_dict_with_heroes[name_of_hero][0]
    if my_dict_with_heroes[name_of_hero][1] > 200:
        mana_points = 200 - my_dict_with_heroes[name_of_hero][1]
    my_dict_with_heroes[name_of_hero][0] += int(hit_points)
    my_dict_with_heroes[name_of_hero][1] += int(mana_points)

command = input()
while command != "End":
    split_command = command.split(" - ")
    action = split_command[0]
    hero_name = split_command[1]
    if action == "CastSpell":
        needed_mana_points, spell_name = int(split_command[2]), split_command[3]
        if my_dict_with_heroes[hero_name][1] >= needed_mana_points:
            my_dict_with_heroes[hero_name][1] -= needed_mana_points
            print(f"{hero_name} has successfully cast {spell_name} and now has {my_dict_with_heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        damage, attacker = int(split_command[2]), split_command[3]
        my_dict_with_heroes[hero_name][0] -= damage
        if my_dict_with_heroes[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {my_dict_with_heroes[hero_name][0]} HP left!")
        else:
            del my_dict_with_heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif action == "Recharge":
        amount_to_recharge = int(split_command[2])
        if my_dict_with_heroes[hero_name][1] + amount_to_recharge > 200:
            amount_to_recharge = 200 - my_dict_with_heroes[hero_name][1]
        my_dict_with_heroes[hero_name][1] += amount_to_recharge
        print(f"{hero_name} recharged for {amount_to_recharge} MP!")
    elif action == "Heal":
        amount_to_heal = int(split_command[2])
        if my_dict_with_heroes[hero_name][0] + amount_to_heal > 100:
            amount_to_heal = 100 - my_dict_with_heroes[hero_name][0]
        my_dict_with_heroes[hero_name][0] += amount_to_heal
        print(f"{hero_name} healed for {amount_to_heal} HP!")
    command = input()

for hero, hero_values in my_dict_with_heroes.items():
    print(hero)
    print(f"HP: {hero_values[0]}")
    print(f"MP: {hero_values[1]}")

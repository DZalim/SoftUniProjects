current_list = input()

current_list_in_list = current_list.split(", ")

position_wolf = current_list_in_list.index("wolf")

if position_wolf + 1 == len(current_list_in_list):
    print(f"Please go away and stop eating my sheep")
else:
    position_sheep = len(current_list_in_list) - position_wolf - 1
    print(f"Oi! Sheep number {position_sheep}! You are about to be eaten by a wolf!")


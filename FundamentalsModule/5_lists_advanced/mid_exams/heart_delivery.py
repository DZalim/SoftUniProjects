size_of_neighborhood = [int(neighborhood) for neighborhood in input().split("@")]

current_index_of_cupid = 0
command = input()
while command != "Love!":
    split_command = command.split()
    step_to_jump = int(split_command[1])
    index_to_jump = current_index_of_cupid + step_to_jump
    if index_to_jump >= len(size_of_neighborhood):
        index_to_jump = 0
    if size_of_neighborhood[index_to_jump] == 0:
        print(f"Place {index_to_jump} already had Valentine's day.")
    else:
        size_of_neighborhood[index_to_jump] -= 2
        if size_of_neighborhood[index_to_jump] == 0:
            print(f"Place {index_to_jump} has Valentine's day.")
    current_index_of_cupid = index_to_jump
    command = input()

print(f"Cupid's last position was {current_index_of_cupid}.")
unsuccessful_house = len(size_of_neighborhood) - size_of_neighborhood.count(0)
if unsuccessful_house == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {unsuccessful_house} places.")

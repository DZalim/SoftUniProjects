sequence_of_targets = [int(value) for value in input().split()]

command = input()
while command != "End":
    split_command = command.split()
    action = split_command[0]
    if action == "Shoot":
        index = int(split_command[1])
        power = int(split_command[2])
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets[index] -= power
            if sequence_of_targets[index] <= 0:
                sequence_of_targets.remove(sequence_of_targets[index])
    elif action == "Add":
        index = int(split_command[1])
        value = int(split_command[2])
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        index = int(split_command[1])
        radius = int(split_command[2])
        if 0 <= index - radius < len(sequence_of_targets) and 0 <= index + radius < len(sequence_of_targets):
            for remove_strike_element in range(index+radius, index-radius - 1, -1):
                sequence_of_targets.remove(sequence_of_targets[remove_strike_element])
        else:
            print("Strike missed!")
    command = input()

print("|".join(str(target) for target in sequence_of_targets))

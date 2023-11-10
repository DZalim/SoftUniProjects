current_string = input()

command = input()
while command != "Travel":
    split_command = command.split(":")
    action = split_command[0]
    if action == "Add Stop":
        index = int(split_command[1])
        string = split_command[2]
        if 0 <= index < len(current_string):
            current_string = current_string[:index]+string+current_string[index:]
        print(current_string)
    elif action == "Remove Stop":
        start_index = int(split_command[1])
        end_index = int(split_command[2])
        if 0 <= start_index < end_index < len(current_string):
            current_string = current_string[:start_index]+current_string[end_index+1:]
        print(current_string)
    elif action == "Switch":
        old_string = split_command[1]
        new_string = split_command[2]
        if old_string in current_string:
            current_string = current_string.replace(old_string, new_string)
        print(current_string)

    command = input()

print(f"Ready for world tour! Planned stops: {current_string}")

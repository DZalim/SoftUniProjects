list_with_groceries = input().split("!")
command = input()

while "Go Shopping!" not in command:
    current_command = command.split()
    name_of_command = current_command[0]
    if name_of_command == "Urgent":
        if current_command[1] not in list_with_groceries:
            list_with_groceries.insert(0, current_command[1])
    elif name_of_command == "Unnecessary":
        if current_command[1] in list_with_groceries:
            list_with_groceries.remove(current_command[1])
    elif name_of_command == "Correct":
        old_item = current_command[1]
        new_item = current_command[2]
        if old_item in list_with_groceries:
            list_with_groceries[int(list_with_groceries.index(old_item))] = new_item
    elif name_of_command == "Rearrange":
        if current_command[1] in list_with_groceries:
            list_with_groceries.remove(current_command[1])
            list_with_groceries.append(current_command[1])
    command = input()

print(", ".join(list_with_groceries))

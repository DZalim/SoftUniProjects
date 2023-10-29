list_of_names_of_friends = input().split(", ")

command = input()
while command != "Report":
    split_command = command.split()
    action = split_command[0]
    if action == "Blacklist":
        name = split_command[1]
        if name in list_of_names_of_friends:
            print(f"{name} was blacklisted.")
            name_index = list_of_names_of_friends.index(name)
            list_of_names_of_friends[name_index] = "Blacklisted"
        else:
            print(f"{name} was not found.")
    elif action == "Error":
        index = int(split_command[1])
        if 0 <= index < len(list_of_names_of_friends):
            name_of_index = list_of_names_of_friends[index]
            if name_of_index != "Blacklisted" and name_of_index != "Lost":
                print(f"{name_of_index} was lost due to an error.")
                list_of_names_of_friends[index] = "Lost"
    elif action == "Change":
        index = int(split_command[1])
        new_name = split_command[2]
        if 0 <= index < len(list_of_names_of_friends):
            name_of_index = list_of_names_of_friends[index]
            print(f"{name_of_index} changed his username to {new_name}.")
            list_of_names_of_friends[index] = new_name
    command = input()

print(f"Blacklisted names: {list_of_names_of_friends.count('Blacklisted')}")
print(f"Lost names: {list_of_names_of_friends.count('Lost')}")
print(" ".join(list_of_names_of_friends))

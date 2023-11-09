activation_key = input()

command = input().split(">>>")
while command[0] != "Generate":
    action = command[0]
    if action == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        upper_or_lower = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        chars_to_replace = activation_key[start_index:end_index]
        if upper_or_lower == "Upper":
            activation_key = activation_key.replace(chars_to_replace, chars_to_replace.upper())
        elif upper_or_lower == "Lower":
            activation_key = activation_key.replace(chars_to_replace, chars_to_replace.lower())
        print(activation_key)
    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        string_to_delete = activation_key[start_index:end_index]
        activation_key = activation_key.replace(string_to_delete, "")
        print(activation_key)
    command = input().split(">>>")

print(f"Your activation key is: {activation_key}")

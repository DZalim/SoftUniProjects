concealed_message = input()

command = input()
while command != "Reveal":
    split_command = command.split(":|:")
    action = split_command[0]
    if action == "InsertSpace":
        index = int(split_command[1])
        concealed_message = concealed_message[:index]+" "+concealed_message[index::]
        print(concealed_message)
    elif action == "Reverse":
        substring = split_command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message += substring[::-1]
            print(concealed_message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = split_command[1]
        replacement = split_command[2]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    command = input()

print(f"You have a new text message: {concealed_message}")

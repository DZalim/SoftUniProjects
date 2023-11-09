encrypted_message = input()

command = input()
while command != "Decode":
    split_command = command.split('|')
    action = split_command[0]
    if action == "Move":
        number_of_letters = int(split_command[1])
        encrypted_message = encrypted_message[number_of_letters:]+encrypted_message[:number_of_letters]
    elif action == "Insert":
        index = int(split_command[1])
        value = split_command[2]
        encrypted_message = encrypted_message[:index]+value+encrypted_message[index:]
    elif action == "ChangeAll":
        substring = split_command[1]
        replacement = split_command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {encrypted_message}")

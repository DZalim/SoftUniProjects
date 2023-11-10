encrypted_password = input()

decrypted_password = ""

command = input()
while command != "Done":
    split_command = command.split()
    action = split_command[0]
    if action == "TakeOdd":
        for odd_index in range(1, len(encrypted_password), 2):
            decrypted_password += encrypted_password[odd_index]
        print(decrypted_password)
    elif action == "Cut":
        index = int(split_command[1])
        length = int(split_command[2])
        decrypted_password = encrypted_password[:index]+encrypted_password[index+length:]
        print(decrypted_password)
    elif action == "Substitute":
        substring = split_command[1]
        substitute = split_command[2]
        if substring in encrypted_password:
            decrypted_password = encrypted_password.replace(substring, substitute)
            print(decrypted_password)
        else:
            print("Nothing to replace!")
    encrypted_password = decrypted_password
    command = input()

print(f"Your password is: {decrypted_password}")

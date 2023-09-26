from sys import maxsize

max_number = -maxsize

while True:
    command = input()
    if command == "Stop":
        break
    else:
        command = int(command)
        if max_number < command:
            max_number = command

print(max_number)
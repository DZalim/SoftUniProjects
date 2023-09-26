from sys import maxsize

min_number = maxsize

while True:
    command = input()
    if command == "Stop":
        break
    else:
        command = int(command)
        if min_number > command:
            min_number = command

print(min_number)


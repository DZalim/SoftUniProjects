list_of_gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    command = command.split()
    if command[0] == "OutOfStock":
        for gift in range(len(list_of_gifts)):
            if command[1] == list_of_gifts[gift]:
                list_of_gifts[gift] = "None"
    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(list_of_gifts):
            list_of_gifts[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        list_of_gifts[-1] = command[1]

for remove_string in list_of_gifts:
    if remove_string == "None":
        continue
    print(remove_string, end=" ")

list_of_phones = input().split(", ")

command = input()
while command != "End":
    split_command = command.split(" - ")
    action = split_command[0]
    if action == "Add":
        phone = split_command[1]
        if phone not in list_of_phones:
            list_of_phones.append(phone)
    elif action == "Remove":
        phone = split_command[1]
        if phone in list_of_phones:
            list_of_phones.remove(phone)
    elif action == "Bonus phone":
        split_phones = split_command[1].split(":")
        old_phone = split_phones[0]
        new_phone = split_phones[1]
        if old_phone in list_of_phones:
            index_old_phone = list_of_phones.index(old_phone)
            list_of_phones.insert(index_old_phone+1, new_phone)
    elif action == "Last":
        phone = split_command[1]
        if phone in list_of_phones:
            list_of_phones.append(phone)
            list_of_phones.remove(phone)

    command = input()

print(", ".join(list_of_phones))

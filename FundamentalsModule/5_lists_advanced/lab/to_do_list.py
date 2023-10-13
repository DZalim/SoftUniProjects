command = input()

to_do_list = [0] * 10

while command != "End":
    splitted_command = command.split("-")
    impotrance = int(splitted_command[0])
    note = splitted_command[1]
    index_for_insert = impotrance - 1
    to_do_list.pop(index_for_insert)
    to_do_list.insert(index_for_insert, note)
    command = input()

print([element for element in to_do_list if element != 0])
list_of_numbers_in_str = input().split()

command = input()
while "end" not in command:
    current_command = command.split()
    direction = current_command[0]
    if len(current_command) > 1:
        first_index = int(current_command[1])
        second_index = int(current_command[2])
    if current_command[0] == "swap":
        list_of_numbers_in_str[first_index], list_of_numbers_in_str[second_index] = list_of_numbers_in_str[second_index], list_of_numbers_in_str[first_index]
    elif current_command[0] == "multiply":
        multiply = int(list_of_numbers_in_str[first_index]) * int(list_of_numbers_in_str[second_index])
        list_of_numbers_in_str[first_index] = str(multiply)
    elif current_command[0] == "decrease":
        index = 0
        for each_number in list_of_numbers_in_str:
            new_number = int(each_number) - 1
            list_of_numbers_in_str[index] = str(new_number)
            index += 1
    command = input()

print(", ".join(list_of_numbers_in_str))
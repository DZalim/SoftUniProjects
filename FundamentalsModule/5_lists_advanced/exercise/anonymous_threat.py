sequence_of_string = input().split()

command = input()

while command != "3:1":
    splitted_command = command.split()
    action = splitted_command[0]
    if action == "merge":
        start_index = int(splitted_command[1])
        end_index = int(splitted_command[2])
        if start_index < 0 or start_index > len(sequence_of_string):
            start_index = 0
        if end_index > len(sequence_of_string):
            end_index = len(sequence_of_string) - 1
        merged_string = "".join([sequence_of_string[merge] for merge in range(start_index, end_index + 1)])
        sequence_of_string[start_index:end_index+1] = ["".join(merged_string)]
    elif action == "divide":
        divide_index = int(splitted_command[1])
        partitions_to_divide = int(splitted_command[2])
        divided_strings = []
        length_of_string_to_divide = len(sequence_of_string[divide_index]) // partitions_to_divide
        for part in range(0, partitions_to_divide*length_of_string_to_divide, length_of_string_to_divide):
            if divide_index < len(sequence_of_string):
                if partitions_to_divide*length_of_string_to_divide - length_of_string_to_divide == part:
                    divided_strings.append(sequence_of_string[divide_index][part:])
                else:
                    divided_strings.append(sequence_of_string[divide_index][part:part+length_of_string_to_divide])
        sequence_of_string = sequence_of_string[:divide_index]+divided_strings+sequence_of_string[divide_index+1:]
    command = input()

print(" ".join(sequence_of_string))

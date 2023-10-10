sequence_of_number_in_str = input().split()
command = input()

shots = 0

while command != "End":
    current_index = int(command)
    if current_index < len(sequence_of_number_in_str):
        loop_index = 0
        for each_number in sequence_of_number_in_str:
            if loop_index == current_index or int(each_number) == -1:
                loop_index += 1
                continue
            else:
                if int(each_number) <= int(sequence_of_number_in_str[current_index]):
                    new_number = int(each_number) + int(sequence_of_number_in_str[current_index])
                else:
                    new_number = int(each_number) - int(sequence_of_number_in_str[current_index])
                sequence_of_number_in_str[loop_index] = str(new_number)
            loop_index += 1
        sequence_of_number_in_str[current_index] = "-1"
        shots += 1
    command = input()

print(f"Shot targets: {shots} ->", end=" ")
print(" ".join(sequence_of_number_in_str))
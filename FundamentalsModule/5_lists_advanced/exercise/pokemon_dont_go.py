sequence_of_numbers = [int(number)for number in input().split()]

sum_of_all_removed_elements = 0

while sequence_of_numbers:
    current_index = int(input())
    current_index_is_less_than_zero = False
    current_index_is_greater_than_lists_length = False
    if current_index < 0:
        current_index_is_less_than_zero = True
        current_index = 0
    elif current_index >= len(sequence_of_numbers):
        current_index_is_greater_than_lists_length = True
        current_index = len(sequence_of_numbers) - 1
    for index in range(len(sequence_of_numbers)):
        if index == current_index:
            continue
        if sequence_of_numbers[index] <= sequence_of_numbers[current_index]:
            sequence_of_numbers[index] += sequence_of_numbers[current_index]
        elif sequence_of_numbers[index] > sequence_of_numbers[current_index]:
            sequence_of_numbers[index] -= sequence_of_numbers[current_index]
    sum_of_all_removed_elements += sequence_of_numbers[current_index]
    sequence_of_numbers.remove(sequence_of_numbers[current_index])
    if current_index_is_less_than_zero:
        sequence_of_numbers.insert(current_index, sequence_of_numbers[-1])
    elif current_index_is_greater_than_lists_length:
        sequence_of_numbers.insert(current_index, sequence_of_numbers[0])

print(sum_of_all_removed_elements)
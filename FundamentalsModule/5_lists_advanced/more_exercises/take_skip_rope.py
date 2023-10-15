string = input()

list_of_numbers = [int(digit) for digit in string if digit.isdigit()]
list_of_strings = [letter for letter in string if not letter.isdigit()]

take_list_of_numbers = [list_of_numbers[take] for take in range(len(list_of_numbers)) if take % 2 == 0]
skip_list_of_numbers = [list_of_numbers[skip] for skip in range(len(list_of_numbers)) if skip % 2 != 0]

final_string = []
list_index = 0
while list_of_strings:
    if len(list_of_strings) < take_list_of_numbers[list_index]:
        take_list_of_numbers[list_index] = len(list_of_strings)
    if take_list_of_numbers[list_index] > 0:
        for append_in_final_string in range(take_list_of_numbers[list_index]):
            final_string.append(list_of_strings[append_in_final_string])
    if len(list_of_strings) < (skip_list_of_numbers[list_index] + take_list_of_numbers[list_index]):
        skip_list_of_numbers[list_index] = len(list_of_strings)
        take_list_of_numbers[list_index] = 0
    for remove_string in range(take_list_of_numbers[list_index] + skip_list_of_numbers[list_index] - 1, -1, -1):
        list_of_strings.remove(list_of_strings[remove_string])
    list_index += 1
    if list_index == len(take_list_of_numbers):
        break

print("".join(final_string))

list_of_int_in_str = input().split()

list_of_int = []
for number_in_str in list_of_int_in_str:
    list_of_int.append(int(number_in_str))

command = input()
while "end" not in command:
    current_command = command.split()
    list_for_exchange = []
    list_of_even_or_odd_numbers = []

    if current_command[0] == "exchange":
        index = int(current_command[1])
        if 0 <= index < len(list_of_int):
            right_side = list_of_int[index + 1: len(list_of_int):]
            left_side = list_of_int[:index + 1:]
            for side_right in right_side:
                list_for_exchange.append(side_right)
            for side_left in left_side:
                list_for_exchange.append(side_left)
            list_of_int = list_for_exchange
        else:
            print("Invalid index")

    elif current_command[0] == "max" or current_command[0] == "min":
        for each_number in list_of_int:
            if current_command[1] == "even":
                if each_number % 2 == 0:
                    list_of_even_or_odd_numbers.append(each_number)
            else:
                if each_number % 2 == 1:
                    list_of_even_or_odd_numbers.append(each_number)
        if current_command[0] == "max":
            if len(list_of_even_or_odd_numbers) > 0:
                max_even_or_odd = max(list_of_even_or_odd_numbers)
                for print_max_even_or_odd in range(len(list_of_int) - 1, -1, -1):
                    if int(list_of_int[print_max_even_or_odd]) == max_even_or_odd:
                        print(print_max_even_or_odd)
                        break
            else:
                print("No matches")
        elif current_command[0] == "min":
            if len(list_of_even_or_odd_numbers) > 0:
                min_even_or_odd = min(list_of_even_or_odd_numbers)
                for print_min_even_or_odd in range(len(list_of_int) - 1, -1, -1):
                    if int(list_of_int[print_min_even_or_odd]) == min_even_or_odd:
                        print(print_min_even_or_odd)
                        break
            else:
                print("No matches")

    elif current_command[0] == "first" or current_command[0] == "last":
        count_of_number = int(current_command[1])
        for numbers_in_list in list_of_int:
            if current_command[2] == "even":
                if numbers_in_list % 2 == 0:
                    list_of_even_or_odd_numbers.append(numbers_in_list)
            else:
                if numbers_in_list % 2 == 1:
                    list_of_even_or_odd_numbers.append(numbers_in_list)
        list_for_first_count_to_print = []
        list_for_last_count_to_print = []
        if current_command[0] == "first":
            if count_of_number < 0:
                break
            elif count_of_number <= len(list_of_int) and len(list_of_even_or_odd_numbers) > 0:
                if count_of_number > len(list_of_even_or_odd_numbers):
                    count_of_number = len(list_of_even_or_odd_numbers)
                for first_count in range(count_of_number):
                    list_for_first_count_to_print.append(list_of_even_or_odd_numbers[first_count])
                print(list_for_first_count_to_print)
            elif len(list_of_even_or_odd_numbers) == 0:
                print("[]")
            elif count_of_number > len(list_of_int):
                print("Invalid count")
        elif current_command[0] == "last":
            if count_of_number < 0:
                break
            elif count_of_number <= len(list_of_int) and len(list_of_even_or_odd_numbers) > 0:
                if count_of_number > len(list_of_even_or_odd_numbers):
                    count_of_number = len(list_of_even_or_odd_numbers)
                list_of_even_or_odd_numbers.reverse()
                for last_count in range(count_of_number-1, -1, -1):
                    list_for_last_count_to_print.append(list_of_even_or_odd_numbers[last_count])
                print(list_for_last_count_to_print)
            elif len(list_of_even_or_odd_numbers) == 0:
                print("[]")
            elif count_of_number > len(list_of_int):
                print("Invalid count")

    command = input()

print(list_of_int)

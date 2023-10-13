def calculate_absolute_value(number):
    for current_number in range(len(number)):
        number[current_number] = abs(float(number[current_number]))
    print(number)


list_of_num_in_str = input().split()
calculate_absolute_value(list_of_num_in_str)

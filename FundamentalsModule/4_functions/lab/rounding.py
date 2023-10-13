def calculate_rounding(numbers):
    for current_number in range(len(numbers)):
        numbers[current_number] = round(float(numbers[current_number]))
    print(numbers)


numbers_in_list = input().split()
calculate_rounding(numbers_in_list)
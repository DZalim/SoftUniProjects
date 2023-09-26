number = int(input())

for current_number in range(1111, 9999 + 1):
    current_number_as_string = str(current_number)
    is_special_number = True
    for current_digit in current_number_as_string:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            is_special_number = False
            break
    if is_special_number:
        print(current_number, end= " ")

def check_perfect_number(current_number):
    sum_of_digits = 0
    for digit in range(1, current_number):
        if current_number % digit == 0:
            sum_of_digits += digit
    if sum_of_digits == current_number:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
returned_result = check_perfect_number(number)
print(returned_result)
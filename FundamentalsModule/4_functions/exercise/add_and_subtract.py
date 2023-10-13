def sum_numbers(first, second):
    result_sum_numbers = first + second
    return result_sum_numbers


def subtract(sum_first_two, third):
    result_subtract = sum_first_two - third
    return result_subtract


def add_and_subtract(first, second, third):
    returned_result = sum_numbers(first, second)
    final_result = subtract(returned_result, third)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())

final_result = add_and_subtract(first_number, second_number, third_number)
print(final_result)
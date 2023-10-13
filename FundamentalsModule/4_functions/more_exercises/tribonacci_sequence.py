def calculate_tribonacci_sequence(number):
    calculate_numbers = [1]
    for number in range(1, number):
        sum_for_append = 0
        if len(calculate_numbers) < 3:
            for append_sum in range(len(calculate_numbers)):
                sum_for_append += calculate_numbers[append_sum]
            calculate_numbers.append(sum_for_append)
        else:
            for append_sum in range(len(calculate_numbers) - 3, len(calculate_numbers)):
                sum_for_append += calculate_numbers[append_sum]
            calculate_numbers.append(sum_for_append)
    return calculate_numbers


number_for_print = int(input())
result = calculate_tribonacci_sequence(number_for_print)
number_of_string = ([str(number) for number in result])
print(" ".join(number_of_string))
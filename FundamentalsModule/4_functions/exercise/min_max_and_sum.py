def min_max_sum_of_numbers(numbers):
    list_of_numbers = []
    for number in numbers:
        list_of_numbers.append(int(number))
    min_number = min(list_of_numbers)
    max_number = max(list_of_numbers)
    sum_of_numbers = sum(list_of_numbers)
    return min_number, max_number, sum_of_numbers


list_of_numbers_in_str = input().split()
minim, maxim, sum_num = min_max_sum_of_numbers(list_of_numbers_in_str)

print(f"The minimum number is {minim}")
print(f"The maximum number is {maxim}")
print(f"The sum number is: {sum_num}")
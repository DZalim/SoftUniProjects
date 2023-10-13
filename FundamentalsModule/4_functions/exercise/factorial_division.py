def factorial_number(first, second):
    sum_of_factorial = first
    for current_num in range(first - 1, second, -1):
        sum_of_factorial *= current_num
    return sum_of_factorial


first_num = int(input())
second_num = int(input())

returned_result = factorial_number(first_num, second_num)
print(f"{returned_result:.2f}")
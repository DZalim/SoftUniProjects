from collections import deque

numbers = deque([int(x) for x in input().split(', ')])
searched_index = int(input())

searched_number = numbers[searched_index]

total_clock_cycles = 0
numbers_copy = deque(sorted(numbers.copy()))

for number in numbers_copy:
    total_clock_cycles += number
    if number == searched_number:
        if numbers.count(number) > 1:
            for number_index in range(len(numbers)):
                if number == searched_number and searched_index == number_index:
                    break
                elif numbers[number_index] == searched_number and searched_index != number_index:
                    total_clock_cycles += number
        print(total_clock_cycles)
        exit()


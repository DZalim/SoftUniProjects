from collections import deque


def list_manipulator(list_of_numbers, add_or_remove, beginning_or_end, *numbers):

    list_of_numbers = deque(list_of_numbers)

    if add_or_remove == 'add':
        if beginning_or_end == 'beginning':
            for number in numbers[::-1]:
                list_of_numbers.appendleft(number)

        elif beginning_or_end == 'end':
            for number in numbers:
                list_of_numbers.append(number)

    elif add_or_remove == 'remove':
        if beginning_or_end == 'beginning':
            if numbers:
                count_for_remove = numbers[0]
                for remove in range(count_for_remove-1, -1, -1):
                    list_of_numbers.popleft()
            else:
                list_of_numbers.popleft()

        elif beginning_or_end == 'end':
            if numbers:
                count_for_remove = numbers[0]
                for remove in range(count_for_remove-1, -1, -1):
                    list_of_numbers.pop()
            else:
                list_of_numbers.pop()

    return list(list_of_numbers)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

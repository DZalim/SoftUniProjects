from collections import deque


def best_list_pureness(*args):
    number_k = args[-1]
    my_list = deque([el for el in args[0]])

    best_pureness = float('-inf')
    rotation = 0

    for k_time in range(number_k + 1):
        current_pureness = 0
        for number_index, number in enumerate(my_list):
            current_pureness += number_index * number
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            rotation = k_time
        my_list.rotate()

    return f"Best pureness {best_pureness} after {rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

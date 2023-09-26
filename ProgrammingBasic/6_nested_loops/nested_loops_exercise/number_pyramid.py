number = int(input())
number_counter = 0
is_current_bigger_than_number = False

for row in range(1, number + 1):
    for column in range(1, row + 1):
        number_counter += 1
        if number_counter > number:
            is_current_bigger_than_number = True
            break
        print(number_counter, end=" ")
    if is_current_bigger_than_number:
        break
    print()

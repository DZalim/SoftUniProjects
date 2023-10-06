list_of_numbers_in_string = input().split()
count_for_remove = int(input())

list_of_numbers_in_int = []

for number in list_of_numbers_in_string:
    list_of_numbers_in_int.append(int(number))

for current_remove in range(count_for_remove):
    list_of_numbers_in_int.remove(min(list_of_numbers_in_int))

for string_number in range(len(list_of_numbers_in_int)):
    num = list_of_numbers_in_int[string_number]
    if string_number == len(list_of_numbers_in_int) - 1:
        print(num)
    else:
        print(num, end=", ")


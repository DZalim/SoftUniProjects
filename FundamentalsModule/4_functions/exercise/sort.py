list_of_numbers_in_str = input().split()

list_of_numbers = []
for number in list_of_numbers_in_str:
    list_of_numbers.append(int(number))

sorted_result = sorted(list_of_numbers)
print(sorted_result)
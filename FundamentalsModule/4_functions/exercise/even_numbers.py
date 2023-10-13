list_of_numbers_in_str = input().split()

list_of_numbers = []
for number in list_of_numbers_in_str:
    list_of_numbers.append(int(number))

filtered_result = filter(lambda x: x % 2 == 0, list_of_numbers)
print(list(filtered_result))
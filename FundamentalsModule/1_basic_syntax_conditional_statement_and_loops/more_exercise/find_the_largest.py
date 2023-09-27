number = input()

number_in_list = list(number)
number_in_list.sort(reverse=True)

print("".join(number_in_list))

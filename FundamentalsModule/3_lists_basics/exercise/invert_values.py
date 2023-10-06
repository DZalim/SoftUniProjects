list_of_strings = input().split()

list_of_integer = []

for element in list_of_strings:
    current_element = -(int(element))
    list_of_integer.append(current_element)

print(list_of_integer)


list_in_strings = input().split(", ")

list_in_int = []

for number in list_in_strings:
    list_in_int.append(int(number))

for index in range(len(list_in_int)-1, -1, -1):
    if list_in_int[index] == 0:
        list_in_int.remove(list_in_int[index])
        list_in_int.append(0)

print(list_in_int)

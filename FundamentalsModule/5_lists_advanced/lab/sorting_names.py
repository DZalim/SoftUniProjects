list_of_name = input().split(", ")

sorted_list = sorted(list_of_name, key=lambda x: (-len(x), x))

print(sorted_list)

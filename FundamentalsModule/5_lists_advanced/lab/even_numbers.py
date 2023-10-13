#list_of_numbers = input().split(", ")
#print([index for index in range(len(list_of_numbers)) if int(list_of_numbers[index]) % 2 == 0])

list_of_numbers = list(map(int, input().split(", ")))
print(list(map(lambda x: list_of_numbers.index(x), list(filter(lambda x: x % 2 == 0, list_of_numbers)))))

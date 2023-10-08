number_of_people = input().split()
skip_number_k = int(input())

list_of_executed = []
skip_number_k = skip_number_k - 1
len_list = len(number_of_people)
index = 0

while len_list > 0:
    index = (skip_number_k + index) % len_list
    list_of_executed.append((number_of_people.pop(index)))
    len_list -= 1

print(f"[{','.join(list_of_executed)}]")

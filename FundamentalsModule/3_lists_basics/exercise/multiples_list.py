factor = int(input())
count = int(input())

list_for_print = []

for number in range(1, count+1):
    multiply = factor * number
    list_for_print.append(multiply)

print(list_for_print)
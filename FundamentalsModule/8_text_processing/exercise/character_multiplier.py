string_to_multiply = input().split()

max_string = max(len(string_to_multiply[0]), len(string_to_multiply[1]))

total_sum = 0

for index in range(max_string):
    if index < len(string_to_multiply[0]) and index < len(string_to_multiply[1]):
        total_sum += ord(string_to_multiply[0][index]) * ord(string_to_multiply[1][index])
    elif len(string_to_multiply[0]) == max_string:
        total_sum += ord(string_to_multiply[0][index])
    elif len(string_to_multiply[1]) == max_string:
        total_sum += ord(string_to_multiply[1][index])

print(total_sum)

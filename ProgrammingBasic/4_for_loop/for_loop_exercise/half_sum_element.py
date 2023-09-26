count_of_numbers = int(input())
first_number = int(input())

max_number = first_number
total_sum = first_number

for number in range (count_of_numbers - 1):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_number:
        max_number = current_number

sum = total_sum - max_number

if sum == max_number:
    print(f"Yes\nSum = {max_number}")
else:
    diff = abs(sum - max_number)
    print(f"No\nDiff = {diff} ")

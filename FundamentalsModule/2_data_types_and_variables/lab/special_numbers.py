count_n = int(input())

for current_number in range (1, count_n + 1):
    sum_of_digits = 0
    for digit in str(current_number):
        sum_of_digits += int(digit)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{current_number} -> True")
    else:
        print(f"{current_number} -> False")
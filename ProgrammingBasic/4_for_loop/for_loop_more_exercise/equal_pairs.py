numbers = int(input())

sum_first_and_second = 0
sum_first_and_second_previous = 0
diff = 0
max_diff = diff

for num in range(numbers):
    first_number = int(input())
    second_number = int(input())
    if num > 0:
        sum_first_and_second_previous = sum_first_and_second
    sum_first_and_second = first_number + second_number
    if num > 0:
        diff = abs(sum_first_and_second_previous - sum_first_and_second)
        if diff > max_diff:
            max_diff = diff

if diff == 0:
    print(f"Yes, value={sum_first_and_second}")
else:
    print(f"No, maxdiff={diff}")



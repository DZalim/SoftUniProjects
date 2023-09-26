first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    even_sum = 0
    odd_sum = 0
    current_number = str(number)
    for index, digit in enumerate(current_number):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if odd_sum == even_sum:
        print(number, end=" ")

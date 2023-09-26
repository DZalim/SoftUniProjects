number = int(input())

numbers = 0

for num in range (number):
    current_number = int(input())
    numbers += current_number

average_number = numbers / number

print(f"{average_number: .2f}")
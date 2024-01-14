numbers = tuple(float(number) for number in input().split())

numbers_dict = {}

for number in numbers:
    numbers_dict[number] = numbers.count(number)

for key, value in numbers_dict.items():
    print(f"{key} - {value} times")

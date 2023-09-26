count_of_numbers = int(input())

for first_string in range(count_of_numbers):
    for second_string in range(count_of_numbers):
        for third_string in range(count_of_numbers):
            print(f"{chr(first_string+97)}{chr(second_string+97)}{chr(third_string+97)}")
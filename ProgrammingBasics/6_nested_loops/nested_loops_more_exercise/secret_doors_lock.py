first_number_end_range = int(input())
second_number_end_range = int(input())
third_number_end_range = int(input())

for first_number in range (1, first_number_end_range + 1):
    if first_number % 2 == 0:
        for second_number in range (2, second_number_end_range + 1):
            is_prime_number = True
            for second in range (2, second_number):
                if second_number % second == 0:
                    is_prime_number = False
            if is_prime_number:
                for third_number in range (1, third_number_end_range + 1):
                    if third_number % 2 == 0:
                        print(f"{first_number} {second_number} {third_number}")

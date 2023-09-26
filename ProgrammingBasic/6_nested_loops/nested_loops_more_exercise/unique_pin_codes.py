upper_bound_of_a_first_number = int(input())
upper_bound_of_a_second_number = int(input())
upper_bound_of_a_third_number = int(input())

for first_number in range(1, upper_bound_of_a_first_number + 1):
    if first_number % 2 == 0:
        for second_number in range (2, upper_bound_of_a_second_number + 1):
            prime_number = True
            for number in range(2, second_number):
                if second_number % number == 0:
                    prime_number = False
            if prime_number:
                for third_number in range(1, upper_bound_of_a_third_number + 1):
                    if third_number % 2 == 0:
                        print(f"{first_number} {second_number} {third_number}")

print()


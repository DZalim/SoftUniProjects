start_range_first_couple = int(input())
start_range_second_couple = int(input())
diff_end_first_couple = int(input())
diff_end_second_couple = int(input())

for first_couple in range(start_range_first_couple, start_range_first_couple + diff_end_first_couple + 1):
    first_couple_is_prime_number = True
    for number_one in range(2, first_couple):
        if first_couple % number_one == 0:
            first_couple_is_prime_number = False
    for second_couple in range(start_range_second_couple, start_range_second_couple + diff_end_second_couple +1):
        second_couple_is_prime_number = True
        for number_two in range(2, second_couple):
            if second_couple % number_two == 0:
                second_couple_is_prime_number = False
        if first_couple_is_prime_number and second_couple_is_prime_number:
            print(f"{first_couple}{second_couple}")


start_range = int(input())
end_range = int(input())

for number_one in range(start_range, end_range + 1):
    for number_two in range(start_range, end_range + 1):
        for number_three in range(start_range, end_range + 1):
            for number_four in range(start_range, end_range + 1):
                if ((number_one % 2 == 0 and number_four % 2 != 0) or (number_one % 2 != 0 and number_four % 2 == 0)) \
                        and (number_one > number_four) and ((number_two + number_three) % 2) == 0:
                    print(f"{number_one}{number_two}{number_three}{number_four}", end=" ")


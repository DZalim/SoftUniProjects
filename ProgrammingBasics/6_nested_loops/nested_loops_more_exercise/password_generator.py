number_n = int(input())
number_l = int(input())

for number_one in range(1, number_n + 1):
    for number_two in range(1, number_n + 1):
        for number_three in range(1, number_l + 1):
            for number_four in range(1, number_l + 1):
                for number_five in range(1, number_n + 1):
                    if number_one < number_five and number_two < number_five:
                        print(f"{number_one}{number_two}{chr(number_three + 96)}{chr(number_four + 96)}{number_five}",\
                              end = " ")

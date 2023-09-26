number_n = int(input())

for number_one in range (1, 10):
    for number_two in range(1, 10):
        for number_three in range(1, 10):
            for number_four in range(1, 10):
                if ((number_one + number_two) == (number_three + number_four))\
                        and (number_n % (number_one+number_two)) == 0:
                    print(f"{number_one}{number_two}{number_three}{number_four}", end= " ")
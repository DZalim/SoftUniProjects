number_n = int(input())

found_combination = False

for number_a in range(1, 10):
    for number_b in range(9, number_a - 1, -1):
        for number_c in range(10):
            for number_d in range(9, number_c - 1, -1):
                if (number_a + number_b + number_c + number_d) == (number_a * number_b * number_c * number_d)\
                        and number_n % 10 == 5:
                    found_combination = True
                    print(f"{number_a}{number_b}{number_c}{number_d}")
                    break
                elif (number_a * number_b * number_c * number_d) // (number_a + number_b + number_c + number_d) == 3\
                        and number_n % 3 == 0:
                    found_combination = True
                    print(f"{number_d}{number_c}{number_b}{number_a}")
                    break
            if found_combination:
                break
        if found_combination:
            break
    if found_combination:
        break

if not found_combination:
    print("Nothing found")

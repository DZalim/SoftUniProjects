number_of_1_lev = int(input())
number_of_2_leva = int(input())
number_of_5_leva = int(input())
total_sum = int(input())

for one_lev in range (number_of_1_lev + 1):
    for two_leva in range(number_of_2_leva + 1):
        for five_leva in range(number_of_5_leva + 1):
            if one_lev * 1 + two_leva * 2 + five_leva * 5 == total_sum:
                print(f"{one_lev} * 1 lv. + {two_leva} * 2 lv. + {five_leva} * 5 lv. = {total_sum} lv.")


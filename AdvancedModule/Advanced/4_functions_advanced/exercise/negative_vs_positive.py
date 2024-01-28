def sum_numbers(*numbers):
    sum_of_negative = sum([number for number in numbers if number < 0])
    sum_of_positive = sum([number for number in numbers if number > 0])

    print(sum_of_negative)
    print(sum_of_positive)

    if sum_of_positive > abs(sum_of_negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers_sequence = (int(number) for number in input().split())

sum_numbers(*numbers_sequence)

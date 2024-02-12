def numbers_searching(*args):
    set_of_numbers = sorted(set(args))
    all_needed_numbers = {number for number in range(min(args), max(args) + 1)}
    missing_number = list(all_needed_numbers.difference(set_of_numbers))
    duplicate_numbers = []

    for number in set_of_numbers:
        if args.count(number) > 1:
            duplicate_numbers.append(number)

    result = [missing_number[-1], duplicate_numbers]

    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

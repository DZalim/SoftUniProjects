def palindrome_integers(numbers):
    for number in numbers:
        if number == number[::-1]:
            print("True")
        else:
            print("False")


list_of_numbers_in_str = input().split(", ")
palindrome_integers(list_of_numbers_in_str)
def addition(first_number, second_number):
    return int(first_number) + int(second_number)


def subtraction(first_number, second_number):
    return int(first_number) - int(second_number)


def multiplication(first_number, second_number):
    return int(first_number) * int(second_number)


def division(first_number, second_number):
    if second_number != "0":
        return int(first_number) // int(second_number)
    else:
        return 0


def main(first, second, operand):
    if operand == "1":
        return addition(first, second)
    elif operand == "2":
        return subtraction(first, second)
    elif operand == "3":
        return multiplication(first, second)
    elif operand == "4":
        return division(first, second)


print("Menu:")
print("     1.Addition")
print("     2.Subtraction")
print("     3.Multiplication")
print("     4.Division")
print("     5.Quit")

while True:
    choice_input = input("Enter your choice: [1], [2], [3], [4] or [5] ")
    if choice_input == "5":
        print("Thank you. Goodbye!")
        break
    if choice_input == "1" or choice_input == "2" or choice_input == "3" or choice_input == "4":
        first_input = input(" Enter the first number: ")
        second_input = input(" Enter the second number: ")
        result = main(first_input, second_input, choice_input)
        if choice_input == "1":
            choice_input = "+"
        elif choice_input == "2":
            choice_input = "-"
        elif choice_input == "3":
            choice_input = "*"
        elif choice_input == "4":
            choice_input = "/"
        print(f"Result: {first_input} {choice_input} {second_input} = {result}")
    else:
        print("Invalid input. Try again!")

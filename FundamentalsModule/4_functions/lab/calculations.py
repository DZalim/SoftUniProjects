def calculations(current_operator, first_number, second_number):
    if current_operator == "multiply":
        result = first_number * second_number
    elif current_operator == "divide":
        result = first_number // second_number
    elif current_operator == "add":
        result = first_number + second_number
    elif current_operator == "subtract":
        result = first_number - second_number
    return result


operator = input()
first_num = int(input())
second_num = int(input())
returned_result = calculations(operator, first_num, second_num)
print(returned_result)

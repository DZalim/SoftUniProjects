def calculate_result_of_multiplication(first, second, third):
    if first == 0 or second == 0 or third == 0:
        return "zero"
    elif (first > 0 and (second < 0 and third < 0)) or \
            (second > 0 and (first < 0 and third < 0)) or \
            (third > 0 and (first < 0 and second < 0)) or \
            (first > 0 and second > 0 and third > 0):
        return "positive"
    else:
        return "negative"


first_number = int(input())
second_number = int(input())
third_number = int(input())

result = calculate_result_of_multiplication(first_number, second_number, third_number)
print(result)
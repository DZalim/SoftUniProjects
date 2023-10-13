def odd_and_even_sum(digits):
    odd_sum = 0
    even_sum = 0
    for digit in digits:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return odd_sum, even_sum


digits_int_str = input()

returned_odd_result, returned_even_result = odd_and_even_sum(digits_int_str)
print(f"Odd sum = {returned_odd_result}, Even sum = {returned_even_result}")

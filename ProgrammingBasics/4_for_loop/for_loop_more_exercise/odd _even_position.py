count_n = int(input())

odd_sum = 0
odd_min = 0
odd_max = 0
even_sum = 0
even_min = 0
even_max = 0

for number in range(1, count_n+1):
    current_number = float(input())
    if number == 1:
        odd_sum += current_number
        odd_max = current_number
        odd_min = current_number
    elif number == 2:
        even_sum += current_number
        even_max = current_number
        even_min = current_number
    elif number % 2 != 0:
        odd_sum += current_number
        if current_number > odd_max:
            odd_max = current_number
        if current_number < odd_min:
            odd_min = current_number
    else:
        even_sum += current_number
        if current_number > even_max:
            even_max = current_number
        if current_number < even_min:
            even_min = current_number

print(f"OddSum={odd_sum:.2f},")
if odd_min != 0:
    print(f"OddMin={odd_min:.2f},")
else:
    print("No,")
if odd_max != 0:
    print(f"OddMax={odd_max:.2f},")
else:
    print("No.")
print(f"EvenSum={even_sum:.2f},")
if even_min != 0:
    print(f"EvenMin={even_min:.2f},")
else:
    print("No,")
if even_max != 0:
    print(f"EvenMax={even_max:.2f}")
else:
    print("No")




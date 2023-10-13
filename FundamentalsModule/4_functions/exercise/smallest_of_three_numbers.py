def smallest_number(first, second, third):
    if first < second and first < third:
        result = first
    elif second < first and second < third:
        result = second
    elif third < second and third < first:
        result = third
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

smallest = smallest_number(first_number, second_number, third_number)
print(smallest)
def grades(current_number):
    if 2 <= current_number < 3:
        result = "Fail"
    elif 3 <= current_number < 3.50:
        result = "Poor"
    elif 3.50 <= current_number < 4.50:
        result = "Good"
    elif 4.50 <= current_number < 5.50:
        result = "Very Good"
    elif 5.50 <= current_number <= 6:
        result = "Excellent"
    return result


current_grade = float(input())
print(grades(current_grade))

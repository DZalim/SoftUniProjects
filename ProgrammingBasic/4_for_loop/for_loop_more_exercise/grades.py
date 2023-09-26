number_of_students = int(input())

top_students = 0
between_4_and_5 = 0
between_3_and_4 = 0
fail = 0
total_grade = 0

for student in range (number_of_students):
    grade = float(input())
    if 2 <= grade < 3:
        fail +=1
    elif 3 <= grade < 4:
        between_3_and_4 += 1
    elif 4 <= grade < 5:
        between_4_and_5 += 1
    elif  grade >= 5:
        top_students += 1
    total_grade += grade

average_grade = total_grade / number_of_students

top_students_percent = top_students / number_of_students * 100
between_4_and_5_percent = between_4_and_5 / number_of_students * 100
between_3_and_4_percent = between_3_and_4 / number_of_students * 100
fail_percent = fail / number_of_students * 100

print(f"Top students: {top_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_5_percent:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_4_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average_grade:.2f}")


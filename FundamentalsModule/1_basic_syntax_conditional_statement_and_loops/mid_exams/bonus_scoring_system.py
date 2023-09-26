from math import ceil

number_of_the_students = int(input())
number_of_the_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
lectures = 0

for student in range (number_of_the_students):
    attendance_of_student = int(input())
    total_bonus = attendance_of_student / number_of_the_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        lectures = attendance_of_student

print(f"Max Bonus: {ceil(max_bonus)}.\nThe student has attended {lectures} lectures.")
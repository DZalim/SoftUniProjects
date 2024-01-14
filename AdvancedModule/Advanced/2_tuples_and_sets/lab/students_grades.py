count_of_students = int(input())

students_grades = {}

for student in range(count_of_students):
    student_name, grade = input().split()
    if student_name not in students_grades.keys():
        students_grades[student_name] = []
    students_grades[student_name].append(float(grade))

for key, value in students_grades.items():
    average_grade = sum(value)/len(value)
    formatted_grades = ['%.2f' % grade for grade in value]
    print(f"{key} -> {' '.join(formatted_grades)} (avg: {average_grade:.2f})")

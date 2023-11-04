pair_of_rows = int(input())

my_dict_with_grades = {}

for current_commands in range(pair_of_rows):
    current_student = input()
    current_grade = float(input())
    if current_student not in my_dict_with_grades.keys():
        my_dict_with_grades[current_student] = []
    my_dict_with_grades[current_student].append(current_grade)

for name, grades in my_dict_with_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")

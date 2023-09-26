name = input()

total_grades = 0
clas = 0
failed = 0

while True:
    grade = float(input())
    if grade < 4:
        failed += 1
        if failed == 2:
            print(f"{name} has been excluded at {clas + 1} grade")
            break
    else:
        total_grades += grade
        clas += 1
        if clas == 12:
            average_grade = total_grades / clas
            print(f"{name} graduated. Average grade: {average_grade:.2f}")
            break



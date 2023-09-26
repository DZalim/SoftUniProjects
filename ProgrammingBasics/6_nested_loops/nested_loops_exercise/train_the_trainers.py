number_of_jurys = int(input())

total_grade = 0
total_presentations = 0

name_of_the_presentation = input()
while name_of_the_presentation != "Finish":
    total_presentations += 1
    grade_for_presentation = 0
    for grades in range(number_of_jurys):
        current_grade = float(input())
        grade_for_presentation += current_grade
    average_grade_per_presentation = grade_for_presentation / number_of_jurys
    total_grade += average_grade_per_presentation
    print(f"{name_of_the_presentation} - {average_grade_per_presentation:.2f}.")
    name_of_the_presentation = input()

average_grade = total_grade / total_presentations
print(f"Student's final assessment is {average_grade:.2f}.")

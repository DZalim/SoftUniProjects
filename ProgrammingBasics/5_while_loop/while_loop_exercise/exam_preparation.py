max_grade_for_fail = int(input())

solved_problem = 0
total_grades = 0
failed = 0
is_failed = False

name_of_task = input()

while name_of_task != "Enough":
    grade = int(input())
    if grade <= 4:
        failed += 1
        if failed == max_grade_for_fail:
            is_failed = True
            break
    total_grades += grade
    solved_problem += 1
    last_solve = name_of_task
    name_of_task = input()

if is_failed:
    print(f"You need a break, {failed} poor grades.")
else:
    average_score = total_grades / solved_problem
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {solved_problem}")
    print(f"Last problem: {last_solve}")

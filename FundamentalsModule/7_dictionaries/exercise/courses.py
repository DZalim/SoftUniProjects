command = input()

my_courses_dict = {}

while command != "end":
    current_course, current_student = command.split(" : ")
    if current_course not in my_courses_dict.keys():
        my_courses_dict[current_course] = []
    my_courses_dict[current_course].append(current_student)
    command = input()

for course_name, registered_students in my_courses_dict.items():
    print(f"{course_name}: {len(registered_students)}")
    for student in registered_students:
        print(f"-- {student}")

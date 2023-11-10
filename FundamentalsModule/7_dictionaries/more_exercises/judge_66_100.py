command = input()

my_dict_with_username_courses_and_points = {}
my_dict_with_username_points = {}

while command != "no more time":
    name_of_student, current_course, current_points = command.split(" -> ")
    current_points = int(current_points)
    if current_course not in my_dict_with_username_courses_and_points.keys():
        my_dict_with_username_courses_and_points[current_course] = {name_of_student: current_points}
    elif current_course in my_dict_with_username_courses_and_points.keys():
        if name_of_student not in my_dict_with_username_courses_and_points[current_course].keys():
            my_dict_with_username_courses_and_points[current_course][name_of_student] = current_points
        elif name_of_student in my_dict_with_username_courses_and_points[current_course].keys():
            if current_points > my_dict_with_username_courses_and_points[current_course][name_of_student]:
                my_dict_with_username_courses_and_points[current_course][name_of_student] = current_points
    command = input()

sort_nested_dict_by_value = {key: dict(sorted(val.items(), key=lambda ele: ele[1], reverse=True))
       for key, val in my_dict_with_username_courses_and_points.items()}

for course, course_value in sort_nested_dict_by_value.items():
    print(f"{course}: {len(course_value)} participants")
    iteration = 1
    for user, points in course_value.items():
        print(f"{iteration}. {user} <::> {points}")
        iteration += 1

for username in sort_nested_dict_by_value.values():
    for user, points in username.items():
        if user not in my_dict_with_username_points.keys():
            my_dict_with_username_points[user] = 0
        my_dict_with_username_points[user] += points

sorted_username_points = dict(sorted(my_dict_with_username_points.items(), key=lambda x: x[1], reverse=True))

print("Individual standings:")

iteration = 1
for username, total_points in sorted_username_points.items():
    print(f"{iteration}. {username} -> {total_points}")
    iteration += 1

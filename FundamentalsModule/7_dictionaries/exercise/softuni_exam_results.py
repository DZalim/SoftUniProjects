command = input()

my_course_dict = {}
username_points_dict = {}

while command != "exam finished":
    if "banned" in command:
        username, action = command.split("-")
        del username_points_dict[username]
    else:
        username, language, points = command.split("-")
        points = int(points)
        if language not in my_course_dict.keys():
            my_course_dict[language] = 0
        my_course_dict[language] += 1
        if username not in username_points_dict.keys():
            username_points_dict[username] = 0
        if username_points_dict[username] < points:
            username_points_dict[username] = points
    command = input()

print(f"Results:")
for username, points in username_points_dict.items():
    print(f"{username} | {points}")
print(f"Submissions:")
for language, submissions_count in my_course_dict.items():
    print(f"{language} - {submissions_count}")

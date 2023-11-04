contest = input()

my_dict_with_contests_passwords = {}
my_dict_with_usernames_results = {}

while contest != "end of contests":
    current_contest, password = contest.split(":")
    my_dict_with_contests_passwords[current_contest] = password
    contest = input()

submissions = input()
while submissions != "end of submissions":
    submission_contest, submission_password, username, points = submissions.split("=>")
    points = int(points)
    if submission_contest in my_dict_with_contests_passwords.keys() and my_dict_with_contests_passwords[submission_contest] == submission_password:
        if username not in my_dict_with_usernames_results.keys():
            my_dict_with_usernames_results[username] = {submission_contest: points}
        else:
            for username_key, username_value in my_dict_with_usernames_results.items():
                if username_key == username:
                    if submission_contest not in username_value.keys():
                        my_dict_with_usernames_results[username][submission_contest] = points
                    else:
                        if my_dict_with_usernames_results[username][submission_contest] < points:
                            my_dict_with_usernames_results[username][submission_contest] = points
    submissions = input()

max_points = 0
username_max_value = ""
for username, value in my_dict_with_usernames_results.items():
    if sum(value.values()) > max_points:
        max_points = sum(value.values())
        username_max_value = username
print(f"Best candidate is {username_max_value} with total {max_points} points.")

sorted_dictionary_by_name = dict(sorted(my_dict_with_usernames_results.items()))

print(f"Ranking:")
for key, value in sorted_dictionary_by_name.items():
    print(key)
    sorted_value = dict(sorted(value.items(), key=lambda x: x[1], reverse=True))
    for key2, value2 in sorted_value.items():
        print(f"#  {key2} -> {value2}")

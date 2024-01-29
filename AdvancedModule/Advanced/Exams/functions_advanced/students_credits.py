def students_credits(*args):
    courses_credits = {}

    args = [list_item.split('-') for list_item in args]

    for course_name, credits, max_test_points, my_points in args:
        course_credits = int(credits) * (int(my_points) / int(max_test_points))
        courses_credits[course_name] = course_credits

    if sum(courses_credits.values()) >= 240:
        result = f"Diyan gets a diploma with {sum(courses_credits.values()):.1f} credits.\n"
    else:
        result = f"Diyan needs {(240 - sum(courses_credits.values())):.1f} credits more for a diploma.\n"

    sorted_dict = sorted(courses_credits.items(), key=lambda x: -x[1])

    for key, value in sorted_dict:
        result += f"{key} - {value:.1f}\n"

    return result


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)

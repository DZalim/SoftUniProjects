def gather_credits(needed_credits, *courses_info):
    enrolled_courses = {}

    for course, credits in courses_info:
        if course not in enrolled_courses:
            enrolled_courses[course] = credits

        if sum(enrolled_courses.values()) >= needed_credits:
            break

    if sum(enrolled_courses.values()) >= needed_credits:
        result = f"Enrollment finished! Maximum credits: {sum(enrolled_courses.values())}.\n"
        result += f"Courses: {', '.join(course for course in sorted(enrolled_courses.keys()))}"
    else:
        result = f"You need to enroll in more courses! You have to gather {needed_credits - sum(enrolled_courses.values())} credits more."

    return result


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

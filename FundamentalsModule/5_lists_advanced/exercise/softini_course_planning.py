sequence_of_courses = [course for course in input().split(", ")]

command = input()
while command != "course start":
    split_command = command.split(":")
    action = split_command[0]
    lesson_title = split_command[1]
    if action == "Add":
        if lesson_title not in sequence_of_courses:
            sequence_of_courses.append(lesson_title)
    elif action == "Insert":
        index_for_insert = int(split_command[2])
        if lesson_title not in sequence_of_courses:
            sequence_of_courses.insert(index_for_insert, lesson_title)
    elif action == "Remove":
        if lesson_title in sequence_of_courses:
            sequence_of_courses.remove(lesson_title)
            if lesson_title+"-"+"Exercise" in sequence_of_courses:
                sequence_of_courses.remove(lesson_title+"-"+"Exercise")
    elif action == "Swap":
        lesson_title_to_swap = split_command[2]
        if lesson_title in sequence_of_courses and lesson_title_to_swap in sequence_of_courses:
            index_lesson_title = sequence_of_courses.index(lesson_title)
            index_lesson_title_to_swap = sequence_of_courses.index(lesson_title_to_swap)
            sequence_of_courses[index_lesson_title], sequence_of_courses[index_lesson_title_to_swap] = \
                sequence_of_courses[index_lesson_title_to_swap], sequence_of_courses[index_lesson_title]
            if lesson_title_to_swap+"-"+"Exercise" in sequence_of_courses:
                sequence_of_courses.remove(lesson_title_to_swap+"-"+"Exercise")
                sequence_of_courses.insert(index_lesson_title+1, lesson_title_to_swap+"-"+"Exercise")
            elif lesson_title + "-" + "Exercise" in sequence_of_courses:
                sequence_of_courses.remove(lesson_title + "-" + "Exercise")
                sequence_of_courses.insert(index_lesson_title_to_swap + 1, lesson_title + "-" + "Exercise")
    elif action == "Exercise":
        if lesson_title in sequence_of_courses and lesson_title+"-"+"Exercise" not in sequence_of_courses:
            lecture_index = sequence_of_courses.index(lesson_title)
            sequence_of_courses.insert(lecture_index+1, lesson_title+"-"+"Exercise")
        elif lesson_title not in sequence_of_courses:
            sequence_of_courses.append(lesson_title)
            sequence_of_courses.append(lesson_title + "-" + "Exercise")

    command = input()

for number in range(1, len(sequence_of_courses) + 1):
    print(f"{number}.{sequence_of_courses[number-1]}")

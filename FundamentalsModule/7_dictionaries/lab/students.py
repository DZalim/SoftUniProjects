data = input()

my_dict = {}

while ":" in data:
    student_name, student_id, course_name = data.split(":")
    if course_name not in my_dict:
        my_dict[course_name] = {student_id:student_name}
    else:
        my_dict[course_name][student_id] = student_name
    data = input()

data = data.replace("_", " ")

for course, value in my_dict.items():
    if course == data:
        for student_id, student_name in value.items():
            print(f"{student_name} - {student_id}")

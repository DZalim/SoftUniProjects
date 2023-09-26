first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

total_hours = students_count // (first_employee + second_employee + third_employee)
left_students_last_hour = students_count % (first_employee + second_employee + third_employee)

if left_students_last_hour == 0:
    time = total_hours
else:
    time = total_hours + 1
if time > 3:
    time += time//3

print(f"Time needed: {time}h.")

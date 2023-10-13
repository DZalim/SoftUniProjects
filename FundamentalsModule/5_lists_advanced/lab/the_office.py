# hapiness_employees = [int(employee) for employee in input().split()]
# hapiness_factor = int(input())
#
# list_of_score = [int(score) * hapiness_factor for score in hapiness_employees]
# happy_peoples = [int(happy) for happy in list_of_score if int(happy) >= sum(list_of_score) / len(list_of_score)]
#
# print(f"Score: {len(happy_peoples)}/{len(hapiness_employees)}. Employees are happy!" if len(happy_peoples) >= len(
#     hapiness_employees) // 2 else f"Score: {len(happy_peoples)}/{len(hapiness_employees)}. Employees are not happy!")


hapiness_employees = input().split()
hapiness_factor = int(input())

employees = list(map(lambda x: int(x) * hapiness_factor, hapiness_employees))

filtered_employees = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))

if len(filtered_employees) >= len(employees) / 2:
    print(f"Score: {len(filtered_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_employees)}/{len(employees)}. Employees are not happy!")

command = input()

my_dict_with_company_users = {}

while command != "End":
    company_name, user_id = command.split(" -> ")
    if company_name not in my_dict_with_company_users.keys():
        my_dict_with_company_users[company_name] = []
    if user_id not in my_dict_with_company_users[company_name]:
        my_dict_with_company_users[company_name].append(user_id)
    command = input()

for company_name, employee_id in my_dict_with_company_users.items():
    print(company_name)
    for employee in employee_id:
        print(f"-- {employee}")

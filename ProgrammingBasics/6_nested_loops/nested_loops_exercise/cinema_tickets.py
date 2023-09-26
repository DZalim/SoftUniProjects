standard = 0
student = 0
kid = 0

name_of_film = input()
while name_of_film != "Finish":
    free_seats = int(input())
    sold_seats = 0
    for seats in range(free_seats):
        type_of_ticket = input()
        if type_of_ticket == "End":
            break
        elif type_of_ticket == "student":
            student += 1
        elif type_of_ticket == "standard":
            standard += 1
        elif type_of_ticket == "kid":
            kid += 1
        sold_seats += 1
    total_filled_capacity = sold_seats / free_seats * 100
    print(f"{name_of_film} - {total_filled_capacity:.2f}% full.")
    name_of_film = input()

total_ticket = standard + student + kid
percent_student = student / total_ticket * 100
percent_standard = standard / total_ticket * 100
percent_kid = kid / total_ticket * 100

print(f"Total tickets: {total_ticket}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")


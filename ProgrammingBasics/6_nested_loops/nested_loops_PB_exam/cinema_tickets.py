name_of_film = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while name_of_film != "Finish":
    free_seats = int(input())
    sold_seats = 0
    for ticket in range (free_seats):
        type_of_ticket = input()
        if type_of_ticket == "End":
            break
        elif type_of_ticket == "student":
            student_tickets += 1
        elif type_of_ticket == "standard":
            standard_tickets += 1
        elif type_of_ticket == "kid":
            kid_tickets += 1
        sold_seats += 1
    percent_sold_tickets = sold_seats / free_seats * 100
    print(f"{name_of_film} - {percent_sold_tickets:.2f}% full.")
    name_of_film = input()

total_tickets = student_tickets + standard_tickets + kid_tickets
student_tickets_percent = student_tickets / total_tickets * 100
standard_tickets_percent = standard_tickets / total_tickets * 100
kid_tickets_percent = kid_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_percent:.2f}% student tickets.")
print(f"{standard_tickets_percent:.2f}% standard tickets.")
print(f"{kid_tickets_percent:.2f}% kids tickets.")

name_of_the_film = input()
type_of_the_room = input()
number_of_the_tickets = int(input())

price_per_ticket = 0

if name_of_the_film == "A Star Is Born":
    if type_of_the_room == "normal":
        price_per_ticket = 7.50
    elif type_of_the_room == "luxury":
        price_per_ticket = 10.50
    elif type_of_the_room == "ultra luxury":
        price_per_ticket = 13.50
elif name_of_the_film == "Bohemian Rhapsody":
    if type_of_the_room == "normal":
        price_per_ticket = 7.35
    elif type_of_the_room == "luxury":
        price_per_ticket = 9.45
    elif type_of_the_room == "ultra luxury":
        price_per_ticket = 12.75
elif name_of_the_film == "Green Book":
    if type_of_the_room == "normal":
        price_per_ticket = 8.15
    elif type_of_the_room == "luxury":
        price_per_ticket = 10.25
    elif type_of_the_room == "ultra luxury":
        price_per_ticket = 13.25
elif name_of_the_film == "The Favourite":
    if type_of_the_room == "normal":
        price_per_ticket = 8.75
    elif type_of_the_room == "luxury":
        price_per_ticket = 11.55
    elif type_of_the_room == "ultra luxury":
        price_per_ticket = 13.95

revenue = number_of_the_tickets * price_per_ticket

print(f"{name_of_the_film} -> {revenue:.2f} lv.")
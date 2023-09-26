name_of_the_film = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_for_ticket = float(input())
percent_for_the_cinema = int(input())

revenue = number_of_days * number_of_tickets * price_for_ticket
net_revenue = f"{revenue - (revenue * (percent_for_the_cinema / 100)):.2f}"

print(f"The profit from the movie {name_of_the_film} is {net_revenue} lv.")
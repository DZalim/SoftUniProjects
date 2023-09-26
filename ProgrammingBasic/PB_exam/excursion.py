number_of_people_in_group = int(input())
number_of_overnights = int(input())
number_of_transport_card = int(input())
number_of_museum_tickets = int(input())

price_for_overnights = number_of_overnights * 20
price_for_transport_card = number_of_transport_card * 1.60
price_for_museum_tickets = number_of_museum_tickets * 6

price_for_group = (price_for_overnights + price_for_transport_card + price_for_museum_tickets) * number_of_people_in_group
total_price = price_for_group * 1.25

print(f"{total_price:.2f}")
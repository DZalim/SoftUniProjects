name_of_airline = input()
number_of_tickets_for_adults = int(input())
number_of_tickets_for_children = int(input())
net_price_for_ticket_of_adult = float(input())
service_fee = float(input())

net_price_for_ticket_of_children = net_price_for_ticket_of_adult * 0.30
price_for_ticket_of_children = net_price_for_ticket_of_children + service_fee
price_for_ticket_of_adults = net_price_for_ticket_of_adult + service_fee

revenue = number_of_tickets_for_children * price_for_ticket_of_children \
          + number_of_tickets_for_adults * price_for_ticket_of_adults

profit = (f"{revenue * 0.20:.2f}")

print(f"The profit of your agency from {name_of_airline} tickets is {profit} lv.")
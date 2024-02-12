from collections import deque

customers = deque([int(customer) for customer in input().split(', ')]) #queue
taxis = [int(taxi) for taxi in input().split(', ')]  #stack

total_time = 0

while customers and taxis:
    current_customer = customers[0]
    current_taxi = taxis.pop()

    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft()

if not customers:
    print(f"All customers were driven to their destinations\n"
          f"Total time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations\n"
          f"Customers left: {', '.join(str(customer) for customer in customers)}")

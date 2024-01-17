from collections import deque

pizza_orders = deque(int(x) for x in input().split(', '))  #queue
employees_capacity = [int(x) for x in input().split(', ')]  #stack

made_pizza = 0

while pizza_orders and employees_capacity:
    current_pizza = pizza_orders.popleft()

    if current_pizza <= 0 or current_pizza > 10:
        continue

    current_employee = employees_capacity.pop()

    if current_pizza <= current_employee:
        made_pizza += current_pizza
    else:
        made_pizza += current_employee
        remaining_pizza = current_pizza - current_employee
        pizza_orders.appendleft(remaining_pizza)

if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {made_pizza}')
    if employees_capacity:
        print(f"Employees: {', '. join(str(x) for x in employees_capacity)}")

if not employees_capacity:
    print('Not all orders are completed.')
    if pizza_orders:
        print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")

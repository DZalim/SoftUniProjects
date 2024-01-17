from collections import deque

bowls_of_ramen = [int(x) for x in input().split(', ')] #stack
customers = deque(int(x) for x in input().split(', ')) # queue

while bowls_of_ramen and customers:
    last_bowl = bowls_of_ramen.pop()
    first_customer = customers.popleft()

    if last_bowl > first_customer:
        bowls_of_ramen.append(last_bowl - first_customer)
    elif last_bowl < first_customer:
        customers.appendleft(first_customer - last_bowl)

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")

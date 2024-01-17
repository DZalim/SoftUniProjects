from collections import deque

initial_fuel = deque(int(fuel) for fuel in input().split())  # stack
additional_consumption_index = deque(int(consumption) for consumption in input().split())  # queue
needed_fuel = deque(int(fuel) for fuel in input().split())  # queue

reached_altitude = []
index = 1
john_failed = False

while initial_fuel and additional_consumption_index:
    current_initial_fuel = initial_fuel.pop()
    current_consumption = additional_consumption_index.popleft()
    current_needed_fuel = needed_fuel.popleft()

    result = current_initial_fuel - current_consumption

    current_altitude = 'Altitude' + ' ' + str(index)

    if result >= current_needed_fuel:
        reached_altitude.append(current_altitude)
        print(f"John has reached: {current_altitude}")
        index += 1
    else:
        print(f"John did not reach: {current_altitude}")
        john_failed = True
        break

if reached_altitude and john_failed:
    print("John failed to reach the top.")
    print(f"Reached altitudes:", end=' ')
    print(*reached_altitude, sep=', ')
elif not reached_altitude and john_failed:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")

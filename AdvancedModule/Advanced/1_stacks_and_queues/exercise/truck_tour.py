from collections import deque

pumps_information = deque([[int(data) for data in input().split()] for _ in range(int(input()))])

pumps_information_copy = pumps_information.copy()
petrol_in_tank = 0
index = 0

while pumps_information_copy:
    needed_petrol, distance = pumps_information_copy.popleft()
    petrol_in_tank += needed_petrol

    if petrol_in_tank >= distance:
        petrol_in_tank -= distance
    else:
        pumps_information.rotate(-1)
        pumps_information_copy = pumps_information.copy()
        index += 1
        petrol_in_tank = 0

print(index)

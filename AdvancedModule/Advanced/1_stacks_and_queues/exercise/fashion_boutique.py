from collections import deque

box_of_clothes = deque([int(box) for box in input().split()]) #stack
rack_capacity = int(input())

total_racks = 1
current_capacity = rack_capacity

while box_of_clothes:
    current_box_of_clothes = box_of_clothes.pop()
    if current_box_of_clothes <= current_capacity:
        current_capacity -= current_box_of_clothes
    else:
        total_racks += 1
        current_capacity = rack_capacity - current_box_of_clothes

print(total_racks)

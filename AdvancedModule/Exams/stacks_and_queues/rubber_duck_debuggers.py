from collections import deque

time_for_single_task = deque(int(task_time) for task_time in input().split())  # queue
number_of_tasks = deque(int(task) for task in input().split())  # stack

rubber_ducks = {'Darth Vader Ducky': 0, 'Thor Ducky': 0, 'Big Blue Rubber Ducky': 0, 'Small Yellow Rubber Ducky': 0}

while time_for_single_task and number_of_tasks:
    current_time = time_for_single_task.popleft()
    current_task = number_of_tasks.pop()

    calculated_time = current_task * current_time

    if 0 < calculated_time <= 60:
        rubber_ducks['Darth Vader Ducky'] += 1
    elif 60 < calculated_time <= 120:
        rubber_ducks['Thor Ducky'] += 1
    elif 120 < calculated_time <= 180:
        rubber_ducks['Big Blue Rubber Ducky'] += 1
    elif 180 < calculated_time <= 240:
        rubber_ducks['Small Yellow Rubber Ducky'] += 1
    else:
        decreased_number_of_task = current_task - 2
        number_of_tasks.append(decreased_number_of_task)
        time_for_single_task.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, count in rubber_ducks.items():
    print(f'{duck}: {count}')

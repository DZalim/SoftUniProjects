number_of_rooms = int(input())

total_free_chairs = 0

for room in range(1, number_of_rooms+1):
    command = input().split()
    free_chairs = command[0]
    visitors = int(command[1])
    difference = len(free_chairs) - visitors
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {room}")
    total_free_chairs += difference

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")

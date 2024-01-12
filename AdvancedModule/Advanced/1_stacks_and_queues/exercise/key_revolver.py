from collections import deque

bullet_price = int(input())
size_of_the_gun_barrel = int(input())
bullets = deque([int(bullet) for bullet in input().split()])  # stack
locks = deque([int(lock) for lock in input().split()])  # queue
intelligence_value = int(input())

removed_bullets = 0
current_barrel = 0

while locks and bullets:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    if current_bullet <= current_lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(current_lock)

    removed_bullets += 1
    current_barrel += 1
    if current_barrel == size_of_the_gun_barrel and len(bullets) > 0:
        print('Reloading!')
        current_barrel = 0

bullets_cost = bullet_price * removed_bullets
earned_money = intelligence_value - bullets_cost

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")

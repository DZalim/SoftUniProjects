from collections import deque

males = [int(x) for x in input().split()]  #stack
females = deque(int(x) for x in input().split())  #queue

matches = 0

while males and females:

    last_male = males[-1]
    first_female = females[0]

    if last_male <= 0:
        males.pop()
        continue
    elif first_female <= 0:
        females.popleft()
        continue

    males.pop()
    females.popleft()

    if last_male % 25 == 0 or first_female % 25 == 0:
        if last_male % 25 == 0:
            males.pop() if males else None
            females.appendleft(first_female)
        elif first_female % 25 == 0:
            females.popleft() if females else None
            males.append(last_male)
        continue

    if last_male == first_female:
        matches += 1
    else:
        males.append(last_male - 2)

print(f"Matches: {matches}")
print(f"Males left: {', '.join(str(x) for x in reversed(males)) or 'none'}")
print(f"Females left: {', '.join(str(x) for x in females) or 'none'}")

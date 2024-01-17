from collections import deque

wedding_present = [int(x) for x in input().split()] #stack
magic_level = deque(int(x) for x in input().split()) #queue

crafted_present = {'Diamond Jewellery': 0,
                   'Gemstone': 0,
                   'Gold': 0,
                   'Porcelain Sculpture': 0,
                   }

while wedding_present and magic_level:
    last_present = wedding_present.pop()
    first_level = magic_level.popleft()

    result = last_present + first_level

    if result < 100:
        if result % 2 == 0:
            last_present *= 2
            first_level *= 3
            result = last_present + first_level
        else:
            result *= 2
    elif result > 499:
        result /= 2

    if 100 <= result < 200:
        crafted_present['Gemstone'] += 1
    elif 200 <= result < 300:
        crafted_present['Porcelain Sculpture'] += 1
    elif 300 <= result < 400:
        crafted_present['Gold'] += 1
    elif 400 <= result < 500:
        crafted_present['Diamond Jewellery'] += 1

if crafted_present['Gemstone'] > 0 and crafted_present['Porcelain Sculpture'] > 0 or \
crafted_present['Gold'] > 0 and crafted_present['Diamond Jewellery']:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if wedding_present:
    print(f"Materials left: {', '.join(str(x) for x in wedding_present)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for key, value in crafted_present.items():
    if value > 0:
        print(f"{key}: {value}")

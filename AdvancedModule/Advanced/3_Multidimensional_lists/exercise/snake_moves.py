from collections import deque

n, m = [int(x) for x in input().split()]
text = list(input())

current_text = deque(text)

for print_count in range(n):
    while len(current_text) < m:
        current_text.extend(text)

    if print_count % 2 == 0:
        print(*[current_text.popleft() for letter in range(m)], sep='')
    else:
        print(*[current_text.popleft() for letter in range(m)][::-1], sep='')

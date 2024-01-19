from collections import deque
from math import floor

string_expression = deque(input().split())

queue = deque()

while string_expression:
    current_symbol = string_expression.popleft()
    if current_symbol not in '+-*/':
        queue.append(int(current_symbol))
    else:
        while len(queue) > 1:
            result = eval(f'{queue.popleft()} {current_symbol} {queue.popleft()}')
            queue.appendleft(floor(result))

print(*queue)

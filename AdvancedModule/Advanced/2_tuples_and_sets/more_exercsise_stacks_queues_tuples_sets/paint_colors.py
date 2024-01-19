from collections import deque

words = deque(input().split())

colors = {'red', 'yellow', 'blue', 'orange', 'purple', 'green'}
secondary_color = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'blue', 'yellow'}
}

found_words = []

while words:
    first_side = words.popleft()
    last_side = words.pop() if words else ""

    for word in (first_side + last_side, last_side + first_side):
        if word in colors:
            found_words.append(word)
            break
    else:
        first_side = first_side[0:-1]
        last_side = last_side[0:-1]
        index_to_insert = len(words) // 2
        words.insert(index_to_insert, first_side) if first_side else None
        words.insert(index_to_insert, last_side) if last_side else None

for found_word in found_words:
    if found_word in secondary_color.keys() and not secondary_color[found_word].issubset(found_words):
        found_words.remove(found_word)

print(found_words)

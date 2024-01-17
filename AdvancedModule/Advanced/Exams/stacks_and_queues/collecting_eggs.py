from collections import deque

eggs_size = deque([int(x) for x in input().split(', ')]) #queue
papers_size = [int(x) for x in input().split(', ')] #stack

boxes = 0

while eggs_size and papers_size:
    first_egg = eggs_size.popleft()
    if first_egg <= 0 or first_egg == 13:
        if first_egg == 13:
            papers_size[0], papers_size[-1] = papers_size[-1], papers_size[0]
        continue

    paper_size = papers_size.pop()

    result = first_egg + paper_size

    if result <= 50:
        boxes += 1

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f"Eggs left: {', '.join([str(x) for x in eggs_size])}")
if papers_size:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers_size])}")

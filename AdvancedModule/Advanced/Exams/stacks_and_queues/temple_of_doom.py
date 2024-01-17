from collections import deque

tools = deque(int(tool) for tool in input().split())  # queue
substances = deque(int(substance) for substance in input().split())  # stack
challenges = [int(challenge) for challenge in input().split()]

while True:
    first_tool = tools.popleft()
    last_substance = substances.pop()

    result = first_tool * last_substance

    if result in challenges:
        challenges.remove(result)
    else:
        tool_to_add_end = first_tool + 1
        tools.append(tool_to_add_end)
        substance_to_add_end = last_substance - 1
        if substance_to_add_end > 0:
            substances.append(substance_to_add_end)

    if (not tools or not substances) and challenges:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break
    elif not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

if tools:
    print(f"Tools:", end=" ")
    print(*tools, sep=', ')
if substances:
    print(f"Substances:", end=" ")
    print(*substances, sep=', ')
if challenges:
    print(f"Challenges:", end=" ")
    print(*challenges, sep=', ')

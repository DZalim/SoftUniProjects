first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [first_sequence.add(y) for y in x],
    "Add Second": lambda x: [second_sequence.add(y) for y in x],
    "Remove First": lambda x: [first_sequence.discard(y) for y in x],
    "Remove Second": lambda x: [second_sequence.discard(y) for y in x],
    "Check Subset": lambda x: print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence)),
}


for _ in range(int(input())):
    com_1, com_2, *data = input().split()
    command = com_1 + " " + com_2
    data = [int(x) for x in data]
    functions[command](data)

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')

numbers = []

commands = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None,
}

for _ in range(int(input())):
    data = [int(command) for command in input().split()]
    command = data[0]
    commands[command](data)

numbers.reverse()
print(*numbers, sep=', ')

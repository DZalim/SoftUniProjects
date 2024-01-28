from functools import reduce


def operate(operator, *args):
    commands = {
        '+': reduce(lambda x, y: x + y, args),
        '-': reduce(lambda x, y: x - y, args),
        '*': reduce(lambda x, y: x * y, args),
        '/': reduce(lambda x, y: x / y, args),
    }

    return commands[operator]


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

from math import log

number = int(input())

try:
    second = int(input())
    print(f'{log(number, second):.2f}')
except ValueError:
    print(f'{log(number):.2f}')

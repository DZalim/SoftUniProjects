from math import floor

from actions import execute_expression


# def truncate(f, n):
#     return floor(f * 10 ** n) / 10 ** n


expression = input()

result = execute_expression(expression)
# print(f"{truncate(result, 2)}")
print(f"{result:.2f}")

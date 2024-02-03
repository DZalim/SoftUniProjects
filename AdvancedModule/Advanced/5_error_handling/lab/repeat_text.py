text_ro_repeat = input()

try:
    times_to_repeat = int(input())
    print(text_ro_repeat*times_to_repeat)
except ValueError:
    print('Variable times must be an integer')

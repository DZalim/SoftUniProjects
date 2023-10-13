current_string = input()
number_of_repeat = int(input())

repeat_string = lambda string, number: string * number
result = repeat_string(current_string, number_of_repeat)

print(result)
